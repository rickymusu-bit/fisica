# Introduzione alla fisica e alla misura — piano editoriale

Data del piano: 21/10/2026 (Europe/Rome). Stato aggiornato al 22/10/2026: primi due capitoli pubblicati; percorso in sviluppo. Le sezioni di progettazione conservano le decisioni iniziali, superate dagli avanzamenti finali dove specificato.
Fonte delle regole: MASTER_PROMPT.md v69.6, AGENTS.md, riferimenti/STILE_DISPENSE.md, riferimenti/esempio_irraggiamento.md.
Macrocategoria approvata dall'utente: **Introduzione alla fisica e alla misura**.
Approvati: 12 capitoli; proporzionalità inversa e quadratica nello stesso capitolo.
Non ancora approvati: revisione dello schema del metodo scientifico, bozze dei singoli capitoli, conversioni HTML, pubblicazione. Simulazione semplice del piano inclinato approvata dall'utente il 22/10/2026: 2–3 inclinazioni predefinite, pallina che parte da ferma, stessa lunghezza del percorso, cronometro e tabella risultati; senza attrito regolabile o grafici del moto.

## Indice editoriale concordato

1. Il metodo scientifico — metodo_scientifico_it.html.
2. Le grandezze fisiche e il Sistema internazionale — sezioni «Che cosa significa misurare», «Le sette grandezze e unità di base», «Le unità derivate» di sistema_internazionale_notazione_it.html.
3. Le potenze di dieci e la notazione scientifica — sezione «Dal molto grande al molto piccolo», incluse potenze e notazioni, dello stesso sorgente.
4. I prefissi del Sistema internazionale — sezione «I prefissi del SI» dello stesso sorgente.
5. Le cifre significative — sezione omonima, conteggio, arrotondamento e regole di calcolo dello stesso sorgente.
6. Gli strumenti di misura — «Analogico o digitale?» e «Che cosa chiedere a uno strumento», incluse portata, prontezza, risoluzione, sensibilità, precisione e accuratezza, di strumenti_errori_incertezza_it.html.
7. Errori e incertezza di misura — «Perché le misure cambiano o si spostano» e «Errore e incertezza: due domande diverse» dello stesso sorgente.
8. Le misure ripetute — «Da cinque letture a un risultato», con media e semidispersione; chiarire che questa non rappresenta automaticamente tutta l'incertezza, dello stesso sorgente.
9. Il piano cartesiano e i grafici — «Due grandezze, una coppia di coordinate» e l'interazione «Trascina P» di grafici_piano_cartesiano_it.html.
10. La proporzionalità diretta — «Dalle proporzioni alla retta» dello stesso sorgente.
11. Le relazioni lineari — «Intercetta e pendenza: rette diverse» dello stesso sorgente.
12. Le relazioni non lineari — «Proporzionalità inversa» e «Relazione quadratica» dello stesso sorgente.

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
