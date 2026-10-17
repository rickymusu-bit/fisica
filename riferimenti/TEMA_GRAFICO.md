# Tema grafico comune

Aggiornamento: 17 ottobre 2026, ore 00:58 (Europe/Rome).
Master: v57, A6.

## Scelta approvata

L’utente ha indicato https://mac-template.webflow.io/ come template per tutti i capitoli e per la home del sito: «Questo tema è il riferimento». La scelta è permanente fino a una diversa indicazione esplicita. Non richiedere una nuova scelta per ogni capitolo. L’utente ha poi approvato esplicitamente l’adattamento completo dell’anteprima v6 come tema per tutti i capitoli: Mac, Lexend, indice laterale nativo a scomparsa e collegamenti «← Biblioteca».

## Caratteristiche del riferimento

Pagina e foglio di stile consultati il 17 ottobre 2026 (Europe/Rome). Il CSS del riferimento usa la famiglia Baloo Thambi 2 con alternativa sans-serif, titoli grandi e marcati, superfici prevalentemente bianche e grigie (#c4c4c4), testo e bordi neri, contorni spesso di 4 px e ombre nette sfalsate di 8 px. Le finestre con barra superiore e i pulsanti rettangolari richiamano un’interfaccia desktop classica. Il riferimento contiene anche impaginazioni a due colonne che diventano verticali sugli schermi più piccoli.

La registrazione iniziale derivava dall’HTML e dal CSS. Durante la successiva prova richiesta dall’utente è stata verificata anche la resa statica nel browser Chromium, caricando pagina e risorse tramite HTTPS con verifica TLS. La prova locale riprende finestre, grigi, contorni e ombre del riferimento; la tipografia è adattata alla richiesta di leggibilità sotto indicata.

## Tipografia e leggibilità

L’utente ha apprezzato la prova del tema («Bello») e richiesto un font adatto alle persone con dislessia. Il requisito riguarda la tipografia del tema comune; non richiede di cambiare la struttura grafica.

Carattere corrente: **Lexend**, carattere sans-serif progettato per facilitare la lettura ([progetto ufficiale](https://www.lexend.com/), [font e licenza](https://github.com/google/fonts/tree/main/ofl/lexend)). L’utente ha risposto «Ok» alla prova v2 e ha richiesto la successiva modifica dell’indice. Font variabile incorporato, licenza SIL OFL 1.1 inclusa, funzionamento offline.

Testo a sinistra senza giustificazione, corpo di 21 px su desktop e 19 px su smartphone, interlinea 1,65, spaziatura regolare. Titoli senza compressione della distanza fra le lettere; evitare lunghi tratti in corsivo o maiuscolo. Il font, da solo, non garantisce la stessa leggibilità per tutte le persone.

## Adattamento alle dispense e alla home

Per i capitoli, indice interno in un pannello laterale a scomparsa come nei lettori PDF, richiesto esplicitamente dall’utente al posto dell’indice all’inizio della pagina. Pulsante «Indice» nell’intestazione sempre raggiungibile durante la lettura, pannello inizialmente chiuso, sezione corrente evidenziata, chiusura esplicita o con Esc, selezione di una voce e clic esterno. Pannello sovrapposto alla pagina su smartphone. Usare comandi semantici e gestione del focus, preservando il tema Mac e Lexend. Il catalogo dei materiali nella home e i collegamenti al sito restano distinti dall’indice interno del capitolo.

Compatibilità delle anteprime: apertura e chiusura esplicita devono funzionare anche senza JavaScript. La prova v4 usa `details` e `summary` nativi, senza dipendere da `dialog.showModal()`. Gli script migliorano focus, sezione corrente, chiusura automatica dopo la scelta, Esc e clic esterno; quando non sono eseguiti si naviga con i collegamenti e si chiude con «Chiudi». Verificare anche il tocco reale emulato con script disabilitati, oltre alla sola larghezza dello schermo.

- Riprendere il linguaggio grafico comune per navigazione, copertina, titoli e comandi; mantenere un corpo del testo discorsivo, con larghezza e interlinea adatte alla lettura.
- Usare le cornici in modo selettivo, senza una finestra per ogni paragrafo. Conservare l’ordine del capitolo e la distribuzione delle visuali previsti in A3.
- Conservare colori e dettagli utili di fotografie, grafici e schemi: i filtri in scala di grigi presenti nel template non si trasferiscono automaticamente ai materiali didattici.
- Adeguare titoli e spaziature a smartphone e tablet; conservare contrasto, focus visibile e comandi accessibili secondo A6.
- Realizzare gli HTML autonomi secondo A6. La scelta del riferimento non impone dipendenze da Webflow né l’importazione delle sue immagini o dei suoi contenuti dimostrativi. Per font e materiali valgono le regole di licenza e autonomia del master.
- Per la home preservare indice dei materiali, collegamenti di lettura e download; per i capitoli preservare contenuti e risorse non coinvolti nella revisione.

## Stato

Approvato il riferimento grafico per home e capitoli; HTML esistenti ancora da adeguare. Su richiesta esplicita dell’utente è stata realizzata una [pagina dimostrativa](../lavorazione/tema_grafico/anteprima.html) con il testo del campione sull’irraggiamento e segnaposto per le visuali. La richiesta autorizza questa prova grafica; non costituisce approvazione del capitolo completo. Applicare le fasi pertinenti del master senza chiedere nuovamente la scelta del tema.

Il collegamento alla home ha etichetta **«← Biblioteca»**, in alto e in fondo al capitolo, al posto di «Materiali» o «Indice dei materiali». Destinazione invariata: `https://rickymusu-bit.github.io/fisica/#indice`. Nome scelto dall’assistente in risposta alla richiesta dell’utente di usare una dicitura meno generica, successivamente precisata in una sola parola.
