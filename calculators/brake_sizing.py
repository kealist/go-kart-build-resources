#!/usr/bin/env python3
"""
Brake sizing sanity check for a go-kart.

Computes kinetic energy, required brake torque and clamp force for a target
deceleration, the traction-limited deceleration for REAR-ONLY brakes (most
karts), pedal force for a hydraulic system, and stopping distance.

Examples:
    python3 brake_sizing.py                           # 450 lb, 30 mph, 0.5 g target
    python3 brake_sizing.py --weight 480 --mph 35 --rotor 8
    python3 brake_sizing.py --mechanical              # cable disc; skip hydraulic math

Key formulas:
    KE = 1/2 m v^2
    brake force F = W * decel_g          (at the tire contact patch)
    brake torque T = F * r_tire          (total, split across rotors)
    rotor torque = 2 * mu_pad * F_clamp * r_eff   (two pad faces)
    rear-only traction limit:  decel_g_max = mu * (rear_frac - decel_g*h/L)  -> solve
"""
import argparse

G = 32.174


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--weight", type=float, default=450.0, help="total weight incl. driver, lb (default 450)")
    p.add_argument("--mph", type=float, default=30.0, help="speed to stop from (default 30)")
    p.add_argument("--decel", type=float, default=0.5, help="target deceleration, g (default 0.5)")
    p.add_argument("--tire", type=float, default=20.0, help="rear tire diameter, in (default 20)")
    p.add_argument("--rotor", type=float, default=7.1, help="rotor diameter, in (common 6, 7.1, 8)")
    p.add_argument("--pad-height", type=float, default=1.0, help="radial pad height, in (default 1.0)")
    p.add_argument("--mu-pad", type=float, default=0.38, help="pad-rotor friction (0.3-0.45)")
    p.add_argument("--rotors", type=int, default=1, help="number of braked rotors (default 1, live axle)")
    p.add_argument("--mu-tire", type=float, default=0.7, help="tire-ground friction (0.5 dirt, 0.7-0.9 pavement)")
    p.add_argument("--rear-fraction", type=float, default=0.60, help="static weight fraction on rear (default 0.60)")
    p.add_argument("--cg-height", type=float, default=11.0, help="CG height above ground, in (default 11)")
    p.add_argument("--wheelbase", type=float, default=44.0, help="wheelbase, in (default 44)")
    p.add_argument("--front-brakes", action="store_true", help="brakes on all four wheels (no traction penalty)")
    p.add_argument("--mechanical", action="store_true", help="skip hydraulic pedal-force calc")
    p.add_argument("--master-bore", type=float, default=0.625, help="master cylinder bore, in (default 5/8)")
    p.add_argument("--caliper-bore", type=float, default=1.25, help="caliper piston bore, in (default 1.25)")
    p.add_argument("--caliper-pistons", type=int, default=1, help="pistons per side pushing the pad (default 1)")
    p.add_argument("--pedal-ratio", type=float, default=5.0, help="pedal lever ratio (default 5:1)")
    a = p.parse_args()

    v = a.mph * 5280 / 3600  # ft/s
    m = a.weight / G
    ke = 0.5 * m * v ** 2
    r_tire = a.tire / 2 / 12

    print(f"Vehicle {a.weight:.0f} lb at {a.mph:.0f} mph: kinetic energy {ke:,.0f} ft-lb ({ke*1.3558:,.0f} J)")
    print()

    # Traction-limited decel for rear-only brakes, including weight transfer
    # N_rear = W*(rear_frac) - W*decel*h/L ; F = mu*N_rear = W*decel  => decel = mu*rf/(1+mu*h/L)
    if a.front_brakes:
        decel_limit = a.mu_tire
        print(f"4-wheel brakes: traction-limited decel ~{decel_limit:.2f} g")
    else:
        decel_limit = a.mu_tire * a.rear_fraction / (1 + a.mu_tire * a.cg_height / a.wheelbase)
        print(f"REAR-ONLY brakes, mu={a.mu_tire}, rear static {a.rear_fraction:.0%}, CG {a.cg_height:.0f} in, WB {a.wheelbase:.0f} in:")
        print(f"  traction-limited decel = {decel_limit:.2f} g  <- rear wheels lock beyond this, more brake won't help")
    decel = a.decel
    if decel > decel_limit:
        print(f"  NOTE: target {decel:.2f} g exceeds traction limit; using {decel_limit:.2f} g for sizing.")
        decel = decel_limit

    f_brake = a.weight * decel
    t_total = f_brake * r_tire  # ft-lb
    t_per_rotor = t_total / a.rotors
    d_stop = v ** 2 / (2 * decel * G)
    t_stop = v / (decel * G)
    print()
    print(f"Target decel {decel:.2f} g -> brake force at tires {f_brake:.0f} lb, axle torque {t_total:.0f} ft-lb")
    print(f"Stopping distance {d_stop:.0f} ft in {t_stop:.1f} s (plus reaction time; add ~{v*0.75:.0f} ft at 0.75 s)")

    r_eff = (a.rotor / 2 - a.pad_height / 2) / 12  # ft
    f_clamp = t_per_rotor / (2 * a.mu_pad * r_eff)
    print()
    print(f"Rotor {a.rotor:.1f} in (effective radius {r_eff*12:.2f} in), pad mu {a.mu_pad}, {a.rotors} rotor(s):")
    print(f"  required clamp force per rotor: {f_clamp:.0f} lb")
    energy_per_rotor = ke / a.rotors
    print(f"  energy per rotor per stop: {energy_per_rotor:,.0f} ft-lb  (repeated stops heat-soak small rotors; 6 in rotors get hot fast at this weight)")

    if not a.mechanical:
        import math
        a_m = math.pi * (a.master_bore / 2) ** 2
        a_c = math.pi * (a.caliper_bore / 2) ** 2 * a.caliper_pistons
        pressure = f_clamp / a_c
        f_rod = pressure * a_m
        f_pedal = f_rod / a.pedal_ratio
        print()
        print(f"Hydraulic: master {a.master_bore} in bore ({a_m:.3f} in^2), caliper {a.caliper_bore} in x{a.caliper_pistons} ({a_c:.3f} in^2)")
        print(f"  line pressure {pressure:.0f} psi, pushrod force {f_rod:.0f} lb, pedal force at {a.pedal_ratio}:1 = {f_pedal:.0f} lb")
        if f_pedal > 80:
            print("  WARNING: >80 lb pedal effort is tiring. Increase pedal ratio, smaller master bore, bigger caliper/rotor, or add a rotor.")
        elif f_pedal < 25:
            print("  Note: very light pedal; fine, but check that total pedal travel is not excessive (fluid volume).")
    else:
        print()
        print("Mechanical disc: cable-pull calipers typically deliver a few hundred lb of clamp force at best.")
        print(f"  Compare that to the {f_clamp:.0f} lb needed. If short, go hydraulic or add a second rotor.")

    print()
    print("Rule of thumb for a 400-500 lb kart: hydraulic disc, 7-8 in rotor on the live axle, or dual calipers.")
    print("Band brakes and scrub brakes are not adequate at this weight.")


if __name__ == "__main__":
    main()
