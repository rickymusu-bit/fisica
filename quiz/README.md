# Quiz di Stringhe — specifiche v1.6.1

**Stato:** interfaccia pubblicabile senza archivio di quesiti; il quiz rimane disabilitato fino al caricamento di domande reali.  
**Data:** 24 ottobre 2026 (Europe/Rome).

## Comportamento

- Selezione tramite caselle di controllo di singoli capitoli, anche appartenenti a categorie differenti.
- I capitoli senza quesiti nel dataset per la **difficoltà selezionata** sono visibili ma non selezionabili, con indicazione «Non disponibile». Le categorie prive di qualunque capitolo con quesiti sono disabilitate. Il selettore di categoria riguarda solo i capitoli disponibili e mantiene correttamente il proprio stato completo/parziale. Se cambiando difficoltà un capitolo non ha più domande, viene deselezionato automaticamente.
- La casella di una categoria seleziona/deseleziona tutti i suoi capitoli; se ne sono scelti soltanto alcuni, mostra lo stato parziale.
- Le categorie e i titoli dei capitoli derivano dal catalogo corrente del sito: nessun elenco parallelo da aggiornare.
- L'utente seleziona da **1 a 30 domande**, con **25** inizialmente proposte, tramite campo numerico modificabile e pulsanti **−** e **+** ai lati. I pulsanti variano la quantità di una unità, sono disabilitati agli estremi, e la durata massima si aggiorna immediatamente prima dell'avvio: 2 minuti per domanda (30 domande = 60 minuti).
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

## Generazione delle domande

Il [prompt di generazione](PROMPT_GENERAZIONE_DOMANDE.md), versione v1.1.0, definisce quesiti di conoscenza, ragionamento e calcolo, tre difficoltà e fattibilità entro 120 secondi, compresa la lettura. Distingue quesiti specifici e trasversali, indipendentemente dalla difficoltà.

**Workflow concordato:** ChatGPT prepara un campione iniziale di 9 quesiti (tre tipologie per tre difficoltà, se pertinenti); il docente lo rivede e approva; Codex usa prompt, capitoli e campione approvato per i lotti successivi, i controlli e l’integrazione. I lotti restano soggetti a revisione didattica. Questa divisione è organizzativa: non presume che ChatGPT sia scientificamente superiore a Codex. I controlli automatici non dimostrano chiarezza, adeguatezza o rispetto dei due minuti per gli studenti.

### Tag e selezione: requisito da implementare

Ogni quesito ha uno o più tag che rappresentano tutti gli argomenti necessari alla soluzione. Il filtro usa la condizione **AND**: include una domanda soltanto se **tutti** i suoi tag sono selezionati. Per esempio, una domanda con i tag “energia cinetica” e “calore specifico” è esclusa quando viene selezionato uno solo dei due; è inclusa quando sono selezionati entrambi, anche insieme ad altri argomenti.

I tag non descrivono semplici ambientazioni o oggetti. La selezione dei capitoli può rimanere invariata nell’interfaccia ed essere tradotta nell’insieme dei tag corrispondenti.

Lo schema attuale con un solo campo `chapter` richiederà un adeguamento prima di importare quesiti trasversali. Occorrerà allineare schema, validatore, estrazione e disponibilità dei quesiti alla condizione su tutti i tag. Queste sono specifiche documentali: il filtro multiplo e il nuovo schema non sono implementati da questa revisione.

## Archivio di domande

Quando sarà disponibile, la sorgente sarà **quiz/domande.json**, separata dall'interfaccia. Finché il file manca, la build genera una lista di domande vuota: tutte le caselle dei capitoli e categorie sono disabilitate e il quiz non è avviabile. L'archivio dimostrativo è stato cancellato dal repository. Ogni futuro record conterrà:

\`id\`, \`chapter\` (filename HTML pubblicato), \`level\` (\`easy\`, \`medium\`, \`hard\`), \`prompt\`, \`options\`, \`correct\` (indice dell'alternativa corretta a partire da zero), \`explanation\`.

La build controlla che gli ID siano unici, che il capitolo sia pubblicato, che il numero di alternative coincida con il livello e che la risposta corretta sia valida. Il dataset è incorporato in \`_site/quiz.html\` durante la build, senza richiesta di rete, ma resta un file indipendente nei sorgenti.

**Verifica:** i test automatici generano un piccolo insieme temporaneo di domande durante l'esecuzione, senza salvarlo né pubblicarlo nel sito. Il motore oggi può ripetere domande quando il numero selezionato supera le domande realmente disponibili: questa funzionalità andrà valutata prima di usare i quiz come verifiche scolastiche.

## Struttura

- \`scripts/quiz_site.py\`: costruzione della pagina con capitoli dal catalogo.
- \`quiz/interfaccia.css\`: stile coerente con i token comuni di Stringhe.
- \`quiz/interfaccia.js\`: sessione, estrazione, scadenze, punteggio, correzione.
- \`scripts/strings_site.py\`: integrazione della pagina nel portale.
- \`scripts/build_pages.py\`: copia degli asset nel sito costruito.

L'interfaccia può essere pubblicata anche senza quesiti. L'aggiunta di domande reali richiederà l'archivio quiz/domande.json e una nuova build.

## Verifica

\`\`\`sh
python3 scripts/build_pages.py
python3 -m unittest discover -s scripts -p 'test_*.py'
\`\`\`
