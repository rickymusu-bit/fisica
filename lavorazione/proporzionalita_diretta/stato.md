# Stato — Le relazioni di proporzionalità

**Stato corrente — pubblicato:** capitolo HTML v4 online su Stringhe, PR #79 integrata e GitHub Pages completato. Approvazione esplicita: «Perfetto. Pubblica». URL: https://rickymusu-bit.github.io/fisica/relazioni_proporzionalita_it.html

## Riferimenti e autorizzazioni

Progettazione v3 — 24 ottobre 2026, Europe/Rome. Master consultato: v69.15; istruzioni AGENTS.md, piano dell'area, STILE_DISPENSE.md v7, esempio_irraggiamento.md e docs/visual-guidelines.md. Checklist: A1–A5 (narrazione, formule, monograficità, domande), B1.1–B2 (visuali prima della bozza e approvazioni), B4–B6 (riuso e continuità), C1–C4 (immagini, grafici, accessibilità), D1–D2.1 (verifiche e salvataggio). Applicare economia informativa a testo, figure e didascalie.

Richiesta effettiva: «Iniziamo a creare i capitoli 8 e 9 del piano di lavorazione sull'introduzione alla fisica». Autorizzato l'avvio della progettazione. Le nuove scelte visuali, la bozza completa, la realizzazione HTML e la pubblicazione non sono ancora approvate. Tema comune Stringhe già approvato, da riutilizzare nella successiva fase HTML senza una nuova scelta.

Fonte verificata: grafici_piano_cartesiano_it.html, versione interna v8, blob 9befd930b57d847869b7cc6e9f131e01050223f3. Consultato anche lo stato storico lavorazione/grafici_piano_cartesiano/stato.md. Il manifest corrente esclude il sorgente unificato: consultato, non modificato né riammesso. Il piano iniziale conserva passaggi storici: il manifest corrente include già i capitoli 1–7. Nessun intervento a main, manifest, catalogo o sito pubblico.

Ramo dedicato derivato da main: lavorazione/introduzione-capitoli-8-9. File di stato e proposta salvati; nessuna bozza integrale o HTML realizzati. Revisione preliminare svolta sul testo, sui grafici SVG e sul codice delle interazioni; non si dichiarano prove nel browser o verifiche delle licenze non eseguite.

## Proposta iniziale accorpata — superata dalle decisioni in fondo

Richiesta: «Allora, io farei il piano cartesiano in un capitolo e tutte le relazioni di proporzionalità in un altro». Approvato l'accorpamento: capitolo 8 sul piano cartesiano; capitolo 9 su tutte le relazioni previste dal piano. Il percorso complessivo comprende nove capitoli; non sono più previsti capitoli 10 e 11 separati.

Titolo proposto: «Le relazioni tra grandezze». Percorso futuro proposto: relazioni_grandezze_it.html. Questo file di stato conserva il percorso storico per mantenere continuità e collegamenti, ma riguarda ora l’intero capitolo 9.

Sorgente: sezioni «Dalle proporzioni alla retta», «Intercetta e pendenza: rette diverse», «Proporzionalità inversa» e «Relazione quadratica» di grafici_piano_cartesiano_it.html, con tabelle, grafici e quesiti 3–7. Il capitolo 8 fornisce i prerequisiti di lettura del piano e delle scale: non ripeterne la spiegazione.

## Percorso iniziale — superato per la parte affine

Domanda guida: quando cambia una grandezza, come possiamo prevedere il cambiamento dell’altra?

1. Proporzionalità diretta: y = k·x, rapporto costante per x diverso da zero, significato e unità di k, raddoppio e dimezzamento, retta passante per l’origine. Conservare l’esempio dei quaderni a prezzo unitario fisso.
2. Confronto con le altre rette: y = m·x + q, significato di pendenza e intercetta, quota fissa della consegna e retta decrescente. Per q diverso da zero la relazione è affine e non una proporzionalità diretta; una retta decrescente non è automaticamente una proporzionalità inversa. Il confronto serve a riconoscere i modelli, senza diventare un capitolo separato.
3. Proporzionalità inversa: y = k/x, prodotto x·y costante, esempio dei rettangoli di area 12 cm², raddoppio della base e dimezzamento dell’altezza, curva nel dominio positivo.
4. Proporzionalità quadratica: y = k·x², rapporto y/x² costante per x diverso da zero, lato e area del quadrato, raddoppio del lato e area quadrupla. Non chiamare proporzionalità quadratica una generica funzione di secondo grado con altri termini.
5. Domande finali su riconoscimento delle relazioni da dati, formule e grafici, senza riepiloghi ripetitivi o soluzioni automatiche.

Le divisioni saranno frazioni orizzontali nell’HTML. Definire grandezze, unità, domini e costanti nel punto necessario; non ripetere a ogni grafico avvertenze già chiare. Il caso concreto positivo non deve diventare una definizione generale che escluda k negativo nella proporzionalità diretta.

## Visuali proposte e materiali aperti

Riutilizzare tabelle e grafici del sorgente: quaderni, confronto delle tre rette, rettangoli ad area costante e area del quadrato. Conservare i comandi esistenti «Mostra la retta» / «Mostra la curva» se concordati; nessuna nuova simulazione programmata. Assi con grandezze e unità coerenti con ciascun contesto; non fondere in uno stesso grafico dati con unità diverse.

Copertina: da scegliere per il capitolo unificato; la precedente proposta dei quaderni non è più una scelta corrente automatica. Non riutilizzarla nel corpo. Per gli esempi concreti servono gli schemi delle situazioni: immagine del quaderno e del servizio di consegna da concordare e fornire; rettangoli e quadrati sono oggetti geometrici rappresentabili direttamente in SVG. Non cercare o generare nuove immagini senza richiesta. Niente didascalie che ripetano assi, regole o comandi.

I quesiti originali 3–7 sono assegnati tutti a questo capitolo; 1–2 al capitolo 8. Preservare contenuto e funzione dei quesiti nella bozza. Il paragrafo storico sulla linea interpolante nei dati misurati non va trasferito automaticamente al modello esatto dei prezzi.

## Fattibilità, fase e prossimo passaggio

I grafici e i comandi esistono: riuso leggero, senza servizi esterni o nuove librerie. Separare lo script dei grafici dal codice del punto P, che appartiene al capitolo 8, ed evitare accessi a elementi assenti. Verificare comandi, tastiera, aria-pressed, fallback statico, scale, domini e resa mobile nei due temi. Non sono ancora state svolte prove nel browser sul capitolo unificato.

La precedente stima di 15–30 minuti riguardava soltanto il grafico della diretta e non copre l’intero capitolo unificato. Dopo l’approvazione della bozza occorre una nuova stima complessiva ripartita per materiali, HTML, interazioni, verifiche e salvataggio.

Fase corrente: struttura accorpata definita dall’utente; visuali da concordare. Prossima operazione: definire i materiali e poi preparare bozza.md completa con segnaposto. Nessuna realizzazione HTML, modifica di main o pubblicazione autorizzata.

## Stato corrente — bozza v2 senza intercetta, 24 ottobre 2026

«Va bene, procediamo» autorizza la stesura. Preparata bozza v1 completa; durante il lavoro l’utente richiede «Lascia fuori la parte sull'intercetta». [Bozza v2](bozza.md) aggiornata: titolo «Le relazioni di proporzionalità» e soltanto diretta, inversa e quadratica. Superati i paragrafi precedenti che proponevano relazioni affini e confronti con altre rette.

Eliminati sezione sulle rette con intercetta, esempio della consegna e quota fissa, formula della pendenza, confronto delle tre rette e relativi quesiti. Non serve più un’immagine del servizio di consegna. Restano copertina e immagine del quaderno da scegliere; tabelle, figure geometriche e grafici previsti hanno segnaposto. Nessuna nuova immagine cercata, generata o approvata implicitamente.

Nove domande finali: conservati i quesiti originali 3/6/7 nelle domande 1/4/6; originali 4–5 esclusi dai nuovi capitoli per richiesta e conservati nel sorgente storico. Originali 1–2 al capitolo 8. Formule generali y = k·x, y = k/x, y = k·x² e grandezze costanti spiegate; frazioni orizzontali previste nell’HTML.

Verifica editoriale: controllati prezzi 0/2/4/6/8 €, prodotti dei rettangoli pari a 12 cm², aree dei quadrati, fattori di scala e soluzione implicita dei quesiti; nessuna soluzione pubblicata. Quesito sull’inversa coerente con k = 6; rettangolo con base 8 cm alto 1,5 cm. Nessun grafico tariffario o confronto affine nei segnaposto della bozza v2. Nessuna prova nel browser dichiarata.

Fase corrente: testi da revisionare. Dopo approvazione, comunicare la stima ripartita e raccogliere il via alla realizzazione HTML. Nessun merge o deployment.

## Bozza v3 — viaggio al posto dei rettangoli

24 ottobre 2026. L’utente sceglie esplicitamente il viaggio per la proporzionalità inversa: «fai col viaggio». Sostituita la sezione dei rettangoli con un viaggio in treno su distanza fissa di 120 km, senza fermate e con velocità costante. Formule v·t = d, t = d/v e collegamento al modello generale x·y = k, y = k/x. La costante è una distanza in km, non più un’area.

Tabella: velocità 30/40/60/80/120 km/h e tempi 4/3/2/1,5/1 h. Segnaposto C9-RET sostituito da C9-VIA, con immagine del treno da scegliere e schema dello stesso percorso. Specifica C9-GRA-I aggiornata con nuovi dati, assi, unità e descrizione accessibile. Nessun grafico realizzato e nessuna immagine cercata o generata. Domande 4–5 adattate: triplicare la velocità e calcolare il tempo a 100 km/h.

Verifica numerica: ogni prodotto v·t vale 120 km; 60→120 km/h dimezza 2→1 h; 40→120 km/h riduce 3→1 h; 120/100 = 1,2 h = 1 h 12 min. Il vecchio quesito sui rettangoli conserva la propria funzione nel quesito del viaggio; il sorgente storico resta invariato. Le precedenti specifiche su rettangoli e area costante sono superate. [Bozza corrente v3](bozza.md) da revisionare; capitolo 8 e altre sezioni invariati. HTML, merge e pubblicazione non avviati.

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


Salvataggio remoto verificato: commit `949647f5643410b84b22f14c55ae974781137f7c` sul ramo della PR #79. [Anteprima interattiva corrente](https://raw.githack.com/rickymusu-bit/fisica/949647f5643410b84b22f14c55ae974781137f7c/relazioni_proporzionalita_it.html), HTTPS 200, tipo text/html e byte identici all’HTML locale. Rapporto [verifica-anteprima-online.json](verifica-anteprima-online.json). Nessuna pubblicazione ufficiale eseguita.


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


Nuova anteprima HTML v2 salvata al commit `9dc4df85575ad3ce0b2c5af64ad7dcfc44180f8b` e verificata online: [apri il capitolo](https://raw.githack.com/rickymusu-bit/fisica/9dc4df85575ad3ce0b2c5af64ad7dcfc44180f8b/relazioni_proporzionalita_it.html), HTTPS 200, text/html e byte identici al file locale corrente. Questa anteprima sostituisce i precedenti collegamenti alla v1. Nessun merge o deployment ufficiale.


## Allineamento delle tabelle e clip art richieste — 25 ottobre 2026 (Europe/Rome)

Richiesta dell’utente durante il completamento della PR #79: stesso allineamento delle colonne in tutte le tabelle dei capitoli 8 e 9, e uso delle clip art specifiche Double Decker Bus e Red book partly open negli schemi del capitolo 9. Uniformati al centro intestazioni e dati, senza cambiare ordine, valori o unità. La regola è nel componente locale data-table dei due capitoli, non nel tema comune.

Schemi del capitolo 9: incorporati gli originali SVG di Double Decker Bus di j4p4n (https://openclipart.org/detail/286938/double-decker-bus) e Red book partly open di nerdy (https://openclipart.org/detail/355394/red-book-partly-open). Licenze CC0 1.0 verificate nelle rispettive schede. Originali e metadati JSON-LD conservati in risorse/; nessun ritaglio, deformazione o modifica delle due clip art. Il racconto del viaggio ora dice autobus per corrispondere all’immagine; distanza di 120 km, ipotesi, formule e dati restano invariati. La costante iniziale dei libri resta 15 €/libro e tutti i comandi di k sono preservati. Composizioni e figure geometriche distinte dalle clip art nei crediti; avviso corrente aggiornato senza eliminare quello storico.

Ulteriore richiesta sul serbatoio: eliminata la linea tratteggiata a sinistra, mantenendo il rubinetto originale con goccia; aggiunto a destra il rubinetto con goccia rimossa tramite ChatGPT, in PNG trasparente. Originale SVG conservato. Versione modificata registrata separatamente nei crediti; immagine e posizionamento verificati nell’HTML corrente. Conservate le frecce sugli assi e le tre punte distinte del diagramma delle variabili.

Verifiche superate: 12 layout Chromium (320/390/1440 px, chiaro/scuro), allineamento computato di ogni intestazione/cella, presenza delle clip art richieste e assenza del tratteggio, 54 casi numerici su k e coerenza dei punti/tabelle, tastiera, assi/quadranti/limiti e trascinamento. Nessuno zoom interattivo; un solo zoom statico fuori dai dati. Nessun errore JavaScript, overflow o richiesta esterna. Ispezionate le schermate mobile di rubinetti, libri, autobus e tabelle; aggiunte le schermate delle quattro tabelle nei due temi, desktop/mobile. Crediti aggiornati e associati; credits.py --check, build_pages.py, node --check e git diff --check superati.

Versioni correnti: capitolo 8 HTML v4, bozza v5; capitolo 9 HTML v3, bozza v6. Manifest, catalogo e altri capitoli invariati. Le nuove anteprime sostituiscono quelle precedenti; PR mantenuta in bozza, nessun merge o deployment ufficiale.


Anteprima corrente v3, con tutte le ultime correzioni, verificata online al commit `8ce87daf1e96be30acdc231240442f9d40607a5f`: [apri il capitolo](https://raw.githack.com/rickymusu-bit/fisica/8ce87daf1e96be30acdc231240442f9d40607a5f/relazioni_proporzionalita_it.html), HTTPS 200, text/html e byte identici al file locale. Supera le precedenti anteprime del capitolo.


## Andamento continuo del volume e gruppi di libri distinti

L’utente richiede che il volume del serbatoio sia rappresentato come grandezza che varia continuamente, non soltanto dai punti della tabella, e che le situazioni dei libri siano chiaramente separate, consentendo la sovrapposizione all’interno di ogni gruppo. Realizzata una linea sempre visibile nel grafico principale e in entrambi i confronti delle scale: V cresce con ingresso costante da (0;0) a (3;9), poi resta orizzontale fino a (5;9). I punti restano visibili e indicano gli istanti tabulati. Nessuna interpolazione curva arbitraria: due tratti rettilinei continui, coerenti con apertura e chiusura istantanea del rubinetto nel modello ideale. Aggiunta la spiegazione dei valori intermedi, aggiornata la didascalia e separata l’etichetta P dal tracciato. Nessun nuovo comando, zoom o libreria.

Nel capitolo 9, tre colonne distinte con margini e divisori, etichette «1 libro», «2 libri», «3 libri» e rispettivi prezzi 15/30/45 €. I volumi si sovrappongono solo all’interno del gruppo; i tre gruppi restano separati. Usata la stessa clip art espressamente richiesta, senza modificarla o ritagliarla. L’allineamento centrale di tutte le tabelle, le altre clip art e lo schema dei rubinetti sono preservati.

Verifiche superate: 12 layout e 54 casi di k nei rapporti aggiornati, linea continua visibile con e senza JavaScript, valori 0 L a 0 min, 4,5 L a 1,5 min e 9 L da 3 a 5 min, due tracciati nel confronto delle scale, gruppi di 1/2/3 immagini. Ispezionate direttamente le schermate mobile del tracciato e dei libri; quattro schermate del grafico principale rifinite per l’etichetta P. Crediti, build e assenza di overflow/errori/richieste esterne confermati. Tabelle, assi orientati, punte separate, rubinetto senza goccia a destra e autobus preservati.

Versioni correnti: capitolo 8 HTML v5 e bozza v6; capitolo 9 HTML v4 e bozza v7. Nuova anteprima da consegnare e approvare; PR sempre in bozza, nessun merge o deployment.


Anteprima corrente v4 verificata online al commit `37933d25e673009b5eeac1d6d8b50637bce5bebe`: [apri il capitolo](https://raw.githack.com/rickymusu-bit/fisica/37933d25e673009b5eeac1d6d8b50637bce5bebe/relazioni_proporzionalita_it.html), HTTPS 200 e byte identici al file locale. Comprende il tracciato continuo e i gruppi di libri separati; sostituisce i precedenti collegamenti del capitolo.


## Approvazione esplicita e preparazione della pubblicazione

Dopo le anteprime del commit 37933d25e673009b5eeac1d6d8b50637bce5bebe (capitolo 8 v5, capitolo 9 v4), l’utente scrive «Perfetto. Pubblica». È l’approvazione della versione corrente e l’autorizzazione a integrare la PR #79 e avviare Pages; le precedenti attese di approvazione sono superate per queste versioni. Testo e figure della sezione article risultano identici byte per byte alla versione approvata.

Manifest v16: ammessi i due capitoli dopo Errori e incertezza di misura; catalogo dell’area introduttiva portato a nove capitoli (19 complessivi). Aggiornata soltanto la navigazione delle pagine adiacenti: 7 → 8 → 9 → Termodinamica. Date editoriali dei due nuovi capitoli aggiornate per la prima pubblicazione; nessuna nuova revisione scientifica o grafica. Crediti generali e snapshot sincronizzati per i capitoli ammessi, mantenendo gli originali e gli avvisi storici.

Superati i 24 test automatici, sync_stringhe_theme.py --check, credits.py --check e build_pages.py; controllo dei collegamenti precedente/successivo sui 19 capitoli riuscito. Il controllo browser comune ora verifica anche che il comando esterno del confronto delle scale rimanga fuori dai dati e mantenga il bersaglio di 44 px, preservando i controlli canonici dei vecchi visuali. Verifica finale del portale in corso; nessun ulteriore consenso richiesto per il rilascio già autorizzato.


Controllo finale del portale superato: 250 combinazioni pagina/viewport/tema, 20 copertine, nessun errore JavaScript. Rapporti in lavorazione/sito/verifica-stringhe.json e lavorazione/introduzione_fisica_misura/verifica-pubblicazione.json; schermate aggiornate di home e catalogo. Configurazione pronta per merge e Pages autorizzati.


## Pubblicazione completata e verificata

PR #79 integrata in main al commit `da6c9bde5f15816a5fe060d9dbe36cedbfe636d9` dopo il superamento della [verifica GitHub](https://github.com/rickymusu-bit/fisica/actions/runs/40140622208). [Rilascio Pages](https://github.com/rickymusu-bit/fisica/actions/runs/40140944812) completato con successo. Capitolo corrente: [v4, apri sul sito](https://rickymusu-bit.github.io/fisica/relazioni_proporzionalita_it.html).

Verifica HTTPS finale: dieci file pubblici aggiornati, compresi i due nuovi capitoli, catalogo, home, crediti, quiz e pagine adiacenti, HTTP 200 e identici byte per byte alla build locale; undici indirizzi esclusi, storici o di anteprima HTTP 404. Tutti i 21 controlli superati. Rapporto unico in lavorazione/introduzione_fisica_misura/verifica-pubblicazione-online.json. Nessun contenuto scientifico modificato rispetto alle anteprime approvate. Il presente aggiornamento registra soltanto l’esito del rilascio.
