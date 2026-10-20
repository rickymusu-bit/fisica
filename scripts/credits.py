"""Archivio unico, inventario automatico e rendering statico dei crediti (stdlib).

python3 scripts/credits.py --sync   registra nuove risorse e aggiorna gli snapshot
python3 scripts/credits.py --check  controlla registro, pagina e copie autonome
"""
from __future__ import annotations

import argparse
import base64
import hashlib
from html import escape, unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'risorse/crediti.json'
PUBLIC_URL = 'https://rickymusu-bit.github.io/fisica/crediti.html'
START = '<!-- resource-credits:start -->'
END = '<!-- resource-credits:end -->'


class Node:
    def __init__(self, tag, attrs, start, parent=None):
        self.tag, self.attrs, self.start = tag, dict(attrs), start
        self.end, self.parent, self.children = start, parent, []

    def has_class(self, name):
        return name in self.attrs.get('class', '').split()

    def descendants(self, tag=None):
        for child in self.children:
            if tag is None or child.tag == tag:
                yield child
            yield from child.descendants(tag)


class Document(HTMLParser):
    """Intervalli sul sorgente: nessuna riserializzazione dei contenuti scientifici."""
    VOID = set('area base br col embed hr img input link meta param source track wbr'.split())

    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.offsets = [0]
        self.offsets.extend(m.end() for m in re.finditer('\n', source))
        self.root = Node('document', [], 0)
        self.stack = [self.root]
        self.feed(source)
        self.root.end = len(source)

    def position(self):
        line, column = self.getpos()
        return self.offsets[line - 1] + column

    def handle_starttag(self, tag, attrs):
        pos = self.position()
        node = Node(tag, attrs, pos, self.stack[-1])
        self.stack[-1].children.append(node)
        node.end = pos + len(self.get_starttag_text())
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack[i].end = self.source.find('>', self.position()) + 1
                del self.stack[i:]
                break

    def html(self, node):
        return self.source[node.start:node.end]


def text(html):
    return unescape(re.sub('<[^>]*>', '', html)).strip()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def load_registry():
    return json.loads(REGISTRY.read_text(encoding='utf-8'))


def articles():
    # Comprende gli HTML storici e tradotti; non cambia l'ammissione a Pages.
    return sorted(p for p in ROOT.glob('*.html')
                  if p.name not in {'index.html', 'crediti.html',
                                    'stati_della_materia_e_passaggi_di_stato.html'})


def original_source(source):
    return re.sub(re.escape(START) + r'[\s\S]*?' + re.escape(END), '', source)


def inventory(source):
    """Rileva immagini, poster, font, SVG, canvas e iframe senza modificarli."""
    source = original_source(source)
    doc = Document(source)
    found = []
    for node in doc.root.descendants():
        # Le icone dei comandi sono codice del tema, non figure del capitolo.
        # Non devono ereditare autore/licenza della fotografia che controllano.
        if node.tag == 'svg' and 'data-ui-icon' in node.attrs:
            continue
        values = [(key, node.attrs[key]) for key in
                  ('src', 'poster', 'data-still', 'srcset', 'href', 'xlink:href')
                  if node.attrs.get(key) and (key not in ('href', 'xlink:href') or node.tag == 'image')]
        if node.tag == 'iframe' and node.attrs.get('srcdoc'):
            found.extend(inventory(node.attrs['srcdoc']))
        if node.tag in ('svg', 'canvas'):
            values.append(('inline', doc.html(node)))
        for key, value in values:
            if node.tag == 'script':
                continue
            if value.startswith('data:'):
                header, payload = value.split(',', 1)
                raw = base64.b64decode(payload) if ';base64' in header else unquote(payload).encode()
                kind = header[5:].split(';')[0]
                location = None
            elif key == 'inline':
                raw, kind, location = value.encode(), node.tag, None
            else:
                raw, kind, location = value.encode(), node.tag, value
            metadata = {}
            owner = node
            while owner:
                for field in ('source', 'author', 'license', 'license-url', 'changes', 'id'):
                    if owner.attrs.get('data-credit-' + field):
                        metadata.setdefault(field, owner.attrs['data-credit-' + field])
                owner = owner.parent
            ancestor = node
            while ancestor.parent and not ancestor.attrs.get('id'):
                ancestor = ancestor.parent
            found.append({'id': 'asset-' + digest(raw), 'kind': kind,
                          'description': node.attrs.get('alt') or node.attrs.get('aria-label') or node.tag,
                          'locator': ancestor.attrs.get('id'), 'attribute': key,
                          'location': location,
                          'credit_id': metadata.get('id'), 'metadata': metadata})
    for match in re.finditer(r'url\([\s\'\"]*(data:font/[^)\s\'\"]+)', source):
        value = match[1]
        header, payload = value.split(',', 1)
        raw = base64.b64decode(payload) if ';base64' in header else unquote(payload).encode()
        found.append({'id': 'asset-' + digest(raw), 'kind': header[5:].split(';')[0],
                      'description': 'Font incorporato', 'locator': None,
                      'attribute': 'font-face', 'location': None, 'credit_id': 'font-lexend', 'metadata': {}})
    return found


def sync_inventory(registry):
    previous = {a['id']: a for a in registry.get('assets', [])}
    assets = {}
    resources = {r['id']: r for r in registry['resources']}
    fingerprints = {fingerprint: r['id'] for r in registry['resources']
                    for fingerprint in r.get('fingerprints', [])}
    paths = articles() + [ROOT / 'index.html', ROOT / 'riferimenti/TEMA_DISPENSE.html']
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        source = path.read_text(encoding='utf-8')
        if relative not in registry['documents']:
            title = re.search(r'<title>([\s\S]*?)</title>', source, re.I)
            registry['documents'][relative] = {'title': text(title[1]) if title else path.stem,
                                             'credits': [], 'review': 'Nuovo documento da verificare'}
        registry['documents'][relative].setdefault('anchor', path.stem.replace('_', '-'))
        registry['documents'][relative]['lexend'] = '@font-face' in source and 'Lexend' in source
        occurrences = inventory(source)
        if relative == 'index.html':
            for cover in json.loads((ROOT / 'copertine/manifest.json').read_text()):
                occurrences.append({'id': 'asset-' + digest((ROOT / cover['src']).read_bytes()),
                                    'kind': 'image/webp', 'description': cover['alt'],
                                    'locator': 'cover-image', 'attribute': 'cover-data',
                                    'location': cover['src'], 'credit_id': None, 'metadata': {}})
        for occurrence in occurrences:
            identity = occurrence.pop('id')
            metadata = occurrence.pop('metadata', {})
            if metadata.get('source') and not occurrence['credit_id']:
                resource = next((r for r in registry['resources'] if r.get('source') == metadata['source']), None)
                if resource is None:
                    resource = {'id': 'credit-' + digest(metadata['source'].encode())[:16],
                                'description': occurrence['description'], 'source': metadata['source'],
                                'author': metadata.get('author'), 'license': metadata.get('license'),
                                'license_url': metadata.get('license-url'), 'changes': metadata.get('changes'),
                                'status': 'documented' if metadata.get('license-url') and metadata.get('author') else 'review',
                                'links': [], 'notices': [], 'metadata_sources': [relative], 'fingerprints': []}
                    registry['resources'].append(resource)
                    resources[resource['id']] = resource
                    notice = escape(occurrence['description']) + ' — ' + escape(resource['author'] or 'Autore non documentato')
                    notice += f'. <a href="{escape(resource["source"], quote=True)}">Fonte originale</a>.'
                    if resource['license_url']:
                        notice += f' <a href="{escape(resource["license_url"], quote=True)}">{escape(resource["license"] or "Licenza")}</a>.'
                    else:
                        notice += ' Licenza non documentata.'
                    if resource['changes']:
                        notice += ' Modifiche: ' + escape(resource['changes'])
                    resource['notices'].append(notice)
                occurrence['credit_id'] = resource['id']
            occurrence['credit_id'] = occurrence['credit_id'] or fingerprints.get(identity)
            notice_index = 0
            if occurrence['credit_id'] and occurrence['credit_id'] != 'font-lexend':
                resource = resources[occurrence['credit_id']]
                if metadata.get('changes') and metadata['changes'] != resource.get('changes'):
                    variant = (resource['notices'][0] + '<br>Modifiche per questo utilizzo: ' +
                               escape(metadata['changes']))
                    if variant not in resource['notices']:
                        resource['notices'].append(variant)
                    notice_index = resource['notices'].index(variant)
                if identity not in resource.setdefault('fingerprints', []):
                    resource['fingerprints'].append(identity)
                association = {'resource': resource['id'], 'notice': notice_index}
                if (notice_index and association not in registry['documents'][relative]['credits']) or not any(a['resource'] == resource['id'] for a in registry['documents'][relative]['credits']):
                    registry['documents'][relative]['credits'].append(association)
            if identity not in assets:
                assets[identity] = {k: v for k, v in previous.get(identity, {}).items() if k != 'uses'}
                assets[identity].update(id=identity, kind=occurrence['kind'], uses=[])
            assets[identity]['uses'].append({'document': relative, **occurrence})
    registry['assets'] = sorted(assets.values(), key=lambda a: a['id'])
    known = {r['id'] for r in registry['resources']}
    for asset in registry['assets']:
        for use in asset['uses']:
            if use.get('credit_id') and use['credit_id'] not in known:
                raise ValueError(f"data-credit-id sconosciuto: {use['credit_id']}")
    # Gli originali storici restano nel registro; i documenti correnti citano
    # soltanto i media ancora utilizzati. Le fonti testuali senza impronte
    # restano esplicite e non vengono scambiate per immagini eliminate.
    managed = current_documents()
    for name in managed:
        if name not in registry['documents']:
            continue
        registry['documents'][name]['credits'] = active_associations(registry, name)
    return registry


def current_documents():
    publication = json.loads((ROOT / 'pubblicazione.json').read_text())
    return ['index.html'] + publication['articoli'] + ['riferimenti/TEMA_DISPENSE.html']


def active_associations(registry, document):
    resources = {r['id']: r for r in registry['resources']}
    used = {use.get('credit_id') for asset in registry['assets']
            for use in asset['uses'] if use['document'] == document}
    return [association for association in registry['documents'][document]['credits']
            if not resources[association['resource']].get('fingerprints')
            or association['resource'] in used]


def notice_html(registry, document):
    resources = {r['id']: r for r in registry['resources']}
    lines = []
    for position, association in enumerate(registry['documents'][document]['credits']):
        resource = resources[association['resource']]
        variant = resource['notices'][association['notice']]
        lines.append(f'<li id="{escape(registry["documents"][document]["anchor"])}-credito-{position}">{variant}</li>')
    if not lines:
        lines.append('<li>Non sono presenti crediti grafici nel sorgente originale. '
                     'La licenza delle risorse prive di documentazione resta da verificare.</li>')
    missing = unassociated(registry, document)
    if missing:
        lines.append('<li>Risorse senza attribuzione individuale associata: <ul>' +
                     ''.join('<li>' + escape(description) + '</li>' for description in missing) +
                     '</ul>Provenienza e diritti da verificare; nessuna licenza è dedotta.</li>')
    return re.sub(r'<a href="">([\s\S]*?)</a>', r'\1', '<ul>' + ''.join(lines) + '</ul>')


def unassociated(registry, document):
    missing = []
    for asset in registry.get('assets', []):
        for use in asset['uses']:
            if use['document'] == document and not use.get('credit_id') and asset['kind'].startswith('image/'):
                description = use['description']
                if description in ('source', 'image', 'img'):
                    description = 'Risorsa incorporata o anteprima statica senza metadati individuali'
                if description not in missing:
                    missing.append(description)
    return missing


def font_html(registry):
    return ('<h2>Carattere tipografico</h2><p>Lexend — The Lexend Project Authors. '
            '<a href="https://openfontlicense.org/open-font-license-official-text/">'
            'SIL Open Font License 1.1</a>.</p><pre>' +
            escape(registry['font_license']) + '</pre>')


def legacy_component(registry, document):
    anchor = ('font-lexend' if document == 'riferimenti/TEMA_DISPENSE.html'
              else registry['documents'][document]['anchor'])
    content = notice_html(registry, document)
    font = font_html(registry) if registry['documents'][document].get('lexend') else ''
    return (START + '''
<style data-resource-credits>
.credits-navigation{display:flex;flex-wrap:wrap;gap:12px 24px;max-width:940px;margin:20px auto;padding:0 20px;background:white;color:#080808;font:14px/1.6 Lexend,Arial,sans-serif}
.credits-navigation a{display:inline-flex;align-items:center;min-height:44px}
.resource-credits-dialog{color:#080808;background:#fff;border:3px solid #080808;padding:24px;width:min(900px,calc(100% - 24px));max-width:calc(100% - 24px);max-height:85vh;overflow:auto;font:16px/1.6 Lexend,Arial,sans-serif;overflow-wrap:anywhere}
.resource-credits-dialog::backdrop{background:rgb(0 0 0 / .5)}
.resource-credits-dialog:target:not([open]){display:block;position:relative;margin:24px auto}
.resource-credits-dialog h2{font-size:26px;margin:24px 0 16px}.resource-credits-dialog li{margin-bottom:16px}.resource-credits-dialog pre{white-space:pre-wrap;overflow-wrap:anywhere;font:12px/1.5 monospace}.resource-credits-dialog .credits-close{display:inline-block;min-height:44px}
</style>
<nav class="credits-navigation" aria-label="Crediti e licenze">''' +
            f'<a href="crediti.html#{anchor}" data-public-credits="{PUBLIC_URL}#{anchor}">Crediti e licenze</a>' +
            '<a href="#crediti-autonomi" data-offline-credits>Crediti della copia autonoma</a></nav>' +
            '<dialog class="resource-credits-dialog" id="crediti-autonomi" aria-labelledby="crediti-autonomi-title">'
            '<a class="credits-close" href="#" data-close-credits>Chiudi</a>'
            '<h2 id="crediti-autonomi-title">Crediti e licenze</h2>' +
            f'<p>{escape(registry["documents"][document]["title"])}</p>' + content +
            font + '</dialog>' + '''
<script data-resource-credits>
(() => {
 const dialog=document.getElementById('crediti-autonomi');
 const links=document.querySelectorAll('[data-offline-credits]');
 let opener;
 if(location.protocol==='file:')document.querySelectorAll('[data-public-credits]').forEach(link=>{
  link.href=link.dataset.publicCredits;
 });
 links.forEach(link=>link.addEventListener('click',event=>{
  if(typeof dialog.showModal!=='function')return;
  event.preventDefault();opener=link;dialog.showModal();
 }));
 dialog.querySelector('[data-close-credits]').addEventListener('click',event=>{
  if(!dialog.open)return;event.preventDefault();dialog.close();
 });
 dialog.addEventListener('close',()=>{if(opener)opener.focus();});
})();
</script>
''' + END)


def component(registry, document):
    block = legacy_component(registry, document)
    publication = json.loads((ROOT / 'pubblicazione.json').read_text())
    active = {'index.html', 'riferimenti/TEMA_DISPENSE.html', *publication['articoli']}
    source = (ROOT / document).read_text(encoding='utf-8')
    # Conservare i componenti storici dei documenti fuori dalla revisione.
    if document not in active and 'Crediti della copia autonoma</a>' in source:
        return block
    navigation = ('<nav class="credits-navigation" aria-label="Crediti e licenze">'
                  '<a href="#crediti-autonomi" data-offline-credits>Crediti e licenze</a></nav>')
    block = re.sub(r'<nav class="credits-navigation"[\s\S]*?</nav>', lambda _: navigation, block, count=1)
    title = '<h2 id="crediti-autonomi-title">Crediti e licenze</h2>'
    all_credits = (f'<p><a href="{PUBLIC_URL}" data-public-credits="{PUBLIC_URL}">'
                   'Crediti di tutti gli articoli</a></p>')
    if document == 'riferimenti/TEMA_DISPENSE.html' or registry['documents'][document].get('chapter_labels'):
        all_credits = all_credits.replace('tutti gli articoli', 'tutti i capitoli')
    return block.replace(title, title + all_credits, 1)


def update_component(source, registry, document):
    block = component(registry, document)
    if START in source:
        return re.sub(re.escape(START) + r'[\s\S]*?' + re.escape(END), lambda _: block, source)
    if re.search(r'<footer\b', source):
        return re.sub(r'(?=<footer\b)', lambda _: block + '\n', source, count=1)
    return source.replace('</body>', block + '\n</body>')


def render_page(registry):
    from stringhe_theme import apply_theme, theme_control
    theme = (ROOT / 'riferimenti/TEMA_DISPENSE.html').read_text(encoding='utf-8')
    styles = ''.join(re.findall(r'<style[^>]*>[\s\S]*?</style>', theme))
    publication = json.loads((ROOT / 'pubblicazione.json').read_text())
    public = ['index.html'] + publication['articoli']
    nav, sections, review = [], [], []
    resources = {r['id']: r for r in registry['resources']}
    ordered = public
    for name in ordered:
        info = registry['documents'][name]
        if name == 'riferimenti/TEMA_DISPENSE.html':
            continue
        anchor, title = info['anchor'], escape(info['title'])
        nav.append(f'<li><a href="#{anchor}">{title}</a></li>')
        article_link = (f'<p><a href="{escape(name)}">Apri il capitolo</a></p>' if name in public else
                        '<p>Documento conservato nel repository, escluso dalla pubblicazione.</p>')
        sections.append(f'<section id="{anchor}"><h2>{title}</h2>' + article_link +
                        notice_html(registry, name) + '</section>')
        for association in info['credits']:
            resource = resources[association['resource']]
            if resource['status'] == 'review':
                review.append(f'<li><a href="#{anchor}">{title}</a>: ' +
                              resource['notices'][association['notice']] + '</li>')
        if info.get('review'):
            review.append(f'<li><a href="#{anchor}">{title}</a>: {escape(info["review"])}</li>')
        missing = unassociated(registry, name)
        if missing:
            review.append(f'<li><a href="#{anchor}">{title}</a>: risorse senza metadati individuali: <ul>' +
                          ''.join('<li>' + escape(description) + '</li>' for description in missing) + '</ul></li>')
    return apply_theme('<!DOCTYPE html>\n<html lang="it"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="version" content="v4"><meta name="date" content="2026-10-20">'
            '<title>Crediti e licenze — Stringhe</title>' + styles + '''
<style>.credits-page{max-width:1100px;margin:auto;padding:40px;background:white}.credits-page h1{font-size:clamp(32px,6vw,60px);margin:24px 0}.credits-page h2{font-size:28px;margin:42px 0 22px}.credits-page li{margin:16px 0}.credits-page section{border-top:2px solid;padding-top:8px;margin-top:36px;scroll-margin-top:24px}.credits-page pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.5 monospace}.credits-page{overflow-wrap:anywhere}.credits-page nav a{display:inline-block;min-height:44px}.credits-page .page-nav{display:flex;gap:24px;flex-wrap:wrap}@media(max-width:560px){.credits-page{padding:20px}.credits-page ul{padding-left:22px}.credits-page h2{font-size:24px}}</style>
</head><body><main class="credits-page">''' + theme_control() + '''<nav class="page-nav" aria-label="Navigazione"><a href="articoli.html">← Capitoli</a><a href="#da-verificare">Licenze da verificare</a></nav><h1>Crediti e licenze</h1>
<p>Provenienza delle immagini, delle animazioni e dei caratteri usati in Stringhe. Il sito è gratuito, senza pubblicità e dedicato alla divulgazione e alla didattica. Ogni risorsa conserva i propri diritti: la gratuità non sostituisce una licenza.</p>
<p>Le attribuzioni sono conservate come documentate nei sorgenti. Dove autore, fonte, licenza o modifiche non sono indicati, l’informazione non è disponibile. Le copie autonome dei capitoli includono gli stessi avvisi e la licenza del font, accessibili dal comando «Crediti e licenze», anche senza connessione. Da ogni documento, «Crediti di tutti i capitoli» apre questa pagina generale.</p>
<nav aria-label="Indice dei crediti"><ul>''' + ''.join(nav) + '</ul></nav>' +
            ''.join(sections) + '<section id="da-verificare"><h2>Licenze e attribuzioni da verificare</h2>'
            '<p>Questi materiali richiedono una verifica dei diritti o della documentazione prima di poter considerare conclusa la verifica delle licenze. Nessuna autorizzazione è dedotta dal solo uso didattico.</p><ul>' +
            ''.join(review) + '</ul></section><section id="font-lexend">' + font_html(registry) +
            '</section><p><a href="#">Torna all’inizio</a></p></main></body></html>\n')


def validate(registry):
    ids = [r['id'] for r in registry['resources']]
    if len(ids) != len(set(ids)):
        raise ValueError('Risorsa duplicata')
    if (ROOT / 'licenze/Lexend-OFL.txt').read_text(encoding='utf-8') != registry['font_license']:
        raise ValueError('Licenza del font assente o non aggiornata: eseguire --sync')
    resources = {r['id']: r for r in registry['resources']}
    for name, info in registry['documents'].items():
        for association in info['credits']:
            resource = resources[association['resource']]
            resource['notices'][association['notice']]
        source = (ROOT / name).read_text(encoding='utf-8')
        for node in Document(source).root.descendants('details'):
            if any(node.has_class(c) for c in ('credits', 'font-license', 'image-credits')):
                raise ValueError(f'Sezione finale superflua: {name}')
        if source.count(START) != 1 or component(registry, name) not in source:
            raise ValueError(f'Crediti autonomi assenti o non aggiornati: {name}; eseguire --sync')
    fresh = sync_inventory(json.loads(json.dumps(registry)))
    if fresh['assets'] != registry['assets']:
        raise ValueError('Inventario non aggiornato: eseguire scripts/credits.py --sync')
    for name in current_documents():
        if fresh['documents'][name]['credits'] != registry['documents'][name]['credits']:
            raise ValueError(f'Crediti di immagini non più presenti: {name}; eseguire --sync')
    if (ROOT / 'crediti.html').read_text(encoding='utf-8') != render_page(registry):
        raise ValueError('Pagina crediti non aggiornata: eseguire --sync')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sync', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    registry = load_registry()
    if args.sync:
        sync_inventory(registry)
        for name, info in registry['documents'].items():
            info.setdefault('anchor', Path(name).stem.replace('_', '-'))
            path = ROOT / name
            path.write_text(update_component(path.read_text(encoding='utf-8'), registry, name), encoding='utf-8')
        REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        (ROOT / 'crediti.html').write_text(render_page(registry), encoding='utf-8')
        font = ROOT / 'licenze/Lexend-OFL.txt'
        font.parent.mkdir(exist_ok=True)
        font.write_text(registry['font_license'], encoding='utf-8')
    validate(registry)
    print(f"Crediti verificati: {len(registry['documents'])} documenti, "
          f"{len(registry['resources'])} schede, {len(registry['assets'])} risorse uniche inventariate.")


if __name__ == '__main__':
    main()
