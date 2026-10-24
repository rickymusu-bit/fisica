# Stato — Le relazioni di proporzionalità

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
