# Le relazioni tra grandezze

Versione della bozza: v1 — 24 ottobre 2026.  
Area: Introduzione alla fisica e alla misura.

[C9-COP — Copertina da scegliere per il capitolo unificato; non riutilizzata nel corpo.]

## Raddoppiare una quantità

Un quaderno costa 2 €. Se ne compriamo due spendiamo 4 €, se ne compriamo tre spendiamo 6 €. Il prezzo cresce insieme al numero di quaderni: possiamo prevederlo prima di arrivare alla cassa. Ma due grandezze che aumentano insieme seguono sempre questa stessa regola?

[C9-SIT — Immagine di un quaderno da scegliere e schema dell’acquisto: prezzo unitario 2 €/quaderno, quantità e prezzo totale. Nessun riuso della copertina.]

In questo caso il prezzo unitario rimane fisso: non ci sono sconti o quote aggiuntive. Ogni quaderno aggiunge 2 € alla spesa.

| Numero di quaderni x | Prezzo y (€) |
|---:|---:|
| 0 | 0 |
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |

Se dividiamo il prezzo per il numero di quaderni, otteniamo sempre 2 €/quaderno. È questo **rapporto costante** a caratterizzare la **proporzionalità diretta**:

\[
\frac{y}{x}=k
\]

La stessa relazione si scrive:

\[
y=k\cdot x
\]

La **costante di proporzionalità k** esprime quanto y corrisponde a un’unità di x. Nell’acquisto è il prezzo unitario: 2 €/quaderno. Le sue unità dipendono dalle grandezze confrontate: non è necessariamente un numero senza unità.

Raddoppiando x, anche y raddoppia; triplicando x, y triplica. Cinque quaderni costano quindi 10 €, cinque volte il prezzo di uno e 2 € più di quattro quaderni.

[C9-GRA-D — Riutilizzare punti e comando «Mostra la retta» del grafico dei quaderni. Assi: numero di quaderni e prezzo (€). Modello passante per l’origine; valori numerici coerenti con la tabella.]

Il grafico della proporzionalità diretta è una retta che passa per l’origine: se non compriamo quaderni, la spesa è zero. Il rapporto si calcola per x diverso da zero; il valore nello zero si ricava invece da y = k·x. Nell’esempio gli acquisti possibili corrispondono ai punti con quantità intere.[^1]

## Una retta può partire da un altro valore

Un servizio di consegna chiede 3 € fissi più 2 € per ogni chilometro. Anche qui ogni chilometro aggiunge la stessa cifra, ma il costo comprende una quota iniziale.

[C9-SIT-C — Immagine pertinente a una consegna, da scegliere; schema con percorso, quota fissa 3 € e costo per chilometro 2 €/km. Non disegnare mezzi sostitutivi con sagome astratte.]

Indicando con x il percorso e con y il costo:

\[
y=(2\,\mathrm{€/km})\cdot x+3\,\mathrm{€}
\]

| Percorso x (km) | Costo y (€) |
|---:|---:|
| 0 | 3 |
| 1 | 5 |
| 2 | 7 |
| 3 | 9 |

A un percorso di 2 km corrispondono 7 €: 4 € per il tragitto e 3 € di quota fissa. Con 4 km il costo è 11 €, non 14 €. Raddoppiare il percorso non raddoppia la quota iniziale, quindi non raddoppia il costo totale.

La forma generale di una relazione di questo tipo è:

\[
y=m\cdot x+q
\]

Il coefficiente **m** è la **pendenza**: indica quanto varia y per ogni unità aggiunta a x. La **intercetta q** è il valore di y quando x vale zero e si legge nel punto in cui la retta incontra l’asse verticale. Nel servizio di consegna m vale 2 €/km e q vale 3 €.

Possiamo ricavare la pendenza da due punti distinti della retta:

\[
m=\frac{y_2-y_1}{x_2-x_1}
\]

I pedici 1 e 2 indicano i valori del primo e del secondo punto. Per la consegna, passando da 1 a 3 km il costo aumenta da 5 a 9 €: l’aumento di 4 € diviso per 2 km restituisce 2 €/km.

[C9-GRA-C — Grafico del costo della consegna, con dati della tabella, asse x in km e asse y in euro. Evidenziare intercetta e incremento tra i due punti usati nel calcolo, senza ripetere l’intera spiegazione.]

Con q diverso da zero la relazione si chiama **affine** e non è una proporzionalità diretta. Ponendo q = 0 ritroviamo y = m·x.

La pendenza può anche essere negativa. La retta matematica y = 8 − x, per esempio, diminuisce di un’unità ogni volta che x aumenta di uno. Non descrive però una proporzionalità inversa: a diminuire è una retta, mentre la relazione inversa segue una regola diversa.

[C9-GRA-R — Riutilizzare il confronto delle tre rette y = 2·x, y = 3 + 2·x e y = 8 − x, con x e y numeri astratti. Le due crescenti hanno la stessa pendenza e intercette diverse; la terza scende. Non attribuire a questo confronto unico le unità dei differenti contesti concreti.]

## Quando resta costante il prodotto

Disegniamo rettangoli tutti con area di 12 cm². Una base di 2 cm richiede un’altezza di 6 cm; una base di 4 cm richiede un’altezza di 3 cm. La base raddoppia e l’altezza si dimezza, perché il loro prodotto deve restare uguale all’area.

[C9-RET — Due rettangoli in scala: base 2 cm e altezza 6 cm; base 4 cm e altezza 3 cm. Stessa area di 12 cm². Figure geometriche costruibili direttamente.]

| Base x (cm) | Altezza y (cm) |
|---:|---:|
| 1 | 12 |
| 2 | 6 |
| 3 | 4 |
| 4 | 3 |
| 6 | 2 |
| 12 | 1 |

Questa è una **proporzionalità inversa**. La sua caratteristica è il prodotto costante:

\[
x\cdot y=k
\]

Da cui:

\[
y=\frac{k}{x}
\]

Qui k è l’area di 12 cm². Per ottenere un’altezza dividiamo quindi un’area per una lunghezza. Se la base triplica da 2 a 6 cm, l’altezza diventa un terzo: da 6 a 2 cm.

[C9-GRA-I — Riutilizzare tabella, punti e comando «Mostra la curva» dell’inversa. Assi base (cm) e altezza (cm), dominio positivo.]

Il grafico è un ramo di **iperbole**. Non si appiattisce su una retta: aumentando ancora la base, l’altezza continua a diminuire, ma deve mantenere costante il prodotto. In questo esempio base e altezza sono positive; con base zero non può esistere un rettangolo di area 12 cm².

## Quando il lato raddoppia e l’area quadruplica

Un quadrato di lato 1 cm ha area 1 cm². Se portiamo il lato a 2 cm, il nuovo quadrato contiene quattro quadrati del precedente formato: la sua area è 4 cm².

[C9-QUA — Quadrati di lato 1 e 2 cm, in scala; il secondo suddiviso in quattro quadrati di lato 1 cm. Etichette limitate a lati e aree.]

Indicando con x il lato e con y l’area:

\[
y=x^2
\]

| Lato x (cm) | Area y (cm²) |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |

L’area è direttamente proporzionale **al quadrato del lato**, non al lato. La forma generale di una **proporzionalità quadratica** è:

\[
y=k\cdot x^2
\]

Per x diverso da zero, rimane costante il rapporto:

\[
\frac{y}{x^2}=k
\]

Nel quadrato k vale 1, senza unità: il rapporto fra area e lato al quadrato confronta due aree. In altri modelli il valore e le unità di k possono essere differenti.

Raddoppiare x moltiplica y per quattro; triplicarlo moltiplica y per nove. Se il lato passa da 3 a 6 cm, l’area passa da 9 a 36 cm²: il nuovo quadrato contiene quattro quadrati grandi quanto quello iniziale.

[C9-GRA-Q — Riutilizzare tabella, punti e comando «Mostra la curva» della relazione quadratica. Assi lato (cm) e area (cm²). Lo zero rappresenta il limite di lato e area nulli.]

Il grafico appartiene a una **parabola**; per il lato consideriamo solo x non negativo. La curva passa per l’origine, ma non è una retta. Il passaggio per l’origine, da solo, non basta quindi a riconoscere una proporzionalità diretta.

## Domande di verifica

1. Dalla tabella dei quaderni ricava il costo di un singolo quaderno. Perché la retta del prezzo attraversa l’origine?
2. Quali unità ha k nell’esempio dei quaderni? Che cosa rappresenta?
3. Qual è l’intercetta della consegna da 3 € più 2 € per chilometro? Perché quella relazione non è una proporzionalità diretta?
4. Nella consegna, da 2 a 5 km il costo passa da 7 a 13 €. Calcola la pendenza e spiegane il significato.
5. La retta y = 8 − x scende. Perché non la chiamiamo proporzionalità inversa?
6. Nella tabella dei rettangoli, se la base triplica da 2 cm a 6 cm, come cambia l’altezza? Quale quantità resta uguale?
7. Un rettangolo della stessa serie ha base 8 cm. Quale altezza deve avere?
8. Se il lato di un quadrato passa da 3 cm a 6 cm, prevedi l’area prima di disegnare il punto. Di quanto aumenta rispetto all’area iniziale?
9. Vero o falso? «Se un grafico passa per l’origine, rappresenta una proporzionalità diretta». Motiva con un esempio del capitolo.
10. Per x uguale a 1, 2, 4 si osservano rispettivamente y uguale a 6, 3, 1,5. Quale delle relazioni studiate è compatibile con i dati? Mostra il controllo numerico.
11. Una grandezza segue y = k·x². Se x si dimezza, y diventa la metà, un quarto o il doppio? Motiva.

## Note

[^1]: La retta mostra il modello matematico continuo; nell’acquisto di quaderni interi si usano soltanto le quantità intere. La proporzionalità diretta può anche avere k negativo quando le grandezze ammettono valori con segno: il suo criterio generale resta il rapporto costante.

---

## Materiali e provenienza — sezione di servizio della bozza

Da non trasferire nel contenuto didattico visibile.

- Fonte editoriale: grafici_piano_cartesiano_it.html v8, sezioni diretta, intercetta, inversa e quadratica.
- Conservati i cinque quesiti originali 3–7 nelle domande 1, 3, 5, 6 e 8. Quesiti originali 1–2 assegnati al capitolo 8.
- Tabelle costruite dai modelli dichiarati; nessuna misura sperimentale o tariffa commerciale attuale.
- Formule generali, unità delle costanti e formula della pendenza esplicitate rispetto al sorgente. Il termine affine distingue correttamente la retta con intercetta non nulla; nessuna generica funzione quadratica è chiamata automaticamente proporzionalità quadratica.
- Copertina, immagine del quaderno e immagine della consegna ancora da scegliere. Grafici e figure geometriche indicati dai segnaposto non sono ancora realizzati nel nuovo capitolo.
- Il vecchio grafico comparativo conserva numeri astratti; grafico tariffario con unità separato.
- Testo da revisionare; nessun HTML o pubblicazione avviati.
