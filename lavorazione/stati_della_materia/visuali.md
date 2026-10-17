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

Gli otto file scelti sono stati acquisiti e ispezionati. Gli originali sorgente sono conservati separatamente in `risorse/originali/`; le anteprime a 960 px sono quelle indicate dall’utente e non sono state ricomprese. Per la viscosità è stato acquisito l’originale GIF per conservare il movimento. Peso totale dei file scelti: **4,601,347 byte**; incorporati in base64 circa **6,135,140 byte**, prima del testo e delle tre GIF del moto delle particelle. Gli originali ad alta risoluzione non vanno incorporati automaticamente nell’HTML.

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

## Materiali ancora mancanti per questo capitolo

Restano da scegliere e fornire le **tre GIF del moto delle particelle** (M6 solido, M7 liquido, M8 gas). La GIF della viscosità M11 svolge una funzione diversa e non le sostituisce. L’utente ha detto «Cerco io»: non proseguire autonomamente ricerche o scegliere le candidate storiche come se fossero approvate.

Il precedente errore HTTP 403 è superato per gli otto materiali qui acquisiti. Non dedurre da questo che le candidate GIF del moto siano state scaricate o scelte. Valutare il peso complessivo soltanto quando si conoscono i tre file effettivi; nessuna ottimizzazione è autorizzata implicitamente.

## Prossimo passaggio

Presentare il testo adattato ai materiali scelti e segnalare la risoluzione del vetro; attendere le tre GIF del modello particellare. La bozza resta distinta dall’HTML definitivo. Non modificare il sito o la pubblicazione.
