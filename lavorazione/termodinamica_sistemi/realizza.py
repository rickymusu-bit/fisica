"""Rigenera l'articolo autonomo dal tema e dalla bozza testuale concordata.

Eseguire dalla radice: python3 lavorazione/termodinamica_sistemi/realizza.py
Poi python3 scripts/credits.py --sync e copiare l'HTML verificato in bozza.html.
"""
from pathlib import Path
from html import escape
import base64, re, json
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).resolve().parent
ASSETS=WORK/'risorse'
TITLE='La termodinamica e i sistemi termodinamici'
TARGET=ROOT/'termodinamica_sistemi_it.html'

def data(name):
    return 'data:image/jpeg;base64,'+base64.b64encode((ASSETS/name).read_bytes()).decode()

def attributes(source,author,license,url,changes):
    return ' '.join('data-credit-'+k+'="'+escape(v,quote=True)+'"' for k,v in
                    [('source',source),('author',author),('license',license),('license-url',url),('changes',changes)])

META={
 'TS-0':('copertina-hubble.jpg','Hubble_ultra_deep_field.jpg','NASA e European Space Agency (ESA)','Pubblico dominio','https://commons.wikimedia.org/wiki/File:Hubble_ultra_deep_field.jpg'),
 'TS-1':('caffe.jpg','Coffee_steaming_in_a_mug.jpg','PedanticNarrativeController','CC0 1.0','https://creativecommons.org/publicdomain/zero/1.0/'),
 'TS-3':('thermos.jpg','Термос_(4).jpg','Schekinov Alexey Victorovich','CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
 'TS-4':('corridori.jpg','Runners_during_marathon_Rotterdam.JPG','Peter van der Sluijs','CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
 'TS-5':('motore.jpg','Ferrari_500_(Motor,_2480_cm³),_Bj._1954.jpg','Lothar Spurzem','CC BY-SA 2.0 DE','https://creativecommons.org/licenses/by-sa/2.0/de/'),
 'TS-6':('pile.jpg','Used_batteries_inside_recycling_container.jpg','Waldyrious','CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/'),
 'TS-7':('molle.jpg','Springs_009.jpg','Renard~enwiki (caricamento originale); Zeimusu (ritaglio della data); Qz10 (trasferimento su Commons)','CC BY-SA 3.0','https://creativecommons.org/licenses/by-sa/3.0/'),
}

def text(x,y,lines,size=23):
    if isinstance(lines,str):lines=[lines]
    return '<text x="%s" y="%s" fill="#080808" font-family="Lexend,Arial,sans-serif" font-size="%s">%s</text>'%(x,y,size,''.join('<tspan x="%s" dy="%s">%s</tspan>'%(x,0 if i==0 else 30,escape(s)) for i,s in enumerate(lines)))

def line(x1,y1,x2,y2,arrow=False):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="'+('#0066b3' if arrow else '#080808')+'" stroke-width="'+('5' if arrow else '3')+'"'+(' marker-end="url(#freccia)"' if arrow else '')+'/>'

def boundary(d):
    # Doppio tratto per distinguere il confine anche nelle zone scure della foto.
    return f'<path d="{d}" fill="none" stroke="white" stroke-width="8"/><path d="{d}" fill="none" stroke="#080808" stroke-width="3" stroke-dasharray="10 7"/>'

def scene(key):
    name=META[key][0]
    # Foto complete: nessun ritaglio o ricostruzione del soggetto.
    im=Image.open(ASSETS/name);w=540;h=w*im.height/im.width
    if key=='TS-3':w=310;h=w*im.height/im.width
    if key=='TS-6':w=390;h=390
    x=(900-w)/2;y=135
    out=f'<image href="{data(name)}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/>'
    # Le coordinate dei contorni seguono i soggetti nella foto scelta.
    if key=='TS-1':
        out+=text(28,40,'Sistema: tazza e bevanda',25)+text(28,80,'Ambiente: aria, tavolo e resto della stanza',21)
        out+=boundary('M370,286 Q435,277 528,286 L531,308 Q600,293 597,346 Q592,391 530,407 L527,450 Q470,503 391,468 Q367,448 370,286 Z')
        out+=text(25,550,['Confine: superficie esterna della tazza', 'e superficie ideale sopra l’apertura.'],23)
        out+=line(430,283,430,112,True)+text(465,100,['Materia in uscita:','acqua per evaporazione'],20)
        out+=line(526,440,775,485,True)+text(615,530,['Energia ceduta','all’ambiente'],21)
        H=650
    elif key=='TS-3':
        out+=text(28,42,'Sistema: thermos chiuso e contenuto',25)
        out+=boundary('M348,238 Q337,200 381,177 Q455,140 526,181 Q570,209 555,292 L532,434 Q522,498 451,520 Q386,517 357,472 L329,333 Q316,281 331,257 Z')
        out+=text(24,600,['Materia: scambi impediti.', 'Energia: scambi molto ridotti.'],24)
        out+=text(24,690,['Modello ideale isolato:', 'nessuno scambio di materia o di energia.'],24)
        H=770
    elif key=='TS-4':
        out+=text(28,42,'Sistema: il corpo di un corridore',25)
        out+=text(28,82,'Il contorno segue il corridore in primo piano a sinistra.',20)
        out+=boundary('M250,176 Q268,155 284,174 L286,200 Q307,204 320,226 L332,268 L309,287 L299,326 L319,382 L326,420 L312,446 L280,444 L269,430 L277,411 L261,379 L241,342 L227,305 L216,284 L205,276 L207,250 L231,234 L244,211 Z')
        out+=text(25,560,['Entrano: aria, acqua e alimenti.', 'Escono: aria espirata, sudore e altre sostanze.'],24)
        out+=text(25,645,['Energia: trasferita attraverso calore e lavoro.', 'Gli scambi descrivono il corpo durante l’attività;','non devono essere tutti visibili o simultanei nella foto.'],21)
        H=760
    elif key=='TS-5':
        out+=text(28,42,'Sistema: il motore nel suo insieme',25)
        out+=text(28,82,'Scambi durante il funzionamento',21)
        out+=boundary('M307,230 L340,184 L418,171 L647,227 L689,256 L716,310 L716,406 L666,458 L627,485 L493,490 L362,452 L256,394 L248,354 L294,297 Z')
        out+=text(25,560,['Aria e','combustibile'],22)+text(395,575,'Motore',24)+text(695,560,['Gas di','scarico'],22)
        out+=line(250,575,350,575,True)+line(550,575,645,575,True)
        out+=text(25,640,['Energia in uscita: lavoro attraverso l’albero motore', 'e trasferimento all’ambiente.'],23)
        out+=text(25,720,'Il confine comprende il motore, non l’intera automobile.',21)
        H=770
    elif key=='TS-6':
        out+=text(28,42,'Sistema: una singola pila integra',25)
        out+=text(28,82,'La foto mostra pile usate nella raccolta per il riciclo.',20)
        out+=boundary('M481,198 Q507,188 532,199 L547,294 Q546,312 520,315 Q497,315 488,302 Z')
        out+=text(25,575,['Nel modello di una pila che alimenta un circuito:', 'energia elettrica trasferita all’esterno;', 'possibile energia ceduta come calore.'],24)
        out+=text(25,700,'Nessun flusso macroscopico di materia attraverso l’involucro.',22)
        H=755
    else:
        out+=text(28,42,'Sistema: una delle molle',25)
        out+=text(28,82,'Molle da trazione: consideriamo allungamento e rilascio.',20)
        out+=boundary('M355,215 Q383,205 374,227 Q340,251 347,283 Q358,312 395,320 L404,216 Q409,199 435,198 L596,187 Q612,185 618,204 L631,202 L625,192 Q628,178 640,182 Q686,204 675,266 Q665,312 616,324 L429,343 Q401,346 377,334 Q321,324 318,286 Q315,249 355,215 Z')
        out+=line(348,255,270,255,True)+line(671,245,742,245,True)
        out+=text(25,550,['Allungamento: le forze tirano i due estremi;', 'la molla riceve energia tramite lavoro.'],24)
        out+=text(25,640,['Rilascio: la molla può compiere lavoro all’esterno.', 'La materia resta la stessa; il confine cambia forma.'],23)
        H=735
    return H,out

def figure(key,caption):
    name,source,author,lic,url=META[key]
    meta=attributes('https://commons.wikimedia.org/wiki/File:'+source,author,lic,url,
        'Foto completa, senza ritaglio; sovrapposizione di contorni, frecce ed etichette didattiche. Schema sotto la stessa licenza della foto.' if key!='TS-0' else 'Nessuna modifica; visualizzazione proporzionale.')
    if key=='TS-0':
        return f'<figure class="visual cover" id="ts-0" {meta}><div class="image-frame"><div class="overview"><img src="{data(name)}" width="3100" height="3100" alt="Galassie del campo ultra profondo di Hubble" decoding="async"></div></div><figcaption>{escape(caption)}</figcaption></figure>'
    H,content=scene(key);sid=key.lower()
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {H}" width="900" height="{H}" style="display:block;width:100%;height:auto" role="img" aria-labelledby="titolo-{sid} descrizione-{sid}"><title id="titolo-{sid}">{escape(caption)}</title><desc id="descrizione-{sid}">Fotografia completa e schema degli scambi, con il sistema indicato e le spiegazioni sotto l’immagine.</desc><g id="scena-{sid}"><rect width="900" height="{H}" fill="white"/>{content}</g></svg>'
    zoom=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {H}" width="900" height="{H}" style="display:block;min-width:900px;width:100%;height:auto" role="img" aria-label="{escape(caption,quote=True)}"><use href="#scena-{sid}"/></svg>'
    # Il comando serve alle etichette didattiche, non alle fotografie prive di scritte rilevanti.
    zoom_control=''
    if '<text ' in content:
        zoom_control=f'<details class="image-zoom"><summary><span class="zoom-expand">Ingrandisci l’immagine</span><span class="zoom-collapse">Rimpicciolisci l’immagine</span></summary><div class="zoom-scroll" tabindex="0" role="region" aria-label="Immagine ingrandita scorrevole">{zoom}</div></details>'
    return f'<figure class="visual diagram" id="{sid}" {meta}><div class="image-frame"><div class="overview">{svg}</div>{zoom_control}</div><figcaption>{escape(caption)}</figcaption></figure>'

def inline(s):
    s=escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    for n,key in enumerate(['universo','pile'],1):
        s=s.replace('[^'+key+']',f'<sup class="note-ref"><a href="#nota-{key}" id="richiamo-{key}" role="doc-noteref" aria-label="Nota {n}">[{n}]</a></sup>')
    return s

def main():
    md=(WORK/'bozza.md').read_text()
    blocks=md.split('\n\n');body=[];headings=[];notes=[];current=None;cover=None
    for block in blocks:
        b=block.strip()
        if not b or b.startswith('# ') or b.startswith('<!--'):continue
        if b.startswith('[IMMAGINE'):
            current=re.search(r'TS-\d',b)[0];continue
        if b.startswith('Didascalia:'):
            f=figure(current,b.removeprefix('Didascalia:').strip())
            if current=='TS-0':cover=f
            else:body.append(f)
            continue
        if b.startswith('## '):
            title=b[3:];sid=['una-domanda-enorme','sistema-ambiente-confine','sistemi-isolati','sistemi-aperti','sistemi-chiusi','domande-di-verifica'][len(headings)]
            headings.append((sid,title));body.append(f'<div class="section-heading"><span class="section-number" aria-hidden="true">{len(headings):02}</span><h2 id="{sid}" data-toc tabindex="-1">{escape(title)}</h2></div>');continue
        if b.startswith('[^'):
            key,txt=re.match(r'\[\^(.+?)\]: (.*)',b).groups();notes.append(f'<li id="nota-{key}">{inline(txt)} <a href="#richiamo-{key}" role="doc-backlink" aria-label="Torna al richiamo della nota">↩</a></li>');continue
        if re.match(r'1\. ',b):
            body.append('<ol class="questions">'+''.join('<li>'+inline(re.sub(r'^\d+\. ','',s))+'</li>' for s in b.splitlines())+'</ol>');continue
        body.append('<p>'+inline(b)+'</p>')
    template=(ROOT/'riferimenti/TEMA_DISPENSE.html').read_text()
    template=re.sub(r'<!-- MODELLO CANONICO.*?-->','<!-- Articolo autonomo; tema canonico v8. -->',template, count=1,flags=re.S)
    template=template.replace('<title>Tema grafico delle dispense — modello riutilizzabile</title>',f'<title>{TITLE} — Materia Oscura</title>')
    template=template.replace('name="version" content="v8"','name="version" content="v3"',1).replace('name="date" content="2026-10-18"','name="date" content="2026-10-19"',1)
    template=template.replace('Modello autonomo del tema grafico comune a tutti i capitoli futuri.','Sistema, ambiente e confine; scambi di materia ed energia; sistemi aperti, chiusi e isolati.')
    template=template.replace('Nome dell’area tematica','Materia e calore').replace('Titolo dell’articolo',TITLE)
    template=template.replace('<span class="sidebar-label">Fisica</span>','<span class="sidebar-label">Materia e calore</span>')
    template=re.sub(r'<nav class="sidebar-nav".*?</nav>', '<nav class="sidebar-nav" aria-label="Sezioni dell’articolo"><ol>'+''.join(f'<li class="level-2"><a href="#{sid}"><span class="item-number" aria-hidden="true">{i:02}</span><span>{escape(title)}</span></a></li>' for i,(sid,title) in enumerate(headings,1))+'</ol></nav>',template,count=1,flags=re.S)
    template=re.sub(r'<figure class="visual cover">.*?</figure>',lambda _:cover,template,count=1,flags=re.S)
    template=re.sub(r'(<article class="article">).*?(<nav class="bottom-links")',lambda m:m[1]+''.join(body)+m[2],template,count=1,flags=re.S)
    template=re.sub(r'(<details class="chapter-notes".*?<ol>).*?(</ol>)',lambda m:m[1]+''.join(notes)+m[2],template,count=1,flags=re.S)
    template=template.replace('Versione v8 · 2026-10-18','Versione v3 · 19 ottobre 2026')
    # Marker condiviso da tutti gli schemi; resta definito anche quando una overview è nascosta.
    defs='<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" aria-hidden="true" style="position:absolute"><defs><marker id="freccia" markerUnits="userSpaceOnUse" markerWidth="28" markerHeight="28" viewBox="0 0 8 8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#0066b3"/></marker></defs></svg>'
    template=template.replace('<main>','<main>'+defs,1)
    TARGET.write_text(template)
    print(TARGET.name,TARGET.stat().st_size,'byte')

if __name__=='__main__':main()
