# Stato — quiz

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

Approvazione ricevuta: implementare la semplificazione a categoria unica nell’ambito dell’incarico corrente. Nessuna approvazione di merge o pubblicazione. Verifiche e anteprima: vedere il rapporto `verifica-categoria-unica.md`. Prossimo passo: revisione dell’anteprima e approvazione prima di integrare main.
