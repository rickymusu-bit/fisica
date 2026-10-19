# Stato — La termodinamica e i sistemi termodinamici

Aggiornamento: 19 ottobre 2026 (Europe/Rome). Versione v10.

## Fase corrente

**Revisione v5 salvata; sostituzione della foto della molla in attesa di un nuovo file.** Ripresa richiesta dall’utente: «Finisci il lavoro sulla dispensa dei sistemi termodinamici», con precisazione «Su GitHub». La richiesta corrente autorizza il completamento nel ramo dedicato; non viene registrata come un’approvazione separata del testo né come autorizzazione a pubblicare. Ramo: `termodinamica/percorso-introduttivo`. Nessuna modifica a main, home o manifest.

File finale: `termodinamica_sistemi_it.html`; tema autonomo v8 riutilizzato senza modifiche al CSS o ai comandi comuni. Bozza testuale v2: sola correzione dell’esempio della molla da compressione ad allungamento, coerente con le molle da trazione fotografate.

## Ambito e approvazioni effettive

L’utente ha approvato il primo articolo: che cosa studia la termodinamica; sistema, ambiente e confine; scambi di materia ed energia; sistemi aperti, chiusi e isolati. Temperatura, principio zero, scale, energia interna microscopica, calorimetria e dilatazione restano ai capitoli successivi.

Adottata la domanda introduttiva proposta e approvata dall’utente: «Che cos’hanno in comune un thermos e l’Universo?». Confermati bevanda come esempio iniziale, corpo umano e motore a combustione interna come sistemi aperti, molla come sistema chiuso. L’immagine di pile usate fornita per il punto 6 sostituisce il powerbank: la bozza adatta l’esempio a una singola pila integra nel modello macroscopico, senza presentare le pile nella raccolta come dispositivi visibilmente in funzione. Eliminato il confronto ridondante con la bottiglia, già approvato.

Ricerca Commons esplicitamente autorizzata, con preferenza per foto in contesti reali. L’utente ha poi scelto 1A e fornito sei file specifici; [visuali.md](visuali.md) v2 registra le scelte, autori e licenze. Non chiedere di confermare nuovamente queste immagini né sostituirle autonomamente. Le scelte specifiche prevalgono sulle proposte precedenti di sfondo neutro o molle montate.

## Riferimenti e checklist

Letti AGENTS.md, MASTER_PROMPT.md v60, STILE_DISPENSE.md v6 ed esempio_irraggiamento.md v2. Applicato B1.1: visuali concordate prima della bozza; stesura discorsiva nel repository, senza riportare il capitolo completo in chat.

- Italiano; nessun apparato di obiettivi, riepilogo o formule forzate.
- Sette immagini identificate, copertina non ripetuta all’interno; segnaposto con schema fisico per ogni esempio.
- Domanda iniziale, definizione di sistema/ambiente/confine, isolamento e confronto thermos–Universo, sistemi aperti e sistemi chiusi.
- Otto domande finali miste, riferite ai contenuti trattati, senza soluzioni.
- Due note brevi: Universo osservabile; condizioni del modello di pila integra.
- Nessuna simulazione, applicazione separata o esercizio numerico introdotti.
- In impaginazione applicare automaticamente il tema autonomo corrente, da leggere integralmente, e le regole specifiche di AGENTS su identità, crediti, navigazione e composizione mobile.

## Controlli scientifici della bozza

Thermos come approssimazione, non isolamento perfetto; Universo intero distinto da Universo osservabile, senza deduzioni sulla conservazione globale dell’energia. Chiuso non implica confine rigido né assenza di lavoro. Per il motore specificato combustione interna e sistema nel suo insieme, senza dedurne il funzionamento dalla sola foto. Pila come dispositivo integro nel consueto modello macroscopico con lavoro elettrico e senza flussi macroscopici di materia. Molla può immagazzinare/restituire energia meccanica senza dover essere contenitore. Nuvola del caffè descritta come goccioline, non vapore gassoso visibile.

Riferimenti consultati nei passaggi precedenti: DOE Fundamentals Handbook https://archives.standards.doxcelerate.com/documents/doe-hdbk-1012-1-92-thermodynamics-heat-transfer-and-fluid-flow-volume-1-of-3 ; NASA https://ntrs.nasa.gov/api/citations/19880002196/downloads/19880002196.pdf ; lavoro elettrico nei sistemi chiusi https://people.ohio.edu/urieli/thermo/Intro/Chapt.1_6/Chapter3a.html . Schede Commons delle immagini scelte consultate il 19 ottobre 2026.

## Realizzazione e materiali recuperati

Le sette foto sono state scaricate integralmente, ispezionate e incorporate senza compressione, conversione, ritaglio o sostituzione. Originali e metadati delle fonti in `risorse/`. Schemi SVG con foto, contorni del sistema e descrizioni degli scambi; medesima composizione su desktop e mobile e ingrandimento nativo. Nessuna simulazione aggiunta.

Attribuzione Springs 009.jpg: il registro pubblico dei caricamenti su en.wikipedia documenta Renard~enwiki (18 giugno 2005, caricamento originale, commento “This is a test to learn how to upload photos”) e Zeimusu (stessa data, “Crop time stamp”). Commons documenta il trasferimento di Qz10 e la migrazione a CC BY-SA 3.0. Conservati i crediti di tutti i contributori documentati, senza affermare che Qz10 sia il fotografo o dedurre un nome reale. La scheda Commons non esplicita un campo autore; la cronologia e la scheda sono conservate come prove di provenienza.

Registro unico aggiornato con `scripts/credits.py --sync`; snapshot della copia autonoma e OFL Lexend inclusi. Foto originali nelle figure SVG, senza duplicare i byte nel componente di ingrandimento. Script riproducibile: `realizza.py`; dopo la rigenerazione eseguire `--sync`.

## Verifiche e prossimo passo

Controllo scientifico: classificazioni, confini e flussi coerenti; molla da trazione; nessun risultato numerico inventato; nessun nuovo argomento. Controllati sette visuali, otto domande, ancore univoche e risolte e assenza di segnaposto. `scripts/credits.py --check`, build Pages e `git diff --check` superati. La build resta limitata agli articoli già ammessi: l’HTML nuovo non viene pubblicato automaticamente.

Verifica Chromium offline completata a 1280 e 390 px: nessun errore JavaScript, nessun overflow della pagina, indice con apertura/chiusura, richiamo/ritorno delle note, ingrandimento e scorrimento dei visuali, dialogo dei crediti, font OFL e pausa/ripresa logo funzionanti. Verificati ingrandimento e crediti anche senza JavaScript. Report: `verifiche-browser.json`; anteprime desktop/mobile nella stessa cartella. Ispezionati visivamente tutti e sei gli schemi. CSS del tema confrontato byte per byte; tutte le foto incorporate confrontate per SHA-256 con gli originali.

File corrente autonomo: `termodinamica_sistemi_it.html`, v5 · 19 ottobre 2026, 13,39 MB circa; copia corrente identica in `bozza.html`. Salvataggio sul ramo dedicato, senza unione né pubblicazione. Prossimo passaggio: revisione del risultato; per l’eventuale pubblicazione aggiornare catalogo, sequenza degli articoli e manifest solo dopo autorizzazione. Nessun via a main o alla pubblicazione ricevuto.

## Revisione v2 — immagini e frecce

Richiesta esplicita dell’utente del 19 ottobre 2026: nessun ingrandimento per immagini senza scritte rilevanti; frecce diverse dal nero, più corte e dentro i bordi. Scelto blu #0066b3 per aste e punte, lasciando neri i confini dei sistemi. Accorciate tutte e sei le frecce; quelle del caffè e della molla sono contenute nella rispettiva foto, comprese le punte.

Il generatore aggiunge l’ingrandimento soltanto quando lo schema contiene etichette didattiche. Le sei composizioni attuali le contengono e mantengono il comando; la foto di copertina ne è priva. Nessun ingrandimento aggiunto per le scritte commerciali presenti nelle foto. Tema comune e originali invariati. Aggiornati HTML corrente, copia di lavorazione e anteprime; verificati colore, coordinate rispetto ai bordi e uso offline a 1280/390 px. Salvataggio nella stessa PR #36, senza pubblicazione.

## Revisione v3 — spessore e lunghezza delle frecce

Richiesta esplicita: frecce un po’ più spesse; possono uscire dai bordi delle fotografie per chiarezza. Questa indicazione sostituisce il vincolo dei bordi della revisione v2. Aste blu portate da 3 a 5 unità SVG, punte da 24 a 28; ripristinata maggiore estensione delle frecce del caffè e della molla. Restano all’interno del riquadro complessivo dello schema e non coprono le etichette. Originali, testi e regola di ingrandimento invariati. Anteprime e verifiche offline desktop/mobile aggiornate.

## Revisione v4 — calore, evaporazione e forze

Richiesta esplicita: nel caffè frecce corte rosse e spesse attorno al tratteggio senza sovrapposizioni, per il trasferimento di energia termica; freccia blu per l’evaporazione; tutte le frecce dentro il bordo della figura; legenda o didascalia esplicativa. Nella molla frecce spesse verdi.

Realizzate 11 frecce rosse (#c62828, asta 6 e punta 18 unità SVG), orientate verso l’esterno e distanti dal contorno; eliminata la precedente freccia blu dell’energia. Conservata una sola freccia blu per l’acqua in uscita per evaporazione. Le due frecce della molla sono verdi (#16803c), con asta 6 e punta 28, e rappresentano le forze di allungamento. Didascalie aggiornate con i significati fisici; scritta sul confine abbassata per separarla dalle frecce inferiori.

Verifiche offline a 1280 e 390 px: conteggi e colori corretti, minima distanza delle frecce rosse dal tracciato tratteggiato circa 16,77 unità SVG, tutte le frecce dentro il riquadro complessivo. Nessun obbligo di restare dentro il rettangolo fotografico: il bordo richiesto è quello della figura. Report `verifiche-frecce.json`, anteprime aggiornate di caffè e molla. Testi teorici, originali e regola di ingrandimento invariati.

## Revisione v5 — didascalie e nuova foto della molla in attesa

L’utente ha richiesto di eliminare le scritte volanti dalle immagini, usare legenda/didascalia e sostituire la molla con Flickr 30257377 (Ian/morrfin), senza frecce. La pagina Flickr risulta license=0, “Tutti i diritti riservati”. Alla domanda sul permesso l’utente ha risposto esplicitamente: “No, userò un’altra foto”. Non inserire né caricare nel repository il file Flickr; nessuna autorizzazione ricevuta. Il download locale è rimasto fuori dal repository.

Completata la parte indipendente: eliminate tutte le scritte SVG e i relativi spazi vuoti; spiegazioni trasferite nelle didascalie. Eliminati gli ingrandimenti, non essendoci più testi da leggere nelle immagini. Nel caffè conservati contorno, frecce rosse del calore e freccia blu dell’evaporazione, con significato in didascalia. Rimosse dal motore le frecce prive di etichette; scambi spiegati in didascalia.

Per la molla, mantenuta temporaneamente la foto precedentemente scelta Springs 009.jpg, senza frecce, contorno o scritte; spiegazione nelle didascalie e nel testo esistente di allungamento/rilascio. NON considerare conclusa la sostituzione: attendere la nuova immagine dell’utente, verificarne il soggetto e adattare eventualmente l’esempio alla compressione.

Verificato offline a 1280/390 px: nessun testo SVG nei visuali, nessun tasto ingrandimento, molla senza frecce, immagini caricate, note/crediti funzionanti e assenza di overflow/errori. Foto Flickr assente da HTML, registro e file da caricare. Anteprime aggiornate, check crediti/build/diff superati. Prossimo passo: ricevere la nuova foto della molla; nessuna pubblicazione autorizzata.
