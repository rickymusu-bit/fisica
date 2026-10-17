# Visuali — Stati della materia

## Scelte ricevute e acquisite

L’utente ha fornito otto collegamenti Wikimedia come scelta esplicita dei materiali. Non richiedono una nuova approvazione della scelta; nessun ritaglio, modifica delle immagini, rimozione di sfondo o compressione è stato eseguito. Le URL esatte fornite, le fonti, i metadati, gli hash e i percorsi degli originali sono nel [registro dei materiali scelti](risorse/materiali-scelti.json).

| ID | Materiale e fonte | File scelto acquisito | Attribuzione e licenza |
| --- | --- | --- | --- |
| C1 | [Copertina: ghiaccio in mare](https://commons.wikimedia.org/wiki/File:114_once_an_iceberg_now_a_Growler_and_a_scupture_V-P.jpg) | [copertina-ghiaccio.jpg](risorse/copertina-ghiaccio.jpg) | Virtual-Pano; CC BY-SA 4.0 |
| M1 | [Cristallo di bismuto](https://commons.wikimedia.org/wiki/File:Bismuth_crystal_macro.jpg) | [cristallo-bismuto.jpg](risorse/cristallo-bismuto.jpg) | Dschwen; CC BY 2.5 |
| M2 | [Oggetto di vetro](https://commons.wikimedia.org/wiki/File:Uranium-glass-dekor01.jpg) | [vetro-uranio.jpg](risorse/vetro-uranio.jpg) | State Office for Nuclear Safety (SÚJB), Czechia; CC BY-SA 3.0 |
| M10 | [Cristallino, policristallino e amorfo](https://commons.wikimedia.org/wiki/File:Crystalline_polycrystalline_amorphous2.svg) | [strutture-cristalline.png](risorse/strutture-cristalline.png) | Cristal ou amorphe.svg: Cdang; Everything else: Sbyrnes321; CC BY-SA 3.0 |
| M11 | [GIF sulla viscosità](https://commons.wikimedia.org/wiki/File:Demonstration_of_viscosity_of_liquids.gif) | [viscosita.gif](risorse/viscosita.gif) | Amethyst80; CC BY-SA 4.0 |
| M3 | [Olio versato sulla pizza](https://commons.wikimedia.org/wiki/File:Olive_oil_poured_over_a_pizza_in_Quebec_City.jpg) | [olio-versato.jpg](risorse/olio-versato.jpg) | Wilfredor; CC0 |
| M4 | [Dirigibile MZ-3A](https://commons.wikimedia.org/wiki/File:MZ-3A_blimp_at_NAS_Patuxent_River_in_May_2014.JPG) | [dirigibile.jpg](risorse/dirigibile.jpg) | U.S. Navy photo by John F. Williams; Public domain |
| M5 | [Scarica nell’argon](https://commons.wikimedia.org/wiki/File:Argon-glow.jpg) | [plasma-argon.jpg](risorse/plasma-argon.jpg) | Jurii; CC BY 3.0 |

Gli otto file scelti sono stati acquisiti e ispezionati. Gli originali sorgente sono conservati separatamente in `risorse/originali/`; le anteprime a 960 px sono quelle indicate dall’utente e non sono state ricomprese. Per la viscosità è stato acquisito l’originale GIF per conservare il movimento. Peso totale dei file scelti: **4,601,347 byte**; incorporati in base64 circa **6,135,140 byte**, prima del testo e del codice delle tre simulazioni microscopiche riutilizzate. Gli originali ad alta risoluzione non vanno incorporati automaticamente nell’HTML.

## Controlli e integrazione testuale

- **C1:** copertina esclusiva. L’apertura della bozza ora parte dal ghiaccio in mare, senza presentare il mare come acqua chimicamente pura.
- **M1:** identificato correttamente come bismuto; eliminati i riferimenti alla foto di quarzo. Licenza scelta fra quelle disponibili: CC BY 2.5.
- **M2:** la fonte originale è solo **172 × 339 px** e l’anteprima a 960 px è interpolata e sfocata. Per l’impaginazione usare `originali/m2.jpg` senza ingrandimento; segnalare la limitazione all’utente. Attribuzione ricavata dalla descrizione testuale della scheda: State Office for Nuclear Safety (SÚJB), Czechia. Non attribuire la fotografia al solo caricatore.
- **M10:** schema selezionato che sostituisce quello provvisorio precedentemente creato. Mostra tre pannelli, non due: cristallino, policristallino, amorfo. Inserimento diretto senza ridisegno o ritagli; testo e didascalia spiegano brevemente anche i grani del policristallino. L’originale SVG è conservato. Lo schema provvisorio rimane tra i materiali di lavorazione come riferimento, senza essere inserito insieme al nuovo.
- **M11:** originale GIF **690 × 388 px, 63 fotogrammi, 3.793.413 byte**. Ispezionati fotogrammi 0, 20, 40 e 62. È un’animazione illustrativa creata con Blender, non una ripresa sperimentale. A sinistra minore viscosità, a destra maggiore viscosità. La bozza non attribuisce ai due colori sostanze o valori numerici non documentati.
- **M3:** fotografia usata integralmente, con la pizza sullo sfondo; nessun ritaglio. Il getto d’olio resta riconoscibile.
- **M4:** dirigibile, non mongolfiera. Testo e didascalia corretti; i marchi presenti sul mezzo sono elementi della fotografia originale. La scheda e i metadati Commons identificano U.S. Navy / John F. Williams e pubblico dominio.
- **M5:** scarica nell’argon, non fulmine. Il testo distingue ionizzazione del gas ed emissione luminosa degli atomi eccitati; nessuna digressione sulla spettroscopia.

Le fonti/licenze sono state controllate sulle schede Commons e nei relativi metadati, non sulla sola licenza generale del sito. In fase HTML, collocare le attribuzioni richieste nei crediti collassabili e non nelle didascalie. Nessun credito incompleto va inventato.

## Simulazioni microscopiche conservate

Ultima richiesta esplicita: **«Mantieni le simulazioni degli stati microscopici»**. Conservare le tre animazioni locali della v8, con modello e comportamento esistenti:

| ID | Stato | Canvas della fonte |
| --- | --- | --- |
| M6 | Solido | `solidMotion`, 280 × 240 |
| M7 | Liquido | `liquidMotion`, 280 × 240 |
| M8 | Gas | `gasMotion`, 280 × 240 |

I tre canvas condividono lo script esistente, SHA-256 `8d2718622f3eb953ed226eb9ae63e079d5567a6f1a1c90d1fef67c2463e34a6c`. Mantenere gli identificativi e le dipendenze quando saranno collocati vicino ai rispettivi paragrafi. Nessuna nuova simulazione richiesta o programmata. La GIF M11 della viscosità resta distinta e si conserva.

La richiesta supera la precedente ricerca di GIF sostitutive: **non servono più le tre GIF del moto delle particelle**. Non ricercarle e non trattare le vecchie candidate come materiali da integrare. Per questo capitolo non restano nuovi file visuali da richiedere; permane il limite di risoluzione già segnalato per il vetro.

## Prossimo passaggio

La bozza ora riflette foto e schema scelti, GIF della viscosità e simulazioni microscopiche originali. Dopo la conferma del testo adattato, aggiornare la stima e raccogliere il via alla realizzazione HTML secondo B1.1–B2. Provare le animazioni nel nuovo impaginato quando sarà realizzato; nessuna prova browser nuova dichiarata in questo aggiornamento di lavorazione. Non modificare sito o pubblicazione.
