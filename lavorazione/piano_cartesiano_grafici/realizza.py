"""Genera i capitoli 8–9 dalle bozze approvate, senza ammetterli alla pubblicazione."""
from pathlib import Path
from html import escape
import importlib.util,json,re,sys,unicodedata
ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scripts'))
import credits
from stringhe_theme import navigation_header,icon
spec=importlib.util.spec_from_file_location('renderer_misure',ROOT/'lavorazione/strumenti_misura/realizza.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
inline,equation,uri,metadata=base.inline,base.equation,base.uri,base.metadata
AREA='Introduzione alla fisica e alla misura'
CHAPTERS=[('piano_cartesiano_grafici','Il piano cartesiano','piano_cartesiano_grafici_it.html','Playfair_TimeSeries-1.png'),('proporzionalita_diretta','Le relazioni di proporzionalità','relazioni_proporzionalita_it.html','Hyperbolic_orthogonal_dodecahedral_honeycomb.png')]
STYLE='''<style data-component="grafici-proporzioni">
.graph svg{display:block;width:100%;height:auto;background:#fff;color:#182c3b;border-radius:8px}.graph svg text{font-family:Lexend,Arial,sans-serif;fill:#182c3b}.graph .grid{stroke:#d5dfe5;stroke-width:1}.graph .axis{fill:none;stroke:#182c3b;stroke-width:2}.graph .guide{fill:none;stroke:#8c3840;stroke-width:2;stroke-dasharray:6 5}.graph .dot{fill:#0065a8;stroke:#fff;stroke-width:2}.graph .fit{fill:none;stroke:#005e9c;stroke-width:3}.graph .data-chart{min-width:0}.graph .zoom-scroll svg{min-width:650px}.graph button{min-height:44px;cursor:pointer;font:inherit;margin-top:12px}.graph button:focus-visible,.graph [tabindex]:focus-visible{outline:3px solid #d67d00;outline-offset:4px}.graph .move-point{fill:#b5273b;stroke:#fff;stroke-width:2;cursor:grab;touch-action:none}.graph .drag-target{fill:transparent;cursor:grab;touch-action:none}.graph .plane-grid{stroke:#d5dfe5}.graph .plane-axis{stroke:#28475b;stroke-width:2}.graph .plane-tick{font-size:15px}.graph .axis-name,.graph .origin-label{font-size:18px}.graph .quadrant-label{font-size:18px}.graph #plane{max-width:600px;margin:auto;touch-action:pan-y}.coordinate-readout{text-align:center;font-variant-numeric:tabular-nums;margin:12px 0}.graph-hint{font-size:.85em;color:var(--muted)}.data-scroll{overflow-x:auto;max-width:100%}.data-table{border-collapse:collapse;width:100%;font-size:1em}.data-table th,.data-table td{padding:10px 12px;text-align:right;border-bottom:1px solid var(--line)}.data-table th:first-child,.data-table td:first-child{text-align:left}.scale-pair{display:flex;gap:8px}.scale-pair>div{width:50%;min-width:0}.scale-pair .zoom-scroll svg{min-width:650px}.situation{margin:20px 0}.situation img{display:block;max-width:100%;height:auto}.situation .purchase{padding:14px;border:1px solid var(--line);text-align:center;line-height:1.8}.situation .journey{display:block;width:100%;height:auto;background:#fff}.measure-math math{font-family:Lexend,Arial,sans-serif;font-size:1em}.measure-math .math-step{flex:0 0 auto;max-width:100%;overflow-x:auto}.js-enabled .fit{display:none}.js-enabled .show-fit .fit{display:block}.fit-toggle{display:none}.js-enabled .fit-toggle{display:inline-flex;align-items:center}.figure-fallback{font-size:.85em;color:var(--muted)}
</style>'''

def resource_path(name):
 for folder,_,_,_ in CHAPTERS:
  p=ROOT/'lavorazione'/folder/'risorse'/name
  if p.exists():return p
 raise FileNotFoundError(name)

def photo(name,alt,cover=False):
 info=next(iter(json.loads(resource_path(name+'.json').read_text())['query']['pages'].values()))['imageinfo'][0]
 meta=info['extmetadata'];author=re.sub('<[^>]+>','',meta.get('Artist',{}).get('value',''))
 if name=='Hyperbolic_orthogonal_dodecahedral_honeycomb.png':author='Tomruen; immagine realizzata con Curved Spaces di Jeff Weeks'
 lic=meta['LicenseShortName']['value'];url=meta.get('LicenseUrl',{}).get('value') or info['descriptionurl']+'#Licensing'
 attrs=metadata({'source':info['descriptionurl'],'author':author,'license':lic,'license-url':url,'changes':'Immagine intera, nessun ritaglio o alterazione.'})
 return '<figure class="visual photo'+(' cover' if cover else '')+'" '+attrs+'><div class="image-frame"><div class="overview"><img src="'+uri(resource_path(name))+'" alt="'+escape(alt,quote=True)+'" decoding="async"'+('' if cover else ' loading="lazy"')+'></div></div></figure>'

def svg_open(w,h,label):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label,quote=True)}">'

def zoom(svg,label):
 return '<details class="image-zoom"><summary class="media-icon-button" aria-label="Ingrandisci l’immagine"><span class="zoom-expand">'+icon('zoom-in')+'</span><span class="zoom-collapse">'+icon('zoom-out')+'</span></summary><div class="zoom-scroll" tabindex="0" role="region" aria-label="'+escape(label,quote=True)+'">'+svg+'</div></details>'

def graph(points,xmax,ymax,xlabel,ylabel,identity,curve=None,xticks=None,yticks=None,highlight=False):
 # Tutti i punti e le curve derivano dai valori del modello, non da coordinate disegnate a mano.
 X=lambda x:80+500*x/xmax;Y=lambda y:330-260*y/ymax
 label=f'{xlabel}; {ylabel}. Punti: '+', '.join(f'({x}; {str(y).replace(".",",")})' for x,y in points)+'.'
 svg=svg_open(650,420,label)
 def text(x,y,s,anchor='middle',size=19):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}">{escape(str(s))}</text>'
 for x in xticks or range(int(xmax)+1):
  svg+=f'<path class="grid" d="M{X(x)} 70V330"/>'+text(X(x),359,x)
 for y in yticks or range(0,int(ymax)+1,2):
  svg+=f'<path class="grid" d="M80 {Y(y)}H580"/>'+text(63,Y(y)+6,str(y).replace('.',','),'end')
 svg+='<path class="axis" d="M80 65V330H590"/>'+text(80,36,ylabel,'start',20)+text(330,403,xlabel,'middle',20)
 if curve:
  start=xmax/300 if identity!='inverse' else 120/ymax
  samples=[start+(xmax-start)*i/300 for i in range(301)]
  pts=' '.join(f'{X(x):.3f},{Y(curve(x)):.3f}' for x in samples)
  if identity!='inverse':pts='80,330 '+pts
  svg+=f'<polyline class="fit" points="{pts}"/>'
 if highlight:
  svg+=f'<path class="guide" d="M{X(3)} 330V{Y(6)}H80"/>'+text(X(3)+18,Y(6)-13,'P','start',22)
 for x,y in points:svg+=f'<circle class="dot" cx="{X(x)}" cy="{Y(y)}" r="7"/>'
 svg+='</svg>'
 control=''
 if curve:
  kind='retta' if identity=='direct' else 'curva'
  control=f'<button class="button fit-toggle" type="button" aria-pressed="false" aria-controls="chart-{identity}" data-toggle="chart-{identity}" data-kind="{kind}">Mostra la {kind}</button><noscript><p class="figure-fallback">Il modello è mostrato insieme ai punti.</p></noscript>'
 return '<figure class="visual graph" data-credit-id="grafici-capitoli-8-9"><div class="image-frame" id="chart-'+identity+'"><div class="overview">'+svg+'</div>'+zoom(svg,'Grafico ingrandito: '+xlabel+', '+ylabel)+'</div>'+control+'</figure>'

def plane():
 source=(ROOT/'grafici_piano_cartesiano_it.html').read_text()
 svg=re.search(r'<svg id="plane"[\s\S]*?</svg>',source)[0]
 for a,b in [('viewbox','viewBox'),('markerwidth','markerWidth'),('markerheight','markerHeight'),('refx','refX'),('refy','refY')]:svg=svg.replace(a,b)
 svg=svg.replace(' · ','; ')
 svg=re.sub(r'<text id="point-label"[^>]*>[\s\S]*?</text>','',svg)
 # Una sola istanza interattiva; il fallback dello zoom non contiene id o controlli.
 static=re.sub(r' id="[^"]*"| tabindex="[^"]*"| marker-end="[^"]*"','',svg)
 static=static.replace('role="button"','role="img"')
 markup='<div class="image-frame plane-frame"><div class="overview">'+svg+'</div>'+zoom(static,'Piano cartesiano ingrandito e scorrevole')+'</div>'
 return '<figure class="visual graph" data-credit-id="grafici-capitoli-8-9">'+markup+'<div id="coordinate-readout" class="coordinate-readout" aria-live="polite">P = (2; 2); I quadrante</div><p class="graph-hint">Trascina il punto oppure selezionalo e usa le frecce: passo 0,5; con Maiusc, passo 0,1.</p><noscript><p>Il punto statico P = (2; 2) è nel primo quadrante.</p></noscript></figure>'

def situation(chapter):
 s=photo('Library_at_the_biltmore_estate.jpg','Scaffali di libri nella biblioteca della tenuta Biltmore.')
 purchase='3 libri → 6 €' if chapter==8 else '1 libro → 2 €<br>2 libri → 4 €<br>3 libri → 6 €'
 return '<div class="situation">'+s+'<div class="purchase" role="img" aria-label="Vendita ipotetica a prezzo fisso di 2 euro per libro">'+purchase+'<br><span>Prezzo fisso: 2 €/libro</span></div></div>'

def journey():
 return '<div class="situation">'+photo('Las_Vegas_monorail_Excalibur.jpg','Treno della monorotaia presso l’Excalibur a Las Vegas.')+svg_open(400,230,'Viaggio ideale di 120 km, senza fermate: a 60 km/h occorrono 2 h; a 120 km/h occorre 1 h.').replace('<svg ','<svg class="journey" data-credit-id="grafici-capitoli-8-9" ',1)+'<g fill="#182c3b" font-family="Lexend,Arial,sans-serif" font-size="24" text-anchor="middle"><path d="M35 70H365" stroke="#182c3b" stroke-width="3"/><path d="M35 58V82M365 58V82" stroke="#182c3b" stroke-width="3"/><text x="200" y="45">120 km</text><text x="70" y="115">Partenza</text><text x="335" y="115">Arrivo</text><text x="200" y="160">60 km/h → 2 h</text><text x="200" y="205">120 km/h → 1 h</text></g></svg></div>'

def squares():
 return '<figure class="visual graph" data-credit-id="grafici-capitoli-8-9">'+svg_open(500,270,'Quadrati in scala: lato 1 cm e area 1 cm²; lato 2 cm e area 4 cm². Il secondo è diviso in quattro quadrati unitari.')+'<g stroke="#182c3b" stroke-width="2" fill="#c5e3f4"><rect x="75" y="135" width="75" height="75"/><rect x="280" y="60" width="150" height="150"/><path d="M355 60V210M280 135H430"/></g><g font-family="Lexend,Arial,sans-serif" font-size="32" text-anchor="middle"><text x="112.5" y="120">1 cm</text><text x="355" y="45">2 cm</text><text x="112.5" y="250">1 cm²</text><text x="355" y="250">4 cm²</text></g></svg></figure>'

def visual(key):
 pts=[(i,2*i) for i in range(5)]
 if key in ['C8-SIT','C9-SIT']:return situation(8 if key.startswith('C8') else 9)
 if key=='C8-P':return '' # un solo grafico per P e tabella, come previsto dalla bozza
 if key=='C8-INT':return plane()
 if key=='C8-TAB/GRA':return graph(pts,4,10,'Numero di libri','Prezzo (€)','books',highlight=True)
 if key=='C8-SCA':return '<div class="scale-pair">'+''.join('<div>'+graph(pts,4,m,'Numero di libri','Prezzo (€)','scale-'+str(m),yticks=list(range(0,m+1,m//5)))+'</div>' for m in [10,20])+'</div>'
 if key=='C9-GRA-D':return graph(pts,5,10,'Numero di libri','Prezzo (€)','direct',lambda x:2*x)
 if key=='C9-VIA':return journey()
 if key=='C9-GRA-I':return graph([(30,4),(40,3),(60,2),(80,1.5),(120,1)],120,4,'Velocità v (km/h)','Tempo t (h)','inverse',lambda x:120/x,[0,30,60,90,120],[0,1,2,3,4])
 if key=='C9-QUA':return squares()
 if key=='C9-GRA-Q':return graph([(i,i*i) for i in range(5)],4,16,'Lato x (cm)','Area y (cm²)','quadratic',lambda x:x*x,yticks=[0,4,8,12,16])
 raise ValueError(key)

def table(block):
 rows=[[c.strip() for c in r.strip('|').split('|')] for r in block.splitlines()]
 return '<div class="data-scroll"><table class="data-table"><thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in r)+'</tr>' for r in rows[2:])+'</tbody></table></div>'

def render(folder,title,name,cover):
 base.NOTE_REFS.clear()
 source=(ROOT/'lavorazione'/folder/'bozza.md').read_text().split('\n---\n')[0]
 notes=''
 if '\n## Note\n' in source:source,notes=source.split('\n## Note\n')
 body=[];headings=[]
 for block in source.strip().split('\n\n'):
  if block.startswith(('# ','Versione della bozza:')):continue
  if block.startswith('['):
   key=re.match(r'\[([^ ]+)',block)[1]
   if key.endswith('-COP'):continue
   body.append(visual(key));continue
  if block.startswith('## '):
   heading=block[3:];sid=re.sub('[^a-z0-9]+','-',unicodedata.normalize('NFKD',heading).encode('ascii','ignore').decode().lower()).strip('-');headings.append((sid,heading))
   body.append(f'<div class="section-heading"><span class="section-number" aria-hidden="true">{len(headings):02}</span><h2 id="{sid}" data-toc tabindex="-1">{heading}</h2></div>');continue
  if block.startswith('|'):body.append(table(block));continue
  if block.startswith(r'\['):body.append(equation(block));continue
  if re.match(r'1\. ',block):body.append('<ol'+(' class="questions"' if headings[-1][1]=='Domande di verifica' else '')+'>'+''.join('<li>'+inline(re.sub(r'^\d+\. ','',line))+'</li>' for line in block.splitlines())+'</ol>');continue
  body.append('<p>'+inline(block)+'</p>')
 notehtml=''
 if notes:
  items=[]
  for n,txt in re.findall(r'\[\^(\d+)\]:\s*(.*)',notes):items.append('<li id="nota-'+n+'">'+inline(txt)+' <a href="#richiamo-'+n+'" role="doc-backlink" aria-label="Torna al richiamo della nota">↩</a></li>')
  notehtml='<details class="chapter-notes" aria-labelledby="titolo-note"><summary id="titolo-note">Note</summary><div role="doc-endnotes"><ol>'+''.join(items)+'</ol></div></details>'
 template=(ROOT/'riferimenti/TEMA_DISPENSE.html').read_text();doc=credits.Document(template);edits=[]
 for node in doc.root.descendants():
  if node.tag=='title':edits.append((node.start,node.end,'<title>'+title+' — Stringhe</title>'))
  elif node.tag=='meta' and node.attrs.get('name') in ['version','date','description']:
   k=node.attrs['name'];v={'version':'v1','date':'2026-10-24T20:45:00+02:00','description':title+': esempi, grafici e domande di verifica.'}[k];edits.append((node.start,node.end,f'<meta name="{k}" content="{v}">'))
  elif node.tag=='figure' and node.has_class('cover'):
   alt='Grafico storico di William Playfair, con serie di dati nel tempo.' if folder==CHAPTERS[0][0] else 'Struttura geometrica iperbolica a celle dodecaedriche.'
   edits.append((node.start,node.end,photo(cover,alt,True)))
  elif node.tag=='article' and node.has_class('article'):
   bottom=next(n for n in node.descendants('nav') if n.has_class('bottom-links'))
   edits.append((node.start,node.end,'<article class="article">'+'\n'.join(body)+doc.html(bottom)+'</article>'))
  elif node.tag=='details' and node.has_class('chapter-notes'):edits.append((node.start,node.end,notehtml))
  elif node.tag=='header' and node.has_class('topbar'):
   idx=next(n for n in node.descendants('details') if n.has_class('reader-index'));markup=doc.html(idx).replace('Titolo del capitolo',title).replace('<span class="sidebar-label">Fisica</span>','<span class="sidebar-label">'+AREA+'</span>')
   nav='<nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>'+''.join(f'<li class="level-2"><a href="#{sid}"><span>{escape(h)}</span></a></li>' for sid,h in headings)+'</ol></nav>'
   markup=re.sub(r'<nav class="sidebar-nav"[\s\S]*?</nav>',lambda _:nav,markup)
   edits.append((node.start,node.end,navigation_header('chapter',name,markup)))
  elif node.tag=='footer' and node.has_class('footer'):edits.append((node.start,node.end,'<footer class="footer">Versione v1 — 24 ottobre 2026</footer>'))
 for start,end,value in sorted(edits,reverse=True):template=template[:start]+value+template[end:]
 template=template.replace('Nome dell’area tematica',AREA).replace('Titolo del capitolo',title).replace('</head>',STYLE+'</head>',1)
 # I collegamenti tra i due capitoli sono pronti soltanto nei nuovi documenti.
 previous=('errori_incertezza_misura_it.html','Errori e incertezza di misura') if folder==CHAPTERS[0][0] else (CHAPTERS[0][2],CHAPTERS[0][1])
 links=f'<a rel="prev" href="{previous[0]}" data-site-path="{previous[0]}"><span>← Capitolo precedente</span><small>{previous[1]}</small></a>'
 if folder==CHAPTERS[0][0]:links+=f'<a rel="next" href="{CHAPTERS[1][2]}" data-site-path="{CHAPTERS[1][2]}"><span>Capitolo successivo →</span><small>{CHAPTERS[1][1]}</small></a>'
 template=template.replace('<!-- chapter-navigation:end -->','<nav class="chapter-navigation" aria-label="Navigazione tra capitoli">'+links+'</nav><!-- chapter-navigation:end -->',1)
 script=(WORK/'interazioni.js').read_text()
 if folder==CHAPTERS[0][0]:
  old=(ROOT/'grafici_piano_cartesiano_it.html').read_text();start=old.index("const svg=document.getElementById('plane')");js=old[start:old.index('\n})();',start)]
  js=js.replace(",label=document.getElementById('point-label')",'')
  js=re.sub(r"label\.setAttribute\('x',[\s\S]*?label.textContent=`[^`]*`;",'',js)
  js=js.replace(' · ${location()}','; ${location()}')+'\nset(2,2);'
  script+='\n(()=>{'+js+'})();'
 template=template.replace('</body>','<script data-grafici-interactions>'+script+'</script></body>')
 from media_controls import apply_media_controls
 return apply_media_controls(template)

def main():
 registry=credits.load_registry()
 identity='grafici-capitoli-8-9'
 if not any(r['id']==identity for r in registry['resources']):registry['resources'].append({'id':identity,'description':'Grafici di coordinate e proporzionalità, confronto delle scale e quadrati','author':'Stringhe','source':None,'license':None,'license_url':None,'changes':None,'status':'documented','links':[],'notices':['Grafici e schemi matematici del progetto Stringhe, costruiti dai modelli dichiarati. Dati illustrativi: libri usati a 2 €/libro, viaggio ideale di 120 km, area del quadrato. Interazione del punto P adattata dal sorgente grafici_piano_cartesiano_it.html. Non sono misure sperimentali o tariffe del luogo fotografato.'],'metadata_sources':[],'fingerprints':[]})
 for folder,title,name,cover in CHAPTERS:
  (ROOT/name).write_text(render(folder,title,name,cover))
  registry['documents'][name]={'title':title,'anchor':name[:-5].replace('_','-'),'credits':[],'lexend':True,'chapter_labels':True,'review':None}
 credits.sync_inventory(registry)
 for folder,title,name,cover in CHAPTERS:
  p=ROOT/name;p.write_text(credits.update_component(p.read_text(),registry,name))
  # Solo correzione dei percorsi, nessuna risorsa esterna aggiunta all'HTML autonomo.
  work=p.read_text()
  work=re.sub(r'(href=")(?![a-z]+:|#)([^"/]+\.html)(")',lambda m:m[1]+'../../'+m[2]+m[3],work)
  (ROOT/'lavorazione'/folder/'bozza.html').write_text(work)
 credits.REGISTRY.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
 assert (ROOT/'crediti.html').read_text()==credits.render_page(registry),'La pagina pubblica dei crediti deve restare invariata'
 print(json.dumps({name:(ROOT/name).stat().st_size for _,_,name,_ in CHAPTERS},indent=2))
if __name__=='__main__':main()
