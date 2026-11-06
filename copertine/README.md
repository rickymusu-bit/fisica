# Copertine della home

Versione: 1.1.0. Aggiornamento: 2026-11-06T20:38:00+01:00.

La selezione attiva della home contiene 17 fotografie orizzontali. Tre fotografie verticali della raccolta iniziale sono state escluse dalla rotazione: computer quantistico IQM, stambecchi sulla diga del Cingino e Advanced Test Reactor. Le rispettive immagini WebP restano nel repository e il registro dei crediti conserva fonti, attribuzioni e licenze. `manifest.json` conserva file, titoli, descrizioni accessibili e il rinvio `credit_id` al registro unico `../risorse/crediti.json`, che contiene attribuzioni, licenze e provenienze. Le immagini WebP sono copie ridimensionate senza ritagli; i collegamenti agli originali e le impronte SHA-256 dei file recuperati restano nel manifest. Ogni copia mantiene la licenza indicata nella propria scheda.

A ogni caricamento della home viene scelta una voce con uguale probabilità. Viene caricata soltanto quella fotografia; testo alternativo, didascalia e indicazione dei crediti si aggiornano insieme. Una scelta può ripetersi in due visite consecutive. Senza JavaScript viene mostrata la prima immagine. Se un file non si carica, vengono provate le voci successive.

Per aggiungere una copertina, scegliere una fotografia orizzontale (larghezza almeno pari all’altezza), salvare qui la copia WebP e inserire la relativa voce completa nel manifest. Eseguire `python scripts/build_pages.py`: la build genera la home con dati, copertina iniziale e crediti aggiornati, e copia soltanto le immagini elencate nell’artefatto `_site/`. Per allineare anche l’anteprima del sorgente `index.html`, usare `render_covers` da `scripts/home_covers.py`. Gli originali indicati nei link non vengono alterati.

Stringhe rende le attribuzioni disponibili dal comando «Crediti e licenze», che apre gli avvisi incorporati e rimanda alla pagina generale. Non servono richieste a Wikimedia o Flickr durante la visita. Il cambio è effettuato soltanto all’apertura della pagina; non c’è uno slideshow.
