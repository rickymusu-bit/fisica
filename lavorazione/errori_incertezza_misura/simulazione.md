# SIM-07 — Due campioni, misure ripetute e distribuzione dei risultati
Versione v3 — 23 ottobre 2026. Implementata nell’HTML v1; immagini di bilancia e campioni in attesa. Sostituito lo scenario a un solo campione e U assegnata.

## Decisione dell'utente
Bilancia con portata e sensibilità date, proprietà fisse. Due attività: misurare ripetutamente una massa nota per stimare l'errore e una massa ignota per stimare l'incertezza. Grafico sotto la bilancia per mostrare distribuzione dei punti, errore e incertezza.
L'utente precisa: «No allora metti media e semi dispersione nel cap 7». Media e semidispersione entrano nel testo e nell'attività del 7; i contenuti dell'ex capitolo 8 sulle misure ripetute sono trasferiti qui. Il precedente capitolo autonomo sulle misure ripetute è eliminato: il piano passa a undici capitoli e i successivi diventano 8–11. Superati il divieto precedente di media e semidispersione, e lo scenario con U = 3 g assegnata.

## Modello proposto
Configurazione visibile e non modificabile: portata 500 g, passo leggibile q = 1 g, sensibilità del sensore S = 1 mV/g e risposta circa 1 s simulato. Chiarire che “sensibilità” nel linguaggio scolastico può indicare il passo, mentre qui distinguiamo i due concetti.
Due campioni: A con riferimento dichiarato 100 g; B con massa interna 125 g, nascosta in interfaccia, tabelle e grafici. Nessun comando per rivelare il riferimento B o calcolare il suo errore effettivo.
La bilancia è regolata sullo zero; modello senza offset sistematico residuo, con piccoli disturbi sintetici a media nulla. Un disturbo estratto per ogni acquisizione resta fermo fino alla nuova misura; si attende la risposta e si arrotonda al grammo. Ampiezza proposta ±3 g equivalenti. Non rigenerare un rumore “fortunato” per forzare un errore non nullo. Proprietà e massa B non cambiano passando da A a B o ripristinando.
Questo modello limita l'attività all'incertezza da ripetibilità e lettura; la verifica A non dimostra in generale l'assenza di effetti sistematici su tutti i carichi.

## Protocollo
- Selezionare A o B; rimuovere/riposizionare il campione a ogni nuova misura. Leggere e registrare, massimo 10 letture per serie, almeno 5 per il confronto guidato.
- Serie separate e conservate al cambio campione; mostrare sempre unità e numero di letture. L'alunno inserisce le stime prima del feedback; disponibile un aiuto esplicito.
- Per A: stimare il valore centrale con la media, confrontarlo con 100 g, calcolare e = media − riferimento; distinguere errore delle singole letture ed errore del valore medio. Valore assoluto e percentuale disponibili dopo la risposta.
- Per B: stimare il valore centrale dalla media, osservare la dispersione e confrontarla con il passo leggibile. Nessun errore effettivo mostrato; non usare il riferimento A come se fosse il riferimento B.

## Regola didattica proposta per l'incertezza
Media = somma delle letture / numero di letture. Semidispersione d = (massimo − minimo)/2. L'alunno calcola entrambe per ciascuna serie; non sostituire la semidispersione con la massima distanza dalla media.
Per la serie A l'errore del risultato è e = media − riferimento. Per B, criterio scolastico dichiarato U_did = max(q, d): la maggiore fra passo leggibile e semidispersione. L'alunno compila media, d e U, poi confronta con il suggerimento. Scrittura m = (media ± U_did) g, con arrotondamento finale coerente e senza arrotondare i passaggi intermedi.
U_did è una stima didattica provvisoria nel modello con zero regolato, non una valutazione metrologica completa, una probabilità assegnata o una garanzia su letture future. La semidispersione dipende dalle prove raccolte, non è una proprietà fissa dello strumento. Letture coincidenti danno d = 0 ma non U = 0.
La fascia centrata sulla media non coincide necessariamente con l'intervallo minimo–massimo: metà del range non è in generale la distanza dalla media agli estremi. Il grafico mostra entrambi senza sovrapporli semanticamente; non allargare artificialmente d per includere tutti i punti attorno alla media.
Non equiparare automaticamente risoluzione e incertezza né applicare la regola a strumenti con effetti sistematici non controllati. Se A mostra uno spostamento persistente rispetto al riferimento, segnalare che occorre controllare lo strumento prima di fidarsi della stima per B.

## Grafico sotto la bilancia
Grafico a punti sulla scala delle masse: asse orizzontale massa indicata (g); punti sovrapposti verticalmente quando le letture coincidono, un punto per misura. La sovrapposizione è dichiarata “numero di letture allo stesso valore”, non una seconda grandezza fisica. Nessuna curva gaussiana aggiunta senza giustificazione.
Due serie selezionabili e confrontabili con identica scala e unità, etichette A/B e simboli distinti; passare da una serie all'altra non cancella dati. Proposta di scala comune 90–140 g, espandibile soltanto se necessario e sempre uguale per entrambe.
A: linea del riferimento, linea della media e segmento con segno per e. B: linea della media, estremi delle letture e fascia simmetrica ±U, con estremi numerici; etichetta separata per d come metà dell'ampiezza minimo–massimo. Per B il vero valore interno non deve apparire neppure come linea, titolo, suggerimento accessibile o valore di default di un campo.
Punti grezzi, media e fascia U distinti per etichette e tratto, non solo colore. La fascia non è il min–max né una campana di probabilità. Esempio di letture asimmetriche obbligatorio nel controllo del grafico.
Tabella numerica accessibile equivalente, descrizione del grafico aggiornata a ogni registrazione, tastiera, focus visibile e vista mobile con composizione invariata. Nessun asse o punto fittizio prima delle misure.

## Risorse e verifica
Stesse immagini pertinenti di bilancia e campioni, da fornire/scegliere e con diritti verificati; nessun dispositivo o pesetto sostituito con una sagoma astratta. Il grafico quantitativo sarà costruito via codice dai dati simulati.
Controlli: ripetizioni indipendenti, parametri fissi, separazione delle serie, media, semidispersione, U minima q, distinzione e/U, unità, scala comune, dati coincidenti e asimmetrici, reset, feedback, offline, tastiera e smartphone. Risultato nullo per e ammesso; assenza di dispersione osservata non equivale a certezza.
Carico basso, fino a 20 punti complessivi. Stima preliminare condivisa 2–3 ore, ripartita in SIM-06; da consolidare dopo le bozze approvate. Nessun HTML, codice, merge o deployment avviato.

## Implementazione autorizzata

L’utente dà il via con «Ok vai». Modello e comandi realizzati nel codice condiviso del capitolo 6, incorporati nei due HTML. Grafico del 7 con panoramica e ingrandimento del tema comune. Immagini pertinenti di bilancia, pesetti e campioni in attesa: la simulazione usa per ora controlli testuali e non inventa gli oggetti. Specifiche di progetto sopra conservate; fase corrente e verifiche in stato.md.

## Immagini generate e display attivo

Bilancia digitale e pesetto generati su richiesta dell’utente; originali nella lavorazione del capitolo 6 e relative schede di provenienza. Varianti dei pesetti riutilizzano l’originale con dimensioni proporzionate alla radice cubica della massa; etichette HTML separate. Display numerico nella finestra della bilancia e carichi visualizzati sul piatto. Il campione B è privo di etichetta di massa. Immagini incorporate una sola volta tramite definizioni SVG condivise, con riferimenti interni per le istanze; nessuna dipendenza esterna.

## Specifica corrente: sensibilità in grammi e pesetti ingranditi

La richiesta più recente sostituisce l’interfaccia del guadagno elettrico: niente millivolt, nessun controllo separato del segnale. Nel 6 «Sensibilità (passo leggibile)» agisce sul parametro step, in grammi (1, 20, 50); il guadagno interno resta fisso a 1. Nel 7 proprietà fisse con passo di 1 g. Confronto teorico fra sensibilità e risoluzione conservato; nota sul diverso uso scolastico del termine. Pesi più grandi sul piatto e nei selettori, scritte dall’aspetto inciso sul carico, riferimento 100 g etichettato e campione B senza massa nota. Funzionamento nell’HTML scaricato confermato dall’utente.

## Interfaccia didattica corrente

Capitolo 6: Accuratezza e Precisione sostituiscono i nomi tecnici dello spostamento dello zero e dei disturbi. Slider 0–5, valori più alti = prestazione migliore. Mappatura interna: offset=5−accuratezza e noise=5−precisione; reset a 5 per entrambi. Le uscite e il registro usano livelli qualitativi, senza percentuali di accuratezza prive di significato metrologico. Nel 7 etichette semplicemente «Incertezza U», nessuna qualificazione didattica/scolastica ripetuta; cenno alla deviazione standard solo nella nota finale.

## Due attività autonome nel capitolo 7

SIM-07-U: campione ignoto fisso, registro e calcoli di media/d/U, grafico con punti, media, estremi e fascia ±U. SIM-07-E: campione noto di 100 g fisso, registro e calcoli di media/errore, grafico con punti, media, riferimento ed errore. Ogni istanza mantiene stato e timer propri; reset e cancellazione non agiscono sull’altra. Nessun selettore di campione e nessun grafico combinato. Formule e parametri numerici immutati.

## Revisione grafici e calcoli

Scala automatica vicina ai dati, con margine per riferimento o estremi della fascia U e intervallo minimo 8 g. Grafici SVG con larghezza corrispondente alla larghezza effettiva, altezza 282 px e testi almeno 14 px; ResizeObserver mantiene leggibilità sui cambi di viewport. Dominio uguale per gli stessi dati; tre etichette numeriche principali su mobile. Rimossi zoom, campi per le risposte, validazione, confronto su richiesta e aiuto. Statistiche calcolate e mostrate nel grafico dopo ogni lettura; esercizi nelle domande finali del capitolo 7.
