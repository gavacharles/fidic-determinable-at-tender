# Paper 7: Exceptional Events: how exceptional was it?

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** first draft, `paper/manuscript.md` (15 Oct 2026).

**Deepening (`src/ea_compare.py`).**

- **Uganda 2020–21:** COVID triggers were in force from 175 days (public transport) to 647 days (workplace closure). Kenya 11–572 days; Rwanda 107–651; Tanzania 0–94.
- **Project A window:** the triggers covered 129–182 days, against 194 granted and 230 claimed.
- **UCDP baseline:** return periods for fatal events within 50 km of project sites run from 21 months (Kampala) to 288 months (Masindi). UCDP records no Ugandan event in 2020 (the November riots are invisible), so dataset choice decides whether unrest exists.

**Pilot result (Project A COVID-19 claim; `src/covid_claim.py`, `results/covid_claim_days.csv`, `figures/fig_covid_claim.png`).**

- The window granted (10 Mar – 20 Sep 2020, 195 days; 194 granted, 230 claimed) begins 12 days before Uganda's first restriction (international travel ban 22 Mar; workplace and public-transport closure 25 Mar).
- Within the window, some site-relevant restriction applied on 180 days, but public transport was closed on only 129.
- Construction was allowed to continue with workers on site, so the binding restriction matters.
- On OxCGRT coding, "workplace closing required" and "stay at home" persist to end-2021: they also capture closures of other sectors and curfews. **Which indicator defines the event is itself an open choice** ("same pandemic, different verdict"), directly parallel to the rainfall-product finding in Paper 0.

**Next.** UCDP unrest-event return periods by site and month (2020–21 election period); compare with other Exceptional Event claims in the files; East Africa comparison (Kenya, Tanzania, Rwanda in OxCGRT).

**Clause.** 18 Exceptional Events [1999: 19 Force Majeure]: an event beyond a Party's control, which could not reasonably have been provided against, could not reasonably have been avoided once it arose, and is not substantially attributable to the other Party. Listed examples include riot, commotion and natural catastrophes.

**What it leaves open.** Whether unrest, election violence, epidemics or floods meet the test, and the extent of the effect on the works.

**Research questions.**

1. How unusual, for place and time, were the events claimed (unrest, COVID-19 restrictions, floods), measured against historical event data?
2. Do claimed durations match the measured duration and intensity of the event?
3. What objective trigger (event density thresholds, government-order dates) could Particular Conditions adopt?

**Data and access.**

- ACLED (conflict and unrest events, geolocated, dated; free registration).
- Oxford COVID-19 Government Response Tracker; Google mobility (archived).
- Flood return periods from the rainfall project.
- Gazette dates of government orders.

**Method.** Event-density anomalies within a radius of the site against a 10-year baseline, using a return-period approach as in the weather paper. Restriction stringency timelines are compared with claimed periods.

**Novelty.** No empirical treatment of force-majeure or Exceptional Event claims exists. COVID-19 claims make this timely.

**Evidence from practice.** Project A: 230 days claimed for COVID-19 (10 Mar – 20 Sep 2020), 194 granted, overlapping possession delay. Ideal for comparing the stringency timeline with the claim.

**Outputs.** Paper. An "exceptional event trigger" annex.

**Journals.** J. Legal Affairs & Dispute Resolution; International Journal of Disaster Risk Reduction; Construction Management and Economics.

**Feasibility.** High. **4–6 months.** **Risks:** attribution of delay to the event; use the case-file programme evidence.
