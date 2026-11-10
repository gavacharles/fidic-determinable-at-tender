# fidic-determinable-at-tender

Python code, data, results and drafts for a series of data-driven studies of FIDIC clauses whose tests are decided after the event, each turned into a measurable index using open data from Uganda.

Author: Gavamukulya (Gava) Charles.

## Layout

| Path | What it is |
|---|---|
| `papers/NN_<topic>/` | One folder per study: `README.md` (concept note), `src/`, `data/` (raw data not committed), `results/`, `figures/`, `paper/` |
| `common/` | Shared plotting style and helpers |
| `shared_data/src/` | Shared data fetchers (`fetch_oag.py`, `fetch_worldbank.py`) |
| `docs/` | Research agenda, data audit, related work |
| `requirements.txt` | Python dependencies |

### Studies

| Folder | Clause (FIDIC 2017 [1999]) |
|---|---|
| `papers/00_weather_eot` | 8.5(c) [8.4(c)] and MoWT 1229 (main work in the separate `uganda-climate-disputes` repository) |
| `papers/01_price_adjustment` | 13.7 [13.8] |
| `papers/02_site_access` | 2.1 |
| `papers/03_ground_conditions` | 4.12 |
| `papers/04_defects_overloading` | 11 / 4.1 |
| `papers/05_delay_damages` | 8.8 [8.7] |
| `papers/06_notice_time_bar` | 20.2.1 [20.1] |
| `papers/07_exceptional_events` | 18 [19] |
| `papers/08_forces_of_nature` | 17.2 [17.3] |
| `papers/09_delayed_payment` | 14.8 |
| `papers/10_rate_of_progress` | 8.7 / 15.2 [8.6 / 15.2] |

## Setup

```
pip install -r requirements.txt
```

Each study's scripts are in its own `src/` folder; see that study's README.

## Confidentiality

Project documents are not copied into this repository; where used, they are reported only in anonymised form.
