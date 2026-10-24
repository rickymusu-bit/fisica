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
