#!/usr/bin/env python3
"""
Coilover spring sizing for a go-kart swingarm or A-arm suspension.

Given the sprung weight on one axle, the number of shocks, the motion ratio
and shock angle, it reports wheel rate, static sag, ride frequency, the g-load
that uses up all the travel, and the spring rate you would need to hit a target
sag or frequency.

Examples:
    python3 spring_rate.py                                  # rear of a 450 lb kart, 2 shocks, 250 lb/in
    python3 spring_rate.py --sprung-weight 230 --shocks 1 --spring-rate 450 --motion-ratio 0.6
    python3 spring_rate.py --target-sag 0.30               # what spring rate gives 30% sag?
    python3 spring_rate.py --target-hz 2.0                 # what spring rate gives 2.0 Hz?

Definitions:
    motion ratio MR = shock compression / wheel travel  (0.5-0.8 typical for a swingarm;
                      = distance pivot->shock mount / distance pivot->axle for a simple arm)
    effective MR    = MR * cos(shock angle from the direction of wheel travel)
    wheel rate (per shock) = spring rate * MR_eff^2
    sag             = sprung weight / total wheel rate, as a fraction of wheel travel
    ride frequency  = (1 / 2 pi) * sqrt(K_total * g / W)    with g = 386 in/s^2
"""
import argparse
import math

G_IN = 386.1  # in/s^2


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--sprung-weight", type=float, default=230.0,
                   help="sprung weight carried by this axle, lb (default 230: 450 lb x 60%% rear minus ~40 lb unsprung axle/wheels)")
    p.add_argument("--shocks", type=int, default=2, help="number of shocks on this axle (default 2)")
    p.add_argument("--spring-rate", type=float, default=250.0, help="spring rate per shock, lb/in (default 250)")
    p.add_argument("--motion-ratio", type=float, default=0.7, help="shock travel / wheel travel (default 0.7)")
    p.add_argument("--shock-angle", type=float, default=20.0, help="shock angle from wheel-travel direction, degrees (default 20)")
    p.add_argument("--travel", type=float, default=4.0, help="wheel travel, in (default 4)")
    p.add_argument("--shock-stroke", type=float, help="shock stroke, in; if given, checks it against travel x MR")
    p.add_argument("--target-sag", type=float, help="sag fraction to solve spring rate for (e.g. 0.30)")
    p.add_argument("--target-hz", type=float, help="ride frequency to solve spring rate for (e.g. 2.0)")
    a = p.parse_args()

    mr_eff = a.motion_ratio * math.cos(math.radians(a.shock_angle))
    k_wheel_each = a.spring_rate * mr_eff ** 2
    k_total = k_wheel_each * a.shocks
    sag_in = a.sprung_weight / k_total
    sag_frac = sag_in / a.travel
    hz = math.sqrt(k_total * G_IN / a.sprung_weight) / (2 * math.pi)
    remaining = a.travel - sag_in
    g_to_bottom = 1 + remaining * k_total / a.sprung_weight if remaining > 0 else 0
    spring_force_static = a.sprung_weight / a.shocks / mr_eff

    print(f"Sprung weight {a.sprung_weight:.0f} lb on {a.shocks} shock(s), spring {a.spring_rate:.0f} lb/in")
    print(f"Motion ratio {a.motion_ratio} x cos({a.shock_angle:.0f} deg) = effective {mr_eff:.3f}")
    print()
    print(f"Wheel rate: {k_wheel_each:.0f} lb/in per shock, {k_total:.0f} lb/in total at this axle")
    print(f"Static sag:  {sag_in:.2f} in of {a.travel:.1f} in travel = {sag_frac:.0%}   (target 25-33%)")
    print(f"Ride frequency: {hz:.2f} Hz   (short-travel kart ~2.5-3.5 Hz; long-travel buggy ~1.5-2.5 Hz)")
    print(f"Bottoms out at about {g_to_bottom:.1f} g vertical   (aim for >= 2.5-3 g off-road, or add a bump stop)")
    print(f"Static force in each spring: {spring_force_static:.0f} lb -> spring compressed {spring_force_static / a.spring_rate:.2f} in at ride height")
    print(f"Shock stroke needed for full travel: {a.travel * a.motion_ratio:.2f} in"
          + (f"   (you have {a.shock_stroke:.2f} in: {'OK' if a.shock_stroke >= a.travel * a.motion_ratio else 'TOO SHORT, travel limited to ' + format(a.shock_stroke / a.motion_ratio, '.1f') + ' in'})" if a.shock_stroke else ""))

    if sag_frac > 0.40:
        print("  WARNING: sag > 40%: springs too soft for this driver. This is the classic 150 lb shock on a 250 lb driver.")
    elif sag_frac < 0.15:
        print("  Note: sag < 15%: very stiff; ride will be harsh and the wheels will skip on washboard.")

    if a.target_sag or a.target_hz:
        print()
        if a.target_sag:
            k_needed = a.sprung_weight / (a.target_sag * a.travel) / a.shocks / mr_eff ** 2
            print(f"Spring rate for {a.target_sag:.0%} sag: {k_needed:.0f} lb/in per shock")
        if a.target_hz:
            k_tot = (2 * math.pi * a.target_hz) ** 2 * a.sprung_weight / G_IN
            k_needed = k_tot / a.shocks / mr_eff ** 2
            print(f"Spring rate for {a.target_hz:.1f} Hz: {k_needed:.0f} lb/in per shock")
        print("Sag and frequency are linked: f = 3.13 / sqrt(static sag in inches). With 3-5 in of travel you")
        print("cannot have both 30% sag and 2 Hz; size by sag and accept ~3 Hz, or add travel.")
        print("Buy the nearest standard rate (coilover springs come in 25-50 lb/in steps) and adjust with preload.")

    print()
    print("Heavy driver note: a kart shock sold for a 150 lb rider is sprung ~40% too soft for 250 lb.")
    print("Re-spring it (2.5 in ID coilover springs are cheap) rather than cranking preload, which does not change the rate.")


if __name__ == "__main__":
    main()
