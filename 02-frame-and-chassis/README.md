# 02 - Frame and Chassis

Steel tube space frame for a single-seat, non-suspended off-road / yard kart.
Design load: **450-500 lb all-up** (250 lb driver), **3 g vertical**, **factor of safety 2**.
Numbers marked **(est.)** are rough figures, not quotes; prices move.

---

## Heavy driver notes (read first)

- **Do not build the plan-default 1" x 0.083" frame.** That size is fine for a 150 lb driver at ~300 lb all-up.
  At 450-500 lb the same tube runs out of margin at the seat cross-members and the rear axle hanger rails.
- **Recommended tube:** **1" OD x 0.120" wall DOM** round, or **1-1/4" OD x 0.095" wall DOM** round. Square
  equivalents: 1" x 1" x 0.120" or 1-1/4" x 1-1/4" x 0.095". 1-1/4" x 0.120" for the two main side rails and
  the rear axle hanger rails if you plan to jump it.
- **Weight cost of going up a size:** 1" x 0.083" -> 1" x 0.120" adds ~0.3 lb/ft (about 15 lb on a 45 ft frame).
  1" x 0.083" -> 1-1/4" x 0.095" adds ~0.36 lb/ft. Both are cheap insurance compared to a 250 lb driver.
- **Stiffness vs strength:** 1-1/4" x 0.095" is ~80% stiffer in bending than 1" x 0.120" at nearly the same weight.
  Bigger diameter beats thicker wall. Thicker wall is easier to weld without blow-through and tolerates
  gusset/bracket welds better; pick 1" x 0.120" if you are a new MIG welder, 1-1/4" x 0.095" if you are confident.
- **Seat:** tie the seat to the main side rails with at least two cross tubes, not to a floor pan. Use
  5/16" or 3/8" Grade 5 bolts through 3/16" plate tabs, gusseted. Seat mount tabs are the #1 crack location
  on heavy-driver karts.
- **Axle hangers:** 1" axle minimum, two-hole or four-hole 1" flange bearings, hangers welded to the rails
  with a 3/16" plate doubler, not just tabs. 1-1/4" axle if jumping.

---

## 1. Tubing choices

### Round vs square

| | Round | Square |
|---|---|---|
| Strength per lb in bending | Slightly lower than square of same wall | Slightly higher; corners carry material away from the neutral axis |
| Torsion | Much better (closed round section) | Worse; frame twists more on uneven ground |
| Joints | Need coping/notching (hole saw or template) | Simple miter cuts; flat faces for plates |
| Appearance / cleaning | Smooth, less mud trap | Collects mud on top faces |
| Bending | Easy with a rotary draw bender | Needs square dies; often avoided, use miters |
| Cost | DOM ~1.5-2x ERW | Square ERW is the cheapest structural shape |

Typical choice: **round for the perimeter and hoops, square for the floor/seat box and engine plate area**.
A full square-tube frame with miter joints is the fastest build if you have no bender or notcher.

### Common sizes, properties, and what they are good for

Section properties for mild steel round tube (I = moment of inertia, S = section modulus; computed from geometry).

| Size | Weight (lb/ft) | I (in^4) | S (in^3) | Use for |
|---|---|---|---|---|
| 1" x 0.083" round | 0.81 | 0.0253 | 0.051 | Plan default; bumpers, nerf bars, light cross tubes **only** on a heavy kart |
| 1" x 0.120" round | 1.13 | 0.0327 | 0.065 | **Recommended minimum for all structural members** |
| 1-1/4" x 0.095" round | 1.17 | 0.0579 | 0.093 | **Recommended main rails and axle hanger rails** |
| 1-1/4" x 0.120" round | 1.45 | 0.0688 | 0.110 | Main rails if jumping; roll hoop |
| 1" x 1" x 0.083" square | 1.04 | 0.0430 | 0.086 | Floor box, seat box (light driver spec) |
| 1" x 1" x 0.120" square | 1.44 | 0.0555 | 0.111 | Floor box, seat box, engine plate rails |

Material yield strengths (typical, est.; mill certs vary): HREW/ERW A513 1010: 40-50 ksi; **DOM A513 1020: ~65-70 ksi**;
4130 chromoly normalized: ~65-75 ksi. Note DOM is almost as strong as 4130 in the as-welded condition and
costs far less.

### DOM vs ERW vs HREW vs 4130

| Type | What it is | Weldability | Cost (est., 1" x 0.120", per ft) | Verdict |
|---|---|---|---|---|
| **HREW** (hot-rolled electric welded) | Cheapest welded tube, visible internal seam, mill scale | Good with MIG; grind scale at joints | $1.50-2.50 | OK for non-critical parts; seam must not be on the tension face of a bend |
| **ERW / CREW** (cold-rolled electric welded, A513 type 1/2) | Welded, smoother than HREW | Good | $2-3 | Acceptable structural choice if DOM is unavailable |
| **DOM** (drawn over mandrel, A513 type 5, 1020/1026) | ERW tube cold-drawn after welding; seam removed, tight tolerances, higher yield | Excellent with MIG, ER70S-6 wire | $3-5 | **Recommended** for the whole frame |
| **4130 chromoly** | Alloy steel, higher strength-to-weight, thinner wall for same strength | TIG preferred (ER70S-2 or ER80S-D2 filler); MIG possible but less forgiving; no post-weld heat treat in a home shop | $6-10 | Not worth it for a yard kart; weight saved is ~10 lb on a 500 lb vehicle |

Reading on the differences:

- [Metal Supermarkets: Difference between ERW, DOM and seamless tube](https://www.metalsupermarkets.com/difference-between-erw-dom-and-seamless-tube/) - short, accurate explanation of the manufacturing processes.
- [Metal Supermarkets: The 5 types of carbon steel round tube](https://www.metalsupermarkets.com/the-5-types-of-carbon-steel-round-tube/) - HREW, CREW, DOM, seamless, and when each is used.
- [Welding Tips and Tricks: TIG welding 4130 chromoly tubing](https://www.weldingtipsandtricks.com/4130-chromoly-tubing.html) - filler choice and heat control if you do go chromoly.

### Where to buy tubing

| Source | Good for | Notes |
|---|---|---|
| [Metals Depot - DOM round tube](https://www.metalsdepot.com/steel-products/steel-round-tube-dom) | Cut-to-length DOM, no minimum | Also [welded (ERW) round tube](https://www.metalsdepot.com/steel-products/steel-round-tube-welded) for bumpers. Shipping on 6-8 ft lengths is reasonable; 20 ft is not. |
| [Online Metals - 1020/1026 DOM round tube](https://www.onlinemetals.com/en/buy/carbon-steel-round-tube-1020-1026) | Cut-to-length, lists 1" x 0.120" DOM | Similar pricing to Metals Depot; compare shipping. |
| [Speedy Metals - 1" OD x 0.120" DOM](https://speedymetals.com/p-3497-1-od-x-120-wall-dom-steel-tube.aspx) | Priced by the inch | Handy for short pieces (spindle uprights, hanger stubs). |
| [Speedway Motors - 1-5/8" x 0.120" DOM roll cage tube](https://www.speedwaymotors.com/Round-DOM-Roll-Cage-Tubing-1-5-8-Inch-X-12-Inch,461363.html) | Race-oriented DOM and [4130 chassis tube](https://www.speedwaymotors.com/Round-Chromoly-Chassis-Tube-1-1-4-x-0-083-,295406.html) | Good if you want a roll hoop in 1-1/2" or 1-5/8"; also sells tabs, gussets, and weld-in bungs. |
| Local steel yard / fab supply | 20-24 ft sticks of HREW or DOM at **$2-4/ft (est.)** | Cheapest per foot by far; bring a truck or ask them to cut to 8 ft. Ask for A513 DOM 1020 by name. |
| Local scrap / surplus | Bed frames, trampoline tube | **Do not** use unknown steel for structural members. |

Budget for a 1" x 0.120" DOM frame: **45-55 ft of tube, $150-275 (est.)** plus $40-80 of 3/16" plate and
16 ga floor sheet. Order 15% extra for mistakes.

---

## 2. Load paths and where frames crack

Think of the frame as two side rails carrying the driver + engine between the front spindles and the rear
axle hangers, with cross tubes keeping them parallel and resisting twist. Stress concentrates where
**a point load enters a tube** and where **a stiff thing meets a flexible thing**.

| Location | Why it cracks | Fix |
|---|---|---|
| **Seat mount tabs** | 250 lb bouncing on four small tabs welded mid-span to a tube; tab weld toe becomes a stress riser | Tabs on cross tubes that land on the side rails, not mid-span; 3/16" tabs with a wrap-around weld; add a 1" x 1" x 0.120" seat subframe |
| **Rear axle bearing hangers** | All the rear load (60% of 450-500 lb, x3 in a hole) goes through two hangers; thin tabs flex and fatigue | Hangers welded to a doubler plate on a 1-1/4" rail; brace the hanger rail to the main rail with a diagonal; use 4-hole flange bearings |
| **Engine plate** | Vibration + chain pull; plate welded on three sides cracks at the fourth | 3/16" or 1/4" plate, welded all around or bolted on rubber-isolated mounts; chain pull line should pass near a frame rail |
| **Front spindle brackets / kingpin bosses** | Side load when you hit something; bracket welded to a single tube | Weld bosses into a corner (two tubes meeting), gusset below; use 5/8" kingpin bolts |
| **Rear hoop / bumper to rail joint** | Rear-end hits transmit to a single weld | Gusset or a second short tube forming a triangle |
| **Any abrupt stop of a doubler or gusset** | Stiffness jump | Taper gusset ends; do not end a weld exactly at a tube corner |
| **Floor pan plug welds** | Pan carries loads it was not designed for | Stitch weld or bolt the pan; keep it non-structural |

Rule: every point load (seat bolt, bearing, kingpin, engine bolt, pedal pivot, steering bushing) should
land **within 2" of a tube intersection** or on a doubler plate.

### Triangulation

A rectangle of tubes is a mechanism; it stays square only through the bending stiffness of the tubes and
the welds, which is exactly what you are trying not to load. Add diagonals so loads go into tubes as
tension/compression:

- One diagonal in the floor plane (behind the seat or under it).
- Diagonals from the rear axle hanger rails up to the engine deck.
- A gusset (1/8" or 3/16" plate, or a short tube) at every T-joint carrying a point load.
- The front cross member and the steering support hoop should form a triangle with the side rails in plan view.

### Fully welded vs bolted

Fully welded is lighter, stiffer, cheaper, and the norm. Bolt only what must come off: engine plate,
seat, bumpers, nerf bars, and possibly the rear hanger assembly. Use Grade 5 or 8 bolts, nyloc nuts or
lock washers; drill bolt holes through tube only with a sleeve (3/4" x 0.083" tube crush sleeve) or through
a plate tab, never a bare hole through a round tube.

---

## 3. Welding

| Process | Use for | Notes |
|---|---|---|
| **MIG (GMAW), 0.030" ER70S-6, 75/25 gas** | Mild steel: HREW, ERW, DOM | The right tool for this kart. A 140-180 A 120/240 V machine handles 0.120" wall easily. 0.083" wall is easier to blow through than 0.120" - another reason to use thicker wall. |
| Flux-core (FCAW-S) | Outdoors, windy | Works; more spatter, more cleanup, harder on thin wall. |
| **TIG (GTAW), ER70S-2** | 4130 chromoly, thin wall, show welds | Slower; required if you go chromoly. Not needed for DOM. |
| Stick | Thick plate only | Too hot for 0.083-0.120" tube for a beginner. |

Practice: cut 20 coupons of your actual tube, weld T-joints, then cut them apart and saw/grind through the
weld to check penetration before touching the frame. Weld sequence: tack everything, check diagonals, then
weld opposite joints alternately to control warp.

---

## 4. Frame jig / table

- A flat surface is 90% of the jig. Options: a 3/4" MDF or plywood sheet on sawhorses (draw the plan on it
  full size), a steel welding table, or two 4 x 4 ft 1/4" plates leveled with shims. Check with a straightedge
  and a string line across the diagonals.
- Fixture tubes with screwed-down wood blocks, 1" angle-iron stops, or 3/4" conduit clamps on plywood.
  For a steel table, use weld-on tabs and C-clamps, or 2 x 2 angle "cradles".
- Mark the centerline and the axle line on the table. Every dimension references those two lines.
- Build the floor plane first, flat on the table. Add uprights and the rear deck after the floor is tacked.
- Keep a **1/16" per foot** tolerance on rail straightness and a 1/8" tolerance on diagonals for a 48" frame.

---

## 5. Tube notching / coping

- **Hole saw notcher** (Harbor Freight Central Machinery pipe/tubing notcher, item 42324, ~$50-70 est.; JD2 TN-100
  ~$200-300 est.): clamp the tube, drive a bi-metal hole saw the same diameter as the mating tube. Cheap ones
  wobble; a good hole saw (Morse, Starrett, Bahco) matters more than the notcher. Manual for the JD2 unit:
  [JD Squared TN-100 operator manual (PDF, Missouri S&T)](https://web.mst.edu/sdelc/Shop_Documents/Operator%20Manuals/JDsquared%20Tube%20Notcher%20TN-100%20(HPV).pdf).
- **Paper template + grinder**: print a wrap-around template, trace, cut with a 4-1/2" grinder and a half-round
  file. Slower per joint but zero tooling cost. Metalgeek's free online cope calculator generates these
  templates; it is listed at [HomemadeTools.net: homemade coping calculator](https://www.homemadetools.net/homemade-coping-calculator),
  which points to metalgeek.com (search "metalgeek cope calculator"). Print at 100% scale and check the
  printed scale bar.
- **Square tube**: just miter on a chop saw or bandsaw. 45-degree miters with a weld all around are stronger
  than butt joints.
- Gap: fit-up gap under 1/16" (half the wall thickness). Bigger gaps mean weaker, uglier welds.

---

## 6. Tube bending

Bending is optional on a yard kart - most plans are all straight tube with mitered or coped joints. Bend only
where it buys something: the rear hoop, a front bumper, nerf bars, a seat hoop.

| Tool | Capacity | Price (est.) | Notes |
|---|---|---|---|
| **JD2 Model 3 / Model 32** (manual rotary draw) | 1/2" to 2" OD; 2" x 0.120" mild | $400-900 bender + $150-300 per die; [Model 3 at Trick-Tools](https://www.trick-tools.com/JD2_Model_3_Manual_Tubing_Bender_100155_2249), [Model 32 at Trick-Tools](https://www.trick-tools.com/JD2_Model_32_Manual_Tubing_Bender_302000_2247) | Industry-standard hobby bender. Model 32 is the heavier version; both can add hydraulics later. |
| **Rogue Fabrication M601** | to 1-3/4" x 0.156" | ~$750-1100 + dies; [M601 product page](https://www.roguefab.com/product/metal-tube-bender-m601/), [bender configurator](https://www.roguefab.com/bender-configurator/) | Air/hydraulic ready; 180+ degree bends. Their [Bending 101](https://www.roguefab.com/?p=133) and [tech index](https://www.roguefab.com/tech/) teach bend layout, start points, and springback for any bender. |
| **Pro-Tools MB-105 / 105HD** | to 2" ; 105HD rated to 0.134" wall | ~$500-900 + dies ($285-490 each); [MB-105 at Trick-Tools](https://www.trick-tools.com/Pro_Tools_MB_105_Manual_Tubing_Bender_MB_105_4666) | Comparable to JD2 Model 3; dies are the expensive part either way. |
| **Harbor Freight 12-ton hydraulic pipe bender** (item 32888 / 62539) | Pipe, 1/2" to 2" NPS | ~$100-130; [product page](https://www.harborfreight.com/12-ton-hydraulic-pipe-bender-62539.html), [owner's manual (PDF)](https://manuals.harborfreight.com/manuals/32000-32999/32888-193175527103.pdf) | **A pipe bender, not a tube bender.** Dies are sized for pipe OD (1" NPS pipe is 1.315" OD), so 1" tube sits loose and kinks/flattens. Usable only for crush bends in non-structural bumper tube or if you make matching tube dies. Do not use it on frame members. |

Bending notes:

- Rotary draw benders need a die for each tube OD; centerline radius (CLR) of 3-4.5" is typical for 1" to 1-1/4" tube.
- Mild steel springs back 2-5 degrees; chromoly more. Overbend and check with a protractor.
- DOM and 1-1/4" x 0.095" bend well; 1" x 0.083" HREW is prone to wrinkling on the inside of the bend.
- Ordering bends from a local fab shop: usually $10-25 per bend (est.) if you bring the tube and a drawing.

---

## 7. Free / cheap analysis: hand calcs and FEA

### Hand calc (do this even if you run FEA)

Design load: **W = 500 lb** all-up, **3 g**, so total dynamic load **1500 lb**. Rear carries 60% = 900 lb;
worst single case: one rear hanger sees 450 lb (half) to 900 lb (one-wheel landing).

Simply supported beam, point load at mid-span:

```
M = P * L / 4            (in-lb)
sigma = M / S             (psi)
FOS = yield / sigma
```

Example: hanger rail span L = 24", P = 600 lb (one-side landing, partial):

| Tube | S (in^3) | sigma (ksi) | FOS vs DOM 65 ksi | FOS vs HREW 45 ksi |
|---|---|---|---|---|
| 1" x 0.083" | 0.051 | 70.6 | 0.9 | 0.6 |
| 1" x 0.120" | 0.065 | 55.4 | 1.2 | 0.8 |
| 1-1/4" x 0.095" | 0.093 | 38.7 | 1.7 | 1.2 |
| 1-1/4" x 0.120" | 0.110 | 32.7 | 2.0 | 1.4 |

This is deliberately conservative (real frames have continuity and diagonals that share the load), but it
shows why **1" x 0.083" HREW is not acceptable for a 250 lb driver** and why the hanger rail wants 1-1/4" tube or
a shorter span (add a cross tube under the hanger to cut L in half, which cuts stress in half).

Deflection check (stiffness, comfort, and alignment): `delta = P L^3 / (48 E I)`, E = 29e6 psi. Keep static
deflection under ~0.05" per span so the chain and axle stay aligned.

Target: **FOS 2-3 on 2-3 g vertical** for off-road use; FOS 1.5 on a 1.5 g case is enough for a smooth-lawn kart.

### FEA

- [FreeCAD FEM workbench (official wiki)](https://wiki.freecad.org/FEM_Module) - free, uses CalculiX. Model the frame as
  beam elements on tube centerlines (fast, good enough) or solid tubes (slow). Apply 3 g loads at the seat and
  engine mount nodes, fix the four wheel contact points, read von Mises stress and deflection.
- [Autodesk Fusion for personal use](https://www.autodesk.com/products/fusion-360/personal.html) - free hobbyist CAD, but
  the **simulation workspace is not included** in the free tier; use it for modeling and the cut list, run FEA in FreeCAD.
- Student Baja reports in folder 01 show typical load cases (front impact 4-5 g, side 2-3 g, rollover 1.5-2 g, bump 3 g)
  and how they set boundary conditions. Copy the method, scale the loads to 500 lb.
- Sanity rule: if FEA says stress is under 10 ksi everywhere, you fixed the model wrong; if it says over yield
  at a single node at a sharp corner, that is a mesh singularity, look at the stress 1/2" away.

---

## 8. Bumpers and nerf bars

- Front bumper: 1" x 0.083" round, hoop shape, 4-6" ahead of the front tires, bolted on with two 3/8" bolts per side
  so it can be replaced after a hit. Mount to the front cross member, not to spindle brackets.
- Rear bumper: same tube, must cover the engine and sprocket/chain. Doubles as a lift handle; with a 500 lb kart make
  it a hoop, not a bar on two stubs.
- Nerf bars (side): 1" tube from behind the front spindle to ahead of the rear tire, 2-3" outboard of the rails. Keeps
  feet, fence posts, and other karts out of the rear tires. Protect the chain side.
- Chain guard is mandatory: 1/8" plate or 16 ga sheet covering the sprocket and the top run of the chain.

---

## 9. Paint and powder coat prep

1. Finish all welding and **drilling** first; grind welds only where they must clear parts (grinding removes strength at the toe).
2. Drill a 1/8" vent/drain hole in any sealed tube (needed for powder coat ovens and to let condensation out).
3. Remove mill scale: media blast (best; $50-150 est. at a local shop for a kart frame), or wire cup on a grinder plus
   80 grit, then phosphoric acid metal prep.
4. Degrease with acetone or wax-and-grease remover right before coating.
5. **Paint route:** self-etching primer (1 can) + 2-3 coats of rattle-can enamel or, better, a 2K urethane or chassis
   paint in a quart. ~$40-80 est. Touch-up is easy; chips rust.
6. **Powder coat route:** $150-300 est. at a local shop for a kart-size frame. Tougher, no touch-up; mask bearing bores,
   threaded holes (silicone plugs), and any surface that must be metal-to-metal (engine plate, hanger faces). Eastwood sells
   hobby HotCoat guns and powders if you want to do it in a toaster-oven-size setup, but a whole frame needs a shop oven.
7. Do not coat under the engine plate or the hanger faces; coat there cracks and traps grit. Paint them after assembly.
