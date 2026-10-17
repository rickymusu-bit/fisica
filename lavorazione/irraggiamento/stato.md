# Stato corrente — Irraggiamento

Ultimo aggiornamento: 17 ottobre 2026, ore 14:07 (Europe/Rome).

## Risultato e fase

Capitolo italiano completato: [irraggiamento_it.html](../../irraggiamento_it.html), versione v3. Copia identica in [bozza.html](bozza.html); testo approvato in [bozza.md](bozza.md). Non è stata autorizzata l’unione in `main` o la pubblicazione del lavoro corrente. Le decisioni e le prove storiche sono recuperabili nella cronologia Git di questo stesso file.

Documenti correnti: [master](../../MASTER_PROMPT.md), [contenuti e stile](../../riferimenti/CONTENUTI_E_STILE.md), [tema grafico](../../riferimenti/TEMA_GRAFICO.md), [requisiti tecnici](../../riferimenti/REQUISITI_TECNICI.md). Il riordino delle istruzioni non modifica la versione del capitolo.

## Argomento e confini approvati

Irraggiamento termico per il biennio degli istituti tecnici, senza indicare classe o indirizzo nel testo visibile. Apertura sui rettili al Sole; propagazione nel vuoto, onda e spettro elettromagnetico, assorbimento/riflessione/trasmissione, emissione infrarossa e visibile, emissività e cubo di Leslie, corpo nero, legge di Stefan–Boltzmann, potenza emessa e potenza netta. Applicazioni: tostapane, termocamera, isolamento riflettente della sonda Deep Space 1, effetto serra e bilancio terrestre. Quindici domande finali, nessuna soluzione, nessun esercizio svolto o nuova simulazione interattiva.

## Approvazioni effettive

- Tema Mac approvato per home e capitoli; adattamento con Lexend, indice laterale nativo e due collegamenti «← Biblioteca». Campione linguistico approvato, distinto dal contenuto completo.
- Visuali scelte e fornite dall’utente. Bozza e revisioni seguite dal via esplicito «Vai pure». Dopo la pausa sul poster NASA e la correzione mostrata, l’utente ha dichiarato «Dopodiché puoi procedere».
- Foto della lava al posto del ferro incandescente; tostapane dall’allegato scelto. GIF della Terra nella sezione sull’effetto serra, con didascalia approvata e senza pulsanti di pausa o riavvio.
- Seconda foto del rettile per il bilancio radiativo: tre onde gialle entranti, lunghe, spesse e staccate dal corpo; più onde rosse uscenti distribuite sulla superficie. Nessuna etichetta accanto alle frecce, legenda separata. Esempio ipotetico scelto dall’utente: lucertola 30 °C e ambiente 20 °C, senza attribuire misure alla fotografia.
- Poster NASA con etichette italiane: riquadro esplicativo in alto a destra rimosso e nome «National Aeronautics and Space Administration» mantenuto in inglese.
- Comando immagini richiesto: «Ingrandisci l’immagine» nella vista normale e «Rimpicciolisci l’immagine» nella vista ingrandita, anche senza script. Navigazione precedente/successivo richiesta per tutti i capitoli, omettendo il tasto non disponibile ai due estremi. Irraggiamento è il nono e ultimo capitolo corrente.

## Materiali e sorgenti

Fonte unica dei dati dei visuali: [registro](risorse/registro-visuali.json), con originali, fonti, licenze e modifiche; copie inserite nell’HTML in [asset-finali.json](risorse/asset-finali.json). Originali e metadati conservati in `risorse/`.

Grafico teorico della potenza emessa: A = 1 m², ε = 1, σ = 5,67 · 10⁻⁸; intervallo 0–600 K, P(300 K) = 459,27 W e P(600 K) = 7.348,32 W, rapporto 16. SVG e sorgente Python in `risorse/`. Non sono misure sperimentali. Il bilancio del rettile distingue la radiazione solare dal modello semplificato dell’ambiente uniforme; le sole temperature non determinano il bilancio complessivo al Sole. I dati del poster NASA sono medie storiche riferite ai lavori del 2009.

Autore e licenza restano non identificati per GIF, tostapane e figura Concepts of Physics, come dichiarato nei crediti. L’utente ha risposto «no» alla richiesta di ulteriori informazioni su GIF e tostapane: non chiedere nuovamente gli stessi dati né inventare attribuzioni.

Generatore: [genera_capitolo.py](genera_capitolo.py). CSS e codice del pannello leggono le [sorgenti comuni del tema](../../tema/README.md) e vengono incorporati nell’HTML. La [navigazione comune](../../scripts/chapter_navigation.py) usa l’ordine di `index.html`. L’estrazione delle sorgenti ha conservato CSS e JavaScript identici e non richiede una nuova versione dell’HTML.

## Verifiche disponibili

- [browser.json](verifiche/browser.json): 1440/1024/768/390/320 px, nessun overflow di pagina o formule, immagini caricate, indice/focus/tastiera/Esc e ingrandimento funzionanti; nessuna richiesta esterna per le risorse o errore JavaScript. Indice e ingrandimento nativi a 390 px senza script; dopo la scelta della sezione si chiude con «Chiudi». Riduzione del movimento verificata.
- [zoom.json](verifiche/zoom.json): otto comandi, etichette visibili e nomi accessibili coerenti, apertura/chiusura a 1440/390 px con script e 320 px senza script.
- [navigazione-capitoli.json](../sito/navigazione-capitoli.json): nove capitoli a 390 e 1440 px senza script, collegamenti coerenti, attivazione da tastiera e aree di almeno 44 px.
- [integrita.json](verifiche/integrita.json): versione, peso, impronta e identità delle copie correnti. Immagini e contenuto degli HTML conservati durante il riordino della documentazione.

## Punti aperti e prossima operazione

Nessuna modifica didattica pendente. Attendere il riscontro sulla pagina completa. Ogni successiva modifica parte dai file correnti e dalle approvazioni sopra registrate; non ripetere la scelta di tema, font o visuali già accettati. Le informazioni di licenza mancanti restano un limite documentato. Pubblicazione e integrazione in `main` sono distinte dal salvataggio nel ramo di lavoro.
