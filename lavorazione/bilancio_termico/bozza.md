# Il bilancio termico

<!-- Bozza v4 · 19 ottobre 2026, ore 21:48 (Europe/Rome). Testo da approvare; non è l’HTML finale. -->

[IMMAGINE COP-01 — Scena della colazione nel dipinto Le Déjeuner di François Boucher; risorse/copertina-boucher.jpg. Solo copertina, non ripetuta nel corpo.]

Didascalia: Una scena di colazione, con tazze e recipienti sulla tavola. Quando hanno temperature diverse, bevande e recipienti possono scambiare energia.

## Quanto si raffredda il caffè?

Il caffè è appena pronto e scotta. Aggiungiamo del latte freddo, mescoliamo e la bevanda diventa più tiepida. Ma quanto si raffredda il caffè quando aggiungiamo il latte? La risposta cambia se ne versiamo soltanto un goccio oppure una quantità paragonabile a quella del caffè.

[IMMAGINE FIG-03 — Latte versato nel caffè; risorse/versamento-rawpixel.jpg. Fotografia interna distinta dalla copertina.]

Didascalia: Durante il mescolamento il latte entra nel caffè; se le temperature iniziali sono diverse, le due bevande scambiano energia.

Per prevedere la temperatura finale dobbiamo seguire l’energia. Durante il mescolamento il caffè, inizialmente più caldo, cede energia al latte, che si riscalda. Dopo aver mescolato e raggiunto l’**equilibrio termico**, la bevanda ha una temperatura uniforme: la chiamiamo \(T_{\mathrm{eq}}\).[^1]

[IMMAGINE FIG-01 — La tazza di caffè prima del mescolamento; risorse/caffe.jpg. La fotografia illustra il soggetto, senza dati di temperatura sovrapposti.]

Didascalia: Il caffè è la parte inizialmente più calda del sistema che stiamo considerando.

Possiamo essere tentati di fare la media delle due temperature iniziali. Ma questa idea non tiene conto delle quantità mescolate: un goccio di latte non può avere lo stesso effetto di una massa di latte molto maggiore. Per trovare la temperatura finale serve una regola che tenga insieme energia, massa e variazione di temperatura.

## L’energia che esce e quella che entra

Consideriamo dapprima soltanto caffè e latte. L’energia che il caffè cede viene assorbita dal latte: il trasferimento cambia la distribuzione dell’energia fra le due parti, senza cambiarne il totale.[^2] Questa contabilità è il **bilancio termico**.

Per scriverla in modo compatto assegniamo un segno al calore scambiato \(Q\). Per un corpo che assorbe energia, \(Q\) è positivo; per un corpo che cede energia, \(Q\) è negativo. Nel nostro caso, quindi, il calore scambiato dal caffè è negativo e quello scambiato dal latte è positivo. Il bilancio si scrive:

\[
Q_{\mathrm{caffè}}+Q_{\mathrm{latte}}=0
\]

Lo zero non significa che non sia passata energia. Significa che i due trasferimenti hanno lo stesso valore assoluto e segni opposti: tutta l’energia uscita dal caffè è entrata nel latte. Entrambi i calori si misurano in joule, simbolo J.

[IMMAGINE FIG-02 — Il bicchiere di latte prima del mescolamento; risorse/latte.jpg. Nessun valore di massa o temperatura ricavato dalla fotografia.]

Didascalia: Il latte inizialmente più freddo assorbe energia dal caffè e si riscalda.

Per collegare questo scambio alle temperature riprendiamo la relazione \(Q=m\cdot c\cdot\Delta T\). Indichiamo con \(m_{\mathrm{caffè}}\) e \(m_{\mathrm{latte}}\) le masse delle due bevande, con \(T_{\mathrm{caffè}}\) e \(T_{\mathrm{latte}}\) le loro temperature iniziali. Usiamo per entrambe lo stesso calore specifico \(c\), approssimato a quello dell’acqua.[^1] I due calori diventano:

\[
Q_{\mathrm{caffè}}=m_{\mathrm{caffè}}\cdot c\cdot
\left(T_{\mathrm{eq}}-T_{\mathrm{caffè}}\right)
\]

\[
Q_{\mathrm{latte}}=m_{\mathrm{latte}}\cdot c\cdot
\left(T_{\mathrm{eq}}-T_{\mathrm{latte}}\right)
\]

Le differenze sono sempre temperatura finale meno temperatura iniziale. Nel caffè questa differenza è negativa, perché si raffredda; nel latte è positiva, perché si riscalda. I segni richiesti dal bilancio compaiono così direttamente nelle formule.

Usando masse in kg, calore specifico in J/(kg · K) e differenze di temperatura in K otteniamo i calori in J. Possiamo calcolare le differenze anche sottraendo temperature espresse in gradi Celsius: una variazione di 1 °C ha la stessa ampiezza di una variazione di 1 K.

## Una temperatura che tiene conto delle masse

Inseriamo le due espressioni nel bilancio. Il calore specifico comune compare in entrambi i termini e si semplifica. Rimane:

\[
m_{\mathrm{caffè}}\cdot\left(T_{\mathrm{eq}}-T_{\mathrm{caffè}}\right)
+
m_{\mathrm{latte}}\cdot\left(T_{\mathrm{eq}}-T_{\mathrm{latte}}\right)=0
\]

Raccogliendo i termini che contengono \(T_{\mathrm{eq}}\) e isolando questa temperatura, troviamo:

\[
T_{\mathrm{eq}}=
\frac{
m_{\mathrm{caffè}}\cdot T_{\mathrm{caffè}}
+
m_{\mathrm{latte}}\cdot T_{\mathrm{latte}}
}{
m_{\mathrm{caffè}}+m_{\mathrm{latte}}
}
\]

È una **media pesata**: ciascuna temperatura iniziale conta in proporzione alla massa della bevanda. Nella formula possiamo usare temperature tutte in gradi Celsius, ottenendo il risultato in gradi Celsius; oppure tutte in kelvin, ottenendolo in kelvin. Non mescoliamo le due scale nello stesso calcolo.

A parità di temperature iniziali e di massa del caffè, aggiungere più latte freddo porta la temperatura finale più vicino a quella iniziale del latte. Se invece le masse sono uguali, le due temperature hanno lo stesso peso e la formula diventa la media aritmetica. La temperatura finale resta compresa fra le due temperature iniziali.

Il bilancio chiarisce anche un’altra differenza: scambiare la stessa quantità di energia non significa cambiare temperatura dello stesso numero di gradi. Con il calore specifico comune, una massa maggiore cambia temperatura di meno. Più in generale, quando i calori specifici sono diversi, a pesare nella media sono le **capacità termiche** \(m\cdot c\) delle due parti.

## Anche la tazza partecipa

Finora abbiamo seguito soltanto le due bevande. La tazza, però, può assorbire o cedere energia a sua volta. Se inizialmente è più fredda della temperatura finale prevista dal primo modello, assorbe una parte dell’energia e abbassa la temperatura di equilibrio. Se è più calda, può invece contribuire a riscaldare la miscela.

[IMMAGINE FIG-01, RIUSO INTERNO — Richiamo alla stessa fotografia della tazza di caffè, accanto alla spiegazione del recipiente. Non riutilizzare COP-01.]

Didascalia: Anche la tazza può scambiare energia con la bevanda; il suo contributo dipende dalla capacità termica e dalla temperatura iniziale.

Indichiamo con \(C_{\mathrm{tazza}}\) la capacità termica della tazza, misurata in J/K: è l’energia necessaria per aumentarne di un kelvin la temperatura. Se la sua temperatura iniziale è \(T_{\mathrm{tazza}}\), il calore che scambia raggiungendo la stessa temperatura finale della bevanda è:

\[
Q_{\mathrm{tazza}}=
C_{\mathrm{tazza}}\cdot
\left(T_{\mathrm{eq}}-T_{\mathrm{tazza}}\right)
\]

Ora scegliamo come sistema caffè, latte e tazza insieme. Il bilancio deve comprendere tutte e tre le parti:

\[
Q_{\mathrm{caffè}}+Q_{\mathrm{latte}}+Q_{\mathrm{tazza}}=0
\]

La regola resta la stessa: sommare i calori scambiati, ciascuno con il proprio segno. Cambia il numero di corpi di cui seguiamo l’energia. L’equazione permette di trovare la temperatura finale anche quando il contributo del recipiente non è trascurabile.[^2]

## Domande di verifica

1. Il caffè è inizialmente più caldo del latte. Qual è il segno del calore scambiato da ciascuna bevanda durante il mescolamento? Collega la risposta al verso del trasferimento di energia.
2. **Vero o falso?** «Se la somma dei calori scambiati è zero, non è avvenuto alcun trasferimento di energia». Motiva la risposta.
3. Mantieni uguali la massa e la temperatura iniziale del caffè e la temperatura iniziale del latte. Che cosa succede alla temperatura finale se aggiungi una massa maggiore di latte freddo? Spiega usando il bilancio.
4. Nel modello con calore specifico comune e contributo della tazza trascurabile, quando la temperatura finale è la media aritmetica delle due temperature iniziali?
   - A. Sempre.
   - B. Quando le masse delle due bevande sono uguali.
   - C. Quando il caffè parte dalla temperatura maggiore.
   
   Scegli e motiva.
5. **Vero o falso?** «Poiché il caffè cede tanta energia quanta ne assorbe il latte, le loro variazioni di temperatura hanno sempre lo stesso valore assoluto». Motiva la risposta.
6. Trascurando tazza e scambi con l’ambiente, una miscela di caffè caldo e latte freddo può raggiungere una temperatura inferiore a quella iniziale del latte? Spiega.
7. Due bevande hanno masse uguali ma calori specifici diversi. La loro temperatura finale deve essere la media aritmetica di quelle iniziali? Quale grandezza stabilisce il peso di ciascuna parte?
8. La tazza parte da una temperatura inferiore a quella finale prevista trascurandola. Includendola nel bilancio, come cambia la temperatura finale? Quale segno ha il calore assorbito dalla tazza?
9. Perché assumere lo stesso calore specifico per caffè e latte permette di semplificare \(c\) nell’equazione del bilancio? Questa semplificazione significa che il calore specifico è nullo?

## Note

[^1]: Approssimiamo i calori specifici di caffè e latte con quello dell’acqua, assunto costante nell’intervallo considerato. Il modello non comprende cambiamenti di stato e trascura il contributo energetico del mescolamento.

[^2]: Consideriamo trascurabili gli scambi con l’ambiente, l’evaporazione e il lavoro meccanico. Nel primo modello trascuriamo anche lo scambio con la tazza; nell’ultimo lo includiamo. La temperatura calcolata descrive l’equilibrio fra le parti considerate, prima che il raffreddamento verso l’ambiente diventi rilevante.

---

## Crediti — sezione di servizio della bozza

Questa sezione conserva la provenienza per la futura integrazione nel registro unico; non è una sezione didattica né una sezione finale visibile dell’HTML.

- **COP-01**: *Le Déjeuner* (*La colazione / Morning Coffee*, 1739), François Boucher, Musée du Louvre, RF 926; [scheda Commons](https://commons.wikimedia.org/wiki/File:Fran%C3%A7ois_Boucher_002.jpg). Provenienza della riproduzione: The Yorck Project (2002), *10.000 Meisterwerke der Malerei*, DIRECTMEDIA Publishing GmbH. Opera e riproduzione dichiarate di pubblico dominio sulla fonte, PD-Art e [Public Domain Mark 1.0](https://creativecommons.org/publicdomain/mark/1.0/). La scheda distingue il copyright della compilazione, detenuto da Zenodot Verlagsgesellschaft mbH e distribuito sotto GNU FDL, dal pubblico dominio della singola opera e riproduzione. File originale indicato dall’utente conservato integralmente, senza modifiche.
- **FIG-03**: *Pouring Milk Coffee*, indicata come “By Burst” sulla [fonte originale NegativeSpace](https://negativespace.co/pouring-milk-coffee/); versione scelta tramite [Rawpixel, immagine 5915327](https://www.rawpixel.com/image/5915327). [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). File 1024 × 683 px ricevuto dall’utente, senza modifiche; i metadati XMP conservati nel file collegano la foto alla fonte originale e alla licenza.
- **FIG-01**: *A small cup of coffee.JPG*, Julius Schorzman; [scheda Commons](https://commons.wikimedia.org/wiki/File:A_small_cup_of_coffee.JPG). [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/). Versione a 960 px scelta dall’utente; nessuna modifica ulteriore. La fonte reca anche l’avviso originale «NOTE: I only require attribution if you publish this photo in print or if it is used in a for-profit project.»: conservarlo nei metadati, mantenendo comunque l’attribuzione completa.
- **FIG-02**: *Glass of Milk (33657535532).jpg*, NIAID; [scheda Commons](https://commons.wikimedia.org/wiki/File:Glass_of_Milk_(33657535532).jpg), provenienza [Flickr](https://www.flickr.com/photos/54591706@N02/33657535532/). [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/). Versione a 960 px scelta dall’utente, derivata dalla revisione Commons già ritagliata; nessun nuovo ritaglio o modifica.
- L’uguaglianza approssimata dei calori specifici è l’ipotesi didattica esplicitamente richiesta dall’utente. Non vengono assegnate temperature, masse o valori sperimentali alle fotografie.
