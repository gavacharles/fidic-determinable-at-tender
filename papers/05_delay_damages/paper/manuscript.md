# One Rate for Every Road? Testing the Proportionality of FIDIC Delay Damages against the Public Loss from Late Completion

Gavamukulya Charles

*Draft 0.1, 15 October 2026. Paper 5 of "Determinable at tender". Target: Journal of Legal Affairs and Dispute Resolution in Engineering and Construction (ASCE); Transport Policy.*

## Abstract

**Introduction.** FIDIC Sub-Clause 8.8 (1999: 8.7) fixes delay damages at a daily rate stated in the Contract Data, up to a maximum. Ugandan road contracts almost uniformly state 0.05% of the Contract Price per day, capped at 10%. Whether such a clause is enforceable or a penalty depends on whether it is proportionate to the Employer's legitimate interest (*Cavendish Square Holding v Makdessi* [2015] UKSC 67). Yet the rate is set without reference to the road's value, and its proportionality is argued only when damages are deducted.

**Methods.**

- The public loss from a day of late completion is the deferred first-year benefit of the road.
- This is recovered from the economic internal rates of return (EIRR) reported in World Bank appraisal and completion documents for 21 Ugandan road investments (1995–2023): rural trunk, peri-urban and Kampala urban roads.
- A standard appraisal profile is used: 3-year construction, 20-year life, benefit growth 3–7%.
- The Employer's prolongation cost of supervision is added.
- The result is compared with the rate in the Contract Data of five FIDIC road contracts (Projects A–E).

**Results.**

- The 0.05% rate is equivalent to an 18.25% first-year return, i.e. an EIRR of 15.6–18.9%.
- For rural trunk roads the implied daily loss is 0.037–0.064% of project cost, so the uniform rate is 0.8–1.4 times the loss.
- For Kampala urban and peri-urban roads with high returns (EIRR 27–55%), the loss is 0.09–0.23% per day, and the rate recovers only 21–57% of it.
- The 10% cap is reached after 200 days. Delays on the programme's projects run to 500–850 days.

**Discussion.**

- The penalty argument against 0.05% per day fails for typical rural trunk roads: the rate is close to a genuine pre-estimate.
- The real disproportion runs the other way. On high-value urban roads, and on any delay beyond 200 days, the public loss is largely uncompensated and the Contractor's incentive to finish ends at the cap.
- A rate derived from the road's own appraisal (rate = first-year return / 365) is determinable at tender, defensible as a pre-estimate, and costless to compute.

## 1. Introduction

Delay damages are the Employer's remedy for late completion. Under FIDIC 1999 Sub-Clause 8.7 (2017: 8.8):

- the Contractor pays "the amount stated in the Contract Data" for every day between the Time for Completion and the date of the Taking-Over Certificate;
- the total is limited to the maximum stated;
- the damages are "the only damages due from the Contractor for such default" (other than on termination).

The Uganda Ministry of Works and UNRA conditions fill both blanks the same way on almost every road contract: 0.05% of the Contract Price per day, maximum 10%.

The rate is challenged as a penalty whenever damages are deducted. The modern test (*Cavendish*; followed in common-law jurisdictions including Uganda) asks whether the clause is a secondary obligation imposing a detriment "out of all proportion to any legitimate interest of the innocent party in the enforcement of the primary obligation". For a public road the legitimate interest is plainly wider than the Employer's own costs: it is the public benefit the road was built to deliver. That benefit is quantified, road by road, in the economic appraisal that justified the investment. The proportionality question can therefore be answered with numbers, and at tender.

## 2. Data

- **Contract Data.** Delay-damages rate and cap in five FIDIC road contracts (Projects A–E, 2013–2020). All five state 0.05% of the (final) Contract Price per day with a 10% cap. Projects B and E also impose milestone damages at the same daily rate, for failing to complete 30% of the road length (B) or 40% of the works (E) within 60% of the original contract period.
- **Economic returns.** 21 EIRRs (13 appraisal, 8 completion) for 12 Ugandan road investments, from World Bank project appraisal documents and implementation completion reports:
  - Road Sector Programme;
  - RDP Phases 1–3;
  - Transport Sector Development Project;
  - North Eastern Road-corridor Asset Management Project (NERAMP);
  - Albertine Region Sustainable Development Project;
  - Kampala Institutional and Infrastructure Development Project 2 (KIIDP 2).

  Each is classed as rural trunk, peri-urban trunk or urban (`data/eirr_roads.csv`).
- **Delays.** Possession delay periods in the programme's projects (Paper 2): 472–849 days claimed on Project A.

## 3. Methods

**Daily public loss.** With construction cost sunk, a day's delay in opening defers the whole benefit stream by a day. To first order, the loss is the first-year benefit B₁/365; the benefits regained at the end of the asset's life are negligible after discounting. Expressed as a share of project cost C, the daily loss is FYRR/365, where FYRR = B₁/C is the first-year rate of return.

**FYRR from EIRR.** Appraisal documents report EIRR, not FYRR. FYRR is recovered by solving NPV(EIRR) = 0 for a standard appraisal profile:

- cost spread evenly over three years;
- benefits from opening for 20 years, growing at g = 5% a year (sensitivity 3% and 7%);
- no residual value.

**Employer's own cost.** Supervision consultancy of about 6% of works cost over a 3-year contract adds 0.0055% per day.

**Comparison.** The ratio of 0.05% per day to the daily loss; the EIRR at which the two are equal; and the share of the public loss recovered before the 10% cap.

## 4. Results

**The rate's implied return.** 0.05% per day is 18.25% of the Contract Price a year. Net of supervision, it equals the daily loss of a road with an EIRR of 17.2% (15.6–18.9% across the growth sensitivities, Fig. 1b). That sits just above the 12% hurdle used in Ugandan appraisals, and is typical of rural trunk upgrading.

**Rural trunk roads: close to a pre-estimate.** Across the 17 rural and peri-urban trunk cases with EIRR of 12.5–21.3%, the daily loss is 0.037–0.064% of cost (Fig. 1a). The contractual rate is 0.8–1.4 times the loss:

- slightly above it for low-return roads (Kampala–Entebbe 12.7%; NERAMP 13.4%);
- slightly below it for the higher-return rural roads (Soroti–Dokolo–Lira and Vurra–Arua–Koboko–Oraba at appraisal, about 21%).

None of these supports a finding that the rate is "extravagant" or "out of all proportion".

**Urban roads: under-compensation.**

- Kampala's urban roads (KIIDP 2, EIRR 46–53%) imply a daily loss of 0.18–0.22% of cost, and Kampala–Gayaza–Zirobwe at completion (EIRR 55%) 0.23%.
- The uniform rate recovers 21–28% of that loss.
- The one urban contract in the sample (Project E) applies the same 0.05% per day.

**The cap ends the incentive.** At 0.05% per day the 10% cap is reached in 200 days. On a rural trunk road the public loss continues at about the same rate thereafter. Project A's claimed possession delays of 472–849 days, if attributable to the Contractor, would leave 58–76% of the loss beyond the cap. For delay beyond 200 days, the Contractor's marginal cost of further delay falls to zero.

**Appraisal and completion differ.** Completion EIRRs differ from appraisal by −6 to +28 points (Soroti–Lira 21.3% to 15.6%; Kampala–Gayaza–Zirobwe 27.5% to 55.4%). A rate fixed at tender from the appraisal is a pre-estimate in the legal sense, a reasonable forecast when made, and does not need to match the outcome.

## 5. Discussion

**Penalty doctrine is the wrong worry.** Contractors' penalty arguments against 0.05% per day do not survive a comparison with the public loss on typical rural roads. The rate is, by accident or design, close to the value of a day of a road with an 18% return. The doctrinal debate (pre-estimate vs legitimate interest) matters less than the empirical one: once the public benefit is accepted as the legitimate interest, the uniform rate is proportionate for the median road.

**The disproportion runs the other way.** On high-value roads (urban and peri-urban, high-traffic corridors) the rate captures a fraction of the loss, and the cap curtails it further. A uniform rate cross-subsidises: it over-protects the Employer slightly on low-return roads and under-protects it heavily on high-return ones, where delay matters most.

**A determinable rule.** The appraisal that justifies the investment already contains everything needed:

> **Delay damages per day = (first-year economic benefit ÷ 365) + Employer's daily prolongation cost**, stated as a percentage of the Contract Price in the Contract Data, with the appraisal reference.

On that basis:

1. The rate is documented as a pre-estimate at tender, which is the strongest possible answer to a penalty challenge.
2. It scales with the road's value. Urban roads would carry 0.15–0.25% per day; rural roads about 0.04–0.06%.
3. The cap should be set as a number of days of expected delay risk (e.g. 365), not a percentage chosen independently of the rate. Alternatively, a termination right should take over at the cap, so the incentive to complete does not vanish.
4. Section and milestone damages should take the section's share of the benefit, not its share of the price.

**Limitations of a public-benefit measure.** Under English law the Employer's legitimate interest in timely completion of a public road includes public benefit (cf. *Cavendish* on interests beyond compensation). A court applying strict compensatory reasoning might confine it to the Employer's own costs, which are far lower (supervision about 0.006% per day plus financing). On that view, every road's 0.05% would look high. The choice between the two views is itself a reason to state the basis in the Contract Data.

## 6. Limitations

- EIRRs come from donor-funded projects. The FYRR conversion assumes a stylised profile; actual benefit profiles (generated traffic, phasing) vary.
- "Project cost" in appraisal is economic cost, not the Contract Price (financial). The ratio is typically about 0.9, so it does not change the conclusions.
- Contract Data from five contracts; a wider sample of rates (including AfDB and Chinese-financed contracts) is planned.
- Delay attribution is not modelled; the cap analysis assumes Contractor-culpable delay.

## Figures and tables

- Fig. 1 `figures/fig_proportionality.png`
- `results/daily_loss.csv`, `data/eirr_roads.csv`

## References

[To compile: FIDIC 1999 and 2017 (8.7/8.8, Contract Data); *Cavendish Square Holding BV v Makdessi*; *ParkingEye v Beavis* [2015] UKSC 67; *Triple Point Technology v PTT* [2021] UKSC 29; World Bank ICR/PAD references by report number (see data file); HDM-4; Ugandan case law on liquidated damages.]
