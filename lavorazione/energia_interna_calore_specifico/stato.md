# Stato — Energia interna, calore e calore specifico

Versione v9 · Aggiornamento: 19 ottobre 2026 (Europe/Rome).

## Ambito e punto di partenza

Articolo 3 del [percorso introduttivo di termodinamica](../percorso_termodinamica.md) v4: interpretazione microscopica dell’energia interna; distinzione da temperatura e calore; capacità termica e calore specifico; Q = m · c · ΔT. Ambito congiunto esplicitamente previsto dal piano. Esclusi bilancio termico fra corpi, temperatura finale delle miscele, contributo del recipiente, calore latente, dilatazione e sviluppo dei meccanismi di trasmissione.

Richiesta effettiva: «Sul repo https://github.com/rickymusu-bit/fisica crea l'articolo 3 del piano». Autorizza l’avvio del capitolo; non documenta approvazione di visuali, testo o pubblicazione.

Ramo dedicato: `termodinamica/energia-interna-calore-specifico`, derivato da main al commit `a5a54f527db7b8052f09b49773dbcc7740a6d061`. Alla verifica iniziale non esistevano una lavorazione o un HTML di questo capitolo; nessun file precedente sostituito.

## Riferimenti e checklist

Letti integralmente MASTER_PROMPT.md v60 in blocchi, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, piano v4 e manifest di pubblicazione v6. Consultati stato e visuali dell’articolo 2 e visuali dell’articolo 1 per continuità e riuso.

- A1–A5: stile divulgativo, fenomeno concreto, percorso continuo, formule introdotte e interpretate, T maiuscola, notazione scientifica nei calcoli, domande finali senza soluzioni.
- B1.1 e C2: concordare visuali prima della bozza; non cercare o generare nuove immagini autonomamente.
- Bozza completa soltanto in `bozza.md` del ramo; approvazione del testo e via esplicito prima dell’HTML.
- Tema autonomo v8 già approvato; leggere il modello prima di impaginare. Composizione dei visuali identica sui dispositivi, ingrandimento canonico quando serve.
- Crediti nella fonte unica `risorse/crediti.json`, con riuso delle schede esistenti e controlli comuni nella futura fase HTML.
- Non modificare main, manifest, home, articoli precedenti o sospesi; pubblicazione separata.

## Fase corrente

Progettazione delle visuali: proposta concreta v5 salvata in [visuali.md](visuali.md), comprendente domanda iniziale, percorso, confini, tre immagini da scegliere, grafico e tabella proposti e otto nuclei per le domande finali.

Domanda guida scelta dall’utente: «Perché d’estate il mare resta tiepido di notte, anche quando la sabbia è fredda?». Richiesta effettiva: «Allora chiedi perché d'estate il mare resta tiepido di notte anche se la sabbia è fredda». Sostituisce l’apertura sul deserto; autorizzato l’adattamento del percorso e delle proposte visuali, senza attribuire approvazioni a immagini specifiche.

COP-01: spiaggia estiva con mare e sabbia, copertina distinta. FIG-01: battigia di sera o di notte. FIG-02: modello microscopico. GRA-01: temperatura in funzione del calore per masse uguali di acqua e sabbia asciutta, con dati documentati. TAB-01: confronto di calori specifici. Identificativi e funzioni in visuali.md; nessuna nuova scelta attribuita all’utente.

Nessuna simulazione o video proposti: nessuna programmazione, nessun costo di simulazione da stimare. Nessun esercizio svolto o sezione autonoma di applicazioni aggiunti.

## Verifiche e limiti

Identificati numero e titolo dal piano ufficiale. Controllati confini rispetto agli articoli 2 e 4; distinta energia interna dal moto macroscopico e distinta capacità termica dal calore specifico. Il futuro grafico deve rappresentare previsioni, senza inventare misure. La relazione quantitativa non sarà applicata a cambiamenti di stato. Per la spiaggia: c dell’acqua maggiore di quello della sabbia asciutta; a parità di massa ed energia ceduta, minore diminuzione di T. Distinguere questo confronto dal mare reale, dove contribuiscono massa d’acqua coinvolta e rimescolamento. Non assumere uguali masse o uguali perdite di energia per mare e spiaggia, né temperature ricavabili dalle fotografie. Nessun valore universale di c assegnato a sabbie di composizione diversa.

Esaminati materiali già scelti nei primi due articoli: caffè riutilizzabile per richiamo contestuale, ma non necessario alla nuova apertura; bevanda con ghiaccio non adatta a illustrare qui Q = m · c · ΔT. Non cercate, generate o modificate nuove immagini.

Bozza completa v1 creata in bozza.md dopo il «Vai» dell’utente, ricevuto dopo la scelta della domanda sulla spiaggia. Il comando autorizza la stesura corrente; non è approvazione di un testo che ancora non esisteva né scelta dei file delle immagini. Nessun HTML creato. Nessuna verifica HTML/browser o build pertinente a questa fase documentale viene dichiarata eseguita. La shell non raggiunge il proxy nella sandbox predefinita; lettura e salvataggio ufficiali effettuati tramite connettore GitHub.

## Prossima operazione

Bozza.md v3 approvata dall’utente con «Approvata», dopo la revisione che sposta le fonti nei crediti. Non richiedere nuovamente l’approvazione del testo. Ricevere i tre file/collegamenti di spiaggia estiva, battigia serale/notturna e modello microscopico. Dopo il testo approvato, fornire stima totale ripartita e raccogliere via esplicito all’HTML secondo B1.1–B2. Nessuna approvazione dedotta dall’elenco già approvato.

## Bozza v1 completata

Richiesta aggiuntiva effettiva: «Vai». Bozza completa salvata con apertura scelta dall’utente, spiegazione microscopica di U, distinzione temperatura/energia interna/calore, C e c, Q = C · ΔT, C = m · c, Q = m · c · ΔT e relazione inversa con frazione. Segni nel raffreddamento introdotti senza bilancio fra corpi. Ritorno conclusivo al mare, otto domande senza soluzioni e tre note brevi. Nessuna sezione opzionale o simulazione aggiunta.

TAB-01 include acqua pura a 20 °C e sabbia quarzosa indicativa; fonte Engineering ToolBox consultata direttamente. Valori arrotondati 4,18 · 10³ e 8,3 · 10² J/(kg · K). Temperatura e umidità della sabbia non specificate dalla fonte, limite esplicito in nota; non presentarla come misura della spiaggia. Specifiche del grafico nel segnaposto GRA-01: m = 1 kg, T_i = 20 °C, Q da 0 a 1 kJ, due rette dal modello, senza dati sperimentali inventati. Consultata anche OpenStax, College Physics, §14.2 per il controllo della relazione e delle unità; testo formulato autonomamente.

Controllo scientifico e redazionale svolto: simbolo T, unità, proporzioni, segni, distinzione c/C, modello microscopico senza equiparare solidi a gas ideali, confronto mare reale distinto da masse uguali, nessun anticipo del bilancio termico o del calore latente. Segnaposto COP-01/FIG-01/FIG-02/GRA-01/TAB-01 presenti, copertina distinta, otto domande numerate e richiami delle note coerenti. Immagini specifiche mancanti; nessuna ricerca di immagini o generazione effettuata. Bozza testuale da approvare, non HTML definitivo. Nessuna build/browser pertinente a questa fase.

## Revisione corrente — bozza v2

Richiesta esplicita: «Nella tabella metterei valori di comuni sostanze liquidi, solidi e gas, per confrontare e per fare risaltare la particolarità dell'acqua, che è da spiegare». Aggiornamento circoscritto autorizzato ed eseguito, senza richiedere nuovamente via alla stesura. Non è ancora approvazione finale della bozza o via all’HTML.

TAB-01 ampliata a dieci righe, con colonne stato, sostanza/materiale e c: rame 385, ferro 449, sabbia quarzosa 830, alluminio 897; olio d’oliva 1790, etanolo 2440, acqua pura a 20 °C 4182; ossigeno 918, aria secca 1005, azoto 1040 J/(kg · K). Valori della fonte Engineering ToolBox letta direttamente, resi nella bozza in notazione scientifica; acqua e aria arrotondate rispettivamente a 4,18 · 10³ e 1,01 · 10³. Stato raggruppato e acqua evidenziata senza dipendere solo dal colore. Non dichiarato che l’acqua abbia il massimo calore specifico tra tutte le sostanze.

Inserita spiegazione dei legami a idrogeno intermolecolari e del contributo del riassetto delle interazioni all’energia assorbita nel riscaldamento, senza suggerire rottura delle molecole d’acqua o temperatura invariata durante il riscaldamento. Fonte concettuale verificata: OpenStax, Biology 2e §2.2, https://openstax.org/books/biology-2e/pages/2-2-water . Testo originale, senza introdurre chimica avanzata o calore latente.

Domanda 7 adattata al confronto tra i tre stati e alla spiegazione dell’acqua. Aggiunta nota 4 sui valori a pressione costante, essenziale per i gas; nota 2 resa coerente senza estendere l’ipotesi di lavoro trascurabile ai gas che si espandono. Restano otto domande e ora quattro note con richiami. Grafico acqua/sabbia, apertura e resto del testo conservati. Nessuna nuova ricerca di immagini o realizzazione HTML. File specifici delle tre immagini ancora da scegliere.

Controlli della revisione: valori e unità confrontati con la tabella della fonte, raggruppamento degli stati coerente, notazione scientifica e arrotondamenti controllati; condizioni dei gas esplicitate e riferimenti delle note verificati. Salvataggio di bozza, visuali e stato sullo stesso ramo dedicato; nessuna modifica a main o pubblicazione.

## Revisione corrente — bozza v3, fonti nei crediti

Richiesta esplicita dell’utente: «Le fonti dei dati numerici e delle informazioni specifiche vanno nei crediti, non nel testo». Applicata alla bozza: rimossi i riferimenti a Engineering ToolBox e OpenStax dal testo didattico; trasferiti con associazione al contenuto nel componente collassabile «Crediti della copia autonoma», aggiungendo anche la fonte già consultata per la verifica di formule e unità. Note 3 e 4 conservano soltanto condizioni fisiche e limiti utili, senza attribuzioni. Dati della tabella, spiegazione dell’acqua, formule e otto domande invariati.

Regola consolidata nel master v61, C1/C3/D2, sostituendo le precedenti istruzioni che collocavano le fonti nel corpo; allineato risorse/README.md. Le attribuzioni non sono eliminate né le condizioni fisiche spostate fuori dalla spiegazione. Nella fase testuale la sezione collassabile della bozza conserva i riferimenti; in fase HTML confluiranno nel registro unico e nello snapshot comune mediante gli strumenti di sincronizzazione. Nessun inventario parallelo creato, nessun credito.html o HTML pubblicato aggiornato.

Controllati: tre fonti nei soli crediti della bozza, assenza di URL nel contenuto didattico e nelle note, dettagli inizialmente chiusi, valori e formule conservati, otto domande e quattro note con richiami coerenti. Caricamento sul ramo dedicato da verificare prima della consegna. Resta la revisione della bozza e la scelta delle tre immagini prima dell’HTML; non dedurre una nuova approvazione finale.

## Approvazione effettiva della bozza v3

Ricevuto «Approvata» dopo la consegna della bozza v3. Testo completo, tabella ampliata, spiegazione dell’acqua, otto domande e fonti nei crediti sono approvati. Questa approvazione non sceglie file d’immagine non ancora forniti e precede la stima e il via alla realizzazione secondo B1.1–B2. Conservare il testo approvato; eventuali adattamenti alle fotografie devono essere circoscritti.

Materiali ancora necessari: COP-01 spiaggia estiva con mare e sabbia; FIG-01 battigia di sera/notte, immagine diversa dalla copertina; FIG-02 illustrazione microscopica di moto e interazioni delle particelle, preferibilmente utile anche al collegamento con l’acqua. Nessun file specifico scelto, nessuna ricerca autonoma autorizzata. La futura realizzazione comprende grafico GRA-01 e tabella TAB-01 già previsti, senza simulazioni.

Stima da comunicare prima del via HTML: 35–60 minuti di lavoro, esclusa l’attesa dei file e delle risposte. Materiali e crediti 5–10 minuti; tabella, grafico e impaginazione nel tema comune 20–35 minuti; verifiche desktop/mobile, autonomia, anteprime e salvataggio 10–15 minuti. Impegno di calcolo basso, nessuna simulazione. Stima indicativa assumendo immagini disponibili, utilizzabili e senza elaborazioni complesse; accesso operativo e risultati dei controlli possono incidere.

Prossimo passo: ricevere immagini o collegamenti scelti e il via esplicito all’HTML dopo la stima. Nessun via già ricevuto dopo questa stima, nessuna pubblicazione autorizzata. Non chiedere di nuovo l’approvazione della bozza.

## Materiali scelti dall’utente — bozza v4

Ricevuti tre collegamenti precisi dopo approvazione della bozza e stima: sputafuoco indicato esplicitamente come copertina, spiaggia notturna di Ko Li Pe per FIG-01, Thermally Agitated Molecule.gif per FIG-02. Scelta autorizzata, senza chiedere una nuova approvazione degli stessi file. Non è stato espresso un via ulteriore alla realizzazione HTML.

Scaricate e ispezionate le tre immagini: copertina 1920 × 1411 px, 611589 byte; spiaggia originale 5760 × 3840 px, 7665607 byte; GIF 1920 × 1920 px, 2738267 byte, 28 fotogrammi e ciclo di 1120 ms. Nessuna modifica ai file scelti, nessun ritaglio o ricampionamento. Dimensioni e SHA-256 in risorse/verifica-originali.json; copie di anteprima usate soltanto per l’ispezione, fuori dai file ufficiali.

Fonti Commons consultate e licenze verificate: copertina Luc Viatour, CC BY-SA 3.0 tra le licenze offerte, con richiesta di attribuzione nelle immediate vicinanze dell’immagine; spiaggia Piith.hant / Piith Hant, CC BY-SA 4.0; GIF Greg L secondo Commons, caricatore Frokor, fonte dichiarata physics.unlv.edu, CC BY-SA 3.0 tra le licenze offerte. Conservare il credito vicino alla copertina come eccezione prevista da C1, separato dalla didascalia; crediti completi nel componente comune. Non contattato alcun autore.

La GIF mostra una porzione di proteina, non molecole d’acqua né la rete dei loro legami a idrogeno. Didascalia adattata alle vibrazioni degli atomi all’interno della proteina; nessun confronto fra temperature dedotto dall’animazione. Controllati tutti i 28 fotogrammi: 27 diversi dal primo; preservata animazione completa. Per il futuro HTML prevedere pausa/ripresa e movimento ridotto, senza alterare l’originale.

Bozza v4: aggiornati soltanto i tre segnaposto, le relative didascalie, il credito obbligatorio vicino alla copertina e i crediti dei materiali. Apertura sul mare, teoria, dati, formule e domande approvati conservati. Tutte le fonti scientifiche restano nei crediti. Non dedotte temperature della spiaggia dalla foto.

Stima già comunicata 35–60 minuti per la realizzazione, calcolo basso, senza simulazioni: nessuna nuova richiesta della stessa stima o dell’approvazione del testo. Tutti i materiali specifici sono disponibili. Prossimo passo corrente: via esplicito all’HTML dopo la stima, previsto da B1.1–B2; poi lettura del modello comune e realizzazione con grafico, tabella, crediti dal registro unico, anteprime e verifiche. Nessuna pubblicazione autorizzata.

## Sostituzione esplicita FIG-02 — bozza v5

Richiesta dell’utente: «Metti questa gif al posto dell’altra», con collegamento a MD_water.gif. Sostituita nell’articolo l’animazione della proteina con quella dell’acqua, autore Kmckiern, CC BY-SA 4.0, fonte Commons verificata. Aggiornati segnaposto, didascalia e crediti in bozza v5; apertura, teoria, tabella, formule e otto domande approvati invariati. Nessuna nuova approvazione della scelta richiesta.

Il collegamento a 1920 px restituisce una copia ingrandita da 69298768 byte, superiore da sola al limite HTML di 20 MB. Recuperato il file originale della stessa animazione da Commons: 480 × 270 px, 6159492 byte, 300 fotogrammi, ciclo 12000 ms. Nessuna elaborazione/ricompressione del file. La fonte descrive 100 ps simulati: non confondere tempo fisico e durata di riproduzione. Vista la stessa animazione nei fotogrammi 0/100/200; controllata decodifica completa di tutti i fotogrammi. Dettagli e hash in risorse/verifica-originali.json.

La copia ingrandita resta temporaneamente nell’ambiente; non caricata nel repository. Il precedente originale della proteina è conservato, esplicitamente segnato non più usato. I file attivi delle tre immagini pesano complessivamente 14436688 byte: la futura incorporazione base64 e il tema richiedono misura del peso finale, senza presumere conclusa la verifica del limite. Non ottimizzati altri materiali senza autorizzazione.

Nessun HTML realizzato o pubblicazione avviata: resta il via esplicito all’HTML dopo la stima già comunicata. La richiesta corrente autorizza questa sostituzione circoscritta.
