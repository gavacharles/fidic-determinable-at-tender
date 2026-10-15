# Paper 5: Delay Damages: penalty or pre-estimate?

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** first draft, `paper/manuscript.md` (15 Oct 2026).

**Findings.**

- All five contracts state 0.05% of the Contract Price per day with a 10% cap. That is equivalent to an 18.25% first-year return, or an EIRR of about 17%.
- From 21 World Bank EIRRs for Ugandan roads: the rate is 0.8–1.4× the implied public daily loss on rural and peri-urban trunk roads, so it is close to a genuine pre-estimate, not a penalty.
- On Kampala urban roads it recovers only 21–28% of the loss.
- The cap is reached at 200 days, against 472–849-day delays on Project A.
- Proposal: rate = first-year benefit / 365 + supervision, taken from the road's own appraisal.

Scripts: `src/proportionality.py`; data `data/eirr_roads.csv`.

**Clause.** 8.8 Delay Damages [1999: 8.7]; Contract Data rate (often 0.05% of the Contract Price per day, capped at 10%).

**What it leaves open.** Whether the rate is enforceable: a genuine pre-estimate, or proportionate to a legitimate interest (*Cavendish v Makdessi*; Ugandan courts apply common-law principles). The same percentage is applied to rural and urban roads alike.

**Research questions.**

1. What does a day of late completion actually cost the public (road-user costs: vehicle operating costs, travel time) on Ugandan roads?
2. How does the standard 0.05%/day compare with that loss across the network?
3. What rate rule (traffic-based) would be proportionate and defensible?

**Data and access.**

- Traffic counts (UNRA; the OSM-derived models from `uganda-trade-corridors`).
- Vehicle operating cost models (HDM-4 parameters, World Bank RONET).
- Contract prices and delay-damages rates from tender documents.

**Method.** For each road, compute the daily benefit forgone by comparing the improved and existing road, using HDM-4/RONET unit costs and traffic. Compare with the delay-damages rate × contract price, then map ratios across the network.

**Novelty.** Delay-damages enforceability is doctrinal. An empirical proportionality test across a national network has not been done.

**Evidence from practice.** Project B Contract Data (0.05%/day). "Appraising the Possibility of Levying Delay Damages" (UNRA claims folder) is a ready vignette.

**Outputs.** Paper. A rate calculator for Contract Data.

**Journals.** J. Legal Affairs & Dispute Resolution; Transport Policy; J. Construction Engineering and Management.

**Feasibility.** High. **3–5 months.** **Risks:** traffic data gaps; mitigate with modelled traffic.
