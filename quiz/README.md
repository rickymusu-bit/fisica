# Quiz di Stringhe — specifiche v2.5.0

**Stato:** archivio approvato di 300 quesiti di Termologia, 100 per livello. Introduzione alla fisica e alla misura resta non disponibile perché priva di domande.
**Data:** 25 ottobre 2026 (Europe/Rome).

## Comportamento

- Una sessione riguarda **una sola categoria**: attualmente **Termologia** oppure **Introduzione alla fisica e alla misura**.
- Scelta tramite pulsanti radio: selezionare una categoria deseleziona l’altra. Nessuna selezione di capitoli e nessuna combinazione di categorie nella stessa sessione.
- Le categorie senza domande per la difficoltà selezionata appaiono disabilitate con «Non disponibile». Se il cambio di difficoltà rende indisponibile la categoria scelta, questa viene deselezionata e l’avvio resta disabilitato fino a una nuova scelta.
- Il registro `quiz/categorie.json` associa ID stabili ai nomi delle categorie del catalogo corrente. La build rifiuta discrepanze, ID duplicati o categorie sconosciute. Una rinomina della categoria aggiorna la corrispondenza nel registro conservando l’ID; rinominare un capitolo non modifica i quesiti.
- L'utente seleziona da **1 a 30 domande**, con **25** inizialmente proposte, tramite campo numerico modificabile e pulsanti **−** e **+** ai lati. I pulsanti variano la quantità di una unità, sono disabilitati agli estremi, e la durata massima si aggiorna immediatamente prima dell'avvio: 2 minuti per domanda (30 domande = 60 minuti).
- **Quattro alternative per ogni domanda**, a tutti i livelli: facile, medio e difficile.
- Il limite di **120 secondi per domanda** è uguale a tutti i livelli. La difficoltà cambia le operazioni richieste, non il tempo o il numero delle opzioni. Il timer della singola domanda rimane nascosto.
- Il browser gestisce internamente una scadenza per ciascuna domanda. Lo studente vede soltanto il tempo totale rimanente. Quando scade il tempo della domanda, questa viene lasciata senza risposta e si passa alla successiva.
- Durante il quiz compare una griglia numerata da 1 al numero selezionato: indica **risposta data** (confermata), **saltata** (pulsante o scadenza), **corrente** e **da affrontare**, con colori, simboli e nomi accessibili. Le scelte ancora non confermate non contano come risposte date.
- Il riepilogo finale ripropone la griglia: distingue le domande saltate da quelle non raggiunte, ad esempio per chiusura anticipata. Le risposte, le soluzioni e le spiegazioni sono riportate per ogni domanda.
- La griglia è un indicatore, non permette di riaprire domande: ciascun quesito mantiene la propria scadenza. Le saltate sono segnalate in giallo, senza marrone; la domanda corrente ha un bordo di 4 px.
- **Salta** e **Conferma e prosegui** sono affiancati; **Concludi** è sul lato opposto (su mobile in una riga distinta, allineato a destra), in rosso lampone scuro. La conclusione anticipata richiede conferma.
- Il conteggio procede anche cambiando scheda o mettendo l'app in background: al ritorno vengono applicate le scadenze trascorse. Il tempo non è garantito contro manipolazioni intenzionali dell'orologio o del JavaScript locale.
- Dopo l'ultima domanda, alla scadenza totale o alla conclusione anticipata si mostra il risultato come **risposte corrette / domande totali**, oltre agli errori, alle omissioni e alla revisione completa con spiegazioni.
- Le opzioni sono mescolate, così come i quesiti estratti. La risposta non è svelata prima della schermata finale.
- Nessun backend necessario. Non si considera prioritario impedire l'accesso al dataset lato client.

## Notazione di variabili e formule

Domande, alternative e correzione finale usano pedici e apici HTML nativi, come i capitoli: per esempio c<sub>acqua</sub>, T<sub>amb</sub><sup>4</sup> e 10<sup>−5</sup>. La resa conserva font e proporzioni del tema, senza librerie o dipendenze di rete.

I record restano stringhe di testo: `c_acqua` o `c_{acqua}` indicano il pedice, mentre apici e pedici numerici Unicode e potenze come `T^4` sono trasformati solo nella visualizzazione. Il motore costruisce nodi di testo, `sub` e `sup`, senza interpretare HTML nel dataset o nei salvataggi. Gli underscore non compaiono nei contenuti scientifici mostrati.

La stessa formattazione si applica alle sessioni e ai risultati recuperati dai salvataggi precedenti: non cambia versione, contenuto, ordine delle opzioni, indici corretti, risposte o scadenze.

## Salvataggio e ripresa della sessione

Il browser salva automaticamente il quiz sul dispositivo all’avvio e a ogni scelta, conferma, salto o cambio di domanda, oltre che all’uscita dalla pagina. Non scrive il timer ogni secondo: conserva gli istanti di scadenza originali.

Ricaricando la pagina, tornando indietro o riaprendola nello stesso browser/profilo, il quiz riprende automaticamente con gli stessi quesiti, ordine delle alternative, risposte confermate, domanda corrente e scelta non ancora confermata. Una scelta provvisoria resta distinta da una risposta data.

Il tempo trascorso fuori dalla pagina viene conteggiato: le domande scadute vengono saltate; se è scaduto l’intero quiz, compare il risultato. Anche il risultato viene salvato e recuperato, fino al comando **Nuovo quiz**, che cancella la sessione conservata. Non avviene un nuovo sorteggio durante il recupero, neppure se l’archivio del sito è cambiato: il salvataggio contiene i quesiti effettivamente estratti.

Viene conservato un solo quiz per indirizzo della pagina e profilo del browser. Le schede aperte sullo stesso indirizzo condividono la sessione. Il salvataggio è locale (`localStorage`), senza backend; non segue lo studente su altri dispositivi o browser. La cancellazione dei dati del sito o la chiusura di una sessione privata può eliminarlo. Non costituisce protezione contro modifiche intenzionali dei dati locali.

Se il salvataggio non è disponibile o lo spazio è esaurito, un avviso visibile spiega di non chiudere o ricaricare la pagina; il quiz continua in memoria. In questo caso viene richiesto al browser un avviso di uscita durante il quiz, senza garantirne la comparsa su ogni dispositivo. Le sessioni precedenti già avviate mantengono le proprie alternative e scadenze fino alla conclusione; ogni nuovo quiz usa quattro alternative. Un salvataggio corrotto o di versione incompatibile viene rimosso con un messaggio, senza bloccare la pagina.

## Generazione delle domande

Il [prompt di generazione](PROMPT_GENERAZIONE_DOMANDE.md), v1.4.2, definisce domande di conoscenza, ragionamento e calcolo, tre difficoltà e fattibilità entro 120 secondi comprensivi di lettura e scelta. Un quesito può collegare più capitoli della stessa categoria. Non deve richiedere conoscenze di un’altra categoria, salvo prerequisiti di base dichiarati o informazioni sufficienti fornite nel testo.

Il workflow parte da un campione di 9 domande in ChatGPT (una per ogni combinazione tipo/difficoltà, se pertinente), seguito dalla revisione e approvazione del docente. Codex usa prompt, capitoli e campione approvato per generare i lotti richiesti, verificarli e integrarli. I lotti richiedono revisione didattica; i controlli automatici non provano chiarezza e risolvibilità nei due minuti. La divisione è organizzativa, non una garanzia di superiorità scientifica di ChatGPT.

La scelta della categoria unica sostituisce la precedente proposta di tag multipli, filtro AND e classificazione dei contenuti dei capitoli. Non è necessario adattare i singoli HTML per aggiungere tag o ID di argomento.

### Target di produzione

**100 domande facili, 100 medie e 100 difficili per ogni categoria**: 300 per categoria, quindi **600 complessive** per le due categorie attuali. Distribuzione indicativa per ciascun livello: 30 conoscenza, 40 ragionamento, 30 calcolo, adattabile ai contenuti.

Produzione: campione iniziale di 9 domande, revisione del docente e lotti indicativamente da 30 fino al raggiungimento del target con quesiti approvati. Il campione approvato può essere incluso nel totale senza duplicazioni. Restano il limite di 120 secondi, la varietà dei contenuti e il divieto di riempire la quota con domande ripetitive o artificiose. Il target riguarda l’archivio; le sessioni rimangono da 1 a 30 domande.

## Archivio di domande

La sorgente corrente è **quiz/domande.json**, separata dall’interfaccia: contiene 300 quesiti approvati di Termologia (100 per livello, con ripartizione 30 conoscenza, 40 ragionamento e 30 calcolo in ciascun livello). Finché il file manca, la build genera una lista di domande vuota: tutte le categorie sono disabilitate e il quiz non è avviabile. L'archivio dimostrativo è stato cancellato dal repository. Ogni record contiene:

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
- `scripts/build_pages.py`: copia degli asset nel sito costruito.

La build incorpora l’archivio corrente senza richieste di rete durante il quiz. Le modifiche future richiedono revisione didattica e il workflow di anteprima e pubblicazione previsto dal progetto.

## Verifica

```sh
python3 scripts/build_pages.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/verify_quiz_browser.py
```

