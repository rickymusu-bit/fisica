# Stato — Le cifre significative

Ultimo aggiornamento: 23 ottobre 2026 (Europe/Rome). Master consultato integralmente: v69.9.
Ramo dedicato: `lavorazione/cifre-significative`, derivato dal main `1a543c874408664ed6d1ac01a4e6b79019d864f9`.

## Incarico e fase

Richiesta effettiva: «Va bene. Adesso facciamo il capitolo 5». Avvio della progettazione del quinto capitolo del piano Introduzione alla fisica e alla misura: **Le cifre significative**. Nessuna approvazione specifica di visuali nuove, bozza, realizzazione HTML o pubblicazione dedotta dall'incarico.

Fase corrente: proposta di contenuti e visuali pronta in [visuali.md](visuali.md), da concordare prima della bozza secondo B1.1. Nessuno stato precedente dedicato individuato nell'albero main.

## Confini, fonte e domanda

Conteggio e significato delle cifre, zeri e decimali, arrotondamento, regole nei calcoli, numeri esatti e conservazione dell'informazione nei cambi di unità. Esclusi sviluppo di strumenti, errori e calcolo dell'incertezza, previsti nei capitoli 6–8.

Fonte identificata: `sistema_internazionale_notazione_it.html` v12, blob `61a32e96afce2136af8669b1544a02e9d751018d`, sezione `#cifre-significative`. Identità verificata tramite hash Git della copia locale. Consultati stato del sorgente, piano corrente e regole. Originale conservato invariato ed escluso dal sito.

Domanda proposta: perché 12,4 cm e 12,40 cm comunicano informazioni diverse pur avendo lo stesso valore numerico? Tema già scelto: Stringhe comune, modello v23, da leggere/riutilizzare nella fase HTML.

## Visuali e contenuti conservati

Proposto riuso di FIG-01 confronto numerico, TAB-01 conteggio degli zeri, TAB-02 arrotondamento, TAB-03 regole delle operazioni, FIG-02 cassa con quote. COP-01 nuova foto di bilancia digitale da scegliere/fornire dall'utente; nessuna ricerca o generazione avviata. Copertine sempre senza zoom. Diritti dell'immagine della cassa da verificare prima dell'integrazione; non attribuita una licenza per deduzione.

Proposto un solo esempio svolto articolato sui dati originali a = 2,34 m e b = 1,2 m, con formule generali, passaggi e interpretazioni. Quesiti originali 8–13 destinati a questo capitolo: verificato che le dieci domande del capitolo 4 non trattano il fattore esatto come limite alle cifre significative. Nessun video o simulazione proposti, nessun programma realizzato.

## Verifiche preliminari e prossima operazione

Confermata corrispondenza del capitolo 5 con il piano. Controllati i calcoli originali: somma 3,54 → 3,5 m; differenza 1,14 → 1,1 m; area 2,808 → 2,8 m²; rapporto 1,95 → 2,0; perimetro 7,08 → 7,1 m. La regola delle cifre significative va presentata come convenzione utile e non come sostituto universale dell'incertezza.

Checklist pertinente: A1–A5; A6 nella fase HTML; B1.1–B2, B4–B6; C1–C4 per le visuali effettive; D1–D2.1. Consultati STILE_DISPENSE.md, esempio_irraggiamento.md e standard dei visuali.

Prossimo passo: concordare proposta e materiali, ricevere la copertina scelta; quindi scrivere bozza.md con segnaposto e domande definitive. Non sono stati creati HTML né modificati manifest, catalogo, capitoli pubblicati o master. PR di progettazione da mantenere in bozza; autorizzazioni del capitolo 4 non trasferite a questo capitolo.

## Copertina scelta e bozza v1 — 23 ottobre 2026

L’utente sceglie Egyptian measuring tool.jpg e scrive «Procedi» dopo la proposta del capitolo: autorizzata la stesura secondo l’impostazione proposta. La foto della bilancia digitale è superata. Copertina scelta: miniatura 960 per 540 px, intera, senza zoom. Fonte Wikimedia Commons, autore Uriah Welcome, CC BY 2.0, provenienza Flickr e revisione della licenza documentate sulla pagina originale. URL, hash e metadati in risorse/copertina-fonte.json; foto in risorse/copertina-egizia.jpg. Non ricavata una precisione di misura o una datazione dalla fotografia.

[Bozza v1](bozza.md) completa con confronto 12,4/12,40 cm, tre tabelle originali, due procedure numerate, formule generali e calcoli dell’esempio conservati, conversione esatta e dieci domande; quesiti originali 8–13 ripresi nelle prime sei. Calcoli controllati con Decimal; note brevi per convenzione del 5 e rapporto con l’incertezza. Nessun video o simulazione.

La verifica dell’immagine PNG della cassa nel registro unico conferma fonte e licenza non documentate (asset-b17b9591b7a9cc34e9eec460fe2c2216c15619090af2f8bbdc9e44c01079b196). Il segnaposto FIG-02 rimane nella bozza; non inventata un’attribuzione e nessuna immagine sostitutiva cercata o generata. Provenienza da risolvere prima dell’integrazione della figura in un HTML da pubblicare.

Prossimo passo: revisione del testo corrente. Non attribuire al «Procedi» precedente un’approvazione di questa nuova bozza né della pubblicazione. HTML del capitolo 5 non realizzato; manifest e catalogo invariati. Le correzioni al capitolo 4 richieste nello stesso messaggio sono documentate nel relativo stato.

## Bozza e copertina approvate — 23 ottobre 2026

L’utente scrive «Approvo tutto. Quali immagini non hanno licenza nota?» in risposta alla richiesta di approvare l’anteprima corrente del capitolo 4 e il testo del quinto. Approvati testo v1, copertina egizia e impostazione dei visuali del capitolo 5. La domanda sulle licenze non revoca l’approvazione e non viene interpretata come autorizzazione a sostituire immagini o inventarne i diritti.

Punto aperto identificato con precisione: immagine PNG della cassa di legno nello schema FIG-02, senza fonte, autore o licenza documentati. I due SVG di confronto/quote sono elementi ereditati dal sorgente e non certificano i diritti del PNG che incorporano. Copertina 4 SecretDisc / CC BY-SA 3.0 e copertina 5 Uriah Welcome / CC BY 2.0 verificate. Mostrata l’immagine della cassa estratta dal sorgente per identificarla senza ambiguità.

Prossimo passo: risolvere la provenienza del PNG o ricevere una sostituzione scelta dall’utente; poi stimare e realizzare l’HTML secondo il workflow, conservando il testo ora approvato. Non chiedere nuovamente l’approvazione della bozza invariata. L’HTML del quinto resta non realizzato e non pubblicato.

L’utente si offre di cercare un’immagine sostitutiva e chiede quale serva. Richiesta una cassa a base rettangolare vista di tre quarti, due lati adiacenti della base ben visibili, preferibilmente fondo trasparente e senza quote; quote illustrative a = 2,34 m e b = 1,2 m da aggiungere nello schema. Richiesto anche il collegamento alla fonte per verificare la licenza. Nessuna sostituzione ancora scelta o integrata.

## Cassa generata su richiesta — 23 ottobre 2026

L’utente autorizza esplicitamente la generazione dell’immagine per l’esempio: «Se e per un esempio, generala tu». Generata e mostrata una cassa di legno rettangolare vista di tre quarti, su fondo trasparente, priva di scritte e quote. Originale conservato nella cartella generated_images; copia in risorse/cassa-generata.png e provenienza in risorse/cassa-fonte.json. L’immagine sostituisce nella proposta il PNG storico di provenienza non documentata; nessuna licenza di terzi attribuita per deduzione. Quote a = 2,34 m e b = 1,2 m da aggiungere in SVG, dati illustrativi e disegno non in scala. Testo approvato conservato; HTML non avviato. Salvataggio remoto di questa nuova risorsa ancora da completare.

## Realizzazione autorizzata e HTML v1 pronto — 23 ottobre 2026

Dopo la cassa generata e mostrata, l’utente scrive «Ok procedi»: via esplicito a schema quotato e HTML dal testo approvato. Comunicato ambito e stima indicativa di 15–25 minuti, nessuna nuova conferma richiesta. Master v69.9 e modello v23 verificati invariati rispetto alla lettura precedente; modello letto e riutilizzato, senza variante del tema.

Realizzato cifre_significative_it.html v1, copia identica in bozza.html: 12 formule MathML native, due frazioni orizzontali, tre tabelle (7/4/2 righe), due procedure di quattro passi, tre note collassabili, dieci domande finali e navigazione al capitolo 4. Nessun rimando a un capitolo 6 non ancora pubblicato. Copertina egizia incorporata intera, senza zoom. Schema FIG-01 riutilizzato dal sorgente con sola normalizzazione dell’attributo XML viewBox; FIG-02 contiene la cassa generata invariata e quote SVG a/b sui lati adiacenti della base. Originale PNG conservato, schema non in scala; nessun generatore usato per scrivere quote o formule. Generatore ripetibile in realizza.py.

Testo approvato conservato: bozza v2 aggiorna la provenienza/il segnaposto della cassa e sostituisce «fotografia» con «immagine» per coerenza con la generazione. Il PNG storico di fonte ignota non è riprodotto. Registro unico esteso al nuovo capitolo, copertina e schemi; nessuna attribuzione esterna inventata per l’immagine generata. Tutti i precedenti documenti del registro invariati; crediti pubblici invariati perché il nuovo HTML non è ancora ammesso.

Verifiche: crediti --check, tema --check e build riusciti. Nuovo capitolo escluso dalla build pubblica; manifest, catalogo, modello, capitoli pubblicati e sorgenti storici invariati. Browser Chromium a 320/390/768/1024/1440 px in chiaro/scuro, senza overflow né errori JavaScript o richieste esterne; immagini e formule decodificate, indice con Escape/ancore, note/rientri, scorrimento tastiera delle tabelle, zoom della cassa, menu tema effettivo, crediti e OFL, download byte per byte. Senza JavaScript zoom e crediti nativi disponibili; senza rete contenuto in memoria, immagini incorporate e MathML verificati. Nessuna verifica su dispositivi fisici dichiarata. Ispezionate schermate mobile della copertina, frazione e schema, e schema desktop. Peso 8,84 MB, sotto le soglie del master.

Rapporti verifiche-browser.json e verifiche-finali.json. Prossimo passo: salvare e verificare risorse, HTML e schermate sul ramo dedicato, aprire una nuova PR in bozza dopo la precedente #67 già integrata, presentare l’anteprima corrente. Nessun merge o deployment del capitolo 5 prima dell’approvazione esplicita dell’anteprima secondo AGENTS.md. Il testo e la cassa già approvati non richiedono una nuova approvazione separata.

## Revisione richiesta — HTML v2, 23 ottobre 2026

L’utente richiede di togliere lo zoom dalla figura della prima sezione, introdurre l’abbreviazione C.S. prima di usarla, orientare verso l’esterno le punte delle quote fino ai delimitatori e rimuovere del tutto «dati illustrativi, disegno non in scala» da immagine e didascalia. Richiama la regola già presente in A1 del master: eliminare precisazioni superflue e ripetizioni; nessuna nuova regola generale inventata o modifica al master necessaria.

Applicati i quattro interventi in HTML v2 e generatore; bozza v3 allineata. Titolo e definizione iniziale conservano «cifre significative»; la definizione introduce C.S., usata da quel punto nel testo, nelle tabelle, nelle formule descrittive, nelle domande e nella prima figura. Rimossi i doppi punti finali dell’abbreviazione. FIG-01 contiene soltanto l’immagine principale, senza details/pulsante/copia di zoom; quello della cassa resta disponibile. Frecce SVG con punta esterna (auto-start-reverse, refX=8 sul vertice terminale); gli estremi coincidono con i delimitatori. Eliminata la riga ridondante dallo schema e la precisazione dalla didascalia, dalla descrizione alternativa e dai crediti della cassa; tolto anche il inciso analogo nella presentazione dei dati. Nessuna nuova nota aggiunta per sostituire l’avviso rimosso. Sorgente PNG generato invariato.

Verificati crediti e tema, browser a cinque larghezze nei due temi, nessun overflow o errore; nuove asserzioni su figura senza zoom e abbreviazione introdotta. Dodici formule identiche alla v1 salvo la sostituzione delle etichette verbali con C.S.; quantità e risultati invariati. Ispezionate nuova prima figura mobile, schema desktop con frecce esterne, frazione mobile; zoom della cassa, note, tastiera, download, offline e senza JavaScript restano verificati. Rapporti aggiornati; altre dispense e pubblicazione invariati. PR #68 da mantenere in bozza, anteprima corrente v2 da presentare senza pubblicarla.

## Zoom rimosso dalla cassa e regola salvata — HTML v3

Richiesta esplicita dell’utente: togliere lo zoom alla cassa e riservarlo a grafici e schemi con scritte numerose e piccole; successiva conferma «Salva nelle regole questa sullo zoom». Regola integrata nel paragrafo pertinente di A6 del MASTER_PROMPT.md v69.10 e nei rinvii operativi di AGENTS.md: niente zoom su fotografie, copertine e figure con poche etichette leggibili. Conservata la regola delle copertine. Nessuna modifica generale automatica ai capitoli pubblicati dedotta dalla richiesta.

HTML v3 e generatore: rimosso il details di zoom della cassa e la copia duplicata, immagine principale e quote SVG invariate. Nessuno zoom nel capitolo 5: entrambe le figure hanno poche etichette. Bozza v4 allineata soltanto nelle istruzioni visuali; testo e formule invariati. Il file autonomo scende a circa 4,68 MB. Crediti e tema verificati; browser a cinque larghezze nei due temi, immagini, assenza di zoom, note, indice, tabelle, download identico, offline e senza JavaScript superati. Nessun errore JavaScript o overflow. Rapporti e schermate aggiornati. PR #68 ancora in bozza, sito pubblico invariato; nuova anteprima v3 da consegnare.

## Pubblicazione autorizzata — 23 ottobre 2026

L’utente approva l’anteprima HTML v3 corrente con «Perfetto pubblica». Autorizzati inserimento nel catalogo, collegamenti adiacenti, merge della PR #68 e deployment Pages, senza nuova richiesta di conferma. HTML v4 con solo il rimando successivo a Termodinamica, corpo identico all’anteprima approvata; copertina, C.S., frecce esterne, assenza di zoom e rimozione degli avvisi conservate.

Manifest v14 con 15 capitoli; nuovo capitolo al quinto posto dell’area introduttiva. Catalogo e crediti pubblici aggiornati. Navigazione reciproca Prefissi (v4) → Cifre significative (v4) → Termodinamica (v15), copie correnti e generatori pertinenti allineati; contenuti didattici e date degli adiacenti invariati. Verificati i corpi dei tre articoli e la sequenza di tutti i 15 capitoli, normalizzando i rimandi assoluti storici per il controllo dei percorsi. Master v69.10 e AGENTS.md con regola dello zoom inclusi nel rilascio.

Crediti e tema --check, build (20 HTML locali, confronto escluso dal deployment ufficiale) e 18 test riusciti. Verifica completa locale riuscita: 210 combinazioni pagina/viewport/tema e 20 copertine, nessun errore JavaScript. CI remoto da completare prima del merge; poi verificare deployment e corrispondenza HTTPS. Sorgenti esclusi e indirizzi storici non riammessi. La pubblicazione autorizzata sostituisce le precedenti attese di approvazione dell’anteprima.

## Capitolo 5 pubblicato — 23 ottobre 2026

[PR #68](https://github.com/rickymusu-bit/fisica/pull/68) integrata al commit b395589e1f5f06197723171ab4dfb3d33142114c. [Deployment Pages 39992857516](https://github.com/rickymusu-bit/fisica/actions/runs/39992857516) riuscito. [Le cifre significative](https://rickymusu-bit.github.io/fisica/cifre_significative_it.html), HTML v4, è il quinto capitolo del percorso introduttivo. Catalogo, crediti e navigazione aggiornati; master v69.10 e AGENTS.md con regola dello zoom integrati in main.

Verifica HTTPS dopo il deployment: 19 pagine pubbliche HTTP 200 e identiche byte per byte alla build locale; 12 indirizzi esclusi, storici o di anteprima HTTP 404. Rapporto verifica-pubblicazione-online.json e script ripetibile verifica_pubblicazione.py nella lavorazione del quinto capitolo. Le prove locali complete sono riuscite: 18 test, 210 combinazioni pagina/viewport/tema e 20 copertine, oltre ai controlli specifici del capitolo.

Il workflow remoto 39991173540 ha superato tema, crediti, build e test; l’installazione di Chromium ha ritardato il controllo. Il merge regolare è stato accettato da GitHub sulla base della suite locale completa già riuscita. Al controllo successivo alla pubblicazione il CI remoto sta eseguendo le prove browser; il suo esito non è ancora registrato come riuscito. Il deployment e la verifica delle pagine pubbliche sono completati.
