# 08 - Manufacturing Services

Where to get go-kart parts made from the CAD files in section 07. Prices, minimums and lead times are **approximate, US-centric, and dated November 2026**; every service changes them often. Links were checked at time of writing; resources without a link could not be confirmed and are named only.

Heavier-rider note: most of what you order will be 3/16" steel flats, 0.120" wall tube and 1"+ steel round bar. All of the hobby-accessible services below handle those sizes.

---

## 1. Flat laser / waterjet cutting (brackets, gussets, plates, pedal arms)

| Service | Min order | Turnaround (approx.) | Materials | Notes |
|---|---|---|---|---|
| [SendCutSend](https://sendcutsend.com/laser-cutting-services) | ~$39 total | 2-4 days production + shipping | Mild, 4130, stainless, aluminum, plastics | Instant DXF/STEP quote, free US shipping; tapping, deburr, powder, hardware add-ons |
| [OSH Cut](https://oshcut.com/capabilities) | None | 1-5 days | Steel to 1"+, aluminum, stainless, copper | Instant quote, volume discounts, bending, tube, powder coat in-house; [vs SendCutSend comparison](https://www.oshcut.com/comparison) |
| [Xometry sheet cutting](https://www.xometry.com/capabilities/sheet-cutting) | None | ~3-10 days | Wide; laser, [waterjet](https://www.xometry.com/capabilities/sheet-cutting/waterjet-cutting/), plasma | Accepts nested DXF for family pricing; sheets up to 10 x 20 ft; absorbed Big Blue Saw |
| [Fabworks](https://www.fabworks.com/) (Ventura, CA) | None | Days | Steel, stainless, aluminum | Instant STEP quote, 2D laser, bending, 5-axis tube laser; US-made |
| Big Blue Saw | - | - | - | Waterjet pioneer, [folded into Xometry in 2021](https://www.digitalengineering247.com/article/xometry-integrates-big-blue-saws-software-data-for-laser-and-waterjet-sheet-cutting/); use Xometry |
| [Ponoko](https://www.ponoko.com/why) | ~$1-50 | Same day to days | Mostly acrylic, wood, thin sheet | Fine for dash panels and templates, not structural steel |
| Local shop | Often $50-150 | 1-2 weeks | Whatever they stock | Best for thick plate (1/2"+) and plasma; bring a DXF on a USB stick |

Rough pricing (Nov 2026): a 4" x 6" bracket in 3/16" mild steel runs about $8-15 each from SendCutSend/OSH Cut at qty 1, dropping 30-50% at qty 10.

---

## 2. Laser tube cutting (frame members with pre-cut copes, tabs and holes)

A tube laser turns a STEP of each frame tube into a part with perfect fishmouths, slots and bolt holes. You weld it like a kit. This is the single biggest time saver for a DIY frame.

| Service | Status / minimum | Tube range (approx.) | File | Notes |
|---|---|---|---|---|
| [SendCutSend tube cutting](https://sendcutsend.com/services/tube-cutting) | ~$39 min; service has run a **waitlist** when capacity is short, check page | Round, square, rectangular; mild, 4130, stainless, 6061 ([stock list](https://sendcutsend.com/materials/tube)) | STEP/STP | +/-0.005" cut; no deburring; 2-4 day production |
| [OSH Cut tube laser](https://tube.oshcut.com/) | None | Up to 10" OD, 0.375" wall; also [CNC tube bending](https://www.oshcut.com/services/cnc-tube-bending) to 1.5" OD x 0.120" wall | STEP | Instant quote + DFM; no cutouts within 2 OD of a bend; [background article](https://oshcut.com/articles/laser-tube-cutting-technology-accessible-to-all) |
| [Fabworks tube laser](https://www.fabworks.com/services/tube-laser-cutting) | None | Round/square/rectangular, 5-axis | STEP ([guide](https://www.fabworks.com/blog/tube-laser-cutting-guide)) | Bevel-capable copes; 2-3 day ship quoted |
| Local tube laser job shops | Usually $200-500 min | Large | STEP + drawing | Search "tube laser" + your city; many fab shops with Trumpf/BLM machines take small jobs off-season |

Tips: order 1-2 spare tubes of the most complex cope; buy the straight uncut tube from the same service so OD/wall matches their fixtures; model weld gaps (~0.020") into copes.

---

## 3. Bending / forming (pedal brackets, seat mounts, steering supports)

- [SendCutSend CNC bending](https://sendcutsend.com/bending/) - add bends to any laser part; up to ~0.250" steel; +/-1 deg; they set the radius and K-factor per material.
- [OSH Cut bending](https://oshcut.com/capabilities) - sheet bending plus in-browser tube bending; thicker steel limits than most hobby services.
- [Fabworks](https://www.fabworks.com/services/laser-cutting) - bending from STEP of the folded part; [file requirements](https://www.fabworks.com/faq/cut-files) (DXF for flat, STEP for bent/tube, 24 MB max).
- Local: any shop with a press brake will bend your laser-cut flats for $20-60 per setup; bring the folded STEP and a printed drawing with bend angles.

---

## 4. CNC machining (spindles, hubs, bushings, axle collars, steering bosses)

| Service | Min order | Turnaround | Notes |
|---|---|---|---|
| [Xometry CNC quote](https://www.xometry.com/capabilities/cnc-machining-quote) | None, but qty-1 parts often $80+ | 3-10 days | US network; instant STEP quote; good DFM feedback; pricey for one-offs |
| [Protolabs Network (formerly Hubs)](https://www.hubs.com/help-center/how-to-get-a-quote/) | None | ~5+ business days | Global network, US + EU shipping; [rebrand note](https://www.hubs.com/protolabs-network/) |
| [JLCCNC](https://jlccnc.com/capabilities/cnc-machining-service) | ~$1 + shipping | ~3-7 days + 1-2 weeks shipping from China | Cheapest for simple aluminum/steel parts; milling, turning, 5-axis |
| [PCBWay CNC / 3D](https://pcbway.com/blog/News/PCBWay_New_Services__3D_printing_and_CNC_machining.html) | ~$50 CNC | Similar to JLC | Instant quote with DFM; same shipping caveat |
| [RapidDirect](https://www.rapiddirect.com/landing-page/online-cnc-machining-services/) | Low | ~3+ days + shipping | ISO 2768-m standard; AI DFM; China-based |
| Local machinist | Often $100-150 min, hourly $75-150 | 1-3 weeks | Best for one-off spindles, hubs, press-fit bores and anything needing a drawing conversation |

Getting cheap quotes:
- **Simple features:** through-holes, flats, one bore. Every extra face or setup roughly doubles the price.
- **Standard stock:** model from a stock size (e.g. 1.25" round bar, 1/2" plate) and leave the stock surface where it does not matter.
- **Loose tolerances:** leave the default (+/-0.005" or ISO 2768-m) everywhere except bearing bores and shafts.
- **Avoid deep pockets and thin walls:** depth <= 3x tool diameter; no inside corners under 1/8" radius.
- **No threads from the service:** order plain tap-drill holes and tap at home; tapped holes add $5-15 each.
- **Batch:** qty 2-4 of the same part is often only 20-40% more than qty 1.
- **Material:** 6061-T6 aluminum machines 3x faster than steel; 1018/1045 steel for spindles; 4140 only if you need it.

---

## 5. 3D printing (jigs, templates, prototypes, non-structural parts)

- [JLC3DP](https://jlc3dp.com/about-us) - from ~$1 per part; SLA resin, MJF/SLS nylon, FDM, metal; ships worldwide from China (allow 1-2 weeks).
- [PCBWay 3D printing](https://pcbway.com/blog/News/PCBWay_New_Services__3D_printing_and_CNC_machining.html) - FDM/SLA/SLS/metal; from ~$10.
- [Craftcloud](https://craftcloud3d.com) - price-comparison marketplace across many printers, no minimum; shows cheapest and fastest options.
- Home FDM (Bambu, Prusa, Creality) - cheapest for jigs; PETG or ASA for anything near the engine.

OK to print: pedal pads, throttle/brake pedal covers, seat spacers, dash/gauge mounts, wiring clips, fuel-line guides, number plates, **weld fixtures and tube-cope templates** (print the cope profile, wrap it, mark, grind), drill guides for bolt patterns, kill-switch housings.

Not OK to print: spindles, steering arms, hubs, pedal arms, brake levers, seat brackets, anything the kart's weight or the rider's foot force passes through, anything near the exhaust. MJF nylon can handle a shifter knob or a chain-guard bracket; it cannot handle a load path.

---

## 6. Welding services

How to find one:
- Search maps for "welding fabrication", "mobile welder" and "race car fabrication" within 30 miles; sprint-kart, off-road and circle-track shops understand tube frames.
- **Mobile welders** come to your garage; typical $75-150/hr with a 1-2 hr minimum, ideal for tacking a frame you jigged yourself.
- **Makerspaces** with MIG/TIG bays and a required safety class: [Nation of Makers directory](https://nationofmakers.us/resources-folder) and [makerspace.com listings](https://makerspace.com/).
- Community college welding programs often take student projects for the cost of consumables.

What to send or bring:
- The tube-laser-cut frame members (section 2) or saw-cut tubes with printed cope templates.
- An overall drawing with wheelbase, track, ride height and squareness notes, plus the cut list.
- Your laser-cut brackets with tab-and-slot locating features so they self-position.
- Material callouts: mild steel = MIG fine; 4130 = TIG, ER70S-2 or ER80S-D2, no post-weld quench.
- Say what is tack-only, what is full weld, and where you want welds ground flush.

Budget: a welded go-kart frame from pre-cut tubes is typically 3-6 shop hours ($300-700) if you deliver it jigged on a flat table; double that if they cut and fit.

---

## 7. Powder coating and plating

- **Local powder coaters** - search "powder coating" + city; a kart frame plus brackets typically $150-350 in a standard color; sandblast included or +$50-100. Ask for a high-temp or zinc-rich primer under the color if you drive in rain.
- [OSH Cut powder coating](https://www.oshcut.com/services/powder-coating) - coat laser-cut parts in the same order; [color selection guide](https://oshcut.com/learn/selecting-powder-colors) lists Prismatic and RAL options.
- [Prismatic Powders](https://www.prismaticpowders.com/shop/powder-coating-colors) (part of [NIC Industries](https://nicindustries.com/)) - 6,500+ colors, sells 1 lb bags; pick a color here and most local coaters can order it.
- [Eastwood HotCoat DIY kits](https://www.eastwood.com/powder-coating/powder-coat-guns.html) - [PCS-250 gun](https://www.eastwood.com/pcs250-dual-voltage-hotcoat-powder-gun.html) ~$120-230 with oven or booth bundles; needs 5-10 psi air and a dedicated oven (a used kitchen oven, never one you cook in). Good for brackets and pedals; frame too big for a home oven.
- **Zinc plating** - local platers often have $75-150 minimums; cheaper to buy zinc-plated hardware and powder coat everything else.
- Masking: tape every bearing bore, thread and bolt-face before coating; powder is 2-4 thou thick and will ruin a press fit.

---

## 8. Hardware and standard parts

- [McMaster-Carr](https://mcmaster.com/cad-models) - fastest shipping, every bolt/bearing/bushing with free CAD; expensive per part but one order covers a build. [Sprocket catalog](https://www.mcmaster.com/sprockets/) is a good example of the CAD-per-part depth.
- **Fastenal** (fastenal.com) - will-call at local branches; good for Grade 8 by the box.
- [Bolt Depot](https://boltdepot.com/Fastener-Information/Bolts) - cheap small quantities of Grade 8, metric 10.9, nylocks; the reference charts alone are worth a bookmark.
- **Grainger / Zoro** (grainger.com, zoro.com) - bearings, pillow blocks, clamps; Zoro is the same catalog with free shipping over a threshold.
- [Surplus Center](https://www.surpluscenter.com/) - 1" and 1-1/4" axle sprockets, weld-on hubs, pillow-block bearings, roller chain, hydraulic parts at surplus prices; the go-to for live-axle drivetrain parts.
- Kart-specific: GoPowerSports, BMI Karts, Comet Kart Sales (not linked; search by name) for spindles, hubs, tie rods, brake kits sized for 1" and 1-1/4" axles.

---

## 9. Tube and metal stock suppliers

- [Metals Depot](https://www.metalsdepot.com/servicecenter) - no minimum, cut-to-length square/round tube, DOM, plate; ships UPS for short lengths, freight for 20 ft.
- [Online Metals](https://www.onlinemetals.com/) - cut-to-size (+/-0.125") small quantities of tube, bar and plate; good aluminum selection.
- **Midwest Steel & Aluminum** (midweststeelsupply.com) - cut-to-size plate and bar, strong on aluminum and tool plate.
- [Speedway Motors](https://www.speedwaymotors.com/) - 1020 DOM and 4130 chromoly chassis tube in 3, 7 and 10 ft lengths (e.g. 1-1/4" x 0.095", 1-1/2" x 0.095", 1-5/8" x 0.120"), sold to racers.
- **Local steel yards** - cheapest by far for 20-24 ft sticks of 1" x 0.083" or 1-1/4" x 0.120" square/round; call ahead, bring a truck, expect a $25-50 cut fee or cut it yourself. Drop/remnant racks are gold for plate.
- Rule: buy frame tube locally in full sticks; buy exotic (4130, DOM, aluminum) and small cut pieces online.

---

## 10. Comparison table

| Service | Process | Materials | Typical min order | Turnaround (approx.) | Best for |
|---|---|---|---|---|---|
| SendCutSend | Laser, bend, tube, tap, powder | Steel, 4130, SS, Al, plastics | ~$39 | 2-4 d + ship | Brackets, bent parts, small tube orders |
| OSH Cut | Laser, bend, tube laser, tube bend, powder | Steel to thick, Al, SS | None | 1-5 d | Thick plate, tube + sheet in one order |
| Xometry | Laser/waterjet, CNC, sheet metal, 3DP | Very wide | None | 3-10 d | Waterjet, odd materials, big sheets |
| Fabworks | Laser, bend, tube laser | Steel, SS, Al | None | Days | STEP-driven tube and sheet |
| Protolabs Network | CNC, sheet, 3DP | Wide | None | 5+ d | US/EU machined parts with DFM |
| JLCCNC / PCBWay / RapidDirect | CNC, 3DP, sheet | Al, steel, nylon, resin | ~$1-50 | 1-3 wk incl. shipping | Cheapest machined aluminum and nylon prints |
| JLC3DP / Craftcloud | 3DP | Resin, nylon, FDM, metal | ~$1 / none | 1-3 wk | Jigs, pads, housings |
| Local fab shop | Plasma, saw, brake, weld | Steel | $50-200 | 1-3 wk | Thick plate, welding, full frames |
| Local machinist | Mill, lathe | Steel, Al | $100-150 | 1-3 wk | Spindles, hubs, press fits |
| Local powder coater | Powder coat, blast | - | $75-150 | 1-2 wk | Finished frame |

---

## 11. How to get a quote (walkthrough)

1. **Prep files.** One file per part, named `PARTNAME_REV_MATERIAL_THICKNESS_QTY` (e.g. `SPINDLE-BRKT_A_MS_0.188_2.dxf`). Flats as DXF or STEP, bent and tube parts as STEP, machined parts as STEP + PDF drawing. Check scale with a known dimension.
2. **Upload to two services** and compare; instant quotes take minutes. Note that material, thickness and quantity sliders change price non-linearly.
3. **Specify:** material and temper (e.g. "A36/1018 mild steel 0.188", "6061-T6 0.250", "4130 N 1.25 x 0.120 DOM"), quantity, any deburr/tapping/powder add-on, and for CNC the drawing with the two or three tolerances that matter.
4. **Split a frame into shippable pieces.** Hobby services cap length around 8-10 ft for tube and ~44" square for sheet; design main rails to break at a sleeved or butt-welded joint, or buy the long rails locally and order only coped crossmembers, uprights and brackets.
5. **Cost-saving tips**
   - **Nest it yourself** where the service allows (Xometry accepts one nested DXF for family pricing); otherwise order identical parts in one line item.
   - **Material choice:** mild steel is the cheapest per bracket; aluminum costs more per sheet but cuts faster; 4130 only where weight matters.
   - **Skip tapped holes and deburr** from the service; a $15 tap and a flap disc do it at home.
   - **Batch parts across the build** into one order to spread the minimum and shipping; keep a running "next order" list in your CAD project.
   - **Thickness consolidation:** make every bracket 3/16" (one sheet) instead of mixing 1/8" and 3/16"; fewer material changes, better price breaks.
   - **Avoid tight tolerances and cosmetic finishes** in the quote; they are the two biggest multipliers.
6. **Order a test part first** when a fit matters (axle bore, bearing pocket); a $10 coupon saves a $200 re-order.
7. **On arrival:** measure the first part against the drawing before cutting into the next step; report out-of-tolerance parts within the service's window (usually 7-30 days).

---

## 12. International options (non-US readers)

- **UK / EU:** [Fractory](https://fractory.com/frequently-asked-questions/) - instant laser/bend/tube/CNC quotes, no minimum, delivery in ~9 days (Estonia/UK network). [Xometry Europe](https://xometry.eu/en/) - instant DXF/STEP quotes, laser, bend, CNC, 3DP across ~600 EU partners. **Laserhub** (laserhub.com, Germany, link not verified) - laser, bending, tube laser and turning for DE/AT/FR/BE/LU. [Protolabs Network](https://www.hubs.com/help-center/how-to-get-a-quote/) ships across Europe.
- **Canada:** SendCutSend and OSH Cut ship to Canada (duties apply); local laser shops are plentiful in Ontario/Quebec/Alberta.
- **Australia / NZ:** search "online laser cutting instant quote" + country; several national services exist but were not verified here.
- **Anywhere:** JLCCNC, JLC3DP, PCBWay, RapidDirect and Craftcloud ship worldwide from China or via local partners; budget 1-3 weeks and import fees. McMaster-Carr sells internationally only through an account; Bolt Depot and Metals Depot are US-only.
- Tube and plate stock: buy locally everywhere; shipping steel across borders costs more than the metal.
