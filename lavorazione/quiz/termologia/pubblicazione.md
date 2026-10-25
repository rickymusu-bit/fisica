# Quiz di Termologia — integrazione e pubblicazione

25 ottobre 2026 (Europe/Rome). Richiesta dell’utente: «Va bene, pubblica», seguita da «Riprendi». Archivio completo approvato: 300 quesiti, 100 per livello; domande invariate rispetto alla produzione consegnata.

La sorgente attiva è `quiz/domande.json`, identica ad `archivio.json`. La build incorpora tutte le domande nella pagina senza richieste aggiuntive durante il quiz. Termologia è abilitata a ogni livello; l’altra categoria resta non disponibile. Le sessioni da 1 a 30 non ripetono domande nell’insieme corrente di 100 per livello.

## Anteprima corrente

- [Quiz HTML autonomo, con CSS, codice e domande incorporati](anteprima/quiz.html).
- Configurazione scura: [desktop](anteprima/config-1440-dark.png), [mobile](anteprima/config-390-dark.png).
- Configurazione chiara: [desktop](anteprima/config-1440-light.png), [mobile](anteprima/config-390-light.png).
- Quesito reale difficile: [desktop](anteprima/domanda-hard-1440.png), [mobile](anteprima/domanda-hard-390.png).
- [Risultato con soluzioni sul mobile](anteprima/risultato-hard-390.png).

L’anteprima proviene dalla build corrente e usa gli stessi componenti della pagina pubblicata. Gli screenshot sono stati controllati visivamente. Il mobile è emulato in Chromium; non si dichiara una prova su un telefono fisico. L’HTML funziona anche offline; i collegamenti alle altre pagine del sito richiedono accesso ai relativi documenti.

## Verifiche

Superati tema condiviso, crediti, build completa (24 HTML, 20 copertine), 24 test e validazione dell’archivio con i 78 ricalcoli. I test che presumevano l’assenza di domande sono stati aggiornati per confrontare la pagina generata con il dataset reale. La dicitura di indisponibilità futura è mostrata soltanto senza archivio; con domande reali si ricorda che soluzioni e spiegazioni appaiono alla fine.

`scripts/verify_quiz_browser.py` verifica l’archivio reale su desktop e mobile: tutti i livelli, 30 domande uniche per sessione desktop e 3 sul mobile, quattro opzioni, nessun quesito di categoria o livello diversi, punteggio corretto 30/30 e 3/3, tutte le spiegazioni finali, salvataggio/ripresa anche della scelta non confermata e recupero del risultato. Il rapporto [verifica-integrazione.json](verifica-integrazione.json) registra l’esito senza errori JavaScript. La suite già presente verifica anche categorie vuote, scadenze a pagina chiusa, storage bloccato, dati corrotti e salvataggi precedenti.

Il riepilogo usa un trattino al posto del punto centrato come separatore, conformemente alle regole comuni. Non cambiano regole, layout o funzionamento del quiz. Il manifest e i capitoli restano quelli di main `3d8afa2`, compresi i due capitoli appena pubblicati nell’altra categoria.

## Stato della distribuzione

Preparazione e verifiche locali concluse. L’anteprima è consegnata insieme agli screenshot; l’incarico corrente autorizza la pubblicazione di questo archivio approvato. Si attende l’esito della CI del commit finale prima di integrare la PR #81 e controllare il workflow Pages. L’esito remoto e l’indirizzo pubblico saranno registrati dopo la distribuzione.
