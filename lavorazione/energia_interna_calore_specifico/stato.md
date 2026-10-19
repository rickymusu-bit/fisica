# Stato — Energia interna, calore e calore specifico

Versione v4 · Aggiornamento: 19 ottobre 2026 (Europe/Rome).

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

Progettazione delle visuali: proposta concreta v4 salvata in [visuali.md](visuali.md), comprendente domanda iniziale, percorso, confini, tre immagini da scegliere, grafico e tabella proposti e otto nuclei per le domande finali.

Domanda guida scelta dall’utente: «Perché d’estate il mare resta tiepido di notte, anche quando la sabbia è fredda?». Richiesta effettiva: «Allora chiedi perché d'estate il mare resta tiepido di notte anche se la sabbia è fredda». Sostituisce l’apertura sul deserto; autorizzato l’adattamento del percorso e delle proposte visuali, senza attribuire approvazioni a immagini specifiche.

COP-01: spiaggia estiva con mare e sabbia, copertina distinta. FIG-01: battigia di sera o di notte. FIG-02: modello microscopico. GRA-01: temperatura in funzione del calore per masse uguali di acqua e sabbia asciutta, con dati documentati. TAB-01: confronto di calori specifici. Identificativi e funzioni in visuali.md; nessuna nuova scelta attribuita all’utente.

Nessuna simulazione o video proposti: nessuna programmazione, nessun costo di simulazione da stimare. Nessun esercizio svolto o sezione autonoma di applicazioni aggiunti.

## Verifiche e limiti

Identificati numero e titolo dal piano ufficiale. Controllati confini rispetto agli articoli 2 e 4; distinta energia interna dal moto macroscopico e distinta capacità termica dal calore specifico. Il futuro grafico deve rappresentare previsioni, senza inventare misure. La relazione quantitativa non sarà applicata a cambiamenti di stato. Per la spiaggia: c dell’acqua maggiore di quello della sabbia asciutta; a parità di massa ed energia ceduta, minore diminuzione di T. Distinguere questo confronto dal mare reale, dove contribuiscono massa d’acqua coinvolta e rimescolamento. Non assumere uguali masse o uguali perdite di energia per mare e spiaggia, né temperature ricavabili dalle fotografie. Nessun valore universale di c assegnato a sabbie di composizione diversa.

Esaminati materiali già scelti nei primi due articoli: caffè riutilizzabile per richiamo contestuale, ma non necessario alla nuova apertura; bevanda con ghiaccio non adatta a illustrare qui Q = m · c · ΔT. Non cercate, generate o modificate nuove immagini.

Bozza completa v1 creata in bozza.md dopo il «Vai» dell’utente, ricevuto dopo la scelta della domanda sulla spiaggia. Il comando autorizza la stesura corrente; non è approvazione di un testo che ancora non esisteva né scelta dei file delle immagini. Nessun HTML creato. Nessuna verifica HTML/browser o build pertinente a questa fase documentale viene dichiarata eseguita. La shell non raggiunge il proxy nella sandbox predefinita; lettura e salvataggio ufficiali effettuati tramite connettore GitHub.

## Prossima operazione

Presentare bozza.md v1 per revisione; stesura già autorizzata e completata, non richiederne nuovamente il via. Ricevere i tre file/collegamenti di spiaggia estiva, battigia serale/notturna e modello microscopico. Dopo il testo approvato, fornire stima totale ripartita e raccogliere via esplicito all’HTML secondo B1.1–B2. Nessuna approvazione dedotta dall’elenco già approvato.

## Bozza v1 completata

Richiesta aggiuntiva effettiva: «Vai». Bozza completa salvata con apertura scelta dall’utente, spiegazione microscopica di U, distinzione temperatura/energia interna/calore, C e c, Q = C · ΔT, C = m · c, Q = m · c · ΔT e relazione inversa con frazione. Segni nel raffreddamento introdotti senza bilancio fra corpi. Ritorno conclusivo al mare, otto domande senza soluzioni e tre note brevi. Nessuna sezione opzionale o simulazione aggiunta.

TAB-01 include acqua pura a 20 °C e sabbia quarzosa indicativa; fonte Engineering ToolBox consultata direttamente. Valori arrotondati 4,18 · 10³ e 8,3 · 10² J/(kg · K). Temperatura e umidità della sabbia non specificate dalla fonte, limite esplicito in nota; non presentarla come misura della spiaggia. Specifiche del grafico nel segnaposto GRA-01: m = 1 kg, T_i = 20 °C, Q da 0 a 1 kJ, due rette dal modello, senza dati sperimentali inventati. Consultata anche OpenStax, College Physics, §14.2 per il controllo della relazione e delle unità; testo formulato autonomamente.

Controllo scientifico e redazionale svolto: simbolo T, unità, proporzioni, segni, distinzione c/C, modello microscopico senza equiparare solidi a gas ideali, confronto mare reale distinto da masse uguali, nessun anticipo del bilancio termico o del calore latente. Segnaposto COP-01/FIG-01/FIG-02/GRA-01/TAB-01 presenti, copertina distinta, otto domande numerate e richiami delle note coerenti. Immagini specifiche mancanti; nessuna ricerca di immagini o generazione effettuata. Bozza testuale da approvare, non HTML definitivo. Nessuna build/browser pertinente a questa fase.
