# Whose Flood? Return Periods, Temporary-Works Standards and the "Forces of Nature" Risk in FIDIC Sub-Clause 17.2

Gavamukulya Charles

*Draft 0.1, 15 October 2026. Paper 8 of "Determinable at tender". Target: Natural Hazards Review (ASCE); Journal of Legal Affairs and Dispute Resolution in Engineering and Construction (ASCE).*

## Abstract

**Introduction.** FIDIC places loss or damage to the Works on the Contractor during construction (17.2; 1999: 17.2), except where it is caused by an Employer's risk. One such risk is any operation of the forces of nature that is Unforeseeable or against which an experienced contractor could not reasonably have taken adequate preventive precautions (2017: 17.2(d); 1999: 17.3(h)). For road contractors the typical event is a storm that washes out a diversion, culvert or embankment at a river crossing. Whether that storm was "Unforeseeable" and what precautions were "adequate" are decided after the event.

**Methods.**

- The 34 river crossings (HydroRIVERS, catchments ≥ 10 km²) of two Ugandan road projects are identified on the project corridors (Project A, 2019–2024; Project B, 2023–2026).
- Pre-award annual-maximum rainfall (CHIRPS, 1981–2018) is fitted with a GEV distribution at each crossing. The return period of the largest storm each crossing experienced during its contract is estimated, on 1-day and 3-day durations.
- The probability that a temporary works designed for a T-year event is exceeded during a contract is computed for one structure and for a project, allowing for the spatial correlation of storms.

**Results.**

- **Exceedance probability.** A 10-year standard has a 27% chance of being exceeded at a single crossing over a 3-year contract, 41% over 5 years, and 37–59% at some crossing of the project. A 25-year standard: 12–29%.
- **Project A.** On 22 November 2019, during the record short rains, 10 of 13 crossings received a 1-day storm with a 49-year return period. The same storm on a 3-day basis was a 4.5-year event.
- **Project B.** The largest storms to date are about 10-year events at 3 of 21 crossings on a 1-day basis, and 1.6–2.6-year events on a 3-day basis.

**Discussion.** "Unforeseeable" is not a property of a storm. It depends on:

- the duration measured;
- the exposure period, i.e. the contract plus its extensions;
- the number of structures exposed.

Storms rare at one culvert are expected across a project. A contract that states the temporary-works design standard (return period, duration matched to catchment response, data source) makes 17.2(d) determinable: exceedance of the stated event is an Employer's risk, and anything below it is the Contractor's.

## 1. Introduction

Care of the Works is the Contractor's from commencement to taking-over. The exceptions are the Employer's risks: war, riot and other listed events, and, for natural events, forces of nature that are Unforeseeable or against which an experienced contractor could not reasonably have taken adequate precautions. The test bundles two questions:

1. Was the event outside what an experienced contractor would foresee?
2. Were the precautions adequate?

Both are answered in practice by expert opinion after the damage.

Hydrology already offers a language for both questions: the return period of the event, and the design standard of the temporary works. Temporary works are routinely designed to a stated return period, such as 1-in-10 years for river diversions, but the contracts studied do not state it. This paper connects the two:

- How rare were the storms that the programme's river crossings experienced?
- How likely is a given design standard to be exceeded during a road contract?
- What would make the test determinable?

## 2. Data

- **Crossings.** Project A (Masindi–Biiso, 43 km; Kabaale–Kiziranfumbi, 30 km) and Project B (Busunju–Kiboga–Hoima, 145 km) corridors from Paper 2.
  - HydroRIVERS v1.0 reaches with ≥ 10 km² upstream area that cross the centrelines: 13 crossings on A (catchments 13–161 km²) and 21 on B (11–3,710 km²).
- **Rainfall.** CHIRPS v2.0 daily (0.25° regridded as in Paper 0), 1981–2026, extracted at each crossing.
  - The 34 crossings fall in 7 distinct rainfall cells (A: 2, B: 5).
- **Contract windows.**
  - Project A: commencement 25 April 2019; works continued to 2024 (Paper 2).
  - Project B: commencement 10 May 2023, completion date 9 May 2026; window taken to September 2026.

## 3. Methods

**Event rarity.** At each crossing:

- the pre-award annual maxima of 1-day and 3-day rainfall (1981–2018) are fitted with a GEV distribution by maximum likelihood;
- the largest 1-day and 3-day totals in the contract window are assigned their return period;
- the 10-year return level is reported.

**Exceedance during a contract.** For a structure designed to a T-year event, the probability of at least one exceedance in n years is P = 1 − (1 − 1/T)ⁿ. For a project with k crossings, storms are correlated; the effective number of independent crossings is k_eff = k / (1 + (k − 1)ρ̄), where ρ̄ is the mean correlation of annual maxima across distinct rainfall cells. Project-level exceedance is 1 − (1 − 1/T)^(n·k_eff).

## 4. Results

**A design standard is a probability, not a guarantee.** Over a 3-year contract, single-structure exceedance probabilities by design standard are:

| Design standard | Probability of exceedance (3-year contract) |
|---|---|
| 2-year | 88% |
| 5-year | 49% |
| 10-year | 27% |
| 25-year | 12% |
| 100-year | 3% |

Extensions matter. Over 5 years, typical once extensions of time are granted, the 10-year standard is exceeded with 41% probability.

Across a project the probabilities rise. With k_eff = 1.4 (A) and 1.7 (B), mean ρ̄ = 0.38 and 0.50, a 10-year standard is exceeded somewhere with 37–41% probability in 3 years and 53–59% in 5 (Fig. 1a). With truly independent catchments (k = 10), exceedance is almost certain. Finer-resolution rainfall would raise k_eff, and so these probabilities.

**Project A: one storm, two return periods.**

- On 22 November 2019, during the October–December 2019 short rains that Paper 0 finds exceptional, 10 of 13 crossings received 42.6 mm in a day. That is a 49-year event against a local 10-year level of about 37 mm.
- On a 3-day basis the same storm (57.4 mm, 24 November) was a 4.5-year event (10-year level about 64 mm).
- For the small catchments (13–161 km²) of Project A, which respond within hours, the 1-day measure is the relevant one. A party could nonetheless argue either verdict.

**Project B: an ordinary record so far.** The largest 1-day storms reached about a 10-year return period at 3 of 21 crossings (4 September 2024). On 3-day totals, nothing exceeded a 2.6-year event. A washout on Project B would, on this record, be hard to call Unforeseeable. For the 3,710 km² crossing, though, the relevant duration is several days and the relevant data are river flow, not point rainfall.

## 5. Discussion

**"Unforeseeable" depends on three choices.**

1. **Duration.** The same storm was a 1-in-49-year event or a 1-in-4.5-year event depending on whether one or three days were counted. The right duration depends on the catchment's response time, which the contract does not mention.
2. **Exposure period.** Probabilities scale with contract duration. Extensions of time increase the Contractor's exposure, though they are usually granted for Employer risks.
3. **Number of structures.** An event rare at one culvert is expected somewhere along a road crossing a dozen streams. A per-structure test and a per-project test give different answers.

**Precautions are a design standard.** The second limb, what precautions an experienced contractor would take, is in engineering terms the temporary-works design standard. A diversion designed to the 10-year flood is a reasonable precaution against floods up to that level and no more.

**A determinable clause.** The Contract Data should state:

1. **The temporary-works design event** for river crossings: return period (e.g. 10 years), duration (e.g. matched to the time of concentration, at least 1 day for catchments under 500 km²), and the reference data (named gauge or gridded product, baseline period).
2. **The risk split:** damage from an event exceeding the stated design event at that structure is an Employer's risk under 17.2(d); damage from smaller events is the Contractor's.
3. **Re-baselining for extensions:** where the period of exposure is extended for Employer-risk reasons, the design standard is maintained by the Contractor at the Employer's cost, or the excess exposure is the Employer's.

This is the logic of the weather formula in Paper 0 applied to damage rather than delay. It turns a judgment ("Unforeseeable", "adequate") into a comparison of a recorded event with a stated threshold.

## 6. Limitations

- Rainfall, not river flow. CHIRPS at 0.25° smooths convective storms, so point return periods are biased, probably low for 1-day extremes.
- No damage records from the projects are matched to the storms. Monthly progress reports (Paper 10) are the next source.
- GEV fits on 38 annual maxima carry wide uncertainty above the 25-year level.
- The 3,710 km² crossing requires flood-frequency analysis on gauged flow.

## Figures and tables

- Fig. 1 `figures/fig_forces_of_nature.png`
- `data/crossings.csv`, `results/crossing_events.csv`, `results/exceedance_analytic.csv`

## References

[To compile: FIDIC 1999 17.3(h), 17.4; FIDIC 2017 17.2(d); Lehner & Grill (2013) HydroSHEDS/HydroRIVERS; Funk et al. (2015) CHIRPS; Coles (2001) extreme values; CIRIA C648 / temporary works design standards; MoWT Drainage Design Manual (2010).]
