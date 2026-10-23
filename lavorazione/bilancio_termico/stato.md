# Stato — Il bilancio termico

## Revisione corrente — tagli delle precisazioni approvati, 23 ottobre 2026

L’utente ha approvato integralmente i 24 tagli proposti in chat con «Approvo, cancella tutti». Applicati a questo capitolo i punti 11; HTML corrente **v7**, data editoriale 23 ottobre 2026. Aggiornate le copie di lavorazione pertinenti, rimossi i richiami delle note eliminate e rinumerate quelle rimaste conservando le ancore. Master v69.6, riferimenti di stile v6 e campione v2 consultati; tema comune, formule, dati, immagini e simulazioni conservati.

Ramo `revisione/tagli-precisazioni`, derivato dal main aggiornato. Verifiche e schermate desktop/mobile nella [revisione condivisa](../sito/revisione-precisazioni/index.html). Crediti, tema, build e 14 test superati. L’utente ha autorizzato esplicitamente la pubblicazione dell’anteprima corrente con «Pubblica». Autorizzati merge della PR #62 e deployment GitHub Pages; nessuna ulteriore conferma necessaria. Controllo remoto della revisione 033919d65e35302b572c4b965f815ef5b24c4759 superato (Actions 39897584436). Esito del rilascio e verifica dei 12 URL pubblici da registrare nella [PR #62](https://github.com/rickymusu-bit/fisica/pull/62).

Versione v15 — 19 ottobre 2026, ore 22:42 (Europe/Rome).

## Risultato corrente

**Articolo pubblicato e verificato online**, su autorizzazione esplicita «Ok, puoi pubblicare». HTML autonomo v6: [Il bilancio termico](https://rickymusu-bit.github.io/fisica/bilancio_termico_it.html), con copia identica in [bozza.html](bozza.html). Tema canonico v10 e master v64 integrati in main attraverso la PR #42. Le indicazioni precedenti di pubblicazione in attesa sono storiche e superate.

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

## Revisione HTML v3 — presentazione del quadro

Richiesta esplicita: «Sotto la didascalia del quadro, parla del quadro». Aggiunto un paragrafo distinto sotto la didascalia della copertina, nello stesso figcaption con due paragrafi e gli stili canonici, senza nuovi riquadri o CSS. Presenta Le Déjeuner (La colazione), François Boucher, 1739, la scena domestica con adulti e bambini, luce, arredi e collocazione al Louvre. Autore, titolo, data e museo verificati sulla scheda ufficiale https://collections.louvre.fr/ark:/53355/cl010059924 ; descrizione visiva dall’opera già osservata. Fonte collegata dalla scheda del quadro nel registro unico e nei crediti offline. Nessuna attribuzione di identità alle persone o composizione delle bevande.

Testo corrente bozza.md v7; HTML e copia di lavorazione v3. Confronto del testo dell’article e SHA-256 del grafico conferma che la spiegazione di fisica, domande, formule e curve non sono cambiate. Tema CSS e script invariati. Controllo statico e prove browser offline a 1280/390 px: paragrafo sotto la didascalia, nessun overflow o errore JavaScript. Report verifiche-quadro.json; anteprima-quadro-1280.png e anteprima-quadro-390.png. Check crediti, build Pages e diff superati. Salvataggio nella stessa PR #42, senza pubblicazione.

## Revisione HTML v4 — didascalia breve del quadro

L’utente chiarisce che la descrizione del quadro doveva sostituire la didascalia originale, non seguirla, ed essere più breve. Eliminati sia il riferimento ridondante agli scambi di calore nella didascalia sia il lungo paragrafo aggiunto. La copertina ha ora una sola didascalia di due frasi: Le Déjeuner (La colazione), Boucher, 1739, adulti e bambini attorno alla tavola e collocazione al Louvre. Nessun testo aggiuntivo sotto la didascalia. Didascalia centrata sulla figura, secondo la correzione dell’utente e C3.

Bozza testuale v8, HTML e copia autonoma v4. Semplificato il generatore rimuovendo la gestione del paragrafo separato. Fonte museale conservata nei crediti. Testo didattico e grafico confrontati e invariati; modello, formule, domande e fotografie invariati. Anteprime e report del quadro aggiornati a 1280/390 px, nessun overflow o errore. Stessa PR #42, nessuna pubblicazione.

## Revisione HTML v5 — punto centrato riservato alla moltiplicazione

Richiesta esplicita dell’utente: mai usare il punto centrato come separatore, perché può confondersi con il segno di moltiplicazione. Regola integrata in A4 del master v64 e AGENTS.md: vale anche per titoli, didascalie, grafici, legende, testi accessibili, metadati descrittivi e piè di pagina. Esempio del footer aggiornato nel master.

Articolo v5: nei tre testi del grafico i separatori sono sostituiti da punti e punti e virgola. Piè di pagina con trattino lungo fra versione e data; titolo accessibile del logo con due punti. Formule e prodotti di unità conservano la moltiplicazione con punto centrato; testo didattico e formule confrontati e invariati. Curve, colori, dati e modello fisico invariati. Bozza testuale v9.

Modello canonico aggiornato a v10 negli stessi testi del footer e del titolo accessibile del logo, senza modificare CSS, font, disegno o comandi. Terminologia, istruzioni dei crediti, sorgente SVG del logo e suo generatore allineati per evitare ricomparse del separatore. Registro e snapshot aggiornati per le nuove impronte dei soli asset interessati. Nessuna modifica ai sorgenti HTML precedenti o sospesi, al catalogo o al manifest; pubblicazione ancora non autorizzata.

Verifiche pertinenti: assenza di simboli puntiformi nei testi del grafico e nel footer, moltiplicazioni inalterate, confronto del tema, anteprime desktop/mobile e browser offline. Salvataggio nella stessa PR #42.

## Pubblicazione autorizzata

Richiesta esplicita «Ok, puoi pubblicare»: autorizzati integrazione in main, catalogo, manifest, navigazione e rilascio Pages. L’autorizzazione supera i precedenti punti che indicavano la pubblicazione in attesa. HTML v6: contenuto didattico e grafico della v5 invariati; aggiunto soltanto il collegamento successivo a Stati della materia, in attesa del futuro capitolo sulla dilatazione.

Catalogo home v24 e manifest v8: nove articoli, bilancio termico al quarto posto dopo Energia interna e prima di Stati della materia. Collegamenti reciproci aggiornati: energia interna v7 → bilancio v6 → stati v22. Copie di lavorazione e generatore dell’articolo precedente allineati. Testi didattici degli articoli coinvolti confrontati e invariati. Sorgenti esclusi e indirizzi storici invariati. Crediti e snapshot sincronizzati; build Pages con 11 HTML italiani, inclusi home e crediti, e 20 copertine. Controlli offline desktop/mobile del nuovo articolo completati. Anteprima della sequenza di pubblicazione e verifica online da completare prima della consegna finale.

Anteprima della pubblicazione completata: verifiche-pubblicazione.json conferma ordine dei nove articoli, download e percorso catalogo → bilancio → precedente/successivo a 1280/390 px. Nessun errore JavaScript o richiesta esterna nelle prove con output Pages locale. Anteprime catalogo e navigazione consegnate prima dell’integrazione. Pubblicazione tramite la PR #42 e controllo del workflow Pages e dell’URL online dopo il merge.

## Rilascio concluso e verifica online

PR #42 integrata nel commit b33c37b64cfd8157403204990691799114080180. Workflow GitHub Pages [39321182318](https://github.com/rickymusu-bit/fisica/actions/runs/39321182318) completato con successo, build e deploy entrambi riusciti.

Controllati gli URL pubblici senza parametri: home v24, bilancio v6, energia interna v7, stati v22 e crediti, tutti HTTP 200. I tre HTML degli articoli coinvolti sono identici byte per byte alle versioni locali verificate. Catalogo pubblico con nove articoli nell’ordine corretto; navigazione reciproca verificata. Report completo in [verifiche-online.json](verifiche-online.json). Nessuna pubblicazione pendente o materiale mancante; capitolo concluso.
