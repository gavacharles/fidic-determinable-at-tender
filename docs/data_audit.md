# Data audit (15 October 2026)

| Paper | Data in hand | Open sources (tested) | To obtain | Readiness |
|---|---|---|---|---|
| 01 Price adjustment | CIPI raw observations from UBOS releases (3,439 rows; legacy 2006 base and 2016/17 base; categories incl. roads/railways), CIPI vintages, macro (CPI, energy CPI, FX, CBR, T-bills) in `~/Projects/cipi-tracker`; contract OCR text (BoQs, Contract Data) in the climate-disputes scratchpad | UBOS releases | Price-adjustment schedules (Contract Data) from project files; fuel and bitumen prices | **Ready** |
| 02 Site access | Corridor alignments and buildings (`~/Projects/uganda-trade-corridors/data`); Project A ROW status appendix (OneDrive) | Sentinel-2 via Microsoft Planetary Computer STAC; Google Open Buildings temporal | Handover certificates, possession milestones | Method ready |
| 03 Ground conditions | Site-investigation annexes in contract OCR (to search) | ISRIC SoilGrids WCS (200 OK) | National borehole database (DWRM); 4.12 claim files | Partial |
| 04 Defects and overloading | Contract design reports (B–D); OAG text-mining pipeline | OAG reports, World Bank/AfDB PADs/ICRs, UNRA annual reports (public) | none (no UNRA access; open-data design) | Re-designed |
| 05 Delay damages | Truck and cost scripts and corridor network (trade-corridors); Project B Contract Data (0.05%/day); "Appraising delay damages" memo (OneDrive) | OSM; HDM-4/RONET unit costs (literature) | UNRA traffic counts (AADT) | Ready (modelled traffic) |
| 06 Notice time bar | Climate data and EOT notices and determinations (Projects A–D) | CHIRPS, CPC | More dated notices | **Ready (pilot)** |
| 07 Exceptional Events | Project A COVID-19 claim (230 days) | OxCGRT (200 OK), UCDP GED (200 OK) | ACLED needs an API key (alternative: UCDP) | **Ready** |
| 08 Forces of nature | Rainfall, flood models, DEMs (`~/uganda-rainfall-climate`) | CHIRPS, river gauges (partial) | Damage events from monthly reports | Partial |
| 09 Delayed payment | Macro rates (CBR, T-bills, lending) in cipi-tracker; OAG text-mining pipeline | BoU, Auditor General reports | IPC and payment dates (project files, OAG reports) | Partial |
| 10 Rate of progress | Monthly reports (Busunju CMR folder, OneDrive) | Sentinel-2 | Completed-contract progress histories (OAG) | Partial |

## Acquisition sweep (15 October 2026)

| Paper | Acquired (local, `data/` or `shared_data/raw/`, not committed) | Script |
|---|---|---|
| 01 | 60 UBOS CSI/CIPI releases (2017–2026), OCR and parsed: legacy 2016–2022 and CIPI 2022–2026 series, vintages | `papers/01…/src/fetch_ubos.py`, `parse_ubos.py`, `build_series.py` |
| 02 | OSM roads per project area (from the Geofabrik Uganda extract); Sentinel-2 L2A scene catalogue 2017–2025 (Planetary Computer) | `papers/02…/src/fetch_osm_stac.py` |
| 03 | SoilGrids 2.0 clay, sand, silt, bulk density, CEC at 0–5, 15–30 and 60–100 cm (Uganda) | `papers/03…/src/fetch_soilgrids.py` |
| 04, 09, 10 | OAG consolidated annual reports (all years on oag.go.ug); World Bank PADs, ICRs and ICRRs for Ugandan road and transport projects (89 documents) | `shared_data/src/fetch_oag.py`, `fetch_worldbank.py` |
| 07 | OxCGRT (UG, KE, TZ, RW), UCDP GED v24.1 (East Africa) | `papers/07…/src/fetch.py` |
| 08 | HydroRIVERS (26,302 reaches, Uganda + buffer); news headlines corpus (96,329 headlines, 2015–2025, `~/Projects/uganda-urban-headlines`) | `papers/08…/src/fetch_hydro.py` |
| 06 | Climate data from Paper 0 (CHIRPS, CPC, ARC2, POWER) | (Paper 0 repo) |

**Confidential project documents** (OneDrive MOWT, UNRA claims, KCCA price-adjustment case, Masindi–Biiso records) are read in place per paper; a bulk local copy needs the author's explicit permission. Needed:

- P1: KCCA "Sources of Indices" memorandum and opinion; B and C adjustment tables (already in OCR).
- P3: site-investigation and materials reports.
- P5: Busunju design review report (traffic).
- P6: dated notices and claim letters (UNRA claims correspondence).
- P8 and P10: monthly progress reports (Busunju CMR and Reports folders).
- P9: IPC certificates and payment dates.

**Not available:** UNRA internal data (axle loads, traffic counts, IRI); ACLED (API key); GloFAS (CDS key).

**Confidential documents located and text-extracted (read in place; text kept outside the repository):**

| Paper | Document | Contents |
|---|---|---|
| P1 | KCCA KCRRP Lot 1 (Lubaga and Makindye) memorandum on Sub-Clause 13.8 | Text. The two KCCA letters (sources of indices; legal opinion) are scans, to OCR. |
| P3 | Masindi–Biiso Soil and Materials Report; Geotechnical Assessment Report (Sep 2020) | CBR by homogeneous section, geology |
| P4 and P5 | Busunju–Kiboga–Hoima design review report | ADT at 4 count stations, ESAL factors, design CESA |
| P10 | Busunju Monthly Progress Report No. 23 (Jul 2025) | Planned 87.5% vs actual 21.2% physical progress |
| P10 | Busunju status report (Aug 2025) | Text |
| P10 | Masindi–Biiso MPR No. 34 (Mar 2022) | Scan, to OCR |
| P6 | Project A notice CRSG-0247 (land acquisition delays) | Scan, to OCR; DAB notices |
| P9 | Project A IPC No. 30 workbook (xlsx) | To read |
