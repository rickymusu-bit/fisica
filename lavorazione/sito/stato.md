# Stato — Home e GitHub Pages

Aggiornamento: 17/10/2026 19:41 (Europe/Rome).

## Revisione corrente — home italiana v7

Correzione richiesta: Marco Polo è una piattaforma petrolifera offshore, non una nave. Aggiornati didascalia, testo alternativo e titolo interno nel manifest e nei dati della home. Fotografia, crediti e licenza conservati. Versione dell’output aggiornata a v7. Proposta di navigazione presentata: pannello laterale apribile da “Articoli”, con varianti barra fissa su desktop o elenco a scomparsa; scelta dell’utente ancora in attesa, nessuna modifica alla navigazione eseguita.

## Revisione precedente — home italiana v6

Richiesta aggiornata: «Togli proprio le altre lingue, lascia solo il selettore della lingua in alto a destra con solo l’italiano». Rimossi dal template i collegamenti francese e albanese. La build pubblica esclusivamente la home e i nove articoli italiani, con venti copertine: non genera le home tradotte né copia gli articoli tradotti. I sorgenti delle traduzioni restano conservati nel repository e non vengono pubblicati. Il selettore nativo in alto a destra mantiene la sola voce Italiano. Conservate tutte le modifiche già richieste: rimozione Indice, catalogo al clic, icona e peso effettivo dei download. Master consultato: v52; modifica locale autorizzata secondo B2.

Verifiche: build completa con dieci HTML tutti lang=it, assenza di home e articoli fr/sq nell’output; selettore con una sola voce Italiano; Chromium desktop e smartphone, catalogo inizialmente nascosto, apertura e focus da tastiera, ancore e download. Aggiornato README. Ramo dedicato `home/esplora-download`, PR #18. L’utente ha autorizzato esplicitamente la pubblicazione con «Pubblica»: integrazione in main e deployment tramite il workflow Pages esistente autorizzati; verificare il completamento delle Actions e la home online.

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
