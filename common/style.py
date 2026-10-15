"""Plotting style and paths shared by all papers (same palette as the weather paper)."""
from pathlib import Path

import matplotlib as mpl

ROOT = Path(__file__).resolve().parents[1]
INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#fcfcfb"
CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
BLUE = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
RED = ["#fbd5cf", "#f4aa9f", "#ec7f70", "#e34948", "#c13332", "#982524", "#6e1a1a"]

mpl.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF, "figure.dpi": 110,
    "savefig.dpi": 200, "savefig.bbox": "tight", "font.size": 9, "axes.titlesize": 10,
    "axes.titleweight": "bold", "axes.titlelocation": "left", "axes.labelcolor": INK2, "text.color": INK,
    "xtick.color": INK2, "ytick.color": INK2, "axes.edgecolor": GRID, "axes.grid": True, "grid.color": GRID,
    "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False, "lines.linewidth": 2,
    "legend.frameon": False, "axes.prop_cycle": mpl.cycler(color=CAT),
})


def paper_dir(name):
    """Folders for one paper, e.g. paper_dir('01_price_adjustment') -> dict of Paths (created)."""
    d = ROOT / "papers" / name
    out = {k: d / k for k in ("src", "data", "results", "figures", "paper")}
    for p in out.values():
        p.mkdir(parents=True, exist_ok=True)
    return out


def save(fig, folder, name):
    path = Path(folder) / f"{name}.png"
    fig.savefig(path)
    print("wrote", path)
