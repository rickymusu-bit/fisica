# Istruzioni per il progetto

Prima di lavorare leggi integralmente `MASTER_PROMPT.md` e lo stato del capitolo in `lavorazione/<capitolo>/stato.md`. Se lo stato manca, crealo quando il capitolo è identificato, secondo B6; non dedurre approvazioni.

Lavora in un ramo dedicato derivato da `main`. Aggiorna lo stato ai passaggi decisivi e prima di interrompere. GitHub è la fonte ufficiale e Git conserva la cronologia.

Usa nomi stabili senza versione né data e applica le regole del master per i collegamenti già pubblicati. Confronta identità e versione prima di importare o sostituire; segnala i conflitti incerti senza sovrascrivere. Rispetta il workflow di approvazione del master. Durante la migrazione non eliminare materiali su Drive e non attivare o modificare la pubblicazione del sito.

Per struttura e monograficità di tutti i capitoli applica A3 del master; per domande finali, didascalie e precisione proporzionata applica A5, C3 e A1. La revisione degli HTML esistenti deve registrare la suddivisione e verificarne i collegamenti, senza considerare automaticamente completato l'adeguamento.

Prima di scrivere o rivedere il testo delle dispense leggi anche `riferimenti/STILE_DISPENSE.md` e `riferimenti/esempio_irraggiamento.md`, richiamati in A2. Il riferimento comprende la spiegazione discorsiva e l'interpretazione delle formule secondo A4.

Per impaginare o rivedere gli HTML applica automaticamente l’esatto tema grafico comune salvato nel modello autonomo `riferimenti/TEMA_DISPENSE.html`, già approvato, secondo A6 del master; non chiedere di scegliere nuovamente il template. Nei calcoli usa forma decimale leggibile e prefissi SI, riservando la notazione scientifica ai casi utili secondo A4; interpreta i risultati degli esercizi con i confronti concreti previsti da A5.

Il punto centrato e le sue varianti sono riservati alla moltiplicazione matematica, compresi i prodotti di unità. Non usarli mai come separatori, nemmeno in grafici, legende, testi accessibili o fra versione e data. Applicare A4 del master e il tema v10.

Per la temperatura usa sempre il simbolo **T maiuscolo**, anche con pedici (per esempio T_in e T_out), in formule, testo, grafici, schemi ed etichette; usa ΔT per la differenza di temperatura. La t minuscola e Δt restano per il tempo. Richiesta esplicita dell’utente del 18 ottobre 2026.

Usa le note a piè di pagina soprattutto per alleggerire il testo: seleziona precisazioni brevi e utili, elimina ripetizioni di testo/didascalie, puntualizzazioni superflue e approfondimenti troppo tecnici, secondo A1. Mantieni le note collassabili, inizialmente chiuse, con richiami e ritorni cliccabili e versione/data separate nel piè di pagina, secondo A6.

La scritta sopra il titolo dell’articolo deve essere il nome esatto dell’area tematica presente nel catalogo della home (per gli attuali tre articoli: «Materia e calore»), senza il prefisso «Area tematica» e senza la dicitura generica «Fisica». È parte del tema comune v7.

Il nome «← Articoli» dei collegamenti alla home (che sostituisce «← Tutti gli articoli» di A6 per richiesta esplicita dell’utente) e il componente delle note collassabili sono parti integranti del tema comune secondo A6: applicali automaticamente insieme al modello autonomo in ogni capitolo futuro e nelle revisioni che lo adottano.

Per le etichette usa il vocabolario unico di A6. Prima di aggiornare o pubblicare leggi `pubblicazione.json`: modifica soltanto gli articoli conformati ammessi; conserva invariati ed escludi da ogni aggiornamento gli articoli sospesi, salvo richiesta esplicita dell’utente, secondo D2.1.

Non pubblicare né ripristinare vecchi indirizzi o reindirizzamenti degli articoli esclusi e della precedente dispensa unificata: l’utente ne ha richiesto esplicitamente la rimozione. Il manifest di pubblicazione conserva l’elenco degli indirizzi dismessi.

L’ordine degli articoli nell’indice e nella navigazione precedente/successivo è: **Stati della materia → Passaggi di stato → Conduzione → Convezione → Irraggiamento**, secondo la richiesta esplicita del 18 ottobre 2026.

Per la home usa il titolo esatto **Stringhe** e il sottotitolo **L’essenziale della Fisica**, anche nei metadati pertinenti: questa nuova richiesta esplicita dell’utente sostituisce il precedente nome del sito riportato in A6. La gerarchia editoriale resta **Area tematica → Articolo → Sezione**, ma nella home mostra soltanto il nome del gruppo (per esempio «Materia e calore»), senza l’etichetta «Area tematica». Applica `riferimenti/TERMINOLOGIA_SITO.md` corrente insieme alle altre etichette di A6, senza aggiornare i sorgenti esclusi.

Traduci le etichette delle infografiche e degli schemi quando richiesto; questa regola non si estende alle scritte presenti nelle fotografie, comprese le termografie. La foto delle anatre mantiene la scala originale: l’utente ha escluso la conversione.

Il logo grafico definitivo di Stringhe è l’**onda sinusoidale stazionaria a quattro creste**, nera su trasparente, con nodi fissi e ampiezza 20, salvata in `identita/logo-materia-oscura.svg` e `.gif`. Usa solo questa coppia, senza riprendere i tentativi rimossi. Applicala accanto al titolo della home e al posto dell’icona nella barra in alto a sinistra degli articoli conformati e futuri. La scelta, il pulsante di pausa/ripresa, il movimento ridotto e le dimensioni responsive sono parte dell’esatto tema comune **v7** salvato in `riferimenti/TEMA_DISPENSE.html`; specifiche in `identita/README.md` v5. Mantieni i documenti autonomi incorporando SVG e controlli comuni, senza modificare i sette articoli esclusi.

I visuali devono conservare la stessa struttura su ogni dispositivo: non cambiare disposizione, relazioni, assi o organizzazione di schemi, grafici e tabelle nella vista mobile. Ridimensiona proporzionalmente e, se scritte o dettagli risultano troppo piccoli, usa «Ingrandisci l’immagine» del tema con scorrimento interno. Le sorgenti responsive possono cambiare risoluzione, non composizione. Questa richiesta esplicita prevale sulle precedenti indicazioni di A6 e C4 che consentivano di riorganizzare i visuali su smartphone; resta possibile adattare l’impaginazione del testo. Tema autonomo v7. In Passaggi di stato lo schema resta triangolare anche su mobile.

## Presentazione delle bozze dei capitoli

Per richiesta esplicita dell’utente del 18 ottobre 2026, ore 13:42 (Europe/Rome), non riportare mai in chat i testi integrali dei capitoli. Scrivi e aggiorna sempre le bozze nei file `lavorazione/<capitolo>/bozza.md` del repository, sul ramo dedicato. In chat presenta soltanto una sintesi delle modifiche, i punti da approvare e i collegamenti ai file effettivamente salvati. Questa richiesta prevale sull’alternativa di presentazione integrale in chat prevista da A6 e B1.1 del master; restano necessari approvazione delle bozze e via esplicito prima della realizzazione HTML. Non modificare main o pubblicazione senza approvazione.

## Gestione dei crediti e delle licenze — tema v10

Per la richiesta esplicita corrente, migrare i crediti di tutti gli articoli HTML, compresi i sorgenti storici e tradotti: questa revisione circoscritta non li riammette alla pubblicazione. Il manifest di pubblicazione resta invariato.

Applicare C1 del master: nessuna sezione finale visibile automatica per immagini o font. Fonte unica `risorse/crediti.json`; pagina generata `crediti.html`; accesso comune e snapshot incorporato offline del tema v10. Registrare metadati disponibili tramite gli attributi `data-credit-*` e `python3 scripts/credits.py --sync`, quindi eseguire `--check` e la build Pages. Riutilizzare le schede esistenti, conservare gli avvisi OFL di Lexend e rispettare le eccezioni delle singole licenze, anche accanto alla figura quando prescritto. Non eliminare riferimenti scientifici né inventare autorizzazioni. Le istruzioni operative e lo schema sono in `risorse/README.md`.

Il tema v10 usa un solo comando «Crediti e licenze», che apre i crediti incorporati del documento anche offline. Al suo interno «Crediti di tutti gli articoli» apre la pagina generale online. Questa revisione riguarda home, articoli ammessi e modello; i documenti esclusi conservano il componente storico.

## Nuova identità e navigazione — 20 ottobre 2026

Nome ufficiale del sito: **Stringhe**. Sottotitolo esatto: **L’essenziale della Fisica**.
La home è un portale con quattro accessi: Tutti gli articoli, Mi sento fortunato, Quiz e Lingua.
Il catalogo è una pagina indipendente `articoli.html`, con ricerca e filtro per area tematica;
la scelta casuale include soltanto gli articoli approvati in `pubblicazione.json`.
La pagina `quiz.html` presenta il futuro generatore di quiz di verifica su argomenti scelti dall’utente. Il progetto separato «Chi vuol essere rimandato» non fa parte di questa funzione.
Ogni articolo pubblicato offre in testa: Home, Articoli, Scarica, Lingua; resta distinto l'indice interno.
Il tema visivo richiama stringhe vibranti con onde sottili e movimento rispettoso di
`prefers-reduced-motion`. Evitare che la metafora decorativa interferisca con schemi scientifici.
La build applica il tema condiviso tramite `scripts/strings_site.py`, senza aggiornare
i sorgenti degli articoli sospesi. Il logo circolare originale resta obbligatorio, con percorso storico invariato. Le denominazioni storiche nei documenti di provenienza conservano il loro significato; l’interfaccia corrente usa Stringhe.

## Incarico approvato — specifica Stringhe del 20 ottobre 2026

Per il prossimo sviluppo del portale e del tema leggere **prima** `lavorazione/sito/PIANO_IMPLEMENTAZIONE_STRINGHE.md` insieme al master e allo stato: è la lista operativa di Codex per logo circolare originale, copertina casuale, bordi sinusoidali A/B, dark mode opzionale e quiz di verifica futuro. Essa recepisce le correzioni esplicite più recenti dell'utente rispetto alla precedente proposta di design. Conservare la PR in bozza e non pubblicare senza una nuova approvazione.

## Tema Stringhe comune — modello v11

Il piano Stringhe autorizza il restyling globale: portale, servizi, nove copie pubblicabili e modello ufficiale. Token, palette, reticolo e comportamenti sono definiti una sola volta in `identita/tema-stringhe.css`, `tema-init.js`, `tema-controlli.js`, incorporati da `scripts/stringhe_theme.py`. Il modello autonomo v11 conserva le stesse componenti: dopo una modifica condivisa eseguire `python3 scripts/sync_stringhe_theme.py`, poi `--check`. Non generare il modello da un articolo né modificare i sorgenti sospesi. La sincronizzazione riguarda soltanto modello, confronto e pagina dei crediti; non usare `credits.py --sync` per una migrazione generale non autorizzata.

Il selettore Automatico / Chiaro / Scuro vale anche per le nuove dispense e funziona senza storage. Logo e risorse scientifiche non si invertono; i visuali restano sulle superfici appropriate. La navigazione online è relativa; i rimandi del documento scaricato hanno il fallback pubblico.

L’utente ha approvato reticolo A regolare e sinusoidi A di uguale ampiezza. Le varianti B restano soltanto confronti storici. La posizione laterale verticale è una prova richiesta, ancora da valutare; non applicarla automaticamente a tutto il sito. Pagina `lavorazione/sito/anteprima-bordi-stringhe.html`, generata dallo stesso tema e pubblicata solo nell’anteprima di sviluppo. Conservare la PR #43 in bozza. Non unire main né avviare Pages prima della scelta esplicita e dell’autorizzazione alla pubblicazione.
