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
