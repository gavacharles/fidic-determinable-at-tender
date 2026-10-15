"""Download open event data for Uganda and East Africa.

  oxcgrt_uganda.csv  Oxford COVID-19 Government Response Tracker, national daily indicators (Uganda, Kenya,
                     Tanzania, Rwanda), 2020-2022
  ucdp_ged_ea.csv    UCDP Georeferenced Event Dataset v24.1, events in Uganda and neighbours
"""
import io
import zipfile
from pathlib import Path

import pandas as pd
import requests

OUT = Path(__file__).resolve().parents[1] / "data"
OXCGRT = "https://raw.githubusercontent.com/OxCGRT/covid-policy-dataset/main/data/OxCGRT_compact_national_v1.csv"
UCDP = "https://ucdp.uu.se/downloads/ged/ged241-csv.zip"
COUNTRIES = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi", "South Sudan", "DR Congo (Zaire)"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    o = pd.read_csv(OXCGRT, low_memory=False)
    o = o[o.CountryName.isin(["Uganda", "Kenya", "Tanzania", "Rwanda"])]
    o.to_csv(OUT / "oxcgrt_uganda.csv", index=False)
    print("oxcgrt rows", len(o))
    z = zipfile.ZipFile(io.BytesIO(requests.get(UCDP, timeout=600).content))
    name = [n for n in z.namelist() if n.endswith(".csv")][0]
    g = pd.read_csv(z.open(name), low_memory=False)
    g = g[g.country.isin(COUNTRIES)]
    g.to_csv(OUT / "ucdp_ged_ea.csv", index=False)
    print("ucdp rows", len(g), g.country.value_counts().to_dict())


if __name__ == "__main__":
    main()
