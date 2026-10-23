# Capitolo 7 — Errori e incertezza di misura: proposta
Versione v1 — 23 ottobre 2026 (Europe/Rome). Proposta da concordare prima della bozza.

## Domanda e confini
Il cronometro mostra 2,40 s: quanto sappiamo del tempo misurato, e possiamo già dire di quanto abbiamo sbagliato? Distinguere la variabilità delle letture, gli spostamenti rispetto a un riferimento e l'informazione espressa dall'incertezza.
Fonte: `strumenti_errori_incertezza_it.html` v7, sezioni `#errori` e `#confronto`; blob `1d65637b40f2af68e1e1ff55c7d1710259b6087b`.

## Progressione proposta
1. Dalla lettura al risultato: strumento, operatore e condizioni contribuiscono alla misura. Breve richiamo al capitolo 6, senza ripeterne le definizioni.
2. Errori casuali, sistematici e sbagli grossolani: variazioni imprevedibili nell'avvio del cronometro, zero spostato della bilancia, trascrizione errata. Gli esempi restano sviluppati accanto alle foto pertinenti; un dato lontano dagli altri richiede un controllo e non si scarta automaticamente.
3. Bersagli: distinguere dispersione e spostamento rispetto al centro noto; ripetere e fare la media non elimina uno spostamento sistematico. Nessun calcolo della media in questo capitolo.
4. Incertezza: presentare x = (x_m ± U), con valore attribuito x_m e incertezza assoluta U nella stessa unità. La scrittura comunica l'estensione dell'incertezza dichiarata; non è automaticamente un limite invalicabile dell'errore. L'incertezza comprende le informazioni disponibili su strumento, metodo e condizioni.
5. Errore rispetto al riferimento: e = x_m − x_rif, valore assoluto |e|, errore relativo |e| / |x_rif| per riferimento non nullo, ed errore percentuale. Definire simboli, unità e segno; frazioni orizzontali nell'HTML. Non confondere l'errore assoluto con U.
6. Conservare il confronto originale fra 2,40 s e riferimento 2,50 s: e = −0,10 s, |e| = 0,10 s, errore relativo 0,04 e percentuale 4%. Lo scarto equivale a un venticinquesimo del tempo di riferimento. Per rendere il capitolo autonomo, 2,40 s sarà un risultato assegnato, senza ricostruire qui la media. L'eventuale U = 0,09 s sarà dichiarata assegnata a scopo illustrativo, non ricavata dalle cinque letture. Il fatto che |e| superi U invita a controllare la valutazione e i possibili effetti sistematici, ma non prova da solo una causa specifica.
7. Domande finali: conservare il quesito originale 5 sui bersagli e il 7 sulla possibilità di stimare l'incertezza senza conoscere l'errore. Aggiungere classificazioni motivate, lettura di ±U e interpretazione del segno dell'errore. Numero e formulazione definitivi nella bozza.

La tabella delle cinque letture, la linea dei numeri, la media, la semidispersione e la regola scolastica del maggiore fra dispersione e passo restano nel capitolo 8. Nessun algoritmo generale per l'incertezza è introdotto nel 7.

## Visuali proposte
| ID | Materiale | Funzione e posizione |
| --- | --- | --- |
| COP-07 | Foto originale del sismografo | Copertina intera senza zoom, non ripetuta nel corpo; introduce il problema di interpretare le variazioni |
| FIG-07-1 | Infografica originale dei quattro bersagli | Dispersione e spostamento; centro come riferimento noto, non “valore vero” conosciuto in ogni misura |
| FIG-07-2 | Foto originale della bilancia digitale | Zero spostato e registrazione delle letture. Nessun nuovo valore sovrapposto al display |
| TAB-07-1 | Prospetto da concordare: lettura / incertezza / riferimento / errore | Separare informazioni disponibili e quantità calcolabili, accanto alle formule |
| SCH-07-1 | Composizione da concordare con la foto originale del cronometro ed etichette numeriche | Situazione dell'esempio temporale prima dei calcoli; tempo attribuito 2,40 s e riferimento indipendente 2,50 s, dati illustrativi. Non rappresentare un secondo dispositivo inventato |

La foto del sismografo resta soltanto in copertina, il cronometro soltanto nello schema del corpo. La traccia non sarà presentata come prova di rumore o errore: può contenere segnale reale. Scelta da concordare; non realizzare lo schema prima della decisione.

I diritti delle immagini storiche risultano non documentati nello snapshot del sorgente. Verificare provenienza, licenza e leggibilità dell'infografica, senza ridisegnarla o tradurla autonomamente. Se non utilizzabile, concordare un confronto numerico equivalente o chiedere immagini sostitutive. Non cercare né generare nuove immagini in questa fase.

Nessun video o simulazione proposto. L'esempio temporale resta integrato nella teoria; nessuna sezione di esercizi svolti aggiunta automaticamente.

## Ripartizione e regole
Quesiti originali 5 e 7 al capitolo 7; 1–4 al 6; 6 riservato all'8. Tema comune Stringhe v24. Riferimenti: MASTER_PROMPT.md v69.11, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, docs/visual-guidelines.md v1.0.0.
