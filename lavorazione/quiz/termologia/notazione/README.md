# Pedici e apici nel quiz — anteprima

25 ottobre 2026. Correzione della visualizzazione richiesta dall’utente sul quesito con `c_acqua`; nessuna nuova pubblicazione.

- [Quiz HTML interattivo autonomo con tutte le 300 domande](quiz.html).
- Stesso quesito dello screenshot: [desktop scuro](pedici-1440-dark.png), [mobile scuro](pedici-390-dark.png), [320 px](pedici-320-dark.png).
- Tema chiaro: [desktop](pedici-1440-light.png), [mobile](pedici-390-light.png).
- [Soluzione finale sul mobile](soluzione-390.png).
- [Rapporto browser](verifica.json).

Le immagini mostrano la domanda termo-285 con c<sub>acqua</sub> anziché l’underscore. Le sessioni brevi dello screenshot servono a confrontare la tipografia; l’HTML completo conserva le sessioni configurabili da 1 a 30 e tutto l’archivio approvato.

I capitoli di energia interna e irraggiamento e il modello comune usano elementi HTML `sub` e `sup` con CSS, senza librerie matematiche esterne. Il quiz adotta gli stessi elementi e le proporzioni 0,65 per i pedici e 0,68 per gli apici. La correzione riguarda domanda, alternative, intestazione del quesito nel risultato, risposta data, soluzione e spiegazione. Le potenze e gli indici già scritti in Unicode vengono uniformati alla stessa resa.

L’archivio rimane testo semplice e non cambia byte per byte. Il formatter crea nodi di testo e pedici/apici, senza eseguire markup presente nel dataset o nei salvataggi. I nomi con underscore vengono trasformati solo per la visualizzazione, anche se provengono da uno snapshot precedente. Non cambiano le opzioni estratte, gli indici corretti, le risposte, il numero di versione dei salvataggi o le scadenze.

Controlli superati: build, allineamento del tema, registro crediti, 26 test, sintassi JavaScript, suite browser dell’archivio reale e suite generale di timer/storage/categorie. Il nuovo controllo `scripts/verify_quiz_notation.py` copre i 25 nomi con pedice presenti nei dati, Unicode e sintassi con graffe, variabili con potenza dopo il pedice, correzione finale, ricarica e snapshot versione 1. Confermati markup non attendibile reso come testo e assenza di errori JavaScript. Nessuna fuoriuscita orizzontale rilevata nei viewport 1440, 390 e 320 px; temi scuro e chiaro verificati. Il mobile è emulato in Chromium.

La regola generale è aggiunta ad A4 del master v69.19 e al prompt dei quiz v1.4.2; specifiche quiz v2.5.0. Revisione incrementale dei rinvii effettuata, senza modificare altre regole o introdurre nuove dipendenze.

Il lavoro resta sul ramo `fix/quiz-notazione-matematica`. AGENTS §1 richiede «anteprima verificabile della versione corrente» e approvazione esplicita prima di main o Pages: la precedente autorizzazione di pubblicazione non viene riutilizzata. La modifica è pronta per la revisione dell’anteprima, con PR in bozza.
