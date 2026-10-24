# Quiz di Stringhe — specifiche v1.0.0

**Stato:** prototipo funzionante con archivio di prova, non approvato per pubblicazione e non adatto a verifiche valutative.  
**Data:** 24 ottobre 2026 (Europe/Rome).

## Comportamento

- Selezione tramite caselle di controllo di singoli capitoli, anche appartenenti a categorie differenti.
- La casella di una categoria seleziona/deseleziona tutti i suoi capitoli; se ne sono scelti soltanto alcuni, mostra lo stato parziale.
- Le categorie e i titoli dei capitoli derivano dal catalogo corrente del sito: nessun elenco parallelo da aggiornare.
- Tutti i quiz contengono **25 domande a risposta multipla**, senza possibilità di modificare la quantità.
- **Facile:** 3 alternative e 150 secondi per domanda; massimo 62:30.
- **Media:** 4 alternative e 120 secondi per domanda; massimo 50:00.
- **Difficile:** 5 alternative e 90 secondi per domanda; massimo 37:30.
- Il browser gestisce internamente una scadenza per ciascuna domanda. Lo studente vede soltanto il tempo totale rimanente. Quando scade il tempo della domanda, questa viene lasciata senza risposta e si passa alla successiva.
- Il conteggio procede anche cambiando scheda o mettendo l'app in background: al ritorno vengono applicate le scadenze trascorse. Il tempo non è garantito contro manipolazioni intenzionali dell'orologio o del JavaScript locale.
- Dopo la venticinquesima domanda, alla scadenza totale o alla conclusione anticipata si mostrano voto in decimi (corrette × 10 / 25), risposte corrette, errate o omesse e revisione completa con spiegazione. La scala è provvisoria e da validare prima dell'uso valutativo.
- Le opzioni sono mescolate, così come i quesiti estratti. La risposta non è svelata prima della schermata finale.
- Nessun backend necessario. Non si considera prioritario impedire l'accesso al dataset lato client.

## Archivio di domande

La sorgente è **quiz/domande-prova.json**, separata dall'interfaccia. Ogni record contiene:

\`id\`, \`chapter\` (filename HTML pubblicato), \`level\` (\`easy\`, \`medium\`, \`hard\`), \`prompt\`, \`options\`, \`correct\` (indice dell'alternativa corretta a partire da zero), \`explanation\`.

La build controlla che gli ID siano unici, che il capitolo sia pubblicato, che il numero di alternative coincida con il livello e che la risposta corretta sia valida. Il dataset è incorporato in \`_site/quiz.html\` durante la build, senza richiesta di rete, ma resta un file indipendente nei sorgenti.

**Limite del prototipo:** 45 domande, una per ciascuno dei 15 capitoli attuali e per livello; se le domande disponibili non arrivano a 25, il motore le riutilizza fino al numero richiesto, mescolando l'ordine. Questa soluzione serve **solo per provare il flusso** e andrà rimossa quando l'archivio definitivo garantirà almeno 25 domande distinte per ciascuna selezione ammessa. Per verifiche scolastiche servono più quesiti indipendenti, correttezza scientifica verificata e varianti autenticamente equivalenti, non semplici sostituzioni numeriche.

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
