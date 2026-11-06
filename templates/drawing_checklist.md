# Manufacturing drawing / file checklist

Use before sending anything to a laser cutter, machinist or welder.

## Every part
- [ ] Part name, part number, revision, date, your name/contact in the title block
- [ ] Material and thickness called out (e.g. "A36 HR plate 0.188 in" or "6061-T6 0.25 in")
- [ ] Quantity
- [ ] Units stated (in or mm) and scale noted
- [ ] Finish (none / deburr / powder coat color / zinc)
- [ ] File exported at 1:1 scale, no construction geometry, no text in cut layer

## Flat laser / waterjet (DXF)
- [ ] Closed polylines, no overlapping or duplicate lines
- [ ] Hole diameters sized for the fastener clearance (3/8 bolt -> 0.406 in hole) and the service's kerf behavior
- [ ] Hole-to-edge distance >= material thickness (2x is better)
- [ ] Slots and tabs sized with the service's tolerance (+/- 0.010 in typical)
- [ ] Bend lines on a separate layer or in the service's bend-specification format
- [ ] Minimum feature size respected for the thickness (no 0.030 in slits in 1/4 in plate)
- [ ] Engraved part number if the service offers it (saves sorting 30 brackets)

## CNC machined (STEP + drawing)
- [ ] Only critical dimensions toleranced tighter than +/- 0.005 in; everything else default
- [ ] Bores for bearings/shafts: specify the fit (e.g. 1.0000 +0.0005/-0 for a slip fit on a 1 in axle)
- [ ] Keyways: width, depth, and key size called out
- [ ] Threads: size, class, depth, and whether you want them tapped by the shop
- [ ] No deep narrow pockets, internal sharp corners have radii >= tool radius
- [ ] Stock size listed if you want them to use standard bar/plate

## Tube cutting / frame
- [ ] Tube spec: OD x wall, material (e.g. 1.25 x 0.095 DOM A513 T5)
- [ ] Cut list with lengths, end cope/miter angles, and which end is which
- [ ] Bend table: bend centerline radius, degrees, distance between bends, rotation
- [ ] Overall frame assembly drawing with key dimensions (wheelbase, track, rail spacing)
- [ ] Weld symbols or a note ("all joints full fillet weld, 0.125 in, MIG ER70S-6")

## Welding service hand-off
- [ ] Assembly drawing and parts labeled to match
- [ ] Fixturing instructions (what must be square/parallel: axle bearing hangers, spindle brackets)
- [ ] Which welds are structural vs. cosmetic
- [ ] Post-weld: check flatness, any holes to ream after welding
