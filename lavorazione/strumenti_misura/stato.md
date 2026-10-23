# Stato — Gli strumenti di misura
Ultimo aggiornamento: 23 ottobre 2026 (Europe/Rome). Capitolo 6.
Fase: bozza testuale v4 e specifica simulazione v2 pronte per revisione.

## Fonte e ambito
Richiesta corrente: «Facciamo i capitoli 6 e 7», con collegamento al piano.
Ramo: `lavorazione/strumenti-errori-incertezza`, da main `d681439986db6c824fb1c724fa8cf7023e5a38de`.
Sorgente verificato: `strumenti_errori_incertezza_it.html` v7, blob `1d65637b40f2af68e1e1ff55c7d1710259b6087b`, sezioni #strumenti e #caratteristiche.
Confini, visuali identificate e collocazione: [proposta corrente](visuali.md). Misure ripetute, media, semidispersione e incertezza sono riunite nel capitolo 7 per richiesta esplicita; eliminato il capitolo separato sulle ripetizioni.
Domanda iniziale proposta: Una bilancia mostra molte cifre: basta questo per fidarsi della misura?
Template già approvato: Stringhe comune, modello autonomo v24.

## Regole e approvazioni
Letti MASTER_PROMPT.md v69.11, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, docs/visual-guidelines.md v1.0.0 e stato storico del sorgente.
Checklist: A1–A5 per narrazione, monograficità, formule e quesiti; A6 per il tema; B1.1–B2 per visuali → bozza → approvazione → stima e via; B4–B6 per riuso e salvataggi; C1–C4 per immagini e licenze; D1–D2.1 per verifiche e ramo isolato.
L'utente ha approvato l'impostazione e il riuso proposto delle visuali con «Ok», dopo la consegna della PR #72. Bozza v2 ora pronta; nessuna approvazione del testo o via all'HTML ancora ricevuto. Nessuna immagine cercata o generata.
Lo snapshot dei crediti storici dichiara provenienza e diritti non verificati: verificare registro e fonti prima dell'integrazione; il riuso non risolve tale limite.
Simulazione richiesta dall'utente: [specifica](simulazione.md), con modello, comandi, limiti, carico basso e stima preliminare condivisa 2–3 ore, aggiornata per pesetti e grafico. Nessun codice ancora programmato; nessun video.
[Bozza testuale v4](bozza.md) con segnaposto, formule, una nota e otto domande finali. Stima HTML da presentare dopo il testo approvato.

## Completato e prossimo passaggio
Controllati sorgente, descrizioni delle nove immagini e sette quesiti. Ripartizione univoca: 1–4 al 6; 5 e 7 al 7; 6 riservato all'8.
Prossimo passaggio: approvazione della bozza v4; applicare eventuali correzioni, poi presentare stima e richiedere il via all'HTML secondo B1.1–B2. Non riportare il testo integrale in chat.
Nessun HTML nuovo, modifica al manifest/catalogo, merge o deployment. Sorgenti storici e traduzioni invariati ed esclusi. Nessuna verifica browser necessaria o dichiarata per questa fase Markdown.
L'ambiente locale si è disconnesso durante il salvataggio; usati gli strumenti GitHub per conservare e verificare i file sul ramo.

## Bozza v2 completata dopo «Ok»

Conservati integralmente i quesiti originali pertinenti e aggiunte domande di ragionamento, per otto quesiti in ciascun capitolo. Verificati formule, unità, segni, riferimenti dei segnaposto e ripartizione dei sette quesiti storici. Dati nuovi dichiarati illustrativi. La sintassi delle frazioni della bozza è matematica; nell'HTML usare formule native con linea orizzontale. Testo da approvare; nessuna visuale ancora elaborata.

## Copertina scelta e bozza v2

L'utente indica esplicitamente Ytterbium Lattice Double Clock with Photons at NIST.jpg per questo capitolo, sostituendo il calibro. Scelta autorizzata; non richiedere un'altra conferma per la stessa immagine. Autore N. Phillips/NIST; Pubblico dominio: opera del governo federale statunitense, indicata PD-USGov su Commons; fonte https://commons.wikimedia.org/wiki/File:Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg, consultata tramite web. Aggiornati segnaposto, didascalia, proposta e provenienza nella bozza v2. Immagine intera senza zoom o ripetizioni. File binario non ancora acquisito o incorporato: questa fase produce le bozze testuali. Diritti della copertina documentati; diritti delle immagini storiche del corpo ancora da verificare. Nessuna approvazione del testo o via HTML dedotti dalla scelta della copertina.

## Distinzione delle simulazioni richiesta

L'utente richiede una versione nel 6 per le proprietà e una nel 7 con proprietà fisse per errore e incertezza. Registrata la decisione e preparata la specifica del capitolo; aggiornata bozza v3 con attività e segnaposto. Nel 7 U è assegnata da una scheda prima di rivelare il riferimento; nessun calcolo di media o semidispersione. I parametri numerici sono proposti e dichiarati simulati, non specifiche di uno strumento reale. Stima preliminare per entrambe 90–150 minuti, da consolidare dopo il testo approvato; nessun via all'HTML dedotto dalla richiesta di progettazione. Copertine scelte invariate. L'utente intende fornire immagini sostitutive con licenza per i materiali storici del corpo; file non ancora ricevuti. Prossimo passaggio: revisione della bozza v3 e del comportamento proposto; poi stima e via alla realizzazione secondo B1.1–B2.

## Ultime decisioni — pesetti, due serie e capitolo unico

L'utente precisa: nel 6 pesetti di massa differente e slider sotto la bilancia; nel 7 proprietà fisse, misure ripetute di massa nota per l'errore e massa ignota per l'incertezza, grafico sotto lo strumento. Richiede poi «metti media e semi dispersione nel cap 7» e chiarisce che non ha senso separarle dall'incertezza. Decisioni recepite: unico capitolo 7 con ripetizioni → media/semidispersione → stima didattica dell'incertezza → confronto col riferimento. Eliminato l'ex capitolo 8 separato; piano a undici capitoli con i successivi rinumerati.

Bozze v4 e specifiche v2 aggiornate. SIM-07 non assegna più U a priori: l'alunno la stima con la regola scolastica dichiarata U_did = max(d,q); media e semidispersione mostrate e calcolate, senza confonderle con l'errore o con la fascia U. Modello proposto con zero regolato e rumore sintetico; non nascondere sistematici sotto la sola dispersione. Copertine scelte invariate; immagini di bilancia, pesetti e campioni con diritti verificati ancora da acquisire. Stima preliminare 2–3 ore complessive, da consolidare prima del via alla realizzazione.

Checklist aggiuntiva: calcolo e grafico su serie asimmetriche, d distinto dalla distanza media-estremi, U non nulla per letture identiche, grafico dell'ignoto senza riferimento nascosto, conservazione dei sette quesiti storici (1–4 nel 6; 5–7 nel 7). Sorgenti storici invariati. Testo e dettagli proposti da revisionare; nessun codice/HTML, merge o deployment.
