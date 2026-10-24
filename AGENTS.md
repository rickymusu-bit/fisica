# Istruzioni per il progetto

## Regola vincolante — approvazione dell’anteprima prima di pubblicare

Per ogni modifica al sito, presentare prima l’anteprima corrente e attendere sempre l’approvazione esplicita dell’utente prima di integrare main o avviare GitHub Pages. Non riutilizzare un’autorizzazione di pubblicazione precedente per modifiche successive. Preparare il lavoro completo e verificato, una PR in bozza e l’anteprima sul ramo isolato di sviluppo; non fare merge né deployment ufficiale finché l’utente non approva quella specifica anteprima. Richiesta esplicita del 20 ottobre 2026, che prevale sulle autorizzazioni storiche riportate sotto.

Prima di lavorare leggi integralmente `MASTER_PROMPT.md` e lo stato del capitolo in `lavorazione/<capitolo>/stato.md`. Se lo stato manca, crealo quando il capitolo è identificato, secondo B6; non dedurre approvazioni.

Lavora in un ramo dedicato derivato da `main`. Aggiorna lo stato ai passaggi decisivi e prima di interrompere. GitHub è la fonte ufficiale e Git conserva la cronologia.

Usa nomi stabili senza versione né data e applica le regole del master per i collegamenti già pubblicati. Confronta identità e versione prima di importare o sostituire; segnala i conflitti incerti senza sovrascrivere. Rispetta il workflow di approvazione del master. Durante la migrazione non eliminare materiali su Drive e non attivare o modificare la pubblicazione del sito.

Per struttura e monograficità di tutti i capitoli applica A3 del master; per domande finali, didascalie e precisione proporzionata applica A5, C3 e A1. La revisione degli HTML esistenti deve registrare la suddivisione e verificarne i collegamenti, senza considerare automaticamente completato l'adeguamento.

Prima di scrivere o rivedere il testo delle dispense leggi anche `riferimenti/STILE_DISPENSE.md` e `riferimenti/esempio_irraggiamento.md`, richiamati in A2. Il riferimento comprende la spiegazione discorsiva e l'interpretazione delle formule secondo A4.

Per impaginare o rivedere gli HTML applica automaticamente l’esatto tema grafico comune salvato nel modello autonomo `riferimenti/TEMA_DISPENSE.html`, già approvato, secondo A6 del master; non chiedere di scegliere nuovamente il template. Nei calcoli usa forma decimale leggibile e prefissi SI, riservando la notazione scientifica ai casi utili secondo A4; interpreta i risultati degli esercizi con i confronti concreti previsti da A5.

Il punto centrato e le sue varianti sono riservati alla moltiplicazione matematica, compresi i prodotti di unità. Non usarli mai come separatori, nemmeno in grafici, legende, testi accessibili o fra versione e data. Applicare A4 del master e il tema v10.

Per la temperatura usa sempre il simbolo **T maiuscolo**, anche con pedici (per esempio T_in e T_out), in formule, testo, grafici, schemi ed etichette; usa ΔT per la differenza di temperatura. La t minuscola e Δt restano per il tempo. Richiesta esplicita dell’utente del 18 ottobre 2026.

Usa le note a piè di pagina soprattutto per alleggerire il testo: seleziona precisazioni brevi e utili, elimina ripetizioni di testo/didascalie, puntualizzazioni superflue e approfondimenti troppo tecnici, secondo A1. Mantieni le note collassabili, inizialmente chiuse, con richiami e ritorni cliccabili e versione/data separate nel piè di pagina, secondo A6.

La scritta sopra il titolo dell’articolo deve essere il nome esatto dell’area tematica presente nel catalogo della home (per i capitoli attuali: «Termologia»), senza il prefisso «Area tematica» e senza la dicitura generica «Fisica». È parte del tema comune v7.

Il nome «← Articoli» dei collegamenti alla home (che sostituisce «← Tutti gli articoli» di A6 per richiesta esplicita dell’utente) e il componente delle note collassabili sono parti integranti del tema comune secondo A6: applicali automaticamente insieme al modello autonomo in ogni capitolo futuro e nelle revisioni che lo adottano.

Per le etichette usa il vocabolario unico di A6. Prima di aggiornare o pubblicare leggi `pubblicazione.json`: modifica soltanto gli articoli conformati ammessi; conserva invariati ed escludi da ogni aggiornamento gli articoli sospesi, salvo richiesta esplicita dell’utente, secondo D2.1.

Non pubblicare né ripristinare vecchi indirizzi o reindirizzamenti degli articoli esclusi e della precedente dispensa unificata: l’utente ne ha richiesto esplicitamente la rimozione. Il manifest di pubblicazione conserva l’elenco degli indirizzi dismessi.

L’ordine degli articoli nell’indice e nella navigazione precedente/successivo è: **Stati della materia → Passaggi di stato → Conduzione → Convezione → Irraggiamento**, secondo la richiesta esplicita del 18 ottobre 2026.

Per la home usa il titolo esatto **Stringhe** e il sottotitolo **L’essenziale della Fisica**, anche nei metadati pertinenti: questa nuova richiesta esplicita dell’utente sostituisce il precedente nome del sito riportato in A6. La gerarchia editoriale resta **Area tematica → Articolo → Sezione**, ma nella home mostra soltanto il nome del gruppo (per esempio «Termologia»), senza l’etichetta «Area tematica». Applica `riferimenti/TERMINOLOGIA_SITO.md` corrente insieme alle altre etichette di A6, senza aggiornare i sorgenti esclusi.

Traduci le etichette delle infografiche e degli schemi quando richiesto; questa regola non si estende alle scritte presenti nelle fotografie, comprese le termografie. La foto delle anatre mantiene la scala originale: l’utente ha escluso la conversione.

Il logo di Stringhe conserva la curva circolare nera originale a quattro creste, nodi fissi, ampiezza 20 e periodo 4 secondi; l’utente ha richiesto di aggiungere una curva con gradiente blu di uguale ampiezza, in opposizione di fase. I percorsi stabili restano `identita/logo-materia-oscura.svg` e `.gif`. Il generatore `scripts/logo_materia_oscura.py` conserva esattamente la sequenza dell’animazione nera e genera la blu con fattore temporale opposto. La GIF si rigenera con `--gif` dallo stesso SVG. Pausa/ripresa e movimento ridotto controllano entrambe le curve; il fallback statico le mostra distinte. SVG e controlli sono incorporati nel modello e nelle sole copie dei nove articoli ammessi. Nessun aggiornamento ai sorgenti esclusi. Nella home titolo, logo e copertina appartengono a un’unica card senza onde decorative laterali. La foto scende sotto titolo e sottotitolo su ogni schermo ed è allineata al loro margine sinistro, insieme alla didascalia. La didascalia parte sempre dal bordo sinistro dell’immagine effettivamente visibile, senza margini interni o bande di contenimento. Foto intera e proporzioni conservate.

I visuali devono conservare la stessa struttura su ogni dispositivo: non cambiare disposizione, relazioni, assi o organizzazione di schemi, grafici e tabelle nella vista mobile. Ridimensiona proporzionalmente. Riserva «Ingrandisci l’immagine» del tema con scorrimento interno soltanto a grafici e schemi con numerose scritte piccole; non applicarlo alle fotografie o alle figure con poche etichette leggibili. Le sorgenti responsive possono cambiare risoluzione, non composizione. Questa richiesta esplicita prevale sulle precedenti indicazioni di A6 e C4 che consentivano di riorganizzare i visuali su smartphone; resta possibile adattare l’impaginazione del testo. Tema autonomo v7. In Passaggi di stato lo schema resta triangolare anche su mobile.

## Standard dei visuali scientifici — 20 ottobre 2026

Per selezionare, generare, costruire e verificare fotografie, schemi, illustrazioni, grafici e altri visuali del sito, leggere e applicare `docs/visual-guidelines.md`. Questo standard integra `MASTER_PROMPT.md` e il workflow di approvazione: non autorizza la creazione o pubblicazione automatica di immagini, né supera il vincolo di approvazione dell’anteprima prima del merge o del deployment. Per vettori, grafici quantitativi e geometrie esatte preferire SVG e grafici costruiti tramite codice.

## Presentazione delle bozze dei capitoli

Per richiesta esplicita dell’utente del 18 ottobre 2026, ore 13:42 (Europe/Rome), non riportare mai in chat i testi integrali dei capitoli. Scrivi e aggiorna sempre le bozze nei file `lavorazione/<capitolo>/bozza.md` del repository, sul ramo dedicato. In chat presenta soltanto una sintesi delle modifiche, i punti da approvare e i collegamenti ai file effettivamente salvati. Questa richiesta prevale sull’alternativa di presentazione integrale in chat prevista da A6 e B1.1 del master; restano necessari approvazione delle bozze e via esplicito prima della realizzazione HTML. Non modificare main o pubblicazione senza approvazione.

## Gestione dei crediti e delle licenze — tema v10

I crediti correnti devono riferirsi soltanto alle immagini e agli altri materiali ancora presenti nel documento. A ogni sostituzione o rimozione, aggiornare le associazioni del registro, la pagina generale e i crediti incorporati; eliminare dagli avvisi correnti i riferimenti a media non più usati. La pagina pubblica comprende soltanto i capitoli ammessi e la home. Conservare originali, schede e provenienze storiche nel registro, nei materiali di lavorazione e in Git, senza mostrarli come crediti dei capitoli attuali. Preservare le fonti dei dati e delle spiegazioni ancora utilizzati anche quando non sono associate a un’immagine. Eseguire il controllo delle associazioni con `scripts/credits.py --check` prima della consegna.

Per la richiesta esplicita corrente, migrare i crediti di tutti gli articoli HTML, compresi i sorgenti storici e tradotti: questa revisione circoscritta non li riammette alla pubblicazione. Il manifest di pubblicazione resta invariato.

Applicare C1 del master: nessuna sezione finale visibile automatica per immagini o font. Fonte unica `risorse/crediti.json`; pagina generata `crediti.html`; accesso comune e snapshot incorporato offline del tema v10. Registrare metadati disponibili tramite gli attributi `data-credit-*` e `python3 scripts/credits.py --sync`, quindi eseguire `--check` e la build Pages. Riutilizzare le schede esistenti, conservare gli avvisi OFL di Lexend e rispettare le eccezioni delle singole licenze, anche accanto alla figura quando prescritto. Non eliminare riferimenti scientifici né inventare autorizzazioni. Le istruzioni operative e lo schema sono in `risorse/README.md`.

Il tema v10 usa un solo comando «Crediti e licenze», che apre i crediti incorporati del documento anche offline. Al suo interno «Crediti di tutti gli articoli» apre la pagina generale online. Questa revisione riguarda home, articoli ammessi e modello; i documenti esclusi conservano il componente storico.

## Nuova identità e navigazione — 20 ottobre 2026

Nome ufficiale del sito: **Stringhe**. Sottotitolo esatto: **L’essenziale della Fisica**.
La home è un portale con tre accessi: Tutti i capitoli, Mi sento fortunato e Quiz. **Barra universale Stringhe, disposizione A**: lo stesso componente HTML/CSS/JS in ogni pagina, con gruppo contestuale a sinistra e menu Lingua/Tema sempre a destra, pulsanti con icone da almeno 44 px e ordine stabile su desktop/mobile. Home: nessun comando a sinistra; Catalogo e Quiz: Home; Capitolo: Home, Capitoli, Scarica, Indice; Crediti: Home, Capitoli. La pagina corrente non appare come collegamento a sé stessa. Le barre non mostrano il marchio o il logo, che resta nella copertina della home. I due menu sono mutuamente esclusivi, con Escape/clic esterno e tastiera; il nome della funzione appare solo a hover mouse/penna, mai al tocco o focus, con etichette accessibili permanenti. Fonte unica `navigation_header` in `scripts/stringhe_theme.py`, richiamata dai renderer; evitare barre duplicate nei file di servizio o capitoli. La lingua resta soltanto nel menu superiore. Novità sostituisce Esplora e Da leggere, con tre capitoli ordinati per data editoriale decrescente, senza numeri. Per distinguere le pubblicazioni dello stesso giorno, registrare anche l’orario ISO 8601 con fuso in `<meta name="date">`; le vecchie date senza orario valgono come inizio giornata Europe/Rome. Soltanto a parità di istante precede il capitolo più avanti nel catalogo. Aggiornare `<meta name="date">` nelle nuove pubblicazioni o revisioni editoriali; le modifiche al tema non aggiornano le date dei capitoli.
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

## Tema Stringhe comune — modello v24

Il piano Stringhe autorizza il restyling globale: portale, servizi, nove copie pubblicabili e modello ufficiale. Token, palette, reticolo e comportamenti sono definiti una sola volta in `identita/tema-stringhe.css`, `tema-init.js`, `tema-controlli.js`, incorporati da `scripts/stringhe_theme.py`. Il modello autonomo v24 conserva le stesse componenti: dopo una modifica condivisa eseguire `python3 scripts/sync_stringhe_theme.py`, poi `--check`. Non generare il modello da un articolo né modificare i sorgenti sospesi. La sincronizzazione riguarda soltanto modello, confronto e pagina dei crediti; non usare `credits.py --sync` per una migrazione generale non autorizzata.

Il menu Chiaro / Scuro, con icona luna o sole, vale anche per le nuove dispense: default Scuro indipendente dal sistema, scelta persistente, funzionamento senza storage e fallback scuro senza JavaScript. Logo e risorse scientifiche non si invertono; i visuali restano sulle superfici appropriate. La navigazione online è relativa; i rimandi del documento scaricato hanno il fallback pubblico.

L’utente ha approvato reticolo A regolare e sinusoidi A di uguale ampiezza. Le varianti B restano soltanto confronti storici. Approvata anche la posizione laterale verticale: applicarla al tema comune, compreso il corpo continuo degli articoli. Non dividere il testo in card per sezione; riservare fasce laterali senza sovrapporre le curve a paragrafi, formule o figure. Pagina `lavorazione/sito/anteprima-bordi-stringhe.html`, generata dallo stesso tema e pubblicata solo nell’anteprima di sviluppo. Conservare la PR #43 in bozza. Non unire main né avviare Pages prima della scelta esplicita e dell’autorizzazione alla pubblicazione.

## Terminologia e pubblicazione autorizzate — 20 ottobre 2026

La richiesta finale dell’utente sostituisce le indicazioni precedenti: usare **Capitolo / Capitoli** nelle etichette del portale, navigazione, indice e crediti; gerarchia Area tematica → Capitolo → Sezione. Conservare URL storici (`articoli.html`), chiavi del manifest, sorgenti scientifici e documenti esclusi. Nessuna scritta sopra «Stringhe» nella home; sottotitolo blu in entrambi i temi. Modello corrente v22. L’utente ha autorizzato esplicitamente l’integrazione della PR #43 verso main e la pubblicazione tramite Pages; i precedenti vincoli di bozza sono superati. La pagina di confronto resta esclusa dal deployment ufficiale.

## Comandi dei media — regola del 20 ottobre 2026

GIF con unico comando play/pausa a icona in basso a sinistra dell’immagine; immagini ingrandibili con unico comando ingrandisci/rimpicciolisci a icona nella stessa posizione. Nomi accessibili e suggerimenti aggiornati, tastiera, bersagli da almeno 44 px, fermo delle GIF con movimento ridotto e zoom nativo anche senza JavaScript. Componenti canoniche in `identita/media-controls.css`, `media-controls.js` e `scripts/media_controls.py`; applicarle ai capitoli esistenti e futuri e al modello. Per ogni nuova GIF preparare un fermo immagine incorporato (`data-still`) senza alterare l’originale animato. La richiesta generale di allineamento delle didascalie è stata ritirata: non introdurre né applicare quella regola; resta la precedente regola specifica della copertina della home.

## Macro categoria dei fenomeni termici — 20 ottobre 2026

Nome esatto richiesto dall’utente: **Termologia**, in sostituzione di «Materia e calore». Applicarlo al catalogo, ai filtri e alle etichette sopra i titoli e negli indici dei capitoli dell’area, compresi i nuovi capitoli in lavorazione. Conservare indirizzi e identificativi dei collegamenti, ordine, contenuti scientifici, date editoriali e manifest. Il modello comune conserva il segnaposto generico per l’area; i capitoli di questa macro categoria devono compilare quel segnaposto con il nuovo nome.

## Video YouTube su richiesta — 23 ottobre 2026

Applicare C5 del master corrente: riquadro con titolo e icona, senza miniature o fotogrammi, nessuna connessione a YouTube prima del clic; iframe da youtube-nocookie.com soltanto dopo «Carica il video», senza autoplay, con comandi nativi, schermo intero e «Chiudi il lettore». Conservare URL e timestamp; «Apri su YouTube» sempre visibile, anche senza JavaScript, offline o se il lettore non funziona. Usare scripts/youtube_videos.py e identita/youtube-videos.css/js, condivisi dal modello. Dimensioni responsive con minimo del player 200 × 200 px e tastiera/focus accessibili. Non promettere privacy assoluta, assenza di pubblicità o riproduzione garantita dall’HTML locale. Questo incarico autorizza la sola revisione dei video anche nei sorgenti esclusi e tradotti; manifest e stato di pubblicazione restano invariati. Copie HTML di lavorazione correnti da riallineare; materiali storici non riscritti in massa. Le nuove regole sostituiscono il precedente divieto di lettori YouTube incorporati e l’obbligo delle miniature. Modello comune v23 con componente video su richiesta; conservare il tema grafico approvato.

## Zoom selettivo e copertine senza zoom — 23 ottobre 2026

Le immagini di copertina non devono mai avere pulsanti o modalità di zoom/ingrandimento. Applicare A3/A6 del master e il filtro canonico di scripts/media_controls.py, conservando intera l’immagine principale. Lo zoom è riservato ai grafici e agli schemi del corpo con numerose scritte piccole. Non aggiungerlo alle fotografie o alle figure con poche etichette leggibili; non duplicare queste immagini in un pannello di zoom.


## Principio di economia informativa — 24 ottobre 2026

Ogni elemento testuale o visivo deve aggiungere informazione effettivamente utile. Assumere che il lettore sappia interpretare il contesto, osservare le immagini e ricavare inferenze elementari; non verbalizzare ciò che è già chiaramente visibile o appena spiegato. Non confondere completezza, rigore o accessibilità con ripetizione e puntualizzazione sistematica.

- **Testo:** eliminare frasi introduttive vuote, precisazioni ovvie, ripetizioni e digressioni che non cambiano la comprensione. Approfondire invece passaggi nuovi, difficili o controintuitivi.
- **Immagini, schemi e grafici:** usare solo etichette, frecce, legende, titoli interni e annotazioni necessari a riconoscere grandezze, leggere dati o evitare ambiguità. Non replicare nel visuale le spiegazioni del paragrafo.
- **Didascalie:** non descrivere banalmente ciò che è già riconoscibile. Aggiungere solo identificazioni non ovvie, relazioni significative, dati, condizioni o contesto interpretativo non ricavabili altrimenti. Omettere la didascalia descrittiva quando non serve; mantenere attribuzioni, informazioni obbligatorie e supporti di accessibilità nelle sedi appropriate.
- **Rigore e inclusione:** conservare unità, scale, simboli, ipotesi, condizioni di validità e avvertenze quando la loro omissione potrebbe produrre un errore o fraintendimento rilevante. Testi alternativi accessibili non vanno svuotati solo perché l'immagine è comprensibile a chi la vede.
- **Revisione:** per ogni frase, didascalia, etichetta e annotazione chiedersi: «Se la elimino, il lettore perde un'informazione importante o rischia un fraintendimento?». Se no, eliminarla.

Questo criterio vale anche per bozze, anteprime, materiali scaricabili e future revisioni, senza autorizzare modifiche ai capitoli già pubblicati o deroghe al workflow di approvazione.
