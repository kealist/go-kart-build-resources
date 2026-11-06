#!/usr/bin/env python3
"""
Chain tension check for the engine/TC -> axle chain.

Chain tension = torque at the driving sprocket / pitch radius of that sprocket.
Torque at the driving sprocket = engine torque x torque-converter low ratio
(worst case, launching), x efficiency.

Examples:
    python3 chain_check.py                     # 420cc, 40-series TC, 10T #40
    python3 chain_check.py --torque 8.1 --tc-low 2.7 --teeth 10 --chain 35
    python3 chain_check.py --chain 420 --teeth 12

Approximate ANSI/ISO minimum tensile strengths (single strand, lb):
    #35 ~2,100   #40 ~3,700   #41 ~2,000   #420 ~3,500   #428 ~4,000   #50 ~6,100
Industrial practice uses a working load of roughly 1/6 to 1/8 of ultimate for
continuous duty.  Karts are intermittent, shock-loaded and poorly aligned, so a
ratio of ultimate/tension >= 5 is a reasonable target; >= 3 is "it will work
but inspect often".  Chain load is capped by tire traction: once the rear
wheels spin, the chain cannot see more torque, so heavier karts with grippy
tires load the chain harder.
"""
import argparse
import math

CHAINS = {
    "35":  {"pitch": 0.375, "tensile": 2100, "note": "light; fine for 212cc with light driver"},
    "40":  {"pitch": 0.500, "tensile": 3700, "note": "common choice for 420cc karts"},
    "41":  {"pitch": 0.500, "tensile": 2000, "note": "narrow #40; same pitch, weaker; fits many kart sprockets"},
    "420": {"pitch": 0.500, "tensile": 3500, "note": "motorcycle chain, same pitch as #40/#41, popular on karts"},
    "428": {"pitch": 0.500, "tensile": 4000, "note": "wider motorcycle chain"},
    "50":  {"pitch": 0.625, "tensile": 6100, "note": "overkill; heavy"},
}


def pitch_diameter(pitch, teeth):
    return pitch / math.sin(math.pi / teeth)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--torque", type=float, default=18.4, help="engine torque, ft-lb (420cc ~18.4, 212cc ~8.1)")
    p.add_argument("--tc-low", type=float, default=3.5, help="TC low ratio (30 series ~2.7, 40 series ~3.5; 1.0 for clutch)")
    p.add_argument("--teeth", type=int, default=10, help="teeth on driving (TC output) sprocket")
    p.add_argument("--chain", default="40", choices=CHAINS.keys())
    p.add_argument("--axle-teeth", type=int, default=60, help="teeth on axle sprocket (for traction cap)")
    p.add_argument("--weight", type=float, default=450.0, help="total weight incl. driver, lb")
    p.add_argument("--rear-fraction", type=float, default=0.60, help="weight fraction on rear axle")
    p.add_argument("--mu", type=float, default=0.7, help="tire-ground friction (traction cap)")
    p.add_argument("--tire", type=float, default=20.0, help="tire diameter, in")
    p.add_argument("--efficiency", type=float, default=0.9)
    p.add_argument("--shock", type=float, default=1.5, help="shock factor for clutch grab / wheel hop (default 1.5)")
    a = p.parse_args()

    c = CHAINS[a.chain]
    t_engine = a.torque * a.tc_low * a.efficiency * 12  # in-lb at driving sprocket
    # The tires can only transmit so much torque; beyond that they spin and the chain sees no more load.
    t_traction = a.mu * a.weight * a.rear_fraction * a.tire / 2 / (a.axle_teeth / a.teeth)
    t_sprocket = min(t_engine, t_traction)
    print(f"Torque at driving sprocket: engine path {t_engine:,.0f} in-lb, traction cap {t_traction:,.0f} in-lb -> using {t_sprocket:,.0f}")
    pd = pitch_diameter(c["pitch"], a.teeth)
    tension = t_sprocket / (pd / 2) * a.shock
    ratio = c["tensile"] / tension

    print(f"#{a.chain} chain, {a.teeth}T driver: pitch dia {pd:.3f} in -> tension {tension:,.0f} lb (incl. x{a.shock} shock)")
    print(f"Chain min tensile ~{c['tensile']:,} lb -> ratio {ratio:.1f}   ({c['note']})")
    if ratio >= 5:
        print("Verdict: comfortable.")
    elif ratio >= 3:
        print("Verdict: workable; keep it aligned, tensioned, lubed; inspect for stretch often.")
    else:
        print("Verdict: undersized. Use a bigger chain or more teeth on the driving sprocket.")
    print()
    print("Compare all chains at this load:")
    for k, v in CHAINS.items():
        pdk = pitch_diameter(v["pitch"], a.teeth)
        tk = t_sprocket / (pdk / 2) * a.shock
        print(f"  #{k:4} tension {tk:5,.0f} lb  ratio {v['tensile']/tk:4.1f}")
    print()
    print("Heavy driver note: more rider weight means more time at TC low ratio and more wheel-hop shock.")
    print("#35 on a 212cc is fine for a 150 lb rider; at 250 lb consider #40/#420 even on a 212.")


if __name__ == "__main__":
    main()
