# Stato — Le relazioni tra grandezze

## Riferimenti e autorizzazioni

Progettazione v2 — 24 ottobre 2026, Europe/Rome. Master consultato: v69.15; istruzioni AGENTS.md, piano dell'area, STILE_DISPENSE.md v7, esempio_irraggiamento.md e docs/visual-guidelines.md. Checklist: A1–A5 (narrazione, formule, monograficità, domande), B1.1–B2 (visuali prima della bozza e approvazioni), B4–B6 (riuso e continuità), C1–C4 (immagini, grafici, accessibilità), D1–D2.1 (verifiche e salvataggio). Applicare economia informativa a testo, figure e didascalie.

Richiesta effettiva: «Iniziamo a creare i capitoli 8 e 9 del piano di lavorazione sull'introduzione alla fisica». Autorizzato l'avvio della progettazione. Le nuove scelte visuali, la bozza completa, la realizzazione HTML e la pubblicazione non sono ancora approvate. Tema comune Stringhe già approvato, da riutilizzare nella successiva fase HTML senza una nuova scelta.

Fonte verificata: grafici_piano_cartesiano_it.html, versione interna v8, blob 9befd930b57d847869b7cc6e9f131e01050223f3. Consultato anche lo stato storico lavorazione/grafici_piano_cartesiano/stato.md. Il manifest corrente esclude il sorgente unificato: consultato, non modificato né riammesso. Il piano iniziale conserva passaggi storici: il manifest corrente include già i capitoli 1–7. Nessun intervento a main, manifest, catalogo o sito pubblico.

Ramo dedicato derivato da main: lavorazione/introduzione-capitoli-8-9. File di stato e proposta salvati; nessuna bozza integrale o HTML realizzati. Revisione preliminare svolta sul testo, sui grafici SVG e sul codice delle interazioni; non si dichiarano prove nel browser o verifiche delle licenze non eseguite.

## Decisione corrente e confini — 24 ottobre 2026

Richiesta: «Allora, io farei il piano cartesiano in un capitolo e tutte le relazioni di proporzionalità in un altro». Approvato l'accorpamento: capitolo 8 sul piano cartesiano; capitolo 9 su tutte le relazioni previste dal piano. Il percorso complessivo comprende nove capitoli; non sono più previsti capitoli 10 e 11 separati.

Titolo proposto: «Le relazioni tra grandezze». Percorso futuro proposto: relazioni_grandezze_it.html. Questo file di stato conserva il percorso storico per mantenere continuità e collegamenti, ma riguarda ora l’intero capitolo 9.

Sorgente: sezioni «Dalle proporzioni alla retta», «Intercetta e pendenza: rette diverse», «Proporzionalità inversa» e «Relazione quadratica» di grafici_piano_cartesiano_it.html, con tabelle, grafici e quesiti 3–7. Il capitolo 8 fornisce i prerequisiti di lettura del piano e delle scale: non ripeterne la spiegazione.

## Percorso proposto

Domanda guida: quando cambia una grandezza, come possiamo prevedere il cambiamento dell’altra?

1. Proporzionalità diretta: y = k·x, rapporto costante per x diverso da zero, significato e unità di k, raddoppio e dimezzamento, retta passante per l’origine. Conservare l’esempio dei quaderni a prezzo unitario fisso.
2. Confronto con le altre rette: y = m·x + q, significato di pendenza e intercetta, quota fissa della consegna e retta decrescente. Per q diverso da zero la relazione è affine e non una proporzionalità diretta; una retta decrescente non è automaticamente una proporzionalità inversa. Il confronto serve a riconoscere i modelli, senza diventare un capitolo separato.
3. Proporzionalità inversa: y = k/x, prodotto x·y costante, esempio dei rettangoli di area 12 cm², raddoppio della base e dimezzamento dell’altezza, curva nel dominio positivo.
4. Proporzionalità quadratica: y = k·x², rapporto y/x² costante per x diverso da zero, lato e area del quadrato, raddoppio del lato e area quadrupla. Non chiamare proporzionalità quadratica una generica funzione di secondo grado con altri termini.
5. Domande finali su riconoscimento delle relazioni da dati, formule e grafici, senza riepiloghi ripetitivi o soluzioni automatiche.

Le divisioni saranno frazioni orizzontali nell’HTML. Definire grandezze, unità, domini e costanti nel punto necessario; non ripetere a ogni grafico avvertenze già chiare. Il caso concreto positivo non deve diventare una definizione generale che escluda k negativo nella proporzionalità diretta.

## Visuali proposte e materiali aperti

Riutilizzare tabelle e grafici del sorgente: quaderni, confronto delle tre rette, rettangoli ad area costante e area del quadrato. Conservare i comandi esistenti «Mostra la retta» / «Mostra la curva» se concordati; nessuna nuova simulazione programmata. Assi con grandezze e unità coerenti con ciascun contesto; non fondere in uno stesso grafico dati con unità diverse.

Copertina: da scegliere per il capitolo unificato; la precedente proposta dei quaderni non è più una scelta corrente automatica. Non riutilizzarla nel corpo. Per gli esempi concreti servono gli schemi delle situazioni: immagine del quaderno e del servizio di consegna da concordare e fornire; rettangoli e quadrati sono oggetti geometrici rappresentabili direttamente in SVG. Non cercare o generare nuove immagini senza richiesta. Niente didascalie che ripetano assi, regole o comandi.

I quesiti originali 3–7 sono assegnati tutti a questo capitolo; 1–2 al capitolo 8. Preservare contenuto e funzione dei quesiti nella bozza. Il paragrafo storico sulla linea interpolante nei dati misurati non va trasferito automaticamente al modello esatto dei prezzi.

## Fattibilità, fase e prossimo passaggio

I grafici e i comandi esistono: riuso leggero, senza servizi esterni o nuove librerie. Separare lo script dei grafici dal codice del punto P, che appartiene al capitolo 8, ed evitare accessi a elementi assenti. Verificare comandi, tastiera, aria-pressed, fallback statico, scale, domini e resa mobile nei due temi. Non sono ancora state svolte prove nel browser sul capitolo unificato.

La precedente stima di 15–30 minuti riguardava soltanto il grafico della diretta e non copre l’intero capitolo unificato. Dopo l’approvazione della bozza occorre una nuova stima complessiva ripartita per materiali, HTML, interazioni, verifiche e salvataggio.

Fase corrente: struttura accorpata definita dall’utente; visuali da concordare. Prossima operazione: definire i materiali e poi preparare bozza.md completa con segnaposto. Nessuna realizzazione HTML, modifica di main o pubblicazione autorizzata.
