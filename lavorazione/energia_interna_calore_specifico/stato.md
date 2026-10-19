# Stato — Energia interna, calore e calore specifico

Versione v23 · Aggiornamento: 19 ottobre 2026 (Europe/Rome).

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

Realizzazione HTML v1 completata dopo il via «Procedi». Testo e materiali approvati; risultato e controlli nella sezione conclusiva. La cronologia delle fasi precedenti è conservata sotto.

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

## Sostituzione esplicita della copertina — bozza v6

Richiesta dell’utente: «Usa questa come copertina», con collegamento a Ivy_Mike_-_fireball.jpg. Sostituita la copertina dello sputafuoco con l’immagine Ivy Mike, senza ripetere l’approvazione della scelta. Versione 1920 × 1555 px, 185032 byte, scaricata integralmente e osservata direttamente; nessuna modifica. Hash in risorse/verifica-originali.json. Fonte Commons verificata: Charles Wyckoff, provenienza NNSA/NSO Photo Library IVY-52-07, pubblico dominio PD-USGov-DOE.

Bozza v6: aggiornati il solo segnaposto COP-01, la didascalia e il relativo credito. Rimossa l’attribuzione in prossimità della foto che era prescritta soltanto per la precedente copertina; tutti i riferimenti alla nuova fonte restano nei crediti. Didascalia descrittiva con collegamento a energia e temperatura, senza dati numerici sulla detonazione o digressioni. Testo approvato, apertura sul mare, tabella, formule, GIF dell’acqua e domande conservati.

Lo sputafuoco resta conservato come originale già scelto, segnato non corrente. Copertina corrente solo in risorse/copertina-ivy-mike.jpg. File delle tre immagini attive: 14010131 byte complessivi; il peso definitivo dell’HTML autonomo resta da misurare. Nessun HTML o pubblicazione avviati; via alla realizzazione resta distinto e non ancora ricevuto.

## Via alla realizzazione HTML

Ricevuto «Procedi» dopo la stima di 35–60 minuti, approvazione del testo e selezione finale di copertina Ivy Mike, spiaggia notturna e GIF MD water. Realizzazione HTML autorizzata; non chiedere nuovamente conferma. Pubblicazione e integrazione in main restano distinte e non richieste. Avviata lettura del modello comune e preparazione del generatore, conservando i byte delle immagini scelte e il testo approvato.

## Realizzazione conclusa — HTML autonomo v1

File corrente: `energia_interna_calore_specifico_it.html`, v1 · 19 ottobre 2026, **19394762 byte** (19,39 MB decimali). Copia byte per byte in `bozza.html`. Generatore riproducibile `realizza.py`; verificatore `verifica.py`. Eseguire generatore, `python3 scripts/credits.py --sync`, poi verificatore per rigenerare la copia e le anteprime.

Il «Procedi» successivo alla scelta finale di Ivy Mike autorizza la realizzazione dopo la stima. Lavoro completato; non chiedere di nuovo il via all’HTML. Nessuna integrazione in main o pubblicazione autorizzata o eseguita.

Riutilizzato il modello autonomo v8 esatto: tutti gli stili e script comuni confrontati byte per byte e conservati. Componenti specifici aggiunti per tabella e controllo GIF. Copertina Ivy Mike, foto della spiaggia e GIF MD water incorporate senza alterarne i byte; originale della GIF a 480 × 270 px come già documentato. Primo fotogramma PNG estratto soltanto per pausa e movimento ridotto, accreditato alla stessa risorsa. Nessuna compressione o riduzione delle immagini scelte.

Testo della bozza v6 conservato: sette sezioni, cinque formule, tabella dei dieci materiali, otto domande finali e quattro note. Le frazioni usano una linea orizzontale. Tabella a tre colonne e composizione del grafico identiche sui dispositivi; su mobile tabella scorrevole (contenuto 600 px in 296 px), grafico con ingrandimento a 900 px e scorrimento interno. Rette calcolate con m = 1 kg, T_i = 20 °C, Q da 0 a 1 kJ, c dell’acqua 4180 e c della sabbia quarzosa 830 J/(kg · K), coerenti con i valori arrotondati della tabella. Tratto continuo e tratteggiato distinguono i materiali anche senza colore.

Crediti e fonti scientifiche registrati nella fonte unica `risorse/crediti.json`, associati al nuovo articolo e generati in `crediti.html` e nello snapshot offline. Dati e informazioni specifiche citati soltanto nei crediti, non nel corpo o nelle didascalie. Provenienza e stato di pubblico dominio della copertina, licenze CC BY-SA 4.0 di spiaggia e GIF, grafico originale e avvisi OFL Lexend conservati. Nessuna risorsa del nuovo articolo priva di associazione ai crediti. I documenti precedenti restano invariati; la sincronizzazione ha cambiato solo pagina dei crediti e registro, oltre al nuovo HTML.

Peso superiore alla soglia di attenzione di 18 MB comunicato in chat. Peso finale sotto 20 MB; immagini intatte. Non sono necessarie ulteriori ottimizzazioni per rispettare il limite, ma aggiunte future richiederanno una nuova misura.

Verifiche superate:
- `python3 scripts/credits.py --check`, build Pages e `git diff --check`.
- Chromium a 1280 e 390 px, HTML completo caricato in memoria con rete disabilitata: font e immagini carichi, zero richieste esterne, zero errori JavaScript, nessun overflow della pagina o delle formule.
- Indice con Esc e selezione, note con apertura automatica e ritorni, crediti offline con font OFL, pausa/ripresa della GIF e del logo, variazione della preferenza di movimento ridotto, ingrandimento del grafico e scorrimento della tabella.
- Senza JavaScript: indice e crediti consultabili, GIF sostituita dal fotogramma statico con movimento ridotto.
- Confronto dei byte delle tre immagini incorporate, ID univoci e ancore risolte. Formule, righe della tabella, domande e note controllate.

Report: `verifiche-browser.json` e `verifiche-finali.json`. Anteprime desktop/mobile salvate e ispezionate: prima schermata, animazione, tabella, grafico e frazione. La prova offline usa il documento completo in memoria; non viene dichiarata una prova di apertura tramite protocollo file: in questo ambiente.

Navigazione del solo nuovo articolo verso Temperatura ed equilibrio termico e verso il successivo attualmente disponibile, Stati della materia. Nessun link al bilancio termico non ancora realizzato. Manifest, home, articoli precedenti e sospesi invariati. La build continua a pubblicare i sette articoli già ammessi; il nuovo articolo resta escluso finché non sarà autorizzata la pubblicazione.

Prossimo passo: revisione del risultato HTML e delle anteprime, poi eventuale autorizzazione distinta a integrare e pubblicare. Salvataggio remoto verificato al commit di realizzazione `91635c72a7964a65b49be888a672efccaa7b90e6`; PR in bozza aperta e verificata: https://github.com/rickymusu-bit/fisica/pull/38 . Nessuna integrazione o pubblicazione eseguita.

## Revisione corrente — HTML v2 e peso dei visuali

Richiesta: «Nel grafico fai la linea della sabbia gialla e quella dell’acqua blu. Dimmi il peso dei visuali». Eseguita direttamente come modifica circoscritta. Sabbia #b58a00 continua, acqua #0066cc tratteggiata; stessi colori nella legenda. Confronto del sorgente SVG prima/dopo: cambiano soltanto i quattro colori delle rette e dei campioni di legenda, senza variazioni di dati, coordinate, testi o assi. Bozza testuale v7 aggiorna soltanto questa indicazione nel segnaposto.

HTML autonomo v2: 19394778 byte, copia bozza.html identica. Rigenerati gli snapshot e il registro mediante credits.py --sync. Peso dei visuali misurato sui file e sulle occorrenze esatte delle risorse incorporate, in unità decimali, con dettaglio in peso-visuali.json: copertina 185032 byte (246735 nell’HTML); spiaggia 7665607 (10220835); GIF 6159492 (8212678); SVG grafico 3247 (8716, due occorrenze per vista e ingrandimento); fotogramma statico GIF 98303 (262188, due occorrenze per pausa/movimento ridotto); tabella HTML 1879 byte. La codifica base64 aumenta l’ingombro delle immagini. Le misure non comprendono font, logo comune e resto del documento.

Controlli mirati superati: immagini originali incorporate inalterate, CSS/script comuni identici, ID e ancore validi, nessuna risorsa non accreditata, dimensione sotto 20 MB. Chromium offline a 1280 e 390 px per il grafico: nessun overflow o errore JS, ingrandimento e scorrimento funzionanti. Anteprime del grafico aggiornate e verificate; report in verifiche-grafico.json. Report finale aggiornato per peso e SHA-256. I precedenti controlli di indice/note/GIF/crediti restano validi poiché componenti e contenuto corrispondenti sono invariati.

Salvataggio nella stessa PR #38; nessuna pubblicazione o integrazione in main.

## Revisione corrente — HTML v3 e prove di compressione

Richiesta: «Rendi continua la linea dell’acqua. Quanto puoi ridurre la dimensione dei visuali?». Resa continua la linea blu dell’acqua, incluso il campione della legenda, mantenendo gialla e continua quella della sabbia. Dati, geometria, testo e altri visuali invariati. HTML v3: 19394650 byte; copia bozza.html identica. Aggiornati i report di peso e hash, verifiche statiche e prove mirate del grafico a 1280 e 390 px; nessun overflow o errore JS, ingrandimento funzionante.

Eseguite prove reversibili su copie fuori dai materiali correnti, per rispondere quantitativamente alla domanda. Foto: copertina WebP 1920 × 1555 qualità 90 da 185032 a 101328 byte; spiaggia ridimensionata proporzionalmente a 1920 × 1280, WebP qualità 85 da 7665607 a 191742 byte. Stima HTML con sole foto: 9317886 byte, −52,0%, GIF intatta.

GIF: WebP senza perdita da 6159492 a 8869172 byte, quindi non conveniente; verificati tutti i pixel RGBA dei 300 fotogrammi. MP4 H.264 CRF18: 2965911 byte; CRF23: 1772954 byte, mantenendo 480 × 270 px, 300 fotogrammi e 12 secondi. Codifiche con perdita e cambio di formato, da non presentare come equivalenti bit per bit. Con foto ottimizzate e MP4: stima HTML 5059778 byte (−73,9%) oppure 3469170 (−82,1%) con compressione maggiore. L’integrazione MP4 richiederebbe adattamento dei controlli e scelta esplicita; non è stata applicata.

Copie delle fotografie e fotogrammi video esaminati visivamente; nessun ritaglio o modifica del modello fisico. Le prove rimangono in /workspace/compressione-visuali; rapporto delle misure in prove-compressione.json sul ramo. Stime calcolate sulle dimensioni reali delle copie, includendo base64 e mantenendo il resto del documento: il peso definitivo si misurerebbe dopo integrazione. Le foto compresse riducono risoluzione o precisione dei pixel; non dichiarare assenza totale di perdita. Originali e risorse correnti dell’articolo intatti.

Scopo corrente completato: grafico corretto e riduzioni misurate. Nessuna compressione sostitutiva, pubblicazione o integrazione in main eseguita.

## Revisione corrente — HTML v4, sola spiaggia compressa

Richiesta: «Lascia la copertina originale, comprimi solo la spiaggia. In che senso mp4 cambia il formato dell’animazione?». Compressione della sola spiaggia autorizzata ed eseguita; copertina e GIF mantenute esattamente nei file e nei byte della versione precedente. Spiegato che MP4 riprodurrebbe la sequenza come video locale incorporato invece che come immagine animata, richiedendo un componente diverso per riproduzione e pausa; nessuna conversione applicata all’articolo.

Spiaggia: originale JPEG 7665607 byte, 5760 × 3840 px, conservato. Versione corrente WebP qualità 85, 191742 byte, 1920 × 1280 px, riduzione proporzionale senza ritagli. Pixel ridotti/compressi come da scelta; licenza CC BY-SA 4.0 e attribuzione conservate, modifiche dichiarate nel registro unico e nello snapshot offline. L’associazione del solo nuovo articolo usa l’avviso della variante compressa; non duplica il credito del vecchio uso integrale.

HTML autonomo v4: 9429717 byte, circa 9,43 MB, riduzione del 51,4% rispetto ai 19394650 byte precedenti. Copia bozza.html identica; bozza testuale v9 aggiorna soltanto segnaposto e credito della spiaggia. Testo didattico, dati, formule, grafico e domande invariati. Fonti scientifiche sempre nei crediti.

Controlli statici superati: CSS/script comuni identici, immagini correnti incorporate correttamente, copertina e GIF confrontate byte per byte con Git, nessun ID duplicato o ancora mancante, nessuna risorsa non accreditata. Chromium offline a 1280 e 390 px: immagine WebP caricata a 1920 × 1280 px, nessun overflow, errore JS o richiesta esterna; controlli pausa/ripresa della GIF e crediti della modifica funzionanti. Anteprime della spiaggia esaminate alle due larghezze; report verifiche-spiaggia.json, verifiche-finali.json e peso-visuali.json aggiornati.

Nessuna ulteriore compressione o conversione dei materiali; originali preservati. Salvataggio nella stessa PR #38; nessuna pubblicazione o integrazione in main.

## Pubblicazione autorizzata

Ricevuto «Ok pubblica» dopo l’HTML v4 con sola spiaggia compressa e copertina/GIF inalterate. Autorizzati aggiornamento di catalogo, manifest, navigazione reciproca, integrazione PR #38 in main e rilascio GitHub Pages. Nessuna ulteriore approvazione necessaria per queste operazioni.

Controllato il riferimento corrente main: a5a54f527db7b8052f09b49773dbcc7740a6d061, invariato rispetto alla base del ramo. Manifest v7 con otto articoli ammessi, nuovo articolo al terzo posto. Home v21; Temperatura ed equilibrio termico v3 e Stati della materia v20 per i soli collegamenti di navigazione e metadati di versione. Articolo 3 v4 invariato nel contenuto e nei byte. Articoli sospesi e indirizzi dismessi conservati invariati/esclusi. Piano e README aggiornati.

Build, controlli del catalogo e anteprime desktop/mobile precedono l’integrazione. Esito del rilascio e verifica pubblica da registrare dopo il deploy.

Controlli prima del rilascio superati: credits.py --sync/--check, build di 10 pagine HTML (home, crediti e otto articoli), catalogo nell’ordine approvato e download con 9,43 MB / 9429717 byte. Chromium a 1280/390 px: nuovo articolo al terzo posto, apertura dal catalogo e navigazione reciproca verificati; zero errori JS. Anteprime del catalogo e dei link adiacenti salvate, esaminate e consegnate in chat prima dell’integrazione. Report verifiche-pubblicazione.json. Articolo 3 identico ai byte approvati; nei due articoli adiacenti cambiano soltanto navigazione e metadati/footer di versione. Sette sorgenti esclusi confrontati byte per byte e assenti dall’output Pages. Allineato il generatore dell’articolo 2 alla navigazione corrente.

## Integrazione completata; rilascio in attesa del servizio GitHub

PR #38 integrata in main al commit 85fbb652b5c839c437c34f583c1a40b8885ede46, dopo i controlli e le anteprime già documentati. Workflow Pages avviato automaticamente: https://github.com/rickymusu-bit/fisica/actions/runs/39282063076 .

Al controllo del 19 ottobre 2026, ore 16:07 UTC (18:07 Europe/Rome), build e deploy ancora in coda senza runner assegnato, nessuna conclusione o errore applicativo. Pagina del nuovo articolo ancora HTTP 404; non dichiarata pubblicazione riuscita. GitHub Status conferma un incidente aperto, «Degraded availability for GitHub Actions, GitHub Pages and Webhooks», con Actions e Pages in degraded_performance e ritardi di workflow/site builds: https://www.githubstatus.com/ . Nessuna duplicazione o annullamento del rilascio pendente.

URL previsto dopo il rilascio: https://rickymusu-bit.github.io/fisica/energia_interna_calore_specifico_it.html . Da verificare dopo la ripresa del servizio: esito workflow e risposta pubblica, identità dei byte con HTML v4 approvato, terza posizione nel catalogo, download, navigazione reciproca e crediti. L’autorizzazione «Ok pubblica» resta valida per completare questi controlli e correggere eventuali problemi del rilascio.

## Nuovo tentativo richiesto dall’utente

Ricevuto «Riprova». Il 19 ottobre 2026, ore 16:12 UTC, ricontrollati workflow precedente e pagina pubblica: esecuzione ancora in coda e articolo HTTP 404. Richiesta di annullamento della vecchia esecuzione accettata da GitHub; avviato un nuovo workflow_dispatch sul main corrente 47510371271c2d740736d723a8135dc548b9e9fd, senza modifiche all’HTML approvato. Nuova esecuzione: https://github.com/rickymusu-bit/fisica/actions/runs/39283633815 .

Al controllo delle 16:13 UTC anche il nuovo tentativo è ancora in coda, senza esito. GitHub Status continua a segnalare degraded_performance per Actions e Pages e lo stesso incidente aperto. Pubblicazione non dichiarata completata; verifica pubblica ancora da svolgere dopo il rilascio.

## Pubblicazione completata e verificata

Ricevuto «Prova ora». Workflow 39283633815 completato con successo il 19 ottobre 2026 alle 16:40:25 UTC. Verifica del sito pubblico eseguita alle 18:51 UTC: HTTP 200 per articolo, catalogo, due articoli adiacenti e crediti. URL: https://rickymusu-bit.github.io/fisica/energia_interna_calore_specifico_it.html .

HTML pubblico identico byte per byte alla versione v4 approvata: 9429717 byte, SHA-256 cccb2c88fc9d4c96fae8240ae81cbbf8e327fdedd5a8a6531cf7815504f4baf0. Otto articoli nel catalogo nell’ordine del manifest, nuovo articolo terzo, download da 9,43 MB, navigazione reciproca e fonti nei crediti verificati. Report verifiche-sito-pubblico.json. Nessuna nuova esecuzione necessaria; pubblicazione autorizzata completata.

## Revisione richiesta: vapore acqueo e forma decimale

Richiesta esplicita: aggiungere il vapore acqueo ai gas della tabella e usare valori decimali anziché notazione scientifica; regola generale: numeri moderati leggibili in decimale e prefissi SI. Articolo v5, bozza v10. Tabella con undici righe, vapore acqueo a 100 °C: 2020 J/(kg · K), a pressione costante di 1 atm secondo OpenStax, College Physics §14.2, tabella 14.1. Dato e condizioni registrati nei crediti; fonte già presente riutilizzata con nuovo avviso per questo articolo. Gli altri dieci valori sono numericamente invariati, ora scritti senza potenze di dieci.

MASTER_PROMPT v62, A4 e rinvio AGENTS aggiornati alla preferenza generale senza imporre la notazione scientifica a tutti i calcoli. Nessuna revisione generale degli altri capitoli. Tema e risorse visuali invariati byte per byte. Verifiche statiche, crediti e build superati; Chromium offline 1280/390 px: undici righe, dati corretti, nessun overflow della pagina né errore JS, scorrimento interno della tabella su smartphone. Anteprime della tabella salvate e ispezionate. Report verifiche-tabella.json e verifiche-finali.json aggiornati. Richiesta circoscritta eseguita direttamente; aggiornamento della pagina pubblicata in corso.

Revisione pubblicata: PR #39 integrata al commit 667e1239debe230a1796331d7378af56c1dceed1. Workflow 39307005829 concluso con successo; verifica pubblica del 19 ottobre 2026 alle 18:59 UTC superata. Articolo v5 pubblico identico ai byte verificati, 9429445 byte, SHA-256 d04afd7d0886fc1f6ef178867fc0276bd29ddf43af328581f9f08e316345d47d. Undici valori decimali e riga del vapore inclusi; catalogo, download, navigazione e crediti pubblici verificati. Report verifiche-sito-pubblico.json aggiornato. Revisione completata.

## Segnalazione: tabella precedente e home con lista aperta

L’utente vede ancora la notazione scientifica e la lista degli articoli aperta all’arrivo nella home. Verifica HTTP pubblica: articolo corrente v5 già in decimale, undici righe incluso vapore; risposte con Cache-Control max-age=600. Non attribuita con certezza la copia vista dall’utente a una specifica cache. Per evitare il riuso di vecchie revisioni, la build della home aggiunge ai link lettura/download la versione effettiva del rispettivo articolo (?v=N), lasciando disponibili i percorsi canonici e il nome del file scaricato.

Individuata apertura automatica da hash #indice/#materia nello script della home: rimossa. Pannello chiuso all’ingresso e su pageshow, anche con ritorno dalla cronologia; apertura soltanto dai comandi espliciti. Home v22; articolo v5 invariato. Build e crediti superati. Chromium a 1280/390 px: ingresso normale/con hash e ritorno Indietro chiusi, apertura manuale, chiusura X/Esc, collegamento v5 e undici valori decimali verificati, nessun errore JS o overflow. Report verifiche-home-cache.json e anteprime home chiusa. Aggiornamento pubblico in corso.

Correzione pubblicata: PR #40 integrata al commit 354424cf3a4760beea8dc26557cb6f6329fda670, workflow 39308141252 riuscito. Alle 19:07 UTC home canonica e ?v=22 HTTP 200, identiche ai byte della build provata in browser; articolo ?v=5 HTTP 200, identico alla versione decimale verificata. Report verifiche-home-cache-pubblico.json. Browser pubblico diretto limitato dalla fiducia CA del browser; HTTPS verificato con trust di sistema e interazioni provate localmente sull’identico HTML, senza disabilitare la verifica TLS. Consegnare link home ?v=22 e articolo ?v=5 per richiamare subito le revisioni correnti. Segnalazione risolta; nessuna modifica del contenuto dell’articolo o dei sorgenti esclusi.

## Tema v9: comando crediti unificato

Richiesta approvata «Vaai» alla proposta di unificare i comandi dei crediti. Articolo v6 per la sola revisione del componente comune: un comando «Crediti e licenze» apre gli avvisi incorporati, con «Crediti di tutti gli articoli» al suo interno. Contenuto, undici valori decimali e visuali invariati. Bozza HTML allineata e controlli statici superati; browser offline a 390/1280 px e senza JavaScript verificato nel lavoro comune lavorazione/crediti_unificati, che registra anche il rilascio.
