# Stato — Le potenze di dieci e la notazione scientifica

Ultimo aggiornamento: 23 ottobre 2026 (Europe/Rome).
Fase corrente: HTML v3 con copertina di Giove e lettori YouTube su richiesta; revisione comune in corso. Le sezioni di proposta iniziale sotto riportate conservano la progettazione; l’avanzamento finale registra l’approvazione ricevuta.
Ramo dedicato da main: `lavorazione/potenze-dieci-notazione-scientifica`.
Piano di riferimento: [capitolo 3 del percorso](../introduzione_fisica_misura/piano.md).
Area tematica: **Introduzione alla fisica e alla misura**.

## Incarico e approvazioni effettive

Richiesta corrente: «Lavora sul capitolo 3 del piano di lavorazione sul mio repo di fisica lavorazione/introduzione_fisica_misura/piano.md».
Argomento e posizione sono già definiti nel piano dei dodici capitoli. Il tema Stringhe comune è già approvato; non occorre sceglierlo nuovamente.
La richiesta avvia il lavoro editoriale. Non risultano approvate per questo capitolo le visuali definitive, la bozza, la realizzazione HTML o la pubblicazione. Le autorizzazioni dei primi due capitoli non si estendono al terzo.

## Identità del sorgente e confini

Sorgente verificato: [sistema_internazionale_notazione_it.html](../../sistema_internazionale_notazione_it.html), versione interna v11, blob `ede0bed4b28522b2431e4201b39e8f9f10593f88`.
Lo stato storico riporta anche versioni precedenti: per questa progettazione fa fede il file corrente verificato.
La sezione `#scale`, «Dal molto grande al molto piccolo», contiene il materiale del nuovo capitolo. Il sorgente storico resta invariato ed escluso dalla pubblicazione.

Corrispondenza dei contenuti:
- «Che cosa significa misurare», grandezze di base e unità derivate: capitolo 2, già pubblicato; richiamo solo se necessario.
- `#scale`: capitolo 3. Conservare il confronto fra scale, le potenze positive, nulle e negative, il prodotto di potenze e la distinzione fra scritture esponenziale, scientifica e ingegneristica.
- Prefissi e scala dei multipli/sottomultipli: capitolo 4; evitare di anticiparne la tabella.
- Cifre significative, arrotondamenti ed esempio della base rettangolare: capitolo 5.

Progressione proposta: confronto fra dimensioni molto diverse → significato di 10ⁿ → esponente zero e negativo → scritture equivalenti e normalizzazione → confronto fra numeri e semplici operazioni sulle potenze → breve distinzione dalla notazione ingegneristica, senza sviluppare i prefissi.
Chiarire che un esponente negativo indica un fattore positivo minore di uno: non rende negativo il numero. La forma scientifica di un numero non nullo è a · 10ⁿ, con 1 ≤ |a| < 10 e n intero.
Non identificare automaticamente l’esponente della forma scientifica con l’ordine di grandezza: dichiarare e usare coerentemente il criterio di stima adottato. Confrontare inizialmente fattori e scale usando i valori espliciti.
Nessuna applicazione separata, esercizio svolto aggiuntivo o simulazione prevista in questa fase.

## Domanda iniziale proposta

Il diametro della Terra e quello di un atomo richiedono numeri molto diversi: come scriverli e confrontarli senza perdersi tra gli zeri?
L’apertura riprende il confronto già presente nel sorgente. La foto astronomica introduce la scala maggiore; la dimensione atomica sarà presentata come dato del modello, senza attribuirla a una fotografia priva di scala.

## Proposta visuali da concordare

| ID | Materiale e posizione | Funzione e trattamento proposto | Stato |
| --- | --- | --- | --- |
| COP-01 | Foto della Terra oltre l’orizzonte lunare già incorporata in `#scale`, sotto il titolo | Riutilizzarla come copertina, senza ripeterla nel corpo. Verificare la provenienza dell’esatto file e la licenza prima dell’integrazione. | Riuso proposto; diritti non ancora verificati. |
| TAB-01 | Tabelle originali delle lunghezze e delle masse, presso il confronto fra scale | Conservare dati pertinenti e due tabelle distinte; verificare fonti e significato delle stime prima della bozza. Per le masse proporre kg, esplicitando la conversione dai g originali, senza cambiare i valori fisici. | Riuso e conversione proposti. |
| TAB-02 | Tabella numerica delle potenze, presso la spiegazione degli esponenti | Affiancare 1000, 100, 10, 1, 0,1, 0,01, 0,001 alle rispettive potenze da 10³ a 10⁻³; rendere leggibile il passaggio per fattori dieci e l’esponente zero. Solo numeri e relazioni matematiche, nessuna immagine di oggetti da generare. | Nuova tabella proposta, non realizzata. |
| TAB-03 | Confronto fra notazioni già presente in `#scale`, dopo la normalizzazione | Conservare 0,000047 m, 470 · 10⁻⁷ m, 4,7 · 10⁻⁵ m e 47 · 10⁻⁶ m. Rimandare l’equivalenza in µm al capitolo 4; spiegare che la forma ingegneristica usa esponenti multipli di tre. | Riuso con adattamento proposto. |
| VID-01 | [Powers of Ten](https://www.youtube.com/watch?v=0fKBhvDjuy0), vicino al confronto fra scale | Conservare il collegamento esatto e la miniatura esistente, previa verifica dei diritti; apertura su YouTube, nessun lettore incorporato. Osservare il fattore dieci fra inquadrature successive. | Video originale pertinente; riuso proposto. |
| IMG-01 | Micrografie A/B già incorporate, presso la discussione delle piccole dimensioni | Conservarne la funzione: senza scala non si ricava una dimensione dall’immagine. Soggetto e licenza non sono documentati nel sorgente: non inventarli né presentare le immagini come fotografie di atomi. | Materiale originale da verificare; non sostituito. |
| VID-02 | [A Boy and His Atom](https://www.youtube.com/watch?v=oSCX78-8-q0), presso la scala microscopica | Conservare il link originale e l’esatta descrizione: molecole di monossido di carbonio spostate con un microscopio a effetto tunnel. Valutare nella bozza la brevità del raccordo per evitare una digressione. | Riuso proposto; miniatura e diritti da verificare. |

La proposta privilegia i materiali già presenti e non richiede nuove fotografie. Se un originale non è riutilizzabile per provenienza o leggibilità, presentare il problema e chiedere una scelta specifica; non cercare o generare sostituti autonomamente. Le tabelle devono conservare disposizione e relazioni sui diversi dispositivi.

## Domande originali e ripartizione

Il sorgente contiene tredici quesiti. Quesiti 1–3 al capitolo 2; quesiti 4 e 7 al capitolo 3; quesito 6 al capitolo 4; quesiti 8–13 al capitolo 5.
Il quesito 5 attraversa i confini: la conversione di 0,000047 m in forma scientifica e ingegneristica compete al capitolo 3; la scelta del prefisso compete al capitolo 4. Separare le due richieste mantenendo questa provenienza, senza duplicare l’intero quesito.

Per il capitolo 3 conservare quindi:
- confronto fra diametro terrestre e atomico, precisando il significato degli ordini di grandezza;
- riscrittura di 0,000047 m nelle due notazioni;
- lettura critica delle micrografie prive di scala.

Nella bozza completare una breve serie mista di domande, con vero/falso motivati sugli esponenti negativi, riconoscimento di una forma scientifica normalizzata e confronto fra valori espressi nella stessa unità. Numero e formulazione definitivi da fissare nella bozza, senza soluzioni.

## Regole e controlli pertinenti

Letti MASTER_PROMPT.md v69.6, AGENTS.md, riferimenti/STILE_DISPENSE.md v6, riferimenti/esempio_irraggiamento.md v2 e docs/visual-guidelines.md v1.0.0.
Checklist: A1–A5 (monograficità, narrazione, formule e quesiti); A6 (tema autonomo comune, da leggere prima dell’impaginazione); B1.1–B2 (visuali concordate, bozza e via prima dell’HTML); B4–B6 (riuso e stato); C1–C4 (provenienza, scelta, tabelle e didascalie); C5 per i video; D1–D2.1 (verifica e salvataggio sul ramo).

Controlli preliminari svolti: identità/versione del sorgente, sezione di provenienza, tredici quesiti e confini dei capitoli; manifest v11 con sorgente unificato escluso; assenza di uno stato corrente a questo percorso.
I crediti incorporati nel sorgente segnalano risorse senza attribuzione individuale: il loro riuso storico non certifica una licenza. Nessuna nuova associazione nel registro crediti in questa fase.
Non sono stati eseguiti controlli browser, build o credits.py: le modifiche riguardano soltanto la progettazione Markdown.

## Prossimo passaggio

Presentare la proposta all’utente e raccogliere la scelta delle visuali. Poi verificare i dati delle tabelle e i materiali scelti, scrivere la bozza completa soltanto in `bozza.md` sullo stesso ramo, con segnaposto identificabili, e sottoporla all’approvazione. Dopo l’approvazione del testo, fornire la stima ripartita e attendere il via alla realizzazione HTML secondo B1.1.
Nessun HTML, ricerca o generazione di immagini, modifica al catalogo, merge o deployment è autorizzato da questa fase.

## Avanzamento — impostazione approvata e bozza v1

L’utente ha risposto **«Procedi»** alla proposta di riuso dei materiali e alla richiesta di procedere alla bozza. Questa risposta approva l’impostazione presentata e autorizza la stesura; non costituisce approvazione del testo ancora da leggere, via all’HTML o autorizzazione alla pubblicazione.

Completata [bozza.md](bozza.md), v1, 23 ottobre 2026: apertura sul confronto Terra/atomo; esponenti positivi, zero e negativi; forma scientifica e normalizzazione; breve distinzione dalla notazione ingegneristica; confronto fra scale e numeri; prodotto, divisione e somma; lettura delle micrografie; otto domande finali senza soluzioni. Tutti i materiali concordati hanno un segnaposto e una didascalia. Nessuna simulazione o esercizio fisico aggiuntivo.

Verifica dei dati: fonti OpenStax, NASA, ESA/Hubble e USGS, collegate nella sezione di servizio della bozza. Dichiarato il criterio dell’ordine di grandezza come potenza più vicina per fattori moltiplicativi, con precisazione breve in nota; non confuso con il solo esponente scientifico. Rispetto alla conversione pura del sorgente corretti gli ordini di massa di Terra (10²⁵ kg), cenere del Mount St. Helens (10¹² kg) e Via Lattea comprendente materia oscura (10⁴² kg); specificati i soggetti e conservata la provenienza dei valori precedenti. Per la Via Lattea usata una stima rappresentativa del 2019, non dichiarata misura attuale definitiva. Il diametro terrestre circa 12 700 km approssima il diametro medio 12 742 km.

Verifiche numeriche indipendenti svolte: quattro forme della lunghezza 0,000047 m equivalenti; confronto di scale con differenza 17; prodotto pari a 0,12; somma pari a 2300; sette ordini della tabella delle masse verificati dai valori di riferimento. Controllati otto quesiti, otto identificativi dei segnaposto, richiamo/nota e undici coppie dei delimitatori delle formule. Nessuna build o prova browser necessaria per questa sola stesura Markdown.

Materiali e limiti: registro e sorgente non permettono di certificare l’esatta provenienza di COP-01 e IMG-01. Nessuna ricerca o sostituzione di immagini effettuata. Restano da identificare i file e verificare i diritti prima dell’integrazione. Aperti i due URL video originali e verificati i titoli; riproduzione integrale e diritti di redistribuzione delle miniature non verificati. Controllata la descrizione molecolare di VID-02 sulla scheda del record Guinness. Questi punti sono espliciti nella sezione di servizio e non vengono presentati come risolti.

Prossimo passaggio corrente: lettura e approvazione della bozza da parte dell’utente. Dopo il testo approvato, stima ripartita e via esplicito prima dell’HTML secondo B1.1. PR #63 conservata in bozza. Main, HTML storici, manifest, catalogo e pubblicazione invariati.

## Revisione richiesta — bozza v2

Richiesta esplicita: eliminare l’ultima sezione mantenendo A Boy and His Atom; usare soltanto la tabella delle lunghezze per gli ordini di grandezza; togliere il cratere e aggiungere DNA di una cellula e lunghezza complessiva dei cavi Internet mondiali. Modifiche circoscritte autorizzate direttamente; nessuna nuova richiesta di permesso necessaria.

Completato in [bozza.md](bozza.md), v2:
- Rimossa la sezione «Una fotografia non basta a misurare», insieme alle micrografie IMG-01. Conservato VID-02 con introduzione breve e didascalia, spostato in «Confrontare le scale».
- Eliminati TAB-01M, il paragrafo sulle masse e le fonti di massa dalla sezione corrente di servizio. Una sola tabella degli ordini di grandezza, TAB-01L; TAB-02 e TAB-03 restano per potenze e notazioni.
- Tolto il cratere. Aggiunto DNA nucleare disteso dei 46 cromosomi di una cellula umana: circa 2 m, ordine 10⁰ m.
- Per la rete Internet, usato il riferimento globale della fibra ottica per telecomunicazioni, oltre 5 miliardi di km riportati da CORDIS/ECSTATIC: scala 10¹³ m. La richiesta generica di sommare tutti i cavi non ha un totale verificato nelle fonti consultate. Etichetta e nota delimitano quindi il dato alle fibre ottiche, sommando quelle interne ai cavi, senza spacciarlo per lunghezza dei soli tracciati o totale anche dei cavi in rame. Non sostituito con il solo dato sottomarino.
- Modificata la nota sul criterio degli ordini di grandezza per eliminare l’esempio della massa terrestre.
- Quesito 8 sulle micrografie sostituito con confronto fra DNA disteso e altezza di una persona. Questa rimozione specifica dell’utente supera la conservazione del vecchio quesito 7 per il capitolo corrente; testo storico recuperabile in Git.

Fonti nuove collegate nella sezione di servizio: Genomics England e Nature Education per il DNA; scheda Commissione europea CORDIS progetto 101189595 (ECSTATIC) per la rete mondiale; grafico in Optics & Photonics News marzo 2022 per il conteggio in fibra-km. Nessuna immagine cercata, generata o sostituita.

Controlli: nessuna massa, micrografia o cratere nel testo didattico; video originale VID-02 e collegamento conservati; una sola tabella di ordini fisici, otto righe di lunghezze; otto quesiti; 2 m ha ordine 10⁰ m e 5 · 10¹² m ha ordine 10¹³ m con il criterio dichiarato. Fonti e note aggiornate alle risorse correnti. Nessun HTML o registro crediti modificato; nessun merge o deployment.
Prossimo passaggio: approvazione della bozza v2, quindi stima e via alla realizzazione secondo B1.1.

## Realizzazione autorizzata e anteprima HTML v1 — 23 ottobre 2026

Richiesta corrente **«Approvato, procedi»**: approvata la bozza v2 e autorizzata la realizzazione. Comunicato intervallo 30–60 minuti, ripartito in materiali/crediti, impaginazione e verifiche, con carico basso e senza simulazioni. Il comando esplicito dell’utente autorizza il proseguimento; non è approvazione dell’anteprima ancora da mostrare né della pubblicazione.

Realizzati il file stabile `potenze_dieci_notazione_scientifica_it.html` v1 e la copia identica [bozza.html](bozza.html), 525157 byte, dal generatore riproducibile [realizza.py](realizza.py). Modello autonomo Stringhe v22: tutti i CSS e script canonici conservati byte per byte e nello stesso ordine. Estensioni circoscritte per tabelle scorrevoli, frazioni HTML e miniature video. Italiano, tema scuro predefinito, barra universale, indice a sei sezioni, tre tabelle, undici formule, otto quesiti, due note collassabili. A Boy and His Atom mantenuto. Nessun lettore incorporato o dipendenza matematica esterna.

Registro unico esteso con il solo nuovo documento, fonti correnti e occorrenze; inventario aggiornato con la funzione canonica. Nessuna riscrittura degli snapshot degli altri capitoli; pagina pubblica dei crediti invariata, verificata contro il renderer. Il capitolo resta fuori dal manifest e dalla build pubblica fino all’approvazione dell’anteprima. Collegamento al capitolo precedente già pubblicato; nessun rimando a capitoli futuri inesistenti.

Verifiche: `python3 scripts/credits.py --check` superato su 30 documenti, 145 schede, 223 asset; `python3 scripts/build_pages.py` superato, 17 HTML e 20 copertine. [verifica.py](verifica.py) ha controllato 320/390/768/1024/1440 px, chiaro e scuro, senza overflow della pagina o errori JavaScript; tre tabelle, otto righe delle lunghezze, immagini decodificate, indice/Escape, note e ritorni, download identico byte per byte. Menu tema e secondo richiamo controllati anche con azione sui pulsanti effettivi. Autonomia delle immagini e contenuti verificata con rete disattivata e con/senza JavaScript. Report e hash in [verifiche.json](verifiche.json).

Schermate correnti: [desktop](anteprima-1440.png), [mobile](anteprima-390.png), [tabella desktop](tabella-1440.png), [tabella mobile](tabella-390.png), [copertina mobile](copertina-mobile.png). Il controllo iniziale aveva rilevato un’eccedenza delle miniature originali; corretta prima della suite finale. Composizione delle tabelle invariata, scorrimento interno su schermi stretti.

Limite materiale ancora aperto: la copertina incorporata nel sorgente e le miniature originali non hanno attribuzioni/licenze individuali documentate. Ispezionata l’immagine e verificati i metadati disponibili; ricerca di provenienza breve non conclusiva. Non attribuita per somiglianza a uno scatto NASA. Riutilizzo approvato conservato nell’anteprima e segnalato nei crediti; la verifica dei diritti resta necessaria prima della pubblicazione. Non dichiarare il controllo tecnico dei crediti come certificazione delle licenze.

PR #63 mantenuta in bozza, nessun merge né Pages. Prossima operazione: consegnare l’anteprima HTML corrente e le schermate; raccogliere le osservazioni e l’approvazione dell’anteprima secondo AGENTS.md/B5. Risolvere le provenienze mancanti prima di un rilascio ufficiale.

### Salvataggio remoto e consegna dell’anteprima

Realizzazione caricata e verificata sul ramo al commit `392e1bb3dbfe1e471ba7d0599463c83852c12450` nella PR #63, tuttora in bozza. [Anteprima interattiva corrente](https://raw.githack.com/rickymusu-bit/fisica/392e1bb3dbfe1e471ba7d0599463c83852c12450/potenze_dieci_notazione_scientifica_it.html): HTTPS 200, Content-Type text/html, 525157 byte identici al documento locale verificato. [Rapporto HTTPS](verifica-anteprima-online.json). Il primo client Python era rifiutato dal servizio con errore 1010; la verifica con identificativo browser ordinario è riuscita, senza cambiare proxy o policy.

Superati anche i 14 test unitari esistenti (`python3 -m unittest discover -s scripts -p 'test_*.py'`) e `git diff --check`. Il precedente tentativo di discovery nella cartella inesistente tests non costituiva un test eseguito; usata poi la suite effettiva in scripts. Nessuna modifica di test esistenti, tema condiviso o capitoli pubblicati.

Il solo salvataggio successivo del rapporto e di questo resoconto non cambia l’HTML dell’anteprima, le schermate o il manifest. Nessun deployment ufficiale avviato. Restano da approvare l’anteprima e da risolvere i diritti dei media ereditati prima di pubblicare.

## Copertina di Giove scelta dall’utente — HTML v2

Richiesta: «Usa questa come copertina», con il collegamento alla versione Wikimedia 960 px di Map of Jupiter.jpg. Sostituzione autorizzata direttamente; nessuna nuova scelta necessaria. File scaricato dall’URL esatto, 960 × 975 px, 120432 byte, conservato in [risorse/giove.jpg](risorse/giove.jpg) e incorporato byte per byte senza ritagli. HTML v2 e bozza testuale v3: modificata soltanto la copertina, la didascalia e i relativi metadati/crediti; corpo didattico confrontato con la versione precedente e identico.

Fonte verificata: [Wikimedia Commons, Map of Jupiter.jpg](https://commons.wikimedia.org/wiki/File:Map_of_Jupiter.jpg), autore NASA/JPL/Space Science Institute, pubblico dominio PD-USGov-NASA. [Fonte primaria NASA](https://www.nasa.gov/image-article/map-of-jupiters-south/): mappa stereografica dell’emisfero sud, polo sud al centro ed equatore al bordo, immagini Cassini dell’11–12 dicembre 2000. Verificata la [JPL Image Use Policy](https://www.jpl.nasa.gov/jpl-image-use-policy/); credito associato nell’accesso comune, nessuna approvazione istituzionale dichiarata. La vecchia copertina con provenienza incerta non ha più occorrenze o crediti nel capitolo corrente; resta nei materiali storici e in Git.

Crediti canonici e build superati; inventario globale con 30 documenti, 148 schede, 224 asset. Nessun cambiamento alla pagina pubblica dei crediti o agli altri capitoli. Browser mirato: 390 e 1440 px, chiaro/scuro, nessun overflow o errore JavaScript; immagine decodificata, proporzioni originali conservate. Schermate rigenerate. Esiti correnti in [verifiche-copertina.json](verifiche-copertina.json); gli altri rapporti attestano i controlli della precedente revisione, conservati senza attribuirli al nuovo hash.

Restano aperti soltanto i diritti delle due miniature dei video. Alla domanda dell’utente sul fotogramma: estrarre un’immagine non elimina i diritti del video. Occorrono una licenza che consenta il riuso, un permesso del titolare o un’eccezione applicabile allo specifico impiego; citazione dell’autore e finalità didattica non autorizzano automaticamente una copertina. [Guida ufficiale YouTube](https://support.google.com/youtube/answer/2797466?hl=it). Nessun fotogramma estratto o sostituzione delle miniature richiesta o eseguita.

PR #63 in bozza. Prossimo passaggio: consegna della nuova anteprima; nessun merge o Pages senza approvazione dell’anteprima corrente. La copertina è ora documentata, non segnalarla più tra i materiali senza attribuzione certa.

Anteprima corrente della copertina caricata al commit fb43c43ff746b488408d0bbb70e91cbe3a9d7671: https://raw.githack.com/rickymusu-bit/fisica/fb43c43ff746b488408d0bbb70e91cbe3a9d7671/potenze_dieci_notazione_scientifica_it.html . Verifica HTTPS 200 e confronto byte per byte riusciti; rapporto online aggiornato. Nessun deployment ufficiale.

## Lettori YouTube su richiesta — HTML v3

L’utente autorizza esplicitamente il caricamento del lettore al clic, l’aggiornamento delle regole e l’allineamento degli altri capitoli. I due video hanno ora un riquadro con titolo e icona, senza miniature/fotogrammi. Prima del clic non si crea alcun iframe né connessione a YouTube; dopo il clic il servizio youtube-nocookie.com fornisce il lettore con autoplay disattivato, controlli nativi e schermo intero. «Apri su YouTube» resta sempre disponibile; «Chiudi il lettore» rimuove l’iframe, interrompe la riproduzione e restituisce il focus. URL originali e copertina di Giove invariati.

Bozza testuale v4 e HTML v3 dal modello comune v23; modifiche limitate ai video, alle note di servizio e al componente condiviso. Le due miniature sono rimosse dal documento e dai crediti correnti: non restano immagini con attribuzione incerta nel capitolo. Lo stato dei diritti dei filmati non viene trasformato in una licenza per estrarre fotogrammi; il lettore usa l’incorporamento offerto dal servizio. Regole aggiornate in MASTER_PROMPT.md v69.7, C5 e D1, con richiamo in AGENTS.md.

Verifiche comuni e nuova anteprima in [lavorazione/sito/video_youtube/stato.md](../sito/video_youtube/stato.md). PR #63 mantenuta in bozza, nessuna pubblicazione prima dell’approvazione dell’anteprima corrente. I resoconti delle versioni precedenti restano storici; non riferirli al nuovo hash.

Anteprima corrente dopo l’adozione dei lettori: https://raw.githack.com/rickymusu-bit/fisica/dbde455d67ce42427e517ecdd3486381f7c79bfc/lavorazione/sito/video_youtube/index.html . HTML v3 verificato online al commit dbde455d67ce42427e517ecdd3486381f7c79bfc, identico al file locale. I due video non contengono più miniature da attribuire. La PR #63 include anche regole e migrazione degli altri capitoli; resta in bozza.

## Pubblicazione approvata — 23 ottobre 2026

L’utente approva esplicitamente l’anteprima corrente con «Approvo. Fai la pr e pubblica». Autorizzati completamento e merge della PR #63 e deployment Pages; superata l’attesa di approvazione indicata nei resoconti precedenti. Nuovo capitolo HTML v4, contenuto didattico identico all’anteprima v3: aggiunto soltanto il rimando al capitolo successivo. Manifest v12 con 13 capitoli; inserimento al terzo posto dell’area introduttiva, catalogo e pagina dei crediti aggiornati. Navigazione reciproca con Sistema internazionale (v5) e Termodinamica (v13), con copie correnti riallineate e date editoriali conservate. Nessuna riammissione degli HTML storici o tradotti. Verificati contenuti identici al netto di versione/navigazione, navigazione dei 13 capitoli ed esclusioni. Tema, crediti, migrazione video --check, build e 17 test superati. Merge e verifica del deployment da completare.

Suite completa sulla configurazione di pubblicazione: **190 combinazioni pagina/viewport/tema e 20 copertine**, nessun errore JavaScript. Rapporto: `lavorazione/sito/video_youtube/verifiche-portale-pubblicazione.json`. Schermate di controllo temporanee conservate fuori dal repository per evitare riscritture di materiali estranei.
