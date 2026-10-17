# Stato — Stati della materia e passaggi di stato

Ultimo aggiornamento: 2026-10-17 20:55 (Europe/Rome). Master applicato: **v53**, letto integralmente insieme ai due riferimenti di stile.

Fase corrente: suddivisione e tema approvati; bozze complete scritte e controllate, da sottoporre all’approvazione per la revisione richiesta il 17 ottobre 2026. Ramo dedicato `revisione/materia-passaggi-capitoli`, derivato da `main` al commit `d72296ad77a2ae92342386c7dfeb73cc1b44e736`. HTML ufficiale ancora v8: nessuna nuova versione realizzata, integrata o pubblicata.

[Proposta editoriale corrente](proposta-editoriale.md): mappa completa dei contenuti verso due capitoli monografici (`stati_della_materia.html` e `passaggi_di_stato.html`), percorso della riscrittura, riuso di tutte le 13 immagini e delle tre animazioni, materiali mancanti, controlli e stima. La corrispondenza è registrata prima dell'esecuzione, come richiesto da A3.

Approvazione effettiva nuova: richiesta di applicare le regole editoriali, spezzare, riformattare, riordinare e rifare il testo; segnalare nuovi visuali. L’utente ha successivamente risposto **«Approvo»** alla proposta: confermati i due capitoli e il tema della v8. Le nuove immagini non sono ancora state consegnate; le bozze complete non sono ancora state approvate e non è stato dato il via all’HTML previsto da B1.1–B2. Riutilizzare il tema della v8 come revisione dello stile già concordato. Nessuna ricerca o generazione di immagini effettuata.

Verifiche preliminari completate: identità della fonte v8 e blob `8ef5566c73f670dbf23b550e4e36a52cdb7ddfc2`; lettura integrale del documento con parser `huge_tree=True`; 13 immagini, tre animazioni, due tabelle, curva qualitativa e 14 quesiti individuati; due calcoli verificati (167.000 J e 451.400 J). Da correggere il passaggio sulle nuvole, la spiegazione del calore latente e le didascalie; da completare gli schemi degli esercizi e le immagini delle applicazioni. Crediti della fonte incompleti: non attestare licenze verificate.

Punti aperti: file per le copertine e le immagini delle applicazioni, originali adatti agli schemi, riferimenti di licenza mancanti; approvazione delle bozze complete. Nessuna prova dei futuri HTML è stata eseguita, perché non sono ancora stati realizzati. Checklist pertinente: A1–A6, B1.1–B6, C1–C5, D1–D2.1.

Aggiornamento successivo: per **Stati della materia** l'utente ha richiesto tutte foto nuove, schema cristallino/amorfo e ricerca di GIF al posto delle simulazioni. [Registro visuali corrente](../stati_della_materia/visuali.md). Schema realizzato; candidate GIF individuate ma originali non scaricabili nell'ambiente (HTTP 403). Nessuna GIF specifica approvata o inserita. Il riuso di M1–M8 nella proposta iniziale è superato. Passaggi di stato resta invariato.

Bozze correnti: [Stati della materia](../stati_della_materia/bozza.md), con sei domande finali, e [Passaggi di stato](../passaggi_di_stato/bozza.md), con tre applicazioni, due esercizi svolti e otto domande finali. La scrittura completa comprende tutti i nuclei della v8, le formule interpretate, la correzione sulle nuvole e i segnaposto delle immagini. Stati specifici nei rispettivi percorsi di lavorazione.

Prossima operazione: presentare le bozze complete; dopo la loro approvazione aggiornare la stima e raccogliere il via all’HTML. Non modificare la pubblicazione del sito.

## Revisione precedente consolidata

La revisione precedente è stata integrata in `main` con la [PR #6](https://github.com/rickymusu-bit/fisica/pull/6) e pubblicata. [Workflow riuscito](https://github.com/rickymusu-bit/fisica/actions/runs/38935850257). Le approvazioni e verifiche sotto si riferiscono a quel lavoro, non alla nuova suddivisione.

File corrente verificato: [stati_della_materia_e_passaggi_di_stato.html](../../stati_della_materia_e_passaggi_di_stato.html), **v8**. Fonte certa: [stati_della_materia_e_passaggi_di_stato_v6_20261016.html](https://github.com/rickymusu-bit/fisica/blob/a8e171c7c3dcc220521666a8b5330beb4422999e/stati_della_materia_e_passaggi_di_stato_v6_20261016.html), già importata da Drive. La cronologia conserva l’originale; il vecchio URL pubblico verrà reindirizzato mantenendo query e frammento.

Ambito: solo revisione editoriale italiana concordata nel [piano](../revisione-blog.md), preservando contenuti scientifici, tema delle dispense esistenti, figure, video e interazioni non coinvolti. Domanda/apertura corrente: «Perché il ghiaccio mantiene la propria forma, mentre l’acqua prende quella del recipiente? Per capirlo seguiamo il movimento delle particelle, dalle proprietà dei solidi e dei fluidi fino ai passaggi di stato.».

Approvazioni effettive: richiesta di stile da blog e correzioni sul calore; successiva indicazione di conservare domande ed esercizi in fondo; quattro originali forniti dall’utente; **«Vai» ricevuto il 16 ottobre 2026 alle 17:39 (Europe/Rome)** sulla proposta e sulla stima aggiornate. Le approvazioni storiche non documentate dalla migrazione non sono ricostruite.

Completato: indice aggiornato, apparati concordati rimossi e **14 quesiti originali integralmente conservati**, in un’unica sezione finale «Domande ed esercizi». Meta, nome e data aggiornati. 1 script conservati con hash identici; nessuna nuova simulazione o modifica del modello. Immagini e risorse incorporate verificate. Template e comandi esistenti preservati.

Peso: 19864994 byte, sopra 18 MB e sotto il limite di 20 MB. Nessuna immagine aggiunta o compressa. Parser con `huge_tree=True` per non troncare le sezioni finali.

Checklist pertinente: A1–A3 (racconto e attività concordate), A4 (formule preservate), A6 (HTML autonomo e accessibile), B4–B6 (riuso, approvazioni, stato), C1–C5 per i materiali presenti, D1–D2.1 (verifiche, versioni, dimensioni, vecchi collegamenti e salvataggio remoto).

Verifiche e hash: [rapporto strutturale](../revisione-blog-verifiche.json) e [prove nel browser](../revisione-blog-browser.json). Superati i controlli a 1440 e 390 px, senza overflow orizzontale né errori JavaScript; sezione finale e indice funzionanti, vecchi URL reindirizzati mantenendo il frammento; otto download effettivi con nomi e contenuti identici. Tutte le immagini HTML sono decodificate; controlli dei grafici e delle simulazioni provati dove presenti. Il permesso tecnico del sandbox è stato concesso dopo la richiesta dell’utente di mostrarlo. Anteprime mobile delle otto dispense e dettaglio del muro ispezionati; indice del bilancio controllato a layout stabile.

Pubblicazione verificata: [esiti HTTPS e confronto dei file](../sito/revisione-blog-online.json). Homepage, otto dispense e otto reindirizzamenti rispondono HTTP 200 con contenuti identici ai file verificati; esclusioni controllate con HTTP 404. Il browser online dell’ambiente ha incontrato un problema di fiducia del certificato e non viene dichiarato verificato; le prove complete nel browser sono quelle locali sugli stessi file. Verifica TLS mantenuta attiva.

Prossima operazione alla chiusura della revisione precedente: nessun intervento allora pendente per quella revisione. Prima di un nuovo lavoro controllare `main`, master e stato; conservare i risultati approvati e i limiti già segnalati.

## Ritorno all’indice generale

Aggiornamento: 2026-10-16 19:30 (Europe/Rome). Richiesta diretta dell’utente: «metti un tasto in ogni capitolo per tornare all’indice». Modifica circoscritta eseguita secondo B2/B5, master v46. Aggiunti due collegamenti «← Indice dei materiali», all’inizio e prima del piè di pagina, con bersaglio HTTPS al sito e `#indice`, utilizzabili anche dalle copie scaricate. Focus visibile e area cliccabile di almeno 44 px. Versione corrente v8; contenuti didattici, immagini, esercizi e script preservati. Collegamenti del sito, download e vecchi URL aggiornati. Stato: completata e verificata. Prove a 1440 e 390 px, clic e Invio, focus visibile e ritorno all’indice riusciti; contenuti scientifici, script e immagini invariati. [Esiti](../sito/ritorno-indice.json). Distribuzione tramite il [workflow Pages](https://github.com/rickymusu-bit/fisica/actions/workflows/pages.yml) dopo l’integrazione in `main`.

## Nomi stabili

Richiesta esplicita dell’utente: rimuovere versione e data dai nomi, conservandole nei documenti. File rinominati, inclusi gli eventuali materiali francesi e albanesi, con identità verificata e contenuti identici byte per byte; versioni interne invariate. Collegamenti correnti aggiornati; per le dispense italiane i vecchi indirizzi pubblici reindirizzano direttamente ai nomi stabili. [Mappa e hash](../sito/nomi-stabili.json). Nessuna revisione scientifica, immagine o simulazione nuova.

## Approvazione del testo sui passaggi e nuovo schema

L’utente affida a sé la ricerca dei materiali («Cerco io») e approva il testo di Passaggi di stato («va tutto bene»), chiedendo di creare uno schema simile alla mappa con le frecce. Schema P1 realizzato in SVG, con disposizione a triangolo e variante verticale per smartphone, controllato nelle due anteprime. [Registro dello schema](../passaggi_di_stato/risorse/schema-passaggi.md). Bozza aggiornata al nuovo schema; HTML ufficiale e pubblicazione invariati. Prossima operazione: consegnare lo schema e attendere i materiali ancora mancanti prima della realizzazione completa.

## Materiali di Stati della materia ricevuti

Otto materiali scelti tramite collegamenti Wikimedia acquisiti e conservati insieme agli originali. [Registro visuali aggiornato](../stati_della_materia/visuali.md). Bozza adattata a ghiaccio in mare, bismuto, vetro, struttura policristallina, viscosità, olio, dirigibile e scarica nell’argon. Il limite di download precedente è risolto per questi file. Il vetro ha originale di 172 × 339 px; restano da fornire le tre GIF del moto particellare. Nessuna modifica all’HTML ufficiale o alla pubblicazione.

## Decisione corrente sulle simulazioni microscopiche

Ultima istruzione dell’utente: **«Mantieni le simulazioni degli stati microscopici»**. Bozza e registro di Stati della materia aggiornati per conservare i tre modelli originali (solido, liquido, gas). La GIF della viscosità resta distinta. La richiesta delle tre GIF sostitutive è superata: per Stati della materia tutti i visuali necessari sono disponibili. Stato corrente nel [file del capitolo](../stati_della_materia/stato.md); nessuna modifica al codice delle simulazioni o all’HTML ufficiale.

## Foto del vetro sostituita

M2 ora è la tartaruga di vetro di Murano scelta dall’utente, originale 2121 × 1414 px: acquisita e verificata con fonte, autore e licenza, registro e didascalia aggiornati. Risolta la limitazione di risoluzione della foto precedente. Tutti i visuali di Stati della materia restano disponibili; le simulazioni microscopiche sono conservate.

## Nuove immagini di Passaggi di stato

C2 (metallo fuso) e A1 (sudore/Michael Jordan) fornite dall’utente, acquisite, ispezionate e registrate con fonte e licenza. Bozza e didascalie aggiornate. [Registro corrente](../passaggi_di_stato/visuali.md). Copertina con CC BY-NC-ND 2.0 da mantenere integra per l’uso non commerciale; credito specifico Jordan registrato. Restano A2–A3 ed E1–E2, con priorità al riuso dei materiali già disponibili. Nessuna modifica al sito.

## Applicazioni aggiornate: pompa di calore e centrale PWR

L’utente elimina il caso e lo schema frigorifero, richiede la sola spiegazione della pompa di calore e fornisce foto A2 e schema nucleare A3. File e originali salvati, fonti/licenze verificate, bozza e domanda 8 aggiornate. A3 trattato come PWR con tre circuiti, non con ebollizione nel reattore. Restano E1–E2; nessun altro visuale applicativo da richiedere. Dettagli nello [stato di Passaggi di stato](../passaggi_di_stato/stato.md).

## Esercizi illustrati e cambio della massa della scultura

L’utente fornisce scultura di ghiaccio e acqua in ebollizione e richiede gli sfondi originali. Foto e originali acquisiti, fonti/licenze registrate; schemi SVG completi preparati e ispezionati. Correzione successiva: «cambia i numeri per adattarli alla statua». Primo problema aggiornato alla scultura intera con massa ipotizzata di **500 kg**, inizialmente a 0 °C: **167 MJ**. Eliminata la porzione da 0,50 kg; nessuna massa reale dedotta dalla foto. Aggiornati il confronto col secondo esercizio e il quesito 5. Secondo problema invariato: 0,20 kg, 451,4 kJ.

Tutti i visuali di entrambi i capitoli sono disponibili. [Bozza Passaggi di stato](../passaggi_di_stato/bozza.md) aggiornata e schemi nel relativo registro. Prossimo passaggio: presentare testi e stima residua 25–40 minuti, raccogliere conferma e via agli HTML secondo B1.1–B2. Nessuna pubblicazione o HTML finale modificati in questa fase.
