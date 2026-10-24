# Verifica dell’archivio di Termologia

25 ottobre 2026 (Europe/Rome). Archivio candidato completo, senza pubblicazione.

## Esito

Sono presenti 300 quesiti: 100 per livello. Ogni livello comprende 30 conoscenza, 40 ragionamento e 30 calcolo. I 39 record già approvati restano identici ai file del campione e del primo lotto; i 261 nuovi record sono proposte per la revisione del docente.

Controlli superati con `python3 lavorazione/quiz/termologia/verifica_archivio.py`:

- Validatore corrente del repository su tutte le 300 domande; soli sette campi previsti, categoria `termologia`, ID continui e univoci, quattro opzioni distinte, indice corretto e testi completi.
- Conteggi totali e per livello; nei nuovi quesiti, 26 conoscenza, 35 ragionamento e 26 calcolo per livello, che completano il totale 30/40/30 considerando i 13 già approvati per livello.
- Conservazione integrale dei 39 record approvati, compreso l’ordine delle opzioni.
- Distribuzione delle risposte: 75 per ciascuna posizione, con ordine variato e senza ciclo fisso. Il sito potrà mescolare ulteriormente le opzioni.
- Nove lotti di revisione da 29 quesiti, senza ripetizioni di ID fra le schede; corrispondenza puntuale di testo, alternative, lettera corretta e spiegazione con il dataset.
- Collegamenti ai capitoli e tempi stimati entro 120 secondi; metadati separati dal dataset di importazione.
- Ricalcolo dei 78 nuovi quesiti quantitativi: espressione aritmetica, risultato atteso e numero effettivamente presentato nell’opzione corretta, considerando gli arrotondamenti. Le espressioni sono valutate consentendo soltanto numeri e operazioni aritmetiche.
- Nessun testo duplicato, anche dopo la sostituzione dei numeri con un segnaposto. Questo controllo rileva alcune varianti numeriche, ma non dimostra da solo varietà semantica.
- Archivio pubblico `quiz/domande.json` ancora assente: il sito resta invariato.

Superati anche i cinque test esistenti di `scripts/test_quiz.py` e `git diff --cached --check`.

## Revisione dei contenuti e delle sovrapposizioni

Le domande sono state risolte durante la stesura e controllate per ipotesi, unità, segni e risposta unica. Il confronto testuale fra quesiti è stato usato per individuare casi da esaminare, senza trasformare una soglia di somiglianza in un criterio automatico di qualità. Sono stati sostituiti alcuni quesiti troppo vicini fra loro: il secondo caso sul solido amorfo, un confronto termico che ripeteva la sola definizione di equilibrio, un’applicazione diretta di energia uguale potenza per tempo e un ritorno all’equilibrio radiativo troppo simile a un altro confronto di temperature. Al loro posto si richiedono identificazione da più osservazioni, ruolo della massa nel verso dello scambio, potenza per area e separazione fra temperatura finale e rapidità radiativa.

La ripresa di un principio è mantenuta quando cambia l’operazione fisica richiesta: per esempio ricavare la massa o il calore specifico da una misura, controllare una condizione del modello, distinguere uno stato intermedio o coordinare due contributi. Cristallino e policristallino richiedono distinzioni strutturali diverse; non sono trattati come duplicati solo perché le domande hanno parole simili. Il calcolo di una temperatura dopo fusione con Q assegnato è distinto dal ricavare prima Q da potenza e durata, o dal verificare che il calore disponibile in una miscela non fonda tutto il ghiaccio.

Nel quesito termo-300 il modello trascura conduzione e convezione alla pressione atmosferica: non impone il vuoto a ghiaccio in fusione. Nel modello del capillare sono dichiarati la dilatazione della capacità interna e l’approssimazione di sezione costante. Non vengono richieste proprietà di materiali non dichiarate, leggi dei gas non presenti nei capitoli o calcolo avanzato.

La notazione scientifica è usata anche nei distrattori quando sono presenti valori molto piccoli o molto grandi e non sono utili prefissi SI; i valori come kJ e MJ restano espressi con i prefissi quando risultano più leggibili.

## Limiti e fase successiva

I tempi di 40–110 secondi sono stime progettuali, non misure osservate. Il docente deve ancora rivedere i 261 nuovi quesiti, soprattutto la calibrazione dei livelli difficili e dei tempi per i propri studenti. I controlli automatici non provano correttezza didattica, chiarezza o fattibilità in due minuti.

Non sono state eseguite build o prove browser per questa consegna: cambiano soltanto materiali di lavorazione, non il motore o l’archivio caricato dal sito. L’integrazione nell’archivio pubblico, la verifica dell’estrazione e l’anteprima effettiva della pagina appartengono alla fase successiva, dopo la revisione didattica; merge e deployment restano vincolati all’approvazione dell’anteprima corrente.
