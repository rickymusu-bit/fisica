# Stato — Home e GitHub Pages

Aggiornamento: 17/10/2026 19:39 (Europe/Rome).

## Revisione corrente — home italiana v5

Richiesta esplicita: rimuovere Indice in alto a sinistra, mostrare il catalogo soltanto dopo «Esplora gli articoli», sostituire «Scarica HTML» con un’icona e dichiarare il peso effettivo. L’utente ha precisato di lavorare soltanto sull’italiano. Master consultato: v52; modifica locale eseguita direttamente secondo B2, preservando template, copertine e articoli.

Implementazione in `scripts/home_italian.py`, applicata soltanto all’output italiano da `scripts/build_pages.py`. `index.html` resta il template condiviso: questo evita modifiche alle altre home generate. La home italiana pubblicabile dichiara v5. Menu lingua a destra; catalogo nascosto all’arrivo senza ancora, apertura al clic con focus e aria-expanded; supporto alle ancore `#indice` e degli argomenti dai collegamenti già pubblicati. Senza JavaScript il catalogo resta accessibile. Dimensioni da stat dei file reali durante ogni build: kB/MB decimali visibili, byte esatti in tooltip ed etichetta accessibile. Nessuna nuova richiesta di rete dal browser.

Verifiche completate: build sui file reali (20 HTML e 20 copertine); Chromium a 320, 390, 768, 1024 e 1440 px senza overflow; catalogo inizialmente nascosto, clic ripetuto, focus, tastiera, quattro ancore dirette, fallback senza JavaScript, dimensioni di tutti e nove i download e download di un articolo confrontato byte per byte. Output francese e albanese confrontati con il generatore precedente: identici. Aggiornati README e percorso del renderer nel trigger del workflow Pages.

Fase: modifiche verificate, pronte nel ramo dedicato `home/esplora-download` per revisione e integrazione. Questa richiesta non comprende una nuova pubblicazione esplicita; main e deployment restano da aggiornare dopo revisione.

---

## Stato precedente e autorizzazioni

Home `index.html` v4: «Praticamente la Fisica», sottotitolo «Guida essenziale a tutto ciò che ci circonda», tema Mac approvato e Lexend incorporato. Nessun nome o cognome dell’utente nei testi o nei metadati della home; terminologia «articoli» e «argomenti».

Ultima richiesta esplicita: «pubblica l’irraggiamento. poi togli i titoli alle immagini della copertina della home:bastano le didascalie. sempre nella home: la barra superiore usala per l’indice e la selezione della lingua, togli le scritte ripetitive e inutili che ci sono adesso».

Irraggiamento aggiunto come nono articolo italiano, con lettura e download. Si parte dal file approvato del ramo `istruzioni/tema-mac`: contenuto conservato, meta autore rimosso e versione v4. Il precedente articolo Potenza termica usa la v7 pronta nello stesso ramo, con navigazione precedente/successivo; rispetto alla v6 di main cambiano soltanto versione, data e navigazione. [Stato dell’irraggiamento](../irraggiamento/stato.md).

## Home e lingue

Barra superiore persistente con due menu HTML nativi: Indice e lingua. Eliminati il nome del sito e l’etichetta Fisica ripetuti nella barra, l’indice separato nel catalogo e il piè di pagina ripetitivo. Con JavaScript i menu si chiudono con Esc, clic esterno o scelta della sezione; senza script restano utilizzabili tramite summary e collegamenti nativi.

Italiano, francese e albanese sono le lingue già presenti nel repository. La home italiana mostra nove articoli; `index_fr.html` e `index_sq.html`, generati durante la build, mostrano ciascuno i quattro articoli esistenti nella rispettiva lingua. `lingue/home.json` contiene interfaccia, titoli e descrizioni del catalogo e didascalie tradotte. Gli articoli tradotti non sono modificati né generati automaticamente. Il nome del sito resta Praticamente la Fisica.

## Copertine e attribuzioni

Venti copertine fornite e scelte dall’utente, conservate in `copertine/` con manifest, fonti, autori, licenze e hash dei file recuperati. Foto intere, ridimensionate e convertite in WebP senza ritagli. La copertina cambia casualmente a ogni caricamento, con uguale probabilità e possibili ripetizioni. È caricata soltanto la foto scelta; senza JavaScript compare la prima; in caso di errore viene provata la successiva.

Rimossa la barra con il titolo della foto: restano immagine, didascalia e testo alternativo. Crediti di tutte le immagini in una sezione apribile, con indicazione della foto corrente. La raccolta non contiene la precedente foto Super-Kamiokande; i relativi vincoli di autorizzazione riguardano la precedente selezione, conservata nella cronologia Git. Nessuna richiesta esterna per foto o font durante la visita.

## Build, verifiche e pubblicazione

Build verificata: venti HTML (tre home e diciassette articoli: nove italiani, quattro francesi, quattro albanesi), venti copertine, manifest e `.nojekyll`. Il quiz e i documenti di lavorazione restano esclusi. `scripts/home_covers.py` genera la copertina e i crediti; `scripts/home_languages.py` genera le home tradotte; `scripts/build_pages.py` verifica percorsi e lingua prima della copia. Cartelle `copertine/` e `lingue/` e relativi renderer attivano il workflow Pages.

Controlli in [verifiche-home.json](verifiche-home.json): home a 320, 390, 768, 1024 e 1440 px senza overflow, menu persistenti, focus e tastiera; tutte e venti le scelte della copertina con didascalia e crediti coerenti; navigazione delle tre lingue con e senza JavaScript, collegamenti reali agli articoli nella lingua corretta. Irraggiamento verificato a 390 e 1440 px: immagini caricate, indice nativo, assenza di richieste esterne e di errori JavaScript, navigazione dal precedente. Contenuto confrontato integralmente con il sorgente approvato, salvo meta autore e versione. Build e controllo delle differenze superati.

Fase: realizzazione conclusa e verificata, pubblicazione richiesta tramite il workflow Pages esistente dopo l’integrazione in main. Stato del deployment consultabile nelle Actions. Git conserva la cronologia delle versioni precedenti.
