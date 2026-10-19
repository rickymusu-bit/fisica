# Proposta delle visuali — Il bilancio termico

Versione v2 · 19 ottobre 2026, ore 21:27 (Europe/Rome).

## Fenomeno scelto e apertura proposta

«Quanto si raffredda il caffè quando aggiungiamo il latte?»

L’utente ha scelto di mescolare caffè e latte, approssimando il calore specifico di entrambi a quello dell’acqua. Il fenomeno e questa approssimazione sono concordati; la formulazione della domanda è una proposta adattata alla scelta. Caffè inizialmente più caldo del latte: l’energia ceduta dal caffè viene assorbita dal latte. Prima si prevede che la temperatura finale sia compresa fra quelle iniziali; poi si spiega perché non sia sempre la media aritmetica. Non presentare una fotografia come misura di temperature o prova quantitativa.

## Proposte da concordare prima della bozza

| ID | Che cosa mostrare | Domanda e collocazione |
| --- | --- | --- |
| COP-01 | Fotografia di latte versato nel caffè, con soggetti riconoscibili e composizione semplice. | Introduce il mescolamento; copertina distinta dalle immagini interne. Nessun valore dedotto dalla foto. |
| FIG-01 | Fotografia distinta dalla copertina con caffè, latte e tazza riconoscibili; possibile sequenza prima/dopo il mescolamento. | Accanto all'apertura e al bilancio: identificare le due masse e il sistema. Non occorre vapore visibile né una temperatura leggibile. Eventuali dati ed etichette saranno quelli del modello concordato, esplicitamente distinti da misure reali. |
| GRA-01 | Grafico dei calori scambiati in funzione della temperatura finale ipotizzata: energia ceduta dal caffè m_caffè · c_acqua · (T_caffè − T) ed energia assorbita dal latte m_latte · c_acqua · (T − T_latte); l'intersezione individua l'equilibrio. | Dopo l'introduzione del bilancio, permette di leggere energia ceduta e assorbita e comprendere l'unicità della temperatura finale. Assi T (°C) ed energia (J o kJ); dati scelti e dichiarati come modello, non misure. Nessun grafico temporale: il bilancio da solo non determina i tempi. |

La coppia minima di fotografie è COP-01 + FIG-01. L'utente cerca, sceglie e fornisce i file o i collegamenti; nessuna ricerca o generazione avviata. I materiali dell'articolo 3 già esaminati (test Ivy Mike, spiaggia notturna e moto molecolare dell'acqua) non mostrano il mescolamento e non vengono usati come sostituti. Grafico da confermare; può essere omesso per un percorso più leggero, mantenendo foto, formule e ragionamento.

## Percorso scientifico previsto

- Dal mescolamento alla scelta del sistema: caffè e latte, inizialmente trascurando gli scambi con ambiente e tazza. Indicare nella nota del modello che si assumono entrambi i calori specifici costanti e uguali a quello dell’acqua; è l’approssimazione esplicitamente richiesta, non un’uguaglianza esatta fra le proprietà delle due bevande. Si trascura il contributo energetico del mescolamento.
- Convenzione Q > 0 per il corpo che assorbe energia e Q < 0 per quello che la cede; Q = m · c · (T_eq − T_in).
- Bilancio Q_caffè + Q_latte = 0: i calori con segno si sommano a zero, i loro valori assoluti coincidono. Non affermare che le variazioni di temperatura siano uguali.
- Con l’approssimazione concordata, il calore specifico comune si semplifica nel bilancio e la temperatura finale è pesata dalle masse:

  \\[T_{\\mathrm{eq}}=\\frac{m_{\\mathrm{caffè}}\\cdot T_{\\mathrm{caffè}}+m_{\\mathrm{latte}}\\cdot T_{\\mathrm{latte}}}{m_{\\mathrm{caffè}}+m_{\\mathrm{latte}}}\\]

  La media aritmetica vale per masse uguali nel modello adottato. Usare le masse, senza sostituire automaticamente i volumi in millilitri: l’approssimazione sul calore specifico non stabilisce l’uguaglianza delle densità. Richiamare il peso delle capacità termiche quando si interpreta il caso generale, senza appesantire la derivazione.
- Contributo del recipiente, breve e integrato nello stesso fenomeno: Q_rec = C_rec · (T_eq − T_rec,in) e Q_caffè + Q_latte + Q_rec = 0. Se il recipiente parte più freddo della miscela prevista, ne abbassa la temperatura finale. Non introdurre un calorimetro particolare o un'altra applicazione senza concordarne l'immagine.
- Nessun cambiamento di stato, calore latente, dilatazione, velocità dello scambio o nuovo meccanismo di trasmissione. Condizioni brevi e utili nelle note; nessuna ripetizione della teoria dell'articolo 3.
- Domande finali miste, con numero e formulazione da definire nella bozza; nessuna soluzione automatica.

Non proposti video, simulazioni, applicazioni separate o esercizi svolti. Un eventuale esercizio numerico va concordato e richiede schema fisico e interpretazione quantitativa secondo A5.

## Decisioni aperte

Caffè e latte e approssimazione dei calori specifici scelti dall’utente. Ricevere le due fotografie o i collegamenti scelti e concordare le visuali rimanenti. Il contributo del recipiente è proposto come breve parte del capitolo, già compatibile con il piano ma non ancora approvato nel dettaglio.

Dopo queste scelte: bozza completa in `bozza.md` sullo stesso ramo, approvazione del testo, stima totale ripartita e via esplicito prima della realizzazione HTML. Nessun intervento a main o alla pubblicazione.
