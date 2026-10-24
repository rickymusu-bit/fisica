# Prompt per generare le domande dei quiz di Stringhe

**Versione:** v1.0.0  
**Data:** 24 ottobre 2026 (Europe/Rome).  
**Ambito:** quiz del sito Stringhe, distinti dal gioco Fool.

Questo documento è il prompt riutilizzabile per generare quesiti su un argomento, una categoria o un capitolo. Compilare i parametri e applicare tutte le istruzioni seguenti. Le specifiche dell’interfaccia e dell’archivio sono in [README.md](README.md).

## Parametri della richiesta

- Ambito: [argomento / categoria / capitolo].
- Materiale di riferimento: [link o file].
- Destinatari: [livello scolastico; normalmente biennio della scuola secondaria di secondo grado].
- Numero di domande: [numero].
- Distribuzione per tipo: [conoscenza %, ragionamento %, calcolo %].
- Distribuzione per difficoltà: [facili %, medie %, difficili %].
- Ambito dei prerequisiti: [quesiti specifici / quesiti trasversali / entrambi, con distribuzione desiderata].
- Prerequisiti aggiuntivi consentiti: [elenco oppure “nessuno oltre a quelli presenti nel materiale”].
- Strumenti consentiti: [normalmente calcolatrice di base].
- Formato della consegna: [revisione didattica / archivio compatibile con il sito].

Se le distribuzioni non sono indicate, proponi come punto di partenza 30% conoscenza, 40% ragionamento e 30% calcolo, adattandole alle possibilità dell’argomento. Questa distribuzione è un suggerimento, non una quota obbligatoria. Esplicita le quantità intere risultanti.

## 1. Analisi del materiale

Leggi il materiale prima di generare le domande. Individua concetti, leggi, formule, condizioni di validità e competenze effettivamente affrontati. Seleziona soltanto i contenuti pertinenti all’ambito richiesto.

Se non puoi accedere al materiale, segnalalo e chiedimi di fornirlo. Non attribuire al sito contenuti che non hai verificato.

Per una categoria, distribuisci i quesiti tra i capitoli pertinenti evitando concentrazioni ingiustificate. Associa ogni domanda a tutti i capitoli e agli argomenti necessari per risolverla. Un eventuale capitolo principale serve per l’organizzazione, ma non sostituisce l’elenco completo dei prerequisiti.

## 2. Ampiezza dei prerequisiti: quesiti specifici e trasversali

L’ampiezza dei prerequisiti è una dimensione distinta dal tipo di domanda e dalla difficoltà.

**Quesito specifico:** richiede conoscenze proprie di un solo argomento. Può utilizzare più concetti o relazioni interne a quell’argomento. Le abilità matematiche di base dichiarate non lo rendono automaticamente trasversale.

**Quesito trasversale:** richiede conoscenze appartenenti a più argomenti distinti, eventualmente distribuiti tra più capitoli o categorie. Elenca tutti i prerequisiti indispensabili e i capitoli corrispondenti.

Conta i principi effettivamente necessari alla soluzione, non quelli semplicemente citati nel contesto. Usare più principi non rende automaticamente il quesito trasversale: possono appartenere allo stesso argomento. Anche un unico capitolo può raccogliere più argomenti; verifica quindi il contenuto, senza classificare soltanto contando i file.

Un quesito trasversale non è automaticamente difficile: la difficoltà dipende dalle operazioni richieste. Un quesito specifico può essere difficile. Il limite di 120 secondi vale in entrambi i casi.

### Selezione dell’ambito

- Se viene richiesto un solo argomento o capitolo, genera quesiti risolvibili con le conoscenze incluse nell’ambito e con gli eventuali prerequisiti aggiuntivi esplicitamente consentiti.
- Se vengono richiesti più capitoli o una categoria, puoi generare anche quesiti trasversali tra gli argomenti compresi nell’ambito.
- Non introdurre implicitamente altri capitoli per ottenere quesiti più difficili. Se mancano prerequisiti, amplia l’ambito soltanto su indicazione dell’utente oppure escludi il quesito dalla consegna richiesta.
- Una situazione nuova non implica necessariamente conoscenze multiple: può essere risolta con un solo principio già studiato.
- Distingui le informazioni fornite nel testo dalle conoscenze che lo studente deve già possedere.

### Idoneità dei quesiti nel quiz

Un quesito è idoneo soltanto quando tutti i suoi prerequisiti disciplinari obbligatori sono compresi negli argomenti selezionati o tra i prerequisiti di base esplicitamente previsti. La presenza di un solo capitolo associato non basta.

Per esempio, una domanda che combina energia cinetica e riscaldamento di un corpo deve dichiarare entrambi gli argomenti e le relative conoscenze necessarie. Se viene selezionato soltanto il capitolo sul calore specifico, non deve essere proposta richiedendo implicitamente anche la conoscenza dell’energia cinetica.

Questa è una regola didattica e un requisito per la futura selezione dei quesiti; non affermare che il motore attuale la implementi senza verificarlo.

## 3. Tipo di domanda e difficoltà sono dimensioni distinte

Una domanda di conoscenza può essere difficile e una domanda di ragionamento può essere facile. Assegna il tipo prevalente in base all’operazione decisiva per risolverla. La presenza di numeri non rende automaticamente una domanda “di calcolo”.

### Conoscenza

Verifica la comprensione di definizioni, grandezze, unità, leggi e condizioni di validità. Evita di verificare il ricordo della formulazione letterale del testo o di dettagli marginali.

### Ragionamento

Richiedi di prevedere, confrontare, spiegare o dedurre una conseguenza fisica.

Includi situazioni che non compaiono direttamente nel materiale: esperimenti modificati, applicazioni nuove, confronti e casi ipotetici. La regola è: **contesto nuovo, principi già studiati**.

La soluzione deve derivare dai principi studiati e dalle informazioni contenute nella domanda. Se serve conoscere una proprietà particolare di un oggetto o materiale, dichiarala nel testo. Non richiedere nozioni esterne nascoste.

Non considerare sufficiente cambiare i nomi degli oggetti di un esempio già presente. Verifica un trasferimento effettivo delle conoscenze a una situazione diversa.

### Calcolo

Richiedi di ricavare una risposta quantitativa. Fornisci i dati e le costanti necessari e chiarisci le approssimazioni quando incidono sulla soluzione.

Privilegia la scelta e l’applicazione del modello fisico rispetto alla lunghezza dei conti. Consenti, salvo diversa indicazione, una calcolatrice di base.

## 4. Livelli di difficoltà

| Livello | Conoscenza | Ragionamento | Calcolo |
|---|---|---|---|
| Facile | Riconoscere un concetto fondamentale o il significato di una grandezza. | Individuare una conseguenza diretta di un principio, anche in una situazione nuova. | Applicare direttamente una relazione, con dati espliciti e unità coerenti. |
| Medio | Distinguere concetti vicini e riconoscere le condizioni di validità di una legge. | Collegare due idee o confrontare situazioni, individuando quali fattori contano. | Scegliere la relazione e svolgere una semplice trasformazione, conversione o passaggio intermedio. |
| Difficile | Riconoscere una formulazione rigorosa, un limite o una distinzione concettuale sottile ma rilevante. | Coordinare più principi, controllare le ipotesi o distinguere effetti concorrenti. | Impostare una soluzione con più passaggi brevi collegati, scegliendo autonomamente il procedimento. |

### Facile

Richiede un concetto fondamentale e un’applicazione diretta. Il percorso risolutivo è immediatamente riconoscibile. Nel ragionamento basta una deduzione diretta; nel calcolo basta applicare una relazione con dati espliciti e unità coerenti.

Presenta **3 alternative**.

### Medio

Richiede di scegliere il principio pertinente, collegare due idee o distinguere concetti vicini. Può richiedere un passaggio intermedio, una semplice conversione o la trasformazione di una formula. Nel ragionamento occorre confrontare casi o identificare le variabili rilevanti.

Presenta **4 alternative**.

### Difficile

Richiede di coordinare più idee o passaggi, valutare le condizioni di validità di un modello oppure distinguere effetti concorrenti. Il procedimento deve essere individuato dallo studente.

Nelle domande di conoscenza, la difficoltà deriva da distinzioni concettuali e condizioni di validità rilevanti. Nelle domande di ragionamento, la conclusione deve essere deducibile senza conoscenze esterne. Nei calcoli, usa più passaggi significativi ma brevi, evitando algebra inutilmente lunga.

Presenta **5 alternative**.

Non assegnare la difficoltà in base alla lunghezza del testo, al numero di alternative, a vocaboli insoliti o alla presenza di trabocchetti. Cinque alternative riducono la probabilità di indovinare, ma non rendono da sole difficile una domanda facile.

## 5. Vincolo di tempo: massimo 2 minuti per ogni domanda

Ogni domanda deve essere plausibilmente risolvibile entro **120 secondi** da uno studente del livello scolastico previsto che padroneggi i prerequisiti dichiarati. Il limite vale per tutte le tipologie e tutti i livelli di difficoltà, comprese le domande difficili.

I 2 minuti comprendono la lettura del testo e delle alternative, il ragionamento, gli eventuali calcoli e la scelta della risposta.

La difficoltà deve dipendere dalla qualità del ragionamento richiesto, dalla scelta del principio fisico o dalla distinzione concettuale da riconoscere. Mantieni contenuti il testo e il numero di passaggi operativi.

Una domanda difficile può richiedere un’intuizione o il collegamento tra più concetti, ma, una volta individuata la strada, deve consentire una soluzione breve. Evita catene lunghe di deduzioni, calcoli ripetitivi e confronti laboriosi tra le alternative.

Durante la revisione, stima prudentemente il tempo necessario allo studente, senza usare come riferimento la tua rapidità di soluzione. Se una domanda rischia di superare i 2 minuti, semplificala o sostituiscila, preservando la competenza da verificare.

Per ogni domanda indica, nei dati destinati alla revisione, il tempo di risoluzione stimato. La stima è orientativa e dovrà essere verificata con l’uso effettivo; non costituisce una misura osservata.

## 6. Qualità delle domande

Ogni domanda deve:

- avere una sola risposta corretta nelle condizioni indicate;
- contenere tutte le informazioni necessarie;
- usare un linguaggio chiaro, essenziale e fisicamente rigoroso;
- evitare precisazioni ovvie, ripetizioni e dettagli narrativi inutili;
- evitare ambiguità, doppie negazioni e domande ingannevoli;
- essere autonoma rispetto alle altre;
- verificare una competenza riconoscibile.

Dichiara le ipotesi quando la loro assenza permetterebbe risposte diverse. Non appesantire il testo con ipotesi irrilevanti.

Applica il principio di economia informativa del progetto: conserva ciò che serve a comprendere e risolvere il quesito; elimina ciò che ripete informazioni o non modifica la comprensione. Non eliminare dati, unità e condizioni necessari.

Usa notazione e matematica appropriate al livello previsto e alle regole correnti del repository. Per la temperatura usa T e ΔT; riserva t e Δt al tempo.

## 7. Alternative di risposta

Costruisci distrattori plausibili basati su errori reali: confusione tra grandezze, proporzionalità invertite, conversioni errate, applicazione impropria di una legge o intuizioni fisiche scorrette.

Evita alternative assurde, sovrapposte, “tutte le precedenti” e “nessuna delle precedenti”.

Mantieni le alternative omogenee per forma, precisione e lunghezza. Non rendere riconoscibile quella corretta attraverso indizi linguistici.

Distribuisci la posizione delle risposte corrette senza schemi prevedibili. Il successivo mescolamento delle opzioni nel sito non sostituisce la qualità dei distrattori.

## 8. Verifica prima della consegna

- Risolvi ogni domanda e verifica la risposta.
- Controlla calcoli, unità e arrotondamenti.
- Verifica che nessun distrattore sia corretto con un’interpretazione ragionevole.
- Controlla che i prerequisiti siano consentiti.
- Elimina duplicati e semplici riformulazioni della stessa domanda.
- Controlla la varietà dei concetti e delle operazioni richieste.
- Verifica la coerenza della classificazione per tipo e difficoltà.
- Verifica il rispetto del limite di 120 secondi, includendo lettura e scelta.

Per le domande di ragionamento, verifica esplicitamente che la novità riguardi la situazione proposta e che i principi necessari siano già disponibili.

Se il materiale non permette di raggiungere il numero richiesto con domande varie e valide, segnalalo senza colmare il numero con ripetizioni o contenuti fuori ambito.

I livelli assegnati sono stime iniziali: dopo l’uso in classe, i risultati degli studenti potranno aiutare a calibrarli.

## 9. Output per la revisione didattica

Per ogni domanda fornisci:

- identificativo;
- classificazione dei prerequisiti: specifico o trasversale;
- tutti gli argomenti e capitoli necessari, con eventuale capitolo principale;
- tipo prevalente: conoscenza, ragionamento o calcolo;
- difficoltà;
- testo e alternative;
- risposta corretta;
- breve spiegazione della soluzione;
- prerequisiti utilizzati, distinguendo conoscenze richieste e informazioni fornite nel testo;
- una frase che giustifichi il livello di difficoltà;
- tempo di risoluzione stimato, non superiore a 120 secondi.

Le spiegazioni e le informazioni di classificazione sono destinate alla revisione e al feedback finale. Non devono svelare la risposta durante lo svolgimento.

## 10. Compatibilità con l’archivio del sito

Prima di produrre un archivio da importare, rileggi lo schema corrente in [README.md](README.md) e il validatore del progetto. Non inventare un formato incompatibile.

Alla data di questa versione, la destinazione prevista è `quiz/domande.json` e i campi del record sono:

- `id`: identificativo univoco;
- `chapter`: nome del file HTML di un capitolo pubblicato;
- `level`: `easy`, `medium` o `hard`;
- `prompt`: testo della domanda;
- `options`: alternative, rispettivamente 3, 4 o 5;
- `correct`: indice dell’alternativa corretta a partire da zero;
- `explanation`: spiegazione della soluzione.

Lo schema attuale prevede un solo campo \`chapter\`: non è sufficiente, da solo, per rappresentare tutti i prerequisiti dei quesiti trasversali o garantirne l’estrazione corretta. Prima di importare questi quesiti occorrerà adeguare esplicitamente lo schema, il validatore e la selezione affinché controllino tutti i prerequisiti. Non appiattire un quesito trasversale su un solo capitolo rendendolo selezionabile senza le altre conoscenze necessarie.

La scheda di revisione comprende metadati didattici ulteriori rispetto a questo schema. Non aggiungere automaticamente nuovi campi all’archivio o modificare il motore del quiz per salvarli: mantieni distinta la consegna di revisione dal dataset di importazione.

La creazione di questo prompt non genera domande e non modifica timer, interfaccia, archivio o pubblicazione del sito.
