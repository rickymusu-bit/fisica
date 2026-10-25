# Campione quiz — Introduzione alla fisica e alla misura

**Versione:** v2.1.0  
**Data:** 25 ottobre 2026 (Europe/Rome)  
**Stato:** il campione iniziale di 9 domande è stato approvato dal docente il 25/10/2026. Ulteriori 291 domande generate in lotti sono in attesa di revisione didattica. La PR in bozza contiene il file ufficiale proposto `quiz/domande/introduzione_fisica_misura.json`, non pubblicato.

## Fonti e ambito

Categoria `introduzione_fisica_misura`. Percorso di riferimento: `lavorazione/introduzione_fisica_misura/piano.md` (nove capitoli); schema dati e workflow: `quiz/README.md` e `quiz/PROMPT_GENERAZIONE_DOMANDE.md` v1.4.4. Prima dell'approvazione confrontare ogni quesito con il testo corrente dei nove capitoli pubblicati.

Le nove proposte di `campione.json` hanno una sola risposta corretta, quattro alternative e un tempo-obiettivo inferiore a 120 secondi. Stime editoriali, **non tempi osservati**.

| ID | Tipo | Livello | Principio / capitolo prevalente | Prerequisiti | Tempo stimato |
|---|---|---|---|---|---:|
| intro-001 | Conoscenza | Facile | Ipotesi verificabile; metodo scientifico | Specifico: previsioni e verifica | 35 s |
| intro-002 | Ragionamento | Facile | Risoluzione degli strumenti | Specifico: graduazioni e misura | 45 s |
| intro-003 | Calcolo | Facile | Conversioni SI | Specifico: metro e centimetro | 35 s |
| intro-004 | Conoscenza | Medio | Precisione e accuratezza | Specifico: confronto tra misure | 50 s |
| intro-005 | Ragionamento | Medio | Controllo delle variabili | Specifico: metodo sperimentale | 55 s |
| intro-006 | Calcolo | Medio | Conversioni di aree | Trasversale: prefissi, unità derivate | 65 s |
| intro-007 | Conoscenza | Difficile | Scostamento sistematico e dispersione | Trasversale: incertezza, strumenti | 65 s |
| intro-008 | Ragionamento | Difficile | Proporzionalità inversa | Specifico: relazioni tra grandezze | 65 s |
| intro-009 | Calcolo | Difficile | Media e semidispersione | Specifico: misure ripetute | 90 s |

## Revisione didattica

Controllare: correttezza fisica e matematica, livello reale degli studenti, distrattori, coerenza con le dispense pubblicate, notazione, chiarezza delle condizioni e fattibilità in due minuti. Le spiegazioni sono destinate alla correzione finale. I livelli sono proposte da calibrare.

**Il campione è approvato.** L'approvazione non si estende automaticamente alle 291 domande successive. Non effettuare merge o pubblicazione prima dell'autorizzazione finale e della verifica dei test.

## Archivio completo v2.0.0

- Campione: `campione.json` — 9 domande approvate.
- Lotti: `lotti/*.json` — 291 domande generate.
- Archivio introduttivo: `archivio.json` — 300 domande (100 facili, 100 medie, 100 difficili).
- Integrazione proposta: due JSON distinti in `quiz/domande/`, uno per categoria da 300 domande. Il file monolitico è stato ritirato; il quiz usa un manifest compatto e carica il file richiesto solo all'avvio.
- Revisione: `revisione.json` — tipi, fonti, prerequisiti e tempi stimati preliminari.
- Controlli tecnici: `scripts/test_quiz_introduzione.py`; test di integrazione e browser aggiornati.

Controllo delle dimensioni e dello schema eseguito sui dati GitHub; i test Python/browser e la revisione dei contenuti attendono un'esecuzione effettiva. I nuovi quesiti di calcolo sono più numerosi della ripartizione indicativa 30/40/30: la distribuzione va valutata rispetto ai nove capitoli e alla varietà didattica, senza forzare etichette o inventare quesiti per raggiungere una quota.
