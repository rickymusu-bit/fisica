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
from visuali import STYLE,photo,visual,CREDIT8,CREDIT9

def table(block):
 rows=[[c.strip() for c in r.strip('|').split('|')] for r in block.splitlines()]
 model='direct' if 'Numero di libri' in rows[0][0] else 'inverse' if 'Velocità' in rows[0][0] else ''
 return '<div class="data-scroll"><table class="data-table"'+(' data-model-table="'+model+'"' if model else '')+'><thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in r)+'</tr>' for r in rows[2:])+'</tbody></table></div>'

def render(folder,title,name,cover):
 base.NOTE_REFS.clear()
 source=(ROOT/'lavorazione'/folder/'bozza.md').read_text().split('\n---\n')[0]
 notes=''
 if '\n## Note\n' in source:source,notes=source.split('\n## Note\n')
 version='v5' if folder==CHAPTERS[0][0] else 'v4'
 date='2026-10-25T00:48:48+02:00'
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
   k=node.attrs['name'];v={'version':version,'date':date,'description':title+': esempi, grafici e domande di verifica.'}[k];edits.append((node.start,node.end,f'<meta name="{k}" content="{v}">'))
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
  elif node.tag=='footer' and node.has_class('footer'):edits.append((node.start,node.end,'<footer class="footer">Versione '+version+' — 25 ottobre 2026</footer>'))
 for start,end,value in sorted(edits,reverse=True):template=template[:start]+value+template[end:]
 template=template.replace('Nome dell’area tematica',AREA).replace('Titolo del capitolo',title).replace('</head>',STYLE+'</head>',1)
 # I collegamenti tra i due capitoli sono pronti soltanto nei nuovi documenti.
 previous=('errori_incertezza_misura_it.html','Errori e incertezza di misura') if folder==CHAPTERS[0][0] else (CHAPTERS[0][2],CHAPTERS[0][1])
 links=f'<a rel="prev" href="{previous[0]}" data-site-path="{previous[0]}"><span>← Capitolo precedente</span><small>{previous[1]}</small></a>'
 if folder==CHAPTERS[0][0]:links+=f'<a rel="next" href="{CHAPTERS[1][2]}" data-site-path="{CHAPTERS[1][2]}"><span>Capitolo successivo →</span><small>{CHAPTERS[1][1]}</small></a>'
 else:links+='<a rel="next" href="termodinamica_sistemi_it.html" data-site-path="termodinamica_sistemi_it.html"><span>Capitolo successivo →</span><small>La termodinamica e i sistemi termodinamici</small></a>'
 template=template.replace('<!-- chapter-navigation:end -->','<nav class="chapter-navigation" aria-label="Navigazione tra capitoli">'+links+'</nav><!-- chapter-navigation:end -->',1)
 script=(WORK/'interazioni.js').read_text()
 template=template.replace('</body>','<script data-grafici-interactions>'+script+'</script></body>')
 from media_controls import apply_media_controls
 return apply_media_controls(template)

def main():
 registry=credits.load_registry()
 selected=[CHAPTERS[0]] if '--chapter-8' in sys.argv else CHAPTERS
 if not any(r['id']=='clipart-robinet-spadassin' for r in registry['resources']):
  registry['resources'].append({'id':'clipart-robinet-spadassin','description':'Robinet, clip art del rubinetto','author':'spadassin','source':'https://openclipart.org/detail/202080/robinet','license':'CC0 1.0','license_url':'https://creativecommons.org/publicdomain/zero/1.0/','changes':'SVG originale incorporato, ridimensionato proporzionalmente nello schema; nessun ritaglio o modifica della clip art.','status':'documented','links':[],'notices':['Robinet — spadassin. <a href="https://openclipart.org/detail/202080/robinet">Fonte originale</a>. <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. SVG originale ridimensionato proporzionalmente nello schema, senza ritagli o modifiche.'],'metadata_sources':['lavorazione/piano_cartesiano_grafici/risorse/robinet-source.json'],'fingerprints':[]})
 if not any(r['id']=='clipart-robinet-senza-goccia' for r in registry['resources']):
  registry['resources'].append({'id':'clipart-robinet-senza-goccia','description':'Robinet, versione senza goccia','author':'spadassin; modifica con ChatGPT su richiesta','source':'https://openclipart.org/detail/202080/robinet','license':'CC0 1.0 (originale)','license_url':'https://creativecommons.org/publicdomain/zero/1.0/','changes':'Rimozione della goccia con ChatGPT su richiesta dell’utente; PNG con trasparenza. Originale SVG conservato.','status':'documented','links':[],'notices':['Robinet — spadassin. <a href="https://openclipart.org/detail/202080/robinet">Originale Openclipart</a>, <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. Versione con goccia rimossa tramite ChatGPT su richiesta, incorporata come PNG trasparente; originale SVG conservato.'],'metadata_sources':['lavorazione/piano_cartesiano_grafici/risorse/robinet-source.json'],'fingerprints':[]})
 for key,identity,source in [('autobus','clipart-double-decker-bus-j4p4n','https://openclipart.org/detail/286938/double-decker-bus'),('libro','clipart-red-book-nerdy','https://openclipart.org/detail/355394/red-book-partly-open')]:
  info=json.loads((ROOT/'lavorazione/proporzionalita_diretta/risorse'/f'{key}-source.json').read_text())
  if not any(r['id']==identity for r in registry['resources']):
   author=info['artist']['name'];license_url=info['license'];title=info['name']
   registry['resources'].append({'id':identity,'description':title,'author':author,'source':source,'license':'CC0 1.0','license_url':license_url,'changes':'SVG originale incorporato, ridimensionato proporzionalmente nello schema; nessun ritaglio o modifica della clip art.','status':'documented','links':[],'notices':[title+' — '+author+'. <a href="'+source+'">Fonte originale</a>. <a href="'+license_url+'">CC0 1.0</a>. Originale incorporato e ridimensionato proporzionalmente, senza ritagli o modifiche.'],'metadata_sources':['lavorazione/proporzionalita_diretta/risorse/'+key+'-source.json'],'fingerprints':[]})
 for identity,description,notice in [
  (CREDIT8,'Serbatoio, corrispondenze e grafici del piano cartesiano','Schemi e grafici originali realizzati su richiesta per il capitolo 8. Riempimento ideale: 3 L/min fino a 3 min, poi ingresso nullo. Dati costruiti, non misure. Nessuna fotografia dei libri incorporata.'),
  (CREDIT9,'Schemi di libri e autobus e grafici con parametro k','Composizioni degli schemi e grafici del capitolo 9 realizzati nel progetto Stringhe; clip art originali Openclipart dei libri e dell’autobus accreditate separatamente. Prezzo iniziale 15 €/libro; viaggio iniziale 120 km; area del quadrato con k = 1. Confronto matematico y = k·x² separato dal modello del quadrato. Dati costruiti dalle formule, non misure o tariffe reali.')]:
  resource=next((r for r in registry['resources'] if r['id']==identity),None)
  if not resource:registry['resources'].append({'id':identity,'description':description,'author':'Stringhe','source':None,'license':None,'license_url':None,'changes':None,'status':'documented','links':[],'notices':[notice],'metadata_sources':[],'fingerprints':[]})
  elif identity==CREDIT9:
   resource['description']=description
   if notice not in resource['notices']:resource['notices'].append(notice)
 for folder,title,name,cover in selected:
  (ROOT/name).write_text(render(folder,title,name,cover))
  registry['documents'][name]={'title':title,'anchor':name[:-5].replace('_','-'),'credits':[],'lexend':True,'chapter_labels':True,'review':None}
 credits.sync_inventory(registry)
 current_notice=len(next(r for r in registry['resources'] if r['id']==CREDIT9)['notices'])-1
 for association in registry['documents'][CHAPTERS[1][2]]['credits']:
  if association['resource']==CREDIT9:association['notice']=current_notice
 for folder,title,name,cover in selected:
  p=ROOT/name;p.write_text(credits.update_component(p.read_text(),registry,name))
  # Solo correzione dei percorsi, nessuna risorsa esterna aggiunta all'HTML autonomo.
  work=p.read_text()
  work=re.sub(r'(href=")(?![a-z]+:|#)([^"/]+\.html)(")',lambda m:m[1]+'../../'+m[2]+m[3],work)
  (ROOT/'lavorazione'/folder/'bozza.html').write_text(work)
 credits.REGISTRY.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
 published=set(json.loads((ROOT/'pubblicazione.json').read_text())['articoli'])
 if all(name in published for _,_,name,_ in selected):(ROOT/'crediti.html').write_text(credits.render_page(registry))
 else:assert (ROOT/'crediti.html').read_text()==credits.render_page(registry),'La pagina pubblica dei crediti deve restare invariata'
 print(json.dumps({name:(ROOT/name).stat().st_size for _,_,name,_ in selected},indent=2))
if __name__=='__main__':main()
