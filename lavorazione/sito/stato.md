# Stato — Home e GitHub Pages

Aggiornamento: 17/10/2026 18:46 (Europe/Rome).

## Risultato corrente

Home `index.html` v3: «Praticamente la Fisica», sottotitolo «Guida essenziale a tutto ciò che ci circonda». Tema Mac approvato, Lexend incorporato, terminologia «articoli» e «argomenti». Nessuna occorrenza del nome o cognome dell’utente nei testi o nei metadati della home. Catalogo, ancore e otto coppie lettura/download conservati.

L’utente ha fornito e scelto venti immagini per sostituire la singola copertina. Ultima istruzione: «va bene. basta cosi aggiorna la home». Questa richiesta segue le anteprime e la discussione sui crediti e autorizza l’aggiornamento della home sul sito Pages esistente. Nessuna nuova immagine cercata o generata autonomamente; il vecchio file Super-Kamiokande non fa parte della nuova rotazione.

A ogni caricamento la home sceglie una delle venti copertine con uguale probabilità; sono possibili ripetizioni tra visite. Carica solo la foto scelta e aggiorna insieme titolo, testo alternativo, didascalia e riferimento ai crediti. Nessuno slideshow o tracciamento. Senza JavaScript viene mostrata la prima immagine; se un file non si carica viene provata la voce successiva.

## Sorgenti e diritti

Cartella `copertine/`: venti WebP ottimizzate, senza ritagli, e `manifest.json` come fonte per file, titoli, dimensioni, descrizioni, autore, licenza, fonte e modifiche. Collegamenti agli originali e hash dei file recuperati conservati nel manifest; fonti originali non alterate. Licenze rilevate dalle schede Wikimedia Commons, compresa la copia verificata della foto Flickr dell’Advanced Test Reactor. Per il cambio Porsche, autore e successiva modifica della luminosità sono ricavati dalla cronologia del file, dato il metadato automatico mancante. Attribuzione NOIRLab aggiunta alla foto del fondo cosmico. Licenza di ogni immagine collegata nei crediti e conservata sulla copia WebP. La vecchia necessità di autorizzazione per Super-Kamiokande non riguarda questa selezione sostitutiva.

I crediti di tutte le venti immagini sono disponibili in una sezione HTML nativa apribile e la foto corrente viene indicata anche nel testo e nella lista. Non si contattano servizi esterni per mostrare foto, font o crediti. Le versioni WebP pesano complessivamente circa 4,12 MB; la home è circa 284 KB.

## Build e verifiche

`scripts/home_covers.py` valida il manifest e genera copertina iniziale, dati e crediti. `scripts/build_pages.py` conserva la pubblicazione selettiva degli otto articoli italiani e prepara nove HTML, venti copertine, manifest e `.nojekyll`; le fonti e le licenze esterne sono ammesse, mentre i collegamenti di lettura/download devono restare locali. Nessuna modifica agli articoli, alle traduzioni, al quiz o alle impostazioni di hosting.

Verifiche in `verifiche-home.json`: tutte e venti le immagini provate in Chromium con scelta controllata, caricamento riuscito, corrispondenza di alt/titolo/didascalia/crediti e una sola richiesta immagine per visita. Controllati 320, 390, 768, 1024 e 1440 px: nessuno scorrimento laterale, salto da tastiera, crediti apribili, foto mostrate intere con proporzioni conservate. Prova touch a 390 px senza JavaScript e recupero dopo errore della prima immagine superati. Corretto il comportamento di `noscript` durante l’ispezione visiva e ripetuti i controlli di layout. Build completa superata; artefatto privo di file estranei. Nessuna dipendenza esterna durante il caricamento della home.

## Salvataggio e pubblicazione

Ramo `tema/home-mac`, PR #15, derivato da main. Fase: realizzazione conclusa e verificata. Pubblicazione affidata al workflow Pages esistente dopo l’integrazione in main; il relativo esito è consultabile nelle Actions del repository. La cronologia dettagliata delle precedenti home e degli stati resta in Git.
