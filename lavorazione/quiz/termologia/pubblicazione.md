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

**Pubblicazione completata e verificata il 25 ottobre 2026.**

- CI del commit `2d54343d7db89e843ab6970ff6aa855cd9d03647`: [workflow 40169622838](https://github.com/rickymusu-bit/fisica/actions/runs/40169622838), concluso con successo, compresi la suite generale e il browser sull’archivio reale.
- [PR #81](https://github.com/rickymusu-bit/fisica/pull/81) integrata in main con commit `136cb6e200c8133e61b00690a22894cfa1f25030`, conservando gli aggiornamenti concorrenti di main.
- GitHub Pages: [workflow 40169937887](https://github.com/rickymusu-bit/fisica/actions/runs/40169937887), build e deployment conclusi con successo sullo stesso commit di merge.
- [Quiz pubblico](https://rickymusu-bit.github.io/fisica/quiz.html): HTTP 200; archivio servito identico ai 300 record approvati, con 100 facili, 100 medi e 100 difficili. JavaScript e CSS pubblici identici ai file verificati. Dettagli in [verifica-online.json](verifica-online.json).

L’anteprima autonoma è stata avviata anche senza richieste di rete mediante contenuto incorporato. Il browser gestito impedisce la navigazione diretta `file://`; questa limitazione dell’ambiente non riguarda la pagina pubblica, verificata via HTTPS. I controlli sui tempi restano stime progettuali, non prove osservate in classe.
