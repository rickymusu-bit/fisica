# Stato — Home e GitHub Pages

## Rimozione dei vecchi collegamenti — 2026-10-18 09:23 (Europe/Rome)

Richiesta esplicita dell’utente: «Non lo fare. Cancella i vecchi link degli articoli non conformati». Rimossi anche i due reindirizzamenti di compatibilità della precedente dispensa unificata dalla pubblicazione; la build non li copia più e rifiuta un elenco di reindirizzamenti non vuoto. Manifest v2, regola operativa in AGENTS e README aggiornati. Home e tre articoli conformati restano identici; i sette sorgenti sospesi restano conservati e invariati. Il master v59, letto integralmente, prevede già in D2 l’eccezione per la rimozione esplicita dei vecchi indirizzi. Nessuna modifica editoriale o al tema. Output previsto: soltanto home e tre articoli, senza altre pagine HTML. Fase: build e verifica, poi pubblicazione e controlli HTTP 404 dei nove indirizzi dismessi. I blocchi storici che indicano reindirizzamenti mantenuti sono superati da questa richiesta.

## Terminologia unica e articoli conformati — 2026-10-18 09:16 (Europe/Rome)

L’utente ha approvato il vocabolario proposto e chiesto di salvare la regola e aggiornare il sito. Successivamente ha disposto: «Togli dalla pubblicazione gli articoli che non abbiamo conformato e lasciali fuori da ogni aggiornamento». Sono ammessi soltanto Stati della materia, Passaggi di stato e Irraggiamento; i sette sorgenti esclusi, elencati in `pubblicazione.json`, sono conservati identici e non vengono aggiornati. L’esclusione comprende catalogo, download e output Pages, con verifica successiva HTTP 404 per i vecchi indirizzi. Nessuna modifica agli stati o alle bozze dei sette articoli congelati.

Master v59 e AGENTS aggiornati; modello autonomo v4 con nomi coerenti. Home pubblicabile v9, soli tre articoli e pulsanti Scarica con dimensioni reali. Articoli v14/v15/v7, etichette e navigazione allineate. Build controllata tramite elenco ammessi, confronto del catalogo, controllo dei collegamenti e pulizia dell’output; il manifest attiva il workflow Pages quando cambia. I due reindirizzamenti storici della materia restano pubblicati per compatibilità. Ramo `sito/terminologia-coerente`, derivato da main; pubblicazione autorizzata dalla richiesta di aggiornare il sito. Pubblicato con la PR #22 e workflow Pages 39107141160 concluso con successo. Verificati HTTPS: home e tre articoli conformati HTTP 200, identici all’output approvato; sette articoli sospesi HTTP 404; due reindirizzamenti storici disponibili. Sorgenti esclusi ancora identici. Rapporto finale in `lavorazione/sito/terminologia.json`.

Rapporto corrente: `terminologia.json`; anteprime della home e dell’indice a 390/1280 px nella cartella. Il tema e la regola di esclusione sono permanenti; per riammettere un articolo sospeso occorre una richiesta esplicita dell’utente.

## Pubblicazione autorizzata — 2026-10-18 09:00 (Europe/Rome)

L’utente ha approvato le anteprime e richiesto esplicitamente «Ok ok pubblica». Autorizzata l’integrazione del ramo `revisione/materia-passaggi-capitoli` in main e la pubblicazione tramite il workflow Pages esistente: Stati della materia **v13**, Passaggi di stato **v14**, Irraggiamento **v6**. Contenuti approvati al commit `fc325c9ff17e7339a15b403a26b6a98a161e8332`; nessun cambiamento ai tre HTML durante la preparazione della pubblicazione. Master v58 consultato; build locale e copie esatte nell’output verificate. Home con i due capitoli separati e vecchi indirizzi conservati tramite reindirizzamento. Pubblicazione completata tramite PR #20, merge `fb44117ae488c2cded4eb2a0abdeca0002839083`; workflow Pages `39106119681` concluso con successo. Verificati via HTTPS home v8, Stati della materia v13, Passaggi di stato v14, Irraggiamento v6 e i due vecchi indirizzi: HTTP 200 e contenuti identici byte per byte all’output approvato. Esiti e hash in `lavorazione/stati_della_materia_e_passaggi_di_stato/pubblicazione.json`. Non restano passaggi di pubblicazione pendenti. Le indicazioni di mancata autorizzazione nei blocchi storici sottostanti sono superate da questa richiesta.

Aggiornamento: 17/10/2026 19:53 (Europe/Rome).

## Preferenza permanente — anteprima del sito

Richiesta esplicita dell’utente: fornire sempre l’anteprima dopo ogni modifica al sito. Regola registrata nel master v53, sezione B5: anteprima HTML interattiva e immagini delle parti modificate, con vista mobile quando pertinente, prima della pubblicazione e senza una richiesta separata. Per la home v7 l’anteprima è stata preparata e consegnata; l’utente ha autorizzato esplicitamente la pubblicazione della PR #19 con «Ok pubblica».

## Revisione corrente — home italiana v7

Correzione richiesta: Marco Polo è una piattaforma petrolifera offshore, non una nave. Aggiornati didascalia, testo alternativo e titolo interno nel manifest e nei dati della home. Fotografia, crediti e licenza conservati. Versione dell’output aggiornata a v7. L’utente ha scelto esplicitamente «Pannello laterale apribile da Articoli». Realizzato un dialog nativo laterale: comando Articoli in alto a sinistra, Italiano in alto a destra, rimosso Esplora e il suo blocco inferiore. Elenco raggruppato con download e dimensioni reali; chiusura con ×, Esc o clic sullo sfondo. Focus confinato nel dialog e restituito al comando alla chiusura, scorrimento della pagina bloccato durante l’apertura, supporto alle ancore già pubblicate. Senza JavaScript il catalogo è visibile in pagina.

Verifiche completate: build con dieci HTML italiani e venti copertine; Chromium a 320, 390, 768, 1024 e 1440 px; apertura da tastiera, focus, chiusura con tutti e tre i metodi, ritorno al comando, ancore dirette, download confrontato byte per byte e dimensioni dei nove file; nessun overflow o errore JavaScript; fallback senza JavaScript. Controllati visivamente pannello mobile e desktop. Manifest e dati della home coerenti per Marco Polo; immagine, crediti e licenza conservati. README aggiornato.

Fase: modifiche completate e verificate nel ramo `home/copertina-marco-polo`; anteprima consegnata e pubblicazione autorizzata dall’utente con «Ok pubblica». Integrare la PR #19 e verificare il workflow Pages e la home online. La pubblicazione precedente della v6 è conclusa con successo (PR #18, workflow 39055028249).

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
