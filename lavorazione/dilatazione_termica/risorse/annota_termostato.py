"""Annotazioni vettoriali della foto del termostato ritoccata con imagegen.

La fotografia originale e il risultato PNG del ritocco sono conservati.
Esporta una copia fotografica JPEG per la figura autonoma, senza cambiare
composizione o dimensioni. Etichette e richiami sono SVG deterministici.
Legenda: https://en.wikipedia.org/wiki/Thermostat#Simple_two_wire_thermostats
"""
from pathlib import Path
import base64
import re
import json
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
photo = HERE / 'termostato-senza-numeri.png'
with Image.open(photo) as image:
    image.convert('RGB').save(HERE / 'termostato-senza-numeri.jpg', quality=93, subsampling=0)
font = re.search(r'url\(data:font/ttf;base64,([A-Za-z0-9+/=]+)\)', (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text())[1]
photo_data = base64.b64encode((HERE / 'termostato-senza-numeri.jpg').read_bytes()).decode()
# Coordinates refer to the original 512×512 photograph, displayed at 304,74.
labels = [
    {'original_number':1,'lines':['Leva di regolazione','della temperatura'],'x':28,'y':104,'target':[256,83], 'path':'M270 114 H292 470 L560 157'},
    {'original_number':2,'lines':['Lamina bimetallica','avvolta a spirale'],'x':28,'y':360,'target':[221,392], 'path':'M270 376 H292 425 L525 466'},
    {'original_number':3,'lines':['Filo flessibile'],'x':28,'y':260,'target':[221,282], 'path':'M270 260 H288 400 L525 356'},
    {'original_number':4,'lines':['Contatto mobile'],'x':852,'y':180,'target':[262,191], 'path':'M842 180 H820 L650 220 566 265'},
    {'original_number':5,'lines':['Contatto fisso'],'x':852,'y':320,'target':[288,190], 'path':'M842 320 H820 L730 290 592 264'},
    {'original_number':6,'lines':['Magnete'],'x':852,'y':488,'target':[299,229], 'path':'M842 488 H820 L690 390 603 303'},
]
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="660" viewBox="0 0 1120 660" role="img" aria-labelledby="title desc">
<title id="title">Le parti di un termostato bimetallico</title>
<desc id="desc">La fotografia del meccanismo aperto mostra la leva di regolazione della temperatura in alto, la lamina avvolta a spirale in basso, il filo flessibile, il contatto mobile, il contatto fisso e il magnete. Sei frecce collegano i nomi alle parti.</desc>
<defs><style>@font-face{{font-family:Lexend;src:url(data:font/ttf;base64,{font}) format('truetype');font-weight:100 900}}text{{font-family:Lexend,Arial,sans-serif;font-size:22px;font-weight:500;fill:#16324f}}.line{{fill:none;stroke:#16324f;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round;marker-end:url(#arrow)}}.halo{{fill:none;stroke:white;stroke-width:6;stroke-linecap:round;stroke-linejoin:round}}</style>
<marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8 Z" fill="#16324f"/></marker></defs>
<rect width="1120" height="660" fill="white"/>
<image x="304" y="74" width="512" height="512" href="data:image/jpeg;base64,{photo_data}"/>
''']
for label in labels:
    parts.append(f'<path class="halo" d="{label["path"]}"/><path class="line" d="{label["path"]}"/>')
    parts.append(f'<text x="{label["x"]}" y="{label["y"]}">')
    for i,line in enumerate(label['lines']):
        parts.append(f'<tspan x="{label["x"]}" dy="{0 if i==0 else 31}">{line}</tspan>')
    parts.append('</text>')
parts.append('</svg>')
(HERE / 'termostato-annotato.svg').write_text('\n'.join(parts)+'\n')
(HERE / 'termostato-annotazioni.json').write_text(json.dumps({'source':'https://en.wikipedia.org/wiki/Thermostat#Simple_two_wire_thermostats','photo':'WPThermostat new.jpg','photo_origin':[304,74],'photo_display_size':[512,512],'labels':labels},ensure_ascii=False,indent=2)+'\n')
print('SVG annotato:',(HERE/'termostato-annotato.svg').stat().st_size,'byte')
