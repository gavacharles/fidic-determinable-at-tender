# Paper 3: Unforeseeable Physical Conditions: a "foreseeability index"

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** first draft, `paper/manuscript.md` (15 Oct 2026).

**Findings.** Project A subgrade investigation: 62 test pits, soaked CBR95, November 2019.

- CBR95 has no spatial autocorrelation (lag-0.5 km correlation −0.04).
- 84–100% of poor subgrade (CBR95 < 8%) is unforeseen from neighbouring pits at every spacing (1–10 km); the share of poor ground (13% < 8%; 31% < 10%) is estimable.
- SoilGrids is a weak predictor (best AUC 0.64).
- Groundwater was recorded at only 2 pits, during the exceptional 2019 short rains.
- Proposal: a quantity-based ground baseline at tender.

Scripts: `src/parse_testpits.py`, `src/foreseeability.py`, `src/soil_predictor.py`, `src/fetch_soilgrids.py`.

**Clause.** 4.12 Unforeseeable Physical Conditions [1999: 4.12], with 4.10 Use of Site Data and 4.11 Sufficiency of the Accepted Contract Amount. "Unforeseeable" (1.1.87) means not reasonably foreseeable by an experienced contractor by the Base Date. Climatic conditions are excluded.

**What it leaves open.**

- What an experienced contractor should have inferred from the site data and other available information.
- How much investigation was reasonable.
- The boundary with weather: groundwater raised by rain.

**Research questions.**

1. Given data available at the Base Date, how probable was the encountered condition? Build a foreseeability index.
2. How does site-investigation density (boreholes per km, test pits) change foreseeability, and therefore who bears the risk?
3. Can data separate 4.12 physical conditions from 8.5(c) climatic conditions (e.g. groundwater response to rainfall)?

**Data and access.**

- Geological survey maps (Uganda DGSM); ISRIC SoilGrids (250 m; clay, bulk density, depth to bedrock); groundwater (Ministry of Water and Environment); expansive-soil maps.
- Site-investigation reports in contract documents (Projects A–D annexes).
- Claimed conditions from claim files.

**Method.** Spatial prediction of ground properties from Base-Date data (kriging or random-forest on SoilGrids and boreholes). Compute the probability of the encountered condition (e.g. rock at depth, black cotton soil thickness) at the claimed location. Study how probability falls with investigation density. Test the rain–groundwater link with CHIRPS and water-table records.

**Novelty.** 4.12 is the most litigated FIDIC clause, but the doctrinal test has never been operationalised probabilistically. This is a direct twin of the weather paper.

**Evidence from practice.** Search claims folders for 4.12 claims (rock, unsuitable material, groundwater). Project D's addendum notes that "the available [geology] data is out of date". That is itself evidence of the Base-Date problem.

**Outputs.** Paper. A "ground-risk register at tender" template with probability bands.

**Journals.** J. Legal Affairs & Dispute Resolution; Construction Management and Economics; Engineering Geology (for the method).

**Feasibility.** Medium: needs borehole data from projects. **6–9 months.** **Risks:** few georeferenced boreholes; mitigate with project site-investigation annexes and the national borehole database.
