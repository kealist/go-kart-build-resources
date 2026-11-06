# Calculators

Small, dependency-free Python 3 scripts for the back-of-envelope checks you should do
before buying tube or ordering parts. Every default is set for a ~250 lb driver and
a ~450 lb all-up kart. Run any script with `--help` for all flags.

| Script | What it answers |
|---|---|
| `gear_ratio.py` | Top speed, launch force, max climbable grade for a given engine / torque converter / sprocket / tire combination. `--target-mph` suggests sprocket sizes. |
| `brake_sizing.py` | Brake torque and caliper clamp force for a target deceleration, traction limit for rear-only brakes, hydraulic pedal effort, stopping distance. |
| `frame_tube_check.py` | Bending stress, factor of safety and deflection for common round/square tube sizes under the driver's weight at 2-3 g shock load. |
| `axle_check.py` | Combined bending + torsion on a 1 in vs 1.25 in keyed live axle with a keyway stress concentration. |
| `chain_check.py` | Chain tension vs. strength for #35 / #40 / #41 / #420 chain at launch torque. |
| `spring_rate.py` | Wheel rate, static sag, ride frequency and bottom-out g for a coilover swingarm or A-arm; solves the spring rate for a target sag. |

Quick start:

```bash
python3 gear_ratio.py --engine 420 --target-mph 32
python3 brake_sizing.py --weight 450 --mph 30
python3 frame_tube_check.py --driver 250 --g 3 --span 26
python3 axle_check.py --overhang 5
python3 chain_check.py --chain 420
python3 spring_rate.py --sprung-weight 230 --shocks 2 --motion-ratio 0.7 --target-sag 0.30
```

These are hand calcs with stated assumptions, not FEA and not a substitute for a
test ride at walking pace with a helmet on. Material strengths are typical minimums;
your steel supplier's mill certificate is the real number.
