# When Was the Site Given? Satellite Evidence of Right-of-Way Clearance and the Determinability of FIDIC Sub-Clause 2.1 Possession Delays

Gavamukulya Charles

*Draft 0.1, 15 October 2026. Paper 2 of "Determinable at tender". Target: Automation in Construction; Journal of Legal Affairs and Dispute Resolution in Engineering and Construction (ASCE).*

## Abstract

**Introduction.** Under FIDIC Sub-Clause 2.1 the Employer gives the Contractor right of access to, and possession of, the Site within the times stated. Late or partial access is the dominant source of extension of time on Ugandan road contracts. The date access was actually given, section by section, is rarely recorded objectively: it is reconstructed after the event from correspondence, strip maps and compensation records. This paper tests whether open satellite imagery can establish it.

**Methods.**

- Monthly Sentinel-2 L2A imagery (2018–2024) is summarised for 1 km right-of-way sections (60 m corridor) of a 43 km Ugandan road upgrading (Project A).
- Clearance is dated as the first persistent, seasonally adjusted loss of vegetation (NDVI anomaly below −0.12 for at least 5 of the next 6 observations, spanning a wet season), with a rise in the bare-soil index.
- Clearance is compared with the contractual availability date, the Employer's land-acquisition record (strip map) and the Contractor's claimed possession-delay window.

**Results.**

- No section was cleared by the contractual availability date (25 October 2020).
- Clearance came in two waves: January–June 2021 (14 sections) and November 2021–April 2022 (27 sections). By April 2022, 41 of 43 sections (95%) had been cleared.
- Clearing was as complete on stretches the Employer's record showed as *not* acquired (5 of 6 sections) as on acquired land.
- The claimed delay window (8 July 2021 to 24 December 2023, 899 days) extends 20 months beyond the last detected clearance.

**Discussion.** Physical clearance is an objective, low-cost lower bound on the date access was exercised. It diverges from the documentary record in both directions: work proceeded on land recorded as unacquired, while delay was claimed for months after the corridor was cleared. A contract that defines "access" by a verifiable state (cleared length per section, observed by a stated method) and requires a monthly remote-sensing record would make the Sub-Clause 2.1 entitlement determinable as it accrues.

## 1. Introduction

Access to the Site is the Employer's first obligation. Under FIDIC 1999 and 2017 Sub-Clause 2.1:

- the Employer gives the Contractor right of access to, and possession of, all parts of the Site within the time stated in the Contract Data, or otherwise as required by the programme;
- failure entitles the Contractor to time (8.4/8.5) and Cost plus profit;
- the proviso excludes delay caused by the Contractor's own error or delay, including in submitting documents.

On linear works access is granted piecemeal, as land is acquired and compensated under the resettlement action plan.

On Ugandan roads, possession is the largest head of extension. On Project A, successive extension-of-time claims (EOTs 3, 5 and 7) put possession delays at 472, 765 and 849 days, far more than weather (Paper 0).

The difficulty is evidential. A 2.1 claim needs, for each section:

- the date access was due;
- the date it was given;
- whether partial or encumbered access counted;
- whether the Contractor could have used it.

The record is a strip map issued months or years later, correspondence and compensation lists. These are documents produced by the parties and contested by the other side. No measurement independent of the parties exists.

Satellite imagery offers one. When the Contractor clears and grubs the right of way, vegetation disappears and bare soil appears, and the change is visible at 10 m resolution every five days. This paper asks:

1. Can open imagery date right-of-way clearance per kilometre?
2. How does it compare with the possession record and the claim?
3. How should "access" be defined so that it can be verified?

## 2. Data

- **Corridor.**
  - Project A, Masindi–Biiso lot, 43 km. Centreline from OpenStreetMap (the least-cost path along the road from Masindi towards Butiaba, truncated at 43 km to match the contract length).
  - Cut into 43 sections of 1 km, buffered 30 m each side (the nominal right of way).
- **Imagery.**
  - Sentinel-2 L2A (ESA Copernicus; Microsoft Planetary Computer), January 2018 to December 2024, scenes under 50% cloud.
  - Up to three tiles per month, so 168 scenes over 84 months.
  - Clouds, shadow and cirrus masked with the scene classification layer.
  - Per section and month: median NDVI = (B08 − B04)/(B08 + B04) and NDBI = (B11 − B08)/(B11 + B08), from the scene with the larger valid fraction; sections with under 50% valid pixels dropped.
- **Contract record (Project A; anonymised).**
  - Contractual availability of the Site: 25 October 2020.
  - Land acquired by chainage: 12 stretches, 37.5 of 42.9 km, from the Employer's strip map of 9 June 2022 as restated in the Engineer's letter of 8 February 2023 (EOT-7).
  - Contractor's claimed Section 2 delay window: 8 July 2021 to 24 December 2023.

## 3. Methods

- **Seasonal adjustment.** Western Uganda has two dry seasons, and NDVI falls every December to February. Each section's indices are expressed as anomalies from that section's calendar-month median over the pre-works period (January 2018 to September 2020).
- **Clearance date.** The first month from January 2020 in which all of the following hold:
  - the NDVI anomaly is below −max(0.12, 3 × MAD of pre-works anomalies);
  - it stays below the threshold in at least 5 of the next 6 observed months, which rules out a dry-season dip or a single cloudy scene;
  - the NDBI anomaly is positive.
- **Comparison.** Sections are classed as acquired or not (at least 50% of their length in the strip-map stretches). Cleared shares are compared at each key date.

Clearance is the Contractor's own act. Its date is therefore the latest date by which access to that section had in fact been exercised, and an upper bound on the date access was given. Where works start only once access is given, it is close to the access date.

## 4. Results

**No access by the contractual date.** At 25 October 2020 no section shows clearance (Fig. 1). The pre-works record is stable (3 × MAD of anomalies below 0.12 in most sections), so the series would have registered clearing had it occurred.

**Two clearance waves.**

- **First wave, January–June 2021, 14 sections:** km 4–14, 24–25 and 35.
- **Second wave, November 2021–April 2022, 27 sections:** km 0, 2–3, 15–19, 21–23, 26–34 and 36–42.
- By the start of the claimed delay window (8 July 2021), 32% of acquired sections had been cleared. By April 2022, 41 of 43.
- The two sections never detected (km 1 and km 20, pre-works NDVI 0.25 and 0.13, in and near Masindi town) were already sparsely vegetated, so clearance is not visible in NDVI.

**The documentary record and the ground disagree.**

- Of the six sections the strip map shows as mostly *not* acquired, five were cleared, at km 13–14 as early as May 2021, a year before the strip map.
- Either the Contractor worked on land the Employer had not acquired, or the strip map lagged the facts on the ground. Either way, the record on which the possession claim and its determination rest is not a record of access.

**The claim window and the clearance record.**

- The claimed window (899 days) runs to 24 December 2023, 603 days after the last detected clearance.
- If access is equated with physical clearance, most of the window is not explained by lack of access. The remainder would need another ground, such as encumbrances (utilities, structures under 10 m, disputed plots), access to borrow areas, or disruption to sequence.
- Conversely, the 552 days from contractual availability to the end of clearance are an objective measure of how late the corridor became workable.

## 5. Discussion

**A measurement independent of the parties.** Unlike strip maps and correspondence, the satellite record is produced by neither party. It is retrospective (archive from 2015) and cheap: open data and a few hundred lines of code. It cannot see legal title, compensation or small encumbrances, but it fixes when the corridor was physically opened, and that bounds the factual dispute.

**What "access" should mean.** The FIDIC text does not define what state of the Site constitutes access. Practice veers between legal possession (compensation paid), physical clearance and a continuous workable length. Each gives a different date. A determinable clause would:

1. Define access per section as a stated physical state (e.g. ≥ 90% of the corridor length cleared and free of structures over a continuous minimum length, such as 1 km).
2. Name the evidence: a monthly remote-sensing clearance record, here Sentinel-2 seasonally adjusted NDVI, kept by the Engineer and issued with the monthly progress report.
3. Treat sections not handed over by the scheduled date as automatically delayed from that date until the record shows access, without a separate notice contest.
4. Require the Employer's strip map to be issued monthly and reconciled with the clearance record. A section cleared but shown as unacquired triggers an inquiry, not a later surprise.

**Concurrency and the 2.1 proviso.** Where the record shows clearance before legal acquisition, the Contractor was working, and the question becomes disruption rather than prevention. Where it shows the corridor cleared but works idle, the delay has another cause. The clearance record separates the two; neither party's documents can.

## 6. Limitations

- One corridor; Project B (145 km) and the Kabaale–Kiziranfumbi lot are being processed.
- The corridor is reconstructed from OpenStreetMap, not the design alignment. The 30 m buffer approximates the right of way.
- Ten-metre imagery cannot see individual structures, utilities or small encumbrances.
- NDVI loss can come from causes other than clearance (fire, cultivation cycles); the persistence and NDBI rules limit this, and validation against site photographs and handover certificates is planned.
- Clearance dates access only from above; the gap between access and clearance is unobserved.

## Figures and tables

- Fig. 1 `figures/fig_clearance_A_lot3.png`
- `results/clearance_A_lot3.csv`, `results/possession_summary_A_lot3.csv`

## References

[To compile: FIDIC 1999 and 2017 (2.1, 8.4/8.5, 20.1); ESA Sentinel-2 L2A; Planetary Computer; land-acquisition and RAP practice in Uganda (Land Acquisition Act; UNRA RAP framework); remote sensing for construction progress monitoring literature.]
