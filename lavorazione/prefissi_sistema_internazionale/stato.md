## Revisione delle tabelle — 25 ottobre 2026

Ricognizione su tutti i 19 capitoli pubblicati, verifica CSS su desktop e mobile. Corrette 8 tabelle di questo capitolo secondo le regole correnti: intestazioni e dati centrati, mantenendo a sinistra solo colonne di testo discorsivo esteso. HTML ufficiale v5 → v6. Testi scientifici, dati, formule, ordine di righe e colonne, animazioni e media invariati. Data editoriale conservata: modifica soltanto grafica. Bozza: allineata e versionata. Rapporto in lavorazione/sito/allineamento-tabelle.md. Ramo in lavorazione; merge e pubblicazione richiedono approvazione esplicita.

## Revisione corrente — economia informativa, 24 ottobre 2026

Richiesta esplicita dell’utente: «Okay, riscrivi e taglia in modo opportuno», dopo la ricognizione dei 17 capitoli pubblicati. Master v69.15, AGENTS.md, stile v7 e standard dei visuali consultati. Revisione editoriale autorizzata nel ramo `revisione/economia-informativa`; nessuna autorizzazione al merge o alla pubblicazione.

HTML corrente **v5**, derivato da v4. Ridotte ripetizioni fra testo, didascalie e istruzioni; note selezionate e rinumerate con ritorni aggiornati. Tema, fotografie, formule principali e codice delle simulazioni conservati. La copia HTML di lavorazione, dove presente, è riallineata; l’HTML revisionato prevale sulle bozze testuali e sui generatori storici che descrivono stesure precedenti.

Interventi e controlli nella [revisione comune](../sito/economia-informativa/README.md). Prossimo passo: valutazione dell’anteprima corrente e approvazione esplicita prima di integrare main o aggiornare Pages. Le autorizzazioni storiche sottostanti non si estendono a questa revisione.

# Stato — I prefissi del Sistema internazionale

Versione v8 — 23 ottobre 2026 (Europe/Rome).

## Incarico e fase corrente

Richiesta: «Sviluppa il capitolo 4 del piano di lavorazione per l'introduzione alla fisica nel mio repository di fisica».
Il [piano editoriale](../introduzione_fisica_misura/piano.md) identifica il capitolo come **I prefissi del Sistema internazionale**.
Argomento, posizione e tema Stringhe comune sono già definiti. La richiesta avvia lo sviluppo editoriale; non documenta una scelta delle nuove visuali né approvazioni della bozza, dell'HTML o della pubblicazione.

Fase corrente: **HTML v2 approvato con separatore, pubblicazione autorizzata e in preparazione**. Il via «Ok genera» autorizza la realizzazione dal testo v3; la bozza v4 aggiorna copertina e provenienza. [HTML corrente](bozza.html), [bozza testuale](bozza.md), [verifiche](verifiche-finali.json), [schermate desktop/mobile](anteprime/).
Copertina scelta con URL Wikimedia: colonia di batteri e funghi al microscopio, Korinna, CC BY 4.0, incorporata intera a 960 per 957 px. Nessuna immagine mancante. Merge e deployment autorizzati dalla richiesta finale; le attese di copertina e realizzazione riportate nelle sezioni precedenti sono superate da questo avanzamento.

Ramo dedicato: `lavorazione/prefissi-sistema-internazionale`, derivato da main al commit `d5688f6af867cd85bcdb8f975ddb538e3f3c1130`.
Alla verifica iniziale dell'albero completo di main e dei rami con nome contenente «prefissi» non risultano una lavorazione o un ramo preesistenti per questo capitolo.

## Fonti e identità del materiale

- Regole: `MASTER_PROMPT.md` **v69.7**, letto integralmente in blocchi; `AGENTS.md`; `riferimenti/STILE_DISPENSE.md` v6; `riferimenti/esempio_irraggiamento.md` v2; `docs/visual-guidelines.md` v1.0.0.
- Sorgente: `sistema_internazionale_notazione_it.html`, sezione `#prefissi`, blob `61a32e96afce2136af8669b1544a02e9d751018d`. Metadato document-version v10 e piè di pagina v12 non allineati: per questa progettazione l'identità è fissata dal blob; non correggere il sorgente storico nell'ambito del nuovo capitolo.
- Letti lo stato del sorgente, il manifest `pubblicazione.json` v12 e la bozza corrente del capitolo 3 per la continuità e la ripartizione dei quesiti.
- Lo stato del capitolo 2 documenta la fotografia `../grandezze_fisiche_sistema_internazionale/risorse/metro.jpg`: Nenad Stojkovic, CC BY 2.0, già scelta dall'utente e verificata in quel lavoro. Per un eventuale riuso associare la scheda esistente del registro unico al nuovo capitolo, senza duplicarla.
- Fonte normativa da consultare nella stesura: [BIPM, SI Brochure](https://www.bipm.org/en/publications/si-brochure), tabella dei prefissi e regole dei simboli. In questa fase non si dichiara eseguita una nuova consultazione esterna.

## Confini e domanda iniziale

Domanda proposta: «La stessa lunghezza può essere scritta come 1 m, 100 cm oppure 1000 mm: perché cambia il numero, mentre la lunghezza rimane la stessa?».
Usare la fotografia del metro come contesto, senza attribuirle una misura numerica non verificata.

Il capitolo spiega il prefisso come fattore decimale esatto, multipli e sottomultipli, simboli e maiuscole, conversioni anche tra due unità prefissate e scelta di una scrittura leggibile.
Conservare i 24 prefissi del sorgente, compresi quetta, ronna, ronto e quecto; dare maggiore spazio nell'esposizione ai prefissi di uso comune.
Spiegare il caso della massa: il kg è unità di base, ma i prefissi si applicano al grammo.
Includere un breve passaggio sul prefisso quando l'unità è elevata a potenza, per evitare di estendere erroneamente il fattore lineare ad aree e volumi.

Richiamare le potenze del capitolo 3 soltanto quanto serve alle equivalenze. Non ripetere il capitolo sul SI e non anticipare conteggio, arrotondamento o regole delle cifre significative del capitolo 5, strumenti, errori o propagazione delle incertezze. Nessuna digressione sui prefissi binari.

## Corrispondenza con il sorgente

| Contenuto originale | Destinazione nel capitolo 4 |
| --- | --- |
| Apertura di #prefissi, km e mm, M e m, prefisso unito al simbolo | Sviluppo narrativo e lettura dei simboli |
| Scala illustrata yotta–yocto | Conservare nel sorgente; riuso nel nuovo capitolo da valutare secondo la proposta |
| Tabella dei 24 prefissi, inclusi quelli del 2022 | Tabella completa conservata, con contenuti e simboli controllati |
| Conversioni 2,5 km e 0,8 µm | Conservare nella spiegazione delle equivalenze |
| Prefissi del grammo e relazione mg–g–kg | Passaggio sulla massa |
| Quesito originale 6, Mm e mm | Conservare integralmente nelle domande del nuovo capitolo |
| Parte sui prefissi del quesito originale 5 | Riprendere soltanto il collegamento 47 · 10⁻⁶ m = 47 µm; la trasformazione scientifica/ingegneristica è già nel capitolo 3 |
| Quesito originale 12, fattore 100 e cifre significative | Resta assegnato al capitolo 5; qui spiegare solo l'esattezza del fattore |

Le altre domande originali restano negli altri capitoli: non ricopiarle per aumentare il numero dei quesiti.

## Visuali e scelte aperte

Proposta dettagliata in [visuali.md](visuali.md):
COP-01, riuso della foto del metro già scelta, soltanto in copertina;
TAB-01, tabella completa dei prefissi;
TAB-02, confronto di scritture equivalenti;
SCH-01, schema numerico dei passaggi di conversione;
TAB-03, confronto dei fattori per lunghezza, area e volume.

La scala illustrata originale si ferma a yotta/yocto, mentre la tabella è aggiornata ai 24 prefissi. La provenienza della scala non è documentata nel sorgente. Proposta: affidare tabella e conversioni a elementi numerici autonomi, conservando l'originale nel sorgente senza modificarlo. Questa scelta editoriale resta da concordare; nessun ridisegno dell'immagine è stato eseguito.

Nessuna nuova fotografia necessaria nell'impostazione consigliata; nessuna immagine cercata, scaricata o generata. Nessuna simulazione proposta: tabelle e schema statico sono sufficienti e non richiedono comandi aggiuntivi.

## Lavoro completato e verifiche

Identificati piano, sorgente e confini; verificati simboli, 24 fattori del prospetto originale e relazioni numeriche previste nella proposta.
Controllata la continuità con il capitolo 3 e la distinzione dal capitolo 5.
Preparati proposta visuale, stato e aggiornamento circoscritto del piano. Verificare il salvataggio remoto dei tre Markdown prima della consegna.

Questa fase modifica solo documenti editoriali: nessun HTML, registro dei crediti, manifest o contenuto pubblicato viene aggiornato. Non sono necessarie build o prove nel browser; non vengono dichiarate verifiche HTML.

Checklist: A1–A5 (livello, monograficità, notazione e quesiti), B1.1–B2 (visuali prima della bozza; approvazione e via prima dell'HTML), B4–B6 (riuso, stato e salvataggio), C1–C4 (immagini, fonti, tabelle e composizione stabile), D1–D2.1 e AGENTS.md (verifiche pertinenti, ramo dedicato, PR in bozza, nessun merge o deployment senza approvazione corrente).

Prossimo passo: revisione e approvazione della bozza v3 e ricezione della nuova copertina dall'utente. Prima dell'HTML leggere il modello Stringhe corrente, presentare la stima ripartita e attendere il via previsto dal master.

## Integrazione richiesta — conversioni tra prefissi

L'utente scrive: «Aggiungi anche come convertire tra prefissi. Riutilizza la tabella dei prefissi. A che schema ti riferisci?».
Registrati il riuso della tabella esistente e l'ampliamento delle conversioni tra due prefissi. Proposta v2: uso dei fattori della tabella, passaggio per l'unità di riferimento e lettura diretta della differenza degli esponenti; conversioni cm–mm e µm–mm in entrambi i versi, oltre a km–mm. Aggiornato il quesito 4 per verificare la conversione tra due prefissi e il controllo inverso.

Chiarito che SCH-01 è una sequenza numerica con frecce e fattori, per esempio km → m → mm, non una nuova tabella. La richiesta di chiarimento non approva né rifiuta lo schema. Registrata l'alternativa di spiegare i medesimi passaggi nel calcolo accanto alla tabella, senza figura separata. Nessuna nuova visuale realizzata e nessuna approvazione estesa automaticamente a copertina, bozza o HTML.

Verificate le equivalenze 3,2 cm = 32 mm, 750 µm = 0,750 mm e 2,5 km = 2 500 000 mm, le rispettive conversioni inverse e il segno della differenza degli esponenti. Master su main ancora v69.7, blob invariato rispetto alla lettura precedente. Aggiornati soltanto i tre Markdown della progettazione, nella stessa PR #65 in bozza.

## Schema richiesto e bozza v1 — 23 ottobre 2026

L'utente autorizza espressamente lo schema con «Ok fai lo schema». Questa indicazione supera lo stato opzionale/non approvato registrato prima: SCH-01 è realizzato in `risorse/schema-conversioni.svg`. Riuso della tabella dei prefissi già richiesto nel messaggio precedente. La foto del metro resta quella già scelta e documentata per il capitolo 2; nessuna ricerca o sostituzione fotografica.

Schema costruito come SVG autonomo con titolo e descrizione accessibili, fondo bianco e colori piatti. Due sequenze: km–m–mm con fattori 1000 e reciproci; cm–mm–µm con fattori 10, 1000 e reciproci. Esempi numerici distinti, frecce nei due versi, nessun fattore affidato al solo colore. Composizione stabile; nell'HTML futuro applicare l'ingrandimento del tema su mobile.

Preparata [bozza v1](bozza.md): apertura sul cambio di unità, tabella originale dei 24 prefissi, simboli, conversioni per passaggio intermedio e differenza degli esponenti, grammo, aree e volumi, otto domande senza soluzioni. Conservate le conversioni del sorgente; schema collocato nella spiegazione. Non è una bozza HTML e non implica approvazione del testo o della pubblicazione.

Controllo scientifico: consultata la pagina ufficiale [BIPM, SI prefixes](https://www.bipm.org/en/measurement-units/si-prefixes) e confrontati i 24 simboli/esponenti. Verificati fattori, risultati e conversioni inverse con aritmetica decimale esatta; controllate potenze di area/volume e otto quesiti. SVG valido come XML, renderizzato in Chromium a 960 e 390 px: nessuna etichetta fuori dal viewBox, nessun overflow nella prova responsive con ridimensionamento proporzionale. Ispezionate entrambe le schermate: a 390 px è necessario l'ingrandimento previsto dal tema; non dichiarare che le scritte ridotte bastino alla lettura. Nessuna prova HTML completa o build del sito dichiarata.

Schema originale numerico, senza risorse esterne o licenze di immagini da dedurre. La bozza conserva le fonti nella sezione di servizio; registro unico e crediti del nuovo capitolo saranno aggiornati nella realizzazione. Salvare e rileggere sul ramo gli stessi file della PR #65, senza merge né deployment.

## Revisione v2 — potenze di 10 in tutto il capitolo

Richiesta esplicita dell'utente: «visto che questo capitolo viene dopo quello sulla notazione esponenziale, devi assolutamente usare le potenze di 10 dovunque».

Applicata al capitolo la notazione con potenze di 10 in tutte le conversioni, nei fattori diretti e inversi, nelle equivalenze numeriche, nelle tabelle (anche massa e unità elevate a potenza), nei quesiti pertinenti e nello schema, compresa la descrizione accessibile. Questa scelta specifica supera per il capitolo 4 la preferenza generale di A4 per i numeri decimali moderati; non modifica il master o gli altri capitoli. La tabella originale dei 24 prefissi resta invariata.

Esplicitati somma degli esponenti nelle conversioni successive, differenza degli esponenti nel rapporto dei prefissi e prodotto degli esponenti per area/volume. Schema aggiornato sullo stesso percorso, con fattori 10³ e 10⁻³, 10¹ e 10⁻¹; esempi 2,5 km = 2,5 · 10³ m = 2,5 · 10⁶ mm e 3,2 cm = 3,2 · 10¹ mm = 3,2 · 10⁴ µm. Bozza v2 sullo stesso percorso, otto quesiti conservati e adattati nella notazione.

Verificati con aritmetica decimale fattori, risultati e inverse, esponenti di area/volume e assenza dei vecchi fattori decimali nel contenuto didattico. Schema XML valido, renderizzato e ispezionato a 960 e 390 px senza tagli o overflow; ingrandimento da mantenere nell'HTML futuro per la lettura mobile. Modello, foto, geometria dello schema e argomenti non interessati conservati. Non necessaria una build del sito per Markdown e SVG; nessuna verifica HTML completa dichiarata. Revisione da rileggere sul ramo prima della consegna; PR #65 in bozza, nessun merge o deployment.

## Revisione v3 — notazione contestuale, formula e unità derivate

L'utente precisa l'uso della notazione: niente potenze nel testo introduttivo, valori anche in potenze nella tabella introduttiva, poi potenze dove servono al contesto. Richiede formula e procedura esplicite, esempi anche con unità derivate e una nuova copertina che fornirà personalmente. Questa indicazione supera la precedente estensione delle potenze a ogni scrittura numerica e ritira il riuso della foto del metro.

Bozza v3: ripristinati 1 m, 100 cm e 1000 mm nell'apertura; TAB-02 ha tre colonne con scrittura iniziale, valore decimale e potenza. Conservata la tabella originale dei 24 prefissi. Dalla sezione dedicata, fattori e passaggi usano le potenze dove chiariscono il ragionamento, con risultati decimali leggibili quando opportuni.

Presentate definizioni delle due unità rispetto a U, uguaglianza della grandezza e formula generale x_arrivo = x_partenza · 10^(p − q), con p esponente di partenza e q esponente di arrivo. Procedura in quattro passi e formula per unità elevate a potenza, fattore 10^[n(p − q)]. Nessuna nuova approvazione richiesta per questa revisione esplicita del testo.

Aggiunta sezione «Esempi di conversione» richiesta: MPa → kPa; cm² → m²; mm³ → cm³; g/cm³ → kg/m³. Distinto il prefisso di un'unità derivata con nome proprio dal prefisso di un'unità elevata a potenza. Per la densità sostituiti separatamente numeratore e denominatore, mostrando la frazione. Dati assegnati per esercitare equivalenze, non misure o proprietà attribuite a materiali reali. Segnaposto CONV-01–04 per schemi puramente numerici prima dei calcoli; nessun oggetto da cercare o generare. Interpretazioni quantitative dei risultati incluse. Domande finali portate a dieci per coprire formule ed esempi nuovi.

COP-01 è ora soltanto un segnaposto per l'immagine dell'utente: nessuna didascalia, licenza o soggetto inventati; nessuna ricerca autonoma. L'immagine del metro nel capitolo 2 rimane conservata e non va associata ai crediti del nuovo capitolo. Schema SCH-01 invariato e verifiche grafiche precedenti riutilizzate.

Controlli svolti: introduzione senza potenze fuori dalla tabella, doppia scrittura nella tabella introduttiva, tabella di 24 prefissi conservata, dieci quesiti, assenza del percorso metro.jpg nella bozza. Verificati con aritmetica decimale esatta risultati e inverse delle conversioni, fattori quadrati/cubici e densità, più coerenza numerica dei nuovi quesiti. Formule e procedura rilette per esponenti, unità di riferimento comune e trattamento del denominatore. Nessun SVG o HTML modificato; nessuna nuova prova browser o build necessaria. Master corrente v69.7 invariato. Rileggere i quattro Markdown sul ramo dopo il salvataggio; PR #65 in bozza, nessun merge/deployment.

## Registrazione delle regole — master v69.8

Alla domanda «Okay, ma hai registrato le regole?» verificato che le indicazioni correnti erano già presenti nello stato e nella progettazione del capitolo, mentre il master generale era ancora v69.7.

Integrate nelle sezioni pertinenti di MASTER_PROMPT.md v69.8 le regole riutilizzabili: A2 distingue la prevalenza dello stile discorsivo dall'obbligo di rendere tutto narrativo; A4 richiede formule generali riconoscibili con simboli definiti, procedure esplicite quando necessarie e scelte di notazione guidate da contesto e progressione, con fattori in potenze quando spiegano il metodo e decimali utili all'interpretazione. Evitate aggiunte in coda o regole specifiche del capitolo estese indiscriminatamente agli altri.

Restano specifiche del capitolo 4, già registrate nella revisione v3: apertura senza potenze nel testo; tabella introduttiva con entrambe le scritture; formula dei prefissi e casi elevati a potenza; esempi anche con unità derivate; copertina nuova da fornire dall'utente e ritiro del metro. Bozza v3 invariata, da approvare.

Master su main confrontato: ancora v69.7 con identico blob rispetto al ramo prima della modifica. Consolidata v69.8 sullo stesso ramo della PR #65; non è una modifica già integrata in main. Controllate le sole sezioni A2/A4 e l'intestazione, conservando le altre regole. Stato e master da rileggere dal commit remoto dopo il salvataggio. Nessuna modifica HTML, build o pubblicazione.

## Realizzazione autorizzata e copertina scelta — 23 ottobre 2026

L'utente dà il via con «Ok genera». Comunicato l'ambito e una stima indicativa di 20–35 minuti a carico basso; avviata la realizzazione sul ramo esistente, senza ulteriori richieste di via. Durante le verifiche l'utente sceglie la copertina tramite URL Wikimedia: approvazione specifica dell'immagine, nessuna nuova conferma necessaria.

Fonte: [Microscope view of a bacteria and fungi colony growing in fractal pattern structures](https://commons.wikimedia.org/wiki/File:Microscope_view_of_a_bacteria_and_fungi_colony_growing_in_fractal_pattern_structures.jpg). Autore Korinna, CC BY 4.0, verificati sulla pagina originale. Miniatura scelta 960 per 957 px, SHA-256 15d982bd40344f54fa9c77b0eea3fb67d3a41b4d851daeb5b604f18d9851b575, salvata in risorse/copertina-colonia.jpg senza ritagli o modifiche locali. Il server thumb.wikimedia.org ha risposto 403: recuperata la stessa miniatura dal server upload.wikimedia.org. URL scelto, URL effettivo e provenienza in risorse/copertina-fonte.json; attribuzione nel registro unico. Nessuna dimensione fisica o ingrandimento dedotti dalla foto.

Realizzato HTML v1 autonomo prefissi_sistema_internazionale_it.html, copia corrente identica in bozza.html, modello Stringhe v23 letto e riutilizzato. Testo v3 conservato; bozza v4 aggiornata solo per copertina e registrazione della realizzazione. Diciotto formule in MathML nativo, frazioni orizzontali e catene di uguaglianze che vanno a capo; nessuna dipendenza MathJax/KaTeX. Otto tabelle complessive, schema SVG ingrandibile, quattro schemi numerici degli esempi, procedura in quattro passi e dieci quesiti. Nessuna nota o sezione di servizio inventata. Copertina presente soltanto in testa; zoom, indice, menu e crediti canonici conservati. Rimando al capitolo precedente pubblicato; nessun rimando a un capitolo successivo ancora inesistente.

Controlli: credits.py --check superato (31 documenti, 151 schede, 223 risorse); build Pages locale riuscita (18 HTML italiani e 20 copertine), nuovo capitolo correttamente escluso dal manifest e dall'output pubblico. Altri 30 documenti del registro e rispettive occorrenze invariati. Verificati hash di 72 copie originali e identità dei componenti comuni del modello. Registro esteso solo per il nuovo capitolo, la copertina e lo schema; crediti.html pubblico invariato. Nessuna migrazione generale degli snapshot.

Browser Chromium a 320, 390, 768, 1024 e 1440 px, chiaro/scuro, senza overflow del documento: formule, frazioni, immagini decodificate, indice con Escape/ancore, scorrimento delle tabelle con tastiera, zoom dello schema, crediti incorporati e licenza OFL, download byte per byte, fallback senza JavaScript e contenuti incorporati senza rete. Menu Tema provato con selezione effettiva; foto incorporata confrontata con i byte scelti. Ispezionate copertina mobile, formula generale mobile/desktop, tabella mobile e sezione della densità desktop. Tabelle e schema conservano composizione e usano scorrimento/ingrandimento. Nessuna verifica dichiarata su altri motori browser.

Verificata anche la brochure SI ufficiale BIPM, sezioni 3 e 5: prefissi uniti ai simboli, unità prefissate elevate a potenza e prefissi della massa applicati al grammo. Peso HTML 749254 byte, sotto il limite. Rapporti verifiche-finali.json e verifiche-browser.json; generatore realizza.py e verifica ripetibile verifica_browser.py salvati nella lavorazione.

Prossimo passo: revisione dell'anteprima corrente con la copertina scelta. PR #65 da mantenere in bozza; nessun merge o deployment prima dell'approvazione esplicita di questa anteprima secondo AGENTS.md. Salvare e rileggere i file sul ramo prima della consegna; verificare il collegamento dell'anteprima interattiva.

## Caricamento dell’anteprima sospeso dal controllo automatico

Anteprima, copertina e schermate sono complete nel workspace. Il controllo automatico ha rifiutato il caricamento GitHub della schermata anteprime/copertina-dark-1440.png, motivando l'assenza di un'autorizzazione esplicita all'uscita dei contenuti dell'anteprima verso il repository pubblico. Un secondo tentativo della stessa operazione ha confermato il rifiuto; nessuna via alternativa di trasferimento utilizzata. Sospeso il caricamento dell'anteprima. Richiesta all'utente l'autorizzazione esplicita per HTML e schermate nella PR #65; risposta pendente.

Il blob della copertina scelta è stato creato prima del rifiuto, ma nessun commit di realizzazione è stato creato e nessun ramo è stato spostato. La PR remota resta alla progettazione/testo del commit 4912884d897c7b19a5f2bb5274a2bf4888ca2389. Non presentare HTML o schermate come già caricati. File locali pronti per la revisione: prefissi_sistema_internazionale_it.html e lavorazione/prefissi_sistema_internazionale/anteprime/.

## Consegna soltanto in chat — scelta dell'utente

L'utente risponde alla richiesta di autorizzazione con «Consegna soltanto i file qui». Caricamento dell'anteprima definitivamente sospeso per questo incarico: nessun trasferimento alternativo, commit o aggiornamento della PR effettuato. Consegna locale di HTML autonomo e schermate. Diciassette test automatici superati; controllo globale sync_stringhe_theme.py --check superato, con modello, confronto e crediti allineati.

Contenuti, copertina e verifiche restano conservati nel workspace; file di consegna in /workspace/consegna/. La pubblicazione non è autorizzata. Per un eventuale futuro salvataggio dell'anteprima nel repository rispettare la scelta corrente e richiedere nuove istruzioni dell'utente.

Nota sulle verifiche locali: il primo --check del tema aveva rilevato soltanto un newline finale aggiunto nel recupero della pagina di confronto. Ripristinata la copia locale ai byte del sorgente, il controllo completo è passato. Nessuna modifica al tema o alla pagina originale nel repository.

## Separatore, caricamento e pubblicazione autorizzati

L'utente scrive: «Ok per il capitolo 4. Solo metti un separatore nella tabella dei prefissi prima della colonna dei sottomultipli, per leggibilità. Poi procedi a caricamento e pubblicazione». Questa autorizzazione esplicita supera la precedente scelta di consegna solo in chat e il blocco del controllo automatico basato sull'assenza di autorizzazione all'uscita dei contenuti verso GitHub. Autorizzati caricamento del capitolo e delle schermate nella PR #65, merge e deployment Pages dopo le verifiche.

HTML v2: aggiunto un bordo verticale di 2 px prima della quarta colonna di TAB-01, intestazione e dodici righe, usando il token di contrasto del tema. Nessun dato modificato. Separatore verificato a 390 e 1440 px in chiaro/scuro, con scorrimento interno su mobile. Pubblicazione al quarto posto dell'area introduttiva; manifest v13 con quattordici capitoli, catalogo e crediti aggiornati, navigazione reciproca Potenze → Prefissi → Termodinamica. Copie correnti riallineate. Conservate le modifiche della home e del collegamento al repository già presenti nel main c29b6528b6089570adbf7d6674b03ad47edddea5.

La richiesta corrente comprende anche le due correzioni già richieste: metodo scientifico v12 senza zoom sulla copertina, potenze v6 con esponenti nel flusso tipografico corretto. Regola generale sulle copertine in MASTER_PROMPT.md v69.9 e AGENTS.md, filtro nel componente canonico e prova di regressione; formule e testo dei due capitoli preservati. Termodinamica v14 modificata soltanto nella navigazione adiacente. Nessuna riammissione dei sorgenti esclusi.

Verifiche: crediti, build e diciotto test; tema canonico allineato; controlli mirati su separatore, copertine, esponenti, contenuti e risorse. Preparare il commit sul ramo della PR #65 integrando il main corrente, verificare il caricamento e l'anteprima, poi effettuare il merge e verificare il deployment. Non richiedere di nuovo l'autorizzazione già ricevuta per queste modifiche circoscritte.

## Rilascio completato — 23 ottobre 2026

[PR #65](https://github.com/rickymusu-bit/fisica/pull/65) integrata al commit `910bcc2c23c174beb9b53e247c3e03a52c8107aa`, dopo il [controllo remoto 39967227556](https://github.com/rickymusu-bit/fisica/actions/runs/39967227556) riuscito. [Deployment Pages 39967950097](https://github.com/rickymusu-bit/fisica/actions/runs/39967950097) completato con successo. [Capitolo pubblicato](https://rickymusu-bit.github.io/fisica/prefissi_sistema_internazionale_it.html), HTML v2, quarto dell’area introduttiva, con separatore prima dei sottomultipli e copertina scelta dall’utente.

Pubblicate anche le correzioni richieste: Metodo scientifico v12 senza zoom sulla copertina e Potenze di dieci v6 con esponenti nella posizione corretta. Regole registrate nel master v69.9 e in AGENTS.md. Controlli locali e remoti: tema, crediti, build, 18 test, 200 combinazioni pagina/viewport/tema e 20 copertine senza errori JavaScript. Nel browser locale file:// è bloccato dalla policy: verificato il contenuto in memoria con rete bloccata, senza dichiarare accesso locale non eseguito.

Verifica HTTPS dopo il deployment: 18 pagine pubbliche HTTP 200, identiche byte per byte alla build; 11 indirizzi esclusi, storici o di anteprima HTTP 404. [Rapporto](verifica-pubblicazione-online.json). Il primo controllo durante il deployment vedeva ancora la versione precedente; il controllo successivo al completamento è interamente riuscito. Nessuna attività di pubblicazione pendente.

## Nuova copertina scelta — anteprima v3 del 23 ottobre 2026

L’utente richiede esplicitamente la sostituzione con Algae and bacteria in Scanning Electron Microscope, magnification 5000x.JPG, fornendo la miniatura Wikimedia e scrivendo «Procedi». Operazione circoscritta autorizzata: HTML v3 con nuova immagine 960 per 768 px, intera, barra di scala 5 µm e scritte fotografiche originali conservate, nessun comando di zoom. Fonte verificata su Wikimedia Commons, autore SecretDisc, licenza scelta CC BY-SA 3.0. Metadati, URL e hash in risorse/copertina-fonte.json; foto in risorse/copertina-sem.jpg. Copertina precedente conservata come originale storico, rimossa dai crediti correnti. Registro unico, pagina dei crediti e snapshot del capitolo aggiornati; altri documenti del registro invariati. Bozza testuale v5 e generatore allineati.

Contenuto didattico, formule, separatore dei prefissi e navigazione identici alla v2: confronto dopo rimozione delle sole copertine, crediti e versioni. Copia HTML di lavorazione identica alla nuova radice. Crediti --check, tema --check e build superati. Browser Chromium a cinque larghezze e nei due temi: nessun overflow o errore JavaScript, nuova immagine decodificata 960 per 768 px, cover senza zoom, indice, tabella scorrevole, zoom dello schema, download identico, crediti/OFL, lettura senza JavaScript e senza rete. Schermate della copertina mobile e desktop ispezionate. Rapporto verifiche-browser.json aggiornato.

Ramo corrente lavorazione/cifre-significative, PR #67: stessa richiesta comprende bozza del capitolo 5 e questa sostituzione. Sito pubblico non aggiornato: nuova anteprima da presentare e approvare secondo AGENTS.md prima del merge/deployment. L’autorizzazione alla pubblicazione della precedente v2 non viene estesa alla v3.

## Nuova anteprima approvata — 23 ottobre 2026

L’utente risponde «Approvo tutto» alla richiesta esplicita di approvare l’anteprima HTML v3 del quarto e il testo del quinto. Autorizzato il rilascio della nuova copertina del capitolo 4. Controllo remoto 39975086752 riuscito; PR #67 resa pronta e integrata al commit b25f0af4b90f91326c1c54319e5fd8d7ae8f1d1f. Pubblicazione e verifica HTTPS da registrare appena completate. Nessuna immagine di provenienza sconosciuta aggiunta al quarto.

Deployment Pages 39977718327 riuscito. Controllo HTTPS conclusivo: 18 pagine pubbliche HTTP 200 e identiche alla build locale v3, 11 indirizzi esclusi HTTP 404. Nuova copertina del quarto pubblicata, nessun rilascio pendente. Rapporto verifica-pubblicazione-online.json aggiornato.

## Navigazione per il rilascio del capitolo 5 — 23 ottobre 2026

HTML v4: navigazione successiva aggiornata a Le cifre significative, ora quinto capitolo pubblicato su autorizzazione dell’utente. Contenuto, copertina, separatore e risorse invariati. Copia di lavorazione allineata; corpo dell’articolo verificato identico. Intervento circoscritto incluso nella pubblicazione autorizzata della PR #68.

Pubblicazione completata nella PR #68 (b395589e1f5f06197723171ab4dfb3d33142114c), deployment 39992857516 riuscito. Collegamenti aggiornati verificati online, file identici alla build locale.
