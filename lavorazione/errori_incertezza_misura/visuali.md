# Capitolo 7 — Errori e incertezza di misura: proposta
Versione v6 — 23 ottobre 2026 (Europe/Rome). Impostazione e visuali approvate con «Ok»; bozza testuale v4 con simulazione proposta.

## Domanda e confini
Il cronometro mostra 2,40 s: quanto sappiamo del tempo misurato, e possiamo già dire di quanto abbiamo sbagliato? Distinguere la variabilità delle letture, gli spostamenti rispetto a un riferimento e l'informazione espressa dall'incertezza.
Fonte: `strumenti_errori_incertezza_it.html` v7, sezioni `#errori` e `#confronto`; blob `1d65637b40f2af68e1e1ff55c7d1710259b6087b`.

## Progressione proposta
1. Dalla lettura al risultato: strumento, operatore e condizioni contribuiscono alla misura. Breve richiamo al capitolo 6, senza ripeterne le definizioni.
2. Errori casuali, sistematici e sbagli grossolani: variazioni imprevedibili nell'avvio del cronometro, zero spostato della bilancia, trascrizione errata. Gli esempi restano sviluppati accanto alle foto pertinenti; un dato lontano dagli altri richiede un controllo e non si scarta automaticamente.
3. Bersagli: distinguere dispersione e spostamento rispetto al centro noto; ripetere e fare la media non elimina uno spostamento sistematico. Il calcolo della media è sviluppato più avanti nel capitolo.
4. Incertezza: presentare x = (x̄ ± U), con valore attribuito x̄ e incertezza assoluta U nella stessa unità. La scrittura comunica l'estensione dell'incertezza dichiarata; non è automaticamente un limite invalicabile dell'errore. L'incertezza comprende le informazioni disponibili su strumento, metodo e condizioni.
5. Errore rispetto al riferimento: e = x̄ − x_rif, valore assoluto |e|, errore relativo |e| / |x_rif| per riferimento non nullo, ed errore percentuale. Definire simboli, unità e segno; frazioni orizzontali nell'HTML. Non confondere l'errore assoluto con U.
6. Conservare il confronto originale fra 2,40 s e riferimento 2,50 s: e = −0,10 s, |e| = 0,10 s, errore relativo 0,04 e percentuale 4%. Lo scarto equivale a un venticinquesimo del tempo di riferimento. Il valore 2,40 s è ora ricavato come media delle cinque letture originali. U = 0,09 s sarà ricavata dalle cinque letture originali con il criterio scolastico, dopo media e semidispersione. Il fatto che |e| superi U invita a controllare la valutazione e i possibili effetti sistematici, ma non prova da solo una causa specifica.
7. Domande finali: conservare i quesiti originali 5 sui bersagli, 6 su media e semidispersione, 7 su errore e incertezza. Aggiungere classificazioni motivate, lettura di ±U e interpretazione del segno dell'errore. Numero e formulazione definitivi nella bozza.

La richiesta più recente riunisce nel 7 misure ripetute, media, semidispersione e incertezza. Trasferire tabella e grafico delle cinque letture dalla sezione #incertezza del sorgente, e spiegare il criterio scolastico U = max(d,q) con i suoi limiti. Non resta un capitolo separato sulle misure ripetute.

## Visuali proposte
| ID | Materiale | Funzione e posizione |
| --- | --- | --- |
| COP-07 | TV noise.jpg, scelta dall'utente | Copertina intera senza zoom, non ripetuta nel corpo; introduce il rumore come disturbo |
| FIG-07-1 | Infografica originale dei quattro bersagli | Dispersione e spostamento; centro come riferimento noto, non “valore vero” conosciuto in ogni misura |
| FIG-07-2 | Foto originale della bilancia digitale | Zero spostato e registrazione delle letture. Nessun nuovo valore sovrapposto al display |
| TAB-07-1 | Prospetto concordato: lettura / incertezza / riferimento / errore | Separare informazioni disponibili e quantità calcolabili, accanto alle formule |
| SCH-07-1 | Composizione concordata con la foto originale del cronometro ed etichette numeriche | Situazione dell'esempio temporale prima dei calcoli; tempo attribuito 2,40 s e riferimento indipendente 2,50 s, dati illustrativi. Non rappresentare un secondo dispositivo inventato |

La foto del rumore televisivo resta soltanto in copertina, il cronometro soltanto nello schema del corpo. Il televisore non è presentato come strumento per misurare il tempo né il rumore televisivo come errore numerico della misura. Scelta approvata; realizzazione dello schema dopo il via all'HTML.

I diritti delle immagini storiche risultano non documentati nello snapshot del sorgente. Verificare provenienza, licenza e leggibilità dell'infografica, senza ridisegnarla o tradurla autonomamente. Se non utilizzabile, concordare un confronto numerico equivalente o chiedere immagini sostitutive. Non cercare né generare nuove immagini in questa fase.

Proposta iniziale senza simulazioni superata dalla richiesta esplicita: aggiunta SIM-07, bilancia virtuale con proprietà fisse per errore e incertezza. Nessun video. L'esempio temporale resta integrato nella teoria.

## Ripartizione e regole
Quesiti originali 5, 6 e 7 al capitolo 7; 1–4 al 6. Tutti i quesiti conservati senza duplicazione. Tema comune Stringhe v24. Riferimenti: MASTER_PROMPT.md v69.11, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, docs/visual-guidelines.md v1.0.0.

## Copertina corrente scelta esplicitamente

COP-07: [TV noise.jpg](https://commons.wikimedia.org/wiki/File:TV_noise.jpg), Mysid. Pubblico dominio per dichiarazione dell'autore (PD-self). La richiesta diretta dell'utente sostituisce la proposta precedente del sismografo. [File indicato dall'utente](https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a8/TV_noise.jpg/1920px-TV_noise.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail). Conservare proporzioni e immagine intera, nessun ritaglio o zoom. Provenienza e diritti della copertina documentati; il punto aperto sui diritti riguarda ancora le immagini storiche del corpo. Nessuna immagine alternativa cercata o generata.

## Simulazione richiesta

[Specifica corrente](simulazione.md). Attività e segnaposto nella bozza v3; proprietà regolabili nel 6 e fisse nel 7. Stesso modello di base e stessa immagine pertinente della bilancia, da integrare dopo verifica dei diritti o scelta di una sostituzione fornita dall'utente. Nessuna immagine sostitutiva cercata o generata e nessuna programmazione avviata.

## Interfaccia e struttura aggiornate su richiesta

SIM-06: bilancia con pesetti di masse differenti; slider sotto la bilancia per le proprietà. SIM-07: bilancia a proprietà fisse, massa di riferimento nota e massa ignota, misure ripetute e grafico a punti sotto la bilancia. [Specifica corrente](simulazione.md). Nel 7 media, semidispersione, incertezza ed errore sono sviluppati in un unico capitolo; eliminata la precedente separazione con l'8. Il grafico distingue punti, media, riferimento, errore, estremi e fascia U; nessun valore di riferimento nascosto esposto per il campione ignoto.

Aggiunti nel 7 TAB-07-2 e GRAF-07-2 dal sorgente originale delle cinque letture. Nuove immagini necessarie per i pesetti da concordare/fornire, senza ricerca o generazione autonoma. Modelli numerici proposti e stima complessiva 2–3 ore da consolidare dopo la revisione dei testi. Nessun codice ancora realizzato.

## Bilancia e pesetti disponibili

Bilancia digitale e pesetti generati su richiesta, incorporati e riutilizzati nelle figure della stessa bilancia. Schede in risorse/immagini.json; originali e provenienze condivisi nella lavorazione del 6. Le simulazioni non richiedono altre fotografie. Restano soltanto le figure di teoria del voltmetro, termometro, cronometro e bersagli.

## Visuali correnti complete — 24 ottobre 2026

La scelta esplicita dell’utente sostituisce le proposte storiche sopra: FIG-06-3 manometro MAXIMATOR 0–2500 bar; FIG-06-4 termometro clinico a colonna; FIG-06-5 e SCH-07-1 cronometro digitale azzerato. Fotografie intere, non modificate, senza zoom o didascalie ridondanti. FIG-07-1: ricreazione autorizzata del confronto Ossila mediante SVG originale, etichette italiane e stesso ordine concettuale delle righe e colonne. Nessuna figura pendente. Metadati nel registro centrale e schede nelle risorse; autorizzazione e controlli nel file di stato.

## Revisione corrente delle didascalie e del carico

Ripristinate le didascalie su richiesta. FIG-06-1b usa la fotografia della bilancia con pomodoro scelta dall’utente; l’illustrazione generata resta nelle simulazioni. I pesetti caricati riportano le masse in sovrapposizione leggibile; il campione ignoto resta identificato solo da B. Sensibilità trattata nel testo con un confronto qualitativo con la risoluzione.

FIG-07-2 corrente: voltmetro analogico con offset negativo scelto dall’utente, Вольтметр_4.jpg, Желуденко Павло, CC BY 4.0. Fotografia intera con didascalia; sostituisce la bilancia della teoria, senza cambiare la simulazione.

Scelta più recente: SCH-07-1 usa la scena U.S. Navy del cronometraggio della corsa, Chris Desmond, pubblico dominio; intera senza zoom. FIG-07-1 resta senza zoom. Soglia di valutazione delle scritte: 14 CSS px nella vista normale mobile.

## Revisione: grafici separati

Sostituito il grafico A/B unico con due grafici autonomi in sezioni distinte. Prima la massa ignota (incertezza), poi la massa nota (errore). Ogni grafico mostra una sola serie e solo le grandezze pertinenti alla propria attività. Le risorse originali della bilancia e del pesetto sono condivise, senza duplicare i file incorporati. Pubblicazione sospesa su richiesta dell’utente.

## Grafici senza zoom, revisione corrente

Entrambi i grafici delle bilance mostrano un intervallo ravvicinato e adattato alle letture; i testi restano almeno 14 px su smartphone. Nessun comando di zoom. Riepiloghi automatici, senza modulo per inserire i calcoli. Anteprime dedicate a 390 e 1440 px aggiornate.
