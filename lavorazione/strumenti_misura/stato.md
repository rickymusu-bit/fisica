# Stato — Gli strumenti di misura
Ultimo aggiornamento: 24 ottobre 2026 (Europe/Rome). Capitolo 6.
Fase: revisione dei grafici e delle attività in bozza; anteprima aggiornata da revisionare.

## Fonte e ambito
Richiesta corrente: «Facciamo i capitoli 6 e 7», con collegamento al piano.
Ramo corrente: `lavorazione/grafici-misure-leggibili`, da main `3832204ecb1ce05b8d25a135a0709e7228efe94e`.
Sorgente verificato: `strumenti_errori_incertezza_it.html` v7, blob `1d65637b40f2af68e1e1ff55c7d1710259b6087b`, sezioni #strumenti e #caratteristiche.
Confini, visuali identificate e collocazione: [proposta corrente](visuali.md). Misure ripetute, media, semidispersione e incertezza sono riunite nel capitolo 7 per richiesta esplicita; eliminato il capitolo separato sulle ripetizioni.
Domanda iniziale proposta: Una bilancia mostra molte cifre: basta questo per fidarsi della misura?
Template già approvato: Stringhe comune, modello autonomo v24.

## Regole e approvazioni
Letti MASTER_PROMPT.md v69.11, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, docs/visual-guidelines.md v1.0.0 e stato storico del sorgente.
Checklist: A1–A5 per narrazione, monograficità, formule e quesiti; A6 per il tema; B1.1–B2 per visuali → bozza → approvazione → stima e via; B4–B6 per riuso e salvataggi; C1–C4 per immagini e licenze; D1–D2.1 per verifiche e ramo isolato.
L'utente ha approvato l'impostazione e il riuso proposto delle visuali con «Ok», dopo la consegna della PR #72. La richiesta successiva «Ok vai» approva la bozza v4 e autorizza HTML e simulazioni; nessuna nuova conferma di avvio necessaria. Nessuna immagine cercata o generata.
Lo snapshot dei crediti storici dichiara provenienza e diritti non verificati: verificare registro e fonti prima dell'integrazione; il riuso non risolve tale limite.
Simulazione richiesta dall'utente: [specifica](simulazione.md), con modello, comandi, limiti, carico basso e stima preliminare condivisa 2–3 ore, aggiornata per pesetti e grafico. Codice condiviso implementato; nessun video.
[Bozza testuale v4](bozza.md) con segnaposto, formule, una nota e otto domande finali. Avvio autorizzato con «Ok vai» dopo la stima preliminare di 2–3 ore.

## Completato e prossimo passaggio
Controllati sorgente, descrizioni delle nove immagini e sette quesiti. Ripartizione corrente: 1–4 al 6; 5–7 al 7, senza capitolo separato sulle ripetizioni.
Prossimo passaggio: consegnare l’anteprima completa per revisione prima del rilascio. Tutte le immagini richieste sono disponibili; non chiedere nuovamente materiali o via alla realizzazione.
Nuovo HTML v1 e simulazione in lavorazione; nessuna modifica al manifest/catalogo, merge o deployment. Sorgenti storici e traduzioni invariati ed esclusi. Verifiche della fase HTML nel rapporto verifiche-browser.json; le note delle precedenti fasi restano cronologia.
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

## Realizzazione autorizzata — HTML v1

L'utente risponde «Ok vai»: bozza v4 e realizzazione dei due HTML/simulazioni autorizzate, dopo la stima preliminare 2–3 ore. Tema Stringhe v24 riusato; CSS/JS incorporati e MathML nativo. Copertine scelte acquisite dagli originali Wikimedia e incorporate intere senza zoom. Provenienze e attribuzioni nel registro unico e nei crediti autonomi. Nessuna nuova immagine cercata o generata.

Codice del modello e renderer condivisi in ../strumenti_misura/simulazione.js, simulazione.css e realizza.py. Nel 6 selezione/rimozione dei pesetti, somma delle masse, slider, fuori scala, lettura anticipata e stabilizzata, zero e disturbi. Nel 7 campioni separati, acquisizioni indipendenti, media/semidispersione e U scolastica, controllo delle risposte e grafico con ingrandimento canonico e riferimento soltanto per la massa nota. Il valore interno del campione B non è esposto in interfaccia o grafico.

Anteprima corrente in bozza.html e nel file autonomo alla radice; simulazione già utilizzabile con controlli testuali. In attesa delle immagini, gli spazi visuali sono dichiarati: non presentare questi HTML come anteprime grafiche complete o capitoli pronti alla pubblicazione. L'utente chiede l'elenco e intende fornire i materiali; elenco inviato in chat: bilancia digitale, pesetti 10/20/50/100/200 g, campione senza massa scritta; per il corpo bilancia analogica, parallasse, voltmetro 0–15 V, termometro, cronometro e bersagli.

Verifiche: test quantitativi del modello; browser desktop/mobile e chiaro/scuro, calcoli, grafico, tastiera, note, crediti, download e HTML caricato in memoria con rete disabilitata. La navigazione file:// è bloccata dalla policy del Chromium dell'ambiente e non è dichiarata eseguita. Rapporti nelle verifiche JSON e schermate in anteprime/. Crediti, tema e build Pages controllati senza ammettere i nuovi capitoli nel manifest. Sorgenti storici e articoli pubblicati invariati.

Passi della versione esplorativa rivisti a 1/20/50 g per distinguere l’effetto della risoluzione con i pesetti disponibili, tutti multipli di 10 g. Verificato che 10 g siano indicati come 20 g con passo 20 g e come 0 g con passo 50 g; riferimento fisso 1 g nel capitolo 7. Nessuna nuova immagine richiesta per questa scelta.

Verifica finale consolidata in verifiche-finali.json: 7 test quantitativi passati, 20 combinazioni viewport/tema, nessun errore JavaScript o richiesta esterna, crediti/tema/build superati. I due HTML restano esclusi dall’output pubblico; file alla radice e bozza.html identici. Salvataggio sul ramo della PR #72; integrazione immagini ancora aperta.

## Bilancia analogica e parallasse — HTML v2, 24 ottobre 2026

Richiesta dell’utente: Kitchen scale 20101110.jpg e ricreazione del riferimento Vecteezy se non riutilizzabile. Bilancia Batholith PD-self documentata, originale acquisito e incorporato intero in FIG-06-1a. Didascalia aggiornata a 2 kg / divisioni 10 g; eliminato dalla nota il vecchio inciso “sensitivity 20 g”.

Fonte Vecteezy classificata Pro Vector / Pro Standard License; nessuna licenza Pro documentata. L’anteprima commerciale è usata solo come riferimento e non salvata nel repository o incorporata nel capitolo. Creato schema originale con elemento dell’occhio generato su richiesta, linee e scala SVG deterministiche. Intersezioni verificate 4/5/6 cm, stesso indice; scritte italiane. Nessuna generazione dei numeri o delle proiezioni geometriche. Originale generato preservato; composizione e provenienza nella cartella risorse.

Bozza v5 e HTML v2 al percorso stabile; renderer esteso per fotografie verticali e schemi ingrandibili con il componente canonico. Nessuna modifica al modello comune o alla simulazione. Verifiche mirate alle due immagini su cinque larghezze e due temi (10 combinazioni), byte incorporati, note, ingrandimento, tastiera, offline, crediti e build. Rapporti in verifiche-immagini.json e verifiche-finali.json; schermate aggiornate delle due figure in anteprime/. Le verifiche del modello numerico e dei comandi precedenti restano valide: relativo codice invariato.

Restano FIG-06-1b, FIG-06-3/4/5 e immagini della bilancia digitale/pesetti/campioni della simulazione. Capitolo 7 v1 invariato; nessun articolo pubblico, manifest o catalogo modificato. Prossimo passaggio: continuare l’integrazione degli altri materiali forniti. La ricreazione e l’inserimento richiesti non necessitano di una nuova conferma; pubblicazione ancora non autorizzata.

### Correzioni dello schema richieste dall’utente

Base dell’oggetto portata allo zero (y = 750, stessa quota dello zero della scala); estremità superiore mantenuta a 5 cm. Aggiunto il collegamento visivo base–zero. Rimosse “vista laterale schematica” e la descrizione accanto all’oggetto che sostituiva “indice fermo davanti alla scala”, insieme alla relativa linea di richiamo. Linee di vista invariate e geometricamente corrette. Schema, PNG di anteprima, HTML e schermate riallineati nella stessa revisione v2.

## Essenzialità richiesta — HTML v3

Recepita la richiesta di non dichiarare ciò che è già evidente dalle immagini o dal contesto. Schema ripulito da titoli interni, descrizioni delle posizioni e precisazioni ridondanti; omesse le didascalie tautologiche delle due figure integrate. Geometria invariata. Master aggiornato a v69.12, C3/A6; riferimento di stile v7. HTML v3 e bozza v6; verifiche mirate e anteprime aggiornate. Nessun rilascio.

## Matita e indicazioni di vista — HTML v4

L’utente richiede un oggetto riconoscibile, una matita, e il ripristino di “Vista dall’alto”, “Vista frontale”, “Vista dal basso”, ritenute utili. Matita generata come elemento isolato, originale preservato e copia in risorse/matita-generata.png; sostituita la sagoma. Posizione ottenuta con sola rotazione e scala uniforme: punta e base nelle coordinate precedenti, senza deformazione. Geometria, linee di vista e zero invariati. Ripristinate esattamente le tre indicazioni richieste; non eliminarle come ridondanti nelle prossime revisioni. Nessuna nuova didascalia. Bozza v7, HTML v4; crediti e verifiche mirate aggiornati.

## Bilancia e pesetti generati — 24 ottobre 2026

Autorizzazione esplicita dell’utente: «Per la simulazione, genera tu la bilancia e i pesetti». Generati gli originali, lasciati intatti nella cartella generated_images e copiati nella lavorazione. Bilancia e set di pesetti integrati nelle due simulazioni; display attivo sulla finestra dello strumento, immagini dei carichi sul piatto e controlli testuali/accessibili. Campione ignoto rappresentato da pesetto senza massa scritta. Immagini riutilizzate nelle figure della stessa bilancia nel testo. Dati e proprietà del modello invariati.

Implementate definizioni SVG condivise per incorporare una sola volta ciascun originale e limitare il peso dei file senza comprimere o alterare le immagini. Lettura fuori scala OL con messaggio esplicito; selezione, rimozione e ripristino riallineano immagini e letture. Provenienza in ../strumenti_misura/risorse/bilancia-pesetti-fonte.json e registro unico; nessun materiale esterno introdotto. Restano quattro immagini per la teoria: voltmetro 0–15 V, termometro digitale, cronometro e bersagli. Nessuna immagine aggiuntiva necessaria per le simulazioni.

Verifiche concluse: 7 test quantitativi, 20 combinazioni di viewport e tema, interazioni aggiornate e carico dei cinque pesetti; nessun errore JavaScript o richiesta esterna. Crediti, tema e build superati. HTML e copie di lavorazione identici; capitoli esclusi dalla pubblicazione.

## Immagini teoriche completate — 24 ottobre 2026

L’utente ha fornito il manometro MAXIMATOR in sostituzione del voltmetro, il termometro clinico a colonna e il cronometro digitale e ha chiesto di ricreare i bersagli Ossila. Fotografie scelte incorporate intere, senza cambiare scale o display; metadati Commons verificati e conservati. Manometro: Photo by CEphoto, Uwe Aranas, CC BY-SA 3.0. Termometro: Jacek Halicki, CC BY-SA 4.0. Cronometro: Lesselich, CC BY-SA 3.0. Schede e associazioni nel registro unico, crediti offline aggiornati.

Esempio della portata e domanda finale adattati alla scala nera 0–2500 bar, con pressione attesa di 3000 bar. Prontezza descritta attraverso il termometro a colonna. Il cronometro azzerato illustra lo strumento; l’apertura del capitolo 7 presenta esplicitamente i tempi come ipotesi, conservando tutti i dati e calcoli dell’esempio.

Bersagli ricreati con SVG originale deterministico ed etichette italiane: colonne precisione alta/bassa, righe accuratezza alta/bassa; A e C in alto, B e D in basso. Nessun elemento grafico del file Ossila incorporato. Geometria verificata dal generatore; file e provenienza in lavorazione/errori_incertezza_misura/risorse/. Omesse didascalie che ripetevano testo o immagine; conservate le tre viste del parallasse. Nessuna immagine ancora da fornire. Versioni HTML correnti: capitolo 6 v6, capitolo 7 v3.

Verifiche finali completate sulla versione corrente: 20 combinazioni di viewport e tema con tutte le interazioni, download e offline; altre 8 combinazioni per le nuove fotografie, crediti e zoom dei bersagli. Nessun errore JavaScript o richiesta esterna. Tutti gli slot immagini risolti; HTML e copie di lavorazione identici. Crediti, tema e build superati. Simulazioni e modello fisico invariati.

## Correzioni richieste: fotografia, sensibilità, didascalie e pesetti — 24 ottobre 2026

Nel capitolo 6 FIG-06-1b ora usa la fotografia 2023_Elektroniczna_waga_kuchenna.jpg scelta dall’utente, Jacek Halicki, CC BY-SA 4.0; scheda Commons conservata in risorse/bilancia-digitale-fonte.json e attribuzione nel registro unico. La bilancia generata resta nella simulazione. Sensibilità spiegata con il solo confronto discorsivo con la risoluzione, senza formula, definizione con simboli o tabella degli allungamenti. Ripristinate didascalie brevi e pertinenti per tutte le figure del corpo dei due capitoli; conservate le scritte delle tre viste del parallasse.

Pesetti sul piatto con massa visibile sovrapposta all’immagine. Nel 7 il riferimento porta 100 g; il campione ignoto porta B, senza rivelare la massa. Modello quantitativo invariato. HTML correnti: capitolo 6 v7 (bozza v10); capitolo 7 v4 (bozza v7). Richieste esplicite dell’utente autorizzano queste modifiche.

Su ulteriore richiesta dell’utente, FIG-07-2 sostituita con il voltmetro Вольтметр_4.jpg (Желуденко Павло, CC BY 4.0). Testo, didascalia, richiamo dopo i bersagli e quesiti coerenti con l’offset negativo; nessun valore numerico dell’offset inventato. Simulazione con bilancia generata invariata.

Verifiche correnti concluse: 7 test quantitativi, 20 combinazioni di viewport e tema e 8 controlli mirati alle figure con didascalie e ai crediti. Etichette dei cinque pesetti verificate; nessun errore JavaScript o richiesta esterna. Download, offline, crediti, tema e build superati. HTML e copie di lavorazione identici, file pubblici invariati. Anteprime aggiornate pronte nella PR #72.

## Fotografia della misura del tempo, zoom e verifica delle simulazioni

Nel capitolo 7, foto del cronometro sostituita su richiesta con la scena U.S. Navy di un istruttore che cronometra la corsa delle reclute: Chris Desmond / U.S. Navy, pubblico dominio PD-USGov-Military-Navy, fonte Commons conservata. Bersagli senza zoom per richiesta esplicita; soglia operativa per future scelte documentata in docs/visual-guidelines.md: scritte necessarie sotto 14 CSS px nella vista normale su schermo da 320 px o dettagli indispensabili illeggibili. La soglia è condizione necessaria, non obbligo automatico di zoom; fotografie e figure con poche scritte restano escluse.

Segnalazione dell’utente: tutte le simulazioni non funzionano. Richiesto in quale contesto (anteprima della chat, HTML scaricato o sito); risposta ancora attesa. Prova attuale in Chromium, 390 px, movimento normale e timer reali: entrambe le bilance inizializzate, due letture registrate ciascuna, nessun errore JavaScript. Il difetto non è riprodotto nel browser di prova; nessuna correzione dichiarata senza causa verificata. Nessuna modifica al modello o al codice delle simulazioni.

## Parallasse senza zoom

Su richiesta esplicita dell’utente, rimosso lo zoom da FIG-06-2. Immagine, didascalia e tre indicazioni di vista conservate. HTML v8. Resta aperta la diagnosi delle simulazioni: attesa la modalità di apertura dall’utente.

## Bilancia da cucina: grammi e pesetti più grandi

L’utente conferma che le simulazioni funzionano nell’HTML scaricato: la precedente segnalazione non descrive un malfunzionamento del file autonomo. Richiede di eliminare i millivolt, usare grammi per la sensibilità, ingrandire i pesetti e mostrare le masse con aspetto inciso.

Rimosso il pannello del segnale e lo slider del guadagno elettrico. Il controllo unico «Sensibilità (passo leggibile)» usa 1, 20, 50 g e regola la quantizzazione; la convenzione scolastica è chiarita nella nota già presente, senza cambiare il confronto qualitativo della teoria. Proprietà della bilancia del 7 riportate senza millivolt. Registro in grammi; nessun guadagno elettrico esposto.

Pesetti sul piatto ingranditi da 16 a 28 unità relative alla larghezza della bilancia, altezza minima 36 px; più spazio sopra il piatto, con display riallineato alla finestra originale. Etichette senza fondo o cartellino, colore e rilievo leggero per simulare incisione; campione B senza massa esposta. Originali raster preservati, nessuna alterazione delle masse reali del modello. HTML: capitolo 6 v9, capitolo 7 v8.

Verifiche concluse sulla revisione corrente: 7 test quantitativi, 20 combinazioni di viewport/tema, tutte le interazioni, download, offline e no-JS; nessun errore o richiesta esterna. Masse visibili e pesetti interamente nel riquadro a 390 e 1440 px. Crediti, tema e build superati; HTML e copie di lavorazione identici. Sorgenti pubblici e manifest invariati.

## Precisione, accuratezza e incertezza senza qualificazioni ripetute

Su richiesta esplicita, nel 6 gli slider presentano soltanto concetti già introdotti: «Accuratezza» e «Precisione», con scala qualitativa da Molto bassa ad Alta. Aumentare il controllo riduce rispettivamente lo spostamento costante e l’ampiezza della variabilità; valori iniziali Alta per entrambi, modello interno 0 g. Registro aggiornato con gli stessi nomi qualitativi. Parametri tecnici conservati soltanto nel codice.

Nel 7 eliminata la qualificazione didattica/scolastica da testo corrente, tabella, campi, grafico, aiuti, risposte e confronto. Si usa «incertezza U». Limite del criterio spostato nella nota finale già associata alla formula: cenno breve alla deviazione standard come dispersione di tutte le letture rispetto alla media, senza formule nuove. Regola U=max(d,q), dati e risultati invariati. HTML correnti: capitolo 6 v10, capitolo 7 v9.

Verifica conclusa: 7 test quantitativi e 20 combinazioni viewport/tema con interazioni, download e offline superati. Ripristino ad Alta, mappatura dei controlli, etichette e testo controllati; nessun errore JavaScript o richiesta esterna. Crediti e build superati; HTML e copie di lavorazione identici.

## Pubblicazione sospesa e attività del 7 separate

L’utente aveva autorizzato la pubblicazione con «Va bene publica», poi ha interrotto esplicitamente con «Aspetta» e richiesto la separazione delle simulazioni. Nessun push, merge o deployment è avvenuto; la pubblicazione resta sospesa in attesa della revisione del risultato nuovo. Il recupero di origin/main è stato eseguito, ma il tentativo di integrazione non ha modificato la working tree.

Capitolo 7 ora con due sezioni: «Stimare l’incertezza di una massa ignota» e «Misurare l’errore rispetto a una massa nota». Ogni sezione ha propria bilancia, campione fisso, registro, campi di calcolo e grafico; nessun selettore comune. Incertezza: campione B, media, semidispersione e U; grafico con una sola serie, estremi e fascia. Errore: campione A di 100 g, media ed errore; grafico con una sola serie, riferimento e scarto. Calcoli, cancellazione e ripristino indipendenti. Identificativi dei grafici e delle copie zoom univoci.

Modello numerico, proprietà fisse e masse conservati; nessun valore nascosto B esposto come riferimento. Grafici singoli con annotazioni separate dai punti, senza le due righe sovrapposte del confronto precedente. HTML capitolo 7 v10, bozza v12. Codice condiviso aggiornato anche nell’HTML del 6 v11, con attività del 6 invariata.

Verifica conclusa: 7 test quantitativi e 20 combinazioni viewport/tema, due attività e grafici indipendenti, cinque letture/calcoli per entrambe, reset/cancellazione isolati, limiti delle acquisizioni, download/offline/no-JS superati. Nessun errore JavaScript o richiesta esterna. Crediti e build superati; manifest pubblico invariato. Anteprime specifiche delle due attività salvate; nessuna pubblicazione effettuata.

## Pubblicazione nuovamente autorizzata

L’utente approva la versione con le due attività separate con «Okay, pubblica». Questa autorizzazione supera la sospensione precedente e riguarda l’anteprima corrente. Integrato main, inclusa l’implementazione Quiz già pubblicata e il principio di economia informativa; conflitti solo documentali risolti conservando le istruzioni correnti.

Aggiunti i due capitoli al manifest e al catalogo italiano, aggiornati i collegamenti 5 → 6 → 7 e il passaggio alla Termologia, con ritorno dalla Termodinamica al 7. Crediti pubblici generati dal registro unico; date editoriali dei nuovi capitoli aggiornate. Nessun contenuto scientifico degli altri capitoli modificato. Contenuto del corpo dei due capitoli identico nella build pubblica; comandi di zoom resi idempotenti rispetto alla componente canonica.

## Grafici ravvicinati e simulazioni senza campi di calcolo

Richiesta esplicita successiva alla pubblicazione: ridurre l’intervallo di entrambi i grafici per leggerli senza zoom; rimuovere le parti in cui lo studente inserisce i calcoli e lasciare esercizi nelle domande. Nuovo ramo isolato dalla versione pubblicata; nessun aggiornamento del sito autorizzato per questa nuova anteprima.

Assi adattati alle letture raccolte, includendo riferimento o fascia U e un margine; ampiezza minima 8 g, anziché i precedenti 50 g. Dominio uguale sui dispositivi, meno etichette sull’asse negli schermi piccoli, caratteri effettivi di almeno 14 CSS px. Dimensioni del grafico aggiornate quando cambia la larghezza. Nessuno zoom e nessuno scorrimento orizzontale per i grafici delle due bilance. Riepiloghi automatici di media/d/U o media/errore conservati.

Rimossi campi di risposta, pulsanti di controllo/confronto e aiuto ai calcoli. Istruzioni delle attività orientate all’osservazione; due esercizi di calcolo nelle domande finali (9 e 10), mantenendo i primi otto quesiti. Controlli di acquisizione, limiti delle letture e indipendenza delle bilance invariati. HTML 7 v11 (bozza v13); HTML 6 v12 per il codice condiviso, attività del 6 invariata.

Verifica completata: 7 test quantitativi, 19 test del portale e 20 combinazioni viewport/tema. Testo dei grafici almeno 14 px effettivi, scale ravvicinate, nessuno zoom e nessun modulo di calcolo; dieci domande finali. Misure, registri, indipendenza, download e offline superati. Crediti, tema e build superati. Immagini delle due scale mobile/desktop ispezionate. Nessuna modifica al sito ufficiale.

## Portata, risoluzione e pannello richiudibile

Successiva richiesta dell’utente: portata massima 500 g, nome corretto Risoluzione per il passo minimo leggibile e comando per collassare gli slider del capitolo 6. Implementate portate 200/300/500 g, valore iniziale 500 g. Corretto il nome nel controllo, nel registro e nelle istruzioni; eliminata dalla nota la precedente attribuzione alla sensibilità del controllo della bilancia. Confronto teorico tra sensibilità e risoluzione conservato.

Proprietà raccolte in details nativo inizialmente aperto, con summary «Proprietà della bilancia», area di almeno 44 px e tastiera. Chiudere/riaprire non modifica letture o impostazioni; i pulsanti di registrazione e ripristino si avvicinano alla bilancia. Versioni aggiornate: capitolo 6 v13 (bozza v13), capitolo 7 v12 (bozza v13), quest’ultimo per il codice condiviso. Restano i grafici ravvicinati senza zoom e i calcoli nelle domande del 7. PR #76 in bozza; nessuna pubblicazione nuova autorizzata.

Controlli completati: portata massima 500 g, fuori scala a 300 g con 380 g caricati, riapertura del pannello senza perdita delle impostazioni e tastiera; schermate del pannello chiuso a 390 e 1440 px. Superati 7 test quantitativi, 19 test del portale e 20 combinazioni viewport/tema, più interazioni aggiornate, download e offline. Nessun errore JavaScript o richiesta esterna.

## Pulizia dei riferimenti alla configurazione e alla natura dei valori

Su richiesta esplicita, rimossi «Configurazione N», la relativa colonna del registro e il termine configurazione dai messaggi del capitolo 6. Conteggio e separazione interni delle serie conservati per il funzionamento dei comandi, senza esporli nel testo. Rimossa la dicitura «Valori simulati» dalle tre attività e la frase equivalente nelle istruzioni del 6. Dati del modello, formule, controlli e registri restano funzionanti. HTML correnti: capitolo 6 v14 (bozza v14), capitolo 7 v13 (bozza v13). Revisione aggiunta alla PR #76 in bozza, senza pubblicazione.
