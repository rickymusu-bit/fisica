# Stato — Il piano cartesiano e i grafici

## Riferimenti e autorizzazioni

Progettazione v1 — 24 ottobre 2026, Europe/Rome. Master consultato: v69.15; istruzioni AGENTS.md, piano dell'area, STILE_DISPENSE.md v7, esempio_irraggiamento.md e docs/visual-guidelines.md. Checklist: A1–A5 (narrazione, formule, monograficità, domande), B1.1–B2 (visuali prima della bozza e approvazioni), B4–B6 (riuso e continuità), C1–C4 (immagini, grafici, accessibilità), D1–D2.1 (verifiche e salvataggio). Applicare economia informativa a testo, figure e didascalie.

Richiesta effettiva: «Iniziamo a creare i capitoli 8 e 9 del piano di lavorazione sull'introduzione alla fisica». Autorizzato l'avvio della progettazione. Le nuove scelte visuali, la bozza completa, la realizzazione HTML e la pubblicazione non sono ancora approvate. Tema comune Stringhe già approvato, da riutilizzare nella successiva fase HTML senza una nuova scelta.

Fonte verificata: grafici_piano_cartesiano_it.html, versione interna v8, blob 9befd930b57d847869b7cc6e9f131e01050223f3. Consultato anche lo stato storico lavorazione/grafici_piano_cartesiano/stato.md. Il manifest corrente esclude il sorgente unificato: consultato, non modificato né riammesso. Il piano iniziale conserva passaggi storici: il manifest corrente include già i capitoli 1–7. Nessun intervento a main, manifest, catalogo o sito pubblico.

Ramo dedicato derivato da main: lavorazione/introduzione-capitoli-8-9. File di stato e proposta salvati; nessuna bozza integrale o HTML realizzati. Revisione preliminare svolta sul testo, sui grafici SVG e sul codice delle interazioni; non si dichiarano prove nel browser o verifiche delle licenze non eseguite.

## Argomento e confini

Capitolo 8 di Introduzione alla fisica e alla misura. Sorgente: sezione «Due grandezze, una coppia di coordinate» e interazione «Trascina P». Titolo futuro proposto: piano_cartesiano_grafici_it.html.

Percorso proposto: una coppia di dati diventa un punto; assi, origine e ordine (x; y); ascissa e ordinata; valori negativi e quadranti; grandezze e unità sugli assi; scelta e lettura delle scale; passaggio tabella–grafico e lettura di un andamento. Distinguere la lettura delle coordinate dalla ricerca della legge che lega le grandezze. Nessuna pendenza, intercetta o classificazione di proporzionalità: capitoli 9–11.

Domanda iniziale proposta: come possiamo rappresentare due informazioni riferite alla stessa osservazione e leggere dal grafico come cambia una grandezza?

## Visuali proposte, da concordare

- C8-COP: fotografia reale di un grafico su carta millimetrata, copertina senza zoom e senza riutilizzo nel corpo. File da scegliere e fornire dall'utente. Il vecchio grafico del petrolio è disponibile, ma non viene scelto automaticamente: densità, lingua, fonte dei dati e diritti devono essere verificati prima di un riuso; la lunga spiegazione sui dollari del 2022 introduce un prerequisito economico non necessario.
- C8-INT: riutilizzare il piano cartesiano già presente, con punto P trascinabile, proiezioni tratteggiate, coordinate aggiornate e riconoscimento del quadrante o dell'asse. Il codice corrente limita x e y a [−5; 5] e arrotonda ai decimi; mouse/tocco e frecce da tastiera già previsti. Mostrare una sola lettura delle coordinate, evitando duplicazioni di etichette. È un'interazione matematica, senza modello dinamico o misure sperimentali.
- C8-TAB/GRA: tabella breve e corrispondenti punti nello stesso piano; possibile riuso delle coppie dei quaderni (0;0), (1;2), (2;4), (3;6), (4;8), senza introdurre la legge. Ogni coppia deve essere riconoscibile. L'esempio dei quaderni, se mantenuto nel racconto, richiede l'immagine della situazione concordata per il capitolo 9, oltre al grafico.
- C8-SCA: confronto statico dello stesso insieme di dati con due scale verticali uniformi differenti, per mostrare che la lettura dipende dalle tacche e che l'inclinazione apparente non è una variazione dei dati. Evitare assi troncati in questa prima introduzione. Nuovo confronto proposto, non ancora realizzato.

Il materiale copertina e lo schema della situazione sono da scegliere; non sono state cercate o generate immagini nuove. Le figure conserveranno la composizione su smartphone. Assi, unità, scale e descrizioni accessibili restano; omettere didascalie che ripetono assi o istruzioni già espliciti.

## Domande e continuità

Conservare il quesito originale 2 (spostare P nei quadranti e su un asse). Il quesito originale 1 riguarda il petrolio: se quel grafico viene mantenuto, conservarlo; se viene sostituito, conservarne la funzione di lettura di assi/dati adattandolo alla nuova immagine e registrando la sostituzione nella bozza. Il quesito originale 3 appartiene al capitolo 9; 4–5 al capitolo 10; 6–7 al capitolo 11. Non duplicare né perdere i quesiti nella suddivisione. In bozza definire le ulteriori domande su coordinate invertite, scale e lettura di una tabella, senza soluzioni automatiche.

## Fattibilità e prossima operazione

Riuso tecnico leggero, senza librerie o servizi esterni. Prima del riuso verificare isolamento degli identificativi, inizializzazione della lettura, estremi, passaggio sugli assi, tocco e tastiera, fallback e contrasto. Stima preliminare per adattamento e prove della sola interazione: 20–40 minuti, carico basso; non è un tempo misurato. Alternativa più semplice: piano statico con punti già assegnati, meno esplorazione autonoma; non preferita perché l'interazione esiste.

Fase corrente: proposta di contenuti e visuali. Prossimo passaggio: concordare riuso, confronto delle scale e immagini; poi scrivere bozza.md completa con segnaposto. Dopo approvazione della bozza, comunicare stima totale ripartita e raccogliere il via alla realizzazione secondo B1.1. Nessun HTML prima di quel passaggio.
