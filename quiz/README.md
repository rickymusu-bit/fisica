# Quiz di Stringhe — specifiche v1.3.0

**Stato:** prototipo funzionante con archivio di prova, non approvato per pubblicazione e non adatto a verifiche valutative.  
**Data:** 24 ottobre 2026 (Europe/Rome).

## Comportamento

- Selezione tramite caselle di controllo di singoli capitoli, anche appartenenti a categorie differenti.
- La casella di una categoria seleziona/deseleziona tutti i suoi capitoli; se ne sono scelti soltanto alcuni, mostra lo stato parziale.
- Le categorie e i titoli dei capitoli derivano dal catalogo corrente del sito: nessun elenco parallelo da aggiornare.
- L'utente seleziona da **1 a 30 domande**, con **25** inizialmente proposte. La durata massima si aggiorna prima dell'avvio e corrisponde a 2 minuti per ciascuna domanda (30 domande = 60 minuti).
- **Facile:** 3 alternative.
- **Media:** 4 alternative.
- **Difficile:** 5 alternative.
- Il limite di **120 secondi per domanda** è uguale a tutti i livelli. Cambiano difficoltà e numero delle opzioni, non il tempo. Il timer della singola domanda rimane nascosto.
- Il browser gestisce internamente una scadenza per ciascuna domanda. Lo studente vede soltanto il tempo totale rimanente. Quando scade il tempo della domanda, questa viene lasciata senza risposta e si passa alla successiva.
- Durante il quiz compare una griglia numerata da 1 al numero selezionato: indica **risposta data** (confermata), **saltata** (pulsante o scadenza), **corrente** e **da affrontare**, con colori, simboli e nomi accessibili. Le scelte ancora non confermate non contano come risposte date.
- Il riepilogo finale ripropone la griglia: distingue le domande saltate da quelle non raggiunte, ad esempio per chiusura anticipata. Le risposte, le soluzioni e le spiegazioni sono riportate per ogni domanda.
- La griglia è un indicatore, non permette di riaprire domande: ciascun quesito mantiene la propria scadenza. Le saltate sono segnalate in giallo, senza marrone; la domanda corrente ha un bordo di 4 px.
- **Salta** e **Conferma e prosegui** sono affiancati; **Concludi** è sul lato opposto (su mobile in una riga distinta, allineato a destra), in rosso lampone scuro. La conclusione anticipata richiede conferma.
- Il conteggio procede anche cambiando scheda o mettendo l'app in background: al ritorno vengono applicate le scadenze trascorse. Il tempo non è garantito contro manipolazioni intenzionali dell'orologio o del JavaScript locale.
- Dopo l'ultima domanda, alla scadenza totale o alla conclusione anticipata si mostra il risultato come **risposte corrette / domande totali**, oltre agli errori, alle omissioni e alla revisione completa con spiegazioni.
- Le opzioni sono mescolate, così come i quesiti estratti. La risposta non è svelata prima della schermata finale.
- Nessun backend necessario. Non si considera prioritario impedire l'accesso al dataset lato client.

## Archivio di domande

La sorgente è **quiz/domande-prova.json**, separata dall'interfaccia. Ogni record contiene:

\`id\`, \`chapter\` (filename HTML pubblicato), \`level\` (\`easy\`, \`medium\`, \`hard\`), \`prompt\`, \`options\`, \`correct\` (indice dell'alternativa corretta a partire da zero), \`explanation\`.

La build controlla che gli ID siano unici, che il capitolo sia pubblicato, che il numero di alternative coincida con il livello e che la risposta corretta sia valida. Il dataset è incorporato in \`_site/quiz.html\` durante la build, senza richiesta di rete, ma resta un file indipendente nei sorgenti.

**Limite del prototipo:** 45 domande, una per ciascuno dei 15 capitoli attuali e per livello; se le domande disponibili non arrivano al numero selezionato, il motore le riutilizza fino al numero richiesto, mescolando l'ordine. Questa soluzione serve **solo per provare il flusso** e andrà rimossa quando l'archivio definitivo garantirà una quantità sufficiente di domande distinte per ciascuna selezione ammessa. Per verifiche scolastiche servono più quesiti indipendenti, correttezza scientifica verificata e varianti autenticamente equivalenti, non semplici sostituzioni numeriche.

## Struttura

- \`scripts/quiz_site.py\`: costruzione della pagina con capitoli dal catalogo.
- \`quiz/interfaccia.css\`: stile coerente con i token comuni di Stringhe.
- \`quiz/interfaccia.js\`: sessione, estrazione, scadenze, punteggio, correzione.
- \`scripts/strings_site.py\`: integrazione della pagina nel portale.
- \`scripts/build_pages.py\`: copia degli asset nel sito costruito.

La pagina è generata e provabile su un ramo dedicato; **non integrare in main e non pubblicare su GitHub Pages senza approvazione dell'anteprima corrente**.

## Verifica

\`\`\`sh
python3 scripts/build_pages.py
python3 -m unittest discover -s scripts -p 'test_*.py'
\`\`\`
