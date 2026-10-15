# Foreseeable Where, or Foreseeable How Much? Site-Investigation Data and the "Unforeseeable Physical Conditions" Test in FIDIC Road Contracts

Gavamukulya Charles

*Draft 0.1, 15 October 2026. Paper 3 of "Determinable at tender". Target: Journal of Legal Affairs and Dispute Resolution in Engineering and Construction (ASCE), or Engineering, Construction and Architectural Management.*

## Abstract

**Introduction.** FIDIC Sub-Clause 4.12 gives the Contractor time and Cost for physical conditions that were "Unforeseeable": not reasonably foreseeable by an experienced contractor by the Base Date, having regard to the Site data the Employer provided (4.10) and other available information. The test is decided after the event and turns on what the data "should" have told an experienced contractor. This paper asks what site-investigation data can make foreseeable at all.

**Methods.** The analysis uses the subgrade investigation of a 43 km Ugandan road upgrading (62 test pits at 500 m nominal spacing; Atterberg limits, AASHTO class and soaked CBR at 95% MDD, all dug in November 2019).

1. Thinning the test-pit grid to 1, 2, 3, 5 and 10 km simulates the information available at different investigation densities. Each unsampled pit is predicted from its nearest sampled neighbours.
2. Open global soil data (SoilGrids 2.0, 250 m) is tested as an alternative source of "available information".

**Results.**

- Subgrade strength has almost no spatial autocorrelation along the alignment (lag-0.5 km correlation of CBR95 −0.04).
- Consequently, 84–100% of poor subgrade (CBR95 < 8%) is unforeseen from neighbouring pits *at every spacing*, and 54–64% at a CBR95 < 10% threshold.
- The *frequency* of poor ground, by contrast, is stable and estimable: 13% of the alignment below CBR95 8% and 31% below 10%.
- SoilGrids predicts poor subgrade only weakly (|ρ| ≤ 0.30; best AUC 0.64).
- Groundwater was recorded in only 2 pits, during the exceptionally wet late-2019 short rains.

**Discussion.** For heterogeneous subgrades the *location* of adverse ground is not foreseeable from any economical investigation, while its *quantity* is. A test framed on location therefore makes almost every encounter "Unforeseeable" in fact, and leaves the dispute to argument about what an experienced contractor should have inferred. A quantity baseline stated at tender makes the 4.12 test determinable: an expected share of poor subgrade, groundwater depth by season, and only quantities beyond the baseline compensable. Investigation timing is itself a baseline choice and should be stated.

## 1. Introduction

Unforeseeable ground is among the most litigated risks in construction (e.g. *Obrascon Huarte Lain v Attorney General for Gibraltar* [2014] EWHC 1028). FIDIC allocates it by Sub-Clause 4.12 (1999, MDB 2010 and 2017):

- the Contractor is entitled where physical conditions were "Unforeseeable";
- "Unforeseeable" (1.1.6.8 in 1999; 1.1.87 in 2017) means "not reasonably foreseeable by an experienced contractor by the date for submission of the Tender";
- the Contractor is deemed to have examined the Site and the data (4.10);
- climatic conditions are excluded.

The test requires a counterfactual inference: what the data *should* have told an experienced contractor. It is made after the event, by parties with opposite interests. No empirical study has asked what site-investigation data make foreseeable in the first place.

This paper treats foreseeability as a prediction problem. If an experienced contractor had the investigation data available at the Base Date, how well could it have predicted the subgrade it later met? The answer depends on the spatial structure of the ground and on investigation density, both measurable.

## 2. Data

- **Site investigation.** Soil and Materials Investigation Report for a 42–43 km design-and-build road upgrading in western Uganda (Project A of the programme; anonymised).
  - TRRL DCP tests and test pits at about 500 m spacing (LHS/RHS alternating), November 2019.
  - Laboratory results per pit: grading, LL, PL, PI, linear shrinkage, AASHTO class, MDD, OMC, and soaked CBR at 90/93/95% MDD.
  - 62 pits were parsed from the report text (pits split across lines in the PDF are missing for 15–18, 25–28 and 35–37 km; to be completed).
  - The report's homogeneous sections give corrected in-situ CBR ranges of 2–93%.
- **Open soil data.** SoilGrids 2.0 (ISRIC, 250 m): clay, sand, silt, bulk density and CEC at 0–5, 15–30 and 60–100 cm, sampled at each pit, with pits located by chainage along the road centreline (OpenStreetMap).

## 3. Methods

- **Adverse condition:** poor subgrade, soaked CBR95 < 8% (sensitivity 6% and 10%), roughly failing the G7 subgrade class of the General Specifications.
- **Spatial structure:** Pearson correlation of CBR95 between pit pairs at lags of 0.5–5 km.
- **Foreseeability by density:**
  - for spacing s ∈ {1, 2, 3, 5, 10} km and every grid offset, the pits at spacing s form the Base-Date information;
  - an unsampled pit is "foreseeable as poor" if either nearest sampled neighbour is poor;
  - *unforeseen poor* = poor with both neighbours adequate;
  - reported as the share of poor ground unforeseen and as unforeseen kilometres per 10 km.
- **Open data:** Spearman correlation of each SoilGrids layer with PI and CBR95, and ROC AUC for CBR95 < 8%.

## 4. Results

**Little spatial structure.** CBR95 is essentially uncorrelated between neighbouring pits: −0.04 at 0.5 km, −0.24 at 1 km, 0.06 at 2 km, 0.13 at 5 km (Fig. 1a). Subgrade adequacy changes at a scale finer than any practical investigation spacing.

**Location is not foreseeable; frequency is.** Poor subgrade (CBR95 < 8%) makes up 13% of pits. At every investigation spacing from 1 to 10 km, 84–100% of poor pits lie between adequate neighbours and are "unforeseen" (Fig. 1b). At the 10% threshold (31% of pits), 54–64% are unforeseen, again with no improvement as spacing tightens. False alarms (adequate pits next to a poor neighbour) run at 17–30% at the 8% threshold. The *share* of poor ground, by contrast, is estimable from a few pits: at 2 km spacing the estimate is within a few points of the full-grid value.

**Open data do not substitute.** SoilGrids layers correlate weakly with PI (|ρ| ≤ 0.30) and CBR95 (|ρ| ≤ 0.30). The best layer (bulk density, 15–30 cm) separates poor from adequate subgrade with AUC 0.64. Global soil data cannot locate adverse subgrade either.

**Groundwater is a seasonal snapshot.** Water was met in 2 pits (0.5 m at km 22; 1.0 m at km 6) during November 2019. That was the record-wet October–December 2019 short rains, which Paper 0 finds exceptional in this region. An investigation in a drier season would have recorded less groundwater, and a contractor relying on it would have foreseen less.

## 5. Discussion

**The location test fails empirically.** Read as a question of *where*, 4.12 asks whether an experienced contractor could have foreseen poor ground at the place it was met. For a subgrade with no spatial structure at the 0.5 km scale, the honest answer is almost always no, whatever the investigation. The dispute then moves to what the contractor "should have" inferred: the indeterminacy is not resolved by more boreholes.

**Quantity is determinable.** The *proportion* of adverse ground is stable and estimable from a modest investigation. A contract can therefore fix, at tender:

- the expected share of the alignment requiring subgrade improvement (or the quantity of improvement layers or undercut);
- the expected groundwater depth by season;
- the investigation's timing relative to the rains.

The Contractor prices the baseline, and only quantities beyond it are Unforeseeable. That converts a counterfactual inference into a measurement, the logic of the geotechnical baseline report (GBR) used in tunnelling, applied to linear works.

**"Published data" is not enough.** FIDIC 2017 points to data "made available" and other information. Open global soil data are weak predictors at this scale, so they cannot carry the foreseeability test, and the Employer's investigation remains the decisive Base-Date record. That strengthens the case for stating it as a baseline.

**Investigation timing is a hidden choice.** Groundwater measured in an exceptionally wet season inflates the baseline; measured in a dry season, it understates it. The boundary between 4.12 (physical conditions) and the climatic exclusion depends on when the pits were dug. A baseline should state the season, or adjust to a normal season.

## 6. Recommendations

1. Attach a **ground baseline** to the tender: the expected percentage of the alignment (or quantity) with subgrade below the design class, by homogeneous section, with the investigation data.
2. **Compensate quantities beyond the baseline** (e.g. undercut and replacement beyond the baseline quantity at BoQ rates), not "unforeseeability" in the abstract.
3. **State groundwater by season** and the dates of the investigation; adjust to a normal season using rainfall records.
4. **Do not rely on global open soil data** as "available information" for subgrade location.

## 7. Limitations

- One alignment and one investigation; parsing incomplete for three stretches.
- No actual 4.12 claim in the documents reviewed.
- Thinning simulates spacing but not investigation quality.
- CBR is one adverse condition among several (rock, swelling clay, soft ground).
- A multi-project replication (the Busunju design review and other projects' materials reports) is planned.

## Figures and tables

- Fig. 1 `figures/fig_foreseeability.png`
- `results/foreseeability.csv`, `results/autocorrelation.csv`, `results/soil_predictor.csv`

## References

[To compile: FIDIC 1999, 2017 (1.1.87, 4.10, 4.12); *Obrascon Huarte Lain v AG Gibraltar* [2014] EWHC 1028 (TCC); Essex (ed.) Geotechnical Baseline Reports (ASCE, 2007); ISRIC SoilGrids 2.0 (Poggio et al. 2021); TRRL Overseas Road Note 31; MoWT General Specifications.]
