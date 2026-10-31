"""Publication multi-panel figure template (matplotlib).
- theme via rcParams (one sans-serif family, sizes in pt at FINAL size)
- exact mm sizing, automatic a/b/c (or A/B/C) panel labels aligned top-left
- export PDF (fonts embedded, Type 42), SVG (editable text), TIFF (dpi)
Data are SIMULATED (see simulate_data.py)."""
import argparse, os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from simulate_data import growth, survival, cfu

MM = 1/25.4
JOURNAL = {  # width_single, width_double (mm), label case, label size, base font
    "nature":   dict(single=89, double=183, case="lower", label=8, base=7),
    "cell":     dict(single=85, double=174, case="upper", label=9, base=7),
    "elsevier": dict(single=90, double=190, case="lower", label=8, base=7),
    "plos":     dict(single=132, double=190.5, case="upper", label=10, base=8),
}
OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]

def set_theme(base=7, family=("Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"), cjk=False):
    fam = list(family)
    if cjk: fam = fam[:1] + ["Noto Sans TC", "Noto Sans CJK TC", "Noto Sans CJK JP"] + fam[1:]
    plt.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": fam, "font.size": base,
        "axes.titlesize": base, "axes.labelsize": base, "xtick.labelsize": base-1, "ytick.labelsize": base-1,
        "legend.fontsize": base-1, "legend.frameon": False,
        "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": .6,
        "xtick.major.width": .6, "ytick.major.width": .6, "xtick.major.size": 2.5, "ytick.major.size": 2.5,
        "lines.linewidth": 1.0, "axes.prop_cycle": matplotlib.cycler(color=OKABE_ITO),
        "pdf.fonttype": 42, "mathtext.default": "regular", "ps.fonttype": 42, "svg.fonttype": "none",
        "savefig.dpi": 600, "figure.dpi": 150,
    })

def add_panel_labels(fig, axes, case="lower", size=8, dx_mm=-6, dy_mm=2):
    """Place bold labels at the same offset from each axes' top-left -> aligned."""
    w, h = fig.get_size_inches()
    for i, ax in enumerate(axes):
        L = "abcdefghijklmnopqrstuvwxyz"[i]; L = L.upper() if case == "upper" else L
        bb = ax.get_position()
        fig.text(bb.x0 + dx_mm*MM/w, bb.y1 + dy_mm*MM/h, L, fontsize=size, fontweight="bold",
                 ha="left", va="bottom")

def save_all(fig, stem, dpi=600):
    os.makedirs(os.path.dirname(stem) or ".", exist_ok=True)
    fig.savefig(stem + ".pdf"); fig.savefig(stem + ".svg")
    fig.savefig(stem + ".tiff", dpi=dpi, pil_kwargs={"compression": "tiff_lzw"})
    fig.savefig(stem + ".png", dpi=300)

def build(journal="nature", height_mm=110, out="../examples/output/fig_food_micro_py"):
    J = JOURNAL[journal]; set_theme(J["base"])
    fig = plt.figure(figsize=(J["double"]*MM, height_mm*MM))
    axd = fig.subplot_mosaic([["a", "b"], ["c", "c"]], gridspec_kw=dict(left=.08, right=.98, top=.93, bottom=.09, wspace=.3, hspace=.55))
    # a: growth curves (mean ± SD of 3 simulated reps), direct labels
    g = growth(); ax = axd["a"]
    for (temp, d), col in zip(g.groupby("temp_C"), OKABE_ITO[4:7]):
        s = d.groupby("time_h")["log_cfu"].agg(["mean", "std"])
        ax.fill_between(s.index, s["mean"]-s["std"], s["mean"]+s["std"], color=col, alpha=.2, lw=0)
        ax.plot(s.index, s["mean"], "o-", ms=2, color=col)
        i = int(np.argmax(s["mean"].values > 6))  # direct label where curve crosses mid-level
        ax.text(s.index[i]+1.5, s["mean"].iloc[i]-.1, f"{temp} °C", va="top", fontsize=J["base"]-1)
    ax.set(xlabel="Time (h)", ylabel="log$_{10}$ CFU/mL", xlim=(0, 50))
    # b: survival with D-value fit
    sv = survival(); ax = axd["b"]
    for (temp, d), col in zip(sv.groupby("temp_C"), OKABE_ITO[4:7]):
        k, b = np.polyfit(d.time_min, d.log_cfu, 1)
        ax.plot(d.time_min, d.log_cfu, "o", ms=2.5, color=col, alpha=.8)
        x = np.linspace(0, d.time_min.max(), 50); ax.plot(x, b + k*x, color=col)
        ax.text(x[-1], b + k*x[-1] - .3, f"{temp} °C\nD = {-1/k:.1f} min", fontsize=J["base"]-1, ha="center", va="top")
    ax.set(xlabel="Time at temperature (min)", ylabel="log$_{10}$ survivors (CFU/mL)", ylim=(0, 8))
    # c: CFU dot + box
    c = cfu(); ax = axd["c"]; groups = list(dict.fromkeys(c.treatment))
    data = [c.loc[c.treatment == t, "log_cfu_g"] for t in groups]
    ax.boxplot(data, widths=.45, showfliers=False, medianprops=dict(color="black"), boxprops=dict(lw=.6), whiskerprops=dict(lw=.6), capprops=dict(lw=.6))
    rng = np.random.default_rng(1)
    for i, v in enumerate(data, 1):
        ax.scatter(i + rng.uniform(-.12, .12, len(v)), v, s=8, color="#0072B2" if i > 1 else "grey", zorder=3, lw=0)
    ax.set_xticks(range(1, len(groups)+1), groups); ax.set_ylabel("log$_{10}$ CFU/g"); ax.set_ylim(2, 7.5)
    fig.text(.98, .005, "SIMULATED DATA – template only", ha="right", va="bottom", fontsize=5, color="grey")
    add_panel_labels(fig, [axd["a"], axd["b"], axd["c"]], J["case"], J["label"])
    save_all(fig, out); return fig

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--journal", default="nature", choices=JOURNAL); p.add_argument("--out", default=None)
    a = p.parse_args(); build(a.journal, out=a.out or f"../examples/output/fig_food_micro_py_{a.journal}")
