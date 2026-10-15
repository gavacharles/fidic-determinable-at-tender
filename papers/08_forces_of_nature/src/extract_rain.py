"""Daily CHIRPS rainfall at each river crossing (run with the Paper 0 environment, which holds the CHIRPS cube).
Usage: ~/Projects/uganda-climate-disputes/.venv/bin/python extract_rain.py   Output: data/crossing_rain_daily.csv
"""
import sys
from pathlib import Path

import pandas as pd

D = Path(__file__).resolve().parents[1] / "data"
sys.path.insert(0, str(Path.home() / "Projects" / "uganda-climate-disputes" / "src"))
from common import site_series  # noqa: E402

c = pd.read_csv(D / "crossings.csv")
cols = {}
for r in c.itertuples():
    cols[f"{r.corridor}@{r.chainage_km}"] = site_series(r.lat, r.lon, "CHIRPS")
pd.DataFrame(cols).to_csv(D / "crossing_rain_daily.csv")
print(len(cols), "series")
