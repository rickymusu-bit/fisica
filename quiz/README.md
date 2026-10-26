# Quiz di Stringhe — specifiche v2.8.1

**Stato della PR in bozza:** archivio integrato di 600 quesiti, 300 per categoria e 100 per livello. I 300 quesiti di Termologia sono già approvati; per Introduzione alla fisica e alla misura il campione di 9 è stato approvato e i restanti 291 sono stati generati, in attesa di revisione didattica. Il sito pubblico resta invariato fino al merge autorizzato.
**Data:** 26 ottobre 2026 (Europe/Rome).

## Comportamento

- Una sessione riguarda **una sola categoria**: attualmente **Termologia** oppure **Introduzione alla fisica e alla misura**.
- Scelta tramite pulsanti radio: selezionare una categoria deseleziona l’altra. Nessuna selezione di capitoli e nessuna combinazione di categorie nella stessa sessione.
- I conteggi del manifest permettono di conoscere la disponibilità senza scaricare le domande. Le categorie senza domande per la difficoltà selezionata appaiono disabilitate con «Non disponibile». Se il cambio di difficoltà rende indisponibile la categoria scelta, questa viene deselezionata e l’avvio resta disabilitato fino a una nuova scelta.
- Il registro `quiz/categorie.json` associa ID stabili ai nomi delle categorie del catalogo corrente. La build rifiuta discrepanze, ID duplicati o categorie sconosciute. Una rinomina della categoria aggiorna la corrispondenza nel registro conservando l’ID; rinominare un capitolo non modifica i quesiti.
- L'utente seleziona da **1 a 30 domande**, con **25** inizialmente proposte, tramite campo numerico modificabile e pulsanti **−** e **+** ai lati. I pulsanti variano la quantità di una unità, sono disabilitati agli estremi, e la durata massima si aggiorna immediatamente prima dell'avvio: 2 minuti per domanda (30 domande = 60 minuti).
- **Quattro alternative per ogni domanda**, a tutti i livelli: facile, medio e difficile.
- Il tempo totale è **120 secondi × numero di domande**, uguale per tutti i livelli. Non ci sono scadenze o avanzamenti automatici per la singola domanda; la difficoltà cambia il contenuto, non la durata.
- Le alternative salvano subito la risposta. **Indietro** e **Avanti** consentono di consultare e modificare le risposte liberamente; il primo è disabilitato sulla prima domanda e il secondo sull’ultima. Lasciare una domanda senza risposta la segna come saltata.
- La barra di avanzamento misura le risposte date rispetto al totale: si aggiorna subito alla selezione, non aumenta saltando o consultando domande, non diminuisce tornando indietro e arriva al 100% quando tutte hanno una risposta.
- La matrice numerata è navigabile con pulsanti: blu per le risposte date, giallo per le saltate, neutro per le domande da affrontare. La domanda visualizzata ha sempre un bordo di 4 px in gradiente blu, anche se già risposta o saltata. Non vengono svelate soluzioni durante il quiz.
- Il riepilogo finale e le schede delle soluzioni usano verde per le risposte corrette, giallo per le saltate o non raggiunte, rosso per le errate. Il testo distingue le omissioni; restano conteggiate come errate nel punteggio.
- **Indietro** e **Avanti** sono affiancati; **Concludi** resta sul lato opposto e richiede conferma. **Ritorna al quiz** (focus iniziale) o Escape annullano; **Concludi** consegna. Il timer continua a scorrere anche con il dialog aperto.
- Il conteggio procede anche cambiando scheda o mettendo l'app in background: al ritorno vengono applicate le scadenze trascorse. Il tempo non è garantito contro manipolazioni intenzionali dell'orologio o del JavaScript locale.
- Raggiungere o rispondere all’ultima domanda non conclude il quiz. Solo la consegna esplicita o la scadenza totale mostrano punteggio e soluzioni.
- Le opzioni sono mescolate, così come i quesiti estratti. La risposta non è svelata prima della schermata finale.
- Nessun backend necessario. Non si considera prioritario impedire l'accesso al dataset lato client.

## Notazione di variabili e formule

Ogni dato del testo segue la regola **nome della grandezza → simbolo → valore con unità**, definita nel [prompt di generazione, §6](PROMPT_GENERAZIONE_DOMANDE.md#6-qualità-delle-domande). Le grandezze dello stesso tipo sono distinte con pedici brevi e spiegati nel contesto; una grandezza unica usa la sola lettera. La notazione resta coerente nelle soluzioni.

Domande, alternative e correzione finale usano pedici e apici HTML nativi, come i capitoli: per esempio c<sub>a</sub>, T<sub>a</sub><sup>4</sup> e 10<sup>−5</sup>. La resa conserva font e proporzioni del tema, senza librerie o dipendenze di rete.

I record restano stringhe di testo: `c_acqua` o `c_{acqua}` indicano il pedice, mentre apici e pedici numerici Unicode e potenze come `T^4` sono trasformati solo nella visualizzazione. Il motore costruisce nodi di testo, `sub` e `sup`, senza interpretare HTML nel dataset o nei salvataggi. Gli underscore non compaiono nei contenuti scientifici mostrati.

La stessa formattazione si applica alle sessioni e ai risultati recuperati dai salvataggi precedenti: non cambia versione, contenuto, ordine delle opzioni, indici corretti, risposte o scadenze.

## Salvataggio e ripresa della sessione

Il browser salva automaticamente il quiz a ogni scelta e cambio di domanda, oltre che all’uscita dalla pagina. Conserva la scadenza totale originale senza scrivere il timer ogni secondo.

Ricaricando la pagina o riaprendola nello stesso browser/profilo, il quiz riprende con gli stessi quesiti, ordine delle alternative, risposte salvate, domanda visualizzata e scadenza totale originale. Le scelte sono risposte immediate, modificabili fino alla consegna.

Il tempo trascorso fuori dalla pagina viene conteggiato sulla scadenza totale. Se è scaduto l’intero quiz, compare il risultato, conservato fino a **Nuovo quiz**. Non viene ripetuto il sorteggio durante il recupero.

Viene conservato un solo quiz per indirizzo della pagina e profilo del browser. Le schede aperte sullo stesso indirizzo condividono la sessione. Il salvataggio è locale (`localStorage`), senza backend; non segue lo studente su altri dispositivi o browser. La cancellazione dei dati del sito o la chiusura di una sessione privata può eliminarlo. Non costituisce protezione contro modifiche intenzionali dei dati locali.

Se il salvataggio non è disponibile o lo spazio è esaurito, un avviso visibile spiega di non chiudere o ricaricare la pagina; il quiz continua in memoria. In questo caso viene richiesto al browser un avviso di uscita durante il quiz, senza garantirne la comparsa su ogni dispositivo. Le sessioni precedenti mantengono quesiti, alternative e scadenza totale; la scelta provvisoria eventualmente presente diventa subito una risposta. I risultati già conclusi restano invariati. Ogni nuovo quiz usa quattro alternative. Un salvataggio corrotto o di versione incompatibile viene rimosso con un messaggio, senza bloccare la pagina.

## Generazione delle domande

Il [prompt di generazione](PROMPT_GENERAZIONE_DOMANDE.md), v1.5.1, definisce domande di conoscenza, ragionamento e calcolo, tre difficoltà e fattibilità entro 120 secondi comprensivi di lettura e scelta. Un quesito può collegare più capitoli della stessa categoria. Non deve richiedere conoscenze di un’altra categoria, salvo prerequisiti di base dichiarati o informazioni sufficienti fornite nel testo.

Il workflow parte da un campione di 9 domande in ChatGPT (una per ogni combinazione tipo/difficoltà, se pertinente), seguito dalla revisione e approvazione del docente. Codex usa prompt, capitoli e campione approvato per generare i lotti richiesti, verificarli e integrarli. I lotti richiedono revisione didattica; i controlli automatici non provano chiarezza e risolvibilità nei due minuti. La divisione è organizzativa, non una garanzia di superiorità scientifica di ChatGPT.

La scelta della categoria unica sostituisce la precedente proposta di tag multipli, filtro AND e classificazione dei contenuti dei capitoli. Non è necessario adattare i singoli HTML per aggiungere tag o ID di argomento.

### Target di produzione

**100 domande facili, 100 medie e 100 difficili per ogni categoria**: 300 per categoria, quindi **600 complessive** per le due categorie attuali. Distribuzione indicativa per ciascun livello: 30 conoscenza, 40 ragionamento, 30 calcolo, adattabile ai contenuti.

Produzione: campione iniziale di 9 domande, revisione del docente e lotti indicativamente da 30 fino al raggiungimento del target con quesiti approvati. Il campione approvato può essere incluso nel totale senza duplicazioni. Restano il limite di 120 secondi, la varietà dei contenuti e il divieto di riempire la quota con domande ripetitive o artificiose. Il target riguarda l’archivio; le sessioni rimangono da 1 a 30 domande.

## Archivio di domande per categoria

Le sorgenti ufficiali sono **`quiz/domande/termologia.json`** e **`quiz/domande/introduzione_fisica_misura.json`**: 300 quesiti per categoria, 100 per difficoltà. Il file aggregato `quiz/domande.json` è stato ritirato. Le 300 domande di Termologia restano approvate; per Introduzione alla fisica e alla misura il campione di 9 è approvato e le altre 291 sono proposte da revisionare. I lotti e l'archivio di lavorazione sono in `lavorazione/quiz/introduzione_fisica_misura/`. Finché il file manca, la build genera una lista di domande vuota: tutte le categorie sono disabilitate e il quiz non è avviabile. L'archivio dimostrativo è stato cancellato dal repository. Ogni record contiene:

`id`, `category` (un solo ID di `quiz/categorie.json`), `level` (`easy`, `medium`, `hard`), `prompt`, `options`, `correct` (indice da zero), `explanation`.

`category` sostituisce il precedente `chapter`: i quesiti non dipendono da titoli o nomi dei file dei capitoli. I record con `chapter`, `tags`, una categoria multipla o un ID sconosciuto sono rifiutati. L’archivio corrente usa già il formato per categoria unica.

La build controlla che gli ID siano unici, che la categoria sia valida, che ogni domanda abbia esattamente quattro alternative e che la risposta corretta sia valida. Il dataset è incorporato in `_site/quiz.html` durante la build, senza richiesta di rete, ma resta un file indipendente nei sorgenti.

**Verifica:** i test automatici generano un piccolo insieme temporaneo di domande durante l'esecuzione, senza salvarlo né pubblicarlo nel sito. Il motore può ripetere domande se la quantità richiesta supera quella disponibile; con 100 quesiti per livello e sessioni da 1 a 30, i quiz correnti di Termologia estraggono domande distinte. La categoria senza quesiti resta disabilitata.

## Struttura

- `quiz/categorie.json`: ID stabili e corrispondenza con le categorie del catalogo.
- `scripts/quiz_site.py`: costruzione della pagina con capitoli dal catalogo.
- `quiz/interfaccia.css`: stile coerente con i token comuni di Stringhe.
- `quiz/interfaccia.js`: sessione, estrazione, scadenze, punteggio, correzione.
- `scripts/strings_site.py`: integrazione della pagina nel portale.
- `scripts/build_pages.py`: copia degli asset e dei soli archivi di categoria presenti nel registro nel sito costruito.

La build incorpora l’archivio corrente senza richieste di rete durante il quiz. Le modifiche future richiedono revisione didattica e il workflow di anteprima e pubblicazione previsto dal progetto.

## Verifica

```sh
python3 scripts/build_pages.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/verify_quiz_browser.py
```


