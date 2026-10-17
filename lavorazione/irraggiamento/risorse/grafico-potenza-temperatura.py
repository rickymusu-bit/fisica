"""Grafico teorico della legge di Stefan–Boltzmann, senza dati sperimentali."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parent
FONT = ROOT / "lexend.ttf"
font = FontProperties(fname=str(FONT)) if FONT.exists() else FontProperties(family="DejaVu Sans")
SIGMA = 5.67e-8
AREA = 1.0
EMISSIVITY = 1.0
temperature = np.linspace(0, 600, 601)
power = EMISSIVITY * SIGMA * AREA * temperature**4
fig, ax = plt.subplots(figsize=(11.8, 8.1), dpi=150)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.plot(temperature, power, color="#111111", linewidth=3.3)
ax.set_xlim(0, 620)
ax.set_ylim(0, 8000)
ax.set_xticks(np.arange(0, 601, 100))
ax.set_yticks(np.arange(0, 8001, 1000))
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " ")))
ax.grid(axis="y", color="#d4d4d4", linewidth=0.9)
ax.set_axisbelow(True)
for spine in ax.spines.values():
    spine.set_linewidth(1.6)
ax.tick_params(axis="both", labelsize=14, length=5, pad=8)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(font)
    label.set_fontsize(15)
ax.set_xlabel("Temperatura assoluta (K)", fontproperties=font, fontsize=18, labelpad=16)
ax.set_ylabel("Potenza emessa (W)", fontproperties=font, fontsize=18, labelpad=18)
ax.set_title("La potenza emessa cresce con T⁴", fontproperties=font, fontsize=25, loc="left", pad=24)
ax.text(0.035, 0.93, r"$P=\varepsilon\cdot\sigma\cdot A\cdot T^4$", transform=ax.transAxes, fontsize=21)
ax.text(0.035, 0.79, "Area = 1 m²\nEmissività = 1", transform=ax.transAxes,
        fontproperties=font, fontsize=16, linespacing=1.55)
points = [(300, SIGMA * 300**4), (600, SIGMA * 600**4)]
for t, p in points:
    ax.plot([t, t], [0, p], color="#777777", linewidth=1.4, linestyle=(0, (4, 4)))
    ax.scatter([t], [p], color="#111111", edgecolors="white", linewidths=1.8, s=105, zorder=5)
ax.annotate("300 K: circa 459 W", xy=points[0], xytext=(90, 1800),
            fontproperties=font, fontsize=16,
            arrowprops={"arrowstyle": "-", "linewidth": 1.4, "color": "#333333"},
            bbox={"boxstyle": "square,pad=0.5", "facecolor": "white", "edgecolor": "#111111"})
ax.annotate("600 K: circa 7 348 W", xy=points[1], xytext=(290, 5900),
            fontproperties=font, fontsize=16,
            arrowprops={"arrowstyle": "-", "linewidth": 1.4, "color": "#333333"},
            bbox={"boxstyle": "square,pad=0.5", "facecolor": "white", "edgecolor": "#111111"})
fig.text(0.17, 0.025, "Temperatura doppia in kelvin: potenza emessa 16 volte maggiore.",
         fontproperties=font, fontsize=14, color="#222222")
fig.subplots_adjust(left=0.16, right=0.96, top=0.86, bottom=0.15)
fig.savefig(ROOT / "potenza-temperatura.svg", format="svg", metadata={"Description": "Curva teorica P = ε · σ · A · T⁴, A = 1 m², emissività = 1. A 300 K: 459,27 W; a 600 K: 7348,32 W. Rapporto: 16."})
fig.savefig(ROOT / "potenza-temperatura.png", dpi=150)
plt.close(fig)
assert abs(points[1][1] / points[0][1] - 16) < 1e-12
print({"P_300_K_W": points[0][1], "P_600_K_W": points[1][1], "rapporto": 16})
