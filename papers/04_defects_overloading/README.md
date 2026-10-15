# Paper 4: Defects, design and overloading: who broke the road?

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** first draft, `paper/manuscript.md` (15 Oct 2026).

**Findings.**

- Project B design traffic recomputed over 168 defensible input combinations: 2.7–41 MESA (five traffic classes).
  - The axle-load survey choice alone gives ×3.4.
  - Project VEFs are 2.5–3.4× those of other Ugandan surveys and above legal-limit loading, so overloading is built into the design baseline.
- Only 41% of OSM trunk and primary length is on a corridor with a fixed weighbridge (OAG 2025: 5 of 37 corridors); none of the 218 km of Project A and B roads is.
- Proposal: a design-traffic baseline in the Contract, WIM monitoring in the DNP, and a load-adjusted defects test.

Scripts: `src/cesa.py`, `src/weighbridge.py`.

**Originally:** scoped. **Re-designed for open data**: no UNRA data access (15 Oct 2026).

**Open-data design.**

- (i) *Auditor General* annual and value-for-money reports (FY2017/18–2024/25): text-mine defects within the DNP, premature failure, overloading and axle-load control findings by project (reuse the author's OAG text-mining pipeline).
- (ii) *World Bank / AfDB project documents* (PADs, ICRs, PCRs, all public): design traffic and ESALs vs traffic reported at completion, economic analysis, pavement performance notes.
- (iii) *Contract design reports* in project files: design traffic class and ESALs (Projects B–D).
- (iv) *UNRA annual and performance reports* (public PDFs): published axle-load statistics and the share of overloaded vehicles.

**Revised question.** Do public audit and project records show systematic design-load exceedance and early defects? How does the DNP liability regime allocate that risk? Feasibility is now medium (text and document mining); scope is national and comparative rather than measured loading per road.

**Clause.** 11 Defects after Taking Over (11.1–11.4), 4.1 (Yellow Book, fitness for purpose), and the Employer's risks relating to use and occupation. In practice the question is whether early pavement failure is a design, workmanship or overloading problem.

**What it leaves open.** Causation of defects within the Defects Notification Period: actual traffic loading against design loading, maintenance, drainage.

**Research questions.**

1. How much did actual cumulative axle loading (ESALs) exceed design loading on Ugandan national roads?
2. Can loading data apportion responsibility for early failures?
3. What contract mechanism (load-adjusted defects liability, axle-load monitoring obligation) would make causation determinable?

**Data and access.**

- UNRA axle-load control and weighbridge statistics, traffic counts (request; some published in annual reports).
- Pavement roughness (IRI) and condition surveys (UNRA; World Bank RONET).
- Design traffic from pavement design reports (in contract documents).

**Method.** Compare design ESALs with observed ESALs from traffic and axle-load surveys. Estimate the expected service life under observed loading with mechanistic-empirical models. Relate condition deterioration to loading, and build a causation-apportionment model for defects claims.

**Novelty.** Engineering literature studies overloading and deterioration. Nobody has connected this to contractual defect liability and dispute allocation.

**Evidence from practice.** Defects and guardrail or road-sign claims in UNRA folders. Look for DNP disputes in your files.

**Outputs.** Paper. A proposed "load-adjusted defects" clause and monitoring protocol.

**Journals.** J. Infrastructure Systems (ASCE); International Journal of Pavement Engineering; J. Legal Affairs & Dispute Resolution.

**Feasibility.** Medium–low: depends on UNRA data access. **8–12 months.** **Risks:** data access; mitigate through partnership with UNRA or the Ministry of Works.
