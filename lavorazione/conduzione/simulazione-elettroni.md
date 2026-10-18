# Proposta ritirata — Conduzione nel metallo con elettroni mobili

**Stato corrente: ritirata su richiesta dell’utente del 18 ottobre 2026, ore 18:28 (Europe/Rome).** È previsto soltanto uno schema statico del metallo con gli elettroni di conduzione, ancora da scegliere/fornire. Nessuna simulazione da programmare; la stima seguente è storica e non si applica al lavoro corrente. Il resto del documento conserva la precedente proposta.

18 ottobre 2026, ore 17:45 (Europe/Rome). **Proposta di modello e stima, non ancora programmata.**

## Richiesta e base riutilizzabile

L’utente non ha trovato un’immagine adeguata e propone di riprendere la simulazione della conduzione con piccoli punti che rappresentano gli elettroni, in moto caotico, capaci di trasferire energia al reticolo più freddo. Questa richiesta riapre la scelta di usare una simulazione e supera il precedente ritiro, ma non costituisce approvazione del modello dettagliato o via alla programmazione.

La fonte v7 contiene un reticolo di 14 colonne e 5 righe (70 punti). Il codice imposta ampiezza e durata delle oscillazioni in base alla posizione; la distribuzione è prefissata e non evolve attraverso scambi di energia. Riutilizzabili reticolo, geometria e impostazione visiva; non basta aggiungere particelle decorative per dimostrare il trasferimento energetico.

## Risultato didattico proposto

Un unico modello qualitativo di conduzione in un metallo, con reticolo e circa 15–25 elettroni mobili distinguibili. Lati inizialmente a diversa energia termica; il lato freddo ha vibrazioni non nulle. Non è un modello generale di tutti gli isolanti né una simulazione quantistica dei metalli. Nessuna nuova sezione sugli isolanti oltre al testo già concordato.

- I punti grandi rappresentano gli atomi/ioni del reticolo: oscillano intorno a posizioni fisse, senza migrare lungo il pezzo.
- I punti piccoli rappresentano gli elettroni mobili: moto irregolare in tutte le direzioni, senza una marcia collettiva dal caldo al freddo.
- Gli scambi con il reticolo modificano l’energia delle due componenti. I trasferimenti microscopici possono avvenire in entrambi i versi; in media l’energia passa dalla regione più calda a quella più fredda.
- Gli atomi freddi vibrano già: ricevere energia può aumentare mediamente l’ampiezza delle vibrazioni. Gli elettroni non li «mettono in moto» a partire dalla quiete.
- La velocità dei puntini è una convenzione visuale: non va presentata come misura della velocità reale degli elettroni o del suo andamento con la temperatura. Una variazione di colore/indicatore energetico può rendere riconoscibile il trasporto senza questa falsa equivalenza.
- Nessun campo elettrico applicato e nessuna rappresentazione di una corrente elettrica ordinata.

## Modello energetico e condizioni da approvare

Preferibile un piccolo campione isolato dopo la preparazione iniziale: zona sinistra più calda e zona destra più fredda, senza sorgenti esterne mantenute accese. Scambi locali fra elettroni e reticolo e fra zone vicine, con energie sempre positive e bilancio conservato nel modello. Con il tempo la differenza si riduce verso l’equilibrio. L’oscillazione del reticolo deve dipendere dall’energia locale, non da una sequenza temporale decisa in anticipo.

Il modello di scambio è una rappresentazione didattica statistica. Non attribuire valori reali di conducibilità, tempi microscopici, masse o temperature ai parametri illustrativi. Non dichiarare che si stia risolvendo il modello elettronico reale del metallo. Eventuali evidenziazioni di uno scambio devono mostrare la diminuzione energetica del donatore e l’aumento del ricevente.

Comandi: Avvia/Pausa, Ricomincia; legenda per reticolo/elettroni. Rispetto del movimento ridotto, utilizzo da tastiera, rappresentazione statica iniziale chiara. Offline e composizione invariata su mobile. Nessun comando di scelta materiale o nuova comparazione metallo/isolante introdotti automaticamente.

## Verifiche necessarie prima dell’integrazione

Controllare bilancio, assenza di energie negative, riduzione statistica della differenza fra le due regioni e assenza di un moto collettivo artificiale degli elettroni; ampiezza non nulla anche nel lato freddo. Provare pausa, riavvio, movimento ridotto, tastiera e resa mobile/desktop. Separare il motore del modello dall’aspetto del tema v7. Test appropriati alla nuova dinamica, senza dichiarare già verificate prestazioni o risultati.

## Stima preliminare per questa sola interazione

**30–55 minuti di lavoro**, impegno di calcolo previsto basso per il lettore e basso–medio durante lo sviluppo.

- Modello e scambi energetici: 7–12 minuti.
- Adattamento del reticolo e controlli: 12–20 minuti.
- Verifica scientifica/numerica e browser: 8–15 minuti.
- Salvataggio e registro: 3–8 minuti.

Stima non garantita: dipende dalla leggibilità del moto e dall’esito dei controlli energetici. Non comprende l’impaginazione completa dei due capitoli né l’attesa dell’utente. Per contenere il lavoro, riusare il reticolo e mantenere pochi elettroni e i soli controlli essenziali, senza confronti tra materiali o grafici aggiuntivi.

## Passo successivo

Presentare il modello e ottenere il via esplicito prima della programmazione, secondo B2 del master. Dopo la prova separata aggiornare la bozza con la descrizione effettivamente implementata e sottoporla al workflow del capitolo prima degli HTML finali. Main e pubblicazione invariati.
