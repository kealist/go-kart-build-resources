# 01 - Design Fundamentals

Single-seat, off-road / yard kart. Live rear axle, no suspension (by default), small 4-stroke engine.
Target all-up weight with driver: **400-450 lb**. Driver: **~250 lb (113 kg)**.

Everything below is sized for that driver. Where a number is a rough figure rather than a measured or
published value it is marked **(est.)**.

---

## Heavy driver notes (read first)

Most free kart plans (KartFab, diygokarts.com, kartbuilding.net style plans) silently assume a
**~150 lb driver** and a **~250-300 lb all-up weight**. At 250 lb the driver is **~60% of the total
vehicle mass**, not ~45%, and that changes the design in five places:

| Item | Typical plan assumption | What changes at 250 lb driver |
|---|---|---|
| Static load | ~300 lb total | ~430 lb total; every member sees ~1.4x the load |
| Dynamic load (hit a rut / drop off a curb, 2-3 g) | 600-900 lb | **860-1300 lb** through the frame |
| Seat and seat mounts | 4 small tabs, 1/4" bolts | Seat rails tied into main rails, 5/16"-3/8" bolts, gussets |
| Rear axle | 3/4" axle common | **1" axle minimum**; 1-1/4" is not overkill for jumps |
| Tubing | 1" x 0.083" | **1" x 0.120"** or **1.25" x 0.095"** (see folder 02) |
| CG | Low because driver is light | Driver torso dominates CG; seat must go as low and as far forward as leg room allows |
| Ergonomics | 14-15" seat, 36-38" seat-to-pedal | 16-18"+ seat, 40-44" seat-back-to-pedal (measure yourself) |

Rule of thumb: **design to a 450 lb all-up vehicle at 3 g vertical with a factor of safety of 2**, then
check the heaviest realistic single event (rear wheel drop into a hole with all 60% rear weight on one
side). That is the load case most plans never check.

---

## 1. Basic layout and geometry

### Wheelbase and track

| Parameter | Yard / off-road kart target | Notes |
|---|---|---|
| Wheelbase | **40-50 in** (1016-1270 mm) | Shorter = more agile, more pitch on bumps. Go 46-50" for a big driver so leg room is not fighting the engine bay. Racing sprint karts are ~41" by rule; off-road yard karts commonly 44-50". |
| Front track (center to center of tires) | 30-36 in | Wider = more roll resistance. Limit is garage door / trailer width. |
| Rear track | 32-40 in | Usually 1-4" wider than front for stability under power. A 250 lb driver sitting high needs the wide end of this range. |
| Ground clearance (frame bottom) | **4-6 in** loaded | 2-3" on pavement karts; off-road needs more or the belly will beach on ruts. Measure **with the driver seated** - a stiff unsprung kart still sinks 1/2-1" on tire squish alone. |
| Overall length | 65-75 in | Driven by wheelbase + bumpers. |
| Overall width | 36-44 in | Check your trailer, gate, and shed door first. |

Wheelbase-to-track ratio around **1.3-1.5** is a good starting point for a non-suspended kart; above ~1.6 it
starts to push on in corners, below ~1.2 it feels twitchy.

### Center of gravity (CG) and why low matters

With no suspension, the only thing keeping the inside wheels on the ground in a corner is the
**ratio of track width to CG height**. Simplified, the lateral acceleration at which a rigid kart tips is:

```
a_tip (in g)  ≈  (track / 2) / CG_height
```

- 36" track, 14" CG height -> tips at ~1.29 g (tires usually slide first at ~0.7-0.9 g on dirt, so fine)
- 36" track, 20" CG height -> tips at ~0.9 g (now rollover and sliding are the same event: dangerous)

A 250 lb driver sitting upright in a tall seat puts the **driver's CG at roughly 10-12" above the seat
pan** (est.); the seat pan itself may be 6-8" off the ground. That is how you land at a 20" combined
CG. Countermeasures, in order of effectiveness:

1. **Seat pan as low as ground clearance allows** (frame rail height + 1/2" plate, or a dropped seat pan).
2. **Recline the seat 15-25 degrees** - moves torso mass down and back.
3. **Widen rear track** before you widen the front.
4. Keep the engine, battery, and fuel tank low and inboard.

### Weight distribution

Target **40/60 front/rear static** (with driver). Rear bias puts weight on the driven, live axle for traction
and keeps the front light enough to steer without power steering. Acceptable band is roughly 35/65 to 45/55.

- Driver is the big lever: move the seat 1" and you move ~250 lb by 1", which on a 48" wheelbase shifts
  about **5 lb per inch** between axles (250 x 1/48).
- Engine placement is the other lever: a 70 lb engine moved 6" changes distribution by about 9 lb.
- Check it: put each axle on a bathroom scale (or two scales under one axle, sum them) with the driver
  seated in riding position. Target rear reading ~ 0.6 x total.

### Static ride and no-suspension reality

Without suspension the **tires are the suspension**. Use the biggest, lowest-pressure tires that fit:
rear 18x9.50-8 or 20x10-8 at 5-8 psi, front 15x6.00-6 or 16x6.50-8 at 6-10 psi (est. pressures;
go by sidewall and feel). Reserve 1-2" of frame clearance above the tires for flex and mud.

---

## 2. Ergonomics for a large driver

Measure yourself sitting on a kitchen chair against a wall before drawing anything.

| Dimension | Typical plan | For a 250 lb / ~6 ft driver | How to measure |
|---|---|---|---|
| Seat width (inside, at hips) | 14-15 in | **16-18 in, up to 19 in** | Hip width seated + 1-2" |
| Seat-back to pedal face | 36-40 in | **40-46 in** | Heel on floor, knee ~120-130 deg, leg not locked |
| Seat pan to steering wheel rim (bottom) | 10-12 in | **12-14 in** | Thigh clearance; you must be able to get in with the wheel in place |
| Steering wheel diameter | 10-11 in | 11-13 in | Larger wheel = lower effort with a heavy nose |
| Cockpit width between side rails | 18-20 in | **22-26 in** | Entry/exit and elbow room |
| Floor pan length | 24-30 in | 30-36 in | Big feet need room beside the pedals |
| Seat back height | 16-18 in | 20-24 in | Support to the shoulder blades on rough ground |

Other points:

- **Entry/exit**: a big driver cannot easily drop into a kart with a steering shaft across the thighs. Options:
  quick-release steering wheel hub (~$30-60 est.), a steering wheel that tilts, or a wider cockpit so you
  step in beside the column. A side rail no higher than ~10" above the ground helps.
- **Pedals**: use pedals at least 3" wide with a heel stop on the floor. Set the pedal pivot so the
  brake pedal can take a **200+ lb panic stomp** without bending (1/4" plate or 3/4" x 0.120" tube arm).
- **Seat**: molded plastic "high-impact" kart seats from kart vendors are commonly 14-15" wide and will
  not fit. Look at fiberglass **XL / XXL racing seats** (Tillett and similar sell XL sizes), lawn-tractor
  style high-back seats (cheap, wide, padded, ~17-19"), or a UTV/buggy seat. Check the seat's rated
  weight if it has one.
- **Weight transfer when braking**: with 60% rear static and a high CG, braking shifts a lot of load
  forward; a rear-only brake (the usual kart setup) will lock the rear early. Budget for a bigger disc
  (7-8") or plan front brakes later.

---

## 3. Weight budget worksheet

Fill in the right column as you buy parts. Left columns are typical values for a 1" DOM frame,
Predator-class engine, 1" live axle. All **(est.)** unless you weigh them.

| Component | Typical (lb) | Notes | Your kart (lb) |
|---|---|---|---|
| Frame, bare (40-50 ft of 1" x 0.120" DOM + plates) | 55-75 | 1" x 0.083" would be 40-55; 1.25" x 0.095" about 60-80 | |
| Floor pan (16 ga sheet, ~2 x 3 ft) | 12-18 | 14 ga adds ~5 lb | |
| Bumpers / nerf bars | 10-20 | Easy place to lose weight if needed | |
| Engine (Predator 212 / 420 / 670 class) | 38 / 70 / 95 | Dry, without fuel | |
| Clutch or torque converter | 3-8 | 30-series TAV ~6 lb | |
| Live axle 1" x 40", bearings, hangers, hubs, sprocket, brake disc | 25-35 | 1-1/4" axle adds ~8 lb | |
| Rear wheels + tires (pair, 18x9.5-8) | 24-32 | | |
| Front spindles, hubs, wheels + tires (pair) | 14-20 | | |
| Steering (shaft, wheel, pitman, tie rods) | 10-15 | | |
| Brakes (caliper, master or cable, pedal) | 5-8 | | |
| Seat + mounts | 8-15 | Wide high-back seats are heavier | |
| Pedals, throttle cable, linkages | 4-6 | | |
| Fuel tank + 1 gal fuel | 10-12 | | |
| Fasteners, paint, wiring, misc | 10-15 | Always more than you think | |
| **Kart subtotal** | **~230-330** | | |
| Driver | **250** | Add helmet + gear: +5-8 | |
| **All-up** | **~480-580** | Over the 400-450 target: see below | |

What this tells you: a conservatively built steel kart with a 420-class engine and a 250 lb driver
**lands at ~500 lb**, not 400-450. To stay near the target you either:

- use the 212-class engine and the lightest axle package (saves ~45 lb), or
- accept ~500 lb and **size the frame and axle for 500 lb** from the start (recommended; the cost in
  steel is maybe 10 lb and $30).

Do not chase weight by thinning the frame tube. The driver is 50-60% of the mass; you cannot diet the kart
into the plan's assumptions.

---

## 4. Design process

1. **Requirements** (one page): driver weight and height, terrain, top speed target (yard karts: 20-30 mph),
   engine on hand, max width (gate/trailer), budget, tools available (welder type, bender yes/no).
2. **Sketch**: side view and top view on graph paper at 1:4. Put the driver in first (a 250 lb driver
   outline: hip point, knee, heel, shoulder), then the engine, then the axle. Frame last.
3. **CAD**: FreeCAD (free) or Autodesk Fusion personal-use (free, limited). Model the tubes as centerlines
   first, then sweep the tube profile. Confirm ergonomic dimensions against the table above.
4. **Load check**: hand calcs on the three worst members (rear axle hanger rail, seat cross member, main side
   rail between front and rear) at 3 g x 450-500 lb with FOS 2 - see folder 02 for the formulas and tube
   properties. Optional: FreeCAD FEM on the whole frame.
5. **Drawings / cut list**: every tube with length, end angles, notch diameter, and bend data. Print
   full-size templates for notches.
6. **Manufacture**: tack everything on a flat table, re-measure diagonals, then final weld in a sequence that
   alternates sides to limit warp.
7. **Verify**: weigh each axle with the driver seated, check CG height by tilting (or calculation), load
   test the seat mounts by bouncing in it before the first drive.

---

## 5. Design references

### Baja SAE university design reports (free PDFs, excellent for frame load cases and FEA method)

These are student off-road vehicle reports. Their load cases (front impact, side impact, rollover, 3 g
bump, driver weight) and FEA setups transfer directly to a heavy-driver yard kart. Ignore the roll-cage
rules unless you build one.

- [NAU 2014 Mini Baja Team 01 final report (PDF)](https://ceias.nau.edu/capstone/projects/ME/2014/SAE-MiniBaja/team_01/team_01-final-report.pdf) - explicitly designs for a **250 lb driver**; compares 1018 1" x 0.120" baseline tube vs 4130 alternatives on bending stiffness and strength. The most relevant one here.
- [NAU 2014 Team 01 concept generation / selection report (PDF)](https://sce.nau.edu/capstone/projects/ME/2014/SAE-MiniBaja/team_01/team_01-concept-generation-selection-report.pdf) - tube selection trade study and the equivalence math.
- [NAU 2015 Mini Baja frame report (PDF)](https://ceias.nau.edu/capstone/projects/ME/2015/SAE-MiniBaja/frame/frame_report_3.pdf) - frame FEA with front/side/rear/rollover load cases and factors of safety.
- [NAU 2018 Baja frame preliminary report (PDF)](https://www.cefns.nau.edu/capstone/projects/ME/2018/SAEBaja/documents/frameprelim.pdf) - another iteration of the same method; good for seeing how load magnitudes are chosen.
- [University of Alaska Anchorage 2015 Baja design report (PDF)](https://coeng.uaa.alaska.edu/innovation/wp-content/uploads/2020/08/2015-Baja-SAE-All-Terrain-Vehicle-Design-Seawolf-Motorsports_Design-Report.pdf) - SolidWorks FEA correlated against physical deflection tests on a prior frame.
- [University of Akron Zips Baja frame study, 2020 (PDF via CORE)](https://core.ac.uk/download/323028449.pdf) - correlating real frame testing with simulation; shows what simplified FEA gets wrong.
- [University of Utah SAE Baja roll cage poster, 2024 (PDF)](https://mech.utah.edu/wp-content/uploads/2024/12/13-SAE-Baja-Roll-Cage-Team_Poster.pdf) - one-page summary of load cases and results; good quick reference.
- [Baja SAE 2018 rulebook (PDF, bajasae.net)](https://www.bajasae.net/content/2018-BAJA-RULES-FINAL-2017-08-30.pdf) - the roll-cage tubing spec (1018 steel, 1.0" OD x 0.120" wall baseline) and how equivalent tubing is calculated. Newer editions are under "Series Resources" on bajasae.net.

### Go-kart chassis papers / theses

- [Design and Analysis of Go-Kart Chassis for Front, Side and Rear Impact (Zenodo PDF)](https://zenodo.org/records/3584188/files/158%20Design%20and%20Analysis%20of%20Go-Kart%20Chassis%20for%20front,%20side%20and%20Rear%20Impact.pdf) - tubular 4130 kart frame in CATIA with impact load cases, von Mises stress and deformation; a template for your own load check.
- [Go-Kart Chassis Design and Construction - UTP final year project (repository page)](https://utpedia.utp.edu.my/id/eprint/7395/) - older (2004) but complete: stress analysis, FEA, and the build.

### Plans, vendors, and community

- [GoPowerSports go-kart plans page](https://www.gopowersports.com/go-kart-kits/go-kart-plans) - free PDF plans (the KartFab design) with a matching parts kit; the frame is 1" square tube sized for a light driver, so treat it as a layout reference, not a tube spec.
- [GoPowerSports live axle kit (frame not included)](https://www.gopowersports.com/live-axle-go-kart-kit-frame-not-included/) - shows what a complete 1" live-axle package weighs and costs for the budget sheet.
- [OMB Warehouse axles category](https://www.ombwarehouse.com/go-kart-parts/axles) - 1" and 1-1/4" axles, bearings, hangers.
- [diygokarts.com](https://diygokarts.com) - free plans and an active builder forum; search the forum for "big guy", "heavy driver", "1 inch axle" threads.
  - Example build log with frame photos: [Greg's go kart project part 1 - frame](https://www.diygokarts.com/community/threads/gregs-go-kart-project-part-1-frame.18728/)
  - Off-road example: [Viper offroad with full suspension project log](https://www.diygokarts.com/community/threads/viper-offroad-with-full-suspension-project-log.3231/)
- [KartPulse forum: seat advice for a larger driver](https://forums.kartpulse.com/t/seat-advice-for-larger-driver/6887) - racing-kart oriented, but the XL seat sizing discussion applies.
- [Tillett: Choosing your new kart seat (PDF, 2025)](https://tillett.co.uk/wp-content/uploads/2025/12/CHOOSING-YOUR-NEW-KART-SEAT-NEW-2025.pdf) - seat sizing chart including XL; use it to map your hip width to a seat size.
- [Autodesk Fusion for personal use](https://www.autodesk.com/products/fusion-360/personal.html) - free hobbyist CAD; note the simulation workspace is **not** in the free tier (use FreeCAD FEM or hand calcs instead).
- Not linked (could not verify a direct URL in this session): KartFab.com (plans + YouTube build series), BMI Karts (bmikarts.com, parts and frames), kartbuilding.net (free off-road kart plans). Search the names directly.
