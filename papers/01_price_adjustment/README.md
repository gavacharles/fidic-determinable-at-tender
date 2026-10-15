# Paper 1: "Which index?" Sources, rebasing and dead bands in price adjustment (companion to DAM)

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** data assembly in progress (15 Oct 2026). **Repositioned** after review of the author's DAM work (see ../../docs/related_work.md).

**Positioning.** The DAM papers ("Beyond Static Escalation"; "When to Adjust, Not How Much"; "Brent to Site") address the *computational form* of 13.8/13.7: lag, coefficient stability, publication lag, triggers and caps. This paper addresses what they leave open: **the identity and governance of the index itself**. Which source, which series, what happens when the statistical agency rebases or discontinues it, who chooses the weights, and when adjustment starts. It cites and builds on DAM rather than re-estimating escalation dynamics.

**Revised research questions.**

1. *Sources:* how often, and how far, do defensible alternative index sources (UBOS basic heading vs sector index vs international, e.g. Dubai bitumen) change the adjustment on the same contract? Case: the KCCA "Sources of Indices for Price Adjustment" dispute.
2. *Rebasing and discontinuation:* what happened to contracts naming legacy UBOS 2006-base basic-heading indices when UBOS moved to CIPI 2016/17 = 100? Splicing choices and their money effect.
3. *Weights:* how dispersed are bidder-proposed weights across contracts for the same work type, and what do they do to the adjustment?
4. *Commencement and caps:* what share of escalation falls in the 18-month dead band and above the 10% cap, especially in the 2022 shock?
5. *Determinable at tender:* a "tender index pack" naming source, series, splice rule and BoQ-derived weights.

**Found so far.**

- *Contract formulas (Projects B, C, D; OCR of signed contracts, confidential).*
  - Separate formulas per bill: drainage, earthworks, bituminous, ancillary, structures.
  - Indices named: labour, equipment, cement, reinforcement steel, bitumen, fuel, metal products (and explosives in B). All are UBOS construction-sector "basic heading" indices (Jan–Mar 2006 = 100), except bitumen in C, which is priced from Dubai.
  - Non-adjustable portion a = 0.20 everywhere; weights are bidder-proposed (e.g. fuel 0.35 in D's earthworks; bitumen 0.45 in C).
  - 49-day index lag. **No adjustment for the first 18 months after the Base Date** (B, D), i.e. half of a 3-year contract is unprotected. Cap of 10% of the Accepted Contract Amount (B).
- *Index data.* `src/fetch_ubos.py` downloads the UBOS releases; `src/parse_ubos.py` OCRs them and parses six tables per legacy release (29 series):
  - sector indices including roads (paved), roads (gravel) and civil works;
  - basic headings for cement, steel bars, other iron and steel, diesel, bitumen, labour wage rates, equipment charge-out rates and more.

  Output: `data/ubos_input_indices_vintages.csv` (one row per release × item × month, so revisions are kept).
- *Open issue to test.* UBOS rebased to CIPI 2016/17 = 100 (c. 2022). Contracts that name legacy 2006-base basic-heading indices may have lost their index mid-contract. Check what the modern releases publish (modern-format parser still to write).

**Next.**

1. Finish the download and parse all releases (legacy and modern).
2. Build continuous item series and a revision log.
3. Recompute the formula for B, C and D under alternative index and weight choices, and compare with sector indices (roads paved) and with actual cost paths.
4. Quantify the 18-month dead band and the 10% cap during the 2022 fuel and bitumen shock.

**Clause.** 13.7 Adjustments for Changes in Cost [1999: 13.8], with the Schedule of Cost Indexation (Contract Data).

**What it leaves open.** The formula Pn = a + b·Ln/Lo + c·En/Eo + … depends on:

- which indices are named;
- their weightings, including the fixed non-adjustable element *a*;
- the base date;
- the currency of each element;
- what happens when an index is revised, rebased, delayed or discontinued (provisional indices, later correction).

Disputes arise when the named index does not track what the Contractor actually paid, such as fuel or bitumen in 2022, or when a weighting was inherited from another contract.

**Research questions.**

1. How much does the adjustment on the same contract vary across defensible index and weighting choices?
2. How well does the contractual formula track actual input-cost movements (cost pass-through), and for whom does the error fall?
3. What does index revision, rebasing or discontinuation do to settled adjustments?
4. Which formula specification (index basket, weights from the BoQ, update rule) minimises tracking error and dispute exposure?

**Data and access.**

- UBOS CIPI and its components (in hand from your PhD pipeline).
- UBOS CPI, fuel pump prices, bitumen import prices, cement and steel prices, BoU exchange rates (open).
- BoQs and price-adjustment schedules from contracts (in your files; Projects A–D's Contract Data).

**Method.** Recompute Pn for many contracts (real schedules plus synthetic contracts built from BoQ cost shares) under alternative index sets and weights. Benchmark against a "true cost" series built from BoQ quantities × input prices. Measure tracking error, the share of cost shocks passed through, and the verdict dispersion across choices. Run event studies around the 2022 fuel/bitumen shock and the CIPI rebasing.

**Novelty.** Price-adjustment literature is mostly econometric (escalation forecasting) or doctrinal. No study measures the indeterminacy of the FIDIC formula against actual cost paths in an African market.

**Evidence from practice.** Price-adjustment disputes appear in your claims folders (e.g. variation-of-price items in the Mubende–Mityana Employer's comments). Check the Contract Data of Projects A–D for index schedules.

**Outputs.** Paper. An open "tender index pack" (recommended index basket and BoQ-derived weights by work type) for Uganda.

**Journals.** J. Construction Engineering and Management (ASCE); Construction Management and Economics; J. Legal Affairs & Dispute Resolution.

**Feasibility.** High: data largely in hand. **4–6 months.** **Risks:** limited actual-cost data; mitigate with BoQ-based synthetic cost paths.
