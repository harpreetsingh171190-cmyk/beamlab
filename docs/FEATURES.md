# BeamLab — Detailed Feature Log & Engineering Notes

## Browser app features
- Simply supported and cantilever beams.
- Centre point load and full-span uniformly distributed load (UDL).
- Section inertia input or cross-section calculator for solid rectangle, solid circle and hollow circle.
- Maximum deflection, deflection ratio, selected reference limit checks (L/250, L/360, L/500), and status indication.
- Responsive beam schematic, Shear Force Diagram (SFD) and Bending Moment Diagram (BMD).
- Analytics dashboard with deflection-vs-load graph, bending-stress utilization bars, side-by-side simply-supported vs cantilever comparison table, and comparison CSV export.
- Dedicated Support Reaction Calculator: reactions at A/B for the selected idealized beam/load cases.
- Bending Stress Calculator: maximum bending moment, section modulus, elastic bending stress (σ = Mc/I = M/S), user-entered material yield strength (Fy), calculated yield-based Factor of Safety (FoS = Fy / bending stress), a configurable target FoS (default 1.5), separate PASS/FAIL checks for stress versus yield strength and calculated FoS versus target, and CSV export of these checks. The target is an educational screening value, not a universal design-code requirement.
- Educational load combinations: single load, 1.2D + 1.6L, 1.2D + L + W, and 0.9D + W.
- Typical material library values for steel, aluminium, concrete, timber and stainless steel, editable through Young's modulus.
- A 20-element 1D Euler–Bernoulli beam FEM numerical comparison against the closed-form deflection.
- Formula display, recent history in this browser, CSV export, and print / Save as PDF.
- Works offline in a modern browser; no API key or Python required for the browser calculator.

## Start
Open `index.html` in a modern browser.

## Python toolkit
Install packages with `python -m pip install -r requirements.txt`, then run `python python/beam_ml_analysis.py`.
Optional deep learning: `python python/beam_deep_learning.py`.
Optional image preprocessing: `python computer_vision/beam_crack_inspection.py path/to/beam_image.jpg`.

## Engineering limitations
The browser calculator uses:
- Simply supported centre point load: δmax = PL³/(48EI)
- Cantilever end point load: δmax = PL³/(3EI)
- Simply supported full-span UDL: δmax = 5wL⁴/(384EI)
- Cantilever full-span UDL: δmax = wL⁴/(8EI)

Section formulas: rectangle I = bh³/12; solid circle I = πd⁴/64; hollow circle I = π(Do⁴ − Di⁴)/64. Bending stress uses σ = Mc/I; the extreme-fibre distance c is inferred from section dimensions or entered manually for a user-supplied I. The displayed yield-based FoS is a simplified elastic bending check only; it does not account for all structural failure modes or replace a code-based design check.
The L/250, L/360 and L/500 choices are reference checks only, not proof of code compliance. This is a learning/preliminary calculator, not a certified structural design tool. Validate units, assumptions, loads and design requirements with a qualified engineer.

The ML/DL examples are trained on formula-generated synthetic data; model scores do not establish real-world predictive performance. The computer-vision script performs image preprocessing, not reliable crack diagnosis.


## Load combinations and FEM comparison
The load combinations are illustrative only and are not guaranteed to match the user's jurisdiction or structure type. Select combinations and factors required by the applicable design standard. The material library contains typical modulus values, not grade-certified properties.

The FEM comparison is a simple 1D Euler–Bernoulli beam-element model with 20 elements. It is intended as an educational numerical cross-check only, not a full structural FEA package. It omits shear deformation, local stress concentrations, buckling, contact, nonlinear material behaviour, and 2D/3D geometry.


## Additional engineering estimates (latest update)
- Elastic beam slope/rotation estimate in radians and degrees for the supported idealized load cases.
- Simplified yield-limited allowable bending moment and applied-load estimate based on entered yield strength / target FoS and section modulus.
- New outputs are included in CSV/JSON results.

These are educational preliminary estimates, not a code-compliant design. The load-capacity estimate considers bending yield only and does not check deflection, shear capacity, buckling, fatigue, connections, load factors or local effects.


## Latest additions: torsion, combined stress, and material grades

- Torsional shear stress calculator for solid/hollow circular sections, approximate rectangular torsion constant, or user-entered J for manual sections.
- Combined axial + bending + torsional elastic stress screening using a simplified von Mises estimate.
- Expanded illustrative grade selector: S235, S275, S355, S460, ASTM A36, ASTM A572 Grade 50, stainless 304/316, aluminium 6061-T6/6063-T6, and grey cast iron reference entry.
- CSV/JSON reports retain primary beam results; CSV includes combined stress values when calculated.

**Engineering caution:** all grade properties are indicative examples, not guaranteed specifications. Confirm exact product form, thickness, temper, standard, temperature, and datasheet. Cast iron is brittle and does not have one universal yield strength; the included value is only a placeholder and should be replaced with a verified appropriate strength criterion. The combined-stress model is a simplified screening calculation, not a complete code check. For non-circular sections, torsion formulas are approximate; warping, restraint, stress concentrations, buckling, fatigue, and shear-center effects are not modeled.

## Latest update: thermal expansion and fatigue screening
- Thermal expansion calculator using ΔL = α L ΔT, with the expansion coefficient entered in µm/m·°C and free-expansion assumption.
- Modified Goodman fatigue screening using maximum/minimum normal stress, corrected endurance limit, ultimate tensile strength, and a configurable target fatigue FoS.
- Fatigue results are a preliminary infinite-life screening estimate only; the calculator does not predict cycle life or automatically apply Marin factors, stress concentration, surface finish, size, reliability, weld, corrosion, or variable-amplitude corrections.
- Thermal stress is not calculated for restrained expansion. Boundary conditions and restraint stiffness would be needed for that analysis.


## Latest added tools

- **Euler column buckling estimate:** calculates elastic critical load using `Pcr = π²EI/(KL)²`, effective length, buckling factor of safety, and a target-FoS screen for four idealized end conditions.
- **Beam self-weight estimator:** calculates a uniform self-weight load from material density, cross-sectional area, beam length, and gravitational acceleration.
- Both are preliminary educational calculations. Euler buckling does not replace code-based column design, and the self-weight UDL is not automatically applied to the main beam calculation.


## Analytics dashboard update
The browser app now displays a two-support-condition comparison for the selected idealized load case, a deflection response graph over load multipliers from 0× to 2×, and bending-stress utilization against yield and target-FoS allowable stress. The comparison CSV is an educational side-by-side estimate; it does not replace applicable design-code checks.


## Expanded chart dashboard
The dashboard includes deflection vs load multiplier, stress utilization, support-condition comparison, shear force diagram (SFD), bending moment diagram (BMD), deflection shape along the span, bending stress vs load multiplier, and span sensitivity. These charts use simplified ideal beam equations for the selected load/support case and are intended for learning and preliminary checks only. They do not replace code-compliant structural analysis.


## Latest additions
- Symmetric I-section properties from flange width, overall depth, flange thickness and web thickness.
- Hollow rectangular tube properties from outside dimensions and wall thickness.
- Engineering unit converter for length, force, stress/pressure, moment/torque, area, second moment of area, and distributed load.

Section property equations assume ideal, symmetric sections and dimensions in mm. The unit converter uses exact/common conversion factors as listed in the UI. Verify all engineering inputs and design checks against applicable standards.


## Additional engineering tools
- Section modulus, radius of gyration and slenderness estimate based on selected section properties.
- Projected bearing stress screening for pin/plate contact.
- Fillet weld average direct-shear screening using effective throat = 0.707 × leg.
- Simply supported beam with partial-span UDL: support reactions and sampled bending-moment diagram.

These tools are preliminary educational checks, not substitutes for applicable design codes or qualified engineering review.


## Additional engineering tools (latest update)

- Simply supported beam with multiple point loads: reactions and sampled bending-moment diagram.
- Fundamental natural frequency estimate for a uniform simply supported Euler–Bernoulli beam.
- Bolt group direct-shear screening with equal load sharing assumption.
- Thin-walled closed-cylinder pressure-vessel hoop and longitudinal stress screening.

These are educational preliminary calculations, not substitutes for professional design or applicable codes.


## Additional engineering tools (latest update)

- Plane-stress transformation and Mohr's circle: transformed normal/shear stress, principal stresses, maximum in-plane shear and principal angle.
- Power/RPM to shaft torque: solid or hollow circular shaft polar moment, torsional shear stress and allowable-stress ratio.
- Simply supported beam with a linearly varying partial distributed load: reactions and sampled bending-moment diagram using numerical integration.
- Stress-concentration screening: user-supplied Kt, estimated local peak stress and preliminary yield/FoS check.

These are educational/preliminary tools. The stress concentration factor must be sourced from a suitable geometry reference or validated analysis. The varying-load diagram is numerically integrated and sampled; verify critical cases independently.


## Four additional engineering tools (latest update)
- **Mechanical strain & axial elongation:** combines linear-elastic axial strain with free thermal strain and estimates length change.
- **Beam deflection limit checker:** compares a supplied or latest calculated deflection against a user-selected span ratio.
- **Helical compression spring estimate:** estimates spring rate, axial deflection, spring index and Wahl-corrected wire shear stress.
- **Differential thermal expansion:** compares free expansion of two parts with different thermal expansion coefficients.

These are educational/preliminary calculations, not substitutes for applicable codes, validated analysis or professional engineering review.


## Four additional machine-design calculators (latest update)
- Hydraulic cylinder extension/retraction force from pressure, bore/rod area and entered efficiency.
- Hydraulic pump power from pressure, flow rate and overall efficiency.
- Belt drive speed ratio, estimated output torque and output power (ideal pulley ratio; slip not modeled).
- Simple single-stage gear ratio, output speed, torque and power from tooth counts and entered efficiency.

These are preliminary educational estimates. Verify component ratings, duty cycles, dynamic effects, losses and safety factors using manufacturer data and applicable standards.


## Machine Design Module (added)

Five preliminary machine-element tools are included in the latest HTML version:
- Rolling bearing basic L10 life (ball/roller exponent choice)
- Solid shaft diameter estimate under combined bending and torsion
- Rectangular parallel-key shear and bearing/crushing checks
- Multi-plate clutch/brake torque using uniform-wear or uniform-pressure mean radius
- Flywheel mass moment of inertia estimate from energy fluctuation and coefficient of speed fluctuation

These are educational/preliminary calculations. Confirm formulas, units, fatigue/load factors, material data, standards and manufacturer limits for the real application. The shaft formula is a simplified solid circular shaft screen; key stresses are average stresses; bearing L10 is unadjusted basic rating life; clutch torque is idealized; flywheel sizing does not check mechanical stresses, balance or guarding.

## Four additional machine-design calculators (latest update)
- **Spur gear tooth bending stress (Lewis equation):** metric Lewis bending stress from tangential force, module, face width, Lewis form factor and a velocity/dynamic factor, with allowable-stress FoS screen.
- **Journal bearing Sommerfeld screening:** unit bearing pressure and dimensionless Sommerfeld number from load, journal diameter/length, radial clearance, oil viscosity and speed.
- **V-belt drive power rating check:** allowable power (catalogue rating × arc-of-contact factor × length factor × belt count) compared against a service-factored design power.
- **Shaft critical speed (Rayleigh, single mass):** first critical speed from one static deflection value, with an optional operating-speed ratio and a simple resonance-band caution.

These four are preliminary educational screens, not a substitute for AGMA/ISO gear design, a Raimondi–Boyd (or equivalent) journal-bearing design procedure, manufacturer V-belt selection tables, or a full rotordynamic (multi-mass/Dunkerley or FE) critical-speed analysis. The gear check is single-tooth static bending only (no contact/pitting, overload, or reliability factors). The journal-bearing check does not size minimum film thickness, friction loss, temperature rise or stability. The critical-speed estimate uses one lumped deflection and ignores distributed shaft mass, multiple discs/bearings, gyroscopic and torsional effects.


## Four more machine-design calculators (latest update)
- **Power screw (square thread):** torque to raise/lower a load including optional collar friction, efficiency, and a thread-only self-locking check.
- **Bolt tightening torque and preload:** T = K·d·Fi, proof load Fp = Sp·As, and preload as a percentage of proof load with a 60–90% screening band.
- **Roller chain drive:** speed ratio, driven speed, chain speed and approximate chain length in pitches (rounded up to an even number).
- **Band brake:** slack-side tension from T1/T2 = e^(μθ) and braking torque.

These are preliminary educational screens. Power-screw formulas assume a square thread (ACME/trapezoidal threads need a thread-angle correction). Torque factor K varies widely with lubrication and finish. Chain selection needs manufacturer power ratings and service factors. The band-brake model ignores heat, fade, wear and rotation direction.


## Four more machine-design calculators (set 26–29)
- **Riveted lap joint:** shear, crushing and tearing strength per pitch, governing failure mode and joint efficiency.
- **Flange coupling bolts:** bolt shear torque capacity versus service-factored design torque from power and speed.
- **Hertz line contact:** contact half-width and maximum contact pressure for parallel cylinders (or cylinder on flat).
- **Worm gear drive:** speed ratio, wheel speed, efficiency, output torque and a self-locking indication.

Preliminary educational screens only: no edge-tearing/layout checks for rivets, equal bolt sharing for couplings, ideal elastic smooth contact for Hertz, and constant friction (no bearing/churning losses) for worm gears. Verify with standards and manufacturer data.


## Four more machine-design calculators (set 30–33)
- **Spur gear geometry:** pitch diameters, centre distance, pitch-line velocity, tangential force and pinion torque.
- **Shaft angle of twist:** twist angle, twist per metre, torsional stiffness and shear stress for solid or hollow shafts, with a twist-limit check.
- **Thick-walled cylinder (Lamé):** inner/outer hoop stress and a Tresca-based factor of safety.
- **Flat belt power:** centrifugal tension, slack-side tension and transmitted power.

Preliminary educational screens only: standard involute gears without profile shift, no stress raisers in the twist check, closed-end effects ignored in the Lamé check, and no belt creep in the flat-belt model.


## Machine-design usability tools
- **Search/filter:** type a keyword (e.g. gear, bolt, belt, shaft) to show only matching machine-design tools; clear the box to show all.
- **CSV export:** downloads every machine-design tool's current inputs and displayed results as `machine-design-results.csv`. Press each tool's Calculate button first so results are current; the export copies what is shown on screen.


## Four more machine-design calculators (set 34–37)
- **Rotating thin ring / flywheel rim:** rim speed, hoop stress σ = ρω²r², FoS and speed at first yield.
- **Brake energy:** absorbed kinetic energy, stopping time and lumped temperature rise.
- **Motor sizing:** running power, acceleration torque, peak power and service-factored design power.
- **Wire rope hoist:** lead-line tension, rope FoS vs a target, drum speed, drum torque and power at load.

Preliminary educational screens only: rim stresses ignore hub/spokes and rim thickness, brake heating has no cooling, motor sizing ignores thermal duty and torque–speed curves, and the hoist check ignores dynamic loads, rope fatigue and lifting regulations. All of these tools are also covered by the search box and CSV export.


## Four more machine-design calculators (set 38–41)
- **Torsional natural frequency:** shaft torsional stiffness, natural frequency, equivalent critical speed and operating-speed ratio for a shaft with one disc.
- **Hydraulic pipe pressure drop:** velocity, Reynolds number, friction factor (laminar / Swamee–Jain turbulent) and Darcy–Weisbach pressure drop.
- **Bearing equivalent dynamic load:** P = Ks(X·Fr + Y·Fa).
- **Eccentrically loaded bolt group:** direct and torque shear on a circular bolt pattern, worst-bolt stress and PASS/FAIL.

Preliminary educational screens only: single-disc torsional model with no shaft mass, straight pipe only, X and Y must come from the bearing catalogue, and the bolt group check is conservative and shear-only. These tools are also covered by the search box and CSV export.


## Four more machine-design calculators (set 42–45)
- **Helical gear forces:** radial, axial (thrust) and total normal force from tangential force, helix angle and pressure angle.
- **Bolted joint loads:** joint constant, bolt load, clamp force and separation load from bolt/member stiffness, preload and external load.
- **Conveyor drive power:** pulling force, belt power and motor shaft power with friction, incline and efficiency.
- **Press-fit capacity:** torque capacity and axial holding force from interface pressure, diameter, length and friction, with a PASS/FAIL against required torque.

Preliminary educational screens only. The press-fit tool takes interface pressure as an input (it does not compute it from interference), the joint model is linear with constant stiffness, and the conveyor estimate ignores idler/skirt resistance and acceleration. These are also covered by the search box and CSV export.


## Four more machine-design calculators (set 46–49)
- **Interference fit pressure:** interface pressure from diametral interference, hub/shaft moduli and Poisson ratios, then torque capacity and axial holding force (links naturally to tool 45).
- **Helical torsion spring:** applied moment, Ki-corrected bending stress, angular deflection, spring rate and an allowable-stress check.
- **Cam follower (simple harmonic rise):** maximum velocity, maximum acceleration and peak inertia force.
- **Lead / ball screw drive:** required screw speed, driving torque and mechanical power.

Preliminary educational screens only: solid-shaft/thick-hub elastic fit without surface or thermal effects, textbook torsion-spring relations, ideal SHM rise only, and no buckling, critical-speed or nut-life check for screws. These are also covered by the search box and CSV export.


## Four more machine-design calculators (set 50–53)
- **Bracket with two parallel fillet welds:** primary shear, bending-induced stress and resultant weld stress against an allowable value.
- **Endurance limit and Goodman fatigue factor:** Se = 0.5·Sut × (ka·kb·kc·kd·ke) and a Goodman factor of safety from alternating and mean stress.
- **Hydraulic accumulator sizing:** required gas volume from discharge volume, precharge, working pressures and gas exponent, with a precharge-range check.
- **Open flat-belt geometry:** belt length, wrap angle on the small pulley and belt speed.

Preliminary educational screens only: weld treated as a line group, no stress concentration in the fatigue tool, polytropic gas law with absolute pressures for accumulators, and ideal zero-thickness open belt geometry. These are also covered by the search box and CSV export.


## Four more machine-design calculators (set 54–57)
- **Two-stage compound gear train:** overall ratio, output speed, output torque and overall efficiency from four tooth counts and efficiency per mesh.
- **Gearbox / housing thermal check:** heat generated, temperature rise, estimated housing temperature and PASS/FAIL against an allowed temperature.
- **Clevis pin:** double-shear stress, bearing stress in the central member and clevis plates, simple-span bending stress and an overall PASS/FAIL.
- **Vibration isolation:** natural frequency, frequency ratio, transmissibility, isolation efficiency and a resonance/isolation status.

Preliminary educational screens only: ideal gear ratios, steady-state lumped thermal model, simplified clevis pin loading (no tear-out or fatigue), and a single-degree-of-freedom isolator model. These are also covered by the search box and CSV export.


## Four more machine-design calculators (set 58–61)
- **Rack and pinion drive:** pinion pitch diameter, rack speed, thrust force, power and travel per revolution.
- **Thin-walled spherical pressure vessel:** membrane stress, FoS against yield, minimum thickness for a target FoS and a PASS/FAIL.
- **Shaft deflection (central load):** maximum deflection, bearing slope and a deflection-limit check.
- **Rolling bearing friction loss:** friction torque, power loss and heat per hour.

Preliminary educational screens only: ideal rack meshing, thin-shell membrane stress, uniform solid shaft with a central load, and a single friction coefficient for bearings. These are also covered by the search box and CSV export.
