# Which Index? Source Selection, Rebasing and Dead Bands in FIDIC Price Adjustment: Evidence from Ugandan Road Contracts

Gavamukulya Charles

*Draft 0.1, 15 October 2026. Companion to the author's DAM papers ("Beyond Static Escalation"; "When to Adjust, Not How Much"). Target: Journal of Legal Affairs and Dispute Resolution in Engineering and Construction (ASCE), or Construction Management and Economics.*

## Abstract

**Introduction.** Price adjustment under FIDIC Sub-Clause 13.8 (1999, MDB 2010) and 13.7 (2017) multiplies certified work by a weighted ratio of current to base cost indices. Recent work by the author has questioned the formula's computational form: contemporaneous pass-through, fixed coefficients and publication lag. This paper examines what that work leaves open, the *identity* of the index itself:

- which source governs;
- what happens when the statistical agency rebases or discontinues a series mid-contract;
- which vintage of a revised index applies;
- who sets the weights;
- when adjustment begins.

**Methods.**

- Sixty Uganda Bureau of Statistics (UBOS) construction index releases (2017–2026), mostly scanned, were digitised by OCR into release-by-release series of 29 legacy (2006 = 100) and 18 current (CIPI 2016/17 = 100) indices.
- The parsed base values reproduce those printed in signed contracts to within 0.3%.
- The price-adjustment formulas of three Ugandan road contracts were recomputed under the index choices their administrators faced.
- A "sources of indices" dispute on a fourth contract was reproduced.
- Dead-band and cap effects were simulated for contracts with every Base Date from 2016 to 2023.

**Results.**

- The legacy indices named in contracts were discontinued in June 2022, with three to four months of overlap with their replacements. Splice ratios varied by up to 8% within the overlap, and some inputs had no unique successor.
- Across defensible splice and successor choices, the adjustment multiplier on the same contract differed by 3.8–7.0 percentage points by bill (about UGX 3.6 billion on one contract and 8.0 billion on another).
- Current indices were revised in up to 44% of months, by up to 8.6%.
- In the reproduced dispute, the foreign-currency adjustment was 33.2% on US Bureau of Labor Statistics indices and 17.1% on UBOS indices for the same work.
- Bidder weights departed sharply from the statistical agency's own civil-engineering basket (fuel 6–44% against 3%).
- An 18-month dead band withheld up to 5.4 points of escalation, and a 10% cap bound for 27% of Base Dates on a fuel-heavy bill.

**Discussion.** The index in a price-adjustment clause is not a fact fixed at tender but a set of choices made later, by the Engineer, under provisions that delegate them ("if their source is in doubt, it shall be determined by the Engineer"). A tender index pack fixing series identifiers, successor and splice rules, vintage and weights at tender would make the adjustment determinable and complements dynamic adjustment mechanisms.

## 1. Introduction

Price adjustment clauses reallocate input-price risk from contractor to employer by formula. FIDIC's Sub-Clause 13.8 (13.7 in 2017) is the dominant template in East Africa. The amount payable is the certified value multiplied by

> Pn = a + b·Ln/L0 + c·En/E0 + d·Mn/M0 + …

where a is a fixed non-adjustable share and b, c, d … are weights applied to the ratio of current to base indices for labour, equipment, materials and other inputs, read 49 days before the end of the payment period.

The author's previous work questions the *computational form* of this mapping:

- contemporaneous pass-through and fixed coefficients ("Beyond Static Escalation");
- the value of continuous indexation against trigger-gated revision ("When to Adjust, Not How Much");
- the route by which oil shocks reach site costs ("Brent to Site").

Those studies take the governing index as given.

This paper asks a prior question: **which index?** The clause states that "the cost indices or reference prices stated in the table of adjustment data shall be used". The table, however, is completed by the bidder and names a source and a base value, not a series identifier, a vintage, a splice rule or a successor. When a source is unclear, the MDB 2010 text delegates the matter: "If their source is in doubt, it shall be determined by the Engineer". In Uganda this question became live in 2022, when the Uganda Bureau of Statistics (UBOS) replaced its Construction Sector Indices (Jan–Mar 2006 = 100) with the Construction Input Price Index (CIPI, 2016/17 = 100). That happened in the middle of contracts whose tables named the old series, and just as the 2022 fuel and bitumen shock arrived.

Research questions:

- **RQ1 (sources).** How far do defensible alternative sources change the adjustment on the same contract?
- **RQ2 (rebasing and discontinuation).** What happened to contracts naming discontinued series, and how much do splice and successor choices matter?
- **RQ3 (vintages).** How often and how much are indices revised, and does the vintage used change the adjustment?
- **RQ4 (weights).** How do bidder-proposed weights compare with the statistical agency's own basket for the same work?
- **RQ5 (commencement and caps).** What do the common 18-month dead band and 10% cap withhold, and when?
- **RQ6 (drafting).** What would make the index determinable at tender?

## 2. The clause and its delegations

**FIDIC 1999 Red Book 13.8 and MDB 2010 13.8.** The adjustment uses "the cost indices or reference prices stated in the table of adjustment data". If their source is in doubt, the Engineer determines it, with reference to the values at stated dates. Until a current index is available, the Engineer determines a provisional index and the adjustment is recalculated later. The weightings may be adjusted only if Variations render them "unreasonable, unbalanced or inapplicable". The table is completed by the bidder.

**FIDIC 2017 13.7** moves the formula to a Schedule of Cost Indexation with similar delegations.

**Ugandan practice.** The contracts reviewed add:

- a fixed non-adjustable share a = 0.20;
- separate formulas per bill (drainage, earthworks, bituminous works, ancillary works, structures);
- a 49-day lag;
- "price adjustment shall commence 18 months from the Base Date";
- in one case, a cap on total adjustment of 10% of the Accepted Contract Amount.

None of the tables names a series code, a vintage, a splice rule or a successor.

## 3. Data and methods

### 3.1 UBOS index releases

Sixty monthly and bimonthly UBOS releases (December 2017 – February 2026) were obtained from ubos.org. All are scanned images and were digitised by OCR (Tesseract, 200 dpi):

- Legacy releases give six tables each: two sector tables and four "basic heading" tables (cement, concrete articles, steel bars, roofing sheets, other iron and steel, timber, paint, pipes, water tanks, bricks, electrical cable, aggregate, lime, diesel, bitumen, labour wage rates, equipment charge-out rates and others). Each covers the previous and current year by month.
- CIPI releases give item indices in Annex 1, with bitumen in Annex 3, for the 13 months to the release month.

Every value is kept with its release, so revisions can be measured. OCR digit misreads (e.g. 325.24 read as 925.24) were corrected by majority across releases, or by neighbour interpolation for isolated one-month spikes: 14 corrections in all, logged.

**Validation.** The parsed March 2017 values reproduce the base values printed in Project D's Schedule of Adjustment Data:

| Index | Parsed | Contract |
|---|---|---|
| Labour | 331.84 | 332 |
| Equipment | 279.18 | 279 |
| Cement | 189.93 | 190 |
| Steel bars | 293.10 | 293 |
| Diesel | 207.56 | 208 |
| Bitumen | 179.31 | 179 |
| "Metal products" (= other iron & steel) | 222.1 | 222 |

The June 2019 values reproduce all seven of Project C's base values exactly.

### 3.2 Contracts

Four Ugandan road contracts (anonymised; documents reviewed with permission of the author's practice):

| Project | Form | Base | Formula |
|---|---|---|---|
| **C** (urban arterial) | FIDIC 1999 | June 2019 | One local-currency formula on UGX 161.8 bn of work |
| **D** (rural trunk road) | FIDIC MDB 2010 | March 2017 | Five bill-specific formulas on UGX 63.8 bn |
| **B** (rehabilitation) | FIDIC 2017 | about 2022 | Weights in the Appendix to Bid, not in the contract volume; illustrates the 18-month dead band and the 10% cap |
| **E** (urban roads) | FIDIC MDB 2010 | Nov–Dec 2020; commencement Aug 2022 | Local Table A (UBOS) and foreign Table B (USD 15.9 m, US BLS); subject of a "sources of indices" dispute documented in correspondence, a legal opinion and the author's memorandum |

### 3.3 Recomputations

For C and D, Pn is computed monthly with a two-month index lag under 3 × 4 defensible post-June-2022 choices:

- **successor for "metal products":** high-tensile steel bars, roofing sheets, or nails, bolts and screws;
- **splice rule:** link at the last legacy month, link at the first overlap month, mean overlap ratio, or freeze at the last published value (a common fallback when an index ceases).

For E's foreign-currency formula, Pn is computed with US BLS series (via FRED) against current and bid-printed preliminary base values, and with UBOS series.

For Base Dates from January 2016 to January 2023, a 36-month contract (commencement three months after the Base Date, linear progress) is run through D's earthworks and structures formulas and C's formula. The comparison covers escalation with no dead band and no cap, escalation paid with the 18-month dead band, and escalation paid with the dead band and a 10% cap.

## 4. Results

### 4.1 Rebasing and discontinuation (RQ2)

The legacy basic headings end in June 2022; CIPI items begin in March 2022. Only three to four overlap months exist. Over that short overlap, legacy/CIPI ratios vary by up to 8.1% (roofing sheets), 7.7% (lime) and 6.9% (diesel). Mapping is itself a choice. Legacy "steel bars" and "other iron & steel" both map most naturally to CIPI "high-tensile steel bars", at ratios of 1.846 and 1.787. "Metal products", named in all three contracts with tables, has no unique successor.

Applied to Project D, the defensible choices give multipliers after June 2022 that differ by:

| Bill | Spread (percentage points) |
|---|---|
| Earthworks and pavement layers | 7.0 |
| Ancillary road works | 6.9 |
| Drainage | 4.6 |
| Structures | 4.3 |
| Bituminous layers and seals | 3.8 |

This is about **UGX 3.56 billion** if each bill's work fell in July 2022 – December 2025 (5.6% of the adjustable amount). For Project C the spread is 5.0 points on average and 6.1 points by December 2025, about **UGX 8.0 billion**.

### 4.2 Revisions (RQ3)

CIPI item indices were revised between releases in up to 44% of months (bitumen 43%; plastic pipes 36%), by up to 8.6% (sand) and 5.1% (bitumen). The "index applicable on the date 49 days prior" therefore depends on which release the Engineer consults. Revisions also reach base values. Project E's bid printed the US BLS steel-mill-products index for December 2020 as 191.1, marked preliminary; the current published value is 197.2.

### 4.3 Sources (RQ1): Project E

Project E's Table B names US BLS indices for a USD 15.9 million foreign-currency component. The note under the tables names, for foreign inputs, the official index of "the home country of the majority of the bidder's expatriate workforce" (China) or "the source country of the input" (mostly Uganda). The Employer's legal opinion held the note binding and applied contra proferentem against the bidder who drafted the table. The Engineer proposed UBOS indices for both currencies.

Recomputed for August 2022 – December 2025, the foreign-currency multiplier averages:

- **33.2%** on BLS indices (the Contractor reported 32.19%);
- **17.1%** on UBOS indices (the Contractor reported 21.89%).

The choice of source is therefore worth 11–16 percentage points on the foreign component, about UGX 6–9 billion. The base-value vintage (preliminary vs revised BLS) adds about 0.5 point.

### 4.4 Weights (RQ4)

As shares of the adjustable part, bidder weights range widely across bills and contracts:

| Input | Bidder weights | UBOS CIPI civil-engineering basket |
|---|---|---|
| Fuel | 6–44% | 3% |
| Cement | 6–31% | 4% |
| Equipment | 0–31% | 16% |
| Labour | 12–31% | 11% |
| Bitumen | up to 37% | 27% |
| Aggregate, murram, concrete, pipes and other materials | 0% (no bidder formula includes them) | 34% |

Part of the fuel gap is definitional, since equipment hire includes fuel in the official basket. The fixed share a = 0.20 is identical in every table, suggesting a template value rather than an estimate of non-adjustable cost.

### 4.5 Dead band and cap (RQ5)

In Project D, the 18-month dead band withheld escalation averaging 1.4–3.5% by bill, peaking at 11.6% (earthworks). Across Base Dates 2016–2023, D's earthworks formula would have paid 5.8% of contract value on average (maximum 19.1%) with no dead band or cap. The dead band removed 1.2 points on average (maximum 5.4), and a 10% cap bound in 27% of Base Dates: those running into the 2022 shock, cutting the maximum from 15.7% to 10%. The dead band also withholds *falling* prices: for Project C (Base Date June 2019), prices fell by about 3% on average during the first 18 months.

## 5. Discussion

**The index is chosen after the event.** A price-adjustment table looks like a fixed term, but it names a source and a base value, not a series. When a series is discontinued, revised, or its source is disputed, the clause hands the choice to the Engineer. Each defensible choice moves the adjustment by several percentage points of contract value. The magnitudes found here are comparable to the stabilisation gains of better formula design reported in the author's DAM work, so fixing the index matters as much as fixing the form.

**Rebasing is foreseeable.** Statistical agencies rebase every five to ten years. A contract of three years or more, signed near the end of a base period, will probably straddle a rebasing. The risk is foreseeable and allocable but is not allocated.

**Revisions are not errors.** Statistical revisions are legitimate, but the clause does not say which vintage governs. "Provisional index … recalculated when available" in MDB 2010 implies latest-vintage recalculation, an open-ended reopening of past certificates.

**Bidder weights are strategic.** Weights proposed by bidders, unconstrained by the statistical agency's own basket, allow a bidder to load the inputs it expects to rise. The uniform a = 0.20 shows that one parameter, at least, is a convention rather than an estimate.

**Dead bands and caps are risk allocation, not neutral administration.** They transfer the early-contract and tail escalation risk to the Contractor in rising markets, and the corresponding downside to the Employer in falling ones, without either party pricing it explicitly.

**Relation to DAM.** A dynamic or trigger-gated mechanism still consumes indices. The determinability rules below are a precondition for any mechanism, static or dynamic, to be recomputable by both parties: the admissibility constraint of "Beyond Static Escalation".

## 6. A tender index pack

Five elements, attached to the tender documents by the Employer and binding on bidders:

1. **Series identifiers, not sources.** For each input: the publisher, the publication, the table, the item name and, where available, a series code (e.g. "UBOS CIPI, Annex 1, item 6 'Diesel', 2016/17 = 100").
2. **Successor and splice rule.** If a named series is discontinued or rebased, a stated successor (or the published concordance) applies, chain-linked at the last month of overlap. If no successor exists, the input's weight passes to a stated fallback (e.g. the sector index for civil works).
3. **Vintage rule.** The value first published for the month governs, and later revisions do not reopen certificates. Alternatively, the value published N months later governs, with provisional certification in between.
4. **Weights from the statistical basket or the BoQ.** The Employer publishes weights derived from the official civil-engineering basket, or from the BoQ's cost structure. Bidders may deviate only with priced justification, and a is estimated, not conventional.
5. **Explicit commencement and symmetric bounds.** Adjustment from the Base Date, or a stated dead band with its rationale, and caps applied symmetrically (a collar) with a stated treatment of the tail.

## 7. Limitations

- Three contracts with tables and one dispute are not a sample.
- OCR may leave undetected misreads below the screening thresholds.
- The recomputations assume uniform progress and a two-month lag.
- The China "home country" source in Project E was not computed for lack of an open monthly series.
- The counterfactual adjustments are compared with each other, not with contractors' actual costs. Comparing them with actual costs is the domain of the DAM work.

## 8. Conclusion

The index in a FIDIC price-adjustment clause is less determinate than the clause's wording suggests. In Uganda's road contracts, the series named at tender was discontinued mid-contract, is routinely revised, can be read from more than one defensible source, and is weighted by the bidder. Each open choice moves the adjustment by several points of contract value, the scale of a dispute. A tender index pack fixing identifiers, successors, vintages and weights makes the adjustment determinable at tender and is a precondition for any adjustment mechanism, static or dynamic.

## Figures

- Fig. 1 `figures/fig_contract_D.png`: Project D multipliers under defensible choices
- Fig. 2 `figures/fig_contract_C.png`: Project C
- Fig. 3 `figures/fig_kcca.png`: Project E foreign-currency adjustment by source
- Fig. 4 `figures/fig_weights.png`: bidder weights vs the official basket
- Fig. 5 `figures/fig_deadband_cap.png`: dead band and cap by Base Date

## Tables (results/)

`base_check.csv`, `splice_overlap.csv`, `revisions.csv`, `qc_log.csv`, `contract_C_spread.csv`, `contract_D_spread.csv`, `dead_band_D.csv`, `kcca_summary.csv`, `weights.csv`, `deadband_cap_by_base.csv`

## References

[To compile; verify against primary texts.]

- FIDIC (1999) Red Book; FIDIC (2010) MDB Harmonised Edition; FIDIC (2017) Red Book.
- Gavamukulya, Ogra and Aigbavboa: "Beyond Static Escalation"; "When to Adjust, Not How Much"; "Brent to Site" (working papers).
- UBOS Construction Sector Indices and CIPI releases (2017–2026).
- US Bureau of Labor Statistics, CES and PPI series (via FRED).
- Uganda Contracts Act Cap. 284; Evidence Act s. 93; *Santa Okema v Okumu* (2019); *Euromec v Shandong Taikai* (Kenya, 2020); *Forbes v Git* [1922] 1 AC 256.
