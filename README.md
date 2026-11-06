# Go-Kart Build Resources (sized for a 250 lb driver)

A curated, opinionated set of resources for designing a DIY go-kart, checking that
the design is strong enough, and getting the custom parts made by online or local
shops. It is organized in the order you will actually need things.

Most free kart plans and kits assume a 120-170 lb driver. At 250 lb the kart plus
driver lands around 450 lb, which changes the frame tubing, axle, brakes, seat,
engine choice, and gearing. Every section calls those changes out in a
**Heavy driver notes** block near the top.

## How to use this repo

1. Fill in `templates/requirements.md`. Ten minutes here saves weeks later.
2. Read `01-design-fundamentals` and `02-frame-and-chassis` to settle geometry and tube size.
3. Run the scripts in `calculators/` with your numbers. They are hand calcs, not FEA,
   but they will stop you from buying 1 in x 0.065 tube.
4. Pick the powertrain, brakes and axle (`03` to `06`), then build the bill of
   materials from `templates/bom.csv` and `09-parts-sourcing`.
5. Model it (`07-cad-and-drawings`), export DXF/STEP, and get quotes
   (`08-manufacturing-services`, `templates/quote_request_email.md`).
6. Before the first ride, go through `10-safety`.

## Sections

| Folder | What is in it |
|---|---|
| [01-design-fundamentals](01-design-fundamentals/README.md) | Layout, geometry, CG, ergonomics for a large driver, weight budget, design process, SAE Baja reports as worked examples |
| [02-frame-and-chassis](02-frame-and-chassis/README.md) | Tube size and material, where frames crack, triangulation, welding, jigs, notching, bending, simple FEA |
| [03-powertrain](03-powertrain/README.md) | Engines (212 vs 420 class), torque converters vs clutches, chain and sprockets, gearing math |
| [04-steering](04-steering/README.md) | Spindles, Ackermann, caster/camber, tie rods, bump steer |
| [05-brakes](05-brakes/README.md) | Why band brakes are out, mechanical vs hydraulic disc, rotor sizing, pedal ratio |
| [06-wheels-tires-axle-seat](06-wheels-tires-axle-seat/README.md) | 1 in vs 1.25 in axle, bearings, hubs, wheels, tire load ratings, seats that fit |
| [07-cad-and-drawings](07-cad-and-drawings/README.md) | CAD software choices, modeling tube frames, export formats, drawings, tolerances, sheet-metal rules |
| [08-manufacturing-services](08-manufacturing-services/README.md) | Laser/waterjet, tube laser, bending, CNC, 3D printing, welders, powder coat, metal stock; how to get a quote |
| [09-parts-sourcing](09-parts-sourcing/README.md) | Vendor directory and a priced sample BOM for a 420cc heavy-driver kart |
| [10-safety](10-safety/README.md) | Kill switch, guards, belts, cage debate, torque specs, pre-ride checklist |
| [11-plans-builds-community](11-plans-builds-community/README.md) | Plans, documented builds, channels, forums, books, racing rulebooks as design references |
| [12-suspension](12-suspension/README.md) | Rigid vs swingarm vs full suspension, swingarm design, shocks and spring rates for a heavy driver |
| [calculators](calculators/README.md) | Gear ratio / speed / grade, brake sizing, frame tube check, axle check, chain check, spring rate |
| [templates](templates/) | Requirements sheet, BOM, weight and CG worksheet, drawing checklist, quote email, build log |
| [cad](cad/README.md) | Where your own design files go |

## The short version for a 250 lb driver

| Decision | Typical plan spec | Recommended at 250 lb | Why |
|---|---|---|---|
| Main frame tube | 1 in x 0.083 round | 1 in x 0.120 or 1.25 in x 0.095 DOM | Roughly 1.5-2x the bending strength; see `calculators/frame_tube_check.py` |
| Engine | 212cc (6.5 hp) | 420cc (13 hp), or 212cc only for flat yard use | Hill climbing and launch with 450 lb all-up |
| Transmission | centrifugal clutch | torque converter (30 series on 212, 40 series on 420) | Low ratio for launch, clutch slips and overheats under heavy load |
| Chain | #35 | #40 or #420 | More margin at the torque a heavy kart puts through it |
| Rear axle | 1 in keyed | 1.25 in keyed 1045 | Wheel-overhang bending; both sizes have off-the-shelf hubs |
| Brakes | band or mechanical disc | hydraulic disc, 7-8 in rotor | 450 lb at 30 mph is ~13,500 ft-lb to dump every stop |
| Seat | 14-15 in kart bucket | 17-18 in+ seat, UTV or XL bucket | Standard kart seats are built for small racers |
| Tires | whatever the kit has | check load rating, >= 150 lb per rear tire | Many 8 in kart tires are rated for far less than you think |
| Sprocket ratio | 5:1 to 6:1 | 6:1 to 7:1 on a 212, ~6:1 on a 420 | Trade a few mph of top end for launch and hills |
| Suspension springs | shocks as sold for kart kits | re-spring for ~250 lb/in per shock on a 2-shock swingarm | Kit shocks are sprung for 150 lb riders and sit at 40%+ sag; see `calculators/spring_rate.py` |

## Scope

This is written around a single-seat, live-axle, small-4-stroke kart for yard and
trail use, rigid by default with suspension options in section 12, built in a home shop with a MIG welder and an angle
grinder, outsourcing the parts that need a laser or a lathe. It is not a racing
chassis guide. Nothing here makes a kart street legal.

Prices and links were checked in November 2026 and will drift. Links are to primary
sources (vendors, manufacturers, universities, established forums) where possible.

## Contributing

Corrections and additions are welcome. Keep the "heavy driver notes" blocks, verify
links before adding them, and mark estimates as estimates.

## License

MIT, see `LICENSE`. Linked third-party content belongs to its owners.
