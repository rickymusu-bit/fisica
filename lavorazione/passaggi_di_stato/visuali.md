# Visuali — Passaggi di stato

## Materiali nuovi scelti e acquisiti

| ID | Materiale | File e dimensioni | Attribuzione e licenza |
| --- | --- | --- | --- |
| C2 | [Molten Metal](https://www.flickr.com/photos/pamnani/36024324286/) | [copertina.jpg](risorse/copertina.jpg), 1024 × 768 px, 109.079 byte | Rajesh_India; [CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/) |
| A1 | [Michael Jordan, 1997](https://commons.wikimedia.org/wiki/File:Steve_Lipfosky_--_Michael_Jordan_(1997).jpg) | [sudore.jpg](risorse/sudore.jpg), 960 × 1410 px, 245.180 byte; originale 1200 × 1762 px conservato | Steve Lipofsky; [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Credito richiesto: **Lipofsky Basketballphoto.com** |
| A2 | [Unità pompa di calore](https://commons.wikimedia.org/wiki/File:Heat_pump_unit.webp) | [pompa-di-calore.webp](risorse/pompa-di-calore.webp), 960 × 1280 px, 311.006 byte; originale conservato | Wikideas1; CC0 |
| A3 | [Centrale nucleare PWR](https://commons.wikimedia.org/wiki/File:PWR_nuclear_power_plant_diagram.svg) | [centrale-nucleare.png](risorse/centrale-nucleare.png), 960 × 499 px, 122.978 byte; originale SVG conservato | Tennessee Valley Authority; pubblico dominio (PD-USGov-TVA) |
| E1 | [Scultura di ghiaccio](https://commons.wikimedia.org/wiki/File:Ai_Weiweis_Ice_Sculptures_in_Stockholm_2014.jpg) | [scultura-ghiaccio.jpg](risorse/scultura-ghiaccio.jpg), anteprima 960 × 1232 px; originale conservato | Frankie Fouganthin; CC BY-SA 4.0 |
| E2, foto esclusa | [Riferimento conservato: acqua che bolle](https://commons.wikimedia.org/wiki/File:Water_boiling_in_a_pot_on_a_stove.jpg) | [acqua-ebollizione.jpg](risorse/acqua-ebollizione.jpg), anteprima 960 × 966 px; originale 918 × 924 px conservato | Tomwsulcer; CC0 |

Tutte e sei scelte esplicitamente dall’utente, scaricate e ispezionate senza modifiche. [Registro con URL ricevute, fonti, condizioni e hash](risorse/materiali-scelti.json). Non richiedere una nuova approvazione delle stesse scelte.

La copertina mostra una colata di metallo fuso; non attribuire una composizione non documentata e non presentarla come fotografia di ghiaccio o condensa. La licenza è stata verificata sulla pagina Flickr risolta dal photo-ID: titolo, autore e link di licenza nel JSON-LD e nel collegamento rel=license. Il servizio di ricerca non legge la pagina, ma il recupero HTTP dall’ambiente è riuscito. Per la dispensa didattica a uso non commerciale conservare la foto intera, senza ritaglio, modifiche o testo sovrapposto; rispettare attribuzione e link alla licenza. Non attestare il diritto a un uso commerciale o a modifiche.

A1 mostra sudore visibile sulla pelle e sostiene l’applicazione sull’evaporazione; la foto non misura l’energia o il tasso di evaporazione. I marchi sportivi e il pallone sono parti della fotografia originale, non sovrapposizioni da rimuovere. La scheda Commons consente CC BY-SA 3.0 e richiede esplicitamente il credito «Lipofsky Basketballphoto.com»: registrarlo per i crediti collassabili. La didascalia resta fisica e descrittiva.

## Ultima modifica delle applicazioni

L’utente richiede «Niente schema frigorifero, spiega solo la pompa di calore» e fornisce A2 e A3. Rimossi dalla bozza il caso frigorifero e la relativa richiesta di schema. Testo e domanda finale 8 ora riguardano soltanto la pompa di calore in modalità riscaldamento. Spiegati refrigerante più freddo dell’aria esterna, evaporazione all’esterno, compressione, condensazione verso la casa ed espansione, senza aggiungere un nuovo schema o formule di rendimento.

A3 è lo schema illustrato di una centrale nucleare **PWR**, non un generico ciclo con ebollizione nel reattore. Il testo distingue acqua primaria pressurizzata che resta liquida, acqua secondaria che vaporizza e condensa, circuito di raffreddamento. “Generator” è il generatore elettrico, non il generatore di vapore; corrispondenze delle altre etichette inglesi nel testo. Si conserva la figura direttamente, senza traduzioni grafiche, ridisegni o ritagli non richiesti. Densa sul telefono: prevedere apertura ingrandita nell’HTML; non dichiarare già svolta una prova responsive sull’HTML futuro.

A2 e A3 acquisiti nelle versioni scelte e originali, decodificati/parsing SVG verificato, ispezionati. Fonti/licenze lette nelle schede Commons. Nessuna elaborazione dell’immagine effettuata. Questa richiesta supera la necessità precedente di uno schema del circuito frigorifero.

## Materiali già presenti

P1: [schema dei passaggi](risorse/schema-passaggi.md), triangolo e variante verticale, creato su richiesta. P2–P8: immagini e GIF pertinenti nella v8 da riutilizzare. P9: curva qualitativa dell’acqua da adattare alla lettura mobile, senza inventare dati sperimentali. Tabelle semantiche come nella bozza. Non riutilizzare la copertina nel testo.

## Unico esempio svolto: dal ghiaccio al vapore

Ultima richiesta dell’utente: un solo esempio che calcoli l’energia totale per vaporizzare completamente la statua partendo da ghiaccio a 0 °C. Il precedente esercizio separato sulla sola vaporizzazione è sostituito da questo percorso completo.

[Schema corrente E1](risorse/schema-esempio.svg): foto della scultura integrale con **sfondo conservato**, massa ipotizzata 500 kg, ghiaccio a 0 °C → acqua a 0 °C → acqua a 100 °C → vapore a 100 °C. Le tre frecce sono associate a Qf, Qr e Qv. Foto incorporata senza alterarne i byte, dati del modello distinti da misure della foto; attribuzione della foto Frankie Fouganthin / CC BY-SA 4.0.

Dati e risultati: Lf = 334.000 J/kg, c dell’acqua liquida ≈ 4180 J/(kg · K), Lv = 2.257.000 J/kg; pressione atmosferica ordinaria. Fusione 167 MJ, riscaldamento con ΔT = 100 K pari a 209 MJ, vaporizzazione 1128,5 MJ. **Totale 1504,5 MJ = 1.504.500.000 J**, senza dispersioni né energia assorbita dalle attrezzature. Non occorre riscaldare il ghiaccio inizialmente, perché è già a 0 °C; non si surriscalda il vapore finale.

I due schemi precedenti, `schema-fusione.svg` e `schema-vaporizzazione.svg`, sono sostituiti da quello unico; la cronologia Git li conserva. La foto della pentola resta esclusa, senza ricerche o immagini sostitutive. Non inserirla nei crediti degli elementi effettivamente utilizzati.

Tutti i visuali sono disponibili. Lo schema unico è stato ispezionato in anteprima nel browser a 600 px; non equivale alla verifica del futuro HTML definitivo. L’esempio spiega Qr = m · c · ΔT con grandezze, unità e significato prima dei calcoli e somma i tre contributi nella stessa unità. Domande finali 5 e 6 adeguate al percorso completo e all’errore di omettere il riscaldamento.

## GIF ridotte su richiesta esplicita

L’utente ha autorizzato entrambi i metodi su tutte e tre le GIF di questo capitolo. Copie in `risorse/ottimizzate/`, originali `v8-p2.gif`, `v8-p3.gif`, `v8-p4.gif` conservati e verificabili per SHA-256. Larghezza e altezza all’80% con arrotondamento al pixel; circa due terzi dei fotogrammi, ricampionati sull’intera durata. Primo e ultimo stato mantenuti; durata totale e ripetizione invariate. Palette adattiva a 256 colori dopo il ridimensionamento; non è una trasformazione senza perdita.

| GIF | Dimensioni nuove | Fotogrammi | Byte prima → dopo |
|---|---|---|---|
| Fusione dei cubetti | 224 × 360 | 49 → 33 | 3,389,354 → 2,022,673 |
| Evaporazione della goccia | 368 × 221 | 147 → 98 | 4,780,844 → 3,721,751 |
| Acqua in ebollizione | 320 × 240 | 77 → 52 | 5,659,517 → 3,168,285 |

Parametri, indici selezionati, durate, hash e controlli in [ottimizzazione-gif.json](risorse/ottimizzazione-gif.json). Le copie ridotte sono incorporate nell’HTML v10; nessun cambiamento alla GIF di viscosità o ai modelli particellari dell’altro capitolo.
