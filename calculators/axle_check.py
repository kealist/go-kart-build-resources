#!/usr/bin/env python3
"""
Live rear axle check: combined bending + torsion on a solid keyed axle.

Model: axle supported by two bearings; each wheel sits a distance "overhang"
outboard of its bearing (cantilever).  Bending moment at the bearing is the
wheel load times the overhang.  Torsion is the lesser of engine torque x total
ratio and the traction-limited torque.  Von Mises combined stress, with a
keyway stress-concentration factor applied to the allowable.

Examples:
    python3 axle_check.py                          # compare 1.00 and 1.25 in axles
    python3 axle_check.py --overhang 6 --g 3
    python3 axle_check.py --dia 1.0 --torque 8.1 --ratio 16

Formulas (solid round shaft, diameter D):
    S = pi D^3 / 32     sigma_b = M / S
    Zp = pi D^3 / 16    tau = T / Zp
    sigma_vm = sqrt(sigma_b^2 + 3 tau^2)
"""
import argparse
import math

YIELD_1045 = 77000   # psi, cold-drawn 1045 (approx; hot-rolled ~45,000)
KEYWAY_KT = 1.6      # stress concentration at a profiled keyway (approx)


def check(dia, m_inlb, t_inlb):
    s = math.pi * dia ** 3 / 32
    zp = math.pi * dia ** 3 / 16
    sb = m_inlb / s
    tau = t_inlb / zp
    vm = math.sqrt(sb ** 2 + 3 * tau ** 2)
    return sb, tau, vm


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--weight", type=float, default=450.0, help="total weight incl. driver, lb (default 450)")
    p.add_argument("--rear-fraction", type=float, default=0.60, help="weight fraction on rear axle (default 0.60)")
    p.add_argument("--g", type=float, default=3.0, help="vertical shock factor (default 3)")
    p.add_argument("--overhang", type=float, default=4.0, help="wheel centerline to bearing centerline, in (default 4)")
    p.add_argument("--torque", type=float, default=18.4, help="engine torque, ft-lb (420cc ~18.4, 212cc ~8.1)")
    p.add_argument("--ratio", type=float, default=16.2, help="max total ratio engine->axle (TC low x sprockets; 2.7x6=16.2)")
    p.add_argument("--tire", type=float, default=20.0, help="tire diameter, in")
    p.add_argument("--mu", type=float, default=0.7, help="tire-ground friction for traction-limited torque")
    p.add_argument("--yield", dest="yield_psi", type=float, default=YIELD_1045, help="axle yield, psi (default 1045 CD ~77,000)")
    p.add_argument("--kt", type=float, default=KEYWAY_KT, help="keyway stress concentration (default 1.6)")
    p.add_argument("--dia", type=float, action="append", help="axle diameter(s) to check, in (default 1.0 and 1.25)")
    a = p.parse_args()

    dias = a.dia or [1.0, 1.25]
    wheel_load = a.weight * a.rear_fraction / 2 * a.g
    m = wheel_load * a.overhang  # in-lb at bearing
    t_engine = a.torque * a.ratio * 12 * 0.85  # in-lb with drivetrain losses
    t_traction = a.mu * a.weight * a.rear_fraction * a.tire / 2  # in-lb
    t = min(t_engine, t_traction)
    allow = a.yield_psi / a.kt

    print(f"Rear weight {a.weight*a.rear_fraction:.0f} lb, x{a.g:.1f} g -> {wheel_load:.0f} lb per wheel, "
          f"{a.overhang:.1f} in overhang -> bending moment {m:,.0f} in-lb at bearing")
    print(f"Torque: engine path {t_engine:,.0f} in-lb, traction limit {t_traction:,.0f} in-lb -> using {t:,.0f} in-lb")
    print(f"Allowable = yield {a.yield_psi:,.0f} / keyway Kt {a.kt} = {allow:,.0f} psi")
    print()
    print(f"{'dia in':>7} {'bend psi':>10} {'shear psi':>10} {'vonMises':>10} {'FOS':>5}  verdict")
    for d in dias:
        sb, tau, vm = check(d, m, t)
        fos = allow / vm
        verdict = "OK" if fos >= 2 else ("marginal" if fos >= 1.5 else "undersized")
        print(f"{d:7.3f} {sb:10,.0f} {tau:10,.0f} {vm:10,.0f} {fos:5.1f}  {verdict}")

    print()
    print("Notes:")
    print(" - Keep bearings close to the wheels (small overhang). Overhang is the biggest lever on axle stress.")
    print(" - Fatigue matters: a rotating axle sees fully reversed bending every revolution. Aim for FOS >= 2 here.")
    print(" - 1 in axles are standard on 212cc yard karts; for a 250 lb driver off-road, 1.25 in is the")
    print("   comfortable choice and hubs/bearings/sprocket carriers are readily available in both sizes.")


if __name__ == "__main__":
    main()
