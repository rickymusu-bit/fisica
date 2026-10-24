"""Visuali originali richiesti per la revisione dei capitoli 8–9."""
from pathlib import Path
from html import escape
import base64,json,re
ROOT=Path(__file__).resolve().parents[2]
CREDIT8='visuali-piano-serbatoio'
CREDIT9='visuali-proporzioni-parametro'
STYLE='''<style data-component="grafici-proporzioni">
.graph svg,.scene svg{display:block;width:100%;height:auto;background:#fff;color:#182c3b;border-radius:8px}.graph svg text,.scene svg text{font-family:Lexend,Arial,sans-serif;fill:#182c3b}.graph .grid{stroke:#d5dfe5;stroke-width:1}.graph .axis{fill:none;stroke:#182c3b;stroke-width:2}.graph .guide{fill:none;stroke:#8c3840;stroke-width:2;stroke-dasharray:5 4}.graph .dot{fill:#0065a8;stroke:#fff;stroke-width:1.5}.graph .fit,.graph .continuous{fill:none;stroke:#005e9c;stroke-width:3}.graph .reference{stroke:#626b75;stroke-width:2;stroke-dasharray:6 5}.graph .reference[hidden]{display:none!important}.plot-y,.plot-x{font-size:16px;line-height:1.5;color:var(--ink);margin:5px 0}.plot-x{text-align:center}.graph button{min-height:44px;cursor:pointer;margin:12px 0;font:inherit}.graph [tabindex]:focus-visible,.parameter-controls input:focus-visible{outline:3px solid #db8b00;outline-offset:3px}.coordinate-readout{font-variant-numeric:tabular-nums;margin:12px 0;text-align:center}.graph-hint,.graph-reading{font-size:16px;line-height:1.6}.graph .move-point{fill:#b5273b;stroke:#fff;stroke-width:2;cursor:grab;touch-action:none}.graph .drag-target{fill:transparent;cursor:grab;touch-action:none}.data-scroll{overflow-x:auto;max-width:100%}.data-table{border-collapse:collapse;width:100%;font-size:1em}.data-table th,.data-table td{padding:10px 12px;text-align:center;border-bottom:1px solid var(--line)}.parameter-controls{display:none;gap:10px;align-items:center;flex-wrap:wrap;margin:18px 0}.parameter-controls label{width:100%;font-size:17px}.parameter-controls input{width:100%;min-width:0;height:44px;accent-color:var(--accent)}.js-enabled .parameter-controls{display:flex}.fit-toggle{display:none}.js-enabled .fit-toggle{display:inline-flex}.js-enabled .fit{display:none}.js-enabled .show-fit .fit{display:block}.scale-comparison .zoom-scroll svg{min-width:820px;max-width:none}.scale-comparison:has(>.image-zoom[open]) .overview{display:none}.scale-comparison>.image-zoom>summary{margin:10px 0}.graph .probe{fill:#fff;stroke:#b5273b;stroke-width:3}.scene .stroke{stroke:#182c3b;stroke-width:2;fill:none}.scene .water{fill:#b8dff3}.scene text{font-size:24px}
</style>'''

def uri(path):
 mime={'.jpg':'image/jpeg','.png':'image/png','.svg':'image/svg+xml'}[path.suffix]
 return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()

def photo(name,alt,cover=False):
 folder='piano_cartesiano_grafici' if name.startswith('Playfair') else 'proporzionalita_diretta'
 path=ROOT/'lavorazione'/folder/'risorse'/name
 info=next(iter(json.loads(path.with_suffix(path.suffix+'.json').read_text())['query']['pages'].values()))['imageinfo'][0];meta=info['extmetadata']
 author=re.sub('<[^>]+>','',meta.get('Artist',{}).get('value',''))
 if name.startswith('Hyperbolic'):author='Tomruen; immagine realizzata con Curved Spaces di Jeff Weeks'
 attrs={'source':info['descriptionurl'],'author':author,'license':meta['LicenseShortName']['value'],'license-url':meta.get('LicenseUrl',{}).get('value') or info['descriptionurl']+'#Licensing','changes':'Immagine intera, nessun ritaglio o alterazione.'}
 tags=' '.join('data-credit-'+k+'="'+escape(v,quote=True)+'"' for k,v in attrs.items() if v)
 caption='Un grafico storico di William Playfair: la posizione lungo gli assi permette di confrontare serie di dati nel tempo.' if name.startswith('Playfair') else 'Una tassellazione dello spazio iperbolico: le forme cambiano dimensione apparente nella rappresentazione.'
 return f'<figure class="visual photo cover" {tags}><div class="image-frame"><div class="overview"><img src="{uri(path)}" alt="{escape(alt,quote=True)}" decoding="async"></div></div><figcaption>{caption}</figcaption></figure>'

def fmt(v):return f'{v:g}'.replace('.',',')
def svg_open(w,h,label,extra=''):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label,quote=True)}" {extra}>'
def text(x,y,s,anchor='middle',size=24):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}">{escape(str(s))}</text>'

def figure(svg,caption,identity=CREDIT8,cls='scene'):
 return f'<figure class="visual {cls}" data-credit-id="{identity}">{svg}<figcaption>{caption}</figcaption></figure>'

def plot_svg(points,xmax,ymax,identity,xticks,yticks,curve=None,highlight=None,reference=None,continuous=False):
 X=lambda x:50+325*x/xmax;Y=lambda y:245-215*y/ymax
 attrs=f'data-xmax="{xmax}" data-ymax="{ymax}" data-plot="{identity}"'
 s=svg_open(400,295,'Coppie rappresentate: '+', '.join(f'({fmt(x)}; {fmt(y)})' for x,y in points)+'.',attrs)
 s+=f'<defs><clipPath id="clip-{identity}"><rect x="49" y="29" width="328" height="218"/></clipPath></defs>'
 for x in xticks:s+=f'<path class="grid" d="M{X(x)} 30V245"/>'+text(X(x),280,fmt(x))
 for y in yticks:s+=f'<path class="grid" d="M50 {Y(y)}H375"/>'+text(41,Y(y)+8,fmt(y),'end')
 s+='<path class="axis" d="M50 25V245H380"/>'
 if identity=='tank' or identity.startswith('scale-'):
  s+='<path data-axis-tip="x" d="M380 239L392 245L380 251Z" fill="#182c3b"/><path data-axis-tip="y" d="M44 27L50 15L56 27Z" fill="#182c3b"/>'
 def path(fn):
  xs=[xmax*i/400 for i in range(401) if i or identity!='inverse']
  return ' '.join(f'{X(x):.3f},{Y(fn(x)):.3f}' for x in xs)
 if reference:s+=f'<polyline class="fit reference" data-reference hidden clip-path="url(#clip-{identity})" points="{path(reference)}"/>'
 if curve:s+=f'<polyline class="{"continuous" if continuous else "fit"}" data-curve clip-path="url(#clip-{identity})" points="{path(curve)}"/>'
 if highlight:
  x,y=highlight;s+=f'<path class="guide" d="M{X(x)} 245V{Y(y)}H50"/>'+text(X(x)-14,Y(y)-12,'P','end')
 for x,y in points:s+=f'<circle class="dot" data-point-x="{x}" cx="{X(x)}" cy="{Y(y)}" r="5"/>'
 return s+'</svg>'

def graph(points,xmax,ymax,xlabel,ylabel,identity,caption,curve=None,xticks=None,yticks=None,highlight=None,parameter=None,credit=CREDIT9,always_curve=False):
 svg=plot_svg(points,xmax,ymax,identity,xticks or list(range(int(xmax)+1)),yticks or list(range(0,int(ymax)+1,2)),curve,highlight,curve if parameter else None,continuous=always_curve)
 controls=''
 if curve and not always_curve:
  kind='retta' if identity=='direct' else 'curva'
  controls=f'<button class="button fit-toggle" type="button" aria-pressed="false" aria-controls="chart-{identity}" data-toggle="chart-{identity}" data-kind="{kind}">Mostra la {kind}</button>'
 if parameter:
  minimum,maximum,step,initial,unit,probe=parameter
  controls+=f'<div class="parameter-controls"><label for="k-{identity}">Varia k: <output for="k-{identity}" data-k-value>{fmt(initial)} {unit}</output></label><input id="k-{identity}" data-k type="range" min="{minimum}" max="{maximum}" step="{step}" value="{initial}" disabled></div><p class="graph-reading" aria-live="polite" data-model-reading></p>'
  data=f'data-model="{identity}" data-initial="{initial}" data-unit="{unit}" data-probe="{probe}"'
 else:data=''
 return f'<figure class="visual graph" data-credit-id="{credit}" {data}><div class="plot-y">{ylabel}</div><div class="image-frame" id="chart-{identity}"><div class="overview">{svg}</div></div><div class="plot-x">{xlabel}</div>{controls}<figcaption>{caption}</figcaption></figure>'

def plane():
 X=lambda x:160+24*x;Y=lambda y:160-24*y
 s=svg_open(320,320,'Piano cartesiano da meno cinque a cinque, con punto P inizialmente in due, due.','id="plane"')
 for i in range(-5,6):s+=f'<path class="grid" d="M{X(i)} 40V280M40 {Y(i)}H280"/>'
 s+='<path class="axis" d="M35 160H285M160 285V40"/><path data-axis-tip="x" d="M282 154L294 160L282 166Z" fill="#182c3b"/><path data-axis-tip="y" d="M154 42L160 30L166 42Z" fill="#182c3b"/>'
 for i in [-4,-2,2,4]:s+=text(X(i),181,i,size=20)+text(151,Y(i)+7,i,'end',20)
 s+=text(308,168,'x',size=22)+text(174,28,'y',size=22)+text(147,181,'O',size=20)
 for x,y,n in [(235,65,'I'),(65,65,'II'),(65,275,'III'),(235,275,'IV')]:s+=text(x,y,n)
 s+='<path id="x-guide" class="guide" d="M208 112V160"/><path id="y-guide" class="guide" d="M160 112H208"/><circle id="point" class="move-point" cx="208" cy="112" r="9" tabindex="0" role="button" aria-label="Punto P; usa le frecce per spostarlo"/><circle id="hit-point" class="drag-target" cx="208" cy="112" r="30" aria-hidden="true"/>'
 s+='</svg><div id="coordinate-readout" class="coordinate-readout" aria-live="polite">P = (2; 2); I quadrante</div><p class="graph-hint">Trascina P oppure selezionalo e usa le frecce: passo 0,5; con Maiusc, passo 0,1.</p>'
 return figure(s,'Le proiezioni tratteggiate collegano il punto alle sue coordinate. La griglia ha passo 1; le etichette numeriche compaiono ogni due unità.',cls='graph')

def tank():
 s=svg_open(400,320,'Serbatoio: rubinetto aperto, dopo due minuti ci sono sei litri; chiuso al terzo minuto, il volume resta nove litri.')
 for x,level in [(35,170),(235,125)]:
  s+=f'<rect x="{x}" y="{level}" width="130" height="{260-level}" class="water"/><path class="stroke" d="M{x} 110V260H{x+130}V110"/>'
 tap=uri(ROOT/'lavorazione/piano_cartesiano_grafici/risorse/robinet.svg')
 s+=f'<image data-credit-id="clipart-robinet-spadassin" href="{tap}" x="29" y="0" width="113" height="130" preserveAspectRatio="xMidYMid meet" aria-label="Rubinetto, illustrazione di spadassin"/>'
 closed=uri(ROOT/'lavorazione/piano_cartesiano_grafici/risorse/robinet-senza-goccia.png')
 s+=f'<image data-credit-id="clipart-robinet-senza-goccia" href="{closed}" x="229" y="0" width="113" height="130" preserveAspectRatio="xMidYMid meet" aria-label="Rubinetto chiuso, senza goccia"/>'
 s+=text(100,295,'2 min; 6 L')+text(300,295,'3–5 min; 9 L')
 return figure(s+'</svg>','L’ingresso è di 3 litri al minuto fino alla chiusura a 3 minuti. Dopo la chiusura non entra né esce acqua.')

def dependence():
 s=svg_open(400,245,'I tempi 3, 4 e 5 minuti corrispondono tutti al volume di nove litri.')+'<defs><marker id="arrow-dependence" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0L6 3L0 6Z" fill="#182c3b"/></marker></defs>'
 for y,t,end_y in [(50,3,95),(125,4,125),(200,5,155)]:
  s+=text(75,y+8,f'{t} min')+f'<path class="stroke" d="M125 {y}L267 {end_y}" marker-end="url(#arrow-dependence)"/>'
 s+=text(315,133,'9 L')
 return figure(s+'</svg>','A ogni tempo corrisponde un solo volume. Lo stesso volume di 9 L, però, corrisponde a più tempi: invertire la corrispondenza non dà un’unica risposta.')

def book(x,y):
 return f'<g transform="translate({x} {y})"><path d="M0 0H28L36 9V65H0Z" fill="#b8dff3" stroke="#182c3b" stroke-width="2"/><path d="M6 0V65M28 0V9H36M10 19H28M10 26H28" class="stroke"/></g>'

def books():
 s=svg_open(400,205,'Tre situazioni separate: un libro a quindici euro, due libri a trenta euro, tre libri a quarantacinque euro.')
 art=uri(ROOT/'lavorazione/proporzionalita_diretta/risorse/libro.svg')
 s+='<path d="M130 8V190M270 8V190" stroke="#c2cbd3" stroke-width="2"/>'
 for center,count in [(60,1),(200,2),(340,3)]:
  s+=f'<g data-book-group="{count}">'+text(center,27,'1 libro' if count==1 else f'{count} libri')
  left=center-(55+(count-1)*22)/2
  for i in range(count):
   s+=f'<image data-credit-id="clipart-red-book-nerdy" href="{art}" x="{left+i*22}" y="45" width="55" height="80" preserveAspectRatio="xMidYMid meet" aria-label="Libro rosso parzialmente aperto"/>'
  s+=text(center,170,f'{count*15} €')+'</g>'
 return figure(s+'</svg>','Libri della stessa collana a 15 € ciascuno, senza sconti o costi aggiuntivi. La quantità è un conteggio di libri interi.',CREDIT9)

def journey():
 s=svg_open(400,300,'Viaggio ideale in autobus su un percorso di centoventi chilometri, senza fermate e a velocità costante.')
 art=uri(ROOT/'lavorazione/proporzionalita_diretta/risorse/autobus.svg')
 s+=f'<image data-credit-id="clipart-double-decker-bus-j4p4n" href="{art}" x="100" y="0" width="200" height="110" preserveAspectRatio="xMidYMid meet" aria-label="Autobus rosso a due piani"/>'
 s+='<g class="stroke"><path d="M80 111H320M35 150H365M35 140V160M365 140V160"/></g>'
 s+=text(200,140,'120 km')+text(70,193,'Partenza')+text(335,193,'Arrivo')+text(200,240,'60 km/h → 2 h')+text(200,280,'120 km/h → 1 h')
 return figure(s+'</svg>','Due percorrenze dello stesso tragitto ideale in autobus. Il confronto cambia la velocità e mantiene fissa la distanza.',CREDIT9)

def squares():
 s=svg_open(400,260,'Quadrati in scala: lato uno centimetro e area uno centimetro quadrato; lato due centimetri e area quattro centimetri quadrati.')
 s+='<g stroke="#182c3b" stroke-width="2" fill="#b8dff3"><rect x="55" y="120" width="65" height="65"/><rect x="235" y="55" width="130" height="130"/><path d="M300 55V185M235 120H365"/></g>'
 s+=text(87,103,'1 cm')+text(300,38,'2 cm')+text(87,230,'1 cm²')+text(300,230,'4 cm²')
 return figure(s+'</svg>','Il quadrato di lato doppio contiene quattro copie del quadrato iniziale: l’area è quattro volte maggiore.',CREDIT9)

def scales():
 pts=[(0,0),(1,3),(2,6),(3,9),(4,9),(5,9)]
 s=svg_open(820,365,'Stessi dati del serbatoio con scale verticali da zero a dodici litri e da zero a ventiquattro litri.')
 for offset,m in [(0,12),(420,24)]:
  inner=plot_svg(pts,5,m,'scale-'+str(m),[0,1,2,3,4,5],list(range(0,m+1,m//4)),curve=lambda t:min(3*t,9),continuous=True)
  inner=inner.replace('<svg ',f'<svg x="{offset}" y="30" width="400" height="295" ',1)
  s+=inner+text(offset+210,25,f'Volume (L), da 0 a {m}',size=24)+text(offset+215,356,'Tempo (min)',size=24)
 s+='</svg>'
 from stringhe_theme import icon
 zoom='<details class="image-zoom"><summary class="media-icon-button" aria-label="Ingrandisci il confronto delle scale"><span class="zoom-expand">'+icon('zoom-in')+'</span><span class="zoom-collapse">'+icon('zoom-out')+'</span></summary><div class="zoom-scroll" tabindex="0" role="region" aria-label="Confronto delle scale ingrandito">'+s.replace('clip-scale-','zoom-clip-scale-')+'</div></details>'
 return f'<figure class="visual graph scale-comparison" data-credit-id="{CREDIT8}"><div class="image-frame"><div class="overview">{s}</div></div>{zoom}<figcaption>Stessi dati e stesso riempimento continuo, con diversa scala del volume: a destra il tracciato occupa metà dell’altezza.</figcaption></figure>'

def visual(key):
 if key=='C8-SIT':return tank()
 if key=='C8-DIP':return dependence()
 if key=='C8-P':return graph([(0,0),(1,3),(2,6),(3,9),(4,9),(5,9)],5,12,'Tempo t (min)','Volume V (L)','tank','La linea descrive il riempimento continuo; i punti evidenziano gli istanti della tabella. Da 3 minuti il volume rimane costante.',curve=lambda t:min(3*t,9),always_curve=True,xticks=[0,1,2,3,4,5],yticks=[0,3,6,9,12],highlight=(2,6),credit=CREDIT8)
 if key=='C8-INT':return plane()
 if key=='C8-SCA':return scales()
 if key=='C9-SIT':return books()
 if key=='C9-VIA':return journey()
 if key=='C9-QUA':return squares()
 if key=='C9-GRA-D':return graph([(i,15*i) for i in range(5)],4,80,'Numero di libri x','Prezzo y (€)','direct','I punti rappresentano quantità intere; la retta rappresenta il modello continuo. Cambiando k, tabella e punti si aggiornano; il tratteggio conserva k = 15 €/libro.',lambda x:15*x,yticks=[0,20,40,60,80],parameter=(10,20,5,15,'€/libro',2))
 if key=='C9-GRA-I':return graph([(v,120/v) for v in [30,40,60,80,120]],120,6,'Velocità v (km/h)','Tempo t (h)','inverse','L’iperbole passa per le coppie della tabella. Il tratteggio conserva il viaggio di 120 km; cambiare k significa confrontare una distanza diversa.',lambda x:120/x,[0,30,60,90,120],[0,2,4,6],parameter=(60,180,60,120,'km',60))
 if key=='C9-GRA-Q':return graph([(i,i*i) for i in range(5)],4,16,'Lato x (cm)','Area y (cm²)','square','Punti e parabola descrivono la stessa legge dell’area del quadrato, con k = 1. Per i lati usiamo solo x non negativo.',lambda x:x*x,yticks=[0,4,8,12,16])
 if key=='C9-K-Q':return graph([(i,i*i) for i in range(5)],4,32,'x','y','quadratic','Confronto matematico senza unità: il tratteggio indica k = 1. Qui k varia; nella formula dell’area del quadrato resta invece uguale a 1.',lambda x:x*x,yticks=[0,8,16,24,32],parameter=(.5,2,.5,1,'',2))
 raise ValueError(key)
