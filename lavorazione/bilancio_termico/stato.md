# Stato — Il bilancio termico

Versione v10 · 19 ottobre 2026, ore 22:16 (Europe/Rome).

## Risultato corrente

**HTML autonomo v2 completato e verificato**, dopo il via «Ok vai». File ufficiale proposto: `bilancio_termico_it.html`; copia identica in [bozza.html](bozza.html). Tema canonico v9, master v63. Ramo `termodinamica/bilancio-termico`, allineato a main per riutilizzare il tema corrente; main non modificato e pubblicazione non autorizzata.

Articolo 4 del [percorso introduttivo](../percorso_termodinamica.md): energia ceduta e assorbita, convenzione dei segni, temperatura finale ed eventuale contributo della tazza. Esclusi cambiamenti di stato, calore latente, dilatazione e nuovi meccanismi di trasmissione. Caffè e latte con calori specifici approssimati a quello dell’acqua, come richiesto dall’utente.

## Approvazioni effettive

- Avvio: «Sul mio GitHub repo di fisica, facciamo l'articolo pianificato numero 4».
- Fenomeno caffè–latte e approssimazione del calore specifico scelti dall’utente.
- Foto correnti scelte tramite collegamenti specifici; copertina finale **Le Déjeuner di François Boucher** (richiesta «Scusa cambia con questo»). La foto del versamento è quella Rawpixel/NegativeSpace.
- «Ok vai» ricevuto dopo la bozza v4: approvazione del testo e via alla realizzazione. Non richiedere una seconda approvazione o un nuovo via per le stesse parti.
- Durante la realizzazione richiesto esplicitamente il grafico temperatura–tempo con le curve del latte e del caffè. La bozza v5 aggiunge soltanto spiegazione del grafico, segnaposto, didascalia e nota 3.
- Colori richiesti: caffè marrone scuro, latte beige marrone chiaro. Ultima richiesta: «Entrambe le curve con linea continua». Applicata anche alla legenda; questa indicazione sostituisce il precedente tratteggio.
- Nessuna autorizzazione a integrare in main, aggiornare catalogo/manifest o pubblicare.

Stima iniziale comunicata: 25–45 minuti, carico basso; materiali già disponibili, impaginazione nel tema comune, verifiche e salvataggio. Nessuna simulazione o esercizio svolto aggiunti.

## Contenuto e regole applicate

Letti AGENTS.md, MASTER_PROMPT.md v63, STILE_DISPENSE.md v6 ed esempio_irraggiamento.md v2; letto il tema v9 prima dell’impaginazione. Bozza v4 approvata conservata salvo aggiunta circoscritta GRA-02 richiesta; testo corrente in [bozza.md](bozza.md), v5. Nove domande finali senza soluzioni, sette formule, tre note collassabili inizialmente chiuse.

Convenzione Q positivo se assorbito e negativo se ceduto. Media pesata dalle masse quando il calore specifico è comune; media aritmetica soltanto per masse uguali. Per sostanze diverse conta la capacità termica. Nessuna misura dedotta dalle immagini e nessuna conversione implicita da volumi a masse. Condizioni del modello nelle note. Nessuna applicazione separata o nuovo esercizio svolto.

Tema riutilizzato senza modificare CSS, font, logo o script comuni. Formule autonome HTML con frazioni orizzontali e termini che vanno a capo su smartphone. Fotografie senza ingrandimento; grafico con ingrandimento canonico e scorrimento interno. Stessa composizione del grafico a tutte le larghezze. Il solo collegamento precedente punta all’articolo 3; nessun collegamento al futuro articolo di dilatazione ancora inesistente.

## Visuali, crediti e integrità

[visuali.md](visuali.md) registra le scelte. Cinque originali correnti incorporati senza trasformazioni:

- COP-01: Boucher, Le Déjeuner, 1739, Louvre RF 926; `copertina-boucher.jpg`, 1576 × 1942 px, 282712 byte. Fonte Commons, pubblico dominio PD-Art / Public Domain Mark 1.0. Conservato avviso sul distinto copyright GNU FDL della compilazione The Yorck Project.
- FIG-03: versamento, Burst secondo NegativeSpace, versione Rawpixel; `versamento-rawpixel.jpg`, 1024 × 683 px, 177074 byte, CC0. XMP originale conservato.
- FIG-01: caffè, Julius Schorzman; `caffe.jpg`, 960 × 720 px, 109150 byte, CC BY-SA 2.0. Avviso originale dell’autore conservato. La successiva figura FIG-04 illustra la tazza nella sezione sul recipiente.
- FIG-02: latte, NIAID; `latte.jpg`, 960 × 962 px, 137980 byte, CC BY 2.0. Documentata revisione Commons già ritagliata; nessun nuovo ritaglio.

- FIG-04: tazza vuota Black Velvet con piattino, Andy Mabbett (Pigsonthewing); `tazza-black-velvet.jpg`, 1920 × 1920 px, 427290 byte, CC BY-SA 4.0. Sostituisce il riuso di FIG-01 nella sezione sul calore scambiato dal recipiente.

Le copertine e il versamento precedenti restano come originali storici in risorse/, esclusi dagli utilizzi correnti. Font Lexend e OFL incorporati. Registro unico `risorse/crediti.json`, snapshot offline e pagina generale sincronizzati; nessun credito nel testo o nelle didascalie. Schede riusate per fonte; avvisi particolari conservati. Nessuna risorsa del nuovo articolo senza associazione.

## Grafico GRA-02

SVG originale in `risorse/temperatura-tempo.svg`, con Lexend incorporato. Caffè #4b2e1e e latte #af8961, entrambi continui. Nomi accanto alle curve e legenda; equilibrio puntinato a 60 °C. Asse t in secondi (0–300) e T in °C (10–90), stessa struttura desktop/mobile.

Dati dichiarati di modello: caffè 100 g a 80 °C e latte 50 g a 20 °C, calori specifici uguali. Il bilancio determina 60 °C; il tempo caratteristico di 60 s è un’ipotesi aggiuntiva e non una misura. Curve T_c = 60 + 20 exp(−t/60), T_l = 60 − 40 exp(−t/60), t in secondi; tazza e ambiente trascurati. Modello di scambio con flusso proporzionale alla differenza di temperatura; nessun formalismo di calcolo differenziale nel testo. Avvicinamento asintotico senza incrocio finito. Il precedente grafico calore–temperatura GRA-01 non era stato approvato e non è stato realizzato.

## Verifiche completate

- Generatore riproducibile [realizza.py](realizza.py); poi `scripts/credits.py --sync` e `--check`.
- [verifica.py](verifica.py): correttezza del modello su 301 campioni, energia costante entro 7,3 · 10⁻¹² J, curve monotone e senza incroci. Valori iniziali coerenti e capacità termiche rispettate.
- Confronto byte per byte di CSS e script canonici e SHA-256 delle cinque immagini incorporate; ID univoci, ancore risolte, nessun segnaposto o dipendenza esterna.
- Chromium offline a 1280 e 390 px: font, immagini, indice, Esc e focus, note con ritorni, crediti incorporati, pausa/ripresa del logo, movimento ridotto e ingrandimento/scorrimento del grafico. Nessun errore JavaScript, richiesta di rete o overflow della pagina e delle formule.
- Controllati indice, crediti e ingrandimento anche senza JavaScript. Ispezionate visivamente copertina, grafico finale e formula della temperatura di equilibrio su desktop/mobile.
- Build Pages e `git diff --check` superati. Manifest e catalogo invariati: il nuovo articolo non entra in `_site/`. Sorgenti esclusi invariati.

Report: [verifiche-finali.json](verifiche-finali.json) e [verifiche-browser.json](verifiche-browser.json). Anteprime desktop/mobile nella stessa cartella, incluse copertina, grafico, formula e versamento. HTML autonomo circa 2,61 MB, sotto il limite di 20 MB.

## Prossimo passo

Consegnare HTML interattivo e anteprime per la revisione del risultato. Salvare e verificare il caricamento nel ramo dedicato; eventuale integrazione in main e pubblicazione richiedono autorizzazione distinta. Non ripetere le scelte di foto, colori o tipo di linea già autorizzate.

## Salvataggio e consegna verificati

Realizzazione salvata nel commit ad1029b7da18c44b7a1ddf61bb9b74452746e564 e caricata sul ramo ufficiale dedicato. Verificati via download remoto SHA-256 dell’HTML, anteprima del grafico desktop e report finale: identici alle copie locali. PR in bozza [#42](https://github.com/rickymusu-bit/fisica/pull/42), senza integrazione in main né pubblicazione. HTML v1: 2188177 byte; copia bozza.html identica. Consegna: HTML autonomo interattivo, anteprime desktop/mobile e PR per revisione. Prossimo passo effettivo: eventuali correzioni al risultato o autorizzazione esplicita a pubblicare.

## Revisione HTML v2 — foto della tazza

Richiesta esplicita: «Metti questa quando parli del calore assorbito dalla tazza», con il collegamento alla foto Hostess Tableware Black Velvet di Andy Mabbett. Sostituita esclusivamente l’immagine nella sezione Anche la tazza partecipa, assegnando FIG-04; la foto del caffè all’apertura resta FIG-01. Copertina, testo didattico, formule, domande e grafico invariati, verificati con confronto del testo dell’articolo e SHA-256 del grafico. Bozza di testo v6 aggiornata soltanto nel segnaposto e nei crediti di servizio; HTML v2 e copia di lavorazione identici.

Originale scelto scaricato, osservato e incorporato integralmente senza ritagli, conversione o ricampionamento. Fonte e CC BY-SA 4.0 verificate su Commons; documentata la revisione Commons già ritagliata dall’autore. Nuova risorsa nel registro unico e crediti offline. HTML corrente: 2612961 byte (2,61 MB). Anteprime della tazza a 1280/390 px in anteprima-tazza-1280.png e anteprima-tazza-390.png. Verifiche statiche, immagini, browser offline desktop/mobile e senza JavaScript superate; check crediti e build Pages superati. Nessun aggiornamento al catalogo o alla pubblicazione. Salvataggio nella stessa PR #42.
