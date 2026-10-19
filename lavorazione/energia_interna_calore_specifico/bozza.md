# Energia interna, calore e calore specifico

Versione v2 · 19 ottobre 2026 (Europe/Rome).
Bozza testuale per revisione; i segnaposto indicano le visuali da inserire nell’HTML dopo la scelta dei file.

[COP-01 — Fotografia di una spiaggia estiva con mare e sabbia visibili, distinta dalla fotografia interna.]

Didascalia: Il mare e la spiaggia ricevono energia dal Sole durante il giorno, ma la loro temperatura non cambia nello stesso modo.

## Il mare dopo il tramonto

È una sera d’estate. Camminando sulla spiaggia, la sabbia sotto i piedi è ormai fredda; entrando in acqua, invece, il mare è ancora tiepido. Eppure il Sole è tramontato per entrambi. **Perché d’estate il mare resta tiepido di notte, anche quando la sabbia è fredda?**

Durante il giorno acqua e sabbia ricevono energia dal Sole. Dopo il tramonto continuano a cedere energia all’ambiente, ma la loro temperatura può diminuire in modo molto diverso. Per capire perché, dobbiamo distinguere tre idee che nel linguaggio comune tendiamo a sovrapporre: temperatura, energia interna e calore.

[FIG-01 — Fotografia della battigia di sera o di notte, con acqua e sabbia riconoscibili. Non ricavare temperature dalla fotografia; adattare la didascalia al soggetto scelto.]

Didascalia: La battigia dopo il tramonto. L’acqua può restare tiepida mentre lo strato superficiale della sabbia si è già raffreddato.

## L’energia che non vediamo

Anche quando l’acqua sembra ferma, le sue molecole sono in continuo movimento. Lo stesso vale per gli atomi e le molecole dei solidi: nella sabbia, le particelle che costituiscono i granelli vibrano attorno alle loro posizioni. Il movimento possiede energia cinetica. Anche le interazioni tra le particelle contribuiscono all’energia del materiale, attraverso un’energia potenziale legata alla loro disposizione e alle distanze reciproche.

L’insieme di queste energie microscopiche costituisce l’**energia interna**, indicata con \(U\) e misurata in joule, simbolo J. La parola “interna” ci aiuta a distinguerla dall’energia associata al movimento del corpo nel suo insieme o alla sua altezza rispetto al terreno. L’acqua ha energia interna anche quando il recipiente che la contiene è fermo.

[FIG-02 — Illustrazione microscopica scelta: moto delle particelle e loro interazioni, con eventuale confronto fra due temperature. La figura deve distinguere il modello di un solido da quello di un liquido, se li mostra entrambi.]

Didascalia: Nel modello microscopico le particelle si muovono e interagiscono. L’energia interna comprende i contributi di questi movimenti e delle interazioni.

La **temperatura** descrive lo stato termico del corpo ed è collegata al moto microscopico delle particelle. Non indica però quanta energia interna possiede complessivamente il corpo: conta anche quanta materia contiene. Due quantità diverse d’acqua alla stessa temperatura hanno la stessa indicazione sul termometro, ma quella maggiore contiene più particelle e ha un’energia interna maggiore.[^1]

## Il calore è energia che passa

Quando un corpo più caldo cede energia a uno più freddo a causa della differenza di temperatura, chiamiamo **calore** l’energia trasferita. Il simbolo è \(Q\) e l’unità è ancora il joule: stiamo sempre parlando di energia.

Questa distinzione cambia il modo di descrivere ciò che accade. L’acqua del mare possiede energia interna; mentre si raffredda può cedere energia sotto forma di calore. Dire che “contiene calore” confonde l’energia del sistema con un trasferimento tra sistema e ambiente. Anche il lavoro può modificare l’energia interna, come abbiamo visto parlando degli scambi energetici dei sistemi termodinamici.

Ma quanto deve cambiare l’energia di un corpo per farne aumentare la temperatura? Non basta sapere di quanti gradi vogliamo scaldarlo. Contano la massa e il materiale: è qui che acqua e sabbia cominciano a comportarsi diversamente.

## Quanta energia serve per un grado?

La **capacità termica**, indicata con \(C\), descrive quanta energia occorre trasferire come calore a un corpo per aumentarne la temperatura di un kelvin.[^2] Si misura in J/K: una capacità termica maggiore significa che serve più energia per ottenere lo stesso aumento di temperatura.

La relazione è:

\[
Q = C \cdot \Delta T
\]

La variazione di temperatura si calcola sottraendo la temperatura iniziale da quella finale:

\[
\Delta T = T_{\mathrm{f}} - T_{\mathrm{i}}
\]

Se il corpo ha capacità termica doppia, richiede il doppio del calore per lo stesso aumento di temperatura. Anche chiedere un aumento di temperatura doppio, per lo stesso corpo, richiede il doppio del calore. Un aumento di 1 K corrisponde a un aumento di 1 °C: per una differenza di temperatura i due valori numerici coincidono.

La capacità termica riguarda il corpo intero. Per confrontare i materiali dobbiamo invece riferirci alla stessa massa. Il **calore specifico**, indicato con \(c\) minuscola, è il calore necessario per aumentare di un kelvin la temperatura di un chilogrammo di materiale. Si misura in J/(kg · K).

[TAB-01 — Tabella HTML dei calori specifici di solidi, liquidi e gas, raggruppati per stato. Evidenziare la riga dell’acqua senza affidarsi soltanto al colore; stessa struttura su tutti i dispositivi.]

| Stato | Sostanza o materiale | Calore specifico \(c\), in J/(kg · K)[^4] |
| --- | --- | ---: |
| Solido | Rame | \(3{,}85 \cdot 10^2\) |
| Solido | Ferro | \(4{,}49 \cdot 10^2\) |
| Solido | Sabbia quarzosa[^3] | \(8{,}3 \cdot 10^2\) |
| Solido | Alluminio | \(8{,}97 \cdot 10^2\) |
| Liquido | Olio d’oliva | \(1{,}79 \cdot 10^3\) |
| Liquido | Alcol etilico (etanolo) | \(2{,}44 \cdot 10^3\) |
| **Liquido** | **Acqua pura, a 20 °C** | **\(4{,}18 \cdot 10^3\)** |
| Gas | Ossigeno | \(9{,}18 \cdot 10^2\) |
| Gas | Aria secca | \(1{,}01 \cdot 10^3\) |
| Gas | Azoto | \(1{,}04 \cdot 10^3\) |

Didascalia: Il confronto riguarda masse uguali. Tra i materiali riportati, l’acqua liquida richiede più energia per aumentare la temperatura dello stesso numero di gradi.

I valori sono arrotondati dai dati di [Engineering ToolBox, Specific Heat of Common Materials](https://www.engineeringtoolbox.com/specific-heat-capacity-d_391.html). La tabella mette a confronto materiali comuni: l’acqua risalta non soltanto rispetto ai metalli e alla sabbia, ma anche rispetto agli altri liquidi e ai gas elencati. Il valore dell’acqua si riferisce ad acqua pura a 20 °C, usata come riferimento senza attribuire lo stesso valore esatto a ogni acqua marina.

Da dove viene questa particolarità? Le molecole d’acqua si attraggono attraverso interazioni chiamate **legami a idrogeno**. Sono legami tra molecole vicine, diversi da quelli che tengono uniti idrogeno e ossigeno dentro ciascuna molecola. Nell’acqua liquida formano una rete in continuo riassetto.

Quando l’acqua si scalda, l’energia assorbita non aumenta soltanto il moto delle molecole: una parte modifica la rete delle loro interazioni. Per ottenere lo stesso aumento di temperatura occorre quindi trasferire molta energia. Questo contributo dei legami a idrogeno al calore specifico elevato è descritto anche in [OpenStax, Biology 2e, «Water»](https://openstax.org/books/biology-2e/pages/2-2-water). È il collegamento tra l’energia interna microscopica e la capacità del mare di attenuare i cambiamenti di temperatura.

La distinzione tra le due grandezze si esprime così:

\[
C = m \cdot c
\]

Qui \(m\) è la massa, espressa in chilogrammi. Aumentare la quantità dello stesso materiale aumenta la capacità termica del corpo, ma non il suo calore specifico. Quest’ultimo permette di riconoscere il diverso comportamento dei materiali anche quando li confrontiamo a parità di massa.

## La relazione tra calore e temperatura

Sostituendo \(C\) con \(m \cdot c\), otteniamo la **legge fondamentale della calorimetria**:

\[
Q = m \cdot c \cdot \Delta T
\]

Il calore \(Q\) è espresso in joule, la massa \(m\) in chilogrammi, il calore specifico \(c\) in J/(kg · K) e la variazione \(\Delta T\) in kelvin. La relazione lega ciò che viene trasferito alla risposta del corpo: quanto cambia la sua temperatura.[^2]

A parità di materiale e di aumento di temperatura, una massa doppia richiede il doppio del calore. Se invece la massa è la stessa, un materiale con calore specifico maggiore richiede più calore per scaldarsi dello stesso numero di gradi.

Possiamo leggere la relazione anche al contrario:

\[
\Delta T = \frac{Q}{m \cdot c}
\]

A parità di calore assorbito, una massa maggiore oppure un calore specifico maggiore producono un aumento di temperatura minore. Il grafico rende visibile questa differenza.

[GRA-01 — T in funzione di Q assorbito per masse uguali di acqua e sabbia quarzosa, con uguale temperatura iniziale. Due rette calcolate dal modello \(T = T_{\mathrm{i}} + \frac{Q}{m \cdot c}\), con i valori di c della tabella, non dati sperimentali. Specifiche proposte per l’HTML: m = 1 kg per ciascun materiale, T_i = 20 °C, Q da 0 a 1 kJ; asse orizzontale Q (kJ), asse verticale T (°C). Legenda testuale e composizione identica su mobile.]

Didascalia: Le due rette partono dalla stessa temperatura. A parità di calore assorbito, la sabbia quarzosa raggiunge una temperatura maggiore perché ha un calore specifico minore.

La formula descrive anche un raffreddamento. Se la temperatura finale è minore di quella iniziale, \(\Delta T\) è negativa e anche \(Q\) è negativo: il corpo cede calore. Se invece si scalda ricevendo calore, entrambe le grandezze sono positive. Il segno distingue il verso del trasferimento rispetto al corpo considerato.

## Perché il mare resta tiepido?

Torniamo alla spiaggia. L’elevato calore specifico dell’acqua significa che, a parità di massa ed energia ceduta, la sua temperatura diminuisce meno di quella della sabbia asciutta. Durante il giorno vale il ragionamento corrispondente: serve più energia per far aumentare della stessa quantità la temperatura dell’acqua.

Il mare, inoltre, non è soltanto una sottile superficie. Il movimento dell’acqua coinvolge strati diversi e distribuisce l’energia in una massa d’acqua più grande. La temperatura superficiale della sabbia, invece, può cambiare rapidamente senza che tutto il terreno sottostante raggiunga la stessa temperatura.

Ecco perché, dopo il tramonto, possiamo trovare ancora tiepido il mare mentre la sabbia si è raffreddata. Il calore specifico spiega una parte essenziale del contrasto; la massa coinvolta e il rimescolamento aiutano a capire perché il mare reale conserva così bene la temperatura. Non abbiamo dovuto supporre che acqua e spiaggia cedano esattamente la stessa energia: il confronto a parità di massa e calore serviva a isolare il ruolo del materiale.

## Domande di verifica

1. La sabbia si è raffreddata e il mare è ancora tiepido. Quale proprietà dell’acqua aiuta a spiegare la differenza? Quale altro aspetto del mare reale contribuisce al fenomeno?
2. Due quantità diverse d’acqua sono alla stessa temperatura. Hanno necessariamente la stessa energia interna? Motiva la risposta.
3. Vero o falso? «Un corpo caldo contiene molto calore». Riscrivi la frase usando correttamente “energia interna” e “calore”.
4. Raddoppiamo la massa di uno stesso materiale e vogliamo ottenere lo stesso aumento di temperatura. Il calore necessario si dimezza, resta uguale o raddoppia? Spiega usando la formula.
5. Dividendo una quantità d’acqua in due parti uguali, che cosa accade alla capacità termica di ciascuna parte rispetto a quella iniziale? E al calore specifico?
6. Nel grafico, quale materiale presenta la retta più inclinata? Che cosa significa questa inclinazione quando confrontiamo la stessa energia assorbita?
7. Osserva la tabella: per masse uguali e lo stesso aumento di temperatura, quale materiale richiede più calore? Confronta l’acqua con un solido, un altro liquido e un gas della tabella. Quale caratteristica delle interazioni tra le molecole d’acqua contribuisce a spiegare il suo valore elevato?
8. Un corpo cede calore e si raffredda. Quali sono i segni di \(Q\) e di \(\Delta T\)? Perché un valore negativo di \(Q\) non significa che il corpo possieda un’energia interna “sotto zero”?

## Note

[^1]: Nel confronto consideriamo acqua nello stesso stato e nelle stesse condizioni, con lo stesso riferimento per l’energia interna. Non si può ordinare l’energia interna di materiali diversi guardando soltanto la temperatura.

[^2]: Usiamo queste relazioni per riscaldamento o raffreddamento senza cambiamento di stato, con capacità termica e calore specifico approssimativamente costanti nell’intervallo considerato e nelle condizioni per cui è definito il calore specifico usato. Nel confronto tra acqua e sabbia trascuriamo il contributo del lavoro.

[^3]: La tabella della fonte riporta “Sand, quartz” senza precisare temperatura di riferimento o contenuto d’acqua. Il valore è indicativo per quel materiale, non una misura della spiaggia fotografata né una costante di ogni sabbia. Composizione e umidità ne modificano il comportamento.


[^4]: I valori della tabella sono a pressione costante. Per i gas questa condizione è essenziale: scaldare un gas mantenendone fisso il volume richiede un diverso calore specifico. Le temperature di riferimento non sono precisate dalla fonte per tutte le voci; i valori servono a un confronto indicativo.
