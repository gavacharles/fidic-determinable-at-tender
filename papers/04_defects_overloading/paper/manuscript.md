# Overloaded Against What? Design Traffic, Axle-Load Monitoring and the Allocation of Pavement Defects under FIDIC Clause 11

Gavamukulya Charles

*Draft 0.1, 15 October 2026. Paper 4 of "Determinable at tender". Target: Journal of Legal Affairs and Dispute Resolution in Engineering and Construction (ASCE); Journal of Infrastructure Systems.*

## Abstract

**Introduction.** Under FIDIC Clause 11 the Contractor remedies defects notified within the Defects Notification Period at its own cost if they are attributable to design (where it designs), Plant, materials or workmanship. If the cause is something else, such as traffic loading beyond the design, the Employer pays (11.2). For road pavements the defence is almost always "overloading". It can only be tested against two quantities: the design traffic, and the traffic that actually used the road.

**Methods.**

1. The design traffic of a 145 km Ugandan trunk road rehabilitation (Project B) is recomputed under the alternative inputs in its own design review: seven Ugandan axle-load surveys, three growth scenarios, two opening years, two design periods and two lane/direction factors (168 combinations).
2. Axle-load monitoring coverage is measured by tracing the five corridors that the Auditor General's 2025 audit found to carry an operational fixed weighbridge onto the OpenStreetMap trunk and primary network.

**Results.**

- Design traffic ranges from 2.7 to 41 million equivalent standard axles (MESA), crossing five pavement traffic classes.
- The choice of axle-load survey alone moves the 10-year load 3.4-fold: the project survey's equivalence factors are 2.5–3.4 times those of six other Ugandan surveys.
- The designer adopted 10 MESA (T7); the supervision consultant's review adopted 19 MESA (T8).
- Only 41% of trunk and primary road length lies on a corridor with a fixed weighbridge. None of the project roads in the programme does.

**Discussion.** "Overloading" is undefined at tender. The design load is not a fact but a choice among defensible inputs, and actual loading is not measured on most roads. The causation question in Clause 11 is therefore not determinable after the event. Three provisions would make it determinable:

- a design traffic baseline stated in the Contract (CESA, with the equivalence factors used, and whether overloading is included);
- weigh-in-motion monitoring during the Defects Notification Period;
- a load-adjusted defects test: defects compensable where measured cumulative loading exceeds the baselined share for the elapsed period.

## 1. Introduction

Early failure of new pavements is a recurrent finding of public audit in East Africa, and overloading is the standard explanation. The 2025 audit of Uganda's weighbridges by the Office of the Auditor General (OAG) concludes that "vehicle overloading remained prevalent and continued to contribute significantly to faster road deterioration".

In contract terms the question is one of allocation. FIDIC Sub-Clauses 11.1–11.2 (1999 and 2017):

- oblige the Contractor to remedy defects notified in the Defects Notification Period (DNP);
- place the cost on the Contractor where the defect is attributable to its design, Plant, Materials or workmanship;
- otherwise treat the remedy as a variation (2017: 11.2(d) "any other matter" for which the Contractor is not responsible).

Under the Yellow Book the Contractor also designs, so the Works must be fit for their purposes (4.1). A pavement that fails under the design traffic is defective. A pavement that fails under traffic beyond the design may not be.

The causation question thus turns on two measurable quantities: the design traffic, and the traffic carried. This paper asks how determinable each one is in practice.

## 2. Data

- **Design traffic (Project B).**
  - Design review report (Supervision Team, ST) of the Busunju–Kiboga–Hoima rehabilitation design (Design Team, DT). It contains:
    - classified 2018 ADT at four count stations;
    - the project's axle-load survey (Kihemba, May 2018) and six comparison surveys from other Ugandan roads (2009–2017);
    - growth scenarios, design periods and the CESA computation.
  - The DT adopted 10 MESA (class T7, 10-year design). The ST revised this to 19.27 MESA at Busunju (T8) and recommended T8 for the whole road.
- **Axle-load monitoring.** OAG Annual Report FY2024/25, s. 3.1.18, value-for-money audit of road weighbridges (FY2022/23–2024/25). It found eight fixed and six mobile stations, with operational fixed weighbridges on 5 of 37 priority Class A/B corridors.
- **Network.** OpenStreetMap (Geofabrik, Uganda), trunk and primary roads, 4,565 km.

## 3. Methods

**CESA recomputation.**

- CESA = Σ over years of AADT × VEF × 365 × L for the heavy classes (medium and large buses, two- and three-axle trucks, articulated), where AADT = 0.94 × ADT₂₀₁₈ grown at the scenario rates to and beyond opening.
- The lane/direction factor L is not reported ("an assumption has been made"). It is calibrated to reproduce the ST's own 19.27 MESA case (L = 0.74), with 0.5 as the alternative.
- Inputs varied:
  - VEF from each of the seven surveys (semi- and truck-trailer factors averaged for articulated vehicles);
  - low, medium or high growth;
  - opening in 2021 (DT) or 2027 (ST);
  - 10 or 15 years;
  - the two values of L.
- That gives 168 combinations, each classified by the Uganda Road Design Manual and ORN 31 traffic classes (T6 6–10, T7 10–17, T8 17–30, T9 > 30 MESA).

**Monitoring coverage.**

- Each weighed corridor is traced as the least-cost trunk and primary path through its named towns.
- Network length within 150 m of a traced corridor counts as "on a weighed corridor".
- The Project A and B corridors (Paper 2) are overlaid.

## 4. Results

**Design traffic is a range, not a number.**

- One input at a time (Fig. 1a), the ST's 19.3 MESA case moves:
  - to 5.7 MESA with the least severe comparison survey (×3.4);
  - to 32.5 MESA with a 15-year period (×1.7);
  - across 15.8–23.5 MESA with the growth scenario (×1.5);
  - to 13.0 MESA with L = 0.5 (×1.5);
  - to 15.1 MESA with the DT's earlier opening year (×1.3).
- Over all 168 combinations, design traffic spans 2.7–41 MESA (Fig. 1b). For a 10-year design: 62% of combinations fall below T6, 16% in T6, 19% in T7 and 4% in T8.

**The project's own survey is the outlier.**

- With the project's VEFs, 10-year design traffic is 9.1–23.5 MESA (T6 to T8). With any of the five lower comparison surveys it is 2.7–8.7 MESA.
- Project VEFs are 2.5–3.4 times the others: large buses 6.29 against 1.1–3.6; three-axle trucks 5.86 against 0.9–3.9; articulated 10.0 against 3.3–9.6.
- Fourth-power equivalence factors at the legal limits of the EAC Vehicle Load Control Act 2016 are:
  - two-axle truck, 8 t steer + 10 t single: about 3.2;
  - three-axle truck, 8 t + 18 t tandem: about 3.9;
  - six-axle articulated, 8 t + 18 t + 24 t: about 6.7.
- The project's three-axle and articulated factors are therefore above legal loading. The design adopted overloaded traffic as its baseline. The ST nonetheless found the factors "do not appear unrealistic" and kept them.

**Actual loading is mostly unmeasured.**

- The five weighed corridors trace to 1,844 km and cover 1,868 km (41%) of the 4,565 km OSM trunk and primary network: 69% of trunk and 33% of primary (Fig. 2).
- None of the 218 km of Project A and B roads lies on a weighed corridor.
- Even on weighed corridors, OAG found that none of the eight fixed stations met the quarterly calibration schedule, and that weighbridge data were "not systematically analysed".

## 5. Discussion

**Overloaded against what?** An overloading defence asks whether traffic exceeded the design. On Project B the design itself could have been 6, 10, 19 or 32 MESA on documented, defensible inputs. Because the adopted equivalence factors already embody overloaded trucks, a large part of what would be called "overloading" was designed for. Neither party can say at tender which risk the Contractor priced.

**The counterfactual is unobservable.** Where actual loading is not measured, as on all programme roads and most of the network, the DNP dispute is decided by experts reconstructing traffic after the event. It turns on the same inputs (growth, VEF, lane split) whose spread Fig. 1 shows. That reproduces the indeterminacy of the design stage at the dispute stage.

**What would make Clause 11 determinable.**

1. **Design traffic baseline in the Contract.**
   - State CESA by section and design period, the equivalence factors, the growth path and the lane/direction factor.
   - Say expressly whether the baseline includes current overloading or assumes legal loads.
   - Under a Yellow Book, the Employer's Requirements should fix these as Employer data (cf. 1.9/5.1, errors in the Employer's Requirements).
2. **Load monitoring during the DNP.**
   - A weigh-in-motion (WIM) station per contract, or a portable survey each season, as a Contract obligation with a stated owner and calibration.
   - The OAG's own recommendation (WIM, ANPR and automation) supplies the instrument.
3. **Load-adjusted defects test.**
   - A pavement defect within the DNP is presumed to be the Contractor's if measured cumulative ESAs are within the baselined share for the elapsed time; beyond it, the presumption reverses.
   - This replaces a qualitative causation dispute with a ratio both parties can compute.
4. **Re-baselining when the road is re-classified.** Where a design review raises the traffic class (here T7 to T8) after award, the change is a variation with an explicit new baseline, not an implicit transfer of loading risk.

## 6. Limitations

- One project's design review. Comparison VEFs are as reported, without their survey conditions; the lane/direction factor is calibrated.
- The OSM classification of trunk and primary roads is incomplete. The weighed-corridor traces approximate the OAG corridor names.
- No pavement condition or defects records for the project roads. Linking DNP defects to loading (e.g., IRI and condition surveys) awaits data access.
- The legal-limit factors use a fourth-power law with an 8.16 t standard axle. Tandem and tridem equivalence is simplified.

## Figures and tables

- Fig. 1 `figures/fig_cesa.png`: design traffic sensitivity.
- Fig. 2 `figures/fig_weighbridge.png`: weighed corridors vs network and project roads.
- `results/cesa_cases.csv`, `results/cesa_summary.csv`, `results/weighbridge_coverage.csv`

## References

[To compile: FIDIC 1999 and 2017 (4.1, 5.1, 11.1–11.4); Uganda Road Design Manual Vol. 3 Part I (2010); TRL ORN 31 (1993); TRH16 (1991); AASHTO (1993); EAC Vehicle Load Control Act (2016); OAG Uganda Annual Report FY2024/25 s. 3.1.18; Rolt (2001) on overloading in Africa; World Bank RONET.]
