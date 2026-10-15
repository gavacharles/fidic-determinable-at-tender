# Same Pandemic, Different Verdict: Measuring Exceptional Events for FIDIC Clause 18 with Government-Response and Conflict Data

Gavamukulya Charles

*Draft 0.1, 15 October 2026. Paper 7 of "Determinable at tender". Target: Journal of Legal Affairs and Dispute Resolution in Engineering and Construction (ASCE); International Journal of Disaster Risk Reduction.*

## Abstract

**Introduction.** FIDIC Clause 18 (2017; 1999: Clause 19 Force Majeure) relieves a Party prevented by an "Exceptional Event". The event must be exceptional, beyond its control, not reasonably provided against, unavoidable, and not attributable to the other Party. Its duration and its effect on the works decide the extension of time. Clause 18 defines neither how exceptional an event must be nor when it starts and ends. The COVID-19 pandemic and Uganda's 2020–21 election unrest put both questions before Engineers across East Africa.

**Methods.**

- **Restrictions.** Daily Oxford COVID-19 Government Response Tracker (OxCGRT) indicators for Uganda, Kenya, Rwanda and Tanzania (2020–21) are converted into candidate Exceptional Event periods under six defensible triggers: workplace closure, public-transport closure, stay-at-home order, internal movement restriction, international travel ban, and stringency index ≥ 70. These are compared with a granted COVID-19 extension of time on a Ugandan road project (Project A).
- **Unrest.** UCDP georeferenced event data (2000–2023) give the monthly probability of a fatal organised-violence event within 50 km of six project sites.

**Results.**

- **Project A.** The granted window (10 March–20 September 2020; 194 days granted, 230 claimed) begins 12 days before Uganda's first restriction. Within it, the six triggers were in force on 129 to 182 days.
- **Over 2020–21**, Uganda's triggers range from 175 days (public transport) to 647 days (workplace closure).
- **Across countries**, the same pandemic gives Kenya 11–572 days, Rwanda 107–651 and Tanzania 0–94, depending on the trigger.
- **Unrest.** Fatal events near project sites have return periods of 20 months (Kampala) to 288 months (Masindi). UCDP records no Ugandan event in 2020, the year of the November riots, so the choice of event dataset determines whether a "riot" exists at all.

**Discussion.**

- The Exceptional Event test is determinable only once the contract names the trigger: which order, which indicator, which dataset.
- For epidemics, the trigger should be the measure that actually binds on site (for roads, labour movement: public transport and stay-at-home), dated by gazettement.
- For unrest, it should be a recorded event density above a stated site return period, from a named dataset.

## 1. Introduction

Force majeure clauses were written for rare, discrete events. COVID-19 was neither. Governments imposed and lifted overlapping measures for two years, and construction was often exempt in law but constrained in practice through workers' travel, curfews and import delays.

FIDIC 2017 Clause 18 requires an event that is "exceptional", beyond control and unavoidable. It then grants time for any delay "by reason of" it (18.4), with notice within 14 days after the Party became aware (18.2). Both the "exceptional" threshold and the event's duration are left to evidence, so Engineers have to construct them case by case.

Paper 0 showed that for weather, the verdict depends on the data product and baseline chosen. This paper asks whether the same holds for man-made Exceptional Events, and what objective triggers a contract could name.

## 2. Data

- **OxCGRT** (Hale et al. 2021): daily ordinal policy indicators for Uganda, Kenya, Rwanda and Tanzania, 1 January 2020 to 31 December 2022. The indicators used are C2 workplace closing, C5 public transport, C6 stay at home, C7 internal movement, C8 international travel and the composite stringency index.
- **UCDP GED v24** (Sundberg & Melander 2013): georeferenced events of organised violence (state-based, non-state, one-sided) with best-estimate fatalities, East Africa, 1989–2023.
- **Project A** (anonymised; FIDIC 1999 Yellow Book, MoWT conditions): EOT 3 COVID-19 head. The Contractor claimed 230 days; the Engineer granted 194 days for 10 March–20 September 2020, concurrent with possession delay.
- **Sites:** Masindi and Hoima (Project A), Kiboga and Busunju (Project B), Kampala (Project E), Kapchorwa (Project D).

## 3. Methods

- **Candidate event periods.** For each country and trigger: the days in force in 2020–21, the first and last day, and the days within Project A's granted window. The thresholds are:
  - C2 ≥ 2 (closing required for some sectors);
  - C5 ≥ 2 (closed);
  - C6 ≥ 2 (required, except essentials);
  - C7 ≥ 2 (restrictions in place);
  - C8 ≥ 3 (bans on some regions);
  - stringency ≥ 70.
- **Unrest baseline.** For each site, the share of months in 2000–2023 with at least one fatal UCDP event within 50 km. The return period is the inverse of that share.

## 4. Results

**The granted window starts before any restriction.** Uganda's first measures were an international travel ban on 22 March and workplace and public-transport closures on 25 March 2020. The granted window opens on 10 March, 12 days before any restriction (pilot, `results/covid_claim_days.csv`).

**Within the window, the verdict depends on the trigger.** Of the 195 days from 10 March to 20 September 2020, Uganda had:

| Trigger | Days in force |
|---|---|
| International travel ban | 182 |
| Workplace closure | 180 |
| Stay-at-home order | 175 |
| Stringency ≥ 70 | 175 |
| Internal movement restriction | 174 |
| Public-transport closure | 129 |

The 194 days granted exceed every trigger, and the 230 days claimed exceed the window. Public transport, which governs labour movement on rural road sites, was closed on only two-thirds of the window. Some site-relevant restriction applied on 180 days.

**Over the pandemic, the spread widens.**

- In Uganda over 2020–21, triggers were in force from 175 days (public transport) to 647 days (workplace closure; Fig. 1).
- A contractor relying on the stay-at-home order (621 days) could claim an event lasting most of the contract. On public-transport closure it would be less than six months in 2020, plus a 2021 lockdown.

**Across East Africa, the same pandemic gives different events.**

| Country | Public-transport closure | Stay-at-home order | Workplace closure |
|---|---|---|---|
| Rwanda | 107 days | 651 days | 651 days |
| Kenya | 11 days | 572 days | 411 days |
| Tanzania | 0 days | 0 days | 0 days |

Tanzania's only coded measure was an international travel ban (94 days). A contractor with sites in two countries faces two different Exceptional Events from one pandemic.

**Unrest: how exceptional is a riot?**

- Monthly probabilities of a fatal organised-violence event within 50 km range from 0.3% (Masindi; return period 288 months) to 4.9% (Kampala; 21 months) and 4.2% (Busunju; 24 months).
- Busunju and Kampala recorded 8 and 9 events in 2020–21, all in 2021.
- UCDP records no event anywhere in Uganda in 2020. The 18–19 November 2020 protests, in which more than 50 people were killed, do not appear, because riots and repression of protest fall largely outside UCDP's organised-violence definitions.
- A claim for "riot, commotion or disorder" in November 2020 would therefore be exceptional or invisible depending on the dataset chosen (UCDP, ACLED or press reports).

## 5. Discussion

**The event is a construct of the indicator.** As with rainfall (Paper 0), the facts are well recorded; it is the contract that fails to say which fact counts. Engineers then fill the gap with whatever the parties propose. Here that was a window opening before any order, and longer than every candidate trigger.

**A determinable Exceptional Event clause.** Particular Conditions can name:

1. **For epidemics and government action:** the binding measure, the source and the dates. For example: "a gazetted order closing public transport or requiring persons to stay at home in the district of the Site, from the date of the order to the date of its revocation." OxCGRT-type coding or the national gazette fixes the start and end.
2. **For unrest:** an event-density trigger. For example: "fatal events within 50 km of the Site exceeding the 1-in-N-month level for the Site in [named dataset]", with N stated (e.g. 10 years) and the dataset's coverage of riots and protests stated.
3. **Effect, separately:** the trigger establishes the event. Delay to completion still requires programme evidence, and concurrency with Employer delays, such as possession on Project A, must be dealt with expressly.

**Notice.** With a named trigger, awareness (18.2, 14 days) runs from the publication of the order or dataset entry, linking to the notice clock of Paper 6.

## 6. Limitations

- One granted COVID claim. Indicator codings are national; sub-national measures (district lockdowns) are partly captured.
- UCDP's scope is organised violence. ACLED, which codes riots and protests, requires registration and is the next step.
- The effect on progress is not modelled; programme records would be needed.

## Figures and tables

- Fig. 1 `figures/fig_ea_compare.png`
- Pilot: `figures/fig_covid_claim.png`, `results/covid_claim_days.csv`
- `results/ea_indicator_days.csv`, `results/ucdp_site_baseline.csv`

## References

[To compile: FIDIC 1999 Clause 19; FIDIC 2017 Clause 18; Hale et al. (2021) Nature Human Behaviour (OxCGRT); Sundberg & Melander (2013) J. Peace Research (UCDP GED); Raleigh et al. (2010) ACLED; case law on force majeure and COVID-19 (e.g. *Classic Maritime v Limbungan* [2019] EWCA Civ 1102).]
