# SIM-07 — Misurare, dichiarare l'incertezza e confrontare il riferimento
Versione v1 — 23 ottobre 2026. Progettazione richiesta dall'utente; nessun codice ancora realizzato.

## Decisione e confini
Seconda versione della bilancia virtuale di SIM-06, con proprietà fisse. L'alunno effettua e registra misure dello stesso campione e studia errore e incertezza. Nessun controllo per modificare portata, risoluzione, sensibilità, prontezza o disturbi.
Non calcolare media, semidispersione, deviazione standard o riduzione dell'incertezza con il numero di letture: appartengono al capitolo 8 o a sviluppi successivi.

## Modello proposto
Scenario fisso: massa campione 100 g, inizialmente nascosta; portata 500 g, passo 1 g, sensibilità del sensore 1 mV/g e risposta in circa 1 s simulato. Offset +2 g e contributo casuale uniforme fra −1 g e +1 g, rinnovato a ogni misura e poi mantenuto per consentire una lettura stabile. Arrotondamento finale al grammo. Questi parametri sono dati del modello, non misure sperimentali reali.
Proprietà d'uso visibili nella scheda dello strumento; offset effettivo e massa di riferimento nascosti prima del confronto. Il rumore produce letture stabilizzate di 101 g, 102 g oppure 103 g, senza cambiare lo strumento fra le prove.
Ripristina riparte dallo stesso scenario e conserva le proprietà; nessun cambio casuale di offset o campione.

## Attività proposta
1. Appoggiare il campione, attendere la stabilizzazione e registrare una lettura. Ripetere fino a cinque volte per osservare la dispersione.
2. Scegliere una lettura come valore attribuito al risultato; non calcolare automaticamente una media. Domanda guidata: il passo di 1 g basta da solo a conoscere l'incertezza?
3. Aprire la scheda di valutazione: U = 3 g, assegnata per questa attività sulla base dei contributi del modello. L'alunno scrive m = (m_m ± 3) g e indica gli estremi dell'intervallo. Distinguere esplicitamente l'incertezza assegnata dal passo di 1 g e dalla dispersione osservata. Non presentare U come una specifica di accuratezza del costruttore o una tolleranza automaticamente convertibile in incertezza.
4. Mostrare il riferimento 100 g su comando. Calcolare errore con segno, valore assoluto, errore relativo ed errore percentuale sulla lettura selezionata; feedback solo dopo la risposta, conservando i tentativi.
5. Confrontare U con |e| e leggere il significato dei due numeri. Rivelare il modello dello zero spostato: altre letture non cancellano i +2 g.

La scheda può assegnare U prima di conoscere il riferimento, mentre e richiede il riferimento: questo ordine è parte dell'attività. U = 3 g è un parametro didattico dichiarato, non un risultato ricavato dalle cinque letture e non una procedura generale di valutazione dell'incertezza. Nessuna probabilità o garanzia universale attribuita all'intervallo.
Non far inferire l'offset esatto da una sola misura: il pannello finale rivela un dato interno del modello. Non alterare gli errori per garantire una risposta predeterminata.

## Interfaccia e verifiche previste
Stessa fotografia e componenti della versione 6, con configurazione bloccata. Comandi Misura, Registra, Scegli lettura, Scheda dell'incertezza, Mostra riferimento e Ripristina. Prima del riferimento non mostrare errore né “valore vero”; U distinta dall'errore anche nel feedback.
Offline, tastiera e smartphone; evitare annunci continui per i lettori di schermo durante la stabilizzazione. Registro massimo cinque letture. Carico di calcolo basso. Verificare arrotondamento, unità, intervalli, feedback, stato nascosto/rivelato e assenza di modifiche alle proprietà.

Stima condivisa con SIM-06: 90–150 minuti; dipendenze e ripartizione in ../strumenti_misura/simulazione.md. Nessun costo o tempo di calcolo misurato dichiarato. La progettazione è richiesta; testo e via alla realizzazione restano da approvare. Nessun codice o HTML realizzato.
