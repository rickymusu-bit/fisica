# Campione approvato: irraggiamento

Versione v2 · 17 ottobre 2026, ore 00:09 (Europe/Rome).

Estratti della prova approvata in chat, conservati come riferimento linguistico e per la spiegazione delle formule. Non costituiscono un capitolo HTML completo: copertina, immagini definitive, domande e impaginazione seguono il workflow del master. Gli estratti conservano la voce della prova e non impongono una scaletta identica per ogni argomento.

## Apertura e sviluppo del concetto

In una giornata di sole possiamo sentire il viso scaldarsi anche quando l’aria è fredda. Succede in montagna, magari con la neve intorno, ma anche davanti a una finestra: basta spostarsi dalla zona illuminata a quella in ombra per avvertire una differenza. Il Sole è sempre alla stessa distanza e la temperatura dell’aria è praticamente la stessa. Che cosa cambia, allora? E come fa il calore del Sole ad arrivare fino a noi?

Tra la Terra e il Sole ci sono circa 150 milioni di chilometri, quasi interamente occupati dallo spazio vuoto. Non esiste una successione di corpi a contatto che possa trasportare energia per conduzione, né una corrente d’aria che possa portarla fino a noi per convezione. Eppure quell’energia arriva: riscalda il terreno, gli oceani e gli oggetti lasciati all’aperto.

Il trasferimento avviene attraverso la **radiazione elettromagnetica**. Appartengono a questa famiglia la luce visibile, che permette di vedere ciò che ci circonda, e altre radiazioni che i nostri occhi non percepiscono, come l’infrarosso. Tutte possono trasportare energia e propagarsi anche nel vuoto. Quando un corpo assorbe la radiazione che lo raggiunge, riceve energia e può riscaldarsi. Questo modo di trasferire energia viene chiamato **irraggiamento**.

Didascalia della figura prevista: La radiazione solare raggiunge il corpo e lo riscalda anche quando l’aria circostante è fredda.

## Quanta energia emette un corpo?

Una stufa appena tiepida e una resistenza incandescente emettono entrambe radiazione, ma la quantità di energia che cedono ogni secondo è molto diversa. Da che cosa dipende questa differenza? La temperatura ha un ruolo decisivo, ma contano anche l’estensione e le caratteristiche della superficie.

La relazione che descrive questa emissione è la **legge di Stefan-Boltzmann**:

\[
P_{\mathrm{emessa}}=\varepsilon\cdot\sigma\cdot A\cdot T^4
\]

La **potenza emessa** \(P_{\mathrm{emessa}}\) indica quanta energia il corpo emette ogni secondo e si misura in watt. Nella formula, \(A\) è l’area della superficie che emette, espressa in metri quadrati, mentre \(T\) è la sua temperatura assoluta, **espressa in kelvin**.

Il simbolo \(\varepsilon\), che si legge “epsilon”, indica l’**emissività**: un numero compreso tra 0 e 1 che descrive quanto efficacemente una superficie emette radiazione termica. Una superficie con emissività vicina a 1 emette molto più di una superficie con emissività bassa, a parità di area e temperatura. Le superfici metalliche lucide, per esempio, hanno generalmente una bassa emissività.

Infine, \(\sigma\), che si legge “sigma”, è la costante di Stefan-Boltzmann:

\[
\sigma \approx 5{,}67\cdot10^{-8}\,
\mathrm{\frac{W}{m^2\cdot K^4}}
\]

La formula permette di capire che cosa succede cambiando una grandezza alla volta. Se raddoppiamo la superficie, mantenendo uguali temperatura ed emissività, la potenza emessa raddoppia. Un oggetto più esteso ha infatti una superficie maggiore da cui emettere radiazione.

L’effetto della temperatura è molto più marcato, perché nella formula compare alla quarta potenza. Se la temperatura assoluta raddoppia, la potenza emessa diventa:

\[
2^4=16
\]

cioè **sedici volte maggiore**. Passare da 300 K a 600 K significa quindi moltiplicare per sedici la potenza emessa, mantenendo uguali le altre condizioni. Raddoppiare una temperatura in gradi Celsius non produce lo stesso risultato: nella legge bisogna usare i kelvin.

Didascalia del grafico previsto: La potenza emessa cresce sempre più rapidamente all’aumentare della temperatura. Raddoppiando la temperatura in kelvin, diventa sedici volte maggiore.

## L’energia emessa non è tutta energia persa

Se il nostro corpo emette continuamente radiazione, perché non continua a raffreddarsi? Una parte della risposta è che riceve radiazione dall’ambiente. Per capire quanto perde per irraggiamento bisogna quindi confrontare l’energia emessa con quella assorbita.

Per un corpo circondato da un ambiente ampio a temperatura uniforme, la **potenza netta ceduta per irraggiamento** si può esprimere come:

\[
P_{\mathrm{netta}}
=
\varepsilon\cdot\sigma\cdot A\cdot
\left(T^4-T_{\mathrm{amb}}^4\right)
\]

Qui \(T_{\mathrm{amb}}\) è la temperatura dell’ambiente circostante, anch’essa in kelvin. La differenza tra le quarte potenze rappresenta il bilancio tra emissione e assorbimento.

Se il corpo è più caldo dell’ambiente, il risultato è positivo: cede più energia di quanta ne riceva per irraggiamento. Se le temperature sono uguali, il risultato è zero: gli scambi continuano, ma si compensano. Se l’ambiente è più caldo del corpo, il risultato è negativo: attraverso l’irraggiamento il corpo riceve più energia di quanta ne emetta.

Questo spiega perché una parete fredda possa farci sentire più freddo anche senza toccarla. Il nostro corpo emette radiazione verso la parete, ma ne riceve meno rispetto a quella proveniente da una parete più calda. La sensazione dipende quindi anche dalle superfici che ci circondano, oltre che dalla temperatura dell’aria.

