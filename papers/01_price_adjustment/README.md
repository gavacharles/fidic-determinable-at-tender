# Paper 1: "Which index?" Sources, rebasing and dead bands in price adjustment (companion to DAM)

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** full first draft, `paper/manuscript.md` (15 Oct 2026). **Repositioned** after review of the author's DAM work (see ../../docs/related_work.md).

**Positioning.** The DAM papers ("Beyond Static Escalation"; "When to Adjust, Not How Much"; "Brent to Site") address the *computational form* of 13.8/13.7: lag, coefficient stability, publication lag, triggers and caps. This paper addresses what they leave open: **the identity and governance of the index itself**. Which source, which series, what happens when the statistical agency rebases or discontinues it, who chooses the weights, and when adjustment starts. It cites and builds on DAM rather than re-estimating escalation dynamics.

**First results (15 Oct 2026).**

- **Parser validated against a signed contract.** Parsed March 2017 legacy values match the base values printed in Project D's Schedule of Adjustment Data:

  | Index | Parsed | Contract |
  |---|---|---|
  | Labour | 331.84 | 332 |
  | Equipment | 279.18 | 279 |
  | Cement | 189.93 | 190 |
  | Steel bars | 293.10 | 293 |
  | Diesel | 207.56 | 208 |
  | Bitumen | 179.31 | 179 |
  | Metal products (= other iron & steel) | 222.1 | 222 |

  (`results/base_check.csv`)
- **Rebasing.** Legacy basic headings end in June 2022; CIPI 2016/17 items begin in March 2022. Only 3–4 overlap months are available to splice, and the splice ratio varies by up to 7–8% within them (roofing sheets 8.1%, lime 7.7%, diesel 6.9%). Mapping is a choice: legacy steel bars and "metal products" have several defensible CIPI successors. (`results/splice_overlap.csv`)
- **Revisions.** CIPI items are revised in 20–40% of months across releases (bitumen 43%), by up to 3–8%. The "index 49 days before" therefore depends on the vintage used. (`results/revisions.csv`; legacy revisions above 20% are probable OCR errors, to screen.)
- **Contract D recomputed** (`src/contract_recompute.py`; 3 successor mappings × 4 splice rules, including freezing at the last published value):
  - after June 2022, Pn differs by **4–8 percentage points** across defensible choices (earthworks 7.0–7.3; ancillary 7.6–8.1);
  - about **UGX 3.6 bn** spread if each bill's work fell in Jul 2022 – Dec 2025, on about UGX 64 bn of adjustable work (5.6%);
  - **18-month dead band:** unpaid escalation averaged 1.4–3.5% by bill, peaking at **11.6%** (earthworks, fuel-heavy).

  (`results/contract_D_spread.csv`, `results/dead_band.csv`, `figures/fig_contract_D.png`)

**Deep-phase additions (15 Oct 2026).**

- OCR cleaning: 14 corrections (8 cross-release digit misreads, 6 spikes), logged in `results/qc_log.csv`.
- Project C recomputed: base Jun 2019; all 7 base values match UBOS exactly. Spread up to 6.1 points; about UGX 8.0 bn.
- Project E, the KCCA "sources of indices" dispute (Table B US BLS vs UBOS):
  - foreign-currency adjustment 33.2% (BLS) vs 17.1% (UBOS); the Contractor reported 32.19% / 21.89%;
  - the BLS base was preliminary (steel 191.1 → 197.2 revised);
  - the MDB 2010 clause says "if their source is in doubt, it shall be determined by the Engineer".
- Weights vs the UBOS civil-engineering basket: fuel 6–44% vs 3%; no bidder includes aggregate, murram, concrete or pipes (34% of the basket); a = 0.20 everywhere.
- Dead band and cap by Base Date 2016–2023: D earthworks loses 1.2 points on average (max 5.4) to the dead band; the 10% cap binds for 27% of Base Dates.

**Remaining.**

- China source for E (needs a Chinese index series).
- Project B weights (Appendix to Bid not in the volume).
- Reference list.
- Clearance of case material with the parties.

**Original to-do (superseded).**

- Outlier screen for OCR misreads (e.g. a one-month dip around Aug 2019).
- Parse the 4 unparsed CIPI releases.
- Apply to Projects B and C (C includes Dubai bitumen).
- KCCA "sources of indices" case.
- Weight dispersion across contracts.
- Cap analysis.

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
