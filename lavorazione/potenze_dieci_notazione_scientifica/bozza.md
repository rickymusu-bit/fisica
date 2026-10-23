# Le potenze di dieci e la notazione scientifica

<!-- Bozza v1 — 23 ottobre 2026 (Europe/Rome).
Area: Introduzione alla fisica e alla misura.
Impostazione approvata con «Procedi»; testo da approvare.
Segnaposto e sezione finale di servizio non fanno parte del testo pubblicabile. -->

[COP-01 — Foto della Terra oltre l’orizzonte lunare già presente nel sorgente, usata soltanto come copertina. Provenienza dell’esatto file e licenza ancora da accertare.]

Didascalia: La Terra oltre l’orizzonte della Luna. Le dimensioni dei corpi celesti richiedono numeri molto diversi da quelli degli oggetti che maneggiamo ogni giorno.

## Dal molto grande al molto piccolo

Il diametro della Terra è circa 12 700 000 m. Quello di un atomo di idrogeno è circa 0,0000000001 m. Scritti uno accanto all’altro, questi numeri sembrano fatti soprattutto di zeri: basta perderne uno per cambiare il valore di dieci volte. Come possiamo scriverli e confrontarli senza dover ricontare ogni cifra?

Le **potenze di dieci** permettono di raccogliere quegli zeri in una scrittura breve. Un milione si scrive 10⁶; un miliardesimo si scrive 10⁻⁹. L’esponente, il numero piccolo in alto, indica quante volte intervenire con un fattore dieci. Prima di usare questa scrittura per descrivere la Terra o un atomo, vediamo che cosa significa.

## Un passo vale un fattore dieci

Partiamo da 1 e moltiplichiamo per 10: otteniamo 10, poi 100, poi 1000. Il numero 1000 è il prodotto di tre fattori uguali a 10:

\[
10^3 = 10 \cdot 10 \cdot 10 = 1000
\]

Il 10 è la **base** della potenza e il 3 è l’**esponente**. Per gli esponenti interi positivi, l’esponente conta quanti fattori uguali alla base compaiono nel prodotto. Non significa moltiplicare 10 per il numero scritto in alto: 10³ vale 1000, mentre 10 · 3 vale 30.

[TAB-02 — Tabella delle potenze di dieci. Conservare la stessa composizione su ogni dispositivo.]

| Potenza | Valore decimale |
| --- | --- |
| 10³ | 1000 |
| 10² | 100 |
| 10¹ | 10 |
| 10⁰ | 1 |
| 10⁻¹ | 0,1 |
| 10⁻² | 0,01 |
| 10⁻³ | 0,001 |

Didascalia: Scendendo di una riga, l’esponente diminuisce di uno e il valore viene diviso per dieci.

Leggiamo ora la tabella dall’alto verso il basso. Da 1000 passiamo a 100, poi a 10: a ogni passo dividiamo per dieci. Continuando arriviamo a 1, che si scrive **10⁰**. L’esponente zero, quindi, dà 1 e non zero: mantiene la stessa regolarità dei passaggi precedenti.

La successione continua anche sotto 1. Un altro passo porta a un decimo, poi a un centesimo e a un millesimo. Gli esponenti diventano negativi:

\[
10^{-3} = \frac{1}{10^3} = \frac{1}{1000} = 0{,}001
\]

Il segno meno nell’esponente indica un reciproco: **10⁻³ è un numero positivo più piccolo di 1**. Per ottenere un numero negativo occorre un segno meno davanti al numero, come in −10³, che vale −1000. Il posto del segno cambia il significato della scrittura.

## Scrivere lo stesso numero in modi diversi

Torniamo al diametro terrestre. Possiamo raccogliere i sette posti che separano 1,27 da 12 700 000 in una potenza di dieci:

\[
12\,700\,000\ \mathrm{m} = 1{,}27 \cdot 10^7\ \mathrm{m}
\]

Il valore e l’unità sono gli stessi: è cambiato soltanto il modo di scrivere il numero. Il fattore 1,27 dice quanto prendere della scala indicata da 10⁷. La scrittura rende riconoscibili sia le cifre del valore sia la sua dimensione numerica.

La **notazione scientifica** scrive un numero non nullo nella forma:

\[
a \cdot 10^n
\]

Qui n è un numero intero e il coefficiente a ha valore assoluto compreso fra 1 incluso e 10 escluso. Per un numero positivo, quindi, davanti alla virgola rimane una sola cifra diversa da zero. Per l’atomo di idrogeno la scrittura diventa:

\[
0{,}0000000001\ \mathrm{m} = 1 \cdot 10^{-10}\ \mathrm{m}
\]

Quando il coefficiente è 1 possiamo ometterlo e scrivere direttamente 10⁻¹⁰ m. L’esponente negativo segnala che il valore numerico espresso in metri è minore di 1. Anche in questo caso la lunghezza resta positiva.

[TAB-03 — Confronto fra scritture equivalenti, ripreso dal sorgente e separato dal capitolo sui prefissi.]

| Forma | Scrittura della stessa lunghezza |
| --- | --- |
| Decimale | 0,000047 m |
| Esponenziale | 470 · 10⁻⁷ m |
| Scientifica | 4,7 · 10⁻⁵ m |
| Ingegneristica | 47 · 10⁻⁶ m |

Didascalia: Cambiano coefficiente ed esponente, ma ciascuna riga indica la stessa lunghezza.

Per passare da 0,000047 a 4,7 spostiamo la virgola di cinque posti verso destra: il coefficiente è diventato centomila volte maggiore. Il fattore 10⁻⁵ compensa questo cambiamento, così il prodotto conserva il valore iniziale. In senso inverso, moltiplicare 4,7 per 10⁻⁵ sposta la virgola di cinque posti verso sinistra.

Una scrittura con un coefficiente moltiplicato per una potenza di dieci è detta **esponenziale**. Quella scientifica rispetta anche il vincolo sul coefficiente; per questo 470 · 10⁻⁷ è esponenziale ma non è in forma scientifica. Nella **notazione ingegneristica**, invece, l’esponente è un multiplo di tre e, per i numeri positivi, il coefficiente va da 1 incluso a 1000 escluso. Questa scelta si collega ai prefissi del Sistema internazionale, trattati nel capitolo successivo.

La forma scientifica è utile quando rende il numero più leggibile o il confronto più chiaro. Per una lunghezza di 2 m, scrivere 2 · 10⁰ m aggiungerebbe poco. Il vantaggio emerge quando gli zeri diventano numerosi.

## Confrontare le scale

Consideriamo prima due potenze senza coefficienti: 10³ è dieci volte 10² e cento volte 10¹. Ogni aumento di uno nell’esponente corrisponde a un fattore dieci. Se gli esponenti differiscono di tre, il rapporto fra i valori è mille.

[TAB-01L — Tabella delle lunghezze del sorgente, con stime espresse come ordini di grandezza.]

| Dimensione | Ordine di grandezza della lunghezza |
| --- | --- |
| Diametro di un atomo di idrogeno | 10⁻¹⁰ m |
| Diametro di una piccola goccia di pioggia | 10⁻³ m |
| Altezza di una persona | 10⁰ m |
| Larghezza del cratere del Mount St. Helens dopo l’eruzione del 1980 | 10³ m |
| Diametro della Terra | 10⁷ m |
| Diametro del Sole | 10⁹ m |
| Raggio del disco stellare della Via Lattea | 10²¹ m |

Didascalia: Le potenze indicano scale approssimative, dall’atomo alla galassia.

Un **ordine di grandezza** è una stima espressa con una potenza di dieci. Qui scegliamo la potenza più vicina in termini di fattori moltiplicativi.[^1] Non sostituisce una misura precisa: 10⁷ m descrive la scala del diametro terrestre, mentre 1,27 · 10⁷ m ne conserva una stima più dettagliata.

Fra 10⁷ m e 10⁻¹⁰ m ci sono diciassette passaggi di un fattore dieci. Il rapporto fra queste due scale è quindi 10¹⁷: il diametro terrestre è circa centomila milioni di milioni di volte quello atomico. Un confronto così esteso diventa leggibile grazie agli esponenti.

[VID-01 — Miniatura originale e collegamento a Powers of Ten: https://www.youtube.com/watch?v=0fKBhvDjuy0 . Apertura su YouTube, senza lettore incorporato. Diritti della miniatura da verificare.]

Didascalia: In Powers of Ten ogni cambio di scala modifica di un fattore dieci la lunghezza rappresentata dall’inquadratura. Osserva come cambia ciò che diventa visibile.

Lo stesso modo di ragionare vale per le masse. Possiamo confrontarle nella medesima unità, il chilogrammo, passando dall’atomo alla Terra e al Sole. Le potenze della tabella indicano soltanto la scala: la massa di una persona o di una goccia varia da un caso all’altro.

[TAB-01M — Tabella delle masse del sorgente convertita in kg, con correzioni documentate nella sezione di servizio.]

| Oggetto o materiale | Ordine di grandezza della massa |
| --- | --- |
| Atomo di idrogeno | 10⁻²⁷ kg |
| Piccola goccia di pioggia, di diametro circa 1 mm | 10⁻⁶ kg |
| Persona adulta | 10² kg |
| Cenere ricaduta dopo l’eruzione del Mount St. Helens del 18 maggio 1980 | 10¹² kg |
| Terra | 10²⁵ kg |
| Sole | 10³⁰ kg |
| Via Lattea, comprendendo la materia oscura | 10⁴² kg |

Didascalia: Le masse sono espresse tutte in chilogrammi. Gli ordini di grandezza servono a confrontare scale molto diverse.

Quando confrontiamo valori in notazione scientifica, anche il coefficiente conta. A parità di esponente, 4,7 · 10⁻⁵ è maggiore di 3,2 · 10⁻⁵ perché 4,7 è maggiore di 3,2. Per due numeri positivi entrambi in forma scientifica, se gli esponenti sono diversi è maggiore quello con l’esponente maggiore. Così 1,2 · 10⁻⁴ supera 9 · 10⁻⁵, anche se 1,2 è minore di 9: il primo numero vale 0,00012, il secondo 0,00009.

## Calcolare con le potenze di dieci

La scrittura compatta aiuta anche nei calcoli. Moltiplicare 10² per 10³ significa riunire due fattori 10 e altri tre fattori 10: in tutto sono cinque. Per questo, quando moltiplichiamo potenze con la stessa base, **sommiamo gli esponenti**:

\[
10^p \cdot 10^q = 10^{p+q}
\]

La regola vale anche con esponenti negativi. Nel prodotto seguente, le sei divisioni per dieci prevalgono sulle quattro moltiplicazioni:

\[
10^4 \cdot 10^{-6} = 10^{4-6} = 10^{-2} = 0{,}01
\]

Nella divisione facciamo il percorso inverso e sottraiamo gli esponenti:

\[
\frac{10^p}{10^q} = 10^{p-q}
\]

\[
\frac{10^7}{10^{-10}} = 10^{7-(-10)} = 10^{17}
\]

Quest’ultimo passaggio spiega il confronto fra le scale terrestre e atomica: sottrarre un esponente negativo equivale ad aggiungerne il valore positivo.

Se compaiono anche i coefficienti, li moltiplichiamo tra loro e applichiamo la regola alle potenze. Alla fine controlliamo che il coefficiente rispetti il vincolo della forma scientifica:

\[
(4 \cdot 10^3) \cdot (3 \cdot 10^{-5})
= 12 \cdot 10^{-2}
= 1{,}2 \cdot 10^{-1}
\]

Il passaggio da 12 a 1,2 divide il coefficiente per dieci; per conservare il prodotto, la potenza deve aumentare di un fattore dieci, passando da 10⁻² a 10⁻¹. È lo stesso equilibrio usato per trasformare la scrittura decimale in notazione scientifica.

La somma richiede un ragionamento diverso. Due gruppi da mille danno duemila: 10³ + 10³ = 2 · 10³, non 10⁶. La somma degli esponenti appartiene alla regola del prodotto; nella somma dei numeri dobbiamo invece raccogliere la stessa potenza e sommare i coefficienti.

\[
2 \cdot 10^3 + 3 \cdot 10^2
= 2 \cdot 10^3 + 0{,}3 \cdot 10^3
= 2{,}3 \cdot 10^3
\]

## Una fotografia non basta a misurare

Una struttura microscopica può occupare tutta una pagina, mentre la Terra entra nella fotografia di copertina. La grandezza sulla pagina dipende dall’ingrandimento e dall’inquadratura. Per collegarla a una dimensione reale serve un riferimento, come una barra di scala.

[IMG-01 — Micrografie originali A/B del sorgente, senza modificarne composizione o attribuirle a soggetti non documentati. Identità e licenza ancora da accertare.]

Didascalia: Le due micrografie mostrano strutture molto piccole. Senza una barra di scala o un ingrandimento riferito alle condizioni di visualizzazione, la sola immagine non permette di ricavarne le dimensioni reali.

Un’immagine microscopica può anche essere costruita a partire dalle misure di uno strumento. Nel film A Boy and His Atom, i ricercatori hanno spostato molecole di monossido di carbonio con un microscopio a effetto tunnel e registrato immagini successive. La sequenza rende visibile un lavoro svolto su scala molecolare.

[VID-02 — Miniatura originale e collegamento a A Boy and His Atom: https://www.youtube.com/watch?v=oSCX78-8-q0 . Apertura su YouTube, senza lettore incorporato. Diritti della miniatura da verificare.]

Didascalia: Le figure del film sono costruite disponendo molecole sulla superficie. La loro dimensione sullo schermo dipende dall’ingrandimento.

## Domande di verifica

1. Vero o falso? «10⁻³ è un numero negativo». Motiva la risposta e scrivi il suo valore decimale.
2. Perché 10⁰ vale 1? Spiegalo seguendo i passaggi della tabella delle potenze.
3. Quali scritture sono in notazione scientifica: 47 · 10⁻⁶, 4,7 · 10⁻⁵, 0,47 · 10⁻⁴? Riscrivi le altre nella forma corretta senza cambiarne il valore.
4. Scrivi 0,000047 m in notazione scientifica e ingegneristica. Spiega come le due scritture possono indicare la stessa lunghezza.
5. Nella tabella delle lunghezze, quanti ordini di grandezza separano il diametro terrestre da quello di un atomo di idrogeno? Quale fattore approssimativo corrisponde a questa differenza?
6. Quale lunghezza è maggiore, 8 · 10⁻⁶ m oppure 2 · 10⁻⁵ m? Giustifica il confronto senza usare soltanto i coefficienti.
7. Un compagno scrive 10² · 10³ = 10⁶ e 10² + 10³ = 10⁵. Individua l’errore in ciascun calcolo e correggilo.
8. Le micrografie A e B mostrano dettagli molto piccoli. Perché, senza una scala, non puoi ricavare il diametro di una struttura dalla fotografia?

## Note

[^1]: Con questo criterio il passaggio da 10ⁿ a 10ⁿ⁺¹ avviene quando il coefficiente della forma scientifica raggiunge √10, circa 3,16: le due potenze sono allora distanti dallo stesso fattore. Per esempio, la massa terrestre 5,97 · 10²⁴ kg è più vicina a 10²⁵ kg che a 10²⁴ kg secondo questo criterio. L’ordine di grandezza non coincide sempre con la potenza presente nella scrittura scientifica.

---

## Servizio editoriale — fonti, provenienza e controlli

Questa sezione non entra nel contenuto didattico pubblicato. Le fonti confluiranno nel registro unico e nei crediti incorporati durante la realizzazione.

- Sorgente: sistema_internazionale_notazione_it.html v11, sezione #scale, blob ede0bed4b28522b2431e4201b39e8f9f10593f88. Segnaposto e materiali originali conservati, nessuna ricerca di immagini nuove.
- TAB-01L e TAB-01M: [OpenStax, College Physics 2e, 1.2, tabella 1.3](https://openstax.org/books/college-physics-2e/pages/1-2-physical-quantities-and-units). Controllo indipendente di scale atomiche, persona e corpi celesti. Non adottare le definizioni storiche del SI presenti nel testo. Spiegazione originale; nessuna immagine OpenStax ripresa.
- Diametro terrestre: [NASA, Earth Facts](https://science.nasa.gov/earth/facts/), diametro equatoriale 12 756 km. Nel testo circa 12 700 km, cioè 1,27 · 10⁷ m; non è ricavato dalla foto.
- Massa terrestre e solare: [NASA, Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html), 5,9722 · 10²⁴ kg; [NASA, Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html), circa 1,99 · 10³⁰ kg e raggio 695 700 km. Diametro solare circa 1,39 · 10⁹ m.
- Goccia: riferimento rappresentativo di diametro circa 1 mm, coerente con la scala del sorgente. Controllo per una goccia sferica d’acqua: volume pari a un sesto di π · d³, densità circa 1000 kg/m³, massa circa 5,2 · 10⁻⁷ kg, ordine 10⁻⁶ kg con il criterio dichiarato. Calcolo editoriale, da non trasformare in un esercizio aggiuntivo.
- Mount St. Helens: [USGS, Fact Sheet 036-00](https://pubs.usgs.gov/fs/2000/fs036-00/), cratere circa 1,2 per 1,8 miglia (circa 1,9 per 2,9 km), ordine 10³ m; [USGS, Ash eruption and fallout](https://pubs.usgs.gov/gip/msh/ash.html), circa 540 milioni di tons statunitensi di cenere ricaduta. Conversione di controllo: circa 4,9 · 10¹¹ kg, ordine 10¹² kg con il criterio dichiarato. Specificato il materiale: non si attribuisce questa massa a tutti i prodotti dell’eruzione.
- Via Lattea: [NASA/Hubble, What Does the Milky Way Weigh?, 7 marzo 2019](https://science.nasa.gov/missions/hubble/what-does-the-milky-way-weigh-hubble-and-gaia-investigate/) e [ESA/Hubble, heic1905](https://esahubble.org/news/heic1905/). Stima rappresentativa del 2019 di 1,5 milioni di milioni di masse solari, circa 3 · 10⁴² kg, comprendente la materia oscura; usata per la sola scala 10⁴² kg, senza dichiararla misura attuale definitiva. Il raggio del disco stellare ha scala 10²¹ m; non è il raggio dell’alone di materia oscura.
- Correzioni rispetto al sorgente: conversione g → kg con esponenti diminuiti di tre. La sola conversione avrebbe dato Terra 10²⁴ kg, materiale vulcanico 10¹¹ kg e Via Lattea 10⁴¹ kg; la bozza usa rispettivamente 10²⁵, 10¹² e 10⁴² kg dopo controllo dei dati, scelta esplicita del criterio e chiarimento dei soggetti. L’originale resta invariato.
- COP-01 e IMG-01: registro risorse/crediti.json e sorgente privi di attribuzioni individuali sufficienti. La descrizione della copertina non prova l’identità con un particolare scatto NASA. Identificazione dell’esatto file, licenza e qualità visiva da verificare prima dell’integrazione; nessuna autorizzazione dedotta.
- VID-01 e VID-02: URL originali aperti e titoli corrispondenti verificati; riproduzione integrale non verificata. Per VID-02: [Guinness World Records, Smallest stop-motion film](https://www.guinnessworldrecords.com/world-records/smallest-stop-motion-film), fonte primaria del record che descrive molecole di CO e uso del microscopio. Disponibilità delle pagine non equivale a licenza di redistribuzione delle miniature incorporate: verifica ancora aperta.
- Quesiti: n. 5 deriva dal quesito originale 4; n. 4 conserva le conversioni del quesito originale 5, lasciando il prefisso al capitolo 4; n. 8 conserva il quesito originale 7. Cinque quesiti aggiunti per esponenti, normalizzazione, confronto e operazioni. Nessuna soluzione inclusa.
