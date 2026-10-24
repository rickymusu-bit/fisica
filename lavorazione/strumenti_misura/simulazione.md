# SIM-06 — Bilancia con pesetti e proprietà regolabili
Versione v3 — 23 ottobre 2026. Implementata nell’HTML v1; immagini di bilancia e pesetti in attesa.

## Interfaccia richiesta
Bilancia al centro; vassoio di pesetti di masse differenti, identificati in grammi e aggiungibili/rimovibili singolarmente. Proposta di dotazione: 10 g, 20 g, 50 g, 100 g e 200 g, un esemplare per tipo. Somma delle masse realmente caricate sempre visibile per confrontarla con l'indicazione.
Interazione con clic/tocco e comandi da tastiera; trascinamento eventualmente aggiuntivo, mai obbligatorio. Nessun oggetto astratto disegnato al posto della bilancia o dei pesetti: usare immagini pertinenti fornite/scelte dall'utente, con diritti verificati. Le immagini di bilancia e pesetti sono una dipendenza aperta, non un motivo per cercarle o generarle autonomamente.

Sotto la bilancia: slider etichettati, valore e unità correnti, passo discreto dichiarato. Portata 200/500/1000 g, passo leggibile 1/20/50 g, prontezza 0,5/1/2 s simulati; sensibilità del sensore 1/2/5 mV/g. Controlli separati per spostamento dello zero e intensità dei disturbi. Inizialmente zero e disturbi assenti.
Definizione accanto allo slider: “Passo leggibile (risoluzione)”; eventuale uso scolastico di “sensibilità” per quel passo esplicitato, senza confonderlo con la sensibilità metrologica.

## Modello e attività
Massa totale come somma dei pesetti, confronto con la portata prima della lettura; fuori scala blocca Registra. Risposta temporale progressiva dichiarata didattica; registrazione distingue lettura anticipata e stabilizzata. Quantizzazione al passo selezionato dopo la risposta.
Sensibilità: segnale del sensore I = S · m, espresso in mV; conversione digitale coerente m = I/S. Aumentare S cambia il segnale per la stessa massa, non moltiplica la massa indicata. Pannello numerico del segnale, senza conoscenze di circuiti richieste. Offset e disturbo applicati in grammi equivalenti e convertiti coerentemente nel segnale.

Attività: aggiungere pesetti, prevedere la lettura, variare una proprietà e osservare; confrontare portata e carico, cambiamenti a gradini, attesa, segnale, dispersione e spostamento. Ogni modifica di configurazione apre una nuova serie per evitare confronti ambigui.
Comandi: aggiungi/rimuovi pesetto, svuota piatto, registra, azzera serie, ripristina. Tabella di letture con massa caricata, indicazione, configurazione e stato; nessun obbligo di grafico nel 6. Massimo 20 letture per serie.

## Fattibilità e verifica
Codice standard incorporato, offline, mobile e tastiera; nessuna libreria, rete o caricamento scientifico esterno. Rispetto del movimento ridotto e niente animazioni ornamentali. Tempo simulato distinto dalle prestazioni del dispositivo.
Verificare somme, rimozione singola, proprietà effettive degli slider, scala, unità, combinazioni fuori portata, risposta e reset. Modello semplice, dati sintetici, nessuna specifica commerciale implicita.
Carico di calcolo basso. Stima preliminare aggiornata per entrambe le simulazioni: 2–3 ore complessive (25–40 min modello, 35–55 min interfacce e pesetti, 25–35 min grafico/integrazione, 35–50 min verifiche e salvataggio), esclusa attesa delle immagini e delle revisioni. Stima da consolidare dopo l'approvazione delle bozze prima del via all'HTML.
La richiesta autorizza e definisce questa progettazione; dettagli numerici proposti, testo da revisionare, programmazione non avviata.

## Implementazione autorizzata

L’utente dà il via con «Ok vai». Modello e comandi realizzati nel codice condiviso del capitolo 6, incorporati nei due HTML. Grafico del 7 con panoramica e ingrandimento del tema comune. Immagini pertinenti di bilancia, pesetti e campioni in attesa: la simulazione usa per ora controlli testuali e non inventa gli oggetti. Specifiche di progetto sopra conservate; fase corrente e verifiche in stato.md.

### Passi di lettura scelti per l’attività

Nella realizzazione i passi sono 1, 20 e 50 g: con i pesetti tutti multipli di 10 g, i passi 1/5/10 g davano la stessa indicazione in assenza di disturbi. I nuovi passi rendono osservabile la quantizzazione senza richiedere altri pesetti o immagini. Esempio di controllo: carico 10 g, lettura 20 g al passo 20 g oppure 0 g al passo 50 g. Nel 7 il passo resta 1 g.

## Immagini generate e display attivo

Bilancia digitale e pesetto generati su richiesta dell’utente; originali nella lavorazione del capitolo 6 e relative schede di provenienza. Varianti dei pesetti riutilizzano l’originale con dimensioni proporzionate alla radice cubica della massa; etichette HTML separate. Display numerico nella finestra della bilancia e carichi visualizzati sul piatto. Il campione B è privo di etichetta di massa. Immagini incorporate una sola volta tramite definizioni SVG condivise, con riferimenti interni per le istanze; nessuna dipendenza esterna.
