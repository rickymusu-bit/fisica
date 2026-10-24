# Stato — Il piano cartesiano

**Stato corrente — revisione richiesta il 24 ottobre 2026:** HTML v4 verificato; bozza testuale v5. Le nuove istruzioni dell’utente superano le precedenti scelte di riuso delle fotografie, prezzo a 2 € e zoom interattivo. Pubblicazione subordinata all’approvazione della nuova anteprima.

## Riferimenti e autorizzazioni

Progettazione v3 — 24 ottobre 2026, Europe/Rome. Master consultato: v69.15; istruzioni AGENTS.md, piano dell'area, STILE_DISPENSE.md v7, esempio_irraggiamento.md e docs/visual-guidelines.md. Checklist: A1–A5 (narrazione, formule, monograficità, domande), B1.1–B2 (visuali prima della bozza e approvazioni), B4–B6 (riuso e continuità), C1–C4 (immagini, grafici, accessibilità), D1–D2.1 (verifiche e salvataggio). Applicare economia informativa a testo, figure e didascalie.

Richiesta effettiva: «Iniziamo a creare i capitoli 8 e 9 del piano di lavorazione sull'introduzione alla fisica». Autorizzato l'avvio della progettazione. Le nuove scelte visuali, la bozza completa, la realizzazione HTML e la pubblicazione non sono ancora approvate. Tema comune Stringhe già approvato, da riutilizzare nella successiva fase HTML senza una nuova scelta.

Fonte verificata: grafici_piano_cartesiano_it.html, versione interna v8, blob 9befd930b57d847869b7cc6e9f131e01050223f3. Consultato anche lo stato storico lavorazione/grafici_piano_cartesiano/stato.md. Il manifest corrente esclude il sorgente unificato: consultato, non modificato né riammesso. Il piano iniziale conserva passaggi storici: il manifest corrente include già i capitoli 1–7. Nessun intervento a main, manifest, catalogo o sito pubblico.

Ramo dedicato derivato da main: lavorazione/introduzione-capitoli-8-9. File di stato e proposta salvati; nessuna bozza integrale o HTML realizzati. Revisione preliminare svolta sul testo, sui grafici SVG e sul codice delle interazioni; non si dichiarano prove nel browser o verifiche delle licenze non eseguite.

## Argomento e confini

Capitolo 8 di Introduzione alla fisica e alla misura. Sorgente: sezione «Due grandezze, una coppia di coordinate» e interazione «Trascina P». Titolo futuro proposto: piano_cartesiano_grafici_it.html.

Percorso proposto: una coppia di dati diventa un punto; assi, origine e ordine (x; y); ascissa e ordinata; valori negativi e quadranti; grandezze e unità sugli assi; scelta e lettura delle scale; passaggio tabella–grafico e lettura di un andamento. Distinguere la lettura delle coordinate dalla ricerca della legge che lega le grandezze. Pendenza, intercetta e classificazione delle relazioni appartengono al solo capitolo 9.

Domanda iniziale proposta: come possiamo rappresentare due informazioni riferite alla stessa osservazione e leggere dal grafico come cambia una grandezza?

## Visuali proposte, da concordare

- C8-COP: fotografia reale di un grafico su carta millimetrata, copertina senza zoom e senza riutilizzo nel corpo. File da scegliere e fornire dall'utente. Il vecchio grafico del petrolio è disponibile, ma non viene scelto automaticamente: densità, lingua, fonte dei dati e diritti devono essere verificati prima di un riuso; la lunga spiegazione sui dollari del 2022 introduce un prerequisito economico non necessario.
- C8-INT: riutilizzare il piano cartesiano già presente, con punto P trascinabile, proiezioni tratteggiate, coordinate aggiornate e riconoscimento del quadrante o dell'asse. Il codice corrente limita x e y a [−5; 5] e arrotonda ai decimi; mouse/tocco e frecce da tastiera già previsti. Mostrare una sola lettura delle coordinate, evitando duplicazioni di etichette. È un'interazione matematica, senza modello dinamico o misure sperimentali.
- C8-TAB/GRA: tabella breve e corrispondenti punti nello stesso piano; possibile riuso delle coppie dei quaderni (0;0), (1;2), (2;4), (3;6), (4;8), senza introdurre la legge. Ogni coppia deve essere riconoscibile. L'esempio dei quaderni, se mantenuto nel racconto, richiede l'immagine della situazione concordata per il capitolo 9, oltre al grafico.
- C8-SCA: confronto statico dello stesso insieme di dati con due scale verticali uniformi differenti, per mostrare che la lettura dipende dalle tacche e che l'inclinazione apparente non è una variazione dei dati. Evitare assi troncati in questa prima introduzione. Nuovo confronto proposto, non ancora realizzato.

Il materiale copertina e lo schema della situazione sono da scegliere; non sono state cercate o generate immagini nuove. Le figure conserveranno la composizione su smartphone. Assi, unità, scale e descrizioni accessibili restano; omettere didascalie che ripetono assi o istruzioni già espliciti.

## Domande e continuità

Conservare il quesito originale 2 (spostare P nei quadranti e su un asse). Il quesito originale 1 riguarda il petrolio: se quel grafico viene mantenuto, conservarlo; se viene sostituito, conservarne la funzione di lettura di assi/dati adattandolo alla nuova immagine e registrando la sostituzione nella bozza. I quesiti originali 3–7 appartengono al capitolo 9 unificato. Non duplicare né perdere i quesiti nella suddivisione. In bozza definire le ulteriori domande su coordinate invertite, scale e lettura di una tabella, senza soluzioni automatiche.

## Fattibilità e prossima operazione

Riuso tecnico leggero, senza librerie o servizi esterni. Prima del riuso verificare isolamento degli identificativi, inizializzazione della lettura, estremi, passaggio sugli assi, tocco e tastiera, fallback e contrasto. Stima preliminare per adattamento e prove della sola interazione: 20–40 minuti, carico basso; non è un tempo misurato. Alternativa più semplice: piano statico con punti già assegnati, meno esplorazione autonoma; non preferita perché l'interazione esiste.

Fase corrente: proposta di contenuti e visuali. Prossimo passaggio: concordare riuso, confronto delle scale e immagini; poi scrivere bozza.md completa con segnaposto. Dopo approvazione della bozza, comunicare stima totale ripartita e raccogliere il via alla realizzazione secondo B1.1. Nessun HTML prima di quel passaggio.

## Decisione corrente — 24 ottobre 2026

L’utente richiede un capitolo sul piano cartesiano e uno su tutte le relazioni di proporzionalità. Titolo corrente del capitolo 8: «Il piano cartesiano». Il piano complessivo passa a nove capitoli; tutti i precedenti rinvii a capitoli 10–11 sono superati. Le visuali sopra restano proposte, non approvate per effetto dell’accorpamento. Prossimo passaggio: scelta delle visuali e poi bozza.

## Bozza v1 pronta — 24 ottobre 2026

«Va bene, procediamo» autorizza la stesura sulla struttura concordata. [Bozza v1](bozza.md) completa: coordinate e quadranti, interazione esistente, tabella–punti, lettura delle scale e confronto delle stesse coppie con scale diverse; otto domande finali. Copertina e immagine del quaderno restano segnaposto da scegliere, non immagini approvate. Quesito originale 2 conservato; originale 1 adattato dal petrolio ai quaderni per evitare il prerequisito sui dollari del 2022.

Richiesta successiva: esclusione dell’intercetta dal capitolo 9. La ripartizione corrente dei quesiti originali è 1–2 nel capitolo 8, 3/6/7 nel 9; 4–5 esclusi dai nuovi capitoli e conservati nel sorgente storico. Questo supera la ripartizione iniziale 3–7 al 9.

Verificati valori della tabella, coordinate, segni dei quadranti e corrispondenza dei segnaposto. Nessuna prova browser pertinente in questa fase testuale. Fase corrente: revisione della bozza; HTML e pubblicazione non avviati.

## Bozze approvate — passaggio ai materiali, 24 ottobre 2026

Dopo la consegna della bozza v3 del capitolo 9, l’utente risponde «Okay, procediamo». Approvate le bozze correnti: capitolo 8 v1 e capitolo 9 v3, con viaggio di 120 km per l’inversa ed esclusione dell’intercetta. L’indicazione autorizza il proseguimento, senza approvare implicitamente immagini nuove o pubblicazione.

Ricerca interna testuale per quaderno e treno senza risultati: non è emerso un materiale pertinente con provenienza e licenza già documentate. La ricerca non dimostra l’assenza di immagini non indicizzate. Occorrono due copertine e immagini del quaderno e del treno per gli schemi; nessuna ricerca esterna o generazione avviata. La fornitura delle immagini resta il prossimo passaggio necessario ai sensi di C1–C2; non realizzare un HTML definitivo con segnaposto.

Stima preliminare totale per entrambi gli HTML, una volta disponibili i materiali: 60–100 minuti, carico basso. Preparazione e verifica materiali 10–20 min; integrazione testo e figure 25–40 min; adattamento interazioni 10–20 min; verifiche e salvataggio 15–20 min. L’attesa delle immagini è esclusa; eventuali problemi di licenza o resa mobile possono ampliare il tempo. Stima da comunicare all’utente, senza garantire tempi misurati. Nessun HTML, merge o deployment eseguito.


## Realizzazione completata nella PR 79 — 24 ottobre 2026

La richiesta corrente «Finisci il lavoro della pr 79 sul mio repo di fisica», con i quattro URL e l’indicazione di usare i libri nel capitolo 9, autorizza il completamento degli HTML e l’integrazione dei materiali scelti. Non occorre una nuova scelta delle stesse immagini. Il prezzo illustrativo resta 2 €/libro; il contesto è una vendita ipotetica di libri usati, senza attribuire prezzi alla biblioteca fotografata. Per continuità lo stesso esempio sostituisce i quaderni anche nel capitolo 8, conservando dati e funzione dei quesiti. La foto del treno identifica il mezzo, mentre il viaggio di 120 km resta un modello ideale senza fermate e a velocità costante.

Materiali: Playfair_TimeSeries-1.png per la copertina dell’8 (William Playfair, pubblico dominio); Hyperbolic_orthogonal_dodecahedral_honeycomb.png per la copertina del 9 (Tomruen, Curved Spaces di Jeff Weeks, pubblico dominio); Library_at_the_biltmore_estate.jpg per i libri (JoyD Smiths PTMr8, CC0); Las_Vegas_monorail_Excalibur.jpg per il viaggio (ArticCynda, CC BY-SA 4.0). Immagini intere, senza ritagli, conversioni o rimozione dello sfondo; file e risposte API originali nelle risorse, schede uniche in risorse/crediti.json. La fonte in wikitesto documenta autore e PD-self della copertina del 9. La biblioteca è conservata una sola volta nella lavorazione del capitolo 8 e incorporata in entrambi gli HTML autonomi.

Tema canonico v24 riutilizzato senza modificare le componenti condivise. Nuovi HTML stabili: piano_cartesiano_grafici_it.html e relazioni_proporzionalita_it.html, entrambi v1; copie di lavorazione in bozza.html con percorsi relativi adattati. Rigenerazione comune: `python lavorazione/piano_cartesiano_grafici/realizza.py`. Il sorgente storico unificato è consultato e rimane invariato. Le otto e nove domande sono conservate; nessuna soluzione aggiunta. Nessuna sezione sull’intercetta.

Completati piano P trascinabile da −5 a 5, tastiera e proiezioni, punti della tabella e confronto affiancato delle scale; diretta, inversa e quadratica con comandi mostra/nascondi, frazioni MathML, schema del viaggio e quadrati in scala. Nello zoom del piano viene spostato lo stesso elemento interattivo, evitando identificativi duplicati e coordinate fuori sincrono. Grafici piccoli ingrandibili; copertine e fotografie senza zoom. Figure con poche etichette verificate a 320 px: viaggio e quadrati mantengono testi di almeno 14 CSS px; i grafici più densi hanno zoom e scorrimento. Composizione invariata su mobile.

Verifiche: Chromium su 320/390/1440 px in chiaro e scuro, nessun overflow; decodifica di tutte le immagini; assi/proiezioni privi di riempimenti; tastiera, passaggio sugli assi, quadranti, limiti e trascinamento; zoom e fallback senza JavaScript; mostra/nascondi e aria-pressed; indice, note e ritorni, crediti con OFL Lexend. Nessun errore JavaScript o richiesta esterna nei capitoli. Rapporti verifiche-browser.json e schermate aggiornate in anteprime/. Il browser gestito impedisce file://: le prove usano HTTP locale, con tutte le risorse del capitolo incorporate e assenza di richieste esterne; non si dichiara una prova file:// non eseguita.

Controlli scientifici: i prezzi 0/2/4/6/8 € seguono il costo unitario di 2 €/libro; ogni prodotto velocità-tempo della tabella vale 120 km; 120/100 = 1,2 h = 1 h 12 min; aree 0/1/4/9/16 cm² e fattori 4/9 per raddoppio/triplicazione del lato. I quesiti restano coerenti. HTML sotto 18 MB: circa 4,4 MB per l’8 e 14,5 MB per il 9, senza modificare gli originali delle immagini.

`python scripts/credits.py --check` e `python scripts/build_pages.py` superati. Nessuna associazione grafica priva di credito nei due nuovi documenti. Registro aggiornato per i nuovi capitoli, pagina pubblica dei crediti e componenti degli altri capitoli invariati. Manifest, catalogo, capitoli pubblicati e sorgenti esclusi invariati; i due nuovi capitoli restano fuori dall’output ufficiale della build.

Prossima operazione: approvazione dell’anteprima corrente da parte dell’utente. AGENTS.md richiede di «presentare prima l’anteprima corrente e attendere sempre l’approvazione esplicita dell’utente prima di integrare main o avviare GitHub Pages». PR mantenuta in bozza; nessun merge o deployment ufficiale eseguito.


Salvataggio remoto verificato: commit `949647f5643410b84b22f14c55ae974781137f7c` sul ramo della PR #79. [Anteprima interattiva corrente](https://raw.githack.com/rickymusu-bit/fisica/949647f5643410b84b22f14c55ae974781137f7c/piano_cartesiano_grafici_it.html), HTTPS 200, tipo text/html e byte identici all’HTML locale. Rapporto [verifica-anteprima-online.json](verifica-anteprima-online.json). Nessuna pubblicazione ufficiale eseguita.


Allineamento con main ef29a4f (revisione già pubblicata nella PR #80): risolto il solo conflitto in risorse/crediti.json partendo dal registro aggiornato di main e reinserendo le associazioni dei nuovi capitoli. Conservate integralmente le modifiche degli altri capitoli presenti in main. Rigenerazione, controllo dei crediti e build superati; i due nuovi HTML rimangono identici byte per byte alle anteprime verificate sopra.


## Revisione richiesta dall’utente — 24 ottobre 2026

Autorizzate correzioni sostanziali sulle anteprime della PR #79: spiegazione più sviluppata di variabili e assi; nessun esempio dei libri nel capitolo 8; divieto permanente di riciclare immagini ed esempi tra capitoli; zoom solo dove le scritte sono troppo piccole e nessuno zoom sui grafici interattivi correnti; legame tra punti e curve, significato grafico di k, didascalie; schemi originali al posto delle fotografie degli esempi e prezzo dei libri più realistico. La richiesta è già il via alla revisione, senza un nuovo passaggio di conferma. Non autorizza la pubblicazione.

Master aggiornato a v69.16 integrando la regola in A3/B4, senza introdurre contraddizioni con il riuso delle componenti tecniche. AGENTS.md registra la regola, le didascalie e il perimetro dei grafici senza zoom. Schemi originali degli oggetti autorizzati espressamente dalla richiesta, che prevale sul divieto generale di disegnare autonomamente soggetti al posto di fotografie. Nessuna ricerca esterna o generazione di immagini necessaria: geometrie scientifiche e schemi costruiti in SVG deterministico.

Capitolo 8: nuovo esempio esclusivo del serbatoio (nessun riuso rilevato nei 17 capitoli ammessi), con ingresso ideale di 3 L/min fino a 3 min e successiva chiusura. Dati (0;0), (1;3), (2;6), (3;9), (4;9), (5;9). Approfonditi coordinate, scale, quadranti, ruoli sperimentali e unicità della corrispondenza funzionale. Il volume è funzione del tempo a condizioni date; 9 L corrispondono a più istanti, quindi l’inversione non individua un unico tempo. La convenzione degli assi resta distinta dalla causalità. Schema del serbatoio, diagramma delle corrispondenze, piano P e grafici originali; libri e biblioteca esclusi dal contenuto dell’8.

Capitolo 9: libri della stessa collana a 15 €/libro, schemi originali di libri e treno al posto delle due fotografie. Slider k per prezzi 10/15/20 €/libro e distanze 60/120/180 km, con tabella/punti aggiornati, scale fisse e modello iniziale tratteggiato. Quadrato con k = 1 mantenuto; aggiunto confronto puramente matematico y = k·x², senza unità, per k da 0,5 a 2: non si cambia artificiosamente la formula dell’area del quadrato. Spiegato che ogni curva ha un k costante e che variarlo confronta modelli diversi. Distinti punti costruiti da formule e dati sperimentali; quesiti aggiornati senza soluzioni.

Copertine originali conservate e didascalie aggiunte a tutte le figure. Foto della biblioteca e del treno conservate solo come materiali storici; rimosse dalle associazioni dei crediti correnti. Schede separate per i visuali originali dei due capitoli. Ogni grafico interattivo è senza zoom; etichette disegnate per almeno 14 CSS px a 320 px. L’unico zoom rimasto riguarda il confronto statico affiancato delle scale e ha il comando esterno ai dati. Il tema condiviso resta invariato.

Rigenerazione: realizza.py e nuovo modulo visuali.py; interazioni.js gestisce il punto P, le curve e gli slider. Verifiche della revisione in corso; i precedenti rapporti non attestano automaticamente le nuove versioni.


Revisione verificata: superati 12 layout (320/390/1440 px, chiaro/scuro), 54 confronti numerici sui valori di k, tastiera degli slider, coerenza tabella/punti/curve, riferimento tratteggiato e scale fisse. Tutte le etichette dei visuali senza zoom sono almeno 14 CSS px a 320 px; P passa correttamente per assi/quadranti, rispetta gli estremi e risponde al trascinamento. Nessuno zoom sui grafici interattivi; zoom del solo confronto statico delle scale con comando fuori dai dati. Tutte le figure hanno una didascalia. Crediti correnti privi di riferimenti alle due fotografie rimosse; originali storici conservati. Fallback senza JavaScript, indice, note e OFL verificati; nessun errore JavaScript, overflow o richiesta esterna. Prove tramite HTTP locale, non file://. Ispezionate direttamente le schermate dei nuovi schemi, del punto P e dei confronti di k.

`credits.py --check`, `build_pages.py`, `node --check` e `git diff --check` superati. I nuovi HTML v2 pesano circa 2,2 MB e 11,3 MB e restano esclusi dalla pubblicazione ufficiale. Manifest, catalogo, pagina pubblica dei crediti e altri capitoli invariati. I precedenti collegamenti online puntano alla v1 e sono superati dalla nuova anteprima v2 da consegnare con il salvataggio corrente. PR sempre in bozza: nessun merge o deployment.


Nuova anteprima HTML v2 salvata al commit `9dc4df85575ad3ce0b2c5af64ad7dcfc44180f8b` e verificata online: [apri il capitolo](https://raw.githack.com/rickymusu-bit/fisica/9dc4df85575ad3ce0b2c5af64ad7dcfc44180f8b/piano_cartesiano_grafici_it.html), HTTPS 200, text/html e byte identici al file locale corrente. Questa anteprima sostituisce i precedenti collegamenti alla v1. Nessun merge o deployment ufficiale.


## Correzioni locali del capitolo 8 — 25 ottobre 2026 (Europe/Rome)

Richiesta: sostituire il rubinetto disegnato con la clip art specifica https://openclipart.org/detail/202080/robinet, orientare gli assi dei grafici con frecce e separare le punte del diagramma delle variabili. Integrato l’SVG originale «Robinet» di spadassin, CC0 1.0 verificata nella scheda Openclipart. Originale, pagina sorgente e metadati conservati in risorse/; nuova scheda centrale clipart-robinet-spadassin. La clip art è incorporata senza ritaglio o modifiche, ridimensionata proporzionalmente e presente nella sola situazione del rubinetto aperto; lo stato chiuso è esplicitato senza una goccia che suggerisca ingresso d’acqua.

Frecce verso destra e verso l’alto nel grafico tempo–volume, nel piano interattivo e in entrambi i confronti delle scale, comprese le copie ingrandite. Coordinate, dati e comandi invariati. Le tre punte del diagramma tempi–volume terminano a quote 95/125/155 dello schema, distinte di 30 unità, rivolte allo stesso valore 9 L.

HTML del capitolo 8 aggiornato a v3, bozza testuale v4. Il generatore ora supporta --chapter-8 per aggiornare solo il capitolo richiesto; versione e data del capitolo 9 restano indipendenti. Confermata identità byte per byte del capitolo 9 rispetto a HEAD. Nessun aggiornamento al tema comune, ai capitoli pubblicati o al manifest.

Verifiche superate: sei layout Chromium del solo capitolo 8 (320/390/1440 px, chiaro/scuro), frecce su tutti gli assi, punte distinte, clip art incorporata, leggibilità, trascinamento/tastiera di P, zoom statico e fallback senza JavaScript. Nessun errore, overflow o richiesta esterna. Ispezionate direttamente le nuove schermate del rubinetto, della corrispondenza e degli assi. credits.py --check, build_pages.py e git diff --check superati. Rapporti e schermate aggiornati; le verifiche del capitolo 9 sono conservate. PR in bozza, nessun merge o deployment ufficiale.


Anteprima corrente v3 verificata online al commit `c8a89b5bf8195eae5adb6e2022b6f16a491f2eda`: [apri il capitolo](https://raw.githack.com/rickymusu-bit/fisica/c8a89b5bf8195eae5adb6e2022b6f16a491f2eda/piano_cartesiano_grafici_it.html), HTTPS 200, text/html, byte identici al file locale. Questo collegamento supera le precedenti anteprime del capitolo 8.


## Allineamento delle tabelle e clip art richieste — 25 ottobre 2026 (Europe/Rome)

Richiesta dell’utente durante il completamento della PR #79: stesso allineamento delle colonne in tutte le tabelle dei capitoli 8 e 9, e uso delle clip art specifiche Double Decker Bus e Red book partly open negli schemi del capitolo 9. Uniformati al centro intestazioni e dati, senza cambiare ordine, valori o unità. La regola è nel componente locale data-table dei due capitoli, non nel tema comune.

Schemi del capitolo 9: incorporati gli originali SVG di Double Decker Bus di j4p4n (https://openclipart.org/detail/286938/double-decker-bus) e Red book partly open di nerdy (https://openclipart.org/detail/355394/red-book-partly-open). Licenze CC0 1.0 verificate nelle rispettive schede. Originali e metadati JSON-LD conservati in risorse/; nessun ritaglio, deformazione o modifica delle due clip art. Il racconto del viaggio ora dice autobus per corrispondere all’immagine; distanza di 120 km, ipotesi, formule e dati restano invariati. La costante iniziale dei libri resta 15 €/libro e tutti i comandi di k sono preservati. Composizioni e figure geometriche distinte dalle clip art nei crediti; avviso corrente aggiornato senza eliminare quello storico.

Ulteriore richiesta sul serbatoio: eliminata la linea tratteggiata a sinistra, mantenendo il rubinetto originale con goccia; aggiunto a destra il rubinetto con goccia rimossa tramite ChatGPT, in PNG trasparente. Originale SVG conservato. Versione modificata registrata separatamente nei crediti; immagine e posizionamento verificati nell’HTML corrente. Conservate le frecce sugli assi e le tre punte distinte del diagramma delle variabili.

Verifiche superate: 12 layout Chromium (320/390/1440 px, chiaro/scuro), allineamento computato di ogni intestazione/cella, presenza delle clip art richieste e assenza del tratteggio, 54 casi numerici su k e coerenza dei punti/tabelle, tastiera, assi/quadranti/limiti e trascinamento. Nessuno zoom interattivo; un solo zoom statico fuori dai dati. Nessun errore JavaScript, overflow o richiesta esterna. Ispezionate le schermate mobile di rubinetti, libri, autobus e tabelle; aggiunte le schermate delle quattro tabelle nei due temi, desktop/mobile. Crediti aggiornati e associati; credits.py --check, build_pages.py, node --check e git diff --check superati.

Versioni correnti: capitolo 8 HTML v4, bozza v5; capitolo 9 HTML v3, bozza v6. Manifest, catalogo e altri capitoli invariati. Le nuove anteprime sostituiscono quelle precedenti; PR mantenuta in bozza, nessun merge o deployment ufficiale.


Anteprima corrente v4, con tutte le ultime correzioni, verificata online al commit `8ce87daf1e96be30acdc231240442f9d40607a5f`: [apri il capitolo](https://raw.githack.com/rickymusu-bit/fisica/8ce87daf1e96be30acdc231240442f9d40607a5f/piano_cartesiano_grafici_it.html), HTTPS 200, text/html e byte identici al file locale. Supera le precedenti anteprime del capitolo.
