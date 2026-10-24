# Quiz di Stringhe — requisiti funzionali (v1)
Data: 24 ottobre 2026. Stato: prototipo da approvare.

## Selezione
- L'utente seleziona uno o più capitoli tramite checkbox, anche appartenenti a categorie differenti.
- La checkbox della categoria seleziona o deseleziona tutti i capitoli di quella categoria. In presenza di una selezione parziale, il controllo mostra lo stato indeterminato.
- I titoli e le categorie provengono dal catalogo pubblico ammesso in `pubblicazione.json`; non dal repository del gioco Fool.

## Domande
- Ogni sessione comprende esattamente 25 domande a scelta multipla, numero non modificabile.
- Estrazione casuale senza ripetizioni e distribuzione fra i capitoli selezionati.
- Facile: 3 alternative, massimo 150 secondi per domanda.
- Medio: 4 alternative, massimo 120 secondi per domanda.
- Difficile: 5 alternative, massimo 90 secondi per domanda.
- È visibile soltanto il tempo totale rimanente della sessione; il timer della singola domanda resta interno.
- Una domanda senza risposta allo scadere passa automaticamente alla successiva. Il tempo risparmiato su una domanda non si accumula.
- A fine quiz o allo scadere: voto, numero corrette/errate/non risposte e correzione di tutte le domande con soluzione.
- Regola di valutazione provvisoria per l'interfaccia: 1 punto per risposta corretta, 0 per errore o omissione, voto = 10 × corrette/25, con un decimale. Da confermare prima della versione definitiva.

## Architettura
- Pagina integrata in Stringhe usando tema e navigazione comuni.
- Sorgente dei quesiti separato dall'interfaccia, schema `{id,capitolo,livello,testo,opzioni,corretta,spiegazione}`.
- `quiz/domande-prova.json` è **soltanto dimostrativo** (schemi ripetitivi generati automaticamente per testare le interazioni), non un dataset validato.
- La versione statica HTML/JS non protegge la segretezza dell'intero archivio, anche se si presentano solo 25 domande: una protezione reale richiede backend con selezione e correzione server-side.
- Accessibilità: controlli nativi, tema chiaro/scuro, dimensioni touch, contrasto, indicatori di focus.
- Nessun merge in `main` e nessuna pubblicazione Pages senza nuova approvazione dell'anteprima.
