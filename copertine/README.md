# Copertine della home

La raccolta contiene le venti fotografie e immagini scelte dall’utente. `manifest.json` conserva file, titoli, descrizioni accessibili e il rinvio `credit_id` al registro unico `../risorse/crediti.json`, che contiene attribuzioni, licenze e provenienze. Le immagini WebP sono copie ridimensionate senza ritagli; i collegamenti agli originali e le impronte SHA-256 dei file recuperati restano nel manifest. Ogni copia mantiene la licenza indicata nella propria scheda.

A ogni caricamento della home viene scelta una voce con uguale probabilità. Viene caricata soltanto quella fotografia; testo alternativo, didascalia e indicazione dei crediti si aggiornano insieme. Una scelta può ripetersi in due visite consecutive. Senza JavaScript viene mostrata la prima immagine. Se un file non si carica, vengono provate le voci successive.

Per aggiungere una copertina, salvare qui la copia WebP e inserire la relativa voce completa nel manifest. Eseguire `python scripts/build_pages.py`: la build genera la home con dati, copertina iniziale e crediti aggiornati, e copia soltanto le immagini elencate nell’artefatto `_site/`. Per allineare anche l’anteprima del sorgente `index.html`, usare `render_covers` da `scripts/home_covers.py`. Gli originali indicati nei link non vengono alterati.

Stringhe rende le attribuzioni disponibili dal comando «Crediti e licenze», che apre gli avvisi incorporati e rimanda alla pagina generale. Non servono richieste a Wikimedia o Flickr durante la visita. Il cambio è effettuato soltanto all’apertura della pagina; non c’è uno slideshow.
