"""Pagina di revisione dei tre video, esclusa dal deployment ufficiale."""
from pathlib import Path
from html import escape
from strings_site import shell
from youtube_videos import player

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'lavorazione/sito/video_youtube'

def main():
    entries=[('Powers of Ten','https://www.youtube.com/watch?v=0fKBhvDjuy0','potenze_dieci_notazione_scientifica_it.html#vid-01','potenze_dieci_notazione_scientifica-1'),
             ('A Boy and His Atom','https://www.youtube.com/watch?v=oSCX78-8-q0','potenze_dieci_notazione_scientifica_it.html#vid-02','potenze_dieci_notazione_scientifica-2'),
             ('Conduzione del calore nei metalli','https://youtu.be/Sdpcjm2vmLY?is=jQY0_qg6RCA-Pd_9','conduzione_it.html#video-barrette','conduzione-1')]
    body='<section class="service-card"><h1>Video su richiesta</h1><p>Il lettore si carica dopo il clic su «Carica il video». «Apri su YouTube» resta sempre disponibile. Il video richiede Internet.</p></section>'
    for title,url,chapter,stem in entries:
        body+='<section class="service-card"><h2>'+escape(title)+'</h2>'+player(url,title)+'<p><a href="'+chapter+'">Apri nel capitolo</a></p>'
        body+='<details><summary>Schermate su telefono e desktop</summary>'
        for width,label in [(390,'Telefono'),(1440,'Desktop')]:
            body+='<figure><img style="max-width:100%;height:auto" src="lavorazione/sito/video_youtube/'+stem+'-'+str(width)+'.png" alt="'+label+': riquadro '+escape(title,quote=True)+' prima del caricamento"><figcaption>'+label+'</figcaption></figure>'
        body+='</details></section>'
    body+='<section class="service-card"><h2>Documenti storici aggiornati</h2><p>Questi sorgenti conservano il loro stato di esclusione dal sito pubblico.</p><ul>'
    for filename,label in [('potenza_termica_conduzione_convezione_it.html','Potenza termica, conduzione e convezione'),('sistema_internazionale_notazione_it.html','SI e notazione, originale italiano'),('sistema_internazionale_notazione_fr.html','SI e notazione, originale francese'),('sistema_internazionale_notazione_sq.html','SI e notazione, originale albanese')]:
        body+='<li><a href="'+filename+'">'+label+'</a></li>'
    body+='</ul></section>'
    html=shell('Video su richiesta',body,(ROOT/'index.html').read_text(),service=True)
    html=html.replace('<head>','<head><base href="../../../">',1)
    WORK.mkdir(parents=True,exist_ok=True);(WORK/'index.html').write_text(html)
    print('Anteprima:',WORK/'index.html')

if __name__=='__main__':main()
