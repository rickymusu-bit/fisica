# Requisiti tecnici delle dispense

Aggiornamento: 17 ottobre 2026, ore 14:07 (Europe/Rome).

Fonte ufficiale per HTML autonomo, accessibilità tecnica, materiali, diritti, ottimizzazione, versioni e verifiche. Conserva i requisiti tecnici approvati. Contenuti: [contenuti e stile](CONTENUTI_E_STILE.md). Aspetto e interazione: [tema grafico](TEMA_GRAFICO.md). Procedura: [master](../MASTER_PROMPT.md).

<a id="t1"></a>
## T1. Formato HTML, autonomia e lingue

Il risultato finale resta un HTML autonomo e completo, salvo diversa richiesta esplicita, senza sorgente Quarto (.qmd). Prima della realizzazione presenta la bozza del testo in chat o in un file separato, con segnaposto per gli elementi visuali, secondo [P2](../MASTER_PROMPT.md#p2): questa bozza non è la consegna HTML finale. Per un primo capitolo il file contiene quel capitolo; per aggiunte e revisioni aggiorna il documento concordato. Un frammento HTML privo di struttura completa si consegna soltanto se richiesto esplicitamente.

Usa HTML5 con `<!DOCTYPE html>`, `<html lang="it">`, codifica UTF-8, meta viewport, titolo, CSS incorporato e meta versione. Incorpora le immagini e il codice necessari per il funzionamento offline quando possibile. Preferisci HTML, CSS e JavaScript standard, evitando framework e dipendenze esterne non indispensabili.

Se sono richiesti file separati per lingua, ciascuno deve essere autonomo, contenere solo la lingua prevista e non avere un selettore. Solo quando è richiesto esplicitamente un unico file con più lingue, inserisci nella prima schermata pulsanti affiancati con i nomi delle lingue, come nel modello grafici_piano_cartesiano_v4_20261001. Non usare menu a tendina. Evidenzia la lingua attiva con aria-pressed, lascia andare i pulsanti a capo su smartphone e incorpora tutte le traduzioni perché la selezione funzioni offline.

Incorpora il font e la relativa licenza per il funzionamento offline. Per le regole linguistiche delle traduzioni applica [S7](CONTENUTI_E_STILE.md#s7).

<a id="t2"></a>
## T2. Accessibilità e risorse

Usa HTML semantico, figure con didascalia, gerarchia corretta dei titoli, descrizioni accessibili pertinenti, contrasto sufficiente, navigazione da tastiera e focus visibile. Non affidare un’informazione al solo colore. L’alt descrive ciò che è utile capire, senza limitarsi al nome del file.

Per adattamento agli schermi, indice, navigazione e ingrandimento applica il [tema grafico](TEMA_GRAFICO.md). Le formule devono restare leggibili su smartphone; se MathJax o KaTeX dipendono da un servizio esterno, segnala la necessità di Internet e preferisci una soluzione autonoma leggera quando possibile.

<a id="t3"></a>
## T3. Immagini, fedeltà, licenze e crediti

Utilizza le immagini fornite dall’utente senza sostituirle autonomamente; una sostituzione richiede una sua richiesta. Per gli oggetti, le persone e i dispositivi negli schemi degli esempi o esercizi, usa immagini corrispondenti recuperate dal web o fornite dall’utente, comprese fotografie realistiche. Non costruire autonomamente questi soggetti con linee, cerchi, rettangoli, sagome astratte o altre forme geometriche; non generare immagini sostitutive senza esplicita richiesta dell’utente e non trasformare un’immagine scaricata in un disegno geometrico.

Scegli immagini riconoscibili, pertinenti, fedeli e leggibili anche in piccolo, con stile il più possibile coerente. Evita interpretazioni artistiche, caricature, deformazioni e disegni troppo abbozzati. Per immagini generali preferisci l’assenza di sfondo; se non disponibile, usa un fondo neutro, pulito e non caotico. Negli schemi degli esempi e degli esercizi lo sfondo deve essere assente: rimuovilo rendendolo trasparente e preservando il soggetto. Se questo compromette soggetto o comprensione, scarta l’immagine e cercane un’altra. La regola degli esercizi prevale su quella generale del fondo neutro.

Preferisci immagini senza loghi o scritte sovrapposte dal sito di provenienza, soprattutto al centro. Puoi ritagliare quegli elementi solo se restano intatti utilità, soggetto e comprensione; altrimenti scarta l’immagine. La regola vale anche per immagini fornite, delle quali conservi l’originale. I marchi degli oggetti e i loghi naturalmente presenti nelle fotografie reali possono restare: distinguili dalle sovrapposizioni aggiunte dal sito.

Verifica la licenza sulla fonte originale, preferendo pubblico dominio o CC0 quando possibile. Usa licenze compatibili con la dispensa, conserva provenienza e modifiche nel codice e nel registro dei materiali e rispetta le attribuzioni obbligatorie. Colloca i crediti necessari in una sezione separata in fondo alla dispensa, prima del piè di pagina, senza metterli nelle didascalie multimediali né nel piè di pagina. La sezione deve avere un titolo piccolo e discreto, per esempio «Crediti delle immagini», ed essere collassabile tramite gli elementi HTML nativi <details> e <summary>, inizialmente chiusa. Quando viene aperta, deve rendere accessibili e leggibili le attribuzioni obbligatorie, le fonti e le licenze, con collegamenti funzionanti; preserva accessibilità da tastiera e compatibilità offline del documento.

Se non riesci a recuperare un’immagine adatta, fermati e chiedi esplicitamente all’utente di fornirla prima di completare lo schema e consegnare quella parte. Non aggirare la regola con immagini non pertinenti, oggetti astratti o immagini generate.

Puoi affiancare o sovrapporre frecce, vettori, quote, traiettorie, linee di riferimento, collegamenti ed etichette per spiegare la Fisica: non sostituiscono le immagini degli oggetti. Punti e simboli matematici nei grafici, e la pallina di una simulazione puntiforme esplicitamente richiesta o approvata, appartengono al modello fisico concordato; questa possibilità non autorizza a sostituire con sagome astratte gli oggetti reali di altri esercizi.

<a id="t4"></a>
## T4. Trattamento dei materiali forniti

Classifica il materiale prima di intervenire:

- Fotografie e illustrazioni: inseriscile direttamente, nel punto utile, con proporzioni corrette, alt, didascalia e riferimento nel testo quando serve.
- Tabelle, grafici e flowchart forniti come immagini: ricostruiscili come descritto in [T5](REQUISITI_TECNICI.md#t5), senza inserire lo screenshot come risultato finale.
- Infografiche, mappe concettuali, schemi illustrati, linee temporali e altri diagrammi complessi diversi dai flowchart: inseriscili direttamente come immagini. Non ricostruirli o reinterpretarne la struttura senza una richiesta esplicita. Se sono troppo densi o poco leggibili su smartphone, segnalalo invece di ridisegnarli autonomamente.

La classificazione governa il trattamento tecnico; le didascalie seguono [S6](CONTENUTI_E_STILE.md#s6). Le modifiche richiedono la fase di accordo e accettazione prevista nel [workflow](../MASTER_PROMPT.md#p2).

<a id="t5"></a>
## T5. Tabelle, grafici e diagrammi di processo

Per ogni ricostruzione conserva contenuti e significato: numeri, dati, formule, categorie, etichette, unità, ordine, relazioni, sequenze e annotazioni scientificamente importanti. Puoi adattare colori, font, spessori, forme, dimensioni, icone, spaziature e disposizione per uniformarli alla dispensa, senza alterare i dati per rendere il risultato più gradevole. Se un dettaglio non è leggibile, non inventarlo: inserisci nel codice `<!-- DATO DA VERIFICARE: testo non chiaramente leggibile nell’immagine originale -->` e segnala il dato da chiarire quando necessario.

Tabelle: usa HTML semantico, con table, thead, tbody, th e caption quando appropriati. Mantieni intestazioni, unità, categorie e ordine delle righe e colonne; migliora la disposizione soltanto senza cambiarne il significato. Adatta la tabella o usa un contenitore con scorrimento orizzontale.

Grafici: preferisci SVG o HTML/CSS, e JavaScript leggero solo quando utile. Conserva dati, scala, andamento, assi, variabili, unità, punti significativi, legenda e annotazioni. Introduci il grafico, spiega che cosa osservare e collega i dati ai concetti. Indica grandezze e unità degli assi e significato dell’andamento. Non usare grafici decorativi.

Flowchart e diagrammi di processo: conserva passaggi, ordine, condizioni, ramificazioni, relazioni e direzione delle frecce. Preferisci HTML/CSS per strutture semplici e SVG per quelle articolate. Puoi riorganizzare la composizione; su smartphone rendila verticale quando possibile ed evita ampiezze che richiedano continui scorrimenti laterali.

Gli elementi ricostruiti devono condividere lo stile della dispensa e seguire le regole di leggibilità di [G6](TEMA_GRAFICO.md#g6). La composizione degli schemi fisici può usare SVG o HTML/CSS e incorporare immagini scaricate ed elementi esplicativi, mantenendo uso offline, descrizione accessibile e didascalia. Traduci le etichette quando la traduzione è richiesta.

<a id="t6"></a>
## T6. Video e simulazioni

VIDEO. Usa soltanto video e link forniti, salvo richiesta esplicita di cercarne altri. Mantieni il link esatto e gli eventuali timestamp; non sostituirlo autonomamente. Presenta ogni video nel punto didatticamente utile attraverso una miniatura cliccabile, pulsante play sovrapposto e breve titolo o introduzione con ciò che osservare. L’esperienza è: miniatura → clic → apertura nella piattaforma originale.

Non incorporare lettori video, iframe di piattaforme video, autoplay o player YouTube. Il link deve comprendere tutta la miniatura, aprirsi preferibilmente in nuova scheda e usare target="_blank" e rel="noopener". La miniatura condivide larghezza e stile delle immagini, mantiene preferibilmente proporzioni 16:9, ha bordi coerenti e un play con contrasto sufficiente. Realizza il pulsante con CSS, SVG o HTML, senza un’immagine separata quando non serve. Garantisci navigazione da tastiera, focus visibile, aria-label significativo e alt riferito al contenuto o titolo, non soltanto «immagine YouTube».

Per YouTube ricava il VIDEO_ID dal link e usa, quando disponibile, https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg oppure un’altra miniatura ufficiale fornita. Non inventare URL. Se non puoi ottenere una miniatura valida e utilizzabile, fermati per quella parte e chiedi esplicitamente all’utente di fornirla; non usare immagini generiche casuali.

SIMULAZIONI. Puoi creare animazioni e simulazioni JavaScript quando richieste o approvate e utili al fenomeno. Il precedente divieto di animazioni JavaScript non si applica. Preferisci codice standard incorporato, funzionamento offline quando possibile, comandi per pausa e riavvio, uso su smartphone e rispetto della preferenza di riduzione del movimento. Verifica prima il modello e le grandezze fisiche, poi la presentazione.

Il divieto dei lettori incorporati riguarda i video, non una simulazione locale autonoma. Una simulazione incorporata può usare un iframe locale o con contenuto incorporato nel documento, quando serve all’isolamento del codice e non introduce dipendenze superflue. Restano valide le regole delle immagini e la stima preventiva per realizzare una nuova simulazione. Riusa una simulazione approvata quando basta cambiare i dati o correggere una parte circoscritta.

Per le GIF vale il [divieto di comandi di pausa e riavvio](TEMA_GRAFICO.md#g7).

<a id="t7"></a>
## T7. File, peso, ottimizzazione e versioni

Usa nomi di file stabili, senza numero di versione né data: per le dispense HTML mantieni la base del nome e l’eventuale suffisso di lingua, per esempio `<argomento>_it.html`, `<argomento>_fr.html` o `<argomento>.html` per una serie già univoca. Le revisioni aggiornano lo stesso percorso; numero progressivo e data restano nei metadati e nel piè di pagina della dispensa. Incrementa la versione interna anche per piccole modifiche del contenuto; una sola rinomina, senza cambiamenti del file, conserva numero e data interni. Anche master e file di lavorazione usano nomi stabili. Git conserva la cronologia e identifica in modo univoco ogni revisione tramite il commit. Prima di rinominare verifica identità e assenza di collisioni, aggiorna i collegamenti interessati e mantieni funzionanti gli indirizzi già pubblicati tramite reindirizzamenti diretti al percorso corrente, salvo richiesta esplicita dell’utente di rimuoverli. Non eliminare né sovrascrivere file di identità incerta.

Dimensione e ottimizzazione delle dispense HTML: misura il peso effettivo di ciascun file, comprese immagini e risorse incorporate. Punta a **5–8 MB complessivi per capitolo**, inclusi font, codice e immagini incorporate; è un obiettivo di ottimizzazione, non un limite che autorizza a sacrificare contenuti o leggibilità. A partire da 18 MB (18.000.000 byte) avvisa l'utente e valuta possibili ottimizzazioni, specialmente prima di inserire nuovi contenuti visivi. Il limite finale è 20 MB (20.000.000 byte) per file. Con l'approvazione dell'utente puoi ottimizzare copie delle immagini mediante compressione, conversione di formato o riduzione della risoluzione, scegliendo in base al contenuto; conserva sempre gli originali forniti e non alterare informazioni, proporzioni, formule, etichette o dettagli scientifici necessari. Verifica la leggibilità anche su smartphone. La suddivisione per argomento prevista in [S3](CONTENUTI_E_STILE.md#s3) si applica indipendentemente dal peso. Per un capitolo monografico troppo pesante prova prima le ottimizzazioni approvate senza eliminare contenuti. Se la dispensa resta oltre 20 MB, suddividila esclusivamente tra capitoli completi in HTML autonomi, con stile, versioning, indice, numerazione e funzionamento offline coerenti; non spezzare un singolo capitolo. Se un solo capitolo eccede comunque il limite, informa l'utente e concorda una soluzione, senza dividerla autonomamente. Le parti correnti diventano ufficiali nel repository solo dopo verifica, mantenendo recuperabili in Git quelle precedenti. Controlla peso e integrità di ogni parte prima della consegna.

Per le copie dei visuali inserite nell’HTML applica le impostazioni approvate seguenti, coerenti con una colonna di lettura di circa 800 px:

| Tipo di visuale | Risoluzione consigliata | Peso indicativo del file immagine |
| --- | --- | --- |
| Copertina e fotografie | Massimo 1.600 px sul lato lungo | 150–350 KB |
| Immagini piccole o affiancate | 800–1.000 px sul lato lungo | 80–180 KB |
| Spettri, termografie e schemi con scritte | Fino a 2.000 px sul lato lungo, quando necessario per leggere i dettagli | 200–500 KB |
| Grafici e formule realizzati nella pagina | Preferisci SVG o HTML/CSS, mantenendo la natura vettoriale e le regole di [T4](#t4) e [T5](#t5) | Generalmente molto leggeri; verifica il peso effettivo |

Per le fotografie preferisci WebP, con qualità iniziale indicativamente 80–85 su scala 0–100, verificando visivamente il risultato. Per schemi e scritte scegli il formato che preserva meglio linee ed etichette. Non ingrandire un originale piccolo soltanto per raggiungere queste dimensioni. I pesi sono obiettivi indicativi, non soglie rigide; per immagini con dettagli scientifici la leggibilità prevale anche sul limite standard di risoluzione. Se il visuale resta troppo denso su smartphone, segnala il problema senza ridisegnarlo autonomamente in contrasto con [T4](#t4). Conserva gli originali separati: risoluzione e pesi indicati riguardano soltanto le copie per la dispensa; l’utente può fornire i file originali senza ridurli preventivamente. Valuta il peso finale dell’HTML dopo l’incorporamento, che può aumentare rispetto al peso dei soli file immagine. Applica queste impostazioni durante le fasi di realizzazione autorizzate, rispettando eventuali richieste di attesa; non comprimere o convertire anticipatamente i materiali.

Git conserva la cronologia di master, dispense e file di lavorazione; non occorrono copie storiche numerate dello stato o del master nell’albero corrente né una pulizia della Libreria ChatGPT per completare un salvataggio. Distingui lingue, formati e varianti che costituiscono risultati diversi. Dopo aver salvato e verificato una nuova versione, rimuovi dall’albero corrente soltanto duplicati o versioni sostituite della stessa serie identificati con certezza, senza perdere la cronologia Git e senza rompere collegamenti. Chiedi chiarimenti se l’identità non è certa. Conserva immagini originali, materiali di riferimento e documenti unici: non sono versioni obsolete. Non cancellare un originale necessario per comprendere o riutilizzare un materiale approvato. Durante questa migrazione non eliminare alcun materiale su Drive.

Il piè di pagina della dispensa contiene esclusivamente versione e data, per esempio «Versione v2 · 29 settembre 2026», localizzate nelle traduzioni. Escludi commenti editoriali, note sui materiali, descrizioni delle modifiche e bibliografie. Le fonti scientifiche indispensabili stanno nel corpo del testo vicino al contenuto; le attribuzioni delle immagini seguono [T3](REQUISITI_TECNICI.md#t3).

<a id="t8"></a>
## T8. Controlli pertinenti e sufficienti

Prima di consegnare controlla la correttezza scientifica, la chiarezza e l’aderenza allo scopo. Per una nuova dispensa o una ristrutturazione ampia esegui il controllo completo sotto indicato. Per una modifica locale controlla la parte modificata e ciò che può esserne influenzato; non ripetere prove già superate senza una nuova modifica, un errore o un dubbio concreto. Quando cambia un collegamento condiviso, un indice, un’immagine riutilizzata o una funzione comune, controlla anche i punti che ne dipendono.

**Contenuti e calcoli:** verifica le regole di [contenuti e stile](CONTENUTI_E_STILE.md), compresi livello, dati, unità, notazione, schema fisico degli esempi, ordine monografico, domande finali, percorso narrativo e assenza di digressioni non richieste.

**Visuali e diritti:** controlla che materiali scelti e accettati siano presenti nel punto utile; rispetta [scelta e approvazioni](../MASTER_PROMPT.md#p8), [fedeltà, originali e licenze](#t3), [classificazione](#t4), [ricostruzioni](#t5), [copertina](CONTENUTI_E_STILE.md#s3), [didascalie](CONTENUTI_E_STILE.md#s6) e [ottimizzazione](#t7). Richiedi i materiali mancanti senza sostituzioni inventate.

**Funzionamento e lettura:** verifica collegamenti interni ed esterni, indice, ritorno alla Biblioteca, precedente/successivo con assenza del tasto ai due estremi, proporzioni, focus e tastiera, uso mobile, leggibilità di tabelle/formule/grafici, equilibrio fra testo e visuali, ingrandimento con etichetta o icona coerente anche senza script. Applica il [tema](TEMA_GRAFICO.md). Per [video e simulazioni](#t6) controlla miniature, play, destinazioni, assenza di player video incorporati, comandi e bilanci; per le [GIF](TEMA_GRAFICO.md#g7) controlla l’assenza dei comandi vietati. Verifica autonomia e uso offline quando previsti.

**Lingua e file:** verifica [lingua e traduzioni](CONTENUTI_E_STILE.md#s7), [file separati o multilingue](#t1), nome autore, HTML finale, versione e piè di pagina secondo [T7](#t7).

Non dichiarare eseguite verifiche non svolte. Se resta un limite materiale o un dato da chiarire, descrivilo brevemente nella consegna. Una versione provvisoria incompleta si consegna solo se richiesta o concordata; non presentarla come definitiva.

<a id="t9"></a>
## T9. Sorgenti comuni e HTML consegnati

Le sorgenti riutilizzabili del tema sono in [tema/](../tema/README.md); il componente di navigazione sequenziale è in [scripts/chapter_navigation.py](../scripts/chapter_navigation.py). Il generatore incorpora CSS e JavaScript nel documento finale, senza introdurre dipendenze esterne. Per le scelte di aspetto e comportamento fa fede il [tema grafico](TEMA_GRAFICO.md), non una copia di quelle regole nel codice. La separazione delle sorgenti non richiede di rigenerare o uniformare gli HTML non coinvolti nel lavoro.
