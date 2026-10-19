# Proposta — Energia interna, calore e calore specifico

Versione v1 · 19 ottobre 2026 (Europe/Rome).

Articolo 3 del [percorso approvato](../percorso_termodinamica.md). Progettazione iniziale da concordare: non è ancora la bozza completa del testo né il via alla realizzazione HTML.

## Domanda e percorso proposti

**Perché la stessa quantità di energia può scaldare poco una pentola piena d’acqua e molto una quasi vuota?**

Aprire con due quantità diverse d’acqua alla stessa temperatura iniziale, riscaldate ricevendo la stessa energia. La fotografia illustra la situazione; parità di energia e temperatura sono condizioni dell’esperimento mentale, non misure ricavate dall’immagine.

Dall’osservazione passare al modello microscopico: le particelle hanno energia associata al moto e alle interazioni reciproche. L’energia interna U è l’energia microscopica complessiva del sistema; non coincide con l’energia del suo moto d’insieme o della sua posizione rispetto al terreno. La temperatura caratterizza lo stato termico, non misura l’energia interna totale. La connessione con il moto delle particelle va spiegata senza presentare ogni sostanza come un gas ideale.

Definire poi il calore Q come energia trasferita per differenza di temperatura: un corpo possiede energia interna, non una scorta di calore. Collegare al primo articolo ricordando brevemente che anche il lavoro può cambiare l’energia interna, senza introdurre un nuovo sviluppo sul primo principio.

La domanda quantitativa porta a capacità termica C e calore specifico c, distinguendo proprietà dell’intero corpo e proprietà del materiale. Presentare e interpretare Q = C · ΔT, C = m · c e Q = m · c · ΔT; definire ΔT = T_f − T_i e chiarire proporzionalità a massa, calore specifico e variazione di temperatura. Espressioni con divisione rese come frazioni orizzontali nella futura bozza/HTML. Usare T maiuscola e unità J/K e J/(kg · K); differenze Celsius e kelvin hanno lo stesso valore numerico. Una breve nota delimita l’uso della relazione all’intervallo considerato senza cambiamento di stato e con c approssimativamente costante.

Non anticipare la temperatura finale di una miscela, il contributo del recipiente o il bilancio tra corpi: appartengono all’articolo 4. Non sviluppare calore latente, dilatazione o meccanismi di trasmissione. Nessuna sezione autonoma di applicazioni, nessun esercizio svolto, video o simulazione proposti.

## Visuali da concordare

| ID | Che cosa mostrare | Funzione e collocazione | Stato |
| --- | --- | --- | --- |
| COP-01 | Una fotografia di acqua riscaldata in una pentola, senza necessità di mostrare ebollizione. | Copertina: presentare il fenomeno quotidiano. Non ripetere questa fotografia nel testo. | Nuova immagine da fornire/scegliere. |
| FIG-01 | Due recipienti dello stesso tipo con quantità d’acqua chiaramente diverse; preferibilmente un’unica foto con entrambi. | Apertura: distinguere massa d’acqua, temperatura iniziale ed energia ricevuta. Conservare il contesto fotografico; nessun valore dedotto dalla foto. | Nuova immagine da fornire/scegliere, distinta dalla copertina. |
| FIG-02 | Un’illustrazione microscopica già esistente che renda riconoscibili moto e interazioni delle particelle, preferibilmente con confronto fra due temperature dello stesso materiale. | Dopo l’apertura: collegare osservazione e modello; chiarire che il modello non è una fotografia delle particelle. Non rappresentare calore come sostanza contenuta nel corpo. | Immagine da fornire/scegliere. Non ricostruirla o animarla automaticamente. |
| GRA-01 | Grafico di T in funzione del calore assorbito Q per due masse dello stesso materiale, con stessa T iniziale; la massa doppia ha aumento di temperatura dimezzato a parità di Q. | Accanto alla lettura di Q = m · c · ΔT. Dati dichiarati come previsioni del modello, non misure sperimentali. | Proposta di grafico originale da concordare, non ancora realizzato. |
| TAB-01 | Piccola tabella di calore specifico di acqua liquida, alluminio e rame, con valori approssimati e temperatura di riferimento documentati nella bozza. | Chiarire che masse uguali di materiali diversi richiedono energie diverse per lo stesso ΔT. | Proposta di tabella da concordare. Dati e fonte da verificare prima della stesura. |

Se l’immagine microscopica scelta contiene solo moto e non interazioni, la didascalia ne espliciterà la portata e il testo introdurrà separatamente l’energia delle interazioni. Non usare una figura limitata al gas come descrizione indistinta dei solidi e dei liquidi.

Per FIG-01, didascalia proposta: «Le quantità d’acqua sono diverse. Partendo dalla stessa temperatura, la stessa energia ricevuta produce un aumento di temperatura maggiore nella quantità minore.» Le condizioni restano un confronto ipotetico, non la descrizione di un esperimento documentato nella foto.

## Materiali già presenti e riuso

Esaminati i registri delle visuali degli articoli 1 e 2. Il caffè dell’articolo 1 è già scelto dall’utente e conservato in [../termodinamica_sistemi/risorse/caffe.jpg](../termodinamica_sistemi/risorse/caffe.jpg): può sostenere un richiamo al trasferimento di energia, ma non mostra il confronto fra masse e non sostituisce FIG-01. Non occorre riproporne l’approvazione se viene riutilizzato coerentemente.

La bevanda con ghiaccio dell’articolo 2 introdurrebbe un cambiamento di stato, fuori dal confronto quantitativo qui proposto: non viene scelta per illustrare Q = m · c · ΔT. Non sono state cercate, scaricate, generate o alterate nuove immagini. Nessun nuovo credito inventato: il registro unico verrà aggiornato nella fase HTML dopo la scelta dei materiali.

## Domande finali previste

Proposta di otto domande, da formulare integralmente nella bozza dopo la scelta delle visuali: distinguere calore ed energia interna; confrontare quantità diverse dello stesso materiale alla stessa temperatura; motivare un vero/falso sul calore “contenuto”; prevedere l’effetto del raddoppio della massa; distinguere C da c; leggere le due curve del grafico; confrontare materiali della tabella; interpretare il segno di ΔT e di Q per un corpo che si raffredda. Nessuna soluzione o prova con punteggi.

## Decisioni necessarie e seguito

Concordare il percorso e le cinque funzioni visuali; l’utente fornisce i tre file o collegamenti delle immagini COP-01, FIG-01 e FIG-02. Eventuali idee diverse possono sostituire queste proposte prima della stesura. Se non trova un’immagine, concordare una ricerca specifica secondo C2 del master; non avviarla autonomamente.

Dopo l’accordo sulle visuali: scrivere la bozza completa in `bozza.md`, con segnaposto, formule spiegate e otto domande formulate, quindi presentarla per approvazione. Dopo l’approvazione del testo: comunicare la stima totale ripartita e raccogliere il via esplicito all’HTML. Tema comune v8 già approvato, da leggere e riusare esattamente prima dell’impaginazione. Nessuna scelta del tema da riaprire.
