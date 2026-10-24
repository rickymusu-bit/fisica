# Stato — Il piano cartesiano

**Stato corrente — 24 ottobre 2026:** HTML v1 completo e verificato sulla PR #79; bozza testuale v2. Immagini scelte dall’utente e incorporate. Anteprima da approvare prima della pubblicazione. I paragrafi precedenti conservati sotto documentano la cronologia.

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
