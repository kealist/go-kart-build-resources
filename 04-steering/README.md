# 04 – Steering (spindles, geometry, tie rods, shaft, wheel)

## Heavy driver notes (250 lb driver, ~400–450 lb all-up)
- Front axle load on a rear-engine single-seater is roughly 35–40% of total, so each spindle is carrying ~80–90 lb static and 2–3x that over a bump or in a hard turn. The common 5/8" x 4-1/2" "yard kart" spindle with a 1/2" kingpin bolt is sized for a 150 lb kid on grass. Go up a size.
- **Recommended:** spindles with a **3/4" or 5/8" kingpin on a bronze/needle-bushed pivot**, a **5/8" spindle shaft minimum**, and welded (not bolted) spindle brackets. If you run 8" wheels and go off-road, 3/4" spindle shafts with matching 3/4" bore front hubs are worth the extra ~$40.
- Steering effort goes up with front weight and tire width. Keep caster modest (6–10°), use a 12–13" wheel, and keep the pitman arm short enough that lock-to-lock is ~3/4 turn; you do not want to muscle a 450 lb kart through a 1/4-turn-lock steering box.
- Tie rods: 3/8"-24 rod ends with 3/8" OD tube or solid rod. 5/16" is the kid-kart size; it bends when a 250 lb driver clips a root.
- Bump steer matters more because you will compress the (non-suspended, but still flexing) frame and tires further; follow the tie-rod layout rule below.

## Spindle kits – what the sizes mean
| Spec | Light-duty (typical kit) | Recommended for you |
|---|---|---|
| Kingpin (pivot bolt) | 1/2" Grade 5 bolt in a 1/2" hole | 5/8" or 3/4" bolt, bushed; Grade 8 |
| Spindle shaft (what the wheel bearing rides on) | 5/8" x 4" | 5/8" x 4-1/2" to 5" (6" wheels) or 3/4" (8" wheels, off-road) |
| Bracket | 3/16" flat, bolt-on | 1/4" plate, weld-on, with kingpin boss |
| Steering arm hole | 5/16" | 3/8" (rod end bolt) |
| Price per pair with brackets | $35–60 | $60–120 |

- Buy spindles and brackets as a matched set; the bracket sets caster and kingpin inclination for you (usually 0–10° caster built in).
- Left and right spindles are mirror images – the steering arm must point toward the kart centerline (rearward, inboard) for Ackermann.
- Check that the spindle length leaves room for the wheel hub, a washer each side and a castle nut with a cotter pin. Never run a nyloc alone on a front spindle.

Links:
- GoPowerSports spindle & bracket set – https://www.gopowersports.com/spindle-and-bracket-set/ – the standard 5/8" yard-kart set, shows what a "kit" includes.
- GoPowerSports spindle category – https://www.gopowersports.com/go-kart/steering/spindles/ – browse 5/8" and 3/4" spindle shaft options and Manco/Yerf-Dog replacements.
- DIY Go Karts steering/spindle plans – https://www.diygokarts.com/kart-plans/steering-plan-spindles.html – free drawings for welding your own spindles and brackets.
- Purdue evGrandPrix kart assembly manual (PDF) – https://engineering.purdue.edu/evGrandPrix/event/highschool/Documents/evGP-Kart-Assembly-Manual.pdf – clear photos of spindle, eccentric, tie rod and hub assembly order.
- Point Karting steering hardware – https://pointkarting.com/collections/kart-steering-hardware-components – racing-grade (8 mm / 10 mm metric) spindles and kingpins if you want to go upmarket.

## Ackermann geometry basics
- In a turn the inside front wheel follows a tighter radius than the outside wheel, so it must steer **more**. Ackermann is the linkage geometry that does this automatically.
- Classic rule: draw a line from each kingpin through its steering-arm ball joint; both lines should intersect near the **center of the rear axle** (for 100% Ackermann). For a yard kart, aiming at a point 1.0–1.5x the wheelbase behind the front axle (70–100% Ackermann) is fine.
- Practical result: the steering arms angle inboard by roughly **15–25°** on a 40–45" wheelbase / 30–36" track kart.
- Too little Ackermann (parallel steer) = inside tire scrubs, heavy push in tight turns on grass. Too much = twitchy on pavement. Off-road karts tolerate extra Ackermann well.
- Pitman arm layout: with a single pitman arm driving two tie rods, the tie rod pivots on the pitman arm should be **behind** the steering shaft (toward the driver) and spaced ~2–3" apart. This adds Ackermann and reduces bump steer vs. a single center pivot.

### Laying it out on paper or in CAD (10 minutes)
1. Draw the kart plan view to scale: front track (kingpin to kingpin), wheelbase, rear axle line.
2. Mark both kingpin centers. Mark the rear axle midpoint (or your chosen Ackermann target point).
3. Draw a line from each kingpin to the target point. Your steering arm's ball-joint hole should sit **on that line**, at the arm length you chose (typically 3–4" from the kingpin).
4. Draw the pitman arm circle (radius = pitman arm length, typically 2–3") centered on the steering shaft location. Place the two tie-rod pivots on that circle, behind the shaft.
5. Connect pitman pivots to spindle arm holes = tie rod lengths (straight-ahead). Note them; buy tie rods about 1" shorter and let the rod ends make up the length.
6. **Check it:** rotate the pitman arm 30° and 60° in CAD (or with a cardboard cutout pinned at the shaft) and measure the resulting angle of each spindle. Inside wheel should turn more than outside (e.g., 32° vs 24° at full lock). If the outside turns more, the arms point the wrong way.
7. Compute ideal inner angle for a given outer angle: cot(δi) = cot(δo) − track/wheelbase. Compare with what your linkage gives at 20° outer; within ~3° is good for a yard kart.
8. Check lock: at full lock neither tie rod should pass "over center" (go straight in line with the pitman arm) – that is the binding/lock-up failure. Keep at least 15° between tie rod and pitman arm at full lock.

Links:
- Kart360 "Learning Ackermann" – https://kart360.com/learn/steering-adjustment-basics/ackermann – how arm hole position changes Ackermann.
- TKART Ackermann toolbox – https://www.tkart.it/en/toolbox/ackermanns-steering-geometry/ – diagrams of the inner/outer wheel arc.
- KartPulse: "Ackermann is massively misunderstood" – https://forums.kartpulse.com/t/ackermann-is-massively-misunderstood/9347 – racers' nuance, why 100% isn't always the goal.
- DIY Go Karts: reverse Ackermann thread – https://www.diygokarts.com/community/threads/improving-steering-geometry-with-reverse-ackermann-setup.46446/ – what happens when arms point the wrong way.
- Instructables custom kart/ATV steering – https://www.instructables.com/Custom-GoKartATV-Steering – a rack-and-pinion alternative layout.

## Caster, camber, kingpin inclination (typical values for a DIY off-road kart)
| Setting | Typical range | Notes |
|---|---|---|
| Caster (kingpin tilted back at top) | 6–12° (race karts 10–20°) | More caster = more self-centering and inside-wheel lift in turns; more steering effort. For a heavy driver stay ~8°. |
| Kingpin inclination (KPI) (kingpin tilted inboard at top) | 8–12° | Built into the bracket. Helps return-to-center; reduces scrub radius. |
| Camber (wheel tilt) | 0 to −1° (slightly negative) | Yard karts with stub spindles often end up slightly positive under load; aim for 0 at ride height **with you in the seat**. |
| Toe | 0 to 1/8" toe-out (off-road) | Measure at the tire centerline front vs rear with the driver seated. Toe-in makes it wander on grass. |
| Scrub radius | as small as practical | Keep the wheel centerline close to the kingpin axis; wide 8" wheels with big offset make steering heavy. |

- Set everything with the driver's weight on the kart; a 250 lb driver changes front ride height and therefore camber/toe noticeably on a tube frame.

Links:
- Comet Kart Sales: understanding caster and camber – https://cometkartsales.com/blogs/news/understanding-caster-and-camber – plain-language definitions with pictures.
- Kart360 basics of caster and camber – https://kart360.com/features/pro-tip-basics-of-caster-and-camber – effects on handling.
- FlowRacers go-kart camber guide – https://flowracers.com/blog/go-kart-camber/ – how to measure with a straight edge and angle gauge.

## Tie rods and rod ends (heim joints)
- Rod end sizes: **3/8"-24 male rod end, 3/8" ball bore** is the right size for an adult off-road kart. 5/16"-24 is the common kit size and is fine for lightweight karts only. 1/2" is overkill.
- Threads: one end of each tie rod is **left-hand**, the other **right-hand**, so turning the rod adjusts toe without unbolting. Buy LH + RH rod ends and LH + RH jam nuts. Mark the LH end with a groove or paint.
- Tie rod tube: 3/8" solid rod threaded both ends (cheap, bends and stays bent) or 1/2" OD x 0.065" DOM tube with weld-in 3/8"-24 threaded bungs (stiffer, preferred).
- Use a **high-misalignment spacer** or a bent arm so the rod end never binds through steering travel; a rod end run at its misalignment limit wears oval in a season.
- Grade 8 bolts with nyloc nuts through the rod ends; add a large flat washer on the outside of each rod end as a safety retainer in case the ball pops out.
- Price: rod ends $5–9 each, jam nuts $1, tie rod tube/rod $10–15 each. Budget ~$50 for both tie rods.

Links:
- GoPowerSports 3/8" tie rod ends, RH thread – https://www.gopowersports.com/3-8-tie-rod-ends-right-hand-threading/ – 3/8" ball, ~$5.50 each; LH version sold alongside.
- GoPowerSports tie rods category – https://www.gopowersports.com/go-kart-parts/steering/tie-rods-ends/tie-rods – 3/8" generic solid tie rods in common lengths.
- Kart Parts Depot 5/16" bore / 3/8" shank heim – https://kartpartsdepot.com/5_16_Heim_Joint_Bore_with_3_8_Shank_Heim_End_p/sm-hj516with38he.htm – adapter heim so 3/8" rods fit 5/16" spindle arms.
- Kart Parts Depot 3/8" tie rod – https://kartpartsdepot.com/Go_Kart_Steering_3_8_Tie_Rod_p/sm-38tr.htm – LH/RH threaded 3/8" rod.
- Comet Kart Sales tie rods & rod ends – https://cometkartsales.com/collections/tie-rods-rod-ends – racing-grade rod ends, nylon-reinforced tubes.

## Steering shaft, pitman arm, steering wheel hub
- Shaft: **5/8" solid steel** is the standard yard-kart size and is adequate; 3/4" if you weld your own and the shaft is long (>30"). Support it in **two** bearings or bushings (a flange bearing at the dash and a bushing at the pitman end); one bushing lets a heavy driver's arm input flex the shaft.
- Pitman arm: 2–3" between shaft center and tie-rod pivots; weld it or use a splined/keyed arm with a through-bolt. A set-screw-only pitman arm will slip under a 250 lb driver's input.
- Thrust: put a lock collar on each side of the dash bearing so pushing on the wheel can't shove the shaft forward.
- Steering wheel hub: 3-bolt pattern on a 1-3/4" to 2" circle is the small-kart standard; 5/8" splined weld-on hubs (Azusa style) and quick-release hubs are available. Match spline count (Azusa 38-spline vs. others) between shaft and hub.
- Wheel: 12–13" diameter for leverage; a 10" racing wheel makes a heavy kart tiring on grass.
- Steering stops: weld tabs so the spindles stop before the tie rods go over-center and before the tire hits the frame.

Links:
- GoPowerSports 28" steering shaft kit (shaft, collars, two pitman arms) – https://www.gopowersports.com/steering-shaft-kit/ – note it is NOT spline-compatible with Azusa 8134.
- GoPowerSports steering shaft with pitman arm (3/4" shaft, 5/8" stem) – https://www.gopowersports.com/steering-shaft-w-pitman-arm/ – heavier shaft; needs cutting and a welded hub coupler.
- GoPowerSports pitman arm AZ8129 – https://www.gopowersports.com/pitman-steering-arm/ – 5/8" shaft hole, 5/16" tie rod holes (drill to 3/8" if you upsize rods).
- Comet Kart Sales Azusa 5/8" splined steering shaft kit – https://cometkartsales.com/products/azusa-splined-steering-shaft-kit – genuine Azusa, splined for a matching hub.
- Comet Kart Sales Azusa 5/8" splined steering wheel hub – https://cometkartsales.com/collections/all/products/azusa-5-8-splined-steering-wheel-hub-1 – 3-bolt hub for the kit above.
- MFG Supply Azusa steering kit with pitman arms (AZ1873) – https://www.mfgsupply.com/az1873.html – alternate source, lists kit contents.
- Speedway Motors 5/8" quick-release hub – https://www.speedwaymotors.com/Pin-Style-Quick-Release-Aluminum-Steering-Wheel-Hub-5-8In-Steel-Shaft,29001.html – quick-release makes a tight cockpit easier for a large driver.
- GoPowerSports complete steering kit – https://www.gopowersports.com/go-kart-steering-kit-complete/ – one-box option; check its 5/16" rod ends against the sizing advice above.

## Bump steer (and why it bites on a stiff-frame kart)
- Bump steer = toe change as the front end flexes or a wheel rides over a bump. Cause: the tie rod does not swing on the same arc as the spindle/frame relationship.
- Rule of thumb for a rigid (no-suspension) kart: make each **tie rod parallel to the ground and roughly parallel to the line from the kingpin to the pitman pivot** when viewed from the front and from above. Tie rods angled steeply up or down to reach a high pitman arm are the usual mistake.
- Keep the pitman arm at the same height as the spindle steering arms; drop the steering shaft or bend the arms down rather than running tie rods uphill.
- Test: with the kart on the ground and you in the seat, measure toe; then have a helper push down hard on the front bumper. Toe change > 1/16" means fix the geometry.

## Pre-ride steering checklist
- Kingpin bolts torqued, cotter-pinned or nyloc'd, spindles pivot freely with no vertical slop (> 1/32" slop = add a shim washer).
- Rod end jam nuts tight, safety washers on the outside of every rod end, LH end marked.
- Lock-to-lock: no tie rod goes over-center, tires don't touch frame, pedals or feet at full lock.
- Toe re-measured with the driver seated; bump-steer push test passed.
- Steering wheel hub bolts (3) torqued; shaft collars tight; shaft can't move fore/aft.
- Front wheel nuts castle-nutted and pinned; bearings spin freely, no rock on the spindle.
- After the first hour of riding, re-check every item above – new weld-on brackets and fresh rod ends settle.

## Where to buy (summary)
- GoPowerSports – spindles, shafts, pitman arms, rod ends (links above).
- Comet Kart Sales / Point Karting / Kart Parts Depot – Azusa and racing-grade pieces (links above).
- [BMI Karts](https://www.bmikarts.com/) – spindle and steering kits, weld-on brackets; browse the steering category.
- [OMB Warehouse](https://www.ombwarehouse.com/) – steering shafts, hubs and wheels; see the steering category.
- Kartfab – free plans whose steering drawings use the standard 5/8" spindle/pitman layout; search "KartFab go kart plans".
