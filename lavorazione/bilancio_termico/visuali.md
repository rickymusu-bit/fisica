# Proposta delle visuali — Il bilancio termico

Versione v1 · 19 ottobre 2026, ore 18:18 (Europe/Rome).

## Apertura proposta

«Mescolando acqua calda e acqua fredda, come possiamo prevedere la temperatura finale?»

Un unico fenomeno guida: due quantità d’acqua inizialmente a temperature diverse vengono mescolate in un recipiente isolante. Prima si prevede che la temperatura finale sia compresa fra quelle iniziali; poi si spiega perché non sia sempre la media aritmetica. L'energia ceduta dall'acqua calda è assorbita dall'acqua fredda. Non presentare una fotografia come misura di temperature o prova quantitativa.

## Proposte da concordare prima della bozza

| ID | Che cosa mostrare | Domanda e collocazione |
| --- | --- | --- |
| COP-01 | Fotografia di acqua versata da una caraffa in un recipiente, con soggetti riconoscibili e composizione semplice. | Introduce il mescolamento; copertina distinta dalle immagini interne. Nessun valore dedotto dalla foto. |
| FIG-01 | Fotografia diversa di due recipienti con acqua e di un recipiente isolante per la miscela; possibile sequenza prima/dopo. | Accanto all'apertura e al bilancio: identificare le due masse e il sistema. Non occorre vapore visibile né una temperatura leggibile. Eventuali dati ed etichette saranno quelli del modello concordato, esplicitamente distinti da misure reali. |
| GRA-01 | Grafico dei calori scambiati in funzione della temperatura finale ipotizzata: retta Q_c = m_c · c_c · (T − T_c) e retta −Q_f = m_f · c_f · (T_f − T); l'intersezione individua l'equilibrio. | Dopo l'introduzione del bilancio, permette di leggere energia ceduta e assorbita e comprendere l'unicità della temperatura finale. Assi T (°C) ed energia (J o kJ); dati scelti e dichiarati come modello, non misure. Nessun grafico temporale: il bilancio da solo non determina i tempi. |

La coppia minima di fotografie è COP-01 + FIG-01. L'utente cerca, sceglie e fornisce i file o i collegamenti; nessuna ricerca o generazione avviata. I materiali dell'articolo 3 già esaminati (test Ivy Mike, spiaggia notturna e moto molecolare dell'acqua) non mostrano il mescolamento e non vengono usati come sostituti. Grafico da confermare; può essere omesso per un percorso più leggero, mantenendo foto, formule e ragionamento.

## Percorso scientifico previsto

- Dal mescolamento alla scelta del sistema: le due quantità d'acqua, con scambi verso l'ambiente trascurabili.
- Convenzione Q > 0 per il corpo che assorbe energia e Q < 0 per quello che la cede; Q = m · c · (T_eq − T_in).
- Bilancio Q_c + Q_f = 0: i calori con segno si sommano a zero, i loro valori assoluti coincidono. Non affermare che le variazioni di temperatura siano uguali.
- Temperatura di equilibrio come media pesata dalle capacità termiche: T_eq = (m_c · c_c · T_c + m_f · c_f · T_f)/(m_c · c_c + m_f · c_f), da rendere con frazione orizzontale nella futura bozza e nell'HTML. Per la stessa sostanza, c si semplifica; la media aritmetica vale per capacità termiche uguali.
- Contributo del recipiente, breve e integrato nello stesso fenomeno: Q_rec = C_rec · (T_eq − T_rec,in) e Q_c + Q_f + Q_rec = 0. Se il recipiente parte più freddo della miscela prevista, ne abbassa la temperatura finale. Non introdurre un calorimetro particolare o un'altra applicazione senza concordarne l'immagine.
- Nessun cambiamento di stato, calore latente, dilatazione, velocità dello scambio o nuovo meccanismo di trasmissione. Condizioni brevi e utili nelle note; nessuna ripetizione della teoria dell'articolo 3.
- Domande finali miste, con numero e formulazione da definire nella bozza; nessuna soluzione automatica.

Non proposti video, simulazioni, applicazioni separate o esercizi svolti. Un eventuale esercizio numerico va concordato e richiede schema fisico e interpretazione quantitativa secondo A5.

## Decisioni aperte

Concordare apertura e visuali; ricevere le due fotografie o collegamenti scelti. Il contributo del recipiente è proposto come breve parte del capitolo, già compatibile con il piano ma non ancora approvato nel dettaglio.

Dopo queste scelte: bozza completa in `bozza.md` sullo stesso ramo, approvazione del testo, stima totale ripartita e via esplicito prima della realizzazione HTML. Nessun intervento a main o alla pubblicazione.
