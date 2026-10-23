# Le potenze di dieci e la notazione scientifica

<!-- Bozza v3 — 23 ottobre 2026 (Europe/Rome).
Area: Introduzione alla fisica e alla misura.
Impostazione approvata con «Procedi»; testo da approvare.
Segnaposto e sezione finale di servizio non fanno parte del testo pubblicabile. -->

[COP-01 — Mappa dell’emisfero sud di Giove scelta dall’utente: risorse/giove.jpg. Immagine integrale, senza ritagli; attribuzione NASA/JPL/Space Science Institute e pubblico dominio documentati nei crediti.]

Didascalia: Mappa dell’emisfero sud di Giove, ricostruita dalle immagini della sonda Cassini. Il polo sud è al centro e l’equatore lungo il bordo.

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
| Lunghezza totale del DNA dei 46 cromosomi di una cellula umana, disteso | 10⁰ m |
| Diametro della Terra | 10⁷ m |
| Diametro del Sole | 10⁹ m |
| Lunghezza complessiva delle fibre ottiche per telecomunicazioni installate nel mondo[^2] | 10¹³ m |
| Raggio del disco stellare della Via Lattea | 10²¹ m |

Didascalia: Le potenze indicano scale approssimative, dall’atomo alla galassia. Il DNA disteso di una cellula umana raggiunge circa 2 m; le fibre ottiche installate nel mondo, sommate, superano i 5 miliardi di chilometri.

Un **ordine di grandezza** è una stima espressa con una potenza di dieci. Qui scegliamo la potenza più vicina in termini di fattori moltiplicativi.[^1] Non sostituisce una misura precisa: 10⁷ m descrive la scala del diametro terrestre, mentre 1,27 · 10⁷ m ne conserva una stima più dettagliata.

Fra 10⁷ m e 10⁻¹⁰ m ci sono diciassette passaggi di un fattore dieci. Il rapporto fra queste due scale è quindi 10¹⁷: il diametro terrestre è circa centomila milioni di milioni di volte quello atomico. Un confronto così esteso diventa leggibile grazie agli esponenti.

[VID-01 — Miniatura originale e collegamento a Powers of Ten: https://www.youtube.com/watch?v=0fKBhvDjuy0 . Apertura su YouTube, senza lettore incorporato. Diritti della miniatura da verificare.]

Didascalia: In Powers of Ten ogni cambio di scala modifica di un fattore dieci la lunghezza rappresentata dall’inquadratura. Osserva come cambia ciò che diventa visibile.

Nel film A Boy and His Atom, i ricercatori hanno spostato molecole di monossido di carbonio con un microscopio a effetto tunnel e registrato immagini successive. La sequenza rende visibile un lavoro svolto su scala molecolare.

[VID-02 — Miniatura originale e collegamento a A Boy and His Atom: https://www.youtube.com/watch?v=oSCX78-8-q0 . Apertura su YouTube, senza lettore incorporato. Diritti della miniatura da verificare.]

Didascalia: Le figure del film sono costruite disponendo molecole di monossido di carbonio su una superficie.

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

## Domande di verifica

1. Vero o falso? «10⁻³ è un numero negativo». Motiva la risposta e scrivi il suo valore decimale.
2. Perché 10⁰ vale 1? Spiegalo seguendo i passaggi della tabella delle potenze.
3. Quali scritture sono in notazione scientifica: 47 · 10⁻⁶, 4,7 · 10⁻⁵, 0,47 · 10⁻⁴? Riscrivi le altre nella forma corretta senza cambiarne il valore.
4. Scrivi 0,000047 m in notazione scientifica e ingegneristica. Spiega come le due scritture possono indicare la stessa lunghezza.
5. Nella tabella delle lunghezze, quanti ordini di grandezza separano il diametro terrestre da quello di un atomo di idrogeno? Quale fattore approssimativo corrisponde a questa differenza?
6. Quale lunghezza è maggiore, 8 · 10⁻⁶ m oppure 2 · 10⁻⁵ m? Giustifica il confronto senza usare soltanto i coefficienti.
7. Un compagno scrive 10² · 10³ = 10⁶ e 10² + 10³ = 10⁵. Individua l’errore in ciascun calcolo e correggilo.
8. Il DNA disteso di una cellula umana è lungo circa 2 m. Ha lo stesso ordine di grandezza dell’altezza di una persona? Spiega perché questo confronto non descrive le dimensioni della cellula.

## Note

[^1]: Con questo criterio il passaggio da 10ⁿ a 10ⁿ⁺¹ avviene quando il coefficiente della forma scientifica raggiunge √10, circa 3,16: le due potenze sono allora distanti dallo stesso fattore. Per esempio, 4,7 · 10⁻⁵ m è più vicino a 10⁻⁴ m che a 10⁻⁵ m secondo questo criterio. L’ordine di grandezza non coincide sempre con la potenza presente nella scrittura scientifica.

[^2]: La stima somma le fibre ottiche delle reti di telecomunicazione, comprese quelle contenute nello stesso cavo; non misura la sola lunghezza dei percorsi geografici. È un riferimento per la parte ottica dell’infrastruttura di Internet, non un censimento di tutti i cavi, inclusi quelli in rame.

---

## Servizio editoriale — fonti, provenienza e controlli

Questa sezione non entra nel contenuto didattico pubblicato. Le fonti dei contenuti correnti confluiranno nel registro unico e nei crediti incorporati durante la realizzazione.

- Sorgente: sistema_internazionale_notazione_it.html v11, sezione #scale, blob ede0bed4b28522b2431e4201b39e8f9f10593f88. Originale invariato; revisioni precedenti della bozza conservate in Git.
- TAB-01L: unica tabella degli ordini di grandezza, dedicata alle lunghezze. Restano distinte TAB-02 (potenze) e TAB-03 (notazioni), che non sono tabelle di grandezze fisiche diverse. Rimossi cratere e tabella delle masse per richiesta esplicita dell’utente.
- Scale atomiche, persona e galassia: [OpenStax, College Physics 2e, 1.2, tabella 1.3](https://openstax.org/books/college-physics-2e/pages/1-2-physical-quantities-and-units). Raggio del disco stellare della Via Lattea dell’ordine di 10²¹ m; non raggio dell’alone. Spiegazione originale, nessuna immagine OpenStax ripresa.
- Diametro terrestre: [NASA, Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html), raggio medio 6371 km, quindi diametro medio 12 742 km. Nel testo circa 12 700 km, cioè 1,27 · 10⁷ m.
- Diametro solare: [NASA, Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html), raggio medio 695 700 km; diametro circa 1,39 · 10⁹ m. Nessun dato di massa usato nella bozza v2.
- DNA: [Genomics England, Understanding genomics, voce DNA](https://www.genomicsengland.co.uk/genomic-medicine/understanding-genomics) e [Annunziato, DNA Packaging: Nucleosomes and Chromatin, Nature Education](https://www.nature.com/scitable/topicpage/dna-packaging-nucleosomes-and-chromatin-310/). Circa 2 m per il DNA nucleare di una cellula umana diploide con 46 cromosomi, prima della duplicazione. La riga specifica il DNA disteso, non la dimensione della cellula; ordine 10⁰ m con il criterio dichiarato. Non generalizzare il dato a qualsiasi specie, ai gameti o a ogni fase del ciclo cellulare.
- Rete mondiale: [Commissione europea, CORDIS, progetto ECSTATIC, grant 101189595](https://cordis.europa.eu/project/id/101189595), avviato nel 2025. Descrizione e obiettivo riportano oltre 5 miliardi di km di fibra ottica installata per comunicazioni dati: riferimento numerico oltre 5 · 10¹² m, scala 10¹³ m secondo il criterio dichiarato. La fonte non fornisce un limite superiore né un censimento di ogni cavo Internet; la riga è esplicitamente una stima della fibra ottica mondiale. Per il significato del conteggio in fibra-km: [Optics & Photonics News, marzo 2022, articolo sul vetro ottico, grafico Cumulative total of cabled fiber installed worldwide](https://opn-web-afd-d3bfbkd5bcc5asbs.z02.azurefd.net/opn/media/images/pdf/2022/0322/030-039r_opn_03_22.pdf?t=638452572281577707). Le singole fibre di un cavo si sommano: non confondere fibra-km con cavo-km o lunghezza dei tracciati. La nota 2 rende esplicito questo perimetro. Non usare al suo posto il totale dei soli cavi sottomarini.
- COP-01: [Map of Jupiter, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Map_of_Jupiter.jpg), autore NASA/JPL/Space Science Institute, pubblico dominio PD-USGov-NASA. [Fonte NASA, Map of Jupiter’s South](https://www.nasa.gov/image-article/map-of-jupiters-south/), immagini Cassini dell’11–12 dicembre 2000; proiezione stereografica polare, polo sud al centro ed equatore al bordo. [JPL Image Use Policy](https://www.jpl.nasa.gov/jpl-image-use-policy/): credito associato e nessuna approvazione istituzionale implicata. Versione 960 × 975 px scelta dall’utente, salvata in risorse/giove.jpg e incorporata senza modifiche. La vecchia copertina resta nel sorgente storico e in Git; nessun credito corrente per quell’immagine rimossa.
- IMG-01 e sezione «Una fotografia non basta a misurare» rimossi su richiesta. Nessun richiamo residuo alle micrografie nel testo o nei quesiti; i materiali originali non sono stati cancellati dal repository. Le provenienze storiche restano in Git e nello stato.
- VID-01 e VID-02 conservano URL e miniature originali proposti. Collegamenti: [Powers of Ten](https://www.youtube.com/watch?v=0fKBhvDjuy0) e [A Boy and His Atom](https://www.youtube.com/watch?v=oSCX78-8-q0). Titoli verificati, riproduzione integrale e diritti delle miniature ancora da verificare. Per VID-02: [Guinness World Records, Smallest stop-motion film](https://www.guinnessworldrecords.com/world-records/smallest-stop-motion-film), molecole di CO disposte con microscopio a effetto tunnel. Video ricollocato nella sezione sul confronto delle scale, senza ripristinare la sezione eliminata.
- Quesiti: n. 5 deriva dal quesito originale 4; n. 4 conserva le conversioni del quesito originale 5, lasciando il prefisso al capitolo 4. Il quesito sulle micrografie (originale 7) è ritirato da questo capitolo insieme alla sezione richiesta dall’utente; la v1 ne conserva la formulazione. Il nuovo n. 8 riguarda il DNA e il significato della lunghezza totale. Otto domande complessive, senza soluzioni.
