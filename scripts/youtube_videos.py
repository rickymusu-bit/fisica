"""Componente YouTube comune: iframe creato al clic, URL originali conservati."""
from html import escape
import re
from urllib.parse import urlsplit, parse_qs
from pathlib import Path
from credits import Document, text

ROOT = Path(__file__).resolve().parents[1]
LABELS = {
 'it': ('Carica il video', 'Apri su YouTube', 'Chiudi il lettore',
        'Il video richiede Internet. YouTube si carica solo dopo il clic.',
        'Sei offline. Collegati a Internet per caricare il video.',
        'Se il video non si apre, usa «Apri su YouTube». Il servizio può mostrare pubblicità e suggerimenti.'),
 'fr': ('Charger la vidéo', 'Ouvrir sur YouTube', 'Fermer le lecteur',
        'Une connexion Internet est nécessaire. YouTube se charge uniquement après le clic.',
        'Vous êtes hors ligne. Connectez-vous à Internet pour charger la vidéo.',
        'Si la vidéo ne s’ouvre pas, utilisez « Ouvrir sur YouTube ». Le service peut afficher des publicités et des suggestions.'),
 'sq': ('Ngarko videon', 'Hap në YouTube', 'Mbyll lexuesin',
        'Videoja kërkon internet. YouTube ngarkohet vetëm pas klikimit.',
        'Je jashtë linje. Lidhu me internetin për të ngarkuar videon.',
        'Nëse videoja nuk hapet, përdor «Hap në YouTube». Shërbimi mund të shfaqë reklama dhe sugjerime.'),
}

def video_info(url):
    parsed = urlsplit(url)
    if parsed.scheme not in {'http', 'https'}: return None
    host = (parsed.hostname or '').lower()
    query = parse_qs(parsed.query)
    if host in {'youtu.be', 'www.youtu.be'}:
        identity = parsed.path.strip('/').split('/')[0]
    elif host in {'youtube.com', 'www.youtube.com', 'm.youtube.com', 'youtube-nocookie.com', 'www.youtube-nocookie.com'}:
        if parsed.path == '/watch': identity = query.get('v', [''])[0]
        elif re.match(r'^/(embed|shorts|live)/', parsed.path): identity = parsed.path.split('/')[2]
        else: return None
    else: return None
    if not re.fullmatch(r'[A-Za-z0-9_-]{11}', identity): return None
    time = query.get('start', query.get('t', parse_qs(parsed.fragment).get('t', ['0'])))[0]
    if re.fullmatch(r'\d+', time): start = int(time)
    elif re.fullmatch(r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?', time) and time:
        h,m,s=re.fullmatch(r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?',time).groups()
        start=int(h or 0)*3600+int(m or 0)*60+int(s or 0)
    else: start=0
    return identity, start

def player(url, title, lang='it'):
    info = video_info(url)
    if not info: raise ValueError('URL YouTube non riconosciuto: '+url)
    identity, start = info
    load, external, close, initial, offline, loaded = LABELS.get(lang, LABELS['it'])
    e=lambda value:escape(str(value),quote=True)
    return (f'<div class="youtube-player" data-youtube-video="{identity}" data-youtube-start="{start}" '
            f'data-youtube-title="{e(title)}" data-youtube-offline="{e(offline)}" data-youtube-loaded="{e(loaded)}">'
            '<div class="youtube-stage">'
            f'<button class="youtube-load" type="button" data-youtube-load hidden aria-label="{e(load+": "+title)}">'
            '<span class="youtube-play" aria-hidden="true">▶</span>'
            f'<span class="youtube-name">{e(title)}</span><span class="youtube-load-label">{e(load)}</span></button>'
            f'<noscript><p class="youtube-name">{e(title)}</p></noscript></div>'
            f'<a class="youtube-fallback" href="{e(url)}" target="_blank" rel="noopener">{e(external)}</a>'
            f'<button class="youtube-stop" data-youtube-stop type="button" hidden>{e(close)}</button>'
            f'<p class="youtube-notice" data-youtube-notice role="status">{e(initial)}</p></div>')

def apply_youtube_videos(source, include_assets=False):
    document=Document(source)
    html=next(document.root.descendants('html'),None)
    lang=html.attrs.get('lang','it').split('-')[0] if html else 'it'
    edits=[]
    for node in document.root.descendants('a'):
        url=node.attrs.get('href','')
        if not video_info(url) or node.has_class('youtube-fallback'): continue
        # Non toccare citazioni, crediti o collegamenti testuali nel corpo.
        if not node.has_class('video-thumb') and not list(node.descendants('img')): continue
        identity=video_info(url)[0]
        title={'0fKBhvDjuy0':'Powers of Ten', 'oSCX78-8-q0':'A Boy and His Atom',
               'Sdpcjm2vmLY':{'it':'Conduzione del calore nei metalli','fr':'Conduction de la chaleur dans les métaux','sq':'Përcjellja e nxehtësisë në metale'}.get(lang,'Conduzione del calore nei metalli')}.get(identity)
        if not title:
            title=node.attrs.get('aria-label') or text(document.html(node)) or 'Video YouTube'
        edits.append((node.start,node.end,player(url,title,lang)))
    for start,end,value in sorted(edits,reverse=True): source=source[:start]+value+source[end:]
    # Eliminare soltanto istruzioni storiche sul vecchio comando, non le didascalie scientifiche.
    for old,new in {
      'Il video si apre su YouTube.':'',
      "La vidéo s’ouvre sur YouTube.":'', "La vidéo s'ouvre sur YouTube.":'',
      'Videoja hapet në YouTube.':'',
      'Video dell’esperimento: scegli la miniatura per aprirlo sulla piattaforma originale.':'Osserva i diversi tempi di fusione della cera alle estremità delle barrette.'
    }.items(): source=source.replace(old,new)
    has_player='data-youtube-video=' in source
    if has_player or include_assets:
        for tag in ['style','script']:
            source=re.sub(rf'<{tag} data-youtube-ui>[\s\S]*?</{tag}>','',source)
        style=(ROOT/'identita/youtube-videos.css').read_text()
        script=(ROOT/'identita/youtube-videos.js').read_text()
        source=source.replace('</head>','<style data-youtube-ui>'+style+'</style></head>',1)
        source=source.replace('</body>','<script data-youtube-ui>'+script+'</script></body>',1)
    return source
