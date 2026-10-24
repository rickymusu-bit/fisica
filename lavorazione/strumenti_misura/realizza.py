"""Genera i due capitoli autonomi e incorpora il modello condiviso delle misure.

Non modifica il manifest o gli HTML storici. I materiali mancanti sono dichiarati
nelle anteprime di lavorazione e non sostituiti con immagini non autorizzate.
"""
from pathlib import Path
from html import escape
import base64
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scripts'))
import credits
from stringhe_theme import navigation_header, icon

AREA = 'Introduzione alla fisica e alla misura'
NOTE_REFS = {}
CHAPTERS = {
    'strumenti_misura': {'title': 'Gli strumenti di misura', 'name': 'strumenti_misura_it.html', 'mode': 'explore',
        'cover': 'copertina-nist.jpg', 'author': 'N. Phillips/NIST', 'license': 'Pubblico dominio (PD-USGov)',
        'license_url': 'https://creativecommons.org/publicdomain/mark/1.0/',
        'source': 'https://commons.wikimedia.org/wiki/File:Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg',
        'description': 'Strumenti di misura, portata, risoluzione, sensibilità, prontezza, precisione e accuratezza, con bilancia virtuale.'},
    'errori_incertezza_misura': {'title': 'Errori e incertezza di misura', 'name': 'errori_incertezza_misura_it.html', 'mode': 'lab',
        'cover': 'copertina-rumore-tv.jpg', 'author': 'Mysid', 'license': 'Pubblico dominio (PD-self)',
        'license_url': 'https://commons.wikimedia.org/wiki/File:TV_noise.jpg#Licensing',
        'source': 'https://commons.wikimedia.org/wiki/File:TV_noise.jpg',
        'description': 'Errori, misure ripetute, media, semidispersione e incertezza, con misure di masse nota e ignota e grafico interattivo.'}
}
EXTRA = '''<style data-component="misure-capitoli">
.measure-scroll{max-width:100%;overflow-x:auto;border:1px solid var(--line);border-radius:8px}.measure-table{width:100%;min-width:510px;border-collapse:collapse;font-size:16px;line-height:1.55}.measure-table th,.measure-table td{padding:12px 14px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.measure-table th{background:var(--surface-soft)}.measure-table caption{padding:14px;text-align:left;font-weight:600}.measure-scroll:focus-visible{outline:3px solid var(--accent);outline-offset:3px}.measure-math{max-width:100%;overflow-x:auto}.measure-math math{font-family:Lexend,Arial,sans-serif;font-size:1em}.measure-math .math-step{flex:0 0 auto;max-width:100%;overflow-x:auto}.measure-inline-math math{font-family:Lexend,Arial,sans-serif;font-size:1em}.measure-pending{padding:20px;border:1px dashed var(--line);border-radius:8px;color:var(--muted);font-size:15px}.measure-static-graph svg{display:block;min-width:640px;width:100%;height:auto;background:var(--surface)}.measure-graph-text{fill:var(--ink)}.measure-procedure li{margin-bottom:14px}.measure-sensor-table{margin:20px 0}
</style>'''


def mathml(source):
    source = source.strip().replace('{,}', ',')
    pos = 0
    def group():
        nonlocal pos
        while pos < len(source) and source[pos].isspace(): pos += 1
        if pos >= len(source): raise ValueError('Gruppo matematico mancante')
        if source[pos] == '{':
            pos += 1
            return '<mrow>' + parse(True) + '</mrow>'
        c = source[pos]; pos += 1
        return '<mn>' + c + '</mn>' if c.isdigit() else '<mi>' + escape(c) + '</mi>'
    def parse(closing=False):
        nonlocal pos
        out = []
        while pos < len(source):
            c = source[pos]
            if c == '}' and closing:
                pos += 1; return ''.join(out)
            if c.isspace(): pos += 1
            elif c == '{': out.append(group())
            elif c in '^_':
                pos += 1; value = group(); base = out.pop(); tag = 'msup' if c == '^' else 'msub'
                out.append('<' + tag + '>' + base + value + '</' + tag + '>')
            elif c == '\\':
                match = re.match(r'\\([A-Za-z]+|.)', source[pos:]); command = match[1]; pos += len(match[0])
                if command == 'frac': out.append('<mfrac>' + group() + group() + '</mfrac>')
                elif command == 'bar': out.append('<mover accent="true">' + group() + '<mo>¯</mo></mover>')
                elif command == 'mathrm': out.append(group().replace('<mi>', '<mi mathvariant="normal">'))
                elif command in {'Delta', 'pm', 'cdot', 'ldots', '%'}:
                    out.append('<mo>' + {'Delta':'Δ','pm':'±','cdot':'·','ldots':'…','%':'%'}[command] + '</mo>')
                elif command in {'max', 'min'}: out.append('<mi mathvariant="normal">' + command + '</mi>')
                elif command in {',',' '}: out.append('<mspace width="0.2em"/>')
                else: raise ValueError('Comando matematico non gestito: ' + command)
            elif c.isdigit():
                match = re.match(r'\d+(?:,\d+)?', source[pos:]); out.append('<mn>' + match[0] + '</mn>'); pos += len(match[0])
            elif c.isalpha():
                match = re.match(r'[A-Za-z]+', source[pos:]); value = match[0] if match else c
                out.append('<mi>' + escape(value) + '</mi>'); pos += len(value)
            else:
                out.append('<mo>' + escape('−' if c == '-' else c) + '</mo>'); pos += 1
        if closing: raise ValueError('Gruppo matematico non chiuso')
        return ''.join(out)
    return '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>' + parse() + '</mrow></math>'


def inline(source):
    pieces = re.split(r'(\\\([\s\S]*?\\\))', source)
    output = []
    for piece in pieces:
        if piece.startswith(r'\(') and piece.endswith(r'\)'):
            output.append('<span class="measure-inline-math">' + mathml(piece[2:-2]) + '</span>'); continue
        piece = escape(piece)
        piece = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', piece)
        def note_ref(match):
            number=match[1]; count=NOTE_REFS.get(number,0)+1; NOTE_REFS[number]=count
            identity='richiamo-' + number + ('' if count==1 else '-' + str(count))
            return '<sup class="note-ref"><a href="#nota-' + number + '" id="' + identity + '" role="doc-noteref" aria-label="Nota ' + number + '">[' + number + ']</a></sup>'
        piece = re.sub(r'\[\^(\d+)\]',note_ref,piece)
        output.append(piece)
    return ''.join(output)


def equation(block):
    source = block.removeprefix(r'\[').removesuffix(r'\]').strip()
    depth = 0; start = 0; parts = []
    for i, char in enumerate(source):
        if char == '{': depth += 1
        elif char == '}': depth -= 1
        elif char in '=≈' and depth == 0:
            if i > start: parts.append(source[start:i].strip())
            start = i
    parts.append(source[start:].strip())
    return '<div class="equation"><div class="math measure-math" role="math">' + ''.join('<span class="math-step">' + mathml(part) + '</span>' for part in parts) + '</div></div>'


def uri(path):
    suffix = path.suffix.lower()
    mime = {'.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.svg':'image/svg+xml','.webp':'image/webp'}[suffix]
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()


def metadata(data):
    return ' '.join('data-credit-' + field + '="' + escape(value,quote=True) + '"' for field,value in data.items() if value)


def assets(folder):
    path = folder / 'risorse/immagini.json'
    return json.loads(path.read_text()) if path.exists() else {}


def object_svg(data, label=None):
    box=data.get('viewbox',[0,0,data['width'],data['height']])
    return '<svg class="generated-object" viewBox="' + ' '.join(str(v) for v in box) + '" role="img" aria-label="' + escape(label or data['alt'],quote=True) + '"><use href="#' + data['symbol'] + '"/></svg>'


def object_definitions(folder, image_assets):
    unique={data['symbol']:data for data in image_assets.values() if data.get('symbol')}
    if not unique: return ''
    content=''.join('<image id="' + symbol + '" width="' + str(data['width']) + '" height="' + str(data['height']) + '" href="' + uri(folder/data['path']) + '"/>' for symbol,data in unique.items())
    return '<svg class="sim-art-definitions" width="0" height="0" aria-hidden="true" focusable="false" data-credit-id="bilancia-pesetti-generati"><defs>' + content + '</defs></svg>'


def photo(folder, key, caption, image_assets, *, sim=False):
    data = image_assets.get(key)
    if not data:
        label = {'bilancia':'Bilancia digitale con piatto', 'campione':'Campione da pesare'}.get(key, key)
        if sim: return '<div class="sim-photo-pending">' + escape(label) + ': immagine in attesa di scelta.</div>'
        return '<figure class="visual" id="' + key.lower() + '"><div class="measure-pending">Figura ' + escape(key) + ': immagine con licenza in attesa.</div><figcaption>' + inline(caption) + '</figcaption></figure>'
    path = folder / data['path']
    if not path.is_file(): raise FileNotFoundError(path)
    attrs = metadata({k:data.get(k) for k in ('source','author','license','license-url','changes','id')})
    image = object_svg(data) if data.get('symbol') else '<img src="' + uri(path) + '" alt="' + escape(data['alt'],quote=True) + '" loading="lazy" decoding="async">'
    if sim: return '<div ' + attrs + '>' + image + '</div>'
    classes='visual ' + ('diagram' if data.get('diagram') else 'photo') + (' portrait' if data.get('portrait') else '')
    zoom=''
    if data.get('zoom'):
        zoom='<details class="image-zoom"><summary class="media-icon-button" aria-label="Ingrandisci l’immagine"><span class="zoom-expand">' + icon('zoom-in') + '</span><span class="zoom-collapse">' + icon('zoom-out') + '</span></summary><div class="zoom-scroll" tabindex="0" role="region" aria-label="' + escape(data.get('zoom-label','Schema del parallasse ingrandito e scorrevole'),quote=True) + '">' + image.replace('<img ','<img style="min-width:1500px" ',1) + '</div></details>'
    caption_html='' if data.get('hide-caption') else '<figcaption>' + inline(caption) + '</figcaption>'
    return '<figure class="' + classes + '" id="' + key.lower() + '" ' + attrs + '><div class="image-frame"><div class="overview">' + image + '</div>' + zoom + '</div>' + caption_html + '</figure>'


def table(block, key):
    rows = [[cell.strip() for cell in row.strip('|').split('|')] for row in block.splitlines()]
    title = {'TAB-06':'Letture illustrative di una massa di riferimento di 100 g', 'TAB-07-2':'Cinque letture del tempo', 'TAB-07-1':'Risultato, incertezza e riferimento'}[key]
    head = '<thead><tr>' + ''.join('<th scope="col">' + inline(cell) + '</th>' for cell in rows[0]) + '</tr></thead>'
    body = '<tbody>' + ''.join('<tr>' + ''.join(('<th scope="row">' if i == 0 else '<td>') + inline(cell) + ('</th>' if i == 0 else '</td>') for i,cell in enumerate(row)) + '</tr>' for row in rows[2:]) + '</tbody>'
    return '<figure class="visual" id="' + key.lower() + '"><div class="measure-scroll" tabindex="0" role="region" aria-label="' + title + ', tabella scorrevole"><table class="measure-table"><caption>' + title + '</caption>' + head + body + '</table></div></figure>'


def static_graph():
    # Ricostruzione quantitativa della linea dei numeri originale, stessi dati.
    x = lambda t: 65 + (t - 2.30) / .20 * 670
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 255" role="img" aria-label="Cinque tempi: 2,31; 2,37; 2,40; 2,43; 2,49 s. Media 2,40 s, semidispersione 0,09 s."><rect width="800" height="255" fill="none"/>'
    svg += '<rect x="' + str(x(2.31)) + '" y="90" width="' + str(x(2.49)-x(2.31)) + '" height="65" fill="#a8d3ef" fill-opacity=".4"/>'
    svg += '<path d="M65 150H735" stroke="currentColor" stroke-width="2"/>'
    for t in [2.30,2.35,2.40,2.45,2.50]:
        svg += '<path d="M' + str(x(t)) + ' 144v12" stroke="currentColor"/><text class="measure-graph-text" x="' + str(x(t)) + '" y="182" font-size="19" text-anchor="middle">' + f'{t:.2f}'.replace('.',',') + '</text>'
    for t in [2.31,2.37,2.40,2.43,2.49]:
        svg += '<circle cx="' + str(x(t)) + '" cy="122" r="7" fill="#1676bf"/>'
    svg += '<path d="M' + str(x(2.4)) + ' 55V155" stroke="currentColor" stroke-width="2" stroke-dasharray="6 4"/>'
    svg += '<g class="measure-graph-text" font-family="Arial,sans-serif" font-size="20"><text x="400" y="32" text-anchor="middle">Media 2,40 s</text><text x="400" y="220" text-anchor="middle">Estremi 2,31–2,49 s; semidispersione 0,09 s</text><text x="735" y="250" text-anchor="end">Tempo (s)</text></g></svg>'
    return '<figure class="visual" id="graf-07-2" data-credit-id="grafico-misure-tempi"><div class="measure-scroll measure-static-graph" tabindex="0" role="region" aria-label="Grafico delle cinque letture, scorrevole">' + svg + '</div></figure>'


def simulation(folder, mode, image_assets, study=None):
    lab = mode == 'lab'
    title = ('Massa ignota' if study=='uncertainty' else 'Massa di riferimento') if lab else 'Pesetti e proprietà della bilancia'
    result = '<section class="measurement-sim" data-measurement="' + mode + '"' + (' data-study="' + study + '"' if study else '') + ' aria-label="' + title + '"><h3>' + title + '</h3>'
    result += '<p class="sim-intro">' + ('Le proprietà dello strumento sono fisse: portata 500 g, passo leggibile 1 g e risposta di circa 1 s.' if lab else 'Aggiungi i pesetti al piatto e varia una proprietà alla volta con gli slider sotto la bilancia.') + '</p>'
    generated=bool(image_assets.get('bilancia',{}).get('symbol'))
    if generated:
        weight=image_assets['pesetto-100'];box=weight['viewbox'];aspect=box[2]/box[3]
        result=result.replace('class="measurement-sim"','class="measurement-sim sim-has-balance"',1)
        result += '<div class="sim-stage sim-stage-generated"><div class="sim-balance-scene" data-weight-symbol="' + weight['symbol'] + '" data-weight-viewbox="' + ' '.join(str(v) for v in box) + '" style="--weight-aspect:' + str(aspect) + '">' + photo(folder,'bilancia','',image_assets,sim=True) + '<div class="sim-pan" data-pan></div><output class="sim-display sim-device-display" data-display aria-label="Indicazione della bilancia" aria-live="off">0 g</output></div><div class="sim-readout">'
    else:
        result += '<div class="sim-stage"><div>' + photo(folder,'bilancia','',image_assets,sim=True) + '</div><div class="sim-readout"><span class="sim-display-label">Indicazione della bilancia</span><output class="sim-display" data-display aria-live="off">0 g</output>'
    if not lab: result += '<p>Massa caricata: <strong data-loaded-mass>0 g</strong></p>'
    result += '</div></div>'
    button = lambda label, attr, primary=False: '<button type="button" data-interactive disabled ' + attr + (' class="sim-primary"' if primary else '') + '>' + label + '</button>'
    if not lab:
        result += '<div class="sim-weights" role="group" aria-label="Pesetti disponibili">'
        for m in [10,20,50,100,200]:
            img = ''
            if 'pesetto-' + str(m) in image_assets:
                img = photo(folder,'pesetto-' + str(m),'',image_assets,sim=True)
            scale=(m/200)**(1/3)
            result += button('<span class="sim-weight-thumb" style="--weight-size:' + str(scale) + '">' + img + '</span>' + str(m) + ' g', 'data-weight="' + str(m) + '" aria-pressed="false" aria-label="Aggiungi o rimuovi il pesetto da ' + str(m) + ' g"')
        result += button('Svuota il piatto','data-empty') + '</div><details class="sim-settings" open><summary>Proprietà della bilancia</summary><div class="sim-sliders">'
        properties = [('capacity','Portata',2,2,'Il massimo carico misurabile.'),('step','Risoluzione',2,0,'La più piccola variazione di massa distinguibile sul display.'),('response','Tempo di risposta',2,1,'Un tempo più breve corrisponde a maggiore prontezza.'),('offset','Accuratezza',5,5,'Più alta: letture più vicine alla massa caricata.'),('noise','Precisione',5,5,'Più alta: letture ripetute più vicine fra loro.')]
        for key,label,maximum,initial,helptext in properties:
            minimum = 0
            result += '<label class="sim-slider"><span class="sim-slider-head"><span>' + label + '</span><output data-property-output="' + key + '"></output></span><input type="range" data-interactive disabled data-property="' + key + '" min="' + str(minimum) + '" max="' + str(maximum) + '" step="1" value="' + str(initial) + '"><small>' + helptext + '</small></label>'
        result += '</div></details>'
    else:
        result += '<p data-sample-label>' + ('Campione B: massa ignota' if study=='uncertainty' else 'Campione A: riferimento 100 g') + '</p>'
        result += '<div class="sim-buttons">' + button('Appoggia e misura','data-measure',True) + '</div>'
    result += '<p class="sim-status" role="status" data-status>Simulazione pronta dopo il caricamento.</p><div class="sim-buttons">' + button('Registra lettura','data-record',True) + button('Cancella la serie corrente','data-clear') + button('Ripristina tutto','data-reset') + '</div>'
    result += '<noscript><p>Per usare la bilancia virtuale occorre attivare JavaScript. Teoria, tabelle e domande restano leggibili.</p></noscript>'
    if lab:
        result += '<figure class="visual"><div class="image-frame sim-chart-frame"><div class="overview"><div class="sim-chart" data-chart></div></div></div><figcaption data-chart-description>Il grafico sarà popolato dalle letture registrate.</figcaption></figure><p class="sim-legend">Un punto per lettura; i punti uguali sono impilati. Linea continua: media. ' + ('Fascia ambrata: ±U. I tratti alla base indicano gli estremi osservati.' if study=='uncertainty' else 'Linea tratteggiata: riferimento. Segmento rosso: errore della media.') + '</p>'
    result += '<div class="sim-scroll" tabindex="0" role="region" aria-label="Registro delle letture, tabella scorrevole"><table><caption>Letture registrate</caption><thead><tr>'
    headings = ['Campione','Prova','Lettura'] if lab else ['Massa caricata','Lettura','Stato','Proprietà']
    result += ''.join('<th scope="col">' + h + '</th>' for h in headings) + '</tr></thead><tbody data-rows></tbody></table></div>'
    result += '</section>'
    return result


def slug(title):
    plain = unicodedata.normalize('NFKD',title).encode('ascii','ignore').decode().lower()
    return re.sub('[^a-z0-9]+','-',plain).strip('-')


def render(key, data):
    NOTE_REFS.clear()
    folder = ROOT / 'lavorazione' / key
    metadata_path=folder/'risorse/realizzazione.json'
    if not metadata_path.exists():
        metadata_path.write_text(json.dumps({'version':'v1','date':datetime.now(timezone.utc).isoformat(timespec='seconds'),'approved_draft':'v4'},ensure_ascii=False,indent=2)+'\n')
    edition=json.loads(metadata_path.read_text())
    date=datetime.fromisoformat(edition['date']).astimezone(ZoneInfo('Europe/Rome'))
    month=['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre'][date.month-1]
    footer_date=f'{date.day} {month} {date.year}'
    text = (folder/'bozza.md').read_text().split('\n---\n',1)[0]
    main, notes = text.split('\n## Note\n',1)
    blocks = [b.strip() for b in main.split('\n\n') if b.strip()]
    image_assets = assets(folder)
    definitions=object_definitions(folder,image_assets)
    body = [definitions] if definitions else []
    headings = []; pending = None; cover_caption = ''; formulas = 0; missing = []
    for block in blocks:
        if block.startswith(('# ', '[EDITORIALE')): continue
        if block.startswith('[COP-'): pending = 'COVER'; continue
        if block.startswith('*') and block.endswith('*') and not block.startswith('**'):
            caption = block[1:-1]
            if pending == 'COVER': cover_caption = caption; pending = None
            elif pending and pending.startswith(('FIG-','SCH-')):
                body.append(photo(folder,pending,caption,image_assets));
                if pending not in image_assets: missing.append(pending)
                pending = None
            elif body and body[-1].endswith('</figure>'):
                body[-1]=body[-1][:-9] + '<figcaption>' + inline(caption) + '</figcaption></figure>'; pending=None
            else: body.append('<p class="visual-caption">' + inline(caption) + '</p>'); pending = None
            continue
        if block.startswith('[SIM-'):
            body.append(simulation(folder,data['mode'],image_assets,study='uncertainty' if block.startswith('[SIM-07-U') else 'error' if block.startswith('[SIM-07-E') else None)); continue
        if block.startswith('[PROSPETTO'):
            body.append('<div class="measure-scroll measure-sensor-table" tabindex="0" role="region" aria-label="Confronto della sensibilità"><table class="measure-table"><caption>Confronto illustrativo di due termometri a colonna</caption><thead><tr><th>Termometro</th><th>Allungamento per 1 °C</th></tr></thead><tbody><tr><th>A</th><td>2 mm</td></tr><tr><th>B</th><td>1 mm</td></tr></tbody></table></div>'); continue
        if block.startswith('[GRAF-'):
            body.append(static_graph()); pending = 'GRAPH'; continue
        if block.startswith('[TAB-'):
            if pending and pending.startswith(('FIG-','SCH-')):
                body.append(photo(folder,pending,'',image_assets))
                if pending not in image_assets: missing.append(pending)
            pending = re.match(r'\[(TAB-[\d-]+)',block)[1]; continue
        if block.startswith(('[FIG-','[SCH-')):
            if pending and pending.startswith(('FIG-','SCH-')):
                body.append(photo(folder,pending,'Bilancia digitale: strumento del confronto illustrativo.',image_assets));
                if pending not in image_assets: missing.append(pending)
            pending = re.match(r'\[((?:FIG|SCH)-[A-Za-z\d-]+)',block)[1]
            if image_assets.get(pending,{}).get('hide-caption'):
                body.append(photo(folder,pending,'',image_assets)); pending=None
            continue
        if block.startswith('|'):
            body.append(table(block,pending)); pending = None; continue
        if block.startswith('## '):
            title=block[3:]; sid=slug(title); number=len(headings)+1; headings.append((sid,title))
            body.append('<div class="section-heading"><span class="section-number" aria-hidden="true">' + str(number).zfill(2) + '</span><h2 id="' + sid + '" data-toc tabindex="-1">' + inline(title) + '</h2></div>'); continue
        if block.startswith(r'\['): body.append(equation(block)); formulas += 1; continue
        if re.match(r'1\. ',block):
            cls = 'questions' if headings[-1][1]=='Domande di verifica' else 'measure-procedure'
            body.append('<ol class="' + cls + '">' + ''.join('<li>' + inline(re.sub(r'^\d+\. ','',item)) + '</li>' for item in re.split(r'\n(?=\d+\. )',block)) + '</ol>'); continue
        if block.startswith('['): raise ValueError('Segnaposto non gestito: ' + block[:100])
        body.append('<p>' + inline(block) + '</p>')
    note_items = []
    for block in notes.strip().split('\n\n'):
        number,note = re.match(r'\[\^(\d+)\]:\s*(.*)',block,re.S).groups()
        backlinks=' '.join('<a href="#richiamo-' + number + ('' if i==1 else '-' + str(i)) + '" role="doc-backlink" aria-label="Torna al richiamo ' + str(i) + ' della nota ' + number + '">↩' + (str(i) if NOTE_REFS.get(number,0)>1 else '') + '</a>' for i in range(1,NOTE_REFS.get(number,0)+1))
        note_items.append('<li id="nota-' + number + '">' + inline(note) + ' ' + backlinks + '</li>')
    notes_html = '<details class="chapter-notes" aria-labelledby="titolo-note"><summary id="titolo-note">Note</summary><div role="doc-endnotes" aria-labelledby="titolo-note"><ol>' + ''.join(note_items) + '</ol></div></details>'
    attrs = metadata({'source':data['source'],'author':data['author'],'license':data['license'],'license-url':data['license_url'],'changes':'Immagine intera, nessuna modifica.'})
    cover = '<figure class="visual cover photo" ' + attrs + '><div class="image-frame"><div class="overview"><img src="' + uri(folder/'risorse'/data['cover']) + '" alt="' + escape(re.sub(r'\[\^\d+\]','',cover_caption),quote=True) + '" decoding="async"></div></div><figcaption>' + inline(cover_caption) + '</figcaption></figure>'
    template = (ROOT/'riferimenti/TEMA_DISPENSE.html').read_text(); doc = credits.Document(template); edits=[]
    for node in doc.root.descendants():
        if node.tag=='title': edits.append((node.start,node.end,'<title>' + data['title'] + ' — Stringhe</title>'))
        elif node.tag=='meta' and node.attrs.get('name') in {'version','date','description'}:
            name=node.attrs['name']; val={'version':edition['version'],'date':edition['date'],'description':data['description']}[name]
            edits.append((node.start,node.end,'<meta name="' + name + '" content="' + escape(val,quote=True) + '">'))
        elif node.tag=='figure' and node.has_class('cover'): edits.append((node.start,node.end,cover))
        elif node.tag=='article' and node.has_class('article'):
            bottom=next(n for n in node.descendants('nav') if n.has_class('bottom-links'))
            edits.append((node.start,node.end,'<article class="article">' + '\n'.join(body) + doc.html(bottom) + '</article>'))
        elif node.tag=='details' and node.has_class('chapter-notes'): edits.append((node.start,node.end,notes_html))
        elif node.tag=='header' and node.has_class('topbar'):
            index=next(n for n in node.descendants('details') if n.has_class('reader-index'))
            markup=doc.html(index).replace('Titolo del capitolo',data['title']).replace('<span class="sidebar-label">Fisica</span>','<span class="sidebar-label">' + AREA + '</span>')
            nav='<nav class="sidebar-nav" aria-label="Sezioni del capitolo"><ol>' + ''.join('<li class="level-2"><a href="#' + sid + '"><span>' + escape(title) + '</span></a></li>' for sid,title in headings) + '</ol></nav>'
            markup=re.sub(r'<nav class="sidebar-nav"[\s\S]*?</nav>',lambda _:nav,markup)
            edits.append((node.start,node.end,navigation_header('chapter',data['name'],markup)))
        elif node.tag=='footer' and node.has_class('footer'): edits.append((node.start,node.end,'<footer class="footer">Versione ' + edition['version'] + ' — ' + footer_date + '</footer>'))
    for start,end,value in sorted(edits,reverse=True): template=template[:start]+value+template[end:]
    template=template.replace('Nome dell’area tematica',AREA).replace('Titolo del capitolo',data['title'])
    template=re.sub(r'<!-- MODELLO CANONICO[\s\S]*?-->','<!-- Capitolo Stringhe: modello v24. -->',template,count=1)
    template=template.replace('</head>',EXTRA + '<style data-measurement-style>' + (WORK/'simulazione.css').read_text() + '</style></head>',1)
    previous=('cifre_significative_it.html','Le cifre significative') if data['mode']=='explore' else ('strumenti_misura_it.html','Gli strumenti di misura')
    links='<a rel="prev" href="' + previous[0] + '" data-site-path="' + previous[0] + '"><span>← Capitolo precedente</span><small>' + previous[1] + '</small></a>'
    if data['mode']=='explore': links+='<a rel="next" href="errori_incertezza_misura_it.html" data-site-path="errori_incertezza_misura_it.html"><span>Capitolo successivo →</span><small>Errori e incertezza di misura</small></a>'
    if data['mode']=='lab': links+='<a rel="next" href="termodinamica_sistemi_it.html" data-site-path="termodinamica_sistemi_it.html"><span>Capitolo successivo →</span><small>La termodinamica e i sistemi termodinamici</small></a>'
    template=template.replace('<!-- chapter-navigation:end -->','<nav class="chapter-navigation" aria-label="Navigazione tra capitoli">' + links + '</nav><!-- chapter-navigation:end -->',1)
    template=template.replace('</body>','<script data-measurement-script>' + (WORK/'simulazione.js').read_text() + '</script></body>',1)
    from media_controls import apply_media_controls
    return apply_media_controls(template), {'formulas':formulas,'headings':len(headings),'missing_images':sorted(set(missing)), 'version':edition['version']}


def main():
    registry=credits.load_registry(); reports={}
    # Fonti scientifiche ancora pertinenti, accessibili dal componente crediti.
    for identity,description,source,notice in [
        ('metrologia-vim-gum','Vocabolario metrologico e guida all’incertezza','https://www.bipm.org/en/committees/jc/jcgm/publications','Riferimenti terminologici: JCGM 200:2012 (VIM), JCGM 100:2008 (GUM). La regola scolastica max(semidispersione, passo) è una semplificazione dichiarata, non una procedura generale attribuita a questi documenti.'),
        ('grafico-misure-tempi','Linea dei numeri delle cinque letture illustrative',None,'Grafico quantitativo del progetto Stringhe, ricostruito dagli stessi dati illustrativi del sorgente storico; nessuna fotografia esterna riprodotta.'),
        ('parallasse-schema-originale','Schema originale del parallasse',None,'Schema originale realizzato su richiesta: scala, linee di vista e scritte costruiti in SVG con geometria verificata; elementi dell’occhio e della matita generati con ChatGPT. L’immagine commerciale Vecteezy non è riprodotta o incorporata.'),
        ('bersagli-precisione-accuratezza','Confronto di precisione e accuratezza',None,'Schema originale SVG ricreato su richiesta a partire dal confronto concettuale indicato dall’utente: https://www.ossila.com/cdn/shop/files/Syringe_Pump_Accuracy_and_Precision_Potentiostat_Specifications.svg. Geometria e punti costruiti nel progetto Stringhe; nessun elemento del file Ossila incorporato. Etichette italiane.'),
        ('bilancia-pesetti-generati','Bilancia digitale e pesetti delle simulazioni',None,'Immagini della bilancia e del pesetto generate con ChatGPT su richiesta dell’utente. Originali preservati. Il pesetto è riutilizzato con dimensioni di presentazione differenti; masse e letture sono assegnate dal modello interattivo, senza simulare fotografie di esperimenti effettuati.')]:
        if not any(r['id']==identity for r in registry['resources']): registry['resources'].append({'id':identity,'description':description,'source':source,'author':'Stringhe' if source is None else 'JCGM/BIPM','license':None,'license_url':None,'changes':None,'status':'documented','links':[],'notices':[notice],'metadata_sources':[],'fingerprints':[]})
        elif identity=='parallasse-schema-originale':
            next(r for r in registry['resources'] if r['id']==identity)['notices']=[notice]
    for key,data in CHAPTERS.items():
        source,report=render(key,data); reports[key]=report
        (ROOT/data['name']).write_text(source)
        registry['documents'][data['name']]={'title':data['title'],'anchor':data['name'][:-5].replace('_','-'),'credits':[{'resource':'metrologia-vim-gum','notice':0}],'lexend':True,'chapter_labels':True,'review':None}
    credits.sync_inventory(registry)
    for key,data in CHAPTERS.items():
        target=ROOT/data['name']; target.write_text(credits.update_component(target.read_text(),registry,data['name']))
        (ROOT/'lavorazione'/key/'bozza.html').write_bytes(target.read_bytes())
        reports[key]['bytes']=target.stat().st_size
        (ROOT/'lavorazione'/key/'verifiche-strutturali.json').write_text(json.dumps(reports[key],ensure_ascii=False,indent=2)+'\n')
    credits.REGISTRY.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    published=set(json.loads((ROOT/'pubblicazione.json').read_text())['articoli'])
    if all(data['name'] in published for data in CHAPTERS.values()):
        (ROOT/'crediti.html').write_text(credits.render_page(registry))
    else:
        assert (ROOT/'crediti.html').read_text()==credits.render_page(registry), 'La pagina pubblica dei crediti deve restare invariata'
    print(json.dumps(reports,ensure_ascii=False,indent=2))


if __name__=='__main__': main()
