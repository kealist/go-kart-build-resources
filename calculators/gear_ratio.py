#!/usr/bin/env python3
"""
Gear ratio / top speed / hill-climb calculator for a small-engine go-kart.

Pure Python, no dependencies.  Defaults are tuned for a ~250 lb driver on a
420cc-class engine with a torque converter, but every number is a flag.

Examples:
    python3 gear_ratio.py                       # defaults (420cc, TC, 60T/10T)
    python3 gear_ratio.py --engine 212 --axle-teeth 72 --tc-teeth 10
    python3 gear_ratio.py --target-mph 30       # suggest axle sprocket sizes
    python3 gear_ratio.py --clutch              # centrifugal clutch (no TC range)

Formulas:
    speed_mph  = rpm / total_ratio * tire_dia_in * pi / 12 * 60 / 5280
    total_ratio = tc_ratio * (axle_teeth / tc_teeth) [* jackshaft ratio]
    tractive_force_lb = engine_torque_ftlb * total_ratio * efficiency / (tire_dia_in/2/12)
"""
import argparse
import math

# Approximate stock specs (governed ~3600 rpm).  Peak torque is quoted at
# ~2500 rpm by Harbor Freight; verify against the current spec sheet.
ENGINES = {
    "212": {"hp": 6.5, "torque_ftlb": 8.1, "rpm_max": 3600, "note": "Predator 212 / Honda GX200 class"},
    "224": {"hp": 7.0, "torque_ftlb": 9.0, "rpm_max": 3600, "note": "Predator 224 (approx)"},
    "301": {"hp": 8.0, "torque_ftlb": 12.0, "rpm_max": 3600, "note": "Predator 301 (approx)"},
    "420": {"hp": 13.0, "torque_ftlb": 18.4, "rpm_max": 3600, "note": "Predator 420 / Honda GX390 class"},
    "670": {"hp": 22.0, "torque_ftlb": 32.0, "rpm_max": 3600, "note": "Predator 670 V-twin (approx) - overkill"},
}


def speed_mph(rpm, total_ratio, tire_dia_in):
    return rpm / total_ratio * tire_dia_in * math.pi / 12 * 60 / 5280


def tractive_force_lb(torque_ftlb, total_ratio, tire_dia_in, efficiency):
    return torque_ftlb * total_ratio * efficiency / (tire_dia_in / 2 / 12)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--engine", default="420", choices=ENGINES.keys(), help="engine class (default 420)")
    p.add_argument("--torque", type=float, help="override engine peak torque, ft-lb")
    p.add_argument("--rpm", type=int, help="override max engine rpm (stock governor ~3600)")
    p.add_argument("--tire", type=float, default=20.0, help="rear tire diameter, inches (default 20)")
    p.add_argument("--tc-teeth", type=int, default=10, help="teeth on torque-converter/clutch output sprocket (default 10)")
    p.add_argument("--axle-teeth", type=int, default=60, help="teeth on axle sprocket (default 60)")
    p.add_argument("--jackshaft", type=float, default=1.0, help="extra jackshaft ratio, driven/driver (default 1.0 = none)")
    p.add_argument("--tc-low", type=float, default=2.7, help="torque converter low ratio (30 series ~2.7, 40 series ~3.5 - verify)")
    p.add_argument("--tc-high", type=float, default=1.0, help="torque converter high/overdrive ratio (~0.9-1.0)")
    p.add_argument("--clutch", action="store_true", help="centrifugal clutch instead of TC (ratio fixed 1:1)")
    p.add_argument("--weight", type=float, default=450.0, help="total weight incl. driver, lb (default 450 for 250 lb driver)")
    p.add_argument("--efficiency", type=float, default=0.85, help="drivetrain efficiency (default 0.85)")
    p.add_argument("--rolling", type=float, default=0.03, help="rolling resistance coefficient (0.015 pavement, 0.03-0.08 grass/dirt)")
    p.add_argument("--mu", type=float, default=0.7, help="tire-ground friction coefficient for traction limit (default 0.7)")
    p.add_argument("--rear-fraction", type=float, default=0.60, help="static weight fraction on rear axle (default 0.60)")
    p.add_argument("--target-mph", type=float, help="if given, suggest axle sprocket sizes for this top speed")
    a = p.parse_args()

    eng = ENGINES[a.engine]
    torque = a.torque or eng["torque_ftlb"]
    rpm = a.rpm or eng["rpm_max"]
    tc_low, tc_high = (1.0, 1.0) if a.clutch else (a.tc_low, a.tc_high)
    sprocket_ratio = a.axle_teeth / a.tc_teeth * a.jackshaft

    print(f"Engine: {a.engine}cc  ({eng['note']})  torque {torque:.1f} ft-lb, max {rpm} rpm")
    print(f"Sprockets: {a.tc_teeth}T -> {a.axle_teeth}T  (x jackshaft {a.jackshaft})  = {sprocket_ratio:.2f}:1")
    print(f"Tire: {a.tire:.1f} in   Weight: {a.weight:.0f} lb   Drivetrain eff: {a.efficiency:.2f}")
    print()

    total_high = tc_high * sprocket_ratio
    total_low = tc_low * sprocket_ratio
    v_top = speed_mph(rpm, total_high, a.tire)
    print(f"Top speed (TC high {tc_high}:1, total {total_high:.2f}:1): {v_top:5.1f} mph")
    print(f"Speed at TC shift-out (low {tc_low}:1, ~2400 rpm):          {speed_mph(2400, total_low, a.tire):5.1f} mph")

    f_low = tractive_force_lb(torque, total_low, a.tire, a.efficiency)
    f_high = tractive_force_lb(torque, total_high, a.tire, a.efficiency)
    f_traction = a.mu * a.weight * a.rear_fraction
    f_roll = a.rolling * a.weight
    print()
    print(f"Tractive force at wheels, TC low:  {f_low:6.0f} lb")
    print(f"Tractive force at wheels, TC high: {f_high:6.0f} lb")
    print(f"Traction limit (mu*rear weight):   {f_traction:6.0f} lb  <- can't push harder than this, wheels spin")
    print(f"Rolling resistance:                {f_roll:6.0f} lb")

    f_usable = min(f_low, f_traction)
    grade = (f_usable - f_roll) / a.weight
    grade = max(min(grade, 1.0), -1.0)
    print(f"Max climbable grade (from standstill, TC low): {math.degrees(math.asin(grade)):4.1f} deg  "
          f"({grade*100:.0f}% grade)")
    accel_g = (f_usable - f_roll) / a.weight
    print(f"Initial acceleration on flat ground:           {accel_g:4.2f} g")
    if f_low < 0.25 * a.weight and not a.clutch:
        print("  WARNING: launch force < 0.25 g at this weight. Lower gearing (bigger axle sprocket) or more engine.")

    if a.target_mph:
        print()
        print(f"Axle sprocket options for ~{a.target_mph:.0f} mph top speed with {a.tc_teeth}T driver:")
        need_total = rpm * a.tire * math.pi / 12 * 60 / 5280 / a.target_mph
        need_sprocket = need_total / tc_high / a.jackshaft
        need_teeth = need_sprocket * a.tc_teeth
        print(f"  ideal axle sprocket: {need_teeth:.1f} teeth (total ratio {need_total:.2f}:1)")
        for t in range(int(need_teeth) - 6, int(need_teeth) + 8, 2):
            if t < 20:
                continue
            tr = tc_high * t / a.tc_teeth * a.jackshaft
            print(f"  {t:3d}T -> {speed_mph(rpm, tr, a.tire):5.1f} mph top, "
                  f"{tractive_force_lb(torque, tc_low * t / a.tc_teeth * a.jackshaft, a.tire, a.efficiency):5.0f} lb launch force")

    print()
    print("Rules of thumb: a 250 lb driver on a 212cc wants ~6:1 or lower sprocket ratio and a torque converter.")
    print("A 420cc at ~6:1 with a 40-series TC gives both ~35 mph and strong hill climbing.")


if __name__ == "__main__":
    main()
