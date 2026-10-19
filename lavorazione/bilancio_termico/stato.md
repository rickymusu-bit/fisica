# Stato — Il bilancio termico

Versione v2 · 19 ottobre 2026, ore 21:27 (Europe/Rome).

## Identità, ambito e fase

Articolo 4 del [percorso introduttivo di termodinamica](../percorso_termodinamica.md) v5: energia ceduta e assorbita, convenzione dei segni, temperatura finale di equilibrio ed eventuale contributo del recipiente, inizialmente senza cambiamenti di stato. Esclusi calore latente, dilatazione e sviluppo dei meccanismi di trasmissione.

Richiesta effettiva: «Sul mio GitHub repo di fisica, facciamo l'articolo pianificato numero 4». Autorizza l'avvio del capitolo; non documenta approvazione di un testo, immagini, HTML o pubblicazione.

Ramo dedicato `termodinamica/bilancio-termico`, derivato da main. Alla verifica iniziale mancava `lavorazione/bilancio_termico/stato.md` e non risultavano rami con “bilancio”. Piano corrente: capitolo ancora non redatto. Nessun sorgente esistente sostituito.

Fase corrente: proposta di domanda iniziale e visuali salvata in [visuali.md](visuali.md), da concordare prima della bozza.

## Riferimenti e checklist

Letti integralmente MASTER_PROMPT.md v61 in blocchi, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, piano v5 e pubblicazione.json v7. Consultati stato dell'articolo 3 e sue visuali v13 per confini e possibile riuso.

- Italiano, stile discorsivo; unico fenomeno guida, formule spiegate e interpretate, T e ΔT per temperatura.
- Bilancio per un sistema isolato nel modello calorimetrico senza lavoro rilevante: somma dei calori con segno nulla; equivalenza dei moduli ceduto/assorbito.
- Temperatura finale pesata dalle capacità termiche; media aritmetica soltanto per capacità uguali. Nessuna deduzione dei tempi di equilibrio dal solo bilancio.
- A1–A5: notazione scientifica nei calcoli, frazioni orizzontali, condizioni utili nelle note, domande finali senza soluzioni.
- B1.1/C2: concordare visuali prima della bozza, senza cercare o generare immagini autonomamente. Nessuna nuova immagine cercata, scelta o elaborata.
- Bozza completa soltanto nel file `bozza.md` del ramo, dopo le scelte preliminari. Approvazione del testo, stima ripartita e via esplicito prima dell'HTML.
- Tema autonomo v8 già approvato: leggerlo prima dell'impaginazione; nessuna variante, visuali con stessa composizione sui dispositivi, note collassabili e logo canonico.
- Crediti nel registro unico e snapshot offline nella futura fase HTML; nessun credito o fonte nel testo didattico.
- Nessuna modifica a main, home, manifest, pubblicazione, capitoli precedenti o sorgenti esclusi. Il vecchio `bilancio_conservazione_rendimento_it.html` riguarda un'altra lavorazione sospesa e non viene riattivato.

## Proposta e scelte ancora aperte

Scelta esplicita dell’utente: «preferirei parlare di mischiare il caffè con il latte» approssimando i calori specifici a quello dell’acqua. Fenomeno e approssimazione approvati; nessuna approvazione attribuita a specifiche immagini, testo completo o HTML. Apertura adattata proposta: «Quanto si raffredda il caffè quando aggiungiamo il latte?». Il calore specifico comune si semplifica e T_eq è la media delle temperature iniziali pesata dalle masse. La media aritmetica vale per masse uguali; non sostituire automaticamente le masse con i volumi. Precisazione sull’approssimazione in nota, senza sviluppi sulla composizione delle bevande.

Due fotografie distinte: COP-01 latte versato nel caffè e FIG-01 caffè, latte e tazza, distinta dalla copertina. Grafico GRA-01 dei calori in funzione della temperatura finale ipotizzata, opzionale, con dati di modello dichiarati e senza falsa cronologia sperimentale. Breve contributo del recipiente proposto nel medesimo fenomeno.

Le risorse dell'articolo 3 non rappresentano il mescolamento; non riusate come sostituti. Nessun video o simulazione proposti, nessun esercizio svolto o applicazione autonoma aggiunti. Nessuna programmazione o stima di simulazione necessaria.

## Completato e prossimo passo

Identificati numero, titolo, confini e stato del piano. Salvate proposta e lavorazione sul ramo dedicato tramite il connettore GitHub: il clone locale non è riuscito per indisponibilità del proxy, senza modificare la destinazione ufficiale. Non dichiarare eseguita una build o una verifica browser: non esiste ancora un nuovo HTML.

Prossimo passo: ricevere le fotografie o i collegamenti per caffè e latte; concordare grafico e breve contributo della tazza. Conservare il fenomeno e l’approssimazione già scelti senza richiederne nuovamente conferma. Poi preparare la bozza completa nel repository con segnaposto e formulazione delle domande finali. HTML finale previsto, dopo il workflow di approvazione: `bilancio_termico_it.html`.
