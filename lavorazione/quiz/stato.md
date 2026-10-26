# Stato — quiz

## Stato corrente — dati con nome, simbolo e valore

25 ottobre 2026 (Europe/Rome). Master v69.20, prompt di generazione v1.4.3, specifiche quiz v2.5.1. Ramo `fix/quiz-notazione-matematica`, derivato da main `136cb6e200c8133e61b00690a22894cfa1f25030`; [PR #89](https://github.com/rickymusu-bit/fisica/pull/89).

**Richiesta corrente:** registrare e applicare ai quiz l’ordine nome della grandezza a parole, simbolo, valore con unità. Simbolo sempre presente; pedici opportuni e brevi per grandezze dello stesso tipo. Questa richiesta sostituisce la precedente preferenza per soli nomi nei dati del quesito mostrato. Aggiornate le sezioni pertinenti del master e del prompt, senza aggiunte contraddittorie. Conservate le regole su notazione scientifica, SI e pedici/apici tipografici.

**Implementazione:** 158 testi adeguati (90 calcolo, 57 ragionamento, 11 conoscenza); 10 spiegazioni riallineate nella notazione. Tutti i dati fisici, i risultati, gli indici corretti, le difficoltà e le 78 espressioni di ricalcolo restano invariati. Le alternative cambiano solo nella grafia di Q_b/Q_t in termo-137. Sincronizzate le copie dell’archivio, campione e lotti con schede e metadati. Le domande che chiedono il significato di un simbolo non ne anticipano la definizione.

**Resa:** formatter testuale sicuro con `sub`/`sup`, come i capitoli, senza librerie matematiche esterne. Un controllo sul nuovo archivio ha evidenziato un underscore residuo quando un numero precede il simbolo (esempio `2m_B`); corretto il riconoscimento e ampliato il controllo di regressione. La formattazione resta valida anche per sessioni e risultati già salvati, senza sostituire contenuti, scadenze o scelte.

**Verifiche:** archivio di 300 quesiti, 100 per livello, metadati e schede allineati; ricalcolo delle 78 soluzioni aggiuntive; confronto degli indici corretti e delle alternative con il commit precedente. Build, 26 test, JavaScript, tema e crediti. Suite browser dell’archivio reale e controlli della notazione con sessioni precedenti, tutti i pedici correnti e coefficienti numerici, Unicode, graffe, markup non attendibile; viewport 1440, 390 e 320, temi chiaro/scuro. Mobile emulato; i test non provano calibrazione didattica o tempi osservati in classe.

**Anteprima:** [quiz interattivo](termologia/notazione/quiz.html), [rapporto e immagini](termologia/notazione/README.md), [esiti sulla notazione](termologia/notazione/verifica.json). Le immagini storiche della pubblicazione precedente restano invariate.

**Autorizzazione alla pubblicazione:** il 25 ottobre 2026, dopo l’anteprima corrente, l’utente ha scritto «Perfetto, pubblica.». Sono approvati l’adeguamento e la pubblicazione della PR #89: merge in main e deploy GitHub Pages autorizzati, senza ulteriori conferme. La versione funzionale approvata è il commit `3fd79682d846e6c11e62dd7bb78e20b0088fe8ee`; [CI completa superata](https://github.com/rickymusu-bit/fisica/actions/runs/40173676319). Questo aggiornamento registra soltanto l’autorizzazione, senza cambiare quiz o anteprima. Il workflow [Pubblica Stringhe](https://github.com/rickymusu-bit/fisica/actions/workflows/pages.yml) espone l’esito del deploy; destinazione [quiz online](https://rickymusu-bit.github.io/fisica/quiz.html). La PR #88 sul rapporto della precedente pubblicazione resta separata e invariata.

## Pubblicazione del quiz di Termologia — fase precedente

Aggiornamento: 25 ottobre 2026 (Europe/Rome). Master corrente v69.18 e AGENTS v3: lette le modifiche intervenute su main; riguardano visuali, tabelle e manutenzione delle istruzioni e non modificano le specifiche del quiz. Prompt v1.4.1, specifiche quiz v2.4.0.

**Autorizzazione corrente:** dopo aver ricevuto l’archivio completo, l’utente ha scritto «Va bene, pubblica», poi «Riprendi». Sono quindi approvate tutte le 300 domande di Termologia e autorizzata la loro pubblicazione nell’ambito corrente. L’approvazione precedente del primo lotto resta registrata; nessun record delle domande è stato modificato durante l’integrazione.

**Archivio integrato:** `quiz/domande.json`, identico a [archivio.json](termologia/archivio.json). Per ogni livello: 100 domande, di cui 30 conoscenza, 40 ragionamento e 30 calcolo; totale 300 approvate e nessuna in attesa di revisione. Termologia è disponibile a tutte le difficoltà. Introduzione alla fisica e alla misura resta disabilitata perché non ha quesiti. Le sessioni da 1 a 30 pescano in un insieme da 100 per livello, senza ripetizioni. Le sessioni già salvate continuano a recuperare i propri quesiti e scadenze.

Ramo `feature/quiz-termologia-campione`, PR #81. Integrato sul ramo di lavoro main `3d8afa2`, che conserva i due nuovi capitoli già pubblicati nell’altra categoria. Manifest, capitoli e crediti non modificati da questo incarico. Aggiornati i test che presumevano un archivio vuoto e il messaggio della pagina prima dell’avvio; il punto centrato del riepilogo è sostituito da un trattino secondo la regola grafica corrente.

**Verifiche concluse:** tema condiviso allineato; registro crediti verificato; build di 24 HTML e 20 copertine; 24 test superati; validazione di tutti i 300 record e 78 ricalcoli dei nuovi quesiti. Browser Chromium desktop 1440 px e mobile emulato 390 px: archivio reale, tutti i livelli, categorie disponibili/non disponibili, estrazione di domande uniche, correzione completa 30/30 e 3/3, ordine delle opzioni, recupero della sessione e del risultato. Superata anche la suite esistente su categorie, timer, scadenze fuori pagina, storage bloccato, salvataggi corrotti e sessioni precedenti. Nessun errore JavaScript rilevato.

**Anteprima corrente e documentazione:** [rapporto di integrazione](termologia/pubblicazione.md), HTML autonomo e immagini in `termologia/anteprima/`. Gli screenshot usano domande reali e sono stati controllati visivamente. I tempi rimangono stime progettuali, non osservazioni in classe.

**Pubblicazione conclusa:** CI 40169622838 superata; PR #81 integrata con commit `136cb6e200c8133e61b00690a22894cfa1f25030`; workflow Pages 40169937887 concluso con successo. Verifica HTTPS del quiz pubblico: 300 record identici alla sorgente approvata, 100 per livello, e JavaScript/CSS pubblici corrispondenti. Esiti e link in [pubblicazione.md](termologia/pubblicazione.md) e [verifica-online.json](termologia/verifica-online.json). Nessun passaggio di pubblicazione rimasto aperto. Il solo rapporto finale è salvato sul ramo `docs/quiz-termologia-pubblicato` con PR in bozza: il controllo automatico ha rifiutato il push diretto su main perché richiede il workflow PR. Le autorizzazioni non si estendono a revisioni future.

Ultimo aggiornamento: 2026-10-16 14:15 (Europe/Rome). Master consultato: v44.

Fase: materiali esistenti importati senza modifiche; nessuna nuova progettazione o revisione didattica avviata. Ambito: i file elencati sotto. Nessun documento di lavorazione era presente nella cartella Drive dedicata.

- [quiz/Template_dataset_quiz_argomenti_v1_20261008.json](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Template_dataset_quiz_argomenti_v1_20261008.json) — 6,126 byte; provenienza nell’inventario di migrazione.
- [quiz/Prompt_generazione_dataset_quiz_v1_20261008.txt](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Prompt_generazione_dataset_quiz_v1_20261008.txt) — 9,714 byte; provenienza nell’inventario di migrazione.
- [quiz/Chi_vuol_essere_rimandato_regole_v9_20261008.html](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Chi_vuol_essere_rimandato_regole_v9_20261008.html) — 2,305,334 byte; provenienza nell’inventario di migrazione.
- [quiz/Chi_vuol_essere_rimandato_quiz_v3_20261008.html](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Chi_vuol_essere_rimandato_quiz_v3_20261008.html) — 6,360,835 byte; provenienza nell’inventario di migrazione.

Domanda iniziale, template approvato, checklist didattica, visuali e simulazioni: da ricavare dai file soltanto alla prossima lavorazione pertinente. Originali separati e registri di approvazione non presenti nella fonte di lavorazione. Approvazioni di visuali, bozza e via alla realizzazione: non documentate dalle fonti disponibili; la migrazione non le attribuisce all’utente.

Bozza corrente: nessuna fornita separatamente. Alla ripresa usa `bozza.md`, `bozza.html` e `risorse/` soltanto se necessari, con nomi stabili; non duplicare gli HTML ufficiali senza una lavorazione effettiva.

Completato: importazione integrale; verifiche tecniche nel [rapporto](../migrazione/RAPPORTO.md). Punti aperti: eventuali anomalie elencate nel rapporto e informazioni progettuali non documentate. Prossima operazione: identificare la revisione richiesta e la sua versione di partenza, leggere master e file pertinenti, quindi seguire B1–B6 conservando le parti già approvate.

## Separazione del quiz

Aggiornamento: 2026-10-16 16:52 (Europe/Rome). Master aggiornato a v46. I quattro file sono stati trasferiti senza modifiche in [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz), commit `f102b5583ff96c6574a32e32f20129535f6b9341`. Dimensioni e SHA-256 coincidono con gli originali. La richiesta esplicita dell’utente autorizza la separazione; il quiz è escluso dall’indice e dall’artefatto GitHub Pages di fisica. Gli originali restano recuperabili nella cronologia Git e su Drive. Prossime lavorazioni del quiz: usare il repository dedicato.

## Nuovo generatore del sito Stringhe — 24 ottobre 2026

**Versione 1.0.0 (anteprima).** Questa funzione è distinta dal gioco Fool, ospitato nel repository separato Quiz. Ramo di sviluppo: `feature/quiz-verifiche-20261024`. Nessuna pubblicazione in `main` autorizzata.

Requisiti approvati per la progettazione: scelta di uno o più capitoli, anche da categorie diverse, con selezione/deselezione della categoria e stato parziale; 25 domande fisse a risposta multipla; difficoltà facile con 3 alternative e 150 secondi per domanda, media con 4 e 120 secondi, difficile con 5 e 90 secondi; soltanto timer totale visibile, tempo individuale nascosto; correzione finale con voto, errori, soluzioni e spiegazioni. Dataset gestito separatamente dal renderer, senza necessità di proteggerlo con un backend. Obiettivo futuro: utilizzare quesiti adattati come base di verifiche in classe.

Prototipo: `quiz/domande-prova.json` contiene 45 quesiti, 1 per capitolo per difficoltà, destinati soltanto a collaudi. Per raggiungere 25 domande il motore può ripeterli; non è un dataset somministrabile come verifica. Il voto attuale è indicativo (corrette × 10 / 25). Il codice della pagina è in `scripts/quiz_site.py`, `quiz/interfaccia.js`, `quiz/interfaccia.css`, integrato dalla build. Specifiche complete in `quiz/README.md`. In attesa di verifica tecnica completa, anteprima e approvazione specifica prima di qualsiasi merge o deploy.


## Navigazione visiva delle domande — 24 ottobre 2026

**Versione 1.1.0 (bozza, PR #74).** Aggiunta griglia di avanzamento 1–25 nella sessione e nel risultato: domande con risposta confermata, saltate (anche per timeout), corrente, non ancora affrontate; nel riepilogo finale quelle non raggiunte restano distinte dalle saltate. Ogni numero presenta un'etichetta accessibile. Il quiz conserva l'avanzamento in una direzione e i limiti di tempo già definiti. Implementazione ancora su ramo `feature/quiz-verifiche-20261024`, senza pubblicazione su `main`.


## Quiz personalizzabile — 24 ottobre 2026

**Versione 1.2.0 (bozza, PR #74).** I requisiti precedenti (25 domande obbligatorie e tempi diversi per difficoltà) sono superati: numero di quesiti a scelta da 1 a 30, valore iniziale 25, 120 secondi per ogni domanda e durata massima di 60 minuti. La difficoltà cambia solo il livello dei quesiti e le alternative (3/4/5). La griglia di avanzamento usa la quantità effettivamente scelta; le domande saltate hanno sfondo giallo e la domanda corrente un bordo da 4 px, anche nella legenda. Il voto in decimi usa il numero effettivo di quesiti. Restano archivio separato e limite dimostrativo delle ripetizioni. Modifiche in anteprima sul solo ramo `feature/quiz-verifiche-20261024`; nessun merge o deploy su `main` prima dell'approvazione.


## Revisione layout e punteggio — 24 ottobre 2026

**Versione 1.3.0 (bozza, PR #74).** Si sostituisce il voto in decimi con il conteggio `corrette / domande effettivamente selezionate`. I comandi **Salta** e **Conferma e prosegui** sono affiancati, mentre **Concludi** è collocato all'estremità opposta, in rosso lampone scuro; sui display stretti è sulla riga successiva, allineato a destra. Resta la finestra di conferma per interrompere il quiz. Il marrone non viene usato per le domande saltate: si conferma il giallo luminoso della palette di Stringhe, applicato anche alla legenda. Aggiornati i test su punteggio e disposizione dei pulsanti. Non pubblicare su `main` prima dell'approvazione.


## Controlli numero domande — 24 ottobre 2026

**Versione 1.4.0 (bozza, PR #74).** Accanto al campo numerico (valore predefinito 25, intervallo 1–30) sono presenti pulsanti **−** e **+**, con nomi accessibili e dimensioni per il tocco. Agiscono a passi di una domanda, aggiornano subito il tempo massimo e diventano disabilitati agli estremi; rimane possibile digitare direttamente la quantità. Sono stati aggiunti controlli browser per incrementi/decrementi, limiti e durata aggiornata. Anteprima sul solo ramo di prova, senza pubblicazione su `main`.


## Disponibilità delle domande — 24 ottobre 2026

**Versione 1.5.0 (PR #74, non pubblicata).** Prima del merge richiesto, la pubblicazione è stata sospesa per aggiungere un filtro di disponibilità guidato dall'archivio quesiti. Per la difficoltà selezionata, un capitolo privo di domande appare disabilitato con la dicitura «Non disponibile»; una categoria priva di capitoli idonei è anch'essa disabilitata. La selezione globale considera solo capitoli abilitati. Cambiando difficoltà, le scelte divenute inammissibili sono deselezionate. Test browser con dataset ridotto simulato, senza modificare l'archivio dimostrativo effettivo. Non fare merge su `main` finché la revisione non è verificata e approvata.


## Pubblicazione senza quesiti dimostrativi — 24 ottobre 2026

**Versione 1.6.0.** Approvata la pubblicazione della sola interfaccia. Cancellato `quiz/domande-prova.json`; una build senza `quiz/domande.json` include `questions: []`, disabilita ogni capitolo e categoria, mostra un messaggio di indisponibilità e impedisce l'avvio. I test del browser simulano temporaneamente i quesiti in memoria, senza inserirli nel sito né in archivio. Alla disponibilità delle domande autentiche, il file previsto è `quiz/domande.json`. Pubblicazione su `main` autorizzata dall'utente dopo la rimozione del dataset di prova.



## Categoria unica — 24 ottobre 2026

Richiesta corrente: ogni quiz riguarda una sola categoria, Termologia oppure Introduzione alla fisica e alla misura. Questa scelta supera la selezione multipla di capitoli e categorie e la proposta successiva di tag multipli/filtro AND. Interrotta prima di avviarla la classificazione dei contenuti dei 17 capitoli pubblicati: nessun HTML è stato modificato per aggiungere tag.

Implementazione sul ramo `feature/quiz-categoria-unica-20261024`: registro `quiz/categorie.json` con due ID stabili; selettore radio esclusivo; archivio con `category` al posto di `chapter`; validazione del registro contro il catalogo e filtro per categoria/difficoltà. I quesiti possono collegare più capitoli della stessa categoria. Cambiando difficoltà si deseleziona una categoria diventata indisponibile. Nessun archivio reale generato o migrato; invariati quantità, scadenze, alternative, punteggio e correzione.

Aggiornati MASTER_PROMPT.md v69.13 (D2.2), AGENTS.md, prompt di generazione v1.2.0 e specifiche quiz v2.0.0. Recuperato dalla precedente PR #75 il workflow campione ChatGPT → revisione docente → lotti Codex → controlli e revisione. L’approvazione del campione non vale per lotti futuri. Specifico/trasversale resta una distinzione didattica, senza tag tecnici.

Approvazione ricevuta: implementare la semplificazione a categoria unica nell’ambito dell’incarico corrente. Nessuna approvazione di merge o pubblicazione. PR corrente: #77 in bozza (sostituisce la PR #75, chiusa). Verifiche concluse: build, 23 test e suite browser desktop/mobile superati nel workflow https://github.com/rickymusu-bit/fisica/actions/runs/40099155010 sul commit 957bafe785d9f3872151efa24ca66446f9a7ae00. Anteprima HTML e schermate salvate; dettagli nel rapporto `verifica-categoria-unica.md`. Prossimo passo: revisione dell’anteprima e approvazione prima di integrare main.


## Target dell’archivio — 24 ottobre 2026

Richiesta esplicita dell’utente: inserire nel piano l’obiettivo di **100 domande per livello per categoria**. Per Termologia e Introduzione alla fisica e alla misura: 300 domande ciascuna, 600 totali. Ripartizione iniziale per ogni livello: 30 conoscenza, 40 ragionamento e 30 calcolo, adattabile ai contenuti.

Aggiornati il piano di produzione nella sezione 10 del prompt (v1.3.0) e le specifiche quiz (v2.1.0). Procedura: campione di 9, revisione docente, lotti indicativamente da 30 e conteggio delle domande approvate per categoria/livello/tipo. Il campione approvato può concorrere al target senza duplicazioni. Il target riguarda l’archivio e non cambia il numero di domande della sessione. Nessuna domanda generata da questo aggiornamento documentale; nessun merge o deployment autorizzato. Prossima fase di produzione, su richiesta: scegliere la categoria del campione.


## Salvataggio automatico e ripresa — 24 ottobre 2026

Richiesta esplicita dell’utente: implementare il recupero del quiz dopo ricarica o uscita accidentale. Implementazione completata sulla PR #77: snapshot locale con versione, quesiti e ordine delle opzioni, risposte, scelta provvisoria, stato corrente e scadenze originali. Il rientro applica il tempo trascorso; risultato persistente fino a «Nuovo quiz». Dati incoerenti/incompatibili gestiti con avviso e rimozione; storage indisponibile con funzionamento in memoria e richiesta condizionale di avviso prima dell’uscita.

Specifiche v2.2.0, master v69.14 e AGENTS.md aggiornati. Nessuna modifica ai target dell’archivio o ai capitoli. Verifiche concluse: build completa, 23 test e suite browser desktop/mobile superati nel workflow https://github.com/rickymusu-bit/fisica/actions/runs/40101691256 sul commit 26fc64f33512df91a0fceff1c4a5c9f22d153e52. Schermate di ripresa e salvataggio bloccato salvate; dettagli nel rapporto `verifica-salvataggio.md`. Prossimo passo: revisione dell’anteprima e approvazione prima dell’integrazione in main. Nessun merge o deployment autorizzato.


## Quattro alternative per tutti i livelli — 24 ottobre 2026

Richiesta corrente dell’utente: quattro alternative uguali in numero per facile, medio e difficile. Modifica preparata sul ramo `feature/quiz-quattro-alternative-20261024`, derivato da main dopo il merge della PR #77. Aggiornati renderer, validatore, istruzioni di generazione (v1.4.0), specifiche (v2.3.0), master (v69.15) e AGENTS. La difficoltà resta definita dal contenuto cognitivo e non dal numero delle opzioni.

Nuovi salvataggi di sessione in versione 2, con quattro alternative. I salvataggi di sessioni precedenti in versione 1 restano recuperabili con le opzioni originali fino alla conclusione, senza perdere risposte o scadenze; Nuovo quiz usa sempre quattro opzioni. Nessun archivio reale da migrare. Tempo, categorie e target di 100 quesiti per livello restano invariati.

Test aggiunti: accettazione di quattro opzioni e rifiuto di tre/cinque per ciascun livello; recupero delle sessioni precedenti e creazione di nuove sessioni a quattro opzioni. PR #78 in bozza. Verifiche concluse: build completa, 24 test e suite browser desktop/mobile superati nel workflow https://github.com/rickymusu-bit/fisica/actions/runs/40103061944 sul commit 14366820a781cd27cebffecfdec31f1f228c51cf. Rapporto e schermate aggiornati in `verifica-quattro-alternative.md`. Prossimo passo: approvazione della nuova anteprima prima del merge. Nessun merge o deployment autorizzato per questa nuova revisione.


## Colori matrice e conferma conclusione — 26 ottobre 2026

Ramo `fix/quiz-colori-conferma`, derivato da main d2b9d6d. Durante il quiz: risposte confermate blu, saltate gialle, corrente con bordo di 4 px in gradiente blu. Sull’ultima domanda il comando è «Conferma». Concludi apre un dialog nativo HTML con focus iniziale su «Continua il quiz»; Escape annulla e il timer resta attivo. La scadenza chiude il dialog quando termina il quiz. Correzione: matrice e schede soluzione verdi/corrette, gialle/omesse (anche non raggiunte), rosse/errate; punteggio invariato.

Verifiche eseguite: `node --check quiz/interfaccia.js`; compilazione Python del renderer; 5 test `test_quiz.py` superati. Prova interattiva Chromium desktop su anteprima generata dal renderer canonico: sessione con due corrette, una saltata e una errata (2/4), classi e colori calcolati corrispondenti; bordo gradiente 4 px; etichetta ultima domanda; annullamento con pulsante e Escape, conferma anticipata e ripristino risultato dopo ricarica. Verificato timer in movimento durante il dialog. Anteprima usa una cornice minima con il CSS condiviso; non modifica la navigazione pubblica. Non eseguite build completa, verifica su Android fisico o prova scadenza automatica del dialog.

Anteprima verificata: `lavorazione/quiz/colori/quiz.html`. Screenshot in `lavorazione/quiz/colori/`. PR in bozza; merge e pubblicazione in attesa di approvazione dell’anteprima corrente secondo AGENTS.md §1.
