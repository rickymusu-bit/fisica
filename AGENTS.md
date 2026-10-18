# Istruzioni per il progetto

Prima di lavorare leggi integralmente `MASTER_PROMPT.md` e lo stato del capitolo in `lavorazione/<capitolo>/stato.md`. Se lo stato manca, crealo quando il capitolo è identificato, secondo B6; non dedurre approvazioni.

Lavora in un ramo dedicato derivato da `main`. Aggiorna lo stato ai passaggi decisivi e prima di interrompere. GitHub è la fonte ufficiale e Git conserva la cronologia.

Usa nomi stabili senza versione né data e applica le regole del master per i collegamenti già pubblicati. Confronta identità e versione prima di importare o sostituire; segnala i conflitti incerti senza sovrascrivere. Rispetta il workflow di approvazione del master. Durante la migrazione non eliminare materiali su Drive e non attivare o modificare la pubblicazione del sito.

Per struttura e monograficità di tutti i capitoli applica A3 del master; per domande finali, didascalie e precisione proporzionata applica A5, C3 e A1. La revisione degli HTML esistenti deve registrare la suddivisione e verificarne i collegamenti, senza considerare automaticamente completato l'adeguamento.

Prima di scrivere o rivedere il testo delle dispense leggi anche `riferimenti/STILE_DISPENSE.md` e `riferimenti/esempio_irraggiamento.md`, richiamati in A2. Il riferimento comprende la spiegazione discorsiva e l'interpretazione delle formule secondo A4.

Per impaginare o rivedere gli HTML applica automaticamente l’esatto tema grafico comune salvato nel modello autonomo `riferimenti/TEMA_DISPENSE.html`, già approvato, secondo A6 del master; non chiedere di scegliere nuovamente il template. Nei calcoli applica notazione esponenziale e prefissi SI secondo A4; interpreta i risultati degli esercizi con i confronti concreti previsti da A5.

Per la temperatura usa sempre il simbolo **T maiuscolo**, anche con pedici (per esempio T_in e T_out), in formule, testo, grafici, schemi ed etichette; usa ΔT per la differenza di temperatura. La t minuscola e Δt restano per il tempo. Richiesta esplicita dell’utente del 18 ottobre 2026.

Usa le note a piè di pagina soprattutto per alleggerire il testo: seleziona precisazioni brevi e utili, elimina ripetizioni di testo/didascalie, puntualizzazioni superflue e approfondimenti troppo tecnici, secondo A1. Mantieni le note collassabili, inizialmente chiuse, con richiami e ritorni cliccabili e versione/data separate nel piè di pagina, secondo A6.

La scritta sopra il titolo dell’articolo deve essere il nome esatto dell’area tematica presente nel catalogo della home (per gli attuali tre articoli: «Materia e calore»), senza il prefisso «Area tematica» e senza la dicitura generica «Fisica». È parte del tema comune v7.

Il nome «← Articoli» dei collegamenti alla home (che sostituisce «← Tutti gli articoli» di A6 per richiesta esplicita dell’utente) e il componente delle note collassabili sono parti integranti del tema comune secondo A6: applicali automaticamente insieme al modello autonomo in ogni capitolo futuro e nelle revisioni che lo adottano.

Per le etichette usa il vocabolario unico di A6. Prima di aggiornare o pubblicare leggi `pubblicazione.json`: modifica soltanto gli articoli conformati ammessi; conserva invariati ed escludi da ogni aggiornamento gli articoli sospesi, salvo richiesta esplicita dell’utente, secondo D2.1.

Non pubblicare né ripristinare vecchi indirizzi o reindirizzamenti degli articoli esclusi e della precedente dispensa unificata: l’utente ne ha richiesto esplicitamente la rimozione. Il manifest di pubblicazione conserva l’elenco degli indirizzi dismessi.

Per la home usa il titolo esatto **Materia Oscura** e il sottotitolo **Guida pratica per fare luce sulla Fisica**, anche nei metadati pertinenti: questa nuova richiesta esplicita dell’utente sostituisce il precedente nome del sito riportato in A6. La gerarchia editoriale resta **Area tematica → Articolo → Sezione**, ma nella home mostra soltanto il nome del gruppo (per esempio «Materia e calore»), senza l’etichetta «Area tematica». Applica `riferimenti/TERMINOLOGIA_SITO.md` v4 insieme alle altre etichette di A6, senza aggiornare i sorgenti esclusi.

Traduci le etichette delle infografiche e degli schemi quando richiesto; questa regola non si estende alle scritte presenti nelle fotografie, comprese le termografie. La foto delle anatre mantiene la scala originale: l’utente ha escluso la conversione.

Il logo grafico definitivo di Materia Oscura è l’**onda sinusoidale stazionaria a quattro creste**, nera su trasparente, con nodi fissi e ampiezza 20, salvata in `identita/logo-materia-oscura.svg` e `.gif`. Usa solo questa coppia, senza riprendere i tentativi rimossi. Applicala accanto al titolo della home e al posto dell’icona nella barra in alto a sinistra degli articoli conformati e futuri. La scelta, il pulsante di pausa/ripresa, il movimento ridotto e le dimensioni responsive sono parte dell’esatto tema comune **v7** salvato in `riferimenti/TEMA_DISPENSE.html`; specifiche in `identita/README.md` v5. Mantieni i documenti autonomi incorporando SVG e controlli comuni, senza modificare i sette articoli esclusi.

I visuali devono conservare la stessa struttura su ogni dispositivo: non cambiare disposizione, relazioni, assi o organizzazione di schemi, grafici e tabelle nella vista mobile. Ridimensiona proporzionalmente e, se scritte o dettagli risultano troppo piccoli, usa «Ingrandisci l’immagine» del tema con scorrimento interno. Le sorgenti responsive possono cambiare risoluzione, non composizione. Questa richiesta esplicita prevale sulle precedenti indicazioni di A6 e C4 che consentivano di riorganizzare i visuali su smartphone; resta possibile adattare l’impaginazione del testo. Tema autonomo v7. In Passaggi di stato lo schema resta triangolare anche su mobile.

## Presentazione delle bozze dei capitoli

Per richiesta esplicita dell’utente del 18 ottobre 2026, ore 13:42 (Europe/Rome), non riportare mai in chat i testi integrali dei capitoli. Scrivi e aggiorna sempre le bozze nei file `lavorazione/<capitolo>/bozza.md` del repository, sul ramo dedicato. In chat presenta soltanto una sintesi delle modifiche, i punti da approvare e i collegamenti ai file effettivamente salvati. Questa richiesta prevale sull’alternativa di presentazione integrale in chat prevista da A6 e B1.1 del master; restano necessari approvazione delle bozze e via esplicito prima della realizzazione HTML. Non modificare main o pubblicazione senza approvazione.
