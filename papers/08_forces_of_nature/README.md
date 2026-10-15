# Paper 8: Forces of nature and care of the Works: whose flood?

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** first draft, `paper/manuscript.md` (15 Oct 2026).

**Findings.** 34 HydroRIVERS crossings on the Project A and B roads; CHIRPS GEV 1981–2018.

- A 10-year temporary-works standard is exceeded with 27% probability at one structure over 3 years (41% over 5), and 37–59% somewhere on the project.
- Project A, 22 Nov 2019: a 49-year storm on 1-day rainfall at 10 of 13 crossings, but a 4.5-year event on 3-day rainfall.
- Project B to date: ≤ about 10-year (1-day), ≤ 2.6-year (3-day).
- Proposal: state the temporary-works design event (return period, duration, data) in the Contract Data; exceedance at a structure is an Employer's risk.

Scripts: `src/crossings.py`, `src/extract_rain.py` (Paper 0 env), `src/flood_risk.py`.

**Clause.** 17.2 Liability for Care of the Works with Employer's risks in 17.2(d) [1999: 17.3(h)], which covers forces of nature that are Unforeseeable or against which an experienced contractor could not reasonably have taken adequate preventive precautions.

**What it leaves open.** Whether flood, landslide or storm damage to temporary or permanent works was Unforeseeable, and what precautions were reasonable, including temporary works designed to what return period.

**Research questions.**

1. What return period did damaging events have at the site, from rainfall, river-flow and flood models?
2. What return period should temporary works (diversions, culverts, cofferdams) be designed for, given a contract duration?
3. Can a design-standard reference (e.g. temporary works to a 1-in-10-year event over the contract period) make the test determinable?

**Data and access.** CHIRPS and IMERG rainfall; river gauges (Ministry of Water and Environment); flood models and DEMs from `uganda-rainfall-climate` (the Kampala flood work); damage reports in claim files.

**Method.** Rainfall-runoff or flood-frequency analysis at damaged structures; event return periods; the probability of exceedance during the contract (1 − (1 − 1/T)^n) for different temporary-works standards.

**Novelty.** Links hydrological design standards to contractual risk allocation, which is absent from the literature. A sister paper to the weather study, with a different clause.

**Evidence from practice.** Search for washout or damage claims in your files (Projects A–D monthly reports).

**Outputs.** Paper. A temporary-works design-standard clause.

**Journals.** J. Legal Affairs & Dispute Resolution; J. Flood Risk Management; Natural Hazards Review (ASCE).

**Feasibility.** Medium–high. **4–6 months.** **Risks:** few damage events with locations; use case vignettes plus national hazard maps.
