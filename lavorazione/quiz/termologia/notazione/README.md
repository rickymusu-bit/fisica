# Grandezze fisiche e notazione nel quiz — anteprima

25 ottobre 2026. Revisione richiesta dal docente e approvata per la pubblicazione con «Perfetto, pubblica.».

- [Quiz HTML interattivo autonomo con tutte le 300 domande](quiz.html).
- Quesito dello screenshot aggiornato: [desktop scuro](pedici-1440-dark.png), [mobile scuro](pedici-390-dark.png), [320 px](pedici-320-dark.png).
- Tema chiaro: [desktop](pedici-1440-light.png), [mobile](pedici-390-light.png).
- [Soluzione finale sul mobile](soluzione-390.png).
- [Esiti dei controlli browser sulla notazione](verifica.json).

Le immagini mostrano una sessione di un solo quesito per rendere confrontabile il caso segnalato. L’HTML completo conserva tutte le 300 domande e le sessioni configurabili da 1 a 30.

## Regola editoriale applicata

Ogni dato segue l’ordine **nome della grandezza a parole → simbolo → valore con unità**. Il simbolo va sempre fornito insieme al nome. Quando compaiono più grandezze dello stesso tipo, i pedici sono brevi e chiariti dal contesto, per esempio le masse di acqua e ghiaccio m<sub>a</sub> e m<sub>g</sub>. Una grandezza unica usa la sola lettera, per esempio «il calore specifico dell’acqua è c = 4200 J/(kg · K)».

La regola sostituisce quella precedente che permetteva di omettere il simbolo nei dati descritti a parole. Registrata in A4 del master v69.20 e nel prompt dei quiz v1.4.3; specifiche quiz v2.5.1. Rinvii e istruzioni interessate controllati per coerenza.

Sono adeguati **158 testi**: tutte le 90 domande di calcolo, 57 di ragionamento e 11 di conoscenza. Nei quesiti concettuali che chiedono il significato di un simbolo non si anticipa la risposta. Riviste anche 10 spiegazioni per mantenere la notazione coerente. Solo le alternative di termo-137 cambiano nella grafia dei simboli: Q_b e Q_t sostituiscono Q_bevanda e Q_tazza. Restano invariati i dati fisici, i risultati, gli indici corretti, le classificazioni, le 78 espressioni di ricalcolo e le altre alternative. Sono sincronizzati archivio attivo, copie di lavorazione, campione, primo lotto, nove lotti successivi e metadati di revisione. Le approvazioni storiche riguardano i contenuti originari; la presente revisione ha ricevuto una propria approvazione esplicita alla pubblicazione.

## Resa e verifiche

Il quiz usa gli stessi elementi HTML nativi `sub` e `sup` dei capitoli, senza librerie esterne. Il formatter sicuro riconosce anche i simboli preceduti da coefficienti numerici, per esempio `2m_B`. Pedici e apici sono applicati a domanda, alternative e revisione finale; il testo non viene interpretato come HTML. Le vecchie sessioni conservano contenuti e scadenze originali e ricevono soltanto la formattazione tipografica.

Verifiche: archivio, ricalcolo delle soluzioni, build, 26 test unitari, sintassi JavaScript, tema e crediti. Browser Chromium: quiz reale a tutte le difficoltà; caso termo-285 nei temi chiaro/scuro a 1440, 390 e 320 px; tutti i simboli indicizzati dell’archivio, coefficienti prima dei simboli, Unicode e graffe, correzione finale, sessione precedente versione 1 e markup non attendibile. I dettagli degli esiti sono nel rapporto JSON. Mobile emulato; nessuna calibrazione dei tempi osservata in classe.

La [PR #89](https://github.com/rickymusu-bit/fisica/pull/89) contiene la revisione approvata con «Perfetto, pubblica.» il 25 ottobre 2026. La [CI della versione funzionale](https://github.com/rickymusu-bit/fisica/actions/runs/40173676319) è superata. L’autorizzazione comprende merge e GitHub Pages; esito del deploy nel workflow [Pubblica Stringhe](https://github.com/rickymusu-bit/fisica/actions/workflows/pages.yml), destinazione [quiz online](https://rickymusu-bit.github.io/fisica/quiz.html).
