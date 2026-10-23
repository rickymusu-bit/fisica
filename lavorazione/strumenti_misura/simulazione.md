# SIM-06 — Esplorare le proprietà dello strumento
Versione v1 — 23 ottobre 2026. Progettazione richiesta dall'utente; nessun codice ancora realizzato.

## Decisione e obiettivo
L'utente richiede due versioni: nel capitolo 6 una simulazione per le proprietà, nel 7 una versione a proprietà fisse per errore e incertezza. Usare la stessa bilancia virtuale per rendere confrontabili le attività. L'alunno sceglie una massa campione, effettua una lettura e modifica una proprietà alla volta.

## Modello proposto
Massa campione dichiarata, in grammi. Portate selezionabili 200 g / 500 g / 1000 g; passi visualizzati 1 g / 5 g / 10 g; risposta rapida o lenta (0,5 s / 2 s). Fuori portata: segnalazione esplicita e registrazione disabilitata, senza simulare danni.
La lettura si avvicina progressivamente al valore di equilibrio; il comando registra anche il tempo trascorso e distingue una lettura anticipata da una stabilizzata. Zero spostato e piccole variazioni casuali attivabili separatamente, inizialmente assenti. Quantizzazione al passo selezionato dopo la risposta del sensore; valori e fenomeni sono simulati, non specifiche di una bilancia reale.

Per la sensibilità: pannello secondario “Segnale del sensore”, con I in mV e S selezionabile 1 oppure 2 mV/g. Modello statico I = S · m; conversione digitale coerente m = I/S. Cambiando S il segnale raddoppia, mentre la massa indicata resta la stessa. Non moltiplicare semplicemente la massa mostrata per simulare una sensibilità maggiore. Spiegare brevemente che mV indica un segnale elettrico; nessuna elettrotecnica richiesta. Il pannello usa valori numerici, senza introdurre un nuovo grafico.
L'offset viene applicato in grammi equivalenti; anche il rumore è espresso in grammi equivalenti e trasformato coerentemente nel segnale. A parità di risoluzione e rumore equivalente, aumentare S non garantisce da solo una misura migliore.

## Comandi e attività
Scegli campione, Appoggia / Rimuovi, Registra lettura, Azzera tabella, Ripristina. Parametri di portata, risoluzione, risposta e sensibilità modificabili; offset e disturbi in due controlli separati.
Quando cambia la configurazione, aprire una nuova serie identificata senza mescolare letture con proprietà diverse. Campione e configurazione restano visibili. Tabella: campione, lettura, unità, stato stabilizzato/anticipato e configurazione.
Attività: prevedere l'effetto, cambiare un parametro, registrare e confrontare. Precisione e accuratezza emergono confrontando letture raccolte o spostate rispetto alla massa nota.
Usare la foto della bilancia scelta per il capitolo quando i diritti saranno verificati, senza inventare un nuovo oggetto geometrico. Controlli HTML e pannelli numerici costituiscono l'interfaccia; non alterare il display della fotografia.

## Fattibilità e limiti
JavaScript standard incorporato, offline, tastiera e smartphone, niente librerie o rete. Carico di calcolo basso; poche letture e aggiornamenti, massimo 20 registrazioni per serie. Riduzione del movimento: transizione mostrata con stato e valori temporizzati, senza effetti ornamentali. Tempo simulato dichiarato, mai usato come misura delle prestazioni del dispositivo dell'alunno.
Modello intenzionalmente semplice; rumore sintetico e risposta didattica non riproducono una specifica bilancia commerciale.
Stima preliminare con SIM-07: 90–150 minuti complessivi di lavoro, esclusa l'attesa delle immagini e delle risposte. Indicativamente 20–35 min modello, 30–45 min interfacce, 15–25 min integrazione e 25–45 min verifiche/salvataggio. Stima da consolidare dopo le bozze approvate e prima del via alla realizzazione secondo B1.1–B2.
Questa decisione autorizza la progettazione e l'inserimento del segnaposto nella bozza; non sostituisce l'approvazione del testo e il via all'HTML. Nessuna programmazione avviata.
