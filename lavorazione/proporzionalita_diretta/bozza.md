# Le relazioni di proporzionalità

Versione della bozza: v5 — 24 ottobre 2026.
Area: Introduzione alla fisica e alla misura.

[C9-COP — Hyperbolic_orthogonal_dodecahedral_honeycomb.png scelta dall’utente; copertina intera, senza zoom.]

## Raddoppiare una quantità

Immaginiamo di acquistare libri della stessa collana, tutti a 15 € l’uno. Se ne compriamo due spendiamo 30 €, se ne compriamo tre spendiamo 45 €. Il prezzo cresce insieme al numero di libri: possiamo prevederlo prima di arrivare alla cassa. Ma due grandezze che aumentano insieme seguono sempre questa stessa regola?

[C9-SIT — Schema originale con uno, due e tre libri riconoscibili, prezzo unitario 15 €/libro e totali 15/30/45 €. Nessuna fotografia della biblioteca; didascalia sulle condizioni del prezzo.]

In questo caso il prezzo unitario rimane fisso: non ci sono sconti o quote aggiuntive. Ogni libro aggiunge 15 € alla spesa. I valori seguenti si riferiscono a questo prezzo iniziale; cambiando k nel grafico aggiorneremo anche tabella e punti.

| Numero di libri x | Prezzo y (€) |
|---:|---:|
| 0 | 0 |
| 1 | 15 |
| 2 | 30 |
| 3 | 45 |
| 4 | 60 |

Nella tabella iniziale, dividendo il prezzo per il numero di libri otteniamo sempre 15 €/libro. È questo **rapporto costante** a caratterizzare la **proporzionalità diretta**:

\[
\frac{y}{x}=k
\]

La stessa relazione si scrive:

\[
y=k\cdot x
\]

La **costante di proporzionalità k** esprime quanto y corrisponde a un’unità di x. Nell’acquisto è il prezzo unitario: 15 €/libro. Le sue unità dipendono dalle grandezze confrontate: non è necessariamente un numero senza unità.

Raddoppiando x, anche y raddoppia; triplicando x, y triplica. Cinque libri costano quindi 75 €, cinque volte il prezzo di uno e 15 € più di quattro libri.

[C9-GRA-D — Punti, retta y = k·x e selettore k = 10/15/20 €/libro, valore iniziale 15. Scale fisse 0–4 libri e 0–80 €. Tabella e punti aggiornati; retta iniziale tratteggiata di confronto. Nessuno zoom. Didascalia su campioni interi e modello continuo.]

Ogni coppia della tabella determina un punto; la retta del modello **passa per tutti quei punti**, perché ciascuna coppia soddisfa la stessa formula. La retta passa anche per l’origine: senza libri la spesa è zero. Non stiamo unendo i punti in un ordine arbitrario: rappresentiamo tutte le coppie che rispettano y = k·x.[^1]

Il rapporto si calcola per x diverso da zero; il valore nello zero si ricava da y = k·x. In un singolo acquisto il prezzo unitario k resta costante. Cambiare k significa confrontare un’altra situazione, con un altro prezzo unitario: non far cambiare il prezzo da un punto all’altro della stessa retta.

Porta k da 15 a 20 €/libro. A parità di quantità, il prezzo totale aumenta: per due libri passa da 30 a 40 €. La retta diventa **più inclinata verso l’alto**, mantenendo fissi assi e scale, e continua a passare per l’origine. Se k scende a 10 €/libro, due libri costano 20 € e la retta si avvicina all’asse orizzontale. La retta tratteggiata conserva il confronto con il prezzo iniziale: qui l’inclinazione cambia perché cambia il modello, non perché abbiamo modificato la scala.

## Stessa distanza, tempi diversi

Un viaggio in treno copre 120 km. Immaginiamo di percorrerli senza fermate, mantenendo una velocità costante: quanto tempo occorre a 60 km/h? E a 120 km/h?

[C9-VIA — Schema ferroviario originale con treno, percorso e due percorrenze: 120 km; 60 km/h → 2 h; 120 km/h → 1 h. Nessuna fotografia della monorotaia. Didascalia: distanza identica, velocità costante e assenza di fermate.]

A 60 km/h il treno percorre 60 km ogni ora: per coprirne 120 servono 2 ore. A 120 km/h basta un’ora. Raddoppiando la velocità, il tempo si dimezza: il percorso è rimasto lo stesso.

| Velocità v (km/h) | Tempo t (h) |
|---:|---:|
| 30 | 4 |
| 40 | 3 |
| 60 | 2 |
| 80 | 1,5 |
| 120 | 1 |

Nella tabella iniziale, in tutte le righe il prodotto della velocità per il tempo vale 120 km. Indicando con d la distanza:

\[
v\cdot t=d
\]

Per ricavare il tempo dividiamo la distanza per la velocità:

\[
t=\frac{d}{v}
\]

La distanza d è costante; v è la velocità e t il tempo di percorrenza. Usando chilometri e chilometri all’ora, otteniamo il tempo in ore: 1,5 h, per esempio, equivale a un’ora e mezza.

Velocità e tempo sono quindi **inversamente proporzionali**. Se la velocità triplica da 40 a 120 km/h, il tempo diventa un terzo: da 3 ore a un’ora.

La forma generale della **proporzionalità inversa** è:

\[
x\cdot y=k
\]

Da cui:

\[
y=\frac{k}{x}
\]

La caratteristica è il **prodotto costante**. Nel viaggio x corrisponde alla velocità, y al tempo e k alla distanza di 120 km.

[C9-GRA-I — Punti e iperbole t = k/v, selettore k = 60/120/180 km, iniziale 120. Scale fisse 0–120 km/h e 0–6 h; tabella e punti aggiornati. Iperbole iniziale tratteggiata, nessuno zoom. Didascalia sul significato della costante-distanza.]

I punti non sono allineati su una retta: appartengono a un ramo di **iperbole**. Ogni punto della curva, anche tra due valori della tabella, rappresenta una coppia velocità–tempo con lo stesso prodotto. La curva scende: una velocità maggiore richiede meno tempo per coprire la stessa distanza. A velocità zero il viaggio non può essere completato, perciò non esiste un tempo di arrivo finito da rappresentare sull’asse verticale.

Nel grafico puoi anche cambiare k, cioè la distanza del viaggio. Con k = 180 km, alla stessa velocità di 60 km/h occorrono 3 h anziché 2 h: la nuova iperbole si trova **più in alto**, a parità di ascissa positiva. Con k = 60 km basta 1 h e la curva si trova più in basso. Per ciascuna distanza resta valida la proporzionalità inversa: raddoppiare la velocità dimezza il tempo. Stiamo confrontando viaggi diversi; non cambiando la distanza durante uno stesso viaggio.

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

Ogni coppia lato–area della tabella è un punto di una **parabola**. Il modello descrive anche i lati intermedi: per esempio, a 1,5 cm corrispondono 2,25 cm². Poiché un lato non è negativo, qui rappresentiamo soltanto la parte della parabola con x non negativo. La curva passa per l’origine, ma non è una retta: il passaggio per l’origine, da solo, non basta a riconoscere una proporzionalità diretta.

Per osservare il ruolo di k anche in questa famiglia, passiamo al modello generale y = k·x²: nel confronto seguente x e y sono numeri senza unità. Non stiamo cambiando la formula dell’area di un quadrato, per la quale k resta 1.

[C9-K-Q — Confronto matematico y = k·x², k = 0,5/1/2, iniziale 1; assi x e y senza unità, scale fisse 0–4 e 0–32. Parabola iniziale tratteggiata; lettura a x = 2; nessuno zoom. Didascalia che distingue il confronto generale dal quadrato.]

A x = 2, y vale 2 con k = 0,5, vale 4 con k = 1 e vale 8 con k = 2. Aumentando k positivo, la parabola sale più rapidamente e appare più stretta attorno all’asse verticale; diminuendolo si allarga. Tutte queste curve passano per l’origine e mantengono la stessa regola di scala: se x raddoppia, y quadruplica. Il valore di k cambia i valori di y, mentre la dipendenza da x² rimane la stessa.

## Domande di verifica

1. Dalla tabella dei libri ricava il costo di un singolo libro. Perché la retta del prezzo attraversa l’origine?
2. Quali unità ha k nell’esempio dei libri? Come cambia la retta se il prezzo passa da 15 a 20 €/libro? Confronta i prezzi di due libri.
3. Quattro libri costano 60 €. Quanto costano sei libri allo stesso prezzo unitario? Spiega il ragionamento.
4. Nel viaggio di 120 km, se la velocità triplica da 40 a 120 km/h, come cambia il tempo di percorrenza? Quale quantità resta uguale?
5. Quanto tempo richiede il viaggio di 120 km a 100 km/h? Esprimi il risultato in ore e minuti. Se k passa a 180 km mantenendo la velocità, l’iperbole si trova più in alto o più in basso? Perché?
6. Se il lato di un quadrato passa da 3 cm a 6 cm, prevedi l’area prima di disegnare il punto. Di quanto aumenta rispetto all’area iniziale?
7. Vero o falso? «Se un grafico passa per l’origine, rappresenta una proporzionalità diretta». Motiva con un esempio del capitolo.
8. Per x uguale a 1, 2, 4 si osservano rispettivamente y uguale a 6, 3, 1,5. Quale delle relazioni studiate è compatibile con i dati? Mostra il controllo numerico.
9. Una grandezza segue y = k·x². Se x si dimezza mantenendo k, come cambia y? Se invece raddoppi k mantenendo x, come cambia y e come cambia il grafico?

## Note

[^1]: La retta mostra il modello matematico continuo; nell’acquisto di libri interi si usano soltanto le quantità intere. Le tabelle di questo capitolo sono costruite dalle formule dichiarate: con dati sperimentali una curva è invece un modello da verificare e non deve necessariamente attraversare ogni punto esattamente. La proporzionalità diretta può anche avere k negativo quando le grandezze ammettono valori con segno: il suo criterio generale resta il rapporto costante.

---

## Materiali e provenienza — sezione di servizio della bozza

- Revisione richiesta: prezzo illustrativo 15 €/libro, schemi originali di libri e treno al posto delle fotografie. Originali fotografici conservati nella lavorazione, senza associazioni nei crediti correnti.
- Copertina geometrica conservata con didascalia identificativa. Schema del quadrato in scala. Tutti i grafici interattivi senza zoom, con etichette leggibili e comandi esterni all’area dei dati.
- Dati e curve derivano da formule esatte, non da misure. Variazione di k autorizzata dalla richiesta: prezzi 10/15/20 €/libro; distanze 60/120/180 km; confronto quadratico astratto k = 0,5/1/2. Scale fisse, riferimento tratteggiato e lettura a x fissato. La variazione cambia modello; ogni curva ha un k costante.
- Gli otto/nove quesiti dei due capitoli mantengono la ripartizione; quelli del 9 sono aggiornati al prezzo e alla variazione della costante. Nessuna intercetta o relazione affine introdotta.
