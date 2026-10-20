#!/usr/bin/env python3
"""Sostituisce esclusivamente il profilo della parete nell'HTML autonomo Conduzione."""
from pathlib import Path
import base64
import sys
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
HTML = ROOT / "conduzione_it.html"
SVG = ROOT / "lavorazione/conduzione/risorse/parete-temperatura-profilo-curvo.svg"
FIGURE = "visuale-immagine-06-e-grafico-g-1"

def main():
    if not HTML.exists() or not SVG.exists():
        raise SystemExit("Mancano HTML o SVG: nessuna modifica.")
    original = HTML.read_text(encoding="utf-8")
    soup = BeautifulSoup(original, "html.parser")
    figure = soup.find("figure", id=FIGURE)
    if figure is None:
        raise SystemExit(f"Figura {FIGURE!r} assente: nessuna modifica.")
    im = figure.select_one(".overview img")
    if im is None:
        raise SystemExit("Immagine principale mancante: nessuna modifica.")
    alt = ("Profilo qualitativo di temperatura attraverso un muro: aria interna a "
           "25 °C e aria esterna a −5 °C; raccordi curvi nell'aria e variazione "
           "lineare nello spessore della parete.")
    src = "data:image/svg+xml;base64," + base64.b64encode(SVG.read_bytes()).decode("ascii")
    im["src"] = src
    im["alt"] = alt
    for zoom in figure.select("[data-zoom-copy]"):
        zoom["alt"] = alt
        zoom["src"] = src
    caption = figure.find("figcaption")
    if caption is None:
        raise SystemExit("Didascalia mancante: nessuna modifica.")
    caption.string = (
        "L'aria interna è a 25 °C e quella esterna a −5 °C. "
        "Il profilo è qualitativo: vicino alle superfici varia anche la temperatura "
        "dell'aria, mentre all'interno del muro omogeneo a regime stazionario "
        "la temperatura varia linearmente. Le temperature delle due superfici "
        "non coincidono necessariamente con quelle dell'aria."
    )
    # Conserva gli altri elementi e aggiorna solo l'HTML di questa figura.
    output = str(soup)
    test = BeautifulSoup(output, "html.parser").find("figure", id=FIGURE)
    if test is None or "image/svg+xml" not in test.select_one(".overview img").get("src", ""):
        raise SystemExit("Validazione fallita: nessuna modifica.")
    if "--check" in sys.argv:
        print("Figura individuata; sostituzione verificabile, nessun file scritto.")
    else:
        HTML.write_text(output, encoding="utf-8")
        print(f"Aggiornato {HTML}")

if __name__ == "__main__":
    main()
