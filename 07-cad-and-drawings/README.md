# 07 - CAD and Manufacturing Drawings

How to model go-kart parts (frame, brackets, spindles, hubs, pedals, steering) so an online or local shop can make them without a phone call. Prices and plan limits below are as of **November 2026** and change often; check the vendor page before relying on them.

Builder note: at ~250 lb rider weight, size brackets, spindles and mounting plates one step heavier than typical plans (e.g. 3/16" instead of 1/8" plate, 0.120" wall instead of 0.083" tube). Model the heavier part from the start; it is cheaper than re-ordering.

---

## 1. CAD software options (hobbyist licensing)

| Software | Cost for hobbyists | Key limits | Best for |
|---|---|---|---|
| **Onshape Free** | $0 | All documents are public; non-commercial only | Browser-based, nothing to install, excellent frame tool |
| **Autodesk Fusion (Personal Use)** | $0, renew yearly | 10 active editable documents; reduced export list; non-commercial, under $1k/yr revenue | Most tutorials on the web; built-in sheet metal + CAM |
| **FreeCAD 1.x** | $0, open source | Steeper learning curve; 1.0 fixed the old topological-naming problem | Fully offline, no account, no license drift |
| **SolidWorks for Makers** | ~$48/yr (3DEXPERIENCE) | Non-commercial; watermarked files, cloud login required | Industry-standard workflow at hobby price |
| **Shapr3D** | Free Basic (2 projects); Pro ~$299/yr | Free tier is small; tablet/pen oriented | Quick concept modeling on iPad |
| **SketchUp** | Free web tier | Mesh modeler, no parametrics, poor STEP, no sheet metal | **Not recommended** for mechanical parts |

- [Onshape pricing](https://www.onshape.com/en/pricing) - Free plan: unlimited public documents, full CAD, mobile apps.
- [Autodesk: Fusion free license changes](https://autodesk.com/support/technical/article/Fusion-360-Free-License-Changes) - official FAQ on the 10-active-document limit and which exports stay (STEP and STL stay; DXF only from sketch/flat pattern).
- [Hackaday summary of the Fusion personal-use terms](https://hackaday.com/2020/09/16/autodesk-announces-major-changes-to-fusion-360-personal-use-license-terms/) - plain-English rundown of what was cut.
- [FreeCAD 1.0 release announcement](https://freecad.github.io/Website/news/freecad-version-1-0-released/) - what changed in 1.0; download from the freecad.org downloads page (1.0.2 was current at time of writing).
- [SOLIDWORKS for Makers](https://www.solidworks.com/makers) - ~$48/yr, non-commercial, you may sell up to $2k/yr of what you make.
- [Shapr3D subscription plans](https://support.shapr3d.com/hc/en-us/articles/7871961422364) - Basic vs Pro feature list.

Recommendation: **Onshape** if you do not mind public files, **Fusion** if you want the most tutorials and built-in sheet-metal flat patterns, **FreeCAD** if you want zero license risk.

---

## 2. Learning resources

### Onshape
- [Onshape Learning Center overview](https://www.onshape.com/en/blog/learn-cad-onshape-learning-center) - free self-paced courses and the "CAD Basics" pathway; sign in at learn.onshape.com.
- [Too Tall Toby](https://tootalltoby.com/blog) - speed-modeling challenges with 2D drawings you can model in any CAD; search YouTube for "TooTallToby". Excellent for drawing-reading practice.
- [Onshape blog: speed modeling](https://www.onshape.com/en/blog/speed-3d-modeling-record-time) - how the fast modelers structure sketches.

### Fusion
- [Lars Christensen on the Autodesk Fusion blog](https://www.autodesk.com/products/fusion-360/blog/author/lars-christensen/) - his YouTube channel (handle "cadcamstuff") has the classic "Fusion 360 for Absolute Beginners" series; older but still the best on-ramp.
- [HP Academy: 3D sketching fundamentals in Fusion](https://www.hpacademy.com/previous-webinars/349-3d-sketching-fundamentals-in-fusion-360/) - webinar on 3D sketches for roll cages and tube chassis.
- Product Design Online and Kevin Kennedy's "Learn Fusion 360 in 30 Days" (search YouTube) - short daily lessons.

### FreeCAD
- [Basic Part Design Tutorial (0.19+)](https://wiki.freecad.org/Basic_Part_Design_Tutorial_019) - the official one-hour starter.
- [FreeCAD wiki: video tutorials list](https://wiki.freecad.org/Video_tutorials/en) - curated channels, including MangoJelly.
- [MangoJelly Solutions playlist for FreeCAD 1.0](https://blog.freecad.org/2024/08/27/mango-jelly-solutions-latest-playlist-helps-explore-version-1-features/) - slow, complete beginner series; YouTube handle "MangoJellySolutions". Also see the [Understanding FreeCAD course index](https://classcentral.com/classroom/youtube-understanding-freecad-course-beginners-course-90508).

---

## 3. Modeling a tube frame

Workflow that works in every package:

1. **Sketch the skeleton first.** Draw centerlines of every tube as 2D sketches on the top, side and front planes, or one 3D sketch. Dimension wheelbase, track, seat position and steering-shaft angle here; everything else references this.
2. **Sweep tubes along the skeleton.** Use the package's tube/frame tool (below). Keep each tube a separate body so you get a cut list.
3. **Trim/cope at joints.** Decide which tube is "through" and which is "coped". Main rails are through; crossmembers cope onto them.
4. **Add brackets as separate parts** positioned off the frame, so you can send them to a laser service independently.
5. **Export a cut list** (length, angle, OD, wall) for the tube supplier and a STEP of each coped tube for a tube laser.

Tool by package:

- **Onshape - Frame feature.** [Onshape Frames](https://www.onshape.com/en/features/frames): pick a standard profile (ANSI/ISO tube, or a custom 1.25" x 0.120" round), select sketch lines, trim with hierarchy, auto cut list. [Announcement with workflow video](https://onshape.com/en/blog/announcing-onshape-frames).
- **Fusion - Pipe command.** [Tech tip: Pipe command](https://www.autodesk.com/products/fusion-360/blog/tech-tip-pipe-command/): round/square hollow profiles along sketch paths. No rectangular profile and weak junction handling; for rectangular tube, sketch the profile and Sweep, then Combine-Cut to cope. [Forum thread on race-car tube frames](https://forums.autodesk.com/t5/fusion-design-validate-document/race-car-tube-frames/td-p/13203929) covers practical workarounds.
- **FreeCAD - no Blender needed.** Use Part Design Sweep/AdditivePipe along a sketch path for each tube, or install the [Flamingo/Dodo workbench](https://wiki.freecad.org/Flamingo_Workbench) from the Addon Manager (Pype tools create tubes, elbows and frames from skeleton sketches). The older "freecad.frametools" addon (GitHub user looooo) adds a miter-cut command but is lightly maintained.
- **SolidWorks** - Weldments: structural member + trim/extend, cut list built in.

---

## 4. Exporting for manufacturing

| Part type | Process | Send this | Notes |
|---|---|---|---|
| Flat brackets, plates, gussets | Laser / waterjet | **DXF** (2D, 1:1, inch or mm stated) or STEP | Export from a flat pattern or sketch, not "Export sheet as DXF" |
| Bent sheet parts | Laser + CNC bend | **STEP** of the folded part (preferred) or flat DXF + bend lines | Service applies its own K-factor from a STEP |
| Spindles, hubs, bosses | CNC machining / lathe | **STEP** (AP214 or AP242) + PDF drawing if any tolerance matters | STL is rejected for CNC |
| Jigs, pedal pads, templates | 3D printing | **STL** or **3MF** | 3MF keeps units and multiple bodies |
| Coped/notched frame tubes | Laser tube cutting | **STEP** of each tube as its own body | Tube lasers read the 3D model; no DXF unrolling needed |

DXF rules of thumb:
- One closed outline per part, no duplicate or overlapping lines, no text, no dimensions, no construction geometry.
- Convert splines to polylines/arcs; keep units explicit.
- Open the DXF in a second program to check scale before uploading.
- [SendCutSend: 4 ways to export a DXF from Fusion](https://sendcutsend.com/blog/4-ways-to-export-a-dxf-from-fusion-360/) - which menu paths produce clean 2D files.
- [SendCutSend video: exporting clean DXF files](https://sendcutsend.com/education/video/how-to-export-clean-dxf-files/) - common failures (3D DXFs, stray points, unit loss).

Tube cut files: SendCutSend and OSH Cut both want a **.STEP** of the finished tube (copes, holes, slots and end angles modeled). Model each tube as a single body with the exact OD and wall they stock, keep cutouts away from bend regions (OSH Cut blocks cutouts within 2 tube diameters of a bend), and expect no deburring. See [SendCutSend tube cutting](https://sendcutsend.com/services/tube-cutting) and [OSH Cut tube laser](https://tube.oshcut.com/).

---

## 5. 2D manufacturing drawings

**When you need one:** any machined feature with a fit (bearing bore, spindle shaft, kingpin hole), any thread, any surface finish, or anything you want inspected. **When STEP alone is fine:** laser-cut flats, bent brackets, tube cuts, 3D prints. SendCutSend explains why their process ignores drawings: [Why don't you need technical drawings?](https://sendcutsend.com/faq/why-dont-you-need-technical-drawings-callouts/)

Minimum content of a hobby drawing:
- **Title block:** part name, part number/rev, material and condition (e.g. 1018 CRS, 4130 N, 6061-T6), quantity, units, scale, your name/email, date.
- **General tolerance note:** e.g. "Unless otherwise specified: X.X = +/-0.030, X.XX = +/-0.010, X.XXX = +/-0.005, angles +/-1 deg, break edges 0.01-0.03".
- **Views:** front + one section through any bore; isometric for orientation.
- **Call out only what matters:** bearing bore with its fit, thread spec (e.g. 5/8-18 UNF-2B), shaft diameter with tolerance; leave everything else to the general note.
- **Surface finish** only where a seal or bearing rides (e.g. 32 Ra on a spindle journal).

GD&T for hobbyists - use at most these three:
- **Position** on bolt-hole patterns that must mate (e.g. a 4-bolt hub flange).
- **Perpendicularity** of a bore to a mounting face (spindle bore to steering-arm face).
- **Concentricity/runout** on a hub where a wheel rides.
- [CNCCookbook GD&T basics](https://www.cnccookbook.com/gdt-basics) - free, machinist-oriented intro.
- [Five Flute: GD&T basics](https://www.fiveflute.com/guide/gd-t-basics-a-comprehensive-introduction-to-geometric-dimensioning-and-tolerancing) - how to read and place feature control frames.

---

## 6. Standard hobby tolerances (what services actually hold)

| Process | Typical tolerance | Source / note |
|---|---|---|
| CNC machining (standard) | +/-0.005" (ISO 2768-m ~ +/-0.1 mm) | Tighter costs more; ask for +/-0.001" only on bearing fits |
| Laser cutting, sheet metal | +/-0.005" on cut edge; kerf ~0.006-0.010" | [SendCutSend cut tolerance FAQ](https://sendcutsend.com/faq/what-is-your-cut-tolerance/) |
| Waterjet / plasma | +/-0.010 to 0.020"; taper on thick plate | Waterjet leaves a frosted edge; plasma has slag and HAZ |
| CNC bending | +/-1 deg (bends under 24"); +/-0.015" bend-to-edge, plus ~0.015" per additional bend | [SendCutSend bending tolerances](https://sendcutsend.com/faq/what-are-your-tolerances-for-bending/) |
| Laser tube cutting | +/-0.005" cut; tube stock itself is +/-0.005-0.010" OD | [SendCutSend tube](https://sendcutsend.com/services/tube-cutting) |
| Saw-cut stock | +/-0.060 to 0.125" | Metal suppliers' cut-to-length |
| FDM 3D printing | +/-0.2-0.5 mm | Holes shrink; design 0.2 mm oversize |

Design rule: never make two laser-cut parts locate each other through a hole-and-pin fit tighter than 0.010"; use slots or oversize holes with washers and let the frame jig set the geometry.

---

## 7. Designing for sheet metal (brackets, pedal arms, mounting plates)

- **Bend radius:** services fix it per material and thickness; you cannot request a custom one. Use their published inside radius (roughly 1x thickness for mild steel) in your CAD sheet-metal rules. [SendCutSend custom-radius FAQ](https://sendcutsend.com/faq/can-you-bend-parts-with-a-custom-bend-radius/).
- **K-factor:** 0.30-0.50 is normal; use the service's table so the flat pattern matches their press brake. [SendCutSend bending guide](https://sendcutsend.com/blog/the-ultimate-guide-to-sheet-metal-plastic-bending/) and their bending calculator page list K-factor and radius by material.
- **Minimum flange length:** measured from bend center to cut edge; typically 4x thickness plus radius. Short flanges cannot be gripped by the die.
- **Bend relief:** add a relief cut (width >= thickness, depth >= radius + thickness) at every bend that ends in the middle of an edge; otherwise the corner tears.
- **Hole-to-bend distance:** keep holes at least 2.5x thickness + radius from the bend line, or they distort into ovals. Holes inside the bend zone are deformed.
- **Hole-to-edge:** >= 1x thickness (2x on load-bearing brackets).
- **Minimum hole size:** >= thickness for laser; smaller holes become cones.
- **Bend direction and sequence:** a U-channel needs a base at least 2x the flange height so the tooling fits.
- [SendCutSend: From CAD to cut, designing for sheet metal](https://sendcutsend.com/blog/from-cad-to-cut-designing-for-sheet-metal/) - full walkthrough.
- [SendCutSend: preparing bends in CAD (video)](https://sendcutsend.com/education/video/preparing-bends-in-cad/) - setting sheet-metal rules in Fusion/Onshape.
- [Design tips to increase accuracy of sheet metal parts](https://sendcutsend.com/blog/how-to-add-precision-to-your-sheet-metal-parts/) - tab-and-slot, self-fixturing, datum choices.

Heavier-rider note: 3/16" (0.188") mild steel brackets bend fine on online services; 1/4" is usually the max for bending, and the inside radius grows. For pedal arms and steering uprights, prefer a 3/16" laser-cut flat with a welded gusset over thin bent sheet.

---

## 8. Design-for-manufacturing checklists

**Before uploading a flat part (laser/waterjet)**
- [ ] One closed outline, no open contours or overlaps
- [ ] Units confirmed; a 1" test circle measures 1"
- [ ] Holes >= material thickness; slots >= 1.5x thickness wide
- [ ] Hole-to-edge >= thickness; webs between holes >= thickness
- [ ] No tapped holes requested; order holes at tap-drill size and tap yourself
- [ ] Tabs/slots for self-jigging weld assemblies added
- [ ] Part fits the service's max sheet (usually 44" x 44" or less on hobby services)

**Before uploading a machined part (CNC)**
- [ ] Modeled from a standard stock size (round bar, plate) with <= 0.125" per side to remove
- [ ] Internal corners have radius >= 1/8" (tool radius); no sharp inside corners
- [ ] Pocket depth <= 3x tool diameter; no deep narrow slots
- [ ] All fillets/chamfers that are cosmetic are removed (they cost setups)
- [ ] Tolerances only where needed; general note covers the rest
- [ ] Threads called out on drawing, or modeled as plain holes you tap yourself
- [ ] Minimum wall thickness >= 0.060" aluminum, 0.040" steel

**Before uploading a tube (tube laser)**
- [ ] Each tube is one body with exactly the stock OD/wall the service lists
- [ ] Copes clear the mating tube by ~0.020" for weld gap
- [ ] No cutouts within 2 OD of any bend; no features on the weld seam side if it matters
- [ ] Length within service max (often 8-10 ft hobby, check)

**Before sending a frame to a welder**
- [ ] Cut list with lengths, end angles and quantity
- [ ] Overall drawing with wheelbase, track, ride height, seat and steering positions
- [ ] Note which joints are tack-only until squared
- [ ] Mark "DO NOT WELD" on anything that bolts on later

---

## 9. Free engineering references

- [McMaster-Carr CAD models](https://mcmaster.com/cad-models) - free STEP/DXF of nearly every bolt, bearing, sprocket and bushing; drop them into assemblies to check fit.
- [Engineers Edge calculators](https://www.engineersedge.com/calculators/) - beam deflection, bolt torque, press fits, weld sizing, section properties.
- [Bolt Depot fastener information](https://boltdepot.com/Fastener-Information/Bolts) - grade markings, strength tables, torque charts, thread pitch tables.
- [Roark's Formulas for Stress and Strain, 9th ed.](https://www.mhprofessional.com/9781260453751-usa-roarks-formulas-for-stress-and-strain-9e) - the tabulated beam/plate/ring formulas; a used earlier edition is cheap and equally useful.
- **Machinery's Handbook** (Industrial Press, 32nd ed. 2024, ~$170 new; older editions used for $20-40) - threads, fits, materials, speeds/feeds. Any edition from the last 30 years is fine for hobby work.
- **Shigley's Mechanical Engineering Design** (any edition, used) - bolted joints, shafts, keys, fatigue, welds; the textbook behind most of Engineers Edge.

Bolt and thread quick rules for a kart:
- Structural bolts (spindles, steering, seat, engine): Grade 8 / 10.9 minimum; nylon-lock or jam nuts everywhere a nut can vibrate off.
- Kingpin and steering: 1/2" or 5/8" Grade 8 bolts in bronze or poly bushings; never thread into sheet metal.
- Tap-drill sizes and torque values: Bolt Depot tables above; use 75% thread for steel, 50-60% for aluminum.
- Thread engagement: >= 1x bolt diameter in steel, 1.5-2x in aluminum.

---

## 10. Simple FEA (sanity checks, not certification)

Hobby FEA is for comparing design A vs B and catching gross under-sizing, not proving a part is safe. Use a 3-5x factor on rider weight for shock loads (a 250 lb rider landing off a curb puts well over 1,000 lb through the seat mounts).

Tools:
- **Fusion (Personal)** - no simulation in the personal license; use one of the others.
- **Onshape** - simulation is on paid tiers only; export STEP to SimScale or FreeCAD instead.
- **FreeCAD FEM workbench** (CalculiX solver, free, offline) - linear static with fixed constraints and force loads; good enough for brackets and spindles. Start from the FEM tutorials on the FreeCAD wiki.
- [SimScale Community plan](https://simscale.com/product/pricing/) - free cloud FEA; public projects, limited core-hours; upload a STEP and run a static structural case in the browser.

Sane boundary conditions:
- Fix the part only where it is actually bolted or welded (the bolt-hole cylindrical faces or the weld footprint), not a whole face.
- Apply loads where they really enter: wheel load at the spindle journal, pedal force (~150-200 lb) at the pad, seat belt load at the anchor.
- Use a remote load or a small patch, never a single node (that creates a fake stress spike).
- Mesh: at least 3 elements through any thickness you care about; refine around holes and fillets, then re-run to see whether the peak stress moved by less than ~10%.
- Pass criteria: peak von Mises < yield / 2 (mild steel yield ~36 ksi, 4130 N ~63 ksi, 6061-T6 ~40 ksi) and deflection that does not change geometry (steering arm < 0.5 mm under full load).
- If a result looks surprisingly good, check units (lbf vs N, in vs mm) before believing it.
