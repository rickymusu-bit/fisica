"""Ricrea il confronto concettuale fornito dall'utente con geometria originale."""
from pathlib import Path
from math import hypot
import json

ROOT=Path(__file__).resolve().parent/'risorse'
REFERENCE='https://www.ossila.com/cdn/shop/files/Syringe_Pump_Accuracy_and_Precision_Potentiostat_Specifications.svg'
TIGHT=[(-10,-9),(10,9),(-10,9),(10,-9),(0,0),(-18,0),(18,0),(0,-18),(0,18)]
WIDE=[(-42,-36),(42,36),(-60,25),(60,-25),(-10,72),(10,-72),(-74,-25),(74,25),(0,0)]
GROUPS=[('A',280,295,TIGHT,(0,0)),('B',280,665,TIGHT,(-85,0)),('C',650,295,WIDE,(0,0)),('D',650,665,WIDE,(-50,-40))]

def main():
    parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 850" role="img" aria-labelledby="title description">',
    '<title id="title">Precisione e accuratezza</title>',
    '<desc id="description">A: punti raccolti e centrati. B: punti raccolti ma spostati. C: punti dispersi attorno al centro. D: punti dispersi e spostati. Le colonne confrontano la precisione, le righe l’accuratezza.</desc>',
    '<rect width="850" height="850" fill="#fff"/>',
    '<g font-family="Arial,sans-serif" fill="#26323d" text-anchor="middle" font-size="28">',
    '<text x="280" y="68">Precisione alta</text><text x="650" y="68">Precisione bassa</text>',
    '<text transform="translate(40 295) rotate(-90)">Accuratezza alta</text>',
    '<text transform="translate(40 665) rotate(-90)">Accuratezza bassa</text></g>',
    '<path d="M94 110H832M94 480H832M94 18V835M465 18V835" fill="none" stroke="#65717c" stroke-width="2"/>']
    checks=[]
    for letter,cx,cy,offsets,(dx,dy) in GROUPS:
        parts.append(f'<g id="gruppo-{letter}"><text x="{cx-144}" y="{cy-140}" font-family="Arial,sans-serif" font-size="25" font-weight="bold" fill="#26323d">{letter}</text>')
        for r in (150,115,80,45):
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#aabed2" stroke-width="16"/>')
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="#aabed2"/>')
        coords=[(x+dx,y+dy) for x,y in offsets]
        assert all(hypot(x,y)+5.5<150 for x,y in coords)
        mx=sum(x for x,y in coords)/len(coords);my=sum(y for x,y in coords)/len(coords)
        spread=(sum((x-mx)**2+(y-my)**2 for x,y in coords)/len(coords))**.5
        assert abs(mx-dx)<1e-9 and abs(my-dy)<1e-9
        for x,y in coords:parts.append(f'<circle cx="{cx+x}" cy="{cy+y}" r="5.5" fill="#853c17" stroke="#fff" stroke-width="1"/>')
        parts.append('</g>');checks.append({'group':letter,'center':[cx,cy],'points_relative':coords,'centroid_relative':[mx,my],'rms_spread':spread})
    assert checks[0]['rms_spread']==checks[1]['rms_spread']<checks[2]['rms_spread']==checks[3]['rms_spread']
    parts.append('</svg>');(ROOT/'bersagli.svg').write_text('\n'.join(parts)+'\n')
    (ROOT/'bersagli-fonte.json').write_text(json.dumps({'reference':REFERENCE,'authorization':'Ricrea questa immagine, richiesta esplicita dell’utente','method':'Nuovo SVG deterministico: nessun percorso, logo o elemento grafico del file Ossila incorporato. Disposizione concettuale conservata; scritte italiane.','checks':checks},ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
