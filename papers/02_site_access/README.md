# Paper 2: Access to the Site: when was possession really given?

*Part of the research agenda* ***Determinable at tender*** *(see ../../docs/research_agenda.md).*

**Status:** scoped

**Clause.** 2.1 Right of Access to the Site [1999: 2.1]; Contract Data milestones for handover of sections. Linked to 8.5 (EOT) and 20.

**What it leaves open.**

- The date access was actually given, section by section.
- Whether partial or encumbered access counts.
- How much of the delay was caused by the Contractor's own document delays (the 2.1 proviso).

Land acquisition and right-of-way encumbrances are the dominant delay cause on Ugandan roads. In Project A, the possession heads (158 days and more) dwarf weather.

**Research questions.**

1. Can satellite imagery establish an objective, section-level date of clearance and possession?
2. How do Engineer-determined possession delays compare with the remotely sensed record?
3. How should contracts define "access" (clearance thresholds, minimum continuous length) to make it verifiable?

**Data and access.**

- Sentinel-2 (10 m, five-day revisit), Planet (research access), Google Open Buildings temporal, the GHSL built-up layer.
- OpenStreetMap; corridor alignments from contract drawings.
- RAP compensation status reports (Project A's "ROW Acquisition Status" appendix is in your files).

**Method.**

- Detect building removal and vegetation clearing along the corridor buffer with change detection (NDVI and built-up indices, time-series breakpoints).
- Derive "cleared length" per 1 km section and month, and compare with handover milestones and EOT determinations.
- Validate against site photographs and handover certificates.

**Novelty.** Remote sensing has been used for progress monitoring, but not to adjudicate *Employer* possession obligations or to quantify encumbrance as a contractual fact.

**Evidence from practice.**

- Project A: EOTs 3, 5 and 7, with possession delays of 472, 765 and 849 days, and the DAB referral on possession and design overlap.
- Other projects: KKAT–CRSG correspondence.

**Outputs.** Paper. A reproducible "corridor clearance tracker" that Engineers could use monthly.

**Journals.** Automation in Construction; J. Legal Affairs & Dispute Resolution; J. Construction Engineering and Management.

**Feasibility.** Medium–high: method from `uganda-trade-corridors`. **6–8 months.** **Risks:** cloud cover (use Sentinel-1 radar); small structures below 10 m resolution (use Planet or Open Buildings).
