# Le cifre significative

Versione v2 — 23 ottobre 2026 (Europe/Rome). Bozza per revisione; non è ancora l’HTML del capitolo.

[COP-01 — Fotografia dello strumento di misura egizio scelta dall’utente: risorse/copertina-egizia.jpg. Immagine intera, senza zoom, non ripetuta nel corpo.]

Didascalia: Strumento di misura egizio con suddivisioni incise lungo l’asta.

## Uno zero può cambiare una misura?

Su un foglio di laboratorio trovi due lunghezze: 12,4 cm e 12,40 cm. Come numeri sono uguali; una calcolatrice può perfino eliminare lo zero finale senza cambiare il valore. Nella scrittura di una misura, però, quello zero comunica qualcosa. Perché qualcuno ha scelto di conservarlo?

La prima scrittura arriva ai decimi di centimetro; la seconda conserva anche i centesimi. Le **cifre significative** sono le cifre con cui comunichiamo il valore misurato e il dettaglio con cui lo riportiamo. In 12,4 sono tre, mentre in 12,40 sono quattro: lo zero finale fa parte dell’informazione. Aggiungerne altri senza che la misura li giustifichi farebbe apparire il risultato più dettagliato di quanto sia.

[FIG-01 — Riutilizzare il confronto originale 12,4 cm / 12,40 cm, con tre e quattro cifre significative e indicazione di decimi e centesimi.]

Didascalia: Lo zero finale non cambia il valore numerico, ma conserva il posto dei centesimi di centimetro.

L’ultima cifra riportata non è una promessa di esattezza assoluta: nelle misure è già coinvolta nell’incertezza. Il numero di cifre, da solo, non basta per sapere quanto un risultato sia vicino al valore della grandezza. Qui ci interessa come scriverlo senza aggiungere informazioni che non possediamo.[1]

## Quali zeri contano?

Le cifre diverse da zero sono sempre significative. Gli zeri iniziali, prima della prima cifra diversa da zero, servono invece a collocare la virgola: in 0,00082 m contano soltanto 8 e 2. Gli zeri compresi fra cifre significative contano, così come quelli finali dopo la virgola. Ecco perché 0,00450 m ha tre cifre significative: 4, 5 e lo zero finale.

[TAB-01 — Riutilizzare la tabella originale dei sette casi.]

| Misura | Cifre significative | Perché |
| --- | --- | --- |
| 0,00082 m | 2 | Contano 8 e 2; gli zeri iniziali fissano la posizione della virgola. |
| 0,00450 m | 3 | Contano 4, 5 e lo zero finale. |
| 10,03 s | 4 | I due zeri interni sono significativi. |
| 2,400 kg | 4 | I due zeri finali dopo la virgola sono significativi. |
| 120,0 cm | 4 | La scrittura conserva la misura fino ai decimi di centimetro. |
| 1,2 · 10³ m | 2 | Si contano soltanto le cifre del coefficiente 1,2. |
| 1,200 · 10³ m | 4 | Il coefficiente 1,200 conserva quattro cifre. |

Didascalia: La posizione dello zero nella scrittura determina se porta informazione sulla misura.

Il segno, la virgola, l’unità e l’esponente della potenza di dieci non entrano nel conteggio. Non bisogna neppure confondere le cifre significative con le **cifre decimali**, cioè quelle dopo la virgola. In 0,00450 ci sono cinque cifre decimali e tre significative; in 120,0 c’è una sola cifra decimale, ma quattro significative.

Gli interi con zeri finali possono lasciare un dubbio. Se leggi soltanto «1200 m», non sai se chi ha scritto la misura volesse conservare due, tre o quattro cifre significative. La notazione scientifica, già incontrata, elimina l’ambiguità:

\[
1{,}2\cdot10^3\,\mathrm{m}\quad\text{ha 2 cifre significative}
\]

\[
1{,}20\cdot10^3\,\mathrm{m}\quad\text{ha 3 cifre significative}
\]

\[
1{,}200\cdot10^3\,\mathrm{m}\quad\text{ha 4 cifre significative}
\]

La potenza è la stessa e il valore numerico non cambia. A cambiare è il numero di cifre conservate nel coefficiente.

## Arrotondare senza troncare

Una calcolatrice può mostrare più cifre di quelle che vogliamo riportare. Per ridurle usiamo l’**arrotondamento**, scegliendo il valore più vicino alla posizione che abbiamo deciso di conservare. Prima si stabilisce se la richiesta riguarda il numero di cifre significative oppure una posizione decimale: non sono istruzioni equivalenti.

La procedura è questa:

1. Individua l’ultima cifra da conservare, contando dalla prima cifra significativa oppure arrivando alla posizione decimale richiesta.
2. Guarda la prima cifra che eliminerai. Se è minore di 5, lascia invariata l’ultima cifra conservata; se è 5 o maggiore, aumentala di uno, gestendo l’eventuale riporto.[2]
3. Elimina le cifre successive e scrivi il risultato con gli zeri necessari a dichiarare la precisione richiesta. Quando gli zeri finali di un intero sarebbero ambigui, usa la notazione scientifica.
4. Controlla che unità e ordine di grandezza siano rimasti coerenti con il valore iniziale.

[TAB-02 — Riutilizzare i quattro casi originali di arrotondamento.]

| Valore di partenza | Richiesta | Risultato |
| --- | --- | --- |
| 2,343 m | 3 cifre significative | 2,34 m |
| 2,345 m | 3 cifre significative | 2,35 m |
| 0,004567 m | 2 cifre significative | 0,0046 m |
| 9,96 s | 2 cifre significative | 1,0 · 10¹ s |

Didascalia: Nell’ultima riga il riporto cambia la scrittura del numero; il coefficiente 1,0 conserva le due cifre richieste.

Arrotondare non significa semplicemente tagliare le cifre in eccesso. Tagliandole senza modificare l’ultima rimasta si esegue un **troncamento**. Nella seconda riga, il troncamento a tre cifre significative darebbe 2,34 m; l’arrotondamento dà invece 2,35 m, perché la prima cifra scartata è 5.

## Due regole per i calcoli

Quando un risultato deriva da misure, le cifre mostrate dalla calcolatrice non sono tutte automaticamente giustificate. Il calcolo combina dati che possono essere riportati con dettagli diversi. Per decidere come scrivere il risultato usiamo due criteri, a seconda dell’operazione.[3]

[TAB-03 — Riutilizzare la tabella originale che distingue le operazioni.]

| Operazione | Che cosa controllare | Come scrivere il risultato |
| --- | --- | --- |
| Somma o differenza | La posizione decimale meno precisa, dopo aver espresso i dati nella stessa unità. | Arrotonda a quella posizione: per esempio ai decimi se un dato arriva solo ai decimi. |
| Prodotto o divisione | Il dato misurato con meno cifre significative. | Il risultato deve avere quel numero di cifre significative. |

Didascalia: Nelle somme conta la posizione delle cifre; nei prodotti conta quante cifre significative hanno i dati misurati.

Per una somma o una differenza bisogna quindi confrontare le posizioni dopo aver uniformato le unità. Nei prodotti e nelle divisioni si confronta invece il numero di cifre significative dei dati. Contare soltanto i decimali in ogni operazione porterebbe a risultati incoerenti, soprattutto con numeri molto piccoli o espressi in notazione scientifica.

Puoi applicare il metodo in quattro passi:

1. Scrivi i dati con le unità e rendile coerenti con il calcolo.
2. Individua l’operazione e il dato che limita il dettaglio del risultato, usando il criterio adatto della tabella.
3. Esegui i calcoli conservando le cifre disponibili nei passaggi intermedi; annota il limite di precisione senza applicare subito l’arrotondamento.
4. Arrotonda alla fine e controlla che la scrittura dichiari le cifre richieste, senza cambiare il significato fisico del risultato.

## Esempio svolto: le stesse misure, operazioni diverse

Consideriamo la base rettangolare di una cassa. I lati hanno lunghezze assegnate **a = 2,34 m** e **b = 1,2 m**: sono dati illustrativi, non letture ricavate dall’immagine. Con le stesse due misure calcoliamo somma, differenza, area, rapporto e perimetro, osservando quali cifre conservare.

[FIG-02 — Schema della cassa con la nuova illustrazione generata su richiesta, risorse/cassa-generata.png. Aggiungere quote a = 2,34 m e b = 1,2 m sui due lati adiacenti della base, prima dei calcoli. Dati illustrativi; non è una fotografia di misure reali.]

Didascalia: I due lati della base sono i dati usati nei calcoli. Dimensioni illustrative; disegno non in scala.

### Somma e differenza

La lunghezza a arriva ai centesimi di metro; b soltanto ai decimi. Somma e differenza si scrivono quindi fino ai decimi:

\[
a+b=2{,}34\,\mathrm{m}+1{,}2\,\mathrm{m}=3{,}54\,\mathrm{m}\approx3{,}5\,\mathrm{m}
\]

\[
a-b=2{,}34\,\mathrm{m}-1{,}2\,\mathrm{m}=1{,}14\,\mathrm{m}\approx1{,}1\,\mathrm{m}
\]

La somma equivale alla lunghezza complessiva dei due lati se li percorriamo uno dopo l’altro: circa 3,5 m. La differenza dice quanto il lato maggiore supera il minore, circa 1,1 m, poco meno della lunghezza di b. I centesimi ottenuti nell’operazione aritmetica non vanno conservati come se entrambi i dati li giustificassero.

### Area e rapporto

L’area A della base rettangolare è il prodotto dei lati:

\[
A=a\cdot b
\]

\[
A=2{,}34\,\mathrm{m}\cdot1{,}2\,\mathrm{m}=2{,}808\,\mathrm{m^2}\approx2{,}8\,\mathrm{m^2}
\]

Il lato a ha tre cifre significative, b ne ha due: il prodotto va riportato con due. L’area corrisponde a circa 2,8 superfici da 1 m²; il numero 2,808 è utile nel calcolo, ma scriverlo come risultato finale attribuirebbe ai dati un dettaglio che non hanno.

Anche il rapporto r fra i lati usa il criterio delle due cifre significative:

\[
r=\frac{a}{b}
\]

\[
r=\frac{2{,}34\,\mathrm{m}}{1{,}2\,\mathrm{m}}=1{,}95\approx2{,}0
\]

Le unità si semplificano perché confrontiamo lunghezze espresse nella stessa unità. Il risultato non ha unità e indica che a è circa il doppio di b. Scrivere 2,0 conserva due cifre significative; scrivere soltanto 2 ne conserverebbe una.

### Il perimetro e i passaggi intermedi

Il perimetro P comprende due lati di lunghezza a e due di lunghezza b:

\[
P=2\cdot(a+b)
\]

Il fattore 2 conta le due coppie di lati: è un numero esatto, quindi non riduce le cifre significative del risultato. Usiamo la somma non ancora arrotondata, ricordando che la sua posizione limite resta quella dei decimi di metro:

\[
P=2\cdot3{,}54\,\mathrm{m}=7{,}08\,\mathrm{m}\approx7{,}1\,\mathrm{m}
\]

Il perimetro è circa il doppio della lunghezza complessiva dei due lati adiacenti. Se avessimo arrotondato prima 3,54 m a 3,5 m, avremmo ottenuto 7,0 m: il risultato finale sarebbe cambiato di 0,1 m, cioè 10 cm. Conservare cifre nei passaggi intermedi evita di introdurre questo cambiamento; non significa che quelle cifre diventino tutte significative nel risultato finale.

## Cambiare unità conserva l’informazione

Il fattore esatto 2 del perimetro non deriva da una misura. Lo stesso accade con i conteggi esatti e con le conversioni definite fra unità: la relazione 1 m = 100 cm è esatta. Il numero 100, in questo contesto, non è una misura con un numero ambiguo di cifre significative e non limita il risultato della conversione.

Riprendiamo la lunghezza iniziale e scriviamola in metri:

\[
12{,}40\,\mathrm{cm}=12{,}40\cdot10^{-2}\,\mathrm{m}=0{,}1240\,\mathrm{m}
\]

Il valore in metri ha ancora quattro cifre significative. Lo zero iniziale serve a collocare la virgola; quello finale conserva il dettaglio della misura. Anche la posizione dell’ultima cifra rimane equivalente: 0,01 cm corrisponde a 0,0001 m. Il cambio di unità modifica il numero con cui esprimiamo la lunghezza, senza aggiungere o togliere informazione.

Una costante inserita nel calcolo con un valore approssimato va invece trattata in base alle cifre disponibili. Il punto è distinguere un fattore esatto da un dato approssimato: il loro aspetto sulla pagina può essere simile, ma il ruolo nel calcolo è diverso.

## Domande di verifica

1. Quante cifre significative hanno 0,00450 m, 10,03 s e 1,200 · 10³ m? Spiega il ruolo degli zeri.
2. Perché «1200 m» è ambiguo? Riscrivilo dichiarando tre cifre significative.
3. Arrotonda 0,006783 kg a tre cifre significative e spiega quale cifra hai osservato.
4. Quale criterio cambia passando da una somma a un prodotto di misure?
5. Perché il fattore 100 nella conversione da metri a centimetri non limita le cifre significative?
6. Nel calcolo del perimetro, perché conviene mantenere 3,54 m fino all’ultimo passaggio?
7. Vero o falso? «0,00450 ha cinque cifre significative perché ha cinque cifre dopo la virgola». Motiva la risposta.
8. Un compagno scrive 0,124 m come conversione di 12,40 cm. Il valore numerico è equivalente, ma quale informazione della scrittura iniziale ha perso?
9. Devi riportare 2,345 m con tre cifre significative. Confronta il risultato dell’arrotondamento con quello del troncamento e spiega la differenza.
10. Una calcolatrice mostra 2,808 m² dopo aver moltiplicato 2,34 m per 1,2 m. Scegli il risultato coerente fra 2,808 m², 2,81 m² e 2,8 m², motivando la scelta.

## Note

[1] Il conteggio delle cifre significative non determina da solo l’incertezza di una misura e non garantisce l’assenza di errori sistematici. Quando l’incertezza è indicata esplicitamente, valore e arrotondamento devono essere coerenti con essa.

[2] Qui adottiamo la convenzione scolastica che aumenta l’ultima cifra conservata quando la prima scartata è 5 o maggiore. Per valori negativi si arrotonda il valore assoluto e poi si conserva il segno.

[3] Le due regole sono convenzioni operative utili quando non si esegue un calcolo esplicito dell’incertezza; non lo sostituiscono.

---

## Servizio editoriale — fonti, risorse e controlli

Sezione non destinata al contenuto didattico pubblico. Note e crediti seguiranno le componenti canoniche del tema Stringhe nella fase HTML.

- Fonte di partenza: sistema_internazionale_notazione_it.html v12, sezione #cifre-significative, blob Git 61a32e96afce2136af8669b1544a02e9d751018d. Tre tabelle, confronto delle scritture, schema della cassa e tutti i calcoli pertinenti conservati. Quesiti originali 8–13 ripresi nelle domande 1–6; aggiunte quattro domande di ragionamento, senza soluzioni.
- COP-01: immagine scelta dall’utente, [Egyptian measuring tool](https://commons.wikimedia.org/wiki/File:Egyptian_measuring_tool.jpg), autore Uriah Welcome, [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/), provenienza originale [Flickr](https://www.flickr.com/photos/89689539@N00/3480531121). Miniatura scelta 960 per 540 px scaricata intera, senza ritaglio o alterazioni locali; risorse/copertina-fonte.json contiene URL, hash e scelta. Nessuna datazione, precisione o incertezza dedotta dalla sola fotografia. Crediti da associare al nuovo documento nel registro unico durante la realizzazione HTML.
- FIG-01: confronto numerico SVG già presente nel sorgente; riuso della composizione, senza immagine esterna. Provenienza storica documentata dal repository.
- FIG-02: nuova illustrazione della cassa generata con ChatGPT su richiesta esplicita dell’utente, con sfondo trasparente. Originale conservato in risorse/cassa-generata.png, provenienza in risorse/cassa-fonte.json; quote geometriche aggiunte in risorse/schema-cassa.svg. Sostituisce il PNG storico di provenienza non documentata, che non viene riprodotto nel nuovo capitolo. Dati illustrativi, disegno non in scala. Nessuna licenza di terzi dedotta.
- TAB-01–03: sette righe di conteggio, quattro di arrotondamento, due criteri per operazioni; valori originali conservati. Notazione resa coerente col capitolo precedente soltanto dove utile. Le frazioni delle formule andranno renderizzate con linea orizzontale, senza barre di divisione nei calcoli.
- Controlli editoriali: apertura concreta, simboli A/r/P definiti, formule generali esplicite, due procedure numerate, dati illustrativi dichiarati, interpretazioni dei risultati e dieci quesiti. Nessuna simulazione o video; strumenti e incertezza quantitativa rinviati ai capitoli successivi.
- Stato: testo v1 approvato con «Approvo tutto»; immagine della cassa generata e mostrata su richiesta, poi «Ok procedi» autorizza schema quotato e realizzazione HTML. La v2 aggiorna soltanto i segnaposto e la provenienza della cassa. Anteprima HTML corrente da approvare prima della pubblicazione.
