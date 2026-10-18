"""Genera le due anteprime autonome dalle bozze approvate e dal tema v7."""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import base64, copy, hashlib, io, json, re, unicodedata
import markdown

ROOT = Path(__file__).resolve().parents[2]
SOURCE = BeautifulSoup((ROOT/'potenza_termica_conduzione_convezione_it.html').read_text(), 'html.parser')
THEME = (ROOT/'riferimenti/TEMA_DISPENSE.html').read_text()
IMAGES = SOURCE.select('img')
REPORT = {}

def fragment(s):
    return BeautifulSoup(s, 'html.parser')

def data(path):
    p = Path(path)
    mime = {'.jpg':'image/jpeg','.png':'image/png','.gif':'image/gif','.svg':'image/svg+xml'}[p.suffix]
    return 'data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()

def slug(t):
    t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',t).strip('-')

def inline(t):
    return markdown.markdown(t).removeprefix('<p>').removesuffix('</p>')

def figure(src,alt,ident,zoom=False,classes='photo',animated=False):
    f=fragment('<figure class="visual '+classes+'" id="'+ident+'"><div class="image-frame"><div class="overview"><img alt="" loading="lazy" decoding="async"></div></div><figcaption></figcaption></figure>').figure
    im=f.img;im['src']=src;im['alt']=alt
    if animated:
        b=base64.b64decode(src.split(',',1)[1]);image=Image.open(io.BytesIO(b));image.seek(0)
        out=io.BytesIO();image.convert('RGBA').save(out,format='PNG')
        im['data-still']='data:image/png;base64,'+base64.b64encode(out.getvalue()).decode()
        im['data-animated']='true'
        f.append(fragment('<p><button class="button" type="button" data-animation-toggle aria-pressed="false">Metti in pausa l’animazione</button></p>').p)
    if zoom:
        z=fragment('<details class="image-zoom"><summary><span class="zoom-expand">Ingrandisci l’immagine</span><span class="zoom-collapse">Rimpicciolisci l’immagine</span></summary><div class="zoom-scroll" tabindex="0" role="region" aria-label="Immagine ingrandita scorrevole"><img loading="lazy" decoding="async" style="min-width:900px" data-zoom-copy=""></div></details>').details
        z.img['alt']=alt;f.select_one('.image-frame').append(z)
    return f

def old(index,ident,zoom=False,animated=False):
    return figure(IMAGES[index]['src'], IMAGES[index]['alt'],ident,zoom,'gif' if animated else 'diagram' if zoom else 'photo',animated)

def formula(tex):
    formulas={
        r'P=\frac{Q}{\Delta t}':('Potenza termica media','P uguale Q diviso delta t','<span>P = <span class="fraction"><span>Q</span><span>Δt</span></span></span>'),
        r'Q=P\cdot\Delta t':('Energia trasferita','Q uguale P per delta t','<span>Q = P · Δt</span>'),
        r'P=\frac{\lambda\cdot A\cdot\Delta T}{s}':('Legge di Fourier','P uguale lambda per A per delta T diviso s','<span>P = <span class="fraction"><span>λ · A · ΔT</span><span>s</span></span></span>')}
    key=re.sub(r'\s+','',tex);formulas={re.sub(r'\s+','',k):v for k,v in formulas.items()};label,alt,body=formulas[key]
    return fragment(f'<div class="equation"><div class="equation-label">{label}</div><div class="math" role="math" aria-label="{alt}">{body}</div></div>').div

RUNTIME='''
(()=>{
 document.querySelectorAll('[data-zoom-copy]').forEach(img=>{img.src=img.closest('figure').querySelector('.overview img').src;});
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 document.querySelectorAll('img[data-animated]').forEach(img=>{
  const original=img.src,still=img.dataset.still,button=img.closest('figure').querySelector('[data-animation-toggle]');
  let playing=!reduced.matches;
  function sync(){img.src=playing?original:still;button.textContent=playing?'Metti in pausa l’animazione':'Riprendi l’animazione';button.setAttribute('aria-pressed',String(!playing));}
  button.addEventListener('click',()=>{playing=!playing;sync();});
  reduced.addEventListener('change',()=>{playing=!reduced.matches;sync();});sync();
 });
})();
'''

def build(chapter):
    folder=ROOT/'lavorazione'/chapter
    md=(folder/'bozza.md').read_text();title=chapter.capitalize()
    maintext,notes=md.split('## Note\n',1)
    notesmap={int(n):t.strip() for n,t in re.findall(r'^\[(\d+)\] (.*?)(?=\n\n\[\d+\]|\Z)',notes,flags=re.M|re.S)}
    soup=BeautifulSoup(THEME,'html.parser')
    soup.title.string=title+' — Materia Oscura'
    soup.select_one('meta[name="version"]')['content']='v1'
    soup.select_one('meta[name="description"]')['content']=('Conduzione del calore, conduttori e isolanti, potenza termica e legge di Fourier.' if chapter=='conduzione' else 'Convezione naturale e forzata: termosifone, termiche, Sole e sistemi di raffreddamento.')
    author=soup.new_tag('meta',attrs={'name':'author','content':'Riccardo Musumarra'});soup.head.append(author)
    soup.select_one('h1').string=title;soup.select_one('.kicker').string='Materia e calore'
    soup.select_one('.sidebar-book p').string=title;soup.select_one('.sidebar-label').string='Materia e calore'
    soup.select_one('.footer').string='Versione v1 · 18 ottobre 2026'
    cover=soup.select_one('.cover')
    cv=figure(data(folder/'risorse'/('copertina-takoyaki.jpg' if chapter=='conduzione' else 'copertina-plutone.jpg')),
               'Takoyaki in cottura sulla piastra metallica.' if chapter=='conduzione' else 'Celle poligonali nel ghiaccio di azoto di Sputnik Planitia, su Plutone.', 'copertina', classes='cover')
    if chapter=='convezione':cv.figcaption.append(fragment(inline('Le strutture poligonali di Sputnik Planitia, su Plutone, sono associate a lenti moti convettivi nel ghiaccio di azoto.[6]')))
    else:cv.figcaption.string='La piastra metallica trasferisce energia al cibo con cui è a contatto.'
    cover.replace_with(cv)
    article=soup.select_one('article');bottom=copy.deepcopy(article.select_one('.bottom-links'));article.clear()
    mapping={'IMMAGINE 03':(2,False,False),'IMMAGINE 07':(5,False,False),'IMMAGINE 09':(6,True,False),'IMMAGINE 10':(7,False,False),'IMMAGINE 12':(8,False,True),'IMMAGINE 14':(10,True,False),'IMMAGINE 17':(13,True,False),'IMMAGINE 18':(14,True,False),'IMMAGINE 06 E GRAFICO G-1':(4,True,False)}
    files={'IMMAGINE E-1':('elettroni-metallo.gif','Ioni del reticolo metallico in grigio ed elettroni di conduzione in rosa.',False,True),'IMMAGINE V-F':('ventilatore-forzata.jpg','Ventilatore da tavolo con tre pale e base rossa.',False,False),'IMMAGINE N-1':('poiana-termica.jpg','Poiana codarossa in volo ad ali distese nella termica.',False,False),'SCHEMA N-2':('termica-numerata.png','Termica: terreno riscaldato (1), risalita (2), ricircolo discendente (3), eventuale nube (A).',True,False),'SCHEMA S-1A':('sole-schema-it.png','Sezione illustrata di una stella simile al Sole con etichette italiane.',True,False),'IMMAGINE S-1B':('sole-granulazione.jpg','Granulazione della fotosfera solare: regioni luminose separate da bordi scuri.',True,False)}
    last=None;counter=0
    for block in maintext.split('\n\n'):
        b=block.strip()
        if not b or b.startswith('# ') or b.startswith('[COPERTINA') or b.startswith('![') or b.startswith('Didascalia di copertina:'):continue
        if b.startswith('['):
            key=b.split(' —')[0][1:]
            if key.startswith('TABELLA'):continue
            if key=='VIDEO 05':
                f=old(3,'video-barrette');im=f.img;im.extract()
                link=copy.deepcopy(SOURCE.select_one('.video-thumb'));link.clear();link.append(im);link.append(fragment('<span class="video-play" aria-hidden="true">▶</span>').span)
                f.select_one('.overview').append(link);article.append(f);last=f;continue
            if key in mapping:
                idx,z,a=mapping[key];f=old(idx,'visuale-'+slug(key),z,a)
                article.append(f);last=f
                if idx==4:
                    svg=copy.deepcopy(SOURCE.select_one('#profilo-parete'))
                    # Riusa il grafico approvato come immagine SVG autonoma.
                    svg['xmlns']='http://www.w3.org/2000/svg';svg['viewBox']='0 0 640 420'
                    svg.attrs.pop('viewbox',None)
                    for tag in svg.find_all():
                        if tag.has_attr('viewbox'):tag['viewBox']=tag.attrs.pop('viewbox')
                    src='data:image/svg+xml;base64,'+base64.b64encode(str(svg).encode()).decode()
                    graph=figure(src,'Profilo lineare della temperatura nello spessore: 20 °C sulla faccia interna, −10 °C su quella esterna.','grafico-parete',True,'diagram')
                    graph.figcaption.string='Il grafico rappresenta soltanto lo spessore della parete, tra le due facce.'
                    article.append(graph)
                continue
            if key in files:
                name,alt,z,a=files[key];f=figure(data(folder/'risorse'/name),alt,slug(key),z,'gif' if a else 'photo portrait' if key=='IMMAGINE V-F' else 'diagram' if z else 'photo',a)
                article.append(f);last=f;continue
            raise ValueError('Segnaposto sconosciuto: '+key)
        if b.startswith('Didascalia:'):
            if last is None:raise ValueError('Didascalia senza immagine')
            last.figcaption.clear();last.figcaption.append(fragment(inline(b.removeprefix('Didascalia:').strip())));continue
        if b.startswith('\\['):article.append(formula(b[2:-2].strip()));continue
        rendered=fragment(markdown.markdown(b,extensions=['tables']))
        for el in list(rendered.contents):article.append(el.extract())
    # Applicare lo stesso componente del tema a tutte le intestazioni.
    toc=[]
    for h in list(article.select('h2,h3')):
        level=int(h.name[1]);ident=slug(h.text);h['id']=ident;h['data-toc']='';h['tabindex']='-1'
        if level==2:
            counter+=1;wrapper=soup.new_tag('div',attrs={'class':'section-heading'});number=soup.new_tag('span',attrs={'class':'section-number','aria-hidden':'true'});number.string=f'{counter:02}';h.wrap(wrapper);wrapper.insert(0,number)
        toc.append((level,ident,h.text,f'{counter:02}' if level==2 else ''))
    lists=article.select('ol')
    if lists:
        for extra in lists[1:]:
            for li in list(extra.select(':scope > li')):lists[0].append(li.extract())
            extra.decompose()
        lists[0]['class']='questions'
    for table in article.select('table'):
        table['aria-label']='Conducibilità termica indicativa di otto materiali'
        wrap=soup.new_tag('div',attrs={'class':'table-scroll','tabindex':'0','role':'region','aria-label':'Tabella scorrevole delle conducibilità termiche'});table.wrap(wrap)
    article.append(bottom)
    nav=soup.select_one('.sidebar-nav ol');nav.clear()
    for level,ident,text,num in toc:
        li=soup.new_tag('li',attrs={'class':'level-'+str(level)});a=soup.new_tag('a',href='#'+ident)
        sp=soup.new_tag('span',attrs={'class':'item-number','aria-hidden':'true'});sp.string=num;a.append(sp);sp=soup.new_tag('span');sp.string=text;a.append(sp);li.append(a);nav.append(li)
    ol=soup.select_one('.chapter-notes ol');ol.clear()
    for n,text in sorted(notesmap.items()):
        li=soup.new_tag('li',id='nota-'+str(n));li.append(fragment(inline(text)));ol.append(li)
    # Convertire i richiami, anche ripetuti, con ritorni univoci.
    counts={}
    for t in list(soup.find_all(string=True)):
        if t.find_parent(['script','style','template']) or t.find_parent(class_='chapter-notes'):continue
        if not re.search(r'\[\d+\]',str(t)):continue
        parts=re.split(r'(\[\d+\])',str(t));new=[]
        for part in parts:
            if re.fullmatch(r'\[\d+\]',part):
                n=int(part[1:-1]);counts[n]=counts.get(n,0)+1;rid=f'richiamo-{n}-{counts[n]}'
                new.append(fragment(f'<sup class="note-ref"><a href="#nota-{n}" id="{rid}" role="doc-noteref" aria-label="Nota {n}">[{n}]</a></sup>').sup)
            else:new.append(part)
        t.replace_with(*new)
    for n,count in counts.items():
        li=soup.select_one('#nota-'+str(n))
        if li is None:raise ValueError('Nota mancante '+str(n))
        for k in range(1,count+1):li.append(fragment(f' <a href="#richiamo-{n}-{k}" role="doc-backlink" aria-label="Torna al richiamo {k} della nota {n}">↩</a>'))
    credits=soup.select_one('.credits');credits.select_one('p').decompose()
    if chapter=='conduzione':
        text='''<ul><li>Copertina: City Foodsters, <a href="https://commons.wikimedia.org/wiki/File:Honkeohtako%27s_takoyaki,_Osaka;_December_2013_(03).jpg">Takoyaki, Osaka</a>, <a href="https://creativecommons.org/licenses/by/2.0/">CC BY 2.0</a>, senza modifiche.</li><li>Elettroni nel metallo: Jerónimo Cueto, <a href="https://commons.wikimedia.org/wiki/File:Enlace_metalico.gif">Enlace metalico.gif</a>, <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. Animazione originale; fermo immagine per pausa e movimento ridotto.</li><li>Miniatura video: fotogramma dell’esperimento NCSSM Online; collegamento al video originale su YouTube.</li><li>Zuppa, caffettiera, vetrocamera, igloo, palo gelato e parete: materiali già selezionati per la dispensa di origine; diritti dei rispettivi titolari. Etichette di parete e vetrocamera tradotte in italiano. Fonte e licenza di questi materiali non sono documentate nella fonte storica: gli obblighi di attribuzione restano da chiarire prima della diffusione pubblica.</li><li>Grafico della parete: elaborazione didattica già approvata nella fonte v7.</li></ul>'''
    else:
        text='''<ul><li>Copertina Plutone: NASA/JHUAPL/SwRI, <a href="https://commons.wikimedia.org/wiki/File:Pluto%E2%80%99s_Heart_-_Like_a_Cosmic_Lava_Lamp.jpg">Pluto’s Heart</a>, pubblico dominio secondo Commons; senza modifiche.</li><li>Ventilatore: Berthold Werner, <a href="https://commons.wikimedia.org/wiki/File:Ventilator_BW_2026-06-19_16-42-30_standing.jpg">Ventilator BW</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>, senza modifiche.</li><li>Poiana codarossa: NPS / Jacob W. Frank, <a href="https://commons.wikimedia.org/w/index.php?curid=189439471">Red-tailed hawk soaring on a thermal</a>, pubblico dominio (National Park Service); senza modifiche.</li><li>Schema della termica: Dake, <a href="https://commons.wikimedia.org/wiki/File:Thermal_column.svg">Thermal column.svg</a>, <a href="https://creativecommons.org/licenses/by/2.5/">CC BY 2.5</a>, versione PNG senza modifiche.</li><li>Struttura della stella: NASA/CXC/M.Weiss, <a href="https://chandra.harvard.edu/photo/2005/neon/more.html">Illustration of Convection in Sun-like Star</a>, pubblico dominio secondo Commons e <a href="https://chandra.harvard.edu/photo/image_use.html">politica Chandra</a>. Etichette tradotte in italiano con elaborazione del raster; originale conservato nel repository.</li><li>Granulazione: NSO/AURA/NSF, Daniel K. Inouye Solar Telescope, <a href="https://commons.wikimedia.org/wiki/File:Highest_resolution_photo_of_Sun_(NSF)_as_of_January_20,_2020.jpg">fotografia della fotosfera</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, senza modifiche.</li><li>Stanza, fotografia annotata del processore e circuito del radiatore: materiali già approvati della dispensa di origine; diritti dei rispettivi titolari. Schemi della stanza e del radiatore tradotti in italiano. Fonte e licenza di questi materiali non sono documentate nella fonte storica: gli obblighi di attribuzione restano da chiarire prima della diffusione pubblica.</li></ul>'''
    credits.insert(1,fragment(text))
    # Solo collegamenti tra bozze già presenti nel ramo; nessun nuovo URL pubblico.
    chnav=soup.new_tag('nav',attrs={'class':'chapter-navigation','aria-label':'Articoli collegati'})
    other='convezione' if chapter=='conduzione' else 'conduzione'
    rel='next' if chapter=='conduzione' else 'prev'
    chnav.append(fragment(f'<a rel="{rel}" href="../{other}/bozza.html"><small>Articolo {"successivo →" if rel=="next" else "precedente ←"}</small><span>{other.capitalize()}</span></a>'))
    soup.select_one('footer').insert_before(chnav)
    extra=soup.new_tag('script',attrs={'data-chapter-media':''});extra.string=RUNTIME;soup.body.append(extra)
    # Stili dei soli componenti assenti nel modello, senza cambiare il tema.
    css=soup.new_tag('style',attrs={'data-chapter-components':''});css.string='''.table-scroll{overflow-x:auto;max-width:100%;margin:32px 0;border:2px solid #080808}.table-scroll table{border-collapse:collapse;width:100%;min-width:570px;font-size:17px;line-height:1.5}.table-scroll th,.table-scroll td{padding:13px 15px;text-align:left;border-bottom:1px solid #aaa}.table-scroll th{background:#c4c4c4;font-weight:650}.table-scroll tbody tr:last-child td{border-bottom:0}.video-thumb{position:relative;display:block;width:100%}.video-play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:#080808;color:white;border:3px solid white;padding:12px 22px;font-size:32px;line-height:1.4}.visual.gif p{margin:14px 0 0}.visual.gif .button{font-family:inherit;cursor:pointer}''';soup.head.append(css)
    result=str(soup)
    assert len(result.encode())<20_000_000
    assert not soup.select('template')
    assert len(soup.select('.questions > li'))==(12 if chapter=='conduzione' else 7)
    (folder/'bozza.html').write_text(result)
    REPORT[chapter]={'byte':len(result.encode()),'quesiti':len(soup.select('.questions > li')),'figure':len(soup.select('figure')),'sha256':hashlib.sha256(result.encode()).hexdigest()}

if __name__=='__main__':
    build('conduzione');build('convezione');print(json.dumps(REPORT,indent=2))
