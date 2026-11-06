#!/usr/bin/env python3
"""Compute total weight, CG position and front/rear split from weight_and_cg_worksheet.csv.
Usage: python3 cg_from_worksheet.py [worksheet.csv] [--wheelbase 44]
"""
import csv, sys

path = next((a for a in sys.argv[1:] if a.endswith(".csv")), "weight_and_cg_worksheet.csv")
wb = 44.0
if "--wheelbase" in sys.argv:
    wb = float(sys.argv[sys.argv.index("--wheelbase") + 1])

w = mx = mz = 0.0
with open(path, newline="") as f:
    for row in csv.DictReader(f):
        wt = float(row["weight_lb"]); x = float(row["x_in_from_front_axle"]); z = float(row["z_in_above_ground"])
        w += wt; mx += wt * x; mz += wt * z
cgx, cgz = mx / w, mz / w
rear = cgx / wb
print(f"Total weight: {w:.0f} lb")
print(f"CG: {cgx:.1f} in behind front axle, {cgz:.1f} in above ground  (wheelbase {wb:.0f} in)")
print(f"Static split: front {1-rear:.0%} / rear {rear:.0%}   (target ~40/60 for a rear-drive kart)")
print(f"Rollover threshold (half track / CG height): with 30 in track -> {15/cgz:.2f} g lateral")
