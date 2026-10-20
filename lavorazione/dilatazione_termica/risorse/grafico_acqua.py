"""GRA-01: volume of 1 kg liquid water, from NIST GLP 10 (2019).

Source: https://doi.org/10.6028/NIST.IR.7383-2019
GLP 10, section 6.1, printed page 4 (PDF page 13).
Tanaka et al., Metrologia 38 (2001), 301-309.
Air-free pure water, reference pressure 101325 Pa, 0-40 degC.
Calculated reference values, not new experimental measurements.
Run: python3 grafico_acqua.py [output_directory]
"""
from pathlib import Path
import csv
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

def density(T):
    return 999.974950 * (1 - (T - 3.983035)**2 * (T + 301.797)
                        / (522528.9 * (T + 69.34881)))

def volume_ml(T):
    return 1_000_000 / density(T)  # m=1 kg; m^3 converted to mL

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
out.mkdir(parents=True, exist_ok=True)
temperatures = sorted(set([i / 20 for i in range(201)] + [3.983035]))
with (out / 'acqua-densita-volume.csv').open('w', newline='') as stream:
    writer = csv.writer(stream)
    writer.writerow(['T_C', 'rho_kg_m3', 'massa_kg', 'volume_mL'])
    for T in temperatures:
        writer.writerow([f'{T:.6f}', f'{density(T):.9f}', '1', f'{volume_ml(T):.9f}'])

assert abs(density(10) - 999.70270) < 0.00001  # NIST GLP 10, Table 2
assert volume_ml(0) > volume_ml(3.983035) < volume_ml(10)
assert all(density(T) > 999 for T in temperatures)
assert all(volume_ml(a) > volume_ml(b) for a,b in zip(temperatures, temperatures[1:]) if b <= 3.983035)
assert all(volume_ml(a) < volume_ml(b) for a,b in zip(temperatures, temperatures[1:]) if a >= 3.983035)

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
                     'svg.fonttype': 'none', 'axes.unicode_minus': False})
fig, ax = plt.subplots(figsize=(10, 6.6), layout=None)
fig.patch.set_facecolor('white')
fig.subplots_adjust(left=0.17, bottom=0.26, right=0.96, top=0.80)
fig.text(0.17, 0.94, 'Il volume di 1 kg d’acqua liquida', fontsize=20, weight='bold', color='#16324f')
fig.text(0.17, 0.885, 'Acqua pura senza aria disciolta, a pressione atmosferica', fontsize=12, color='#465468')
ax.plot(temperatures, [volume_ml(T) for T in temperatures], color='#1764b5', linewidth=3)
ax.scatter([3.983035], [volume_ml(3.983035)], color='#16324f', s=55, zorder=5)
ax.annotate('Volume minimo\nintorno a 4 °C', xy=(3.983035, volume_ml(3.983035)),
            xytext=(4.65,1000.14), fontsize=13, color='#16324f',
            arrowprops={'arrowstyle':'->','color':'#16324f','lw':1.4})
ax.set_xlim(0,10)
ax.set_ylim(1000.0,1000.32)
ax.set_xlabel('Temperatura T (°C)', labelpad=12)
ax.set_ylabel('Volume (mL)', labelpad=16)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos: f'{x:.2f}'.replace('.',',')))
ax.grid(alpha=0.22, linewidth=0.8)
ax.spines[['top','right']].set_visible(False)
fig.text(0.17,0.11,'Scala verticale ingrandita: non parte da zero.',fontsize=12,color='#465468')
fig.text(0.17,0.065,'Il grafico riguarda solo l’acqua liquida, non il congelamento.',fontsize=12,color='#465468')
fig.savefig(out / 'volume-acqua.svg', metadata={'Title':'Volume di 1 kg d’acqua liquida in funzione della temperatura',
    'Description':'Curva calcolata dalla densità NIST GLP 10/Tanaka, acqua pura air-free a 101325 Pa; non nuove misure sperimentali. Scala verticale 1000,00–1000,32 mL.'})
fig.savefig(out / 'volume-acqua.png', dpi=150)
plt.close(fig)
print({T:{'rho_kg_m3':round(density(T),6), 'V_mL':round(volume_ml(T),6)} for T in (0,3.983035,4,10)})
