# 12 - Suspension Options

The rest of this repo assumes a rigid frame. This section is for the builder who wants to know
what suspension would cost in complexity, parts, weight and money before deciding. Links were
checked against search indexes in November 2026; resources whose page could not be confirmed are
named in words only. Prices are late-2026 approximations; figures marked *(est.)* are estimates.

> **Heavy-driver notes**
> - Almost every kart shock you can buy (Yerf-Dog, Manco, Hammerhead/TrailMaster 150cc, the
>   generic 10-14" "buggy shocks" on eBay/Amazon) is a captive-spring unit sized for a ~150 lb
>   rider on a ~350 lb all-up kart. At 250 lb the rear sprung mass is roughly 40-50% higher, so the
>   same shock sits deep in its stroke, bottoms on every bump and the (usually ~3") stroke *(est.)*
>   is gone before the bump stop is reached.
> - **Spring rate must scale with sprung mass.** To keep the same ride frequency and the same sag,
>   wheel rate goes up in direct proportion to the sprung weight on that corner. A spring picked for
>   a 150 lb driver is wrong for you by about the same ratio; see the worked example below.
> - Suspension adds **~30-60 lb** and **~$300-900** *(est.)* to a kart that is already ~450 lb
>   with you in it. Every pound of swingarm, axle and shock on a 420cc kart is also weight the
>   brakes and the 40-series torque converter have to deal with.
> - The usual DIY rear is an **unsprung live axle in a pivoting swingarm**. It is the only layout
>   that keeps the #40/#420 chain drive, the 1.25" live axle, the hubs and the disc brake you already
>   designed. Independent rear suspension means CV axles or a differential: a different project.
> - The cheap alternative is to stay rigid, run the biggest low-pressure tires that fit (see
>   `01-design-fundamentals` and `06-wheels-tires-axle-seat`) and buy a **suspension seat**
>   (PRP GT/S.E. extra-wide, RST). For yard and trail use at 10-30 mph this gets most of the comfort
>   for a quarter of the work.
> - A good reality check on cost and complexity: Motor1, "Go-Kart Suspension Is Hard",
>   https://www.motor1.com/features/711972/go-kart-suspension-is-hard/ (you end up building
>   real car suspension, just smaller).

---

## 1. Decision table

| | **A. Rigid + big tires + suspension seat** | **B. Rear swingarm only** | **C. Front A-arms (or trailing arms) only** | **D. Full suspension** |
|---|---|---|---|---|
| Layout | Frame as drawn in `02`; 18-22" low-pressure rear tires at 4-8 psi; suspended seat | Live axle carried in a trailing swingarm pivoting on the frame, 1-2 coilovers | Double A-arms with spindle uprights (buggy style) or leading/trailing links; rigid rear | Swingarm (or independent) rear + double A-arm front |
| Wheel travel | 0 (tire deflection ~0.5-1") | 4-6" rear | 3-5" front | 4-8" both ends |
| Complexity | None beyond the base build | Moderate: one pivot, one crossmember, two shock mounts, chain tension through travel | High: 4 arms, 8 pivots, 2 uprights, 2 shocks, steering geometry that moves | Highest; two systems that both change the frame |
| Extra parts | Suspension seat; tires if not already big | Swingarm tube, pivot bolt + bushings, 2 shocks, spring tensioner, brackets, bump stops | 4 A-arms, heims/bushings, 2 uprights with kingpins or ball joints, 2 shocks, revised tie rods | Everything in B and C |
| Approx. cost *(est.)* | $250-900 (mostly the seat) | $200-750 | $300-800 | $600-1,500 |
| Added weight *(est.)* | +10-25 lb (seat) | +25-40 lb | +20-30 lb | +45-70 lb |
| Pros at 250 lb | Cheapest, no new failure points, no geometry to get wrong | Takes the big hits where the weight is (60% rear); keeps the live axle and chain drive | Steering input stays calmer over bumps | Best ride; the kart becomes a small buggy |
| Cons at 250 lb | Still a rigid kart; seat alone cannot absorb 6" holes | Must re-spring (stock shocks bottom); chain and brake routing move; engine mount area needs a crossmember | Rare on its own; stock buggy A-arm kits are light-duty; bump steer must be designed out | Cost, weight, time; braking/accelerating pitch needs real geometry work |
| Pick it if | First build, budget under $2,500, yard/trail at modest speed | You want one upgrade that matters and can live with a rigid front | You already own A-arm/spindle parts (Spiderbox, 150cc buggy) | You are really building a mini-buggy and accept a second winter in the shop |

Recommendation for this repo's baseline kart: build **A** first; design the rear of the frame so **B**
can be added later (leave 14-18" behind the seat hoop free, and put the engine/TC on a crossmember
that can carry a pivot).

## 2. Rear swingarm design

**Layout.** Two arms of tube joined by a crossmember near the axle (an "H" or triangulated "A" in
plan), a pivot cross-tube at the front, and the 1.25" live axle in flange or pillow-block bearings
bolted to the crossmember. Arm length (pivot to axle) 14-20". Shocks from the arms up to a hoop or
tower behind the seat. The wider the pivot (ideally the full frame width, 20"+ between the ears) the
better it resists the twist a live-axle swingarm sees in corners.

**Pivot placement and chain growth.**
- Ideal: pivot **concentric with the jackshaft** (or with the torque converter driven-pulley shaft
  if you can mount the TC output on the pivot axis). Then the center distance from drive sprocket to
  axle sprocket never changes and chain tension is constant through travel. This is the trick behind
  Montesa's constant-chain-tension motocross frames:
  https://motocrossactionmag.com/forgotten-motocross-tech-montesa-constant-chain-tension-cct-jackshaft
  (jackshaft on the swingarm pivot; the article explains why it works).
- Factory 150cc buggies (Hammerhead, TrailMaster) do it the other way: the GY6 engine/CVT hangs on a
  link and moves with the rear end, so the chain stays tight but the whole engine is unsprung
  (the "engine mount link" is also the chain tensioner:
  https://www.gopowersports.com/engine-mount-link-for-150cc/). **Do not copy this with a 420cc plus
  torque converter**; that is ~75 lb of unsprung engine and it kills the suspension.
- If the pivot is offset from the drive sprocket by a few inches, expect roughly 1/4-3/4" of chain
  length change over 30° of swing *(est.)*. Tension the chain at the point of travel where the
  sprocket centers are farthest apart (usually near full compression), and add a **spring-loaded
  idler/tensioner** on the slack run with at least 1" of take-up. A fixed tensioner will either go
  tight and snap the chain at full bump or throw it at full droop.

**Tube.** 1.25" x 0.120" DOM for the arms and pivot cross-tube (1.5" x 0.120" if the arm is over 18"
or you are running a single shock). 1.25" x 0.095" is adequate for the rigid frame but a swingarm
sees the whole rear weight as bending at the pivot plus chain pull; go up a wall thickness. Gusset
the pivot ears and the shock mounts with 3/16" plate.

**Pivot bushings vs bearings.**
- Simplest and best for the money: a 5/8" or 3/4" **grade 8 bolt** through a DOM sleeve welded into
  the pivot tube, running in **UHMW or oil-impregnated bronze (Oilite) bushings** with steel thrust
  washers. Oscillating ±15° does not need a ball bearing. Bushings are ~$10-30 a pair and replaceable.
- Sealed ball bearings (6203/R-series in a housing) work but brinell under oscillating shock loads and
  cost more; use them only if you want zero play and will check them yearly.
- Either way the pivot bolt is in double shear, torqued, and nylocked. Do not hang a pivot off a
  single ear.

**Shock mounting, motion ratio and angle.**
- Motion ratio MR = shock travel / wheel travel = (pivot-to-shock-mount distance / pivot-to-axle
  distance) x cos(shock angle off perpendicular to the arm). Mounting the shock at 70% of the arm
  length, within 20° of perpendicular, gives MR about 0.65-0.7.
- Wheel rate = spring rate x MR². A 0.7 ratio means the spring sees only 49% of the wheel rate; the
  shock also has to stroke MR x wheel travel (4.2" of stroke for 6" of travel at 0.7).
- Keep the shock within 20-30° of perpendicular to the swingarm at ride height. Laying it flatter
  reduces MR, side-loads the shaft and wears the bushings.
- Two shocks (one per side) share the load and resist twist; a single centered shock needs a stiffer
  swingarm and roughly double the spring rate per the math below.

**Anti-squat basics.** At ride height, angle the swingarm so the pivot sits slightly above the axle
(arm sloping down 5-10° toward the rear). Under acceleration the chain pull and the arm angle then
push the rear up a little instead of letting it squat into its travel. A pivot well below the axle
does the opposite: the kart squats under throttle, the chain pulls the suspension down, and you lose
travel exactly when you hit the whoop. The NAU and WPI Baja reports in section 6 walk through the
geometry with diagrams.

**Reference designs (what the factory karts do).**
- **Yerf-Dog Spiderbox 150cc**: double A-arm front with 9-3/4" eye-to-eye shocks
  (https://www.gopowersports.com/9-75-front-shock-yerf-dog-spiderbox-150cc/), live-axle swingarm rear
  with the GY6 engine on the frame. The stock arm bends under hard use; BDX's heavy-duty replacement
  swingarm ($399.99, pre-order at time of writing) tells you the stock tube is too light:
  https://reach.dog/shop/bdx-performance/products/bdx-heavy-duty-yerf-dog-spiderbox-swing-arm
- **Yerf-Dog 3203 / Manco Scorpion class**: 12" eye-to-eye, 10 mm eye shocks on a short swingarm:
  https://monsterscooterparts.com/collections/yerf-dog-3203/products/adjustable-shocks-for-go-karts-mini-bikes-12-eye-to-eye-12-mm-id-set-of-2
- **Hammerhead / TrailMaster 150 XRX/XRS**: rear shock part 6.000.006, 345 mm (13.5") eye-to-eye,
  $44-52: https://hammerheadperformance.com/rear-shock ; the MudHead and Hammerhead fronts use 325 mm
  (12-3/4") units:
  https://monsterscooterparts.com/products/12-3-4-325-mm-adjustable-shock-with-10-mm-eyes-for-150cc-250cc-hammerhead-go-karts-set-of-2
  (reviewers report these bending on 212cc karts; treat as 150 lb-rider parts).
- **TrailMaster Mid XRX (6.5 hp class)**: chain-drive live axle in a swingarm with 8-5/8" shocks:
  https://www.gopowersports.com/shock-8-625-mid-s
- **GoPowerSports Mega Moto 212 rear swingarm kit**: a bolt-on mini-bike swingarm; useful to see how a
  commercial pivot and tensioner are packaged, not as a kart part:
  https://gopowersports.com/mega-moto-212-rear-swing-arm-kit

## 3. Front options

- **Double A-arm with spindle uprights** (what every buggy and Baja car uses). Upper and lower arms
  on bushings or 5/8" heims, an upright carrying the kingpin or two ball joints, the spindle on the
  upright, shock from the lower arm to the frame. The 150cc buggy A-arm/spindle kits ($150-300 a
  side) are light; for 250 lb make the arms from 1" x 0.120" DOM, use 3/4" heims or 5/8" ball joints,
  and re-use Spiderbox/Manco-type kingpin uprights or fabricate 3/16" plate uprights. Camber and
  caster now change through travel; keep the arms near-parallel and near-equal length for a kart.
- **Trailing-arm or leading-link front**. One pivot per side, the spindle on the end of the arm, a
  shock from the arm to the frame. Cheap and what mini-bike "leading link" kits do, but caster changes
  with every inch of travel and the arm sees the full braking torque. Not recommended for a 450 lb kart.
- **Why rigid front + swingarm rear is a reasonable compromise**: 60% of the weight is on the rear,
  the big impacts come through the rear tires, the front already runs on the tire sidewall, and a
  rigid front keeps the Ackermann and bump-steer work in `04-steering` valid. Most DIY swingarm karts
  on the forums are built this way.

## 4. Shocks and springs

**What hobbyists can actually buy.**

| Source | Typical eye-to-eye / stroke *(est.)* | Price *(est.)* | Notes |
|---|---|---|---|
| Chinese kart/buggy shocks (GoPowerSports, Monster Scooter Parts, BDX, eBay) | 8-5/8", 9-3/4", 11", 12", 12-3/4", 13-1/2"; ~2-3.5" stroke | $17-55 each | Captive non-standard springs sized for ~150 lb riders; preload collar only. Catalog: https://www.gopowersports.com/all-go-kart-parts/front-and-rear-end-suspension/150-250-300/ ; softer-sprung 150cc rear: https://bdxperformance.com/products/go-kart-150cc-rear-shock |
| [BMI Karts](https://www.bmikarts.com/) | similar range | $20-60 | Carries the same classes of mini-bike/kart shocks; check their suspension category. |
| ATV/UTV take-off shocks (eBay, Marketplace) | 14-18" eye-to-eye, 3-5" stroke | $40-150 a pair used | Sport-ATV rears are sprung for a 400-600 lb machine plus rider: often the right ballpark. Check the eye width and whether the spring is a 2.5" ID coilover or captive. |
| Fox / Elka / Works premium coilovers | 2.0" body, 6-10" stroke, 2.5" ID springs | $400-1,200 a pair new | Elka 2026 off-road catalog (2.0/2.5/3.0 bodies, springs sold separately): https://www.elkasuspension.com/wp-content/uploads/2026/03/ELKA-OFF-ROAD-SHOCKS_CATALOGUE-LAUNCHCAMPAIGN.pdf ; Fox line explained: https://www.utvsource.com/blog/fox-racing-shocks-ultimate-buyers-guide/ ; IFP vs remote reservoir vs piggyback: https://www.atv.com/buyers-guide/2015-atv-and-utv-shocks-buyers-guide-2415.html |
| Bicycle / motorcycle shocks | - | - | **Avoid.** Bicycle shocks are 1-2" stroke air units rated for 200 lb total. Motorcycle rear shocks are built for a linkage with MR 0.3-0.5 and 1,000+ lb/in springs; on a direct-acting swingarm they are far too stiff and the wrong length. |

**Terms.** *Eye-to-eye* is the extended length between mount centers; *stroke* is how far it
compresses; *compressed length* = eye-to-eye minus stroke. *Spring rate* is in lb/in. *Preload* is how
much the spring is compressed at full extension; it changes sag, not rate. On a linear spring every
turn of preload adds (thread pitch x rate) of force.

**Design procedure.**
1. Sprung corner weight W (lb) = axle weight minus unsprung weight (axle, hubs, wheels, tires,
   brake disc, swingarm) divided by number of shocks on that end.
2. Wheel rate from a target ride frequency f: `WR = W / 386.4 x (2*pi*f)^2` (lb/in).
   Off-road targets: ~1.5-2.5 Hz; see Penske's ride-frequency note,
   https://www.penskeshocks.com/blog/natural-frequency-ride-frequency-cpm-in-race-suspension
   (dirt late models and sprint cars also sit in that band). OptimumG's "Springs & Dampers" Tech
   Tips give the same derivation; the official PDF link could not be confirmed, search the title.
3. Check static sag = W / WR. Target **25-33% of wheel travel**. On a 4-6" travel kart the sag
   target is usually the binding constraint and pushes you toward the stiff end of the band.
4. Spring rate = WR / MR². Buy the nearest stock rate. Required stroke = MR x wheel travel.

**Worked example: 450 lb kart, 60% rear, 0.7 MR swingarm, two shocks, 6" travel.**
- Rear axle weight 270 lb; unsprung rear (1.25" axle, hubs, 2 x 18" tires/wheels, disc, swingarm)
  ~70 lb *(est.)*; sprung rear 200 lb; W per shock = 100 lb.
- Pick sag 1.8" (30% of 6"): WR = 100 / 1.8 = **55 lb/in** at the wheel.
- Ride frequency check: f = (1/2pi) x sqrt(55 x 386.4 / 100) = **2.3 Hz**. In band.
- Spring rate = 55 / 0.7² = **112 lb/in** per shock; buy 110-125 lb/in, 2.5" ID, 8-10" free length.
- Stroke needed = 0.7 x 6" = 4.2"; most $40 kart shocks have ~3" *(est.)*, so this example needs an
  ATV take-off or a 2.0" coilover with 4-5" of stroke.
- Spring force at full bump = 112 x 4.2 + preload ≈ 470-520 lb per spring; the mounts and the pivot
  see this plus the dynamic hit, which is why the brackets get 3/16" gussets.
- Same kart with one centered shock: W = 200 lb, WR = 110 lb/in, spring 225 lb/in.
- For a 150 lb driver the same kart would want ~80 lb/in springs. That 40% gap is the whole
  "stock shocks bottom out" problem.

`calculators/spring_rate.py` in this repo does these steps; run it with your own numbers, e.g.
`python3 calculators/spring_rate.py --sprung-weight 200 --shocks 2 --spring-rate 112 --motion-ratio 0.7 --shock-angle 0 --travel 6`
to print wheel rate, static sag and ride frequency (sprung weight is per axle; the script divides by the shock count, and a non-zero shock angle lowers the effective motion ratio).

**Progressive vs linear.** Linear springs make the math above true and are what you want on a
short-travel swingarm; sag and bottoming are predictable. Progressive (variable-pitch) springs feel
soft at ride height and ramp up near full bump, which is nice on a 150cc buggy with too little
travel but makes the sag target hard to hit and the rate hard to tune. If you want a progressive
feel, stack a short soft "tender" spring on top of a linear main spring with a slider.

**Where to buy 2.5" ID coilover springs ($60-100 each).**
- Summit Racing, all coilover springs filterable by rate/length/ID:
  https://www.summitracing.com/search/part-type/coilover-springs ; Eibach line:
  https://www.summitracing.com/search/product-line/eibach-coilover-springs
- Speedway Motors, Eibach 8" x 2.5" ID 250 lb/in as an example listing:
  https://www.speedwaymotors.com/Eibach-0800-250-0250-Coilover-Spring-250-lbs-in-2-5-ID-8-in-,325848.html
- Jegs, QA1 high-travel 10" springs (lifetime warranty):
  https://www.jegs.com/i/qa1-122-10ht150b-powder-coated-high-travel-coil-spring-10-in-length
- QA1 direct, 8" x 2.5" ID 250 lb/in: https://qa1.net/products/chrome-coil-spring-8in-2-1-2in-id-250lbs-in/
- Hyperco standard 2.5" ID (rates from 85 lb/in up): https://springrates.com/products/hyperco-standard-coilover-spring-id-2-5
  and e.g. the 8" x 200 lb/in: https://jj-motorsports.com/coil-over-spring-2-5in-id-8in-tall-hyp188b0200
- Note: these fit 2.0" coilover bodies (Fox, Elka, QA1, many ATV shocks). The $40 kart shocks use a
  captive spring of odd ID; changing their rate usually means changing the shock.

## 5. Plans and reference builds with suspension

| Resource | Link | One-line note |
|---|---|---|
| SpiderCarts Arachnid (independent front, swingarm rear, 18" tires) | review at https://www.buildyourownracecar.com/spidercarts-arachnid-full-suspension-go-kart-plans-how-to-build-a-go-kart/ ; plan page is linked in `11-plans-builds-community` | Only hobby plan with full suspension; shocks are spec'd for a light driver, re-spring per section 4. |
| SpiderCarts Tarantula (rear suspension) | https://spidercarts.com/tarantula-go-kart-plans/ | Exists as a SpiderCarts plan; one builder's thread with the plan drawing and motor-mount problems: https://www.diygokarts.com/community/goto/post?id=224437 |
| DIY Go Karts: Photos of Arachnid | https://www.diygokarts.com/community/threads/photos-of-arachnid.45569/ | Finished Arachnids; shows swingarm, shock towers and what people changed. |
| DIY Go Karts: looking for rear swing-arm suspension designs | https://www.diygokarts.com/community/threads/looking-for-rear-swing-arm-suspension-designs.19720/ | Sketches and opinions on pivot placement and shock mounting for live-axle swingarms. |
| DIY Go Karts: how do I place my suspension for a rear swing arm setup? | https://www.diygokarts.com/community/goto/post?id=643678 | Motion ratio and shock angle question answered with numbers. |
| DIY Go Karts: Full Suspension Big Block Mini-Buggy Build | https://www.diygokarts.com/community/goto/post?id=573487 | 420/460cc-class swingarm buggy; shows why the engine sits high to clear the arm at full bump. |
| DIY Go Karts: Viper off-road with full suspension project log | https://www.diygokarts.com/community/threads/viper-offroad-with-full-suspension-project-log.3231/ | Older full-suspension log already cited in `01`. |
| DIY Go Karts: designing a 4-trailing-arm go-kart | https://www.diygokarts.com/community/threads/designing-a-4-trailing-arm-go-kart.7633/page-2 | Why a solid axle with independent trailing arms does not work; pick swingarm or go fully independent. |
| DIY Go Karts: IRS rear plans or ideas / suspension ideas | https://www.diygokarts.com/community/threads/irs-rear-plans-or-ideas.1292/ and https://www.diygokarts.com/community/threads/suspension-ideas.24570/ | Independent-rear discussion; read before deciding against swingarm. |
| DIY Go Karts: shock absorbers (travel vs spring rate) | https://www.diygokarts.com/community/goto/post?id=100675 | "More travel is useless if you sit on the bump stops": the heavy-driver problem in one thread. |
| Eng-Tips: long-travel off-road go-kart suspension | https://eng-tips.com/threads/long-travel-off-road-go-kart-suspension.166487 | Engineers discussing geometry for a long-travel kart. |
| Grassroots Motorsports: motorcycle-powered kart question | https://grassrootsmotorsports.com/forum/sprockets/motorcycle-powered-kart-question/65178/page1 | Warning on putting the engine on the swingarm (unsprung weight). |
| kartbuilding.net | *no suspension content found in search* | Its free off-road plan is rigid; use it for the frame and add the swingarm from this section. |
| Red Beard's Garage | channel link in `11-plans-builds-community` | The 670cc off-road kart build shows a rear swingarm; the specific video could not be confirmed by search, browse the channel for the off-road kart series. |
| Cars and Cameras | channel link in `11-plans-builds-community` | Several suspended buggy/kart builds and plenty of "what broke" footage; no single video confirmed by search. |
| NAU Baja team 19 engineering analysis (2014) | https://sce.nau.edu/capstone/projects/ME/2014/SAE-MiniBaja/team_19/team_19-engineering-analysis-report.pdf | Double A-arm front vs 3-link trailing-arm rear with loads and geometry. |
| NAU Baja suspension progress report (2015) | https://ceias.nau.edu/capstone/projects/ME/2015/SAE-MiniBaja/suspension/Suspensions_progress_report.pdf | Spring/damper selection and travel targets. |
| NAU Baja front-end preliminary report (2018) | https://www.ceias.nau.edu/capstone/projects/ME/2018/SAEBaja/documents/frontendprelim.pdf | Front A-arm and steering geometry (Ackermann, bump steer). |
| NAU Baja rear-end poster (2024) | https://sce.nau.edu/capstone/projects/ME/2024/F23toSp24_Baja24/files/RearEndCapstonePoster.pdf | Trailing-arm rear with camber links; axle-path and link-length targets. |
| WPI Baja SAE MQP (2017) | https://digitalcommons.wpi.edu/mqp-all/2824/ | Chassis + suspension design with FEA; double A-arm front, trailing arm rear. |
| WPI Design and Optimization of a Baja SAE Vehicle (2016) | https://digitalcommons.wpi.edu/mqp-all/2815 | Modifying an existing car's suspension and steering; good "what we changed and why". |
| Kettering: suspension and chassis redesign of the 2020 Baja vehicle | https://digitalcommons.kettering.edu/graduate_theses/3 | Thesis-level geometry validation (ADAMS/Ansys); heavier reading. |

The Baja reports are the best free material on this subject: they are written for 400-500 lb
vehicles with 200 lb drivers and real wheel travel, which is closer to your kart than any hobby plan.

## 6. Checklist before cutting

- [ ] Travel vs ground clearance: at full compression the frame, engine, exhaust and seat pan still
      clear the ground and the tires clear the frame; at full droop the chain and shocks are not the
      travel limiters.
- [ ] Bump stops: rubber or polyurethane stops on the frame that the swingarm hits **before** the
      shock bottoms metal-to-metal.
- [ ] Chain: measured center-distance change from full droop to full compression; spring tensioner
      with take-up to match; chain guard still covers the run at both extremes.
- [ ] Brake line / cable: routed along the swingarm with a loop at the pivot; no pull at full droop,
      no pinch at full bump.
- [ ] If the front is suspended: tie rods checked for bump steer through the whole travel (see
      `04-steering`); ball joints or heims at both ends.
- [ ] Shock mounts: double-shear tabs, 3/16" plate, gusseted to a crossmember or hoop, not to a
      single tube wall.
- [ ] Pivot: grade 8 bolt in double shear, bushings with thrust washers, nylock nut, torqued.
- [ ] Springs: rate from the worked example or `calculators/spring_rate.py`; sag measured with you in
      the seat at 25-33% of travel before the first ride.
- [ ] Weight and CG worksheet in `templates/` updated for the added 30-60 lb; brake sizing in
      `05-brakes` rechecked.
