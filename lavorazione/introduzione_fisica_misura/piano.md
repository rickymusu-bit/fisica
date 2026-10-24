# Introduzione alla fisica e alla misura — piano editoriale

Data del piano: 21/10/2026 (Europe/Rome). Indice aggiornato al 24/10/2026: primi sette capitoli ammessi alla pubblicazione; capitoli 8 e 9 realizzati in anteprima nella PR #79. Le sezioni di avanzamento conservano la cronologia, superata dalle decisioni più recenti dove specificato.
Fonte delle regole: MASTER_PROMPT.md v69.6, AGENTS.md, riferimenti/STILE_DISPENSE.md, riferimenti/esempio_irraggiamento.md.
Macrocategoria approvata dall'utente: **Introduzione alla fisica e alla misura**.
Piano iniziale approvato: 12 capitoli, con proporzionalità inversa e quadratica insieme. Misure ripetute, media, semidispersione e incertezza sono riunite nel capitolo 7. Il 24/10/2026 l’utente richiede un capitolo sul piano cartesiano e uno su tutte le relazioni di proporzionalità: il percorso aggiornato comprende **9 capitoli**, con proporzionalità diretta, inversa e quadratica nel capitolo 9.
Non ancora approvati: revisione dello schema del metodo scientifico, bozze dei singoli capitoli, conversioni HTML, pubblicazione. Simulazione semplice del piano inclinato approvata dall'utente il 22/10/2026: 2–3 inclinazioni predefinite, pallina che parte da ferma, stessa lunghezza del percorso, cronometro e tabella risultati; senza attrito regolabile o grafici del moto.

## Indice editoriale concordato

1. Il metodo scientifico — metodo_scientifico_it.html.
2. Le grandezze fisiche e il Sistema internazionale — sezioni «Che cosa significa misurare», «Le sette grandezze e unità di base», «Le unità derivate» di sistema_internazionale_notazione_it.html.
3. Le potenze di dieci e la notazione scientifica — sezione «Dal molto grande al molto piccolo», incluse potenze e notazioni, dello stesso sorgente.
4. I prefissi del Sistema internazionale — sezione «I prefissi del SI» dello stesso sorgente.
5. Le cifre significative — sezione omonima, conteggio, arrotondamento e regole di calcolo dello stesso sorgente.
6. Gli strumenti di misura — «Analogico o digitale?» e «Che cosa chiedere a uno strumento», incluse portata, prontezza, risoluzione, sensibilità, precisione e accuratezza, di strumenti_errori_incertezza_it.html.
7. Errori e incertezza di misura — «Perché le misure cambiano o si spostano», «Da cinque letture a un risultato» ed «Errore e incertezza: due domande diverse» dello stesso sorgente. Percorso unico con misure ripetute, media, semidispersione e stima dell'incertezza; chiarire che la dispersione non rappresenta automaticamente tutta l'incertezza.
8. Il piano cartesiano — «Due grandezze, una coppia di coordinate» e interazione «Trascina P» di grafici_piano_cartesiano_it.html; assi, coordinate, quadranti, unità, scale e passaggio tabella–grafico.
9. Le relazioni di proporzionalità — proporzionalità diretta, inversa e quadratica, dalle sezioni «Dalle proporzioni alla retta», «Proporzionalità inversa» e «Relazione quadratica» di grafici_piano_cartesiano_it.html. Intercetta, rette affini e confronto delle pendenze esclusi su richiesta dell’utente; nessun capitolo 10 o 11 separato.

## Criteri trasversali

Ogni capitolo è autonomo e monografico; conservare gli esempi, le formule, le immagini e le attività corretti e pertinenti. Ridistribuire le domande finali dei quattro documenti secondo gli argomenti, senza perderle o duplicarle. Le ricapitolazioni di argomenti già trattati devono essere brevi e funzionali.
I quattro HTML originali restano esclusi in pubblicazione.json finché non vi sia esplicita autorizzazione di riammissione e anteprima approvata.
Il nome dell'area tematica nella UI sarà esattamente «Introduzione alla fisica e alla misura» al momento della futura pubblicazione, senza modificare ora il catalogo pubblico.
Usare il tema Stringhe comune, la barra universale, lo standard docs/visual-guidelines.md, la gestione centralizzata dei crediti; nessuna nuova immagine senza scelta concordata.

## Primo capitolo: Il metodo scientifico

Sorgente: metodo_scientifico_it.html, con i paragrafi «Dall'osservazione alla prova», «Perché servono le misure» e «Un'ipotesi deve poter essere smentita»; sei quesiti finali originali. Esempio coerente: pallina sul piano inclinato, stesso percorso e diverse pendenze; la tabella contiene tempi dichiarati illustrativi (non osservazioni sperimentali realmente effettuate).
Confini: osservazione, domanda scientifica, ipotesi controllabile, variabili tenute costanti, esperimento, confronto dei dati, falsificabilità e revisione dell'ipotesi. Le regole dettagliate di strumenti, unità, errori e incertezza sono rinviate ai capitoli 2 e 6–8.
Domanda iniziale: una pallina percorre la stessa distanza su una pista più inclinata: è possibile prevedere e verificare se cambia il tempo di discesa?
Visuali esistenti da valutare e riutilizzare se idonei: schema ciclico del metodo scientifico; ritratti storici di Galileo e Popper; tabella illustrativa dei tempi. Criticità: diritti delle immagini storiche e correttezza del diagramma; individuare una copertina pertinente che non sia ripetuta nel corpo. Proposta da sottoporre all'utente: fotografia reale di un piano inclinato con pallina per copertina, schema metodologico per la teoria, tabella già esistente per il confronto. Non cercare o generare visuali prima della scelta.
Fase corrente: proposta visuali e confini pronta; attesa di scelta/approvazione prima di scrivere lavorazione/metodo_scientifico/bozza.md o convertire HTML.
Checklist: A1–A5, B1.1–B2, B4–B6, C1–C3, D1–D2, AGENTS.md. Per realizzazione controllare lo stato sorgente già esistente e aggiornare quel file, preservandone la cronologia.

## Proposta di revisione dello schema metodologico (22/10/2026)

Conservare la logica ciclica dello schema originale, separando esplicitamente osservazione e domanda, ipotesi, previsione verificabile, esperimento controllato, raccolta e confronto dei dati, valutazione e revisione. Due uscite dopo il confronto: risultati coerenti con la previsione → ipotesi sostenuta provvisoriamente e ulteriori verifiche; risultati incoerenti → controllo di procedimento e misure, revisione dell'ipotesi e nuova prova. Evitare che una sola conferma conduca automaticamente a «teoria» o «principio». Questa è una proposta non ancora approvata, non modificare lo schema prima della scelta dell'utente.

## Avanzamento primo capitolo — 22/10/2026

L'utente ha approvato lo schema interattivo con sei fasi e spiegazioni contestuali sotto il diagramma, più una spiegazione discorsiva in capitolo, e la simulazione semplice. La bozza narrativa v1 è salvata in `lavorazione/metodo_scientifico/bozza.md` sul ramo di sviluppo. Le proposte precedenti segnate «non approvate» per lo schema sono superate da questa decisione. Fase corrente: revisione della bozza, nessun HTML o deploy.

## Secondo capitolo — pubblicato il 22 ottobre 2026

**Le grandezze fisiche e il Sistema internazionale**, file autonomo `grandezze_fisiche_sistema_internazionale_it.html`: testo, tre immagini e anteprima approvati. L’utente richiede esplicitamente merge e pubblicazione nella PR #59. Inserimento al secondo posto dopo Il metodo scientifico; seguono i capitoli di Termologia già pubblicati. Il vecchio sorgente unificato `sistema_internazionale_notazione_it.html` resta escluso e invariato. [Stato e verifiche](../grandezze_fisiche_sistema_internazionale/stato.md).

La PR #59 è stata integrata al commit `213ced3645d68affd3212603d2d8c2a9d4c6136f`; workflow Pages 39849357978 riuscito. [Capitolo pubblicato](https://rickymusu-bit.github.io/fisica/grandezze_fisiche_sistema_internazionale_it.html), al secondo posto dell’area dopo Il metodo scientifico. Catalogo, crediti e navigazione reciproca verificati online; i sorgenti storici esclusi restano non pubblicati.

## Terzo capitolo — progettazione avviata il 23 ottobre 2026

**Le potenze di dieci e la notazione scientifica**. Verificato il sorgente unificato v11, sezione `#scale`; definiti i confini rispetto ai capitoli 2, 4 e 5 e la ripartizione dei quesiti originali. Proposta: riutilizzare la foto della Terra come copertina, le tabelle delle scale e del confronto fra notazioni, le micrografie e i due video pertinenti; aggiungere una tabella numerica per gli esponenti positivi, zero e negativi. Provenienza e licenze non documentate restano da verificare.

[Stato e proposta visuali](../potenze_dieci_notazione_scientifica/stato.md), sul ramo `lavorazione/potenze-dieci-notazione-scientifica` derivato da main. Fase corrente: scelta delle visuali prima della bozza, secondo B1.1 del master. Nessuna bozza o realizzazione HTML approvata; nessuna modifica alla pubblicazione o ai sorgenti storici.

### Terzo capitolo — bozza v1 pronta

L’utente approva l’impostazione con «Procedi». Completata la [bozza v1](../potenze_dieci_notazione_scientifica/bozza.md), con otto domande finali, segnaposto dei materiali concordati e fonti dei dati nella sezione di servizio. Chiarito il criterio degli ordini di grandezza e corretti i valori di scala delle masse quando necessario; registrate le modifiche rispetto al sorgente. Le attribuzioni mancanti delle fotografie e i diritti delle miniature restano da verificare prima dell’integrazione.
Fase corrente: approvazione del testo; realizzazione HTML e pubblicazione non ancora avviate. [PR #63 in bozza](https://github.com/rickymusu-bit/fisica/pull/63).

### Terzo capitolo — bozza v2 corretta su richiesta

Rimossa la sezione finale sulla fotografia e le micrografie; conservato A Boy and His Atom nella sezione di confronto. Unica tabella degli ordini di grandezza dedicata alle lunghezze, senza cratere: aggiunti DNA disteso di una cellula umana (circa 2 m, ordine 10⁰ m) e riferimento globale delle fibre ottiche per telecomunicazioni (oltre 5 miliardi di km nella fonte, scala 10¹³ m). Etichetta e nota distinguono il conteggio delle fibre dal totale dei percorsi o di tutti i cavi anche in rame. Fonti, nota e ottavo quesito aggiornati. [Bozza v2](../potenze_dieci_notazione_scientifica/bozza.md) da approvare; HTML e pubblicazione non avviati.

### Terzo capitolo — testo approvato e anteprima realizzata

L’utente approva la bozza v2 con «Approvato, procedi». Realizzato HTML autonomo v1 dal modello Stringhe v22, con tre tabelle, due video esterni, undici formule e otto quesiti. Crediti e build verificati; browser a cinque larghezze in chiaro/scuro, note, indice, download e autonomia controllati. [HTML corrente](../potenze_dieci_notazione_scientifica/bozza.html), [stato e schermate](../potenze_dieci_notazione_scientifica/stato.md). Provenienza della copertina e diritti delle miniature ereditate ancora da risolvere prima del rilascio. PR #63 in bozza; manifest, catalogo, main e sito pubblico invariati. Attesa della revisione dell’anteprima corrente.

### Terzo capitolo — copertina documentata, HTML v2

Sostituita su richiesta la copertina con Map of Jupiter.jpg, scelta dall’utente e incorporata senza ritagli. Fonte NASA/JPL/Space Science Institute e pubblico dominio documentati; didascalia della mappa polare corretta. Testo didattico invariato, crediti/build e browser mobile/desktop verificati, schermate aggiornate. [Stato corrente](../potenze_dieci_notazione_scientifica/stato.md). Restano da verificare soltanto i diritti delle miniature video; PR #63 ancora in bozza.

### Terzo capitolo — lettori YouTube su richiesta

Su richiesta dell’utente, HTML v3 e bozza v4 sostituiscono le miniature con il componente comune del modello v23: lettore youtube-nocookie.com soltanto dopo il clic, nessun autoplay, collegamento esterno sempre disponibile e chiusura del lettore. Nessuna immagine estratta dai video rimane da attribuire. Regole in MASTER_PROMPT.md v69.7, C5; [audit di tutti i capitoli](../sito/video_youtube/stato.md). Anteprima corrente da approvare; catalogo e pubblicazione invariati.

## Pubblicazione approvata — 23 ottobre 2026

L’utente approva esplicitamente l’anteprima corrente con «Approvo. Fai la pr e pubblica». Autorizzati completamento e merge della PR #63 e deployment Pages; superata l’attesa di approvazione indicata nei resoconti precedenti. Nuovo capitolo HTML v4, contenuto didattico identico all’anteprima v3: aggiunto soltanto il rimando al capitolo successivo. Manifest v12 con 13 capitoli; inserimento al terzo posto dell’area introduttiva, catalogo e pagina dei crediti aggiornati. Navigazione reciproca con Sistema internazionale (v5) e Termodinamica (v13), con copie correnti riallineate e date editoriali conservate. Nessuna riammissione degli HTML storici o tradotti. Verificati contenuti identici al netto di versione/navigazione, navigazione dei 13 capitoli ed esclusioni. Tema, crediti, migrazione video --check, build e 17 test superati. Merge e verifica del deployment da completare.

## Rilascio completato — 23 ottobre 2026

[PR #63](https://github.com/rickymusu-bit/fisica/pull/63) pronta e integrata al commit `ffc805cd0b9b82edc40775ffadd69f402f6183d6`, dopo il controllo remoto riuscito [39919713921](https://github.com/rickymusu-bit/fisica/actions/runs/39919713921). [Deployment Pages 39920157184](https://github.com/rickymusu-bit/fisica/actions/runs/39920157184) concluso con successo. [Capitolo pubblicato](https://rickymusu-bit.github.io/fisica/potenze_dieci_notazione_scientifica_it.html), HTML v4, terzo dell’area introduttiva.

Verifica HTTPS successiva al deployment: 17 URL pubblici (13 capitoli e quattro pagine di servizio) HTTP 200 e identici byte per byte alla build locale; 12 URL esclusi, storici o riservati all’anteprima rispondono HTTP 404. Navigazione reciproca dei 13 capitoli corretta; capitolo nuovo e Conduzione hanno rispettivamente due e un riquadro video, senza iframe iniziali. [Rapporto](https://github.com/rickymusu-bit/fisica/blob/main/lavorazione/sito/video_youtube/verifica-pubblicazione-online.json). Non restano attività di pubblicazione pendenti per questo incarico. La riproduzione remota dei filmati resta dipendente dal servizio YouTube; le verifiche non dichiarano un playback remoto non eseguito.

## Quarto capitolo — progettazione avviata il 23 ottobre 2026

**I prefissi del Sistema internazionale**. Identificata la sezione `#prefissi` del sorgente unificato e verificata la continuità con il capitolo 3. Definiti contenuti, conversioni, caso del grammo, breve passaggio sulle unità elevate a potenza e ripartizione dei quesiti originali 5, 6 e 12.

Proposta: riusare in copertina la foto del metro già scelta nel capitolo 2, conservare la tabella dei 24 prefissi e affiancare prospetti numerici e uno schema statico delle conversioni. Proposta di non duplicare nel nuovo capitolo la vecchia scala illustrata yotta–yocto, conservata nel sorgente storico; scelta da concordare. Nessuna nuova immagine cercata o generata, nessuna simulazione prevista.

[Stato](../prefissi_sistema_internazionale/stato.md) e [proposta dei contenuti e delle visuali](../prefissi_sistema_internazionale/visuali.md), sul ramo `lavorazione/prefissi-sistema-internazionale` derivato da main. Fase corrente: scelta dell'impostazione visuale prima della bozza secondo B1.1. Nessuna bozza o realizzazione HTML approvata; nessuna modifica a catalogo, pubblicazione o sorgenti storici.

### Quarto capitolo — conversioni tra prefissi e tabella riutilizzata

L'utente richiede esplicitamente di aggiungere il procedimento per convertire tra prefissi e di riutilizzare la tabella esistente. [Proposta v2](../prefissi_sistema_internazionale/visuali.md) ampliata con fattori della tabella, passaggio per l'unità di riferimento, differenza degli esponenti e conversioni cm–mm e µm–mm in entrambi i versi, oltre a km–mm. Chiarito che lo schema proposto era una sequenza numerica con frecce e fattori: rimane opzionale, con alternativa di integrare i passaggi direttamente nel calcolo. La richiesta di chiarimento non è un'approvazione dello schema. PR #65 ancora in bozza; nessuna realizzazione HTML o pubblicazione avviata.

### Quarto capitolo — schema realizzato e bozza v1 pronta

L'utente autorizza lo schema con «Ok fai lo schema». Realizzato [SCH-01](../prefissi_sistema_internazionale/risorse/schema-conversioni.svg): km–m–mm e cm–mm–µm, fattori espliciti e frecce nei due versi. Completata la [bozza v1](../prefissi_sistema_internazionale/bozza.md) con tabella originale dei 24 prefissi, conversioni tra prefissi tramite unità di riferimento e differenza degli esponenti, caso del grammo, aree/volumi e otto domande. Controllati la tabella sulla fonte BIPM, equivalenze e inverse; schema ispezionato desktop/mobile con ingrandimento da prevedere nell'HTML. Testo da approvare; PR #65 ancora in bozza. Nessuna realizzazione HTML, merge o pubblicazione avviati.

### Quarto capitolo — bozza v2 e schema con potenze di 10

Su richiesta esplicita dell'utente, usare le potenze di 10 in tutto il capitolo per mantenere la continuità con la notazione esponenziale. Aggiornati [bozza v2](../prefissi_sistema_internazionale/bozza.md), tabelle numeriche, fattori diretti e inversi, esempi, quesiti e [schema](../prefissi_sistema_internazionale/risorse/schema-conversioni.svg), compresa la descrizione accessibile. Conservata la tabella dei 24 prefissi. Esplicitate le operazioni sugli esponenti nelle conversioni e nelle unità al quadrato/cubo. Equivalenze e resa grafica verificate; testo da approvare, PR #65 in bozza. Nessun HTML o aggiornamento del sito pubblico.

### Quarto capitolo — bozza v3, formula esplicita ed esempi con unità derivate

L'utente precisa: introduzione senza potenze nel testo, tabella introduttiva con valori decimali e potenze affiancati, poi notazione esponenziale dove utile. [Bozza v3](../prefissi_sistema_internazionale/bozza.md) aggiornata con formula x_arrivo = x_partenza · 10^(p − q), simboli definiti, procedura in quattro passi e fattore 10^[n(p − q)] per unità elevate a potenza. Aggiunti esempi svolti MPa–kPa, cm²–m², mm³–cm³ e g/cm³–kg/m³, con impostazione, calcoli e interpretazione. Dieci quesiti finali. Copertina del metro ritirata su richiesta: attesa nuova immagine dall'utente. Tabella dei 24 prefissi e schema conservati; equivalenze e inverse verificate. Testo da approvare, PR #65 in bozza; nessun HTML o rilascio.

### Quarto capitolo — HTML v1 realizzato, copertina scelta

Con «Ok genera» l'utente autorizza la realizzazione dal testo v3; sceglie poi la foto Wikimedia della colonia al microscopio, Korinna / CC BY 4.0, incorporata intera. [HTML v1](../prefissi_sistema_internazionale/bozza.html) pronto per revisione: tema Stringhe v23, 18 formule native, procedura, tabella originale dei prefissi, quattro esempi con unità derivate, schema ingrandibile e dieci quesiti. [Bozza v4](../prefissi_sistema_internazionale/bozza.md) aggiornata per la sola copertina e la provenienza. Crediti, build locale e browser a cinque larghezze in entrambi i temi verificati, con download e lettura senza rete; [stato, rapporti e schermate](../prefissi_sistema_internazionale/stato.md). PR #65 in bozza, anteprima corrente da approvare. Nessun merge, modifica del manifest o deployment.

### Quarto capitolo — pubblicazione autorizzata, HTML v2

L'utente approva il capitolo, richiede il separatore prima dei sottomultipli e autorizza caricamento e pubblicazione. Separatore applicato e verificato; manifest v13 con 14 capitoli, inserimento al quarto posto, catalogo/crediti e navigazione adiacente aggiornati. Incluse le correzioni richieste a copertina del Metodo scientifico (nessuno zoom) ed esponenti di Potenze di dieci; regola nel master v69.9 e componente canonico. Crediti, build, 18 test e verifiche mirate da consolidare nel rapporto di pubblicazione. PR #65 da integrare dopo i controlli; deployment da verificare.

## Quarto capitolo — rilascio completato — 23 ottobre 2026

[PR #65](https://github.com/rickymusu-bit/fisica/pull/65) integrata al commit `910bcc2c23c174beb9b53e247c3e03a52c8107aa`, dopo il [controllo remoto 39967227556](https://github.com/rickymusu-bit/fisica/actions/runs/39967227556) riuscito. [Deployment Pages 39967950097](https://github.com/rickymusu-bit/fisica/actions/runs/39967950097) completato con successo. [Capitolo pubblicato](https://rickymusu-bit.github.io/fisica/prefissi_sistema_internazionale_it.html), HTML v2, quarto dell’area introduttiva, con separatore prima dei sottomultipli e copertina scelta dall’utente.

Pubblicate anche le correzioni richieste: Metodo scientifico v12 senza zoom sulla copertina e Potenze di dieci v6 con esponenti nella posizione corretta. Regole registrate nel master v69.9 e in AGENTS.md. Controlli locali e remoti: tema, crediti, build, 18 test, 200 combinazioni pagina/viewport/tema e 20 copertine senza errori JavaScript. Nel browser locale file:// è bloccato dalla policy: verificato il contenuto in memoria con rete bloccata, senza dichiarare accesso locale non eseguito.

Verifica HTTPS dopo il deployment: 18 pagine pubbliche HTTP 200, identiche byte per byte alla build; 11 indirizzi esclusi, storici o di anteprima HTTP 404. [Rapporto](../prefissi_sistema_internazionale/verifica-pubblicazione-online.json). Il primo controllo durante il deployment vedeva ancora la versione precedente; il controllo successivo al completamento è interamente riuscito. Nessuna attività di pubblicazione pendente.

## Quinto capitolo — progettazione avviata il 23 ottobre 2026

L'utente avvia «Le cifre significative». Identificata la sezione `#cifre-significative` del sorgente unificato italiano v12 e il materiale riutilizzabile: confronto 12,4/12,40 cm, tre tabelle, schema della base rettangolare ed esempio svolto con cinque calcoli. [Proposta di contenuti e visuali](../cifre_significative/visuali.md) e [stato](../cifre_significative/stato.md) sul ramo `lavorazione/cifre-significative`, derivato dal main aggiornato. Nuova copertina proposta: bilancia digitale, da scegliere/fornire; diritti dell'immagine della cassa da verificare. Nessuna simulazione proposta. Fase: accordo sulle visuali prima della bozza, secondo B1.1; nessuna realizzazione HTML o pubblicazione autorizzata. Capitoli pubblicati e manifest invariati.

### Capitoli 4 e 5 — nuove copertine e bozza del quinto

L’utente sceglie per il quarto Algae and bacteria in Scanning Electron Microscope, magnification 5000x.JPG (SecretDisc, CC BY-SA 3.0), e per il quinto Egyptian measuring tool.jpg (Uriah Welcome, CC BY 2.0), con «Procedi». Fonti originali e licenze verificate; miniature scelte conservate intere, senza zoom. Capitolo 4 HTML v3 e bozza v5: sostituzione circoscritta di copertina/crediti, contenuto e separatore invariati, browser a cinque larghezze e nei due temi superato. Nuova anteprima da approvare prima di aggiornare il sito. [Bozza v1 del capitolo 5](../cifre_significative/bozza.md) completa, con tabelle riutilizzate, formule/procedure esplicite, esempio e dieci domande; testo da approvare. Provenienza dell’immagine della cassa non documentata nel registro: segnaposto conservato, verifica da risolvere prima dell’integrazione. [Stati e lavorazione](../cifre_significative/stato.md) nella PR #67; manifest e catalogo invariati.

### Quinto capitolo — HTML v1 realizzato

Testo approvato con «Approvo tutto»; cassa generata su richiesta e successivo «Ok procedi» per schema quotato e realizzazione. [HTML corrente](../cifre_significative/bozza.html) autonomo dal modello Stringhe v23, copertina egizia senza zoom, 12 formule native, tre tabelle, due procedure, esempio con schema generato e dieci domande. Crediti, tema, build e browser a cinque larghezze/entrambi i temi superati; download, note, zoom, offline e senza JavaScript verificati. Il PNG storico privo di fonte non è usato; nuova provenienza documentata. [Stato e rapporti](../cifre_significative/stato.md). Capitolo non ancora ammesso nel manifest, catalogo pubblico invariato; anteprima corrente da approvare prima del rilascio.

### Quinto capitolo — revisione dell’anteprima, HTML v2

Su richiesta: prima figura senza zoom; C.S. introdotta nella definizione e usata nelle occorrenze successive; punte delle quote della cassa rivolte all’esterno fino ai delimitatori; avviso ripetuto eliminato da immagine e didascalia senza trasferirlo in nota. Bozza v3 e generatore allineati, formule numeriche conservate. Crediti/tema e browser a cinque larghezze nei due temi verificati; [stato e anteprima](../cifre_significative/stato.md) nella PR #68 in bozza. Nessun rilascio autorizzato dell’anteprima corrente.

### Quinto capitolo — zoom selettivo, HTML v3

Tolto anche lo zoom dalla cassa, su richiesta. Regola salvata nel master v69.10 e AGENTS.md: zoom soltanto per grafici e schemi con numerose scritte piccole, mai su fotografie e copertine. Nessun ingrandimento nelle due figure semplici del capitolo 5; file autonomo circa 4,68 MB. Crediti/tema e browser verificati; anteprima v3 nella PR #68 in bozza, sito pubblico invariato.

### Quinto capitolo — pubblicazione autorizzata

«Perfetto pubblica» approva l’anteprima corrente e autorizza il rilascio della PR #68. HTML v4 con solo il rimando successivo aggiunto; corpo invariato rispetto alla v3 approvata. Manifest v14 con 15 capitoli e quinto posto nell’area introduttiva; catalogo, crediti pubblici e navigazione reciproca Prefissi v4 → Cifre significative v4 → Termodinamica v15 aggiornati. Inclusa la regola dello zoom salvata in master v69.10 e AGENTS.md. Crediti, tema, build e 18 test superati; browser locale riuscito su 210 combinazioni pagina/viewport/tema e 20 copertine; CI remoto e verifica del deployment da completare. Nessuna ulteriore conferma da richiedere per questa pubblicazione autorizzata.

## Quinto capitolo — rilascio completato — 23 ottobre 2026

[PR #68](https://github.com/rickymusu-bit/fisica/pull/68) integrata al commit b395589e1f5f06197723171ab4dfb3d33142114c. [Deployment Pages 39992857516](https://github.com/rickymusu-bit/fisica/actions/runs/39992857516) riuscito. [Le cifre significative](https://rickymusu-bit.github.io/fisica/cifre_significative_it.html), HTML v4, è il quinto capitolo del percorso introduttivo. Catalogo, crediti e navigazione aggiornati; master v69.10 e AGENTS.md con regola dello zoom integrati in main.

Verifica HTTPS dopo il deployment: 19 pagine pubbliche HTTP 200 e identiche byte per byte alla build locale; 12 indirizzi esclusi, storici o di anteprima HTTP 404. [Rapporto HTTPS](../cifre_significative/verifica-pubblicazione-online.json) e [script](../cifre_significative/verifica_pubblicazione.py). Le prove locali complete sono riuscite: 18 test, 210 combinazioni pagina/viewport/tema e 20 copertine, oltre ai controlli specifici del capitolo.

Il workflow remoto 39991173540 ha superato tema, crediti, build e test; l’installazione di Chromium ha ritardato il controllo. Il merge regolare è stato accettato da GitHub sulla base della suite locale completa già riuscita. Al controllo successivo alla pubblicazione il CI remoto sta eseguendo le prove browser; il suo esito non è ancora registrato come riuscito. Il deployment e la verifica delle pagine pubbliche sono completati.

## Capitoli 6 e 7 — progettazione avviata il 23 ottobre 2026

Richiesta corrente: «Facciamo i capitoli 6 e 7». Verificati sorgente `strumenti_errori_incertezza_it.html` v7 e stato storico; master v69.11. Proposte per [Gli strumenti di misura](../strumenti_misura/visuali.md) e [Errori e incertezza di misura](../errori_incertezza_misura/visuali.md), con stati separati. Quesiti originali: 1–4 al 6, 5 e 7 al 7, 6 riservato all'8. Media, semidispersione, tabella delle cinque letture e linea dei numeri restano nell'8.

Proposto riuso delle immagini esistenti: calibro in copertina del 6, sismografo in copertina del 7, cronometro nello schema dell'esempio del 7, bersagli soltanto nel suo corpo. Nuovi prospetti e schema da concordare prima della bozza; licenze storiche non documentate da verificare prima dell'integrazione. Nessuna ricerca o generazione avviata, nessuna simulazione proposta.

Ramo `lavorazione/strumenti-errori-incertezza`, da main d681439986db6c824fb1c724fa8cf7023e5a38de. Fase corrente: scelta delle visuali secondo B1.1; nessuna bozza, realizzazione HTML o pubblicazione ancora approvata. Sorgenti storici, catalogo e manifest invariati.

### Capitoli 6 e 7 — visuali concordate, bozze v1 pronte

L'utente approva l'impostazione con «Ok». Completate [Gli strumenti di misura, bozza v1](../strumenti_misura/bozza.md) ed [Errori e incertezza di misura, bozza v1](../errori_incertezza_misura/bozza.md), ciascuna con otto quesiti, formule spiegate, segnaposto delle visuali e una nota breve. Conservati integralmente i sette quesiti originali nella ripartizione concordata, con il quesito sulle misure ripetute riservato all'8.

Nel 6 esplicitata la formula della sensibilità e aggiunte serie illustrative per precisione/accuratezza. Nel 7 conservato il confronto 2,40 s / 2,50 s e chiarito che U = 0,09 s è assegnata all'esempio, senza calcoli di media o semidispersione. Incertezza distinta dall'errore effettivo; nessuna garanzia assoluta attribuita all'intervallo ±U.

Fase corrente: approvazione dei due testi nella PR #72, poi stima e via esplicito alla realizzazione. Licenze dei materiali storici da verificare prima dell'integrazione. Nessun HTML o aggiornamento pubblico; sorgenti storici e manifest invariati.

### Capitoli 6 e 7 — copertine scelte, bozze v2

L'utente sceglie esplicitamente Ytterbium Lattice Double Clock with Photons at NIST.jpg per il 6 e TV noise.jpg per il 7. Superate le proposte del calibro e del sismografo come copertine. Aggiornate bozze v2, didascalie e schede di provenienza; immagini intere senza zoom o ripetizioni nel corpo. Pagine Commons consultate: N. Phillips/NIST, pubblico dominio federale; Mysid, pubblico dominio per dichiarazione dell'autore. Restano da verificare i diritti delle immagini storiche del corpo. Testi da approvare nella PR #72; nessuna realizzazione HTML o pubblicazione avviata.

### Capitoli 6 e 7 — due versioni della simulazione

L'utente richiede una simulazione nel capitolo 6 per sperimentare le proprietà dello strumento e una nel 7 con proprietà fisse per studiare errore e incertezza. Predisposte le specifiche [SIM-06](../strumenti_misura/simulazione.md) e [SIM-07](../errori_incertezza_misura/simulazione.md); bozze v3 con attività, segnaposto e un quesito finale aggiornato, mantenendo i quesiti originali pertinenti. Bilancia virtuale condivisa: regolazioni nel 6; misure, U assegnata e riferimento rivelato successivamente nel 7. Media e semidispersione restano all'8. Parametri numerici proposti, carico basso, stima preliminare 90–150 min per entrambe. Nessun codice o HTML avviato: testo aggiornato da revisionare prima del via. L'utente intende fornire immagini sostitutive con licenza; copertine scelte confermate.

### Capitoli 6 e 7 — pesetti, grafico e contenuti dell'incertezza riuniti

L'utente definisce SIM-06 come bilancia con pesetti di masse differenti e slider sotto lo strumento; SIM-07 come bilancia a proprietà fisse, serie ripetute di una massa nota per stimare l'errore e di una ignota per stimare l'incertezza, con grafico sotto la bilancia. Aggiunge «metti media e semi dispersione nel cap 7» e chiarisce «Non ha senso separare incertezza, media e dispersione».

Decisione applicata: eliminato il capitolo separato sulle misure ripetute; il 7 riunisce teoria, tabella/grafico originali, media, semidispersione, incertezza ed errore. Indice aggiornato a undici capitoli; Piano cartesiano → 8, Proporzionalità diretta → 9, Relazioni lineari → 10, Non lineari → 11. I precedenti rinvii all'8 nei resoconti storici sono superati. Nessun URL pubblicato, catalogo o manifest modificato.

Bozze v4 e specifiche v2: massa nota con riferimento e scarto della media; massa ignota con media, semidispersione e stima scolastica U_did = max(d,q), non un valore assegnato. Il grafico distingue min–max, media, errore e fascia ±U; non rivela la massa ignota. Superato il precedente scenario con U = 3 g assegnata. Regola dichiarata didattica e non universale; zero regolato nel modello, controllo dei possibili sistematici e serie asimmetriche previsti.

Quesiti storici tutti conservati: 1–4 nel 6, 5–7 nel 7; otto quesiti nel 6, nove nel 7. Copertine scelte invariate. Servono immagini pertinenti con licenza per bilancia, pesetti e campioni; nessuna ricerca o generazione avviata. Stima preliminare aggiornata 2–3 ore per entrambe le simulazioni, da consolidare dopo la revisione dei testi. Nessuna programmazione o realizzazione HTML, merge o pubblicazione ancora avviata.

### Capitoli 6 e 7 — avvio autorizzato, HTML e simulazioni realizzati

«Ok vai» approva le bozze v4 e autorizza la realizzazione dopo la stima preliminare. HTML autonomi v1 dal modello Stringhe v24, con copertine scelte incorporate, formule native e due versioni del modello condiviso della bilancia. Il 6 esplora le proprietà con pesetti e slider; il 7 raccoglie due serie e visualizza media, semidispersione, errore e fascia U con ingrandimento canonico. Codice e anteprime salvati sul ramo della PR #72.

Restano da integrare le immagini sostitutive con licenza, che l’utente intende fornire: bilancia e pesetti/campione per le simulazioni e figure del corpo. Gli spazi sono dichiarati nelle anteprime di lavorazione; nessuna immagine non autorizzata aggiunta. Verifiche numeriche/browser, crediti/tema e build nei rapporti dei capitoli. Nessun aggiornamento al manifest, al catalogo o agli articoli pubblicati, nessun merge o deployment. Prossimo passaggio: completamento dei materiali e consegna dell’anteprima completa per revisione.

### Capitolo 6 — bilancia analogica e schema originale, 24 ottobre 2026

Integrata la fotografia Kitchen scale 20101110.jpg scelta dall’utente, Batholith / pubblico dominio PD-self, intera e con didascalia corretta a 2 kg e divisioni 10 g. Per il riferimento Vecteezy Pro eseguita la richiesta condizionale di ricreazione: nuovo schema originale del parallasse con elemento dell’occhio generato e geometria/scritte SVG verificate, senza incorporare il materiale commerciale. Bozza v5, HTML v2, crediti e verifiche mirate aggiornati nella PR #72. Capitolo 7 v1 e simulazioni invariati; altre immagini ancora in attesa. Nessuna modifica al sito pubblico.

### Capitolo 6 — HTML v3, essenzialità delle figure

Su richiesta dell’utente rimossi testi visibili e didascalie che ripetono informazioni già evidenti dall’immagine o dal contesto. Regola consolidata nel master v69.12 e nel riferimento di stile v7. Geometria e simulazioni invariate; altre immagini ancora in attesa.

### Capitolo 6 — HTML v4, matita nel parallasse

Su richiesta, la sagoma è sostituita con una matita riconoscibile e sono ripristinate le tre indicazioni di vista. Posizione, scala e linee di vista conservate; nessuna nuova didascalia. Originale generato preservato, crediti e verifiche mirate aggiornati. Capitolo 7 e simulazioni invariati.

### Bilancia digitale e pesetti generati

Su richiesta dell’utente generate e integrate le immagini della bilancia digitale e dei pesetti nelle due simulazioni. Letture sulla finestra dello strumento e carichi visibili sul piatto; campione ignoto senza etichetta di massa. Immagini riutilizzate nelle figure della stessa bilancia nei due testi. Originali preservati, incorporamento deduplicato tramite definizioni SVG e crediti aggiornati. Restano le quattro figure teoriche di voltmetro, termometro, cronometro e bersagli. Nessuna pubblicazione.

## Capitoli 6 e 7: immagini complete — 24 ottobre 2026

Integrate le ultime immagini scelte dall’utente: manometro in sostituzione del voltmetro, termometro a colonna e cronometro; ricreati su richiesta i quattro bersagli con etichette italiane. Aggiornati gli esempi coerentemente con scale e strumenti fotografati. HTML correnti: strumenti_misura_it.html v6; errori_incertezza_misura_it.html v3. Nessuna immagine pendente. PR #72 in bozza; anteprima da revisionare prima della pubblicazione.

Revisione richiesta il 24 ottobre 2026: capitolo 6 v7 con nuova foto della bilancia digitale nella teoria, sensibilità semplificata e didascalie ripristinate. Etichette di massa sui pesetti; capitolo 7 v4 con didascalie e riferimento etichettato, massa ignota nascosta.

## Ultima revisione del capitolo 7

Pubblicazione fermata dall’utente prima di qualsiasi push/merge/deployment. Attività di incertezza e misura dell’errore separate in due sezioni autonome con bilance, registri, calcoli e grafici propri. Un solo capitolo 7, senza nuove suddivisioni del piano. Anteprima corrente da revisionare prima del rilascio.

## Pubblicazione dei capitoli 6 e 7 autorizzata

Dopo la separazione delle attività del 7, l’utente approva nuovamente con «Okay, pubblica». Capitoli aggiunti al manifest, catalogo aggiornato a sette capitoli dell’area e navigazione collegata. Rilascio in corso nella PR #72.

## Capitoli 8 e 9 — accorpamento richiesto il 24 ottobre 2026

Richiesta: «Allora, io farei il piano cartesiano in un capitolo e tutte le relazioni di proporzionalità in un altro». Decisione applicata nell’indice corrente: capitolo 8 «Il piano cartesiano»; capitolo 9 «Le relazioni tra grandezze». Il titolo del 9 comprende anche il confronto con y = m·x + q: per q diverso da zero questa non è una proporzionalità diretta. La proporzionalità quadratica si esprime y = k·x²; non ogni relazione quadratica è una proporzionalità quadratica.

Il precedente indice a undici capitoli è superato; i resoconti storici ne conservano la cronologia. Quesiti originali del sorgente dei grafici: 1–2 al capitolo 8, 3–7 al capitolo 9. Stati nella PR #79; il percorso storico lavorazione/proporzionalita_diretta/stato.md conserva ora lo stato dell’intero capitolo 9, senza creare un secondo stato. La scelta dell’accorpamento è approvata dalla richiesta; visuali e bozze restano da concordare. Nessuna modifica a main, manifest o sito pubblico.

## Capitoli 8 e 9 — bozze e perimetro definitivo, 24 ottobre 2026

«Va bene, procediamo» autorizza la stesura delle bozze sulla struttura concordata. Preparati [Il piano cartesiano, bozza v1](../piano_cartesiano_grafici/bozza.md), con otto domande, e [Le relazioni di proporzionalità, bozza v2](../proporzionalita_diretta/bozza.md), con nove domande. La successiva richiesta «Lascia fuori la parte sull'intercetta» supera la proposta precedente: eliminati dal 9 sezione affine, quota fissa della consegna, formula della pendenza, confronto delle tre rette e domande associate. Titolo del 9 aggiornato per rispecchiare il perimetro.

Quesiti del sorgente dei grafici: 1–2 nel capitolo 8 (il primo adattato al grafico dei quaderni); 3, 6 e 7 nel capitolo 9; 4–5 esclusi dai nuovi capitoli su richiesta, conservati nel sorgente storico. Restano segnaposto per le immagini da scegliere. Testi da revisionare; nessun HTML o deployment avviato.

### Capitolo 9 — proporzionalità inversa attraverso il viaggio

Su richiesta «fai col viaggio», [bozza v3](../proporzionalita_diretta/bozza.md) sostituisce i rettangoli ad area costante con velocità e tempo per un viaggio ideale in treno di 120 km, senza fermate e a velocità costante. Aggiornati tabella, formule, specifica del grafico e domande 4–5; immagine del treno da scegliere. Diretta, quadratica e capitolo 8 invariati. Testo da revisionare, nessuna realizzazione HTML o pubblicazione.


## Capitoli 8 e 9 — HTML e materiali completati, 24 ottobre 2026

La richiesta di finire la PR #79 e i quattro URL forniti autorizzano la realizzazione delle bozze già approvate. Pronti gli HTML autonomi v1 [Il piano cartesiano](../../piano_cartesiano_grafici_it.html) e [Le relazioni di proporzionalità](../../relazioni_proporzionalita_it.html). Esempio dei libri a 2 €/libro nei due capitoli per continuità; viaggio ideale di 120 km per l’inversa; nessuna intercetta. Copertine Playfair e struttura iperbolica, biblioteca per i libri e monorotaia per il viaggio, con licenze verificate e crediti incorporati. Interazioni, scale, grafici, formule e domande realizzati; prove desktop/mobile, temi, fallback, crediti e build superati. Dettagli e schermate negli stati dei capitoli.

L’anteprima corrente resta da approvare prima di integrare main e pubblicare. PR #79 in bozza, manifest e catalogo ufficiali invariati; nessun merge o deployment.


## Revisione delle anteprime 8–9 su richiesta dell’utente

La nuova richiesta supera il riuso dei libri e della biblioteca nell’8: esempio distinto del serbatoio, dipendenza funzionale e ruolo delle variabili approfonditi, più lettura di coordinate e scale. Nel 9 i libri costano inizialmente 15 €/libro; schemi originali di libri e treno sostituiscono le foto superflue. Le curve passano per i punti dei modelli costruiti; la variazione di k confronta prezzi, distanze e proporzionalità quadratiche a scale fisse, senza alterare la formula dell’area del quadrato. HTML v2, tutte le figure con didascalie, nessuno zoom interattivo. Nuova regola permanente in master v69.16 e AGENTS.md: non riciclare immagini o esempi tra capitoli. Verifiche aggiornate superate, nuova anteprima da approvare; nessuna pubblicazione autorizzata.
