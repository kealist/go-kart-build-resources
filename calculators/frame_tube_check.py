#!/usr/bin/env python3
"""
Frame tube bending check: a seat/floor rail treated as a simply-supported beam
with a centered point load from the driver under a vertical shock load.

This is a rough hand calc, not FEA. It is good for comparing tube sizes and
catching obviously undersized choices. Real frames are statically indeterminate
and welds/bracket geometry matter more than the tube.

Examples:
    python3 frame_tube_check.py                          # table for 250 lb driver, 3 g, 24 in span
    python3 frame_tube_check.py --driver 250 --g 3 --span 30 --rails 2
    python3 frame_tube_check.py --od 1.25 --wall 0.095 --material dom
    python3 frame_tube_check.py --square 1.0 --wall 0.083

Formulas (simply supported, center load P, span L):
    M = P L / 4            sigma = M / S           deflection = P L^3 / (48 E I)
Round tube:   I = pi/64 (D^4 - d^4),  S = 2 I / D
Square tube:  I = (b^4 - (b-2t)^4)/12, S = 2 I / b
"""
import argparse
import math

E = 29.0e6  # psi, steel
STEEL_DENSITY = 0.2836  # lb/in^3

# Approximate minimum yield strengths, psi. Always prefer the mill cert.
MATERIALS = {
    "erw":   {"yield": 40000, "note": "A513 type 1 ERW/HREW 1010-1015, cheap, common at steel yards"},
    "crew":  {"yield": 50000, "note": "A513 cold-rolled ERW 1008-1015 (approx)"},
    "dom":   {"yield": 70000, "note": "A513 type 5 DOM 1020/1026, the usual choice for kart/buggy frames"},
    "4130":  {"yield": 63000, "note": "4130 chromoly normalized; stronger per weight, TIG + more care"},
    "a500":  {"yield": 46000, "note": "A500 grade B square structural tube (approx)"},
}

COMMON_TUBES = [
    ("round", 1.00, 0.065), ("round", 1.00, 0.083), ("round", 1.00, 0.095), ("round", 1.00, 0.120),
    ("round", 1.25, 0.065), ("round", 1.25, 0.083), ("round", 1.25, 0.095), ("round", 1.25, 0.120),
    ("round", 1.50, 0.083), ("round", 1.50, 0.095), ("round", 1.50, 0.120),
    ("square", 1.00, 0.065), ("square", 1.00, 0.083), ("square", 1.00, 0.120),
    ("square", 1.25, 0.083), ("square", 1.25, 0.120), ("square", 1.50, 0.083), ("square", 1.50, 0.120),
]


def section(shape, size, wall):
    if shape == "round":
        d = size - 2 * wall
        i = math.pi / 64 * (size ** 4 - d ** 4)
        area = math.pi / 4 * (size ** 2 - d ** 2)
    else:
        inner = size - 2 * wall
        i = (size ** 4 - inner ** 4) / 12
        area = size ** 2 - inner ** 2
    s = 2 * i / size
    return i, s, area


def check(shape, size, wall, load_lb, span_in, yield_psi):
    i, s, area = section(shape, size, wall)
    m = load_lb * span_in / 4
    sigma = m / s
    fos = yield_psi / sigma if sigma > 0 else float("inf")
    defl = load_lb * span_in ** 3 / (48 * E * i)
    wt_per_ft = area * 12 * STEEL_DENSITY
    return sigma, fos, defl, wt_per_ft


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--driver", type=float, default=250.0, help="driver weight, lb (default 250)")
    p.add_argument("--extra", type=float, default=0.0, help="extra load on the same rails (seat, etc.), lb")
    p.add_argument("--g", type=float, default=3.0, help="vertical shock factor (2 yard use, 3 off-road jumps/curbs)")
    p.add_argument("--span", type=float, default=24.0, help="unsupported rail span between crossmembers, in (default 24)")
    p.add_argument("--rails", type=int, default=2, help="number of parallel rails sharing the load (default 2)")
    p.add_argument("--material", default="dom", choices=MATERIALS.keys())
    p.add_argument("--yield", dest="yield_psi", type=float, help="override yield strength, psi")
    p.add_argument("--od", type=float, help="single round tube OD to check, in")
    p.add_argument("--square", type=float, help="single square tube size to check, in")
    p.add_argument("--wall", type=float, help="wall thickness for --od/--square, in")
    p.add_argument("--min-fos", type=float, default=2.0, help="factor of safety threshold for OK flag (default 2.0)")
    a = p.parse_args()

    y = a.yield_psi or MATERIALS[a.material]["yield"]
    load = (a.driver + a.extra) * a.g / a.rails
    print(f"Driver {a.driver:.0f} lb + {a.extra:.0f} lb, x{a.g:.1f} g, over {a.rails} rail(s) -> {load:.0f} lb per rail")
    print(f"Span {a.span:.0f} in simply supported, center load.  Material {a.material}: yield {y:,.0f} psi "
          f"({MATERIALS[a.material]['note']})")
    print(f"Target FOS >= {a.min_fos}  (2 for yard, 3 for off-road with landings)")
    print()

    tubes = COMMON_TUBES
    if a.od or a.square:
        if not a.wall:
            p.error("--wall is required with --od/--square")
        tubes = [("round", a.od, a.wall)] if a.od else [("square", a.square, a.wall)]

    print(f"{'shape':6} {'size':>5} {'wall':>6} {'lb/ft':>6} {'stress psi':>11} {'FOS':>5} {'defl in':>8}  ok?")
    for shape, size, wall in tubes:
        sigma, fos, defl, wt = check(shape, size, wall, load, a.span, y)
        flag = "OK" if fos >= a.min_fos else "--"
        if defl > a.span / 100:
            flag += " (soft)"
        print(f"{shape:6} {size:5.2f} {wall:6.3f} {wt:6.2f} {sigma:11,.0f} {fos:5.1f} {defl:8.3f}  {flag}")

    print()
    print("Notes:")
    print(" - A center point load on a simply supported span is conservative for a welded frame but ignores")
    print("   stress concentration at welds and brackets, which is where frames actually crack.")
    print(" - Add gussets/triangulation at the seat mounts, bearing hangers and engine plate rather than")
    print("   only bumping wall thickness.")
    print(" - For a 250 lb driver: 1 in x 0.120 or 1.25 in x 0.095 DOM for main rails is a comfortable choice;")
    print("   1 in x 0.083 (the usual plan spec) is marginal for off-road use at this weight.")


if __name__ == "__main__":
    main()
