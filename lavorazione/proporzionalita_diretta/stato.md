# Stato — La proporzionalità diretta

## Riferimenti e autorizzazioni

Progettazione v1 — 24 ottobre 2026, Europe/Rome. Master consultato: v69.15; istruzioni AGENTS.md, piano dell'area, STILE_DISPENSE.md v7, esempio_irraggiamento.md e docs/visual-guidelines.md. Checklist: A1–A5 (narrazione, formule, monograficità, domande), B1.1–B2 (visuali prima della bozza e approvazioni), B4–B6 (riuso e continuità), C1–C4 (immagini, grafici, accessibilità), D1–D2.1 (verifiche e salvataggio). Applicare economia informativa a testo, figure e didascalie.

Richiesta effettiva: «Iniziamo a creare i capitoli 8 e 9 del piano di lavorazione sull'introduzione alla fisica». Autorizzato l'avvio della progettazione. Le nuove scelte visuali, la bozza completa, la realizzazione HTML e la pubblicazione non sono ancora approvate. Tema comune Stringhe già approvato, da riutilizzare nella successiva fase HTML senza una nuova scelta.

Fonte verificata: grafici_piano_cartesiano_it.html, versione interna v8, blob 9befd930b57d847869b7cc6e9f131e01050223f3. Consultato anche lo stato storico lavorazione/grafici_piano_cartesiano/stato.md. Il manifest corrente esclude il sorgente unificato: consultato, non modificato né riammesso. Il piano iniziale conserva passaggi storici: il manifest corrente include già i capitoli 1–7. Nessun intervento a main, manifest, catalogo o sito pubblico.

Ramo dedicato derivato da main: lavorazione/introduzione-capitoli-8-9. File di stato e proposta salvati; nessuna bozza integrale o HTML realizzati. Revisione preliminare svolta sul testo, sui grafici SVG e sul codice delle interazioni; non si dichiarano prove nel browser o verifiche delle licenze non eseguite.

## Argomento e confini

Capitolo 9 di Introduzione alla fisica e alla misura. Sorgente: sezione «Dalle proporzioni alla retta», tabella dei quaderni e grafico SVG chart-direct. Titolo futuro proposto: proporzionalita_diretta_it.html.

Domanda iniziale proposta: se raddoppiamo il numero di quaderni acquistati, raddoppia anche il prezzo? Situazione centrale: prezzo unitario fisso di 2 €/quaderno, senza quota fissa o sconti; dati costruiti dal modello, non misure.

Percorso: rapporto costante per x diverso da zero, costante di proporzionalità e sue unità, formule generali y = k·x e k = y/x (in HTML frazione orizzontale), previsioni raddoppiando/triplicando/dimezzando x nei limiti del dominio; tabella e grafico con origine; riconoscimento numerico della relazione. Spiegare k come prezzo unitario, non come semplice numero privo di unità. Il rapporto non è definito in x = 0, ma il modello assegna y = 0: precisazione breve nel punto necessario o in nota.

Lasciare al capitolo 10 il trattamento di intercetta, rette con quota fissa e calcolo della pendenza. Qui basta il collegamento intuitivo fra k e aumento di y per unità di x, senza una seconda trattazione. Inversa e quadratica restano al capitolo 11. Non presentare «entrambe crescono» come criterio sufficiente. Il modello generale ammette anche k negativo per grandezze con segno: non definire la proporzionalità esclusivamente come crescita, pur mantenendo il caso concreto positivo.

## Visuali proposte, da concordare

- C9-COP: foto reale di quaderni in cartoleria, per la copertina, senza zoom; file da scegliere e fornire dall'utente. Non riutilizzarla nello schema interno.
- C9-SIT: un'altra immagine di un quaderno, preferibilmente con sfondo trasparente o rimovibile, per lo schema essenziale dell'acquisto e del prezzo unitario 2 €/quaderno. Non disegnare un oggetto sostitutivo con sagome astratte. File da scegliere e fornire; nessuna ricerca o generazione effettuata.
- C9-TAB: riutilizzare tabella originale: numero di quaderni 0, 1, 2, 3, 4; prezzo 0, 2, 4, 6, 8 €. Aggiungere il rapporto solo se serve alla lettura, senza ripeterne i valori in più apparati.
- C9-GRA: riutilizzare grafico originale e comando «Mostra la retta». Punti e modello distinti, assi con grandezze/unità. Per l'acquisto i numeri di quaderni sono interi: la retta visualizza il modello matematico, non la possibilità di acquistare frazioni di quaderno. Conservare questa distinzione in una breve nota se la linea continua viene mostrata.
- Nessuna simulazione nuova o cursore di k proposto: il comando esistente basta al passaggio tabella–modello. Un confronto tra pendenze diverse sarà valutato nel capitolo 10.

Rimuovere dal materiale adattato separatori puntiformi usati fuori dalle moltiplicazioni e spiegazioni ripetute come «Punti = tabella; linea = regola» quando il contesto e il pulsante rendono già chiara la funzione. Le informazioni non ovvie su dati e dominio restano. Il paragrafo sulla linea interpolante nei dati sperimentali non è necessario nel modello esatto dei prezzi: non trasferirlo automaticamente nel capitolo 9, conservarlo nella fonte storica e valutarne la collocazione nei futuri contenuti sui grafici sperimentali.

## Domande e continuità

Conservare il quesito originale 3: ricavare il prezzo unitario dalla tabella e spiegare il passaggio per l'origine. Progettare nella bozza ulteriori domande su previsione di prezzi, unità di k e riconoscimento del rapporto costante, con pochi calcoli e senza soluzioni automatiche. Ripartizione completa dei sette quesiti originali documentata nello stato del capitolo 8.

## Fattibilità e prossima operazione

Interazione esistente binaria, costo sul dispositivo basso: nessuna integrazione temporale, libreria o dipendenza esterna. Verificare che il codice non dipenda dal piano trascinabile eliminato da questo capitolo: lo script unificato accede a plane/point e va separato. Conservare pulsante, stato aria-pressed e funzionamento da tastiera; prevedere una lettura statica utile senza JavaScript. Stima preliminare per isolamento e prove del solo grafico: 15–30 minuti, carico basso; non è un tempo misurato. Alternativa statica con punti e retta sempre visibili: minore lavoro tecnico, nessuna rivelazione progressiva; il riuso del comando resta preferibile.

Fase corrente: proposta di contenuti e visuali. Prossimo passaggio: concordare i materiali, poi scrivere bozza.md completa con segnaposto. Dopo approvazione della bozza, comunicare stima totale ripartita e raccogliere il via alla realizzazione secondo B1.1. Nessun HTML prima di quel passaggio.
