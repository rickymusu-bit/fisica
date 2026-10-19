# Stato — La termodinamica e i sistemi termodinamici

Aggiornamento: 19 ottobre 2026 (Europe/Rome). Versione v6.

## Fase corrente

**HTML v1 completato e verificato, pronto per la revisione.** Ripresa richiesta dall’utente: «Finisci il lavoro sulla dispensa dei sistemi termodinamici», con precisazione «Su GitHub». La richiesta corrente autorizza il completamento nel ramo dedicato; non viene registrata come un’approvazione separata del testo né come autorizzazione a pubblicare. Ramo: `termodinamica/percorso-introduttivo`. Nessuna modifica a main, home o manifest.

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

File finale autonomo: `termodinamica_sistemi_it.html`, v1 · 19 ottobre 2026, 13,39 MB circa; copia corrente identica in `bozza.html`. Salvataggio sul ramo dedicato, senza unione né pubblicazione. Prossimo passaggio: revisione del risultato; per l’eventuale pubblicazione aggiornare catalogo, sequenza degli articoli e manifest solo dopo autorizzazione. Nessun via a main o alla pubblicazione ricevuto.
