# Il metodo scientifico
Bozza editoriale v1 — 22 ottobre 2026
Area: Introduzione alla fisica e alla misura
Stato: proposta da approvare; non è un HTML pubblicabile.

[IMMAGINE DI COPERTINA — Fotografia reale di pallina e piano inclinato, da fornire o scegliere; non ripeterla nel corpo.]

Una pallina viene lasciata libera lungo una pista inclinata. Arriva in fondo dopo un certo tempo. Se solleviamo un'estremità della pista, sembra naturale aspettarsi che raggiunga la fine più rapidamente. Ma come possiamo distinguere una previsione affidabile da una semplice impressione? E se la prima prova desse un risultato inatteso?

Per rispondere non basta osservare una volta sola. Occorre formulare una domanda precisa, preparare prove confrontabili e raccogliere risultati che possano anche contraddire l'idea iniziale. Questo è il cuore del metodo scientifico: un modo di conoscere il mondo attraverso ipotesi controllabili e confronti con la realtà.

## Dall'osservazione all'ipotesi

La prima cosa che notiamo è il movimento della pallina. Da questa osservazione nasce una domanda: mantenendo invariato il tratto percorso, un piano più inclinato produce un tempo di discesa minore? La domanda delimita ciò che vogliamo studiare: non tutte le caratteristiche del moto, ma il legame tra inclinazione e tempo.

Possiamo allora formulare un'**ipotesi**: aumentando l'inclinazione, la pallina percorre la stessa distanza in meno tempo. L'ipotesi non è ancora un risultato: è un'idea da sottoporre a verifica. Ne ricaviamo una **previsione** concreta: nella prova con il piano più inclinato, il cronometro dovrebbe indicare un tempo inferiore rispetto alla prova con il piano meno inclinato.

[SCHEMA INTERATTIVO 1 — Sei fasi selezionabili in colonna: osservazione e domanda; ipotesi; previsione; esperimento; analisi dei dati; conclusioni e nuove verifiche. Ogni fase apre, sotto lo schema, un breve testo esplicativo e un esempio riferito alla pallina. Una biforcazione conclusiva illustra «coerente con la previsione → nuove verifiche» e «non coerente → controllo della procedura, revisione e nuova prova». Sempre disponibile alternativa testuale senza JavaScript, controlli da tastiera e lettura su smartphone. Testi contestuali concordati in chat il 22/10/2026.]

## Un esperimento deve permettere il confronto

Se cambiassimo contemporaneamente la pallina, il materiale della pista e la sua inclinazione, non sapremmo a quale cambiamento attribuire un eventuale tempo diverso. Per rendere interpretabile la prova, utilizziamo la stessa pallina, la stessa pista e un tratto di uguale lunghezza. La lasciamo partire da ferma, senza spingerla. Cambiamo soltanto l'inclinazione.

Poi ripetiamo le discese e misuriamo il tempo. La ripetizione è utile perché la partenza e la lettura del cronometro non sono mai perfettamente identiche. Le modalità con cui gli strumenti misurano e le incertezze dei risultati saranno affrontate negli altri capitoli: qui ci interessa soprattutto comprendere perché la procedura deve essere controllata.

[SIMULAZIONE 1 — Piano inclinato con pallina che parte da ferma, lunghezza percorsa invariata, 2–3 inclinazioni predefinite, Avvia/Ripeti, cronometro e tabella dei tempi. Nessun attrito regolabile e nessun grafico posizione/velocità. Il modello dovrà chiarire se la pallina rotola senza slittare o è rappresentata come punto materiale che scivola senza attrito; non confondere i due casi. Valori generati dal modello, non spacciati per misure reali; eventuali tempi dipendenti da un modello deterministico non devono oscillare casualmente a ogni ripetizione. Non programmare prima del via alla realizzazione.]

## Che cosa raccontano i dati?

Immaginiamo di aver registrato alcuni tempi di discesa. Nella tabella del materiale originale, per esempio, le prove su una pista meno inclinata danno 2,2 s, 2,1 s e 2,3 s; con una pendenza maggiore danno 1,5 s, 1,6 s e 1,5 s. **Sono valori illustrativi**, costruiti per ragionare: non vanno presentati come misure effettuate in laboratorio.

[TABELLA 1 — Riutilizzare la tabella originale: percorso di 1,0 m, tre prove per ciascuna delle due inclinazioni, con etichetta visibile «Dati illustrativi».]

I tempi della seconda serie sono inferiori a quelli della prima. Per questa situazione, i dati sono coerenti con la previsione. Ma essere coerenti con una previsione non equivale a dimostrare che essa sarà vera in qualunque circostanza. Possiamo progettare altre prove, cambiare l'inclinazione in modo controllato e verificare se il comportamento continua a ripetersi.

## Quando un risultato ci costringe a cambiare idea

Una buona ipotesi deve poter essere **messa in difficoltà** da un'osservazione possibile. Se sosteniamo che, a parità di condizioni, aumentando l'inclinazione il tempo diminuisce, dobbiamo ammettere la possibilità che una prova accurata mostri il contrario. Questo requisito viene chiamato *falsificabilità*.

Se il risultato non coincide con la previsione, non scartiamo subito l'intera spiegazione. Controlliamo la procedura, l'apparato, le condizioni della prova e le misure. Se la differenza resiste ai controlli, potrebbe essere necessario correggere o abbandonare l'ipotesi. Il metodo scientifico non è una scala che porta automaticamente dall'ipotesi alla verità: è un percorso in cui le idee vengono continuamente confrontate con nuove prove.

Galileo Galilei è una figura centrale nello sviluppo dello studio sperimentale del moto; Karl Popper ha evidenziato il ruolo delle prove capaci di mettere in discussione le ipotesi. I loro contributi non trasformano però la ricerca scientifica in una ricetta immutabile: nella pratica, osservazioni, modelli, domande ed esperimenti si influenzano reciprocamente.

## Domande di verifica

1. Nel confronto tra le due inclinazioni, quali condizioni bisogna mantenere uguali? Spiega perché.
2. Osserva la tabella illustrativa: quale previsione è sostenuta dai dati? Puoi affermare che valga in ogni circostanza?
3. Perché ripetere la misura del tempo è più utile che registrare un'unica prova?
4. Nello schema, che cosa succede quando l'ipotesi non è confermata? Perché anche un risultato inatteso è utile?
5. Indica un risultato sperimentale che metterebbe in difficoltà l'ipotesi sulla pendenza. Quali controlli faresti prima di trarre una conclusione?
6. Vero o falso? «Se dieci esperimenti sono in accordo con un'ipotesi, questa non potrà più essere smentita». Motiva la risposta.

---

## Note di lavorazione — non includere nel testo pubblico

- La scelta del modello dinamico della simulazione è da formalizzare prima della programmazione. La soluzione più lineare è una pallina idealizzata che scivola senza attrito, con accelerazione costante g sin(θ) lungo la pista; se la grafica la mostra in rotazione, questo modello sarebbe incoerente e occorrerebbe introdurre il rotolamento. Evitare la rotazione visiva nell'idealizzazione scelta.
- A parità di lunghezza inclinata L e partenza da ferma, per il modello senza attrito: t = sqrt(2L/(g sin θ)). La formula non è necessaria nel testo del capitolo.
- La tabella esistente rappresenta un esperimento illustrativo e non deve essere numericamente ricavata dalla simulazione senza verificarne la compatibilità.
- Nessun ritratto storico o nuova fotografia è autorizzato automaticamente. Schema nuovo approvato come comportamento, non ancora come resa grafica.
- HTML, interazione e anteprima richiedono la successiva fase di approvazione e il via secondo il master.
