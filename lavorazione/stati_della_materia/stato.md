# Stato — Stati della materia

## Pubblicazione autorizzata — 2026-10-18 09:00 (Europe/Rome)

L’utente ha approvato le anteprime e richiesto esplicitamente «Ok ok pubblica». Autorizzata l’integrazione del ramo `revisione/materia-passaggi-capitoli` in main e la pubblicazione tramite il workflow Pages esistente: Stati della materia **v13**, Passaggi di stato **v14**, Irraggiamento **v6**. Contenuti approvati al commit `fc325c9ff17e7339a15b403a26b6a98a161e8332`; nessun cambiamento ai tre HTML durante la preparazione della pubblicazione. Master v58 consultato; build locale e copie esatte nell’output verificate. Home con i due capitoli separati e vecchi indirizzi conservati tramite reindirizzamento. Pubblicazione completata tramite PR #20, merge `fb44117ae488c2cded4eb2a0abdeca0002839083`; workflow Pages `39106119681` concluso con successo. Verificati via HTTPS home v8, Stati della materia v13, Passaggi di stato v14, Irraggiamento v6 e i due vecchi indirizzi: HTTP 200 e contenuti identici byte per byte all’output approvato. Esiti e hash in `lavorazione/stati_della_materia_e_passaggi_di_stato/pubblicazione.json`. Non restano passaggi di pubblicazione pendenti. Le indicazioni di mancata autorizzazione nei blocchi storici sottostanti sono superate da questa richiesta.

## Revisione corrente — 2026-10-18 01:30 (Europe/Rome)

Richiesta diretta: note collassabili, pulsanti «Biblioteca», riparazione dei modelli particellari e del grafico del calore latente, note anche per Irraggiamento. L’utente ha precisato che il problema si presenta nell’**anteprima dentro ChatGPT**. Master **v56** consultato integralmente; modello autonomo **v3**. Regole persistenti aggiornate in A6, AGENTS e STILE_DISPENSE. Note native `details`/`summary`, chiuse all’apertura, con richiami che aprono la sezione e ritorni. Etichetta «← Biblioteca» nei due collegamenti di ciascun capitolo e nel modello. Tema comune riusato integralmente, senza altre varianti grafiche.

**Versione corrente v13**, HTML e bozza sincronizzati. Dimensioni intrinseche dichiarate per le immagini, per riservare lo spazio ed evitare spostamenti durante i salti alle note. Le tre simulazioni JavaScript sono conservate; la funzione del modello originale è incorporata senza cambiamenti. I tre controlli di pausa/avvio sono indipendenti e rispettano la preferenza di movimento ridotto. Se gli script non sono eseguiti, vengono mostrate tre GIF di 6 s ricavate dai canvas originali a 280 × 240 px, con poster statici per movimento ridotto. Non sono simulazioni sostitutive né nuovi modelli fisici. Risorse e derivazione in `risorse/anteprime-modelli.json`. Foto scelte e GIF della viscosità conservate; 6 note, 9 richiami, 6 domande.

Peso corrente 7892485 byte, sotto 18 MB. Verifiche della revisione corrente: `../stati_della_materia_e_passaggi_di_stato/verifica-interazioni.json`; anteprime desktop/mobile aggiornate nella cartella del capitolo. Consegna per lettura; **nessuna pubblicazione né unione in main**. I paragrafi sottostanti conservano la cronologia; il presente blocco identifica lo stato corrente.

Ultimo aggiornamento: 2026-10-17 22:14 (Europe/Rome). Master v53, letto integralmente con i riferimenti di stile; intestazione e hash ricontrollati, invariati. Ramo `revisione/materia-passaggi-capitoli`, derivato da `main` al commit `d72296ad77a2ae92342386c7dfeb73cc1b44e736`.

## Ambito e fonte

Proprietà di solidi, liquidi, gas e plasma attraverso il modello particellare; breve confronto viscosità/densità e spiegazione dei tre pannelli dello schema scelto. Fonte: v8 di `stati_della_materia_e_passaggi_di_stato.html`, blob `8ef5566c73f670dbf23b550e4e36a52cdb7ddfc2`. [Mappa della suddivisione](../stati_della_materia_e_passaggi_di_stato/proposta-editoriale.md). Nessuna trattazione dei passaggi di stato in questo capitolo.

## Decisioni effettive e fase corrente

Approvati due capitoli distinti e tema della v8. Successivamente richieste tutte foto nuove e uno schema cristallino/amorfo; forniti otto materiali selezionati, acquisiti e controllati, con originali, fonti, licenze e hash nel [registro](risorse/materiali-scelti.json). Riferimento completo: [visuali](visuali.md).

Ultima istruzione: **«Mantieni le simulazioni degli stati microscopici»**. Conservare M6–M8 della v8: `solidMotion`, `liquidMotion`, `gasMotion`, tutti 280 × 240, con modello e comportamento esistenti. Script comune SHA-256 `8d2718622f3eb953ed226eb9ae63e079d5567a6f1a1c90d1fef67c2463e34a6c`. La richiesta di sostituirle con GIF è superata: non mancano più tre GIF e non occorrono altre ricerche. M11, la GIF della viscosità, si conserva insieme alle simulazioni.

Fase: [bozza completa aggiornata](bozza.md), da confermare dopo l’adattamento ai materiali scelti. Domanda iniziale corrente: «Da che cosa dipende, allora, la capacità di mantenere una forma?». Nessun nuovo HTML realizzato o pubblicato; l’approvazione delle scelte visuali non viene trasformata in approvazione del testo aggiornato o via all’HTML.

## Materiali correnti

C1 copertina ghiaccio in mare; M1 bismuto; M2 tartaruga di vetro di Murano; M3 olio sulla pizza; M4 dirigibile; M5 scarica nell’argon; M6–M8 simulazioni originali; M9 tabella semantica; M10 schema scelto cristallino/policristallino/amorfo; M11 GIF viscosità, 63 fotogrammi. Lo schema provvisorio precedentemente creato resta un riferimento di lavorazione, senza doppio inserimento. Vetro: nuova foto della tartaruga di Murano, originale 2121 × 1414 px; superata la limitazione della foto precedente. Nessuna compressione o modifica delle immagini effettuata.

Per questo capitolo **tutti i materiali visuali necessari sono disponibili**. Le vecchie candidate GIF non sono state scelte e non vanno integrate. La cronologia Git conserva le decisioni precedenti.

## Verifiche e prossima operazione

Controllati in questo aggiornamento: tre canvas e script presenti nella fonte, riferimenti M6–M8 ripristinati nella bozza, domanda 5 riferita alle simulazioni, M11 distinta, richiesta delle GIF rimossa dai punti aperti correnti. Nessun codice della simulazione modificato; nessuna prova browser nuova dichiarata. Sei domande finali conservate. Gli otto file scelti e i relativi originali erano già stati verificati: non ripetuta l’acquisizione.

Prossima operazione: confermare il testo adattato ai materiali scelti, aggiornare la stima e raccogliere il via all’HTML secondo B1.1–B2. Poi trasferire i tre modelli vicino alle spiegazioni preservando identificativi e script, verificare funzionamento offline, lettura e navigazione, integrare crediti e salvare `stati_della_materia.html`. La bozza di Passaggi di stato resta approvata; i suoi materiali ancora mancanti sono nel relativo stato. Nessuna modifica alla pubblicazione del sito.

## Sostituzione della foto del vetro

L’utente ha fornito la tartaruga di vetro come nuova scelta per M2. Anteprima 960 × 640 px e originale 2121 × 1414 px acquisiti, decodificati e conservati senza modifiche; foto ispezionata. Fonte Commons e attribuzione Murray Foubister / CC BY-SA 2.0 verificate. Registro aggiornato con la vecchia foto marcata come sostituita e conservata come riferimento. Bozza e didascalia aggiornate; nessuna nuova approvazione richiesta per la scelta esplicita. Nessuna modifica alle simulazioni, alla GIF della viscosità o al sito.

## Via alla realizzazione

L’utente ha confermato «Ok procedi»: realizzazione dei due HTML autorizzata. HTML v9 integrati, verifiche in corso; nessuna pubblicazione. Peso iniziale: stati 6.270.253 byte, passaggi 20.808.247 byte. Richiesta autorizzazione puntuale per ottimizzare senza perdita le GIF del secondo capitolo, secondo il limite di 20 MB del master.

## Anteprima HTML realizzata — 2026-10-17 23:18 (Europe/Rome)

HTML v9 in `bozza.html`, copia con nome stabile alla radice del ramo di lavorazione; anteprime desktop/mobile salvate. Immagini incorporate, simulazioni particellari originali conservate e dotate di pausa, preferenza di movimento ridotto rispettata; curva selezionabile e PWR ingrandibile. Verifiche Chromium 390/1280 px e offline superate: immagini integre, nessun errore JavaScript, nessuna eccedenza orizzontale della pagina, 6/8 domande finali. Calcoli dell’esempio verificati: totale 1.504.500.000 J. Build locale superata, indice a 10 articoli e 12 casi di vecchi URL con query/frammenti verificati. Nessuna pubblicazione o modifica del workflow.

**Punto aperto:** Stati della materia pesa 6.270.253 byte; Passaggi di stato pesa 20808480 byte, oltre il limite di 20.000.000 byte. Richiesta in chat approvazione per ottimizzare senza perdita copie delle tre GIF, conservando fotogrammi, colori e tempi; risposta non ancora ricevuta. File di Passaggi di stato consegnato come anteprima, non dichiarato definitivo conforme al peso. Le attribuzioni dei visuali ereditati incompleti sono dichiarate nei crediti; recuperata e verificata per hash la GIF di fusione (Moussa, pubblico dominio).

## Prossima operazione

Ricevuta l’autorizzazione, ottimizzare copie delle GIF con confronto integrale dei fotogrammi decodificati e tempi, aggiornare incorporamento e misura del peso. Verificare le sole parti interessate e consegnare v9 conforme. Non pubblicare senza la successiva approvazione dell’anteprima.

## Aggiornamento peso di Passaggi di stato — 2026-10-17 23:29

L’utente ha richiesto espressamente entrambi i metodi di downsampling su tutte le GIF di Passaggi di stato. Copie ridotte integrate nella v10: 14252684 byte, limite rispettato. Originali conservati. Il precedente punto aperto sull’autorizzazione è risolto. Stati della materia resta v9 e non è modificato; nessuna pubblicazione.

## Tema comune applicato — 2026-10-17 23:35 (Europe/Rome)

Richiesta esplicita dell’utente: «Ricordati di applicare il tema». Allineato al tema comune già presente in `irraggiamento_it.html` v4 e nella home: Lexend incorporato con licenza, grigio/nero, bordi netti, copertina e indice laterale accessibile. Il precedente riferimento al tema v8 è superato da questa richiesta. **Versione corrente v10**, peso 6517363 byte. Testo didattico di ogni sezione confrontato con il precedente e invariato; tutte le immagini e GIF hanno gli stessi byte incorporati. Modello particellare originale conservato. Tema applicato anche ai comandi, alle tabelle e alle formule; solo evidenziazione della curva adattata al tema, senza modifiche ai dati.

Verifiche Chromium offline a 390/1280 px superate: Lexend caricato, indice apribile e chiudibile con Escape e con i collegamenti, focus/inert ripristinati, immagini integre, comandi delle simulazioni/curva e ingrandimento PWR funzionanti; nessuna eccedenza orizzontale o errore JavaScript. HTML di lavoro sincronizzato e anteprime desktop/mobile aggiornate. Build locale superata. Registro comune `../stati_della_materia_e_passaggi_di_stato/verifica-tema.json`. Nessuna pubblicazione.

## Regole editoriali aggiornate — 18 ottobre 2026, ore 00:31 (Europe/Rome)

Master v54: l’utente segnala errori nel tema e richiede di salvare l’esatto tema grafico adottato come modello autonomo per i capitoli futuri: `riferimenti/TEMA_DISPENSE.html`. Il riferimento operativo è questo modello, non il file del capitolo sull’irraggiamento. A6 ora stabilisce il modello autonomo già scelto, il riuso di struttura/stili e il confronto desktop/mobile; rimossa la richiesta ripetuta del template. A4 impone notazione esponenziale e prefissi SI nei calcoli; A5 richiede un confronto quantitativo concreto per interpretare ogni risultato significativo degli esercizi. Aggiornati anche AGENTS.md e il riferimento linguistico pertinente.

Questa operazione salva le regole: non modifica gli HTML né attesta che le versioni correnti siano già conformi alla richiesta più rigorosa. Alla revisione dei capitoli applicare il modello grafico autonomo esatto, adeguare la scrittura dei calcoli e integrare il confronto finale, conservando visuali e risultati fisici approvati. Nessuna pubblicazione.

## Correzione secondo il modello autonomo e master v55 — 2026-10-18 00:49 (Europe/Rome)

L’utente ha autorizzato la correzione dei due capitoli, scelto il confronto con il consumo domestico e stabilito la nuova regola delle precisazioni nelle note a piè di pagina. **Versione corrente v11**, 6519321 byte, HTML di lavoro sincronizzato. CSS e JavaScript comuni riusati identici da `riferimenti/TEMA_DISPENSE.html`; rimosse le sovrascritture del tema. Struttura dei titoli, etichetta Fisica in copertina, cornici/overview delle figure, formule con etichetta e righe native, pulsanti, indice e navigazione ripresi dal modello. Gli stili aggiuntivi sono limitati ai componenti assenti dal modello: tabelle, canvas, curva, modello fisico e note. Foto scelte e GIF ridotte conservate nei byte originali incorporati. Modello particellare invariato, con controllo della pausa isolato dal codice del tema.

Precisazioni spostate nelle note al termine del contenuto, prima dei crediti; richiami numerati e collegamenti di ritorno. Nuova regola salvata nel master v55 e nei riferimenti/AGENTS. Dati e passaggi necessari alla spiegazione restano nel corpo. Sei/otto domande finali conservate.

Verifiche: confronto automatico degli stili effettivi con il modello a 390/1280 px, CSS/JS comuni confrontati integralmente, immagini caricate offline, nessuna eccedenza orizzontale o errore JS, curve/pausa/ingrandimento funzionanti. Calcoli e tutti i 24 frammenti storici controllati. Formule prive di tagli sul telefono. Anteprime aggiornate; risultati in `../stati_della_materia_e_passaggi_di_stato/verifiche-finali.json`. Build locale superata, entrambi sotto 20 MB. Limiti di attribuzione dei materiali ereditati già dichiarati conservati. Nessuna pubblicazione.

## Prossima operazione corrente

Consegnare le anteprime revisionate per la lettura dell’utente. Nessuna pubblicazione o unione in main autorizzata.

Il componente Note con richiamo e ritorno è ora salvato nel modello autonomo **v2** per il riuso futuro. Nessuna modifica ai CSS o ai comandi dei componenti preesistenti; gli stili delle note, già verificati nel browser, sono centralizzati nel modello e incorporati identici nei due capitoli. La sola ricollocazione del CSS non cambia la resa. Pesi correnti: Stati della materia 6519356 byte; Passaggi di stato 14548360 byte.

## Rilettura completa delle precisazioni tecniche — 2026-10-18 00:56 (Europe/Rome)

Richiesta dell’utente: cercare ovunque nel testo le precisazioni troppo tecniche e spostarle nelle note. **Versione corrente v12**, 6520699 byte. Riletti teoria, applicazioni, didascalie ed esempio. Approfondimenti trasferiti, senza eliminare le informazioni: grani-cristallini, origine-viscosita, plasma-cariche-luce. Nel corpo restano concetti fondamentali, significato delle formule, dati/calcoli e confronto finale con il consumo domestico. Le note ora sono 6, con 9 richiami; numerazione riordinata secondo la lettura, ritorni multipli per le note condivise.

Tema/CSS, JavaScript, immagini/GIF e tutte le formule confrontati con la versione precedente e identici. Nessuna modifica dei risultati numerici, del modello particellare, dei confini dei capitoli o delle domande finali. Bozza testuale e HTML sincronizzati. Verifica Chromium offline a 390/1280 px: immagini caricate, nessuna eccedenza orizzontale né errore JS, formule senza tagli; tutti i richiami e ritorni verificati su telefono. Sei/otto domande conservate; anteprime aggiornate. Build locale superata. Nessuna pubblicazione.

## Prossima operazione corrente

Consegna delle anteprime alleggerite, in attesa della lettura dell’utente. Nessuna pubblicazione autorizzata.
