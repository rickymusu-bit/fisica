# Prompt per generare le domande dei quiz di Stringhe

**Versione:** v1.4.4
**Data:** 25 ottobre 2026 (Europe/Rome).
**Ambito:** quiz del sito Stringhe, distinti dal gioco Fool.

Questo documento è il prompt riutilizzabile per generare quesiti per un quiz su una sola categoria del sito. Compilare i parametri e applicare tutte le istruzioni seguenti. Le specifiche dell’interfaccia e dell’archivio sono in [README.md](README.md).

## Parametri della richiesta

- Categoria unica: [ID definito in `quiz/categorie.json`].
- Materiale di riferimento: [link o file].
- Destinatari: [livello scolastico; normalmente biennio della scuola secondaria di secondo grado].
- Numero di domande del lotto: [numero; target complessivo nella sezione 10].
- Distribuzione per tipo: [conoscenza %, ragionamento %, calcolo %].
- Distribuzione per difficoltà: [facili %, medie %, difficili %].
- Ampiezza didattica: [quesiti su un solo argomento / quesiti che collegano più argomenti della stessa categoria / entrambi].
- Prerequisiti aggiuntivi consentiti: [elenco oppure “nessuno oltre a quelli presenti nel materiale”].
- Strumenti consentiti: [normalmente calcolatrice di base].
- Formato della consegna: [revisione didattica / archivio compatibile con il sito].

Se le distribuzioni non sono indicate, proponi come punto di partenza 30% conoscenza, 40% ragionamento e 30% calcolo, adattandole alle possibilità dell’argomento. Questa distribuzione è un suggerimento, non una quota obbligatoria. Esplicita le quantità intere risultanti.

## 1. Analisi del materiale

Leggi il materiale prima di generare le domande. Individua concetti, leggi, formule, condizioni di validità e competenze effettivamente affrontati. Seleziona soltanto i contenuti della categoria richiesta e leggi i capitoli pubblicati che la compongono.

Se non puoi accedere al materiale, segnalalo e chiedimi di fornirlo. Non attribuire al sito contenuti che non hai verificato.

Distribuisci i quesiti tra i contenuti della categoria evitando concentrazioni ingiustificate. Puoi indicare i capitoli consultati nella scheda di revisione come fonti didattiche; titoli e percorsi non sono chiavi dell’archivio delle domande.

## 2. Una sola categoria per ogni quiz

La categoria è l’intero ambito del quiz: per esempio Termologia oppure Introduzione alla fisica e alla misura. Non è possibile selezionare singoli capitoli o combinare categorie nella stessa sessione.

Ogni domanda è associata a un solo ID stabile di categoria, definito in `quiz/categorie.json`. L’ID resta invariato se cambiano il nome visibile della categoria o titoli e percorsi dei capitoli. Il registro collega gli ID alle categorie del catalogo corrente.

Non generare tag multipli di argomento e non richiedere la classificazione dei capitoli per contenuti. Questa soluzione sostituisce le precedenti proposte di filtro AND e mappatura dei prerequisiti per capitolo.

### Prerequisiti e ragionamento trasversale

Una domanda specifica richiede conoscenze di un solo argomento; una domanda trasversale collega più argomenti o principi della stessa categoria. Questa distinzione resta utile nella revisione didattica, ma non è un criterio tecnico di selezione.

La difficoltà è indipendente da questa distinzione: una domanda specifica può essere difficile e una trasversale facile. Conta i principi effettivamente necessari, non quelli semplicemente citati.

Non richiedere conoscenze disciplinari di un’altra categoria, salvo prerequisiti di base esplicitamente previsti. Se una situazione richiede una proprietà esterna, fornisci nel testo le informazioni sufficienti; altrimenti escludi il quesito dalla consegna. Non usare il livello difficile per introdurre conoscenze non previste.

Una situazione nuova può essere risolta anche con un solo principio studiato. Mantieni distinta la novità del contesto dall’ampiezza dei prerequisiti.

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

Presenta **4 alternative**.

### Medio

Richiede di scegliere il principio pertinente, collegare due idee o distinguere concetti vicini. Può richiedere un passaggio intermedio, una semplice conversione o la trasformazione di una formula. Nel ragionamento occorre confrontare casi o identificare le variabili rilevanti.

Presenta **4 alternative**.

### Difficile

Richiede di coordinare più idee o passaggi, valutare le condizioni di validità di un modello oppure distinguere effetti concorrenti. Il procedimento deve essere individuato dallo studente.

Nelle domande di conoscenza, la difficoltà deriva da distinzioni concettuali e condizioni di validità rilevanti. Nelle domande di ragionamento, la conclusione deve essere deducibile senza conoscenze esterne. Nei calcoli, usa più passaggi significativi ma brevi, evitando algebra inutilmente lunga.

Presenta **4 alternative**.

Non assegnare la difficoltà in base alla lunghezza del testo, al numero di alternative, a vocaboli insoliti o alla presenza di trabocchetti.

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

Presenta ogni dato nell’ordine **nome della grandezza a parole → simbolo → valore con unità**. Per esempio: «la massa del blocco è m = 0,20 kg» e «il calore specifico dell’acqua è c = 4200 J/(kg · K)». La sola descrizione a parole non sostituisce il simbolo: lo studente deve poterlo usare direttamente nell’impostazione. Se ci sono più grandezze dello stesso tipo, usa pedici opportuni e brevi, collegati esplicitamente al corpo, al materiale o allo stato: per esempio «le masse di acqua e ghiaccio sono m_a = … e m_g = …» oppure «le temperature iniziale e finale sono T_i = … e T_f = …». Quando la grandezza è unica, usa la sola lettera. Mantieni i simboli coerenti in domanda, alternative e spiegazione. Applica il criterio anche ai dati forniti come confronti o relazioni; non anticipare la risposta nei quesiti che chiedono proprio il significato di un simbolo. Dichiara le ipotesi quando la loro assenza permetterebbe risposte diverse. Non appesantire il testo con ipotesi irrilevanti.

Applica il principio di economia informativa del progetto: conserva ciò che serve a comprendere e risolvere il quesito; elimina ciò che ripete informazioni o non modifica la comprensione. Non eliminare dati, unità e condizioni necessari.

Usa notazione e matematica appropriate al livello previsto e alle regole correnti del repository. Per la temperatura usa T e ΔT; riserva t e Δt al tempo. Per i numeri molto piccoli o molto grandi usa la notazione scientifica a · 10ⁿ, con 1 ≤ |a| < 10, quando non è utile ricorrere ai prefissi SI. Usa i prefissi quando rendono i valori più leggibili, per esempio 144 kJ; conserva la notazione scientifica per coefficienti come α = 1,2 · 10⁻⁵ K⁻¹. Applica la stessa scelta a dati, opzioni e soluzioni. Pedici e apici devono essere resi tipograficamente in tutti i campi visualizzati, comprese alternative e spiegazioni: non lasciare underscore visibili. Nei sorgenti testuali il motore riconosce `c_a`, `c_{a}`, `T_a⁴` e le cifre Unicode in pedice/apice; conserva le stringhe del dataset e delega la resa a `sub` e `sup` nativi, come nei capitoli. Non inserire HTML eseguibile nei record.

## 7. Alternative di risposta

Ogni domanda presenta **esattamente quattro alternative**, indipendentemente dal livello: una sola corretta e tre distrattori.

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
- ID della categoria;
- argomenti e prerequisiti effettivamente utilizzati, con i capitoli consultati come riferimenti di revisione;
- tipo prevalente: conoscenza, ragionamento o calcolo;
- difficoltà;
- testo e alternative;
- risposta corretta;
- breve spiegazione della soluzione;
- prerequisiti utilizzati, distinguendo conoscenze richieste e informazioni fornite nel testo;
- una frase che giustifichi il livello di difficoltà;
- tempo di risoluzione stimato, non superiore a 120 secondi.

Le spiegazioni e le informazioni di classificazione sono destinate alla revisione e al feedback finale. Non devono svelare la risposta durante lo svolgimento.

## 10. Workflow ChatGPT, docente e Codex

### Target dell’archivio

Obiettivo concordato: **100 domande per ciascun livello di difficoltà e per ciascuna categoria**, quindi **300 domande per categoria**.

| Categoria | Facili | Medie | Difficili | Totale |
|---|---:|---:|---:|---:|
| Termologia | 100 | 100 | 100 | 300 |
| Introduzione alla fisica e alla misura | 100 | 100 | 100 | 300 |
| Totale attuale | 200 | 200 | 200 | 600 |

Come riferimento iniziale, ciascun livello comprende 30 domande di conoscenza, 40 di ragionamento e 30 di calcolo. Le proporzioni per tipo restano adattabili ai contenuti; il target di 100 per livello non giustifica duplicati, quesiti artificiosi o domande fuori ambito. Se non è raggiungibile con qualità adeguata, segnala lo scostamento senza riempire artificialmente la quota.

Dopo il campione iniziale di 9 domande e la revisione del docente, procedi in lotti indicativamente da 30 domande, con eventuale ultimo lotto ridotto. Le domande del campione possono concorrere al target se approvate e mantenute nell’archivio definitivo, senza duplicarle. Tieni il conteggio per categoria, livello e tipo distinguendo proposte, revisionate e approvate: il target è raggiunto con domande approvate.

Il target riguarda la dimensione dell’archivio, non la lunghezza di una sessione del quiz (che resta da 1 a 30 domande). Non avviare automaticamente la generazione di tutte le 600 domande: rispetta il lotto e la fase richiesti dall’utente.

### Fase 1 — Progettazione e campione in ChatGPT

Usa ChatGPT per discutere formulazioni, difficoltà, situazioni nuove, distrattori e valore didattico. Parti da un campione di **9 domande**, una per ciascuna combinazione tra le tre tipologie (conoscenza, ragionamento, calcolo) e le tre difficoltà (facile, medio, difficile), purché l’argomento permetta tutte le combinazioni. Segnala eventuali combinazioni non pertinenti senza forzarle.

Per ogni domanda presenta la scheda di revisione prevista nella sezione 9, con categoria e prerequisiti. Questo campione serve a calibrare lo stile e i livelli, non impone la stessa distribuzione ai lotti successivi.

### Fase 2 — Revisione del docente

Il docente valuta correttezza, chiarezza, distrattori, livello e plausibilità dei due minuti per i propri studenti. Applica le correzioni e conserva il campione approvato come riferimento insieme al prompt corrente. Non attribuire approvazioni non ricevute.

La revisione del campione calibra la generazione successiva; non approva automaticamente le domande ancora da produrre.

### Fase 3 — Generazione dei lotti con Codex

Codex legge i capitoli correnti nel repository, questo prompt e il campione effettivamente approvato. Genera i lotti richiesti rispettando categoria unica, distribuzioni e prerequisiti. Predispone l’archivio nel formato compatibile con il sito, tenendo separati i dati per la revisione quando lo schema non li supporta.

Prima dell’importazione, verifica che ogni domanda abbia un solo ID di categoria riconosciuto e che sia risolvibile con i contenuti di quella categoria e i prerequisiti dichiarati.

### Fase 4 — Controlli e revisione dei lotti

Codex verifica formato, ID univoci, categoria riconosciuta, numero di alternative, indice corretto, duplicati rilevabili e calcoli automatizzabili. Verifica che la scelta di categoria sia esclusiva e che una sessione non estragga mai domande di altre categorie o difficoltà. Verifica anche le categorie prive di domande e il cambio di difficoltà.

Il docente rivede il contenuto didattico prima dell’uso. Un controllo automatico può verificare un calcolo o un identificativo di categoria, ma non dimostra che una domanda sia chiara, ben calibrata o risolvibile dai propri studenti entro 120 secondi. La conferma dei tempi richiede l’uso effettivo.

### Fase 5 — Integrazione e verifica del sito

Codex prepara l’integrazione, controlla estrazione, opzioni, soluzioni e spiegazioni, e segue il workflow corrente del repository per ramo, PR, anteprima e pubblicazione. L’approvazione didattica non sostituisce le autorizzazioni previste per merge e deployment.

### Criterio di scelta dello strumento

La divisione tra ChatGPT per il confronto didattico e Codex per i lotti e l’integrazione è una scelta pratica di workflow. Non implica una superiorità scientifica o didattica automatica di ChatGPT. Anche Codex può generare domande: la qualità dipende dal modello utilizzato, dai materiali disponibili, dalle istruzioni e dalla revisione.

Non presumere che i due strumenti condividano automaticamente tutto il contesto. Salva nel repository prompt, campione approvato e decisioni necessarie alla ripresa, con percorsi stabili e cronologia Git.

## 11. Compatibilità con l’archivio del sito

Prima di produrre un archivio da importare, rileggi lo schema corrente in [README.md](README.md) e il validatore del progetto. Non inventare un formato incompatibile.

Alla data di questa versione, la destinazione prevista è `quiz/domande.json` e i campi del record sono:

- `id`: identificativo univoco;
- `category`: ID stabile di una sola categoria, definito in `quiz/categorie.json`;
- `level`: `easy`, `medium` o `hard`;
- `prompt`: testo della domanda;
- `options`: esattamente quattro alternative per tutti i livelli;
- `correct`: indice dell’alternativa corretta a partire da zero;
- `explanation`: spiegazione della soluzione.

Il campo `category` sostituisce il vecchio `chapter`. Non usare titoli, nomi dei file o tag multipli per classificare i record. Se si incontrano archivi nel vecchio schema, occorre una migrazione esplicita: il validatore rifiuta record con `chapter` o `tags`.

La scheda di revisione comprende metadati didattici ulteriori rispetto a questo schema. Non aggiungere automaticamente nuovi campi all’archivio o modificare il motore del quiz per salvarli: mantieni distinta la consegna di revisione dal dataset di importazione.

Questo prompt non autorizza a generare lotti non richiesti, inventare approvazioni o pubblicare il sito.

## 12. Manutenzione del prompt delle domande

**Politica di manutenzione e versionamento (MAJOR.MINOR.PATCH).** Per tutti i prompt canonici, a ogni modifica esegui una revisione incrementale delle sezioni coinvolte e dei loro rimandi: elimina duplicazioni, riferimenti obsoleti e prolissità senza modificare vincoli, comportamenti o autorizzazioni. PATCH indica correzioni compatibili, MINOR aggiunte compatibili, MAJOR modifiche incompatibili o riorganizzazioni sostanziali delle istruzioni. Prima di ogni aggiornamento MAJOR effettua un refactoring strutturale completo, ricontrollando organizzazione, sovrapposizioni, coerenza e dipendenze. Eseguilo anche su richiesta esplicita o quando problemi strutturali importanti lo richiedono, indipendentemente dalla versione. Il refactoring che preserva le regole non comporta di per sé un incremento MAJOR: scegli il livello in funzione dei cambiamenti effettivi. Presenta criticità e proposte prima del refactoring completo e richiedi approvazione per cambiamenti sostanziali; non risolvere autonomamente contraddizioni né fare merge o pubblicare senza autorizzazione. Non aumentare la versione una seconda volta per il solo refactoring. Le versioni sono indipendenti per documento e la cronologia Git conserva il passato. La nuova politica sostituisce le precedenti soglie numeriche fisse (ogni dieci versioni).

La manutenzione del prompt non autorizza nuovi lotti, modifiche all'archivio, merge o pubblicazione del sito.
