# Stato — Anteprima del tema comune

Aggiornamento: 17 ottobre 2026, ore 00:46 (Europe/Rome). Master applicato: v53; riferimento grafico scelto espressamente dall’utente, https://mac-template.webflow.io/.

Richiesta esplicita: mostrare un esempio di pagina con quel tema usando il testo del riferimento di stile. Questa richiesta autorizza una prova grafica separata dal capitolo e dal sito pubblico.

Realizzato [anteprima.html](anteprima.html), v1: HTML autonomo con il testo completo dei tre estratti in `riferimenti/esempio_irraggiamento.md`, quattro formule in HTML/CSS, indice interno, ritorno ai materiali, segnaposto per copertina e visuali previste. Nessuna nuova fotografia, illustrazione o simulazione. Il primo titolo interno è adattato a un titolo rivolto al lettore; testo e formule del campione sono conservati. Le didascalie previste accompagnano i segnaposto.

Aspetto: bianco e grigio, bordi neri e ombre nette, intestazioni delle finestre, indice rettangolare, font Baloo Thambi 2 incorporato. La licenza SIL OFL 1.1 è incorporata nella pagina. Il layout mantiene una colonna di lettura e si adatta allo smartphone.

Verifiche: Chromium a 1440 e 390 px; nessun errore JavaScript o scorrimento orizzontale della pagina; indice interno funzionante, quattro formule presenti, font caricato e nessuna dipendenza esterna per contenuto e stile. I collegamenti all’indice pubblico richiedono Internet. Resa desktop e smartphone ispezionata. Esiti in `verifiche.json`; immagini di anteprima nella stessa cartella. HTML inferiore a 0,5 MB.

Stato: prova pronta da mostrare; giudizio dell’utente sull’adattamento grafico ancora da ricevere. Nessun HTML ufficiale o configurazione di pubblicazione modificato. Salvataggio nel ramo `istruzioni/tema-mac`; verificare il caricamento remoto prima della consegna.

## Revisione tipografica — v2

17 ottobre 2026, ore 00:48 (Europe/Rome). L’utente ha apprezzato il tema e richiesto un font che vada bene per le persone con dislessia. Proposto Lexend e applicato all’anteprima v2 al posto di Baloo Thambi 2, con testo a sinistra, interlinea 1,65, corpo 21 px (19 px su smartphone) e titoli senza spaziatura compressa. Font variabile e licenza SIL OFL 1.1 incorporati. Testo, formule, segnaposto e struttura grafica preservati. Formule a 20 px su smartphone, con scorrimento interno quando necessario; sostituiti i simboli di freccia non disponibili nel font con indicatori CSS. Master v54 registra il requisito comune; la scelta specifica di Lexend resta da valutare dall’utente. Verifiche rinnovate a 1440 e 390 px: font caricato, indice da tastiera funzionante, nessun errore JavaScript o scorrimento orizzontale della pagina; anteprime aggiornate.

## Indice laterale — v3

17 ottobre 2026, ore 00:58 (Europe/Rome). Risposta dell’utente alla v2: «Ok», seguita dalla richiesta di sostituire l’indice iniziale con una barra laterale a scomparsa come in un lettore PDF. Lexend accettato come base della revisione.

Anteprima v3: rimosso l’indice orizzontale iniziale; aggiunto pannello laterale con dialog nativo, aperto dal pulsante «Indice» nell’intestazione persistente. Sezioni cliccabili, indicatore della sezione corrente, chiusura con pulsante, Esc, clic esterno e selezione di una voce. Focus contenuto nel pannello durante l’apertura; dopo la navigazione passa al titolo della sezione. JavaScript e CSS incorporati, nessuna libreria esterna. Testo, formule, visuali e tipografia conservati.

Verificati in Chromium a 1440 e 390 px: chiuso all’avvio, apertura da tastiera, focus nel pannello, Esc e ritorno al pulsante, navigazione alle sezioni con chiusura e focus sul titolo, pulsante accessibile durante lo scorrimento, voce corrente corretta, chiusura dal fondo esterno, nessun errore JavaScript o scorrimento laterale della pagina. Esiti aggiornati in `verifiche.json`; nuove anteprime a pannello aperto in `indice-desktop.png` e `indice-smartphone.png`.

Master v55 e riferimento grafico allineati alla richiesta. Nessun aggiornamento degli HTML ufficiali o del sito pubblicato. Salvataggio nel ramo dedicato; prossimo passaggio mostrare la nuova anteprima all’utente.

## Correzione dell’apertura su mobile — v4

17 ottobre 2026, ore 01:02 (Europe/Rome). L’utente segnala che il pannello non si apre al tocco e precisa di usare l’anteprima del file dentro ChatGPT. La v3 si apre nell’emulazione touch Chromium con JavaScript, ma non con gli script disabilitati. Questo riproduce il sintomo, senza attestare le impostazioni interne dell’anteprima ChatGPT.

Sostituiti dialog e apertura esclusivamente JavaScript con `details`/`summary` nativi: apertura e chiusura al tocco funzionano anche senza script. Aspetto e contenuti conservati. Con JavaScript restano focus gestito, Esc, clic esterno, chiusura selezionando una sezione e voce corrente. Senza script, dopo aver scelto una sezione si chiude il pannello con lo stesso comando nativo «Chiudi».

Verifiche in `verifiche.json`: desktop 1440 px, mobile touch 390 px con e senza JavaScript, mobile touch 320 px senza JavaScript. Superate apertura, chiusura, navigazione e assenza di scorrimento laterale; verificati inoltre focus, Esc e clic esterno con script attivi. Nessun errore JavaScript. Le verifiche non sono eseguite nell’anteprima interna di ChatGPT. Anteprime aggiornate. Nessun HTML ufficiale o pubblicazione modificato.

## Nome del collegamento alla home — v5

17 ottobre 2026, ore 01:05 (Europe/Rome). L’utente chiede di sostituire «Materiali» con un nome meno generico. Applicata «← Biblioteca di fisica» a entrambi i collegamenti della prova; URL invariati. Master v56 e riferimento grafico allineati. Adeguata la disposizione dell’intestazione per il testo più lungo sugli schermi stretti. Nessun HTML ufficiale o pubblicazione modificato.

## Etichetta in una parola — v6

17 ottobre 2026, ore 01:06 (Europe/Rome). L’utente precisa che l’etichetta deve essere una sola parola. Applicata «← Biblioteca» in alto e in fondo alla pagina; URL invariati. Master v57 e riferimento grafico allineati.

## Approvazione del tema completo

17 ottobre 2026, ore 05:26 (Europe/Rome). L’utente conferma: «Va bene. Questo è il tema grafico per tutti i capitoli. Ora torniamo a pianificare il contenuto». L’anteprima v6 diventa il riferimento grafico approvato per tutti i capitoli; comprende Lexend, indice laterale nativo e link «← Biblioteca». La scelta Mac per la home rimane valida. Approvazione grafica distinta da quella del contenuto del capitolo. Prossima attività nella lavorazione irraggiamento: progettazione dei contenuti e delle visuali.
