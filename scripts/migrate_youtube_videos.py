"""Audit di tutti i capitoli; migrazione circoscritta ai video già presenti.

Non modifica il manifest né gli HTML privi di video. Le copie correnti di
lavorazione sono riallineate solo se esistono; gli originali storici restano.
"""
from pathlib import Path
from html import escape
import hashlib
import json
import re
import argparse
import subprocess
from credits import Document
from youtube_videos import apply_youtube_videos, video_info

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'lavorazione/sito/video_youtube'
COPIES={
 'conduzione_it.html':'lavorazione/conduzione/bozza.html',
 'potenze_dieci_notazione_scientifica_it.html':'lavorazione/potenze_dieci_notazione_scientifica/bozza.html',
}

def versioned(source):
    document=Document(source)
    meta=next((n for n in document.root.descendants('meta') if n.attrs.get('name')=='version'),None)
    footer=next(document.root.descendants('footer'),None)
    match=re.search(r'\bv(\d+)\b',document.html(meta) if meta else document.html(footer) if footer else '')
    if not match: return source
    previous='v'+match[1];current='v'+str(int(match[1])+1)
    edits=[]
    for node in [meta,footer]:
        if node: edits.append((node.start,node.end,document.html(node).replace(previous,current)))
    for start,end,value in sorted(edits,reverse=True):source=source[:start]+value+source[end:]
    return source

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
    publication=json.loads((ROOT/'pubblicazione.json').read_text())
    report={'scope':'Tutti i capitoli HTML alla radice, compresi sorgenti esclusi e traduzioni; nessuna pubblicazione.',
            'base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(), 'documents':[]}
    failures=[]
    for path in sorted(ROOT.glob('*.html')):
        if path.name in {'index.html','crediti.html','articoli.html','quiz.html'}: continue
        source=path.read_text(encoding='utf-8-sig');document=Document(source)
        links=[n.attrs['href'] for n in document.root.descendants('a') if video_info(n.attrs.get('href',''))]
        migrated=apply_youtube_videos(source)
        status='publicable' if path.name in publication['articoli'] else 'non pubblicato'
        baseline=subprocess.check_output(['git','show','HEAD:'+path.name],cwd=ROOT,text=True)
        original_links=[n.attrs['href'] for n in Document(baseline).root.descendants('a') if video_info(n.attrs.get('href',''))]
        if links!=original_links: raise ValueError('URL originali alterati: '+path.name)
        row={'file':path.name,'publication':status,'video_urls':links,'players':migrated.count('data-youtube-video='),
             'changed_since_base':baseline!=migrated,'original_urls_preserved':links==original_links,
             'before_sha256':hashlib.sha256(baseline.encode()).hexdigest(),'after_sha256':hashlib.sha256(migrated.encode()).hexdigest(),
             'html_video_tags':len(list(document.root.descendants('video'))),
             'remote_iframes':[n.attrs.get('src') for n in document.root.descendants('iframe') if n.attrs.get('src','').startswith(('http:','https:'))]}
        if migrated!=source:
            if args.check: failures.append(path.name)
            else:
                # Il nuovo capitolo è rigenerato dal proprio generatore con versione corrente.
                if 'data-youtube-video=' not in source: migrated=versioned(migrated)
                path.write_text(migrated)
        if path.name in COPIES and (ROOT/COPIES[path.name]).exists():
            if args.check and (ROOT/COPIES[path.name]).read_bytes()!=path.read_bytes(): failures.append(COPIES[path.name])
            elif not args.check:(ROOT/COPIES[path.name]).write_bytes(path.read_bytes())
        report['documents'].append(row)
    if failures: raise ValueError('Componenti video da aggiornare: '+', '.join(failures))
    if not args.check:
        WORK.mkdir(parents=True,exist_ok=True)
        (WORK/'inventario.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(f"Controllati {len(report['documents'])} documenti; {sum(bool(d['video_urls']) for d in report['documents'])} con video YouTube.")

if __name__=='__main__':main()
