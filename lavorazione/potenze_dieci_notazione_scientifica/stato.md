# Stato — Le potenze di dieci e la notazione scientifica

Ultimo aggiornamento: 23 ottobre 2026 (Europe/Rome).
Fase: progettazione dei contenuti e proposta visuali pronta per la scelta dell’utente.
Ramo dedicato da main: `lavorazione/potenze-dieci-notazione-scientifica`.
Piano di riferimento: [capitolo 3 del percorso](../introduzione_fisica_misura/piano.md).
Area tematica: **Introduzione alla fisica e alla misura**.

## Incarico e approvazioni effettive

Richiesta corrente: «Lavora sul capitolo 3 del piano di lavorazione sul mio repo di fisica lavorazione/introduzione_fisica_misura/piano.md».
Argomento e posizione sono già definiti nel piano dei dodici capitoli. Il tema Stringhe comune è già approvato; non occorre sceglierlo nuovamente.
La richiesta avvia il lavoro editoriale. Non risultano approvate per questo capitolo le visuali definitive, la bozza, la realizzazione HTML o la pubblicazione. Le autorizzazioni dei primi due capitoli non si estendono al terzo.

## Identità del sorgente e confini

Sorgente verificato: [sistema_internazionale_notazione_it.html](../../sistema_internazionale_notazione_it.html), versione interna v11, blob `ede0bed4b28522b2431e4201b39e8f9f10593f88`.
Lo stato storico riporta anche versioni precedenti: per questa progettazione fa fede il file corrente verificato.
La sezione `#scale`, «Dal molto grande al molto piccolo», contiene il materiale del nuovo capitolo. Il sorgente storico resta invariato ed escluso dalla pubblicazione.

Corrispondenza dei contenuti:
- «Che cosa significa misurare», grandezze di base e unità derivate: capitolo 2, già pubblicato; richiamo solo se necessario.
- `#scale`: capitolo 3. Conservare il confronto fra scale, le potenze positive, nulle e negative, il prodotto di potenze e la distinzione fra scritture esponenziale, scientifica e ingegneristica.
- Prefissi e scala dei multipli/sottomultipli: capitolo 4; evitare di anticiparne la tabella.
- Cifre significative, arrotondamenti ed esempio della base rettangolare: capitolo 5.

Progressione proposta: confronto fra dimensioni molto diverse → significato di 10ⁿ → esponente zero e negativo → scritture equivalenti e normalizzazione → confronto fra numeri e semplici operazioni sulle potenze → breve distinzione dalla notazione ingegneristica, senza sviluppare i prefissi.
Chiarire che un esponente negativo indica un fattore positivo minore di uno: non rende negativo il numero. La forma scientifica di un numero non nullo è a · 10ⁿ, con 1 ≤ |a| < 10 e n intero.
Non identificare automaticamente l’esponente della forma scientifica con l’ordine di grandezza: dichiarare e usare coerentemente il criterio di stima adottato. Confrontare inizialmente fattori e scale usando i valori espliciti.
Nessuna applicazione separata, esercizio svolto aggiuntivo o simulazione prevista in questa fase.

## Domanda iniziale proposta

Il diametro della Terra e quello di un atomo richiedono numeri molto diversi: come scriverli e confrontarli senza perdersi tra gli zeri?
L’apertura riprende il confronto già presente nel sorgente. La foto astronomica introduce la scala maggiore; la dimensione atomica sarà presentata come dato del modello, senza attribuirla a una fotografia priva di scala.

## Proposta visuali da concordare

| ID | Materiale e posizione | Funzione e trattamento proposto | Stato |
| --- | --- | --- | --- |
| COP-01 | Foto della Terra oltre l’orizzonte lunare già incorporata in `#scale`, sotto il titolo | Riutilizzarla come copertina, senza ripeterla nel corpo. Verificare la provenienza dell’esatto file e la licenza prima dell’integrazione. | Riuso proposto; diritti non ancora verificati. |
| TAB-01 | Tabelle originali delle lunghezze e delle masse, presso il confronto fra scale | Conservare dati pertinenti e due tabelle distinte; verificare fonti e significato delle stime prima della bozza. Per le masse proporre kg, esplicitando la conversione dai g originali, senza cambiare i valori fisici. | Riuso e conversione proposti. |
| TAB-02 | Tabella numerica delle potenze, presso la spiegazione degli esponenti | Affiancare 1000, 100, 10, 1, 0,1, 0,01, 0,001 alle rispettive potenze da 10³ a 10⁻³; rendere leggibile il passaggio per fattori dieci e l’esponente zero. Solo numeri e relazioni matematiche, nessuna immagine di oggetti da generare. | Nuova tabella proposta, non realizzata. |
| TAB-03 | Confronto fra notazioni già presente in `#scale`, dopo la normalizzazione | Conservare 0,000047 m, 470 · 10⁻⁷ m, 4,7 · 10⁻⁵ m e 47 · 10⁻⁶ m. Rimandare l’equivalenza in µm al capitolo 4; spiegare che la forma ingegneristica usa esponenti multipli di tre. | Riuso con adattamento proposto. |
| VID-01 | [Powers of Ten](https://www.youtube.com/watch?v=0fKBhvDjuy0), vicino al confronto fra scale | Conservare il collegamento esatto e la miniatura esistente, previa verifica dei diritti; apertura su YouTube, nessun lettore incorporato. Osservare il fattore dieci fra inquadrature successive. | Video originale pertinente; riuso proposto. |
| IMG-01 | Micrografie A/B già incorporate, presso la discussione delle piccole dimensioni | Conservarne la funzione: senza scala non si ricava una dimensione dall’immagine. Soggetto e licenza non sono documentati nel sorgente: non inventarli né presentare le immagini come fotografie di atomi. | Materiale originale da verificare; non sostituito. |
| VID-02 | [A Boy and His Atom](https://www.youtube.com/watch?v=oSCX78-8-q0), presso la scala microscopica | Conservare il link originale e l’esatta descrizione: molecole di monossido di carbonio spostate con un microscopio a effetto tunnel. Valutare nella bozza la brevità del raccordo per evitare una digressione. | Riuso proposto; miniatura e diritti da verificare. |

La proposta privilegia i materiali già presenti e non richiede nuove fotografie. Se un originale non è riutilizzabile per provenienza o leggibilità, presentare il problema e chiedere una scelta specifica; non cercare o generare sostituti autonomamente. Le tabelle devono conservare disposizione e relazioni sui diversi dispositivi.

## Domande originali e ripartizione

Il sorgente contiene tredici quesiti. Quesiti 1–3 al capitolo 2; quesiti 4 e 7 al capitolo 3; quesito 6 al capitolo 4; quesiti 8–13 al capitolo 5.
Il quesito 5 attraversa i confini: la conversione di 0,000047 m in forma scientifica e ingegneristica compete al capitolo 3; la scelta del prefisso compete al capitolo 4. Separare le due richieste mantenendo questa provenienza, senza duplicare l’intero quesito.

Per il capitolo 3 conservare quindi:
- confronto fra diametro terrestre e atomico, precisando il significato degli ordini di grandezza;
- riscrittura di 0,000047 m nelle due notazioni;
- lettura critica delle micrografie prive di scala.

Nella bozza completare una breve serie mista di domande, con vero/falso motivati sugli esponenti negativi, riconoscimento di una forma scientifica normalizzata e confronto fra valori espressi nella stessa unità. Numero e formulazione definitivi da fissare nella bozza, senza soluzioni.

## Regole e controlli pertinenti

Letti MASTER_PROMPT.md v69.6, AGENTS.md, riferimenti/STILE_DISPENSE.md v6, riferimenti/esempio_irraggiamento.md v2 e docs/visual-guidelines.md v1.0.0.
Checklist: A1–A5 (monograficità, narrazione, formule e quesiti); A6 (tema autonomo comune, da leggere prima dell’impaginazione); B1.1–B2 (visuali concordate, bozza e via prima dell’HTML); B4–B6 (riuso e stato); C1–C4 (provenienza, scelta, tabelle e didascalie); C5 per i video; D1–D2.1 (verifica e salvataggio sul ramo).

Controlli preliminari svolti: identità/versione del sorgente, sezione di provenienza, tredici quesiti e confini dei capitoli; manifest v11 con sorgente unificato escluso; assenza di uno stato corrente a questo percorso.
I crediti incorporati nel sorgente segnalano risorse senza attribuzione individuale: il loro riuso storico non certifica una licenza. Nessuna nuova associazione nel registro crediti in questa fase.
Non sono stati eseguiti controlli browser, build o credits.py: le modifiche riguardano soltanto la progettazione Markdown.

## Prossimo passaggio

Presentare la proposta all’utente e raccogliere la scelta delle visuali. Poi verificare i dati delle tabelle e i materiali scelti, scrivere la bozza completa soltanto in `bozza.md` sullo stesso ramo, con segnaposto identificabili, e sottoporla all’approvazione. Dopo l’approvazione del testo, fornire la stima ripartita e attendere il via alla realizzazione HTML secondo B1.1.
Nessun HTML, ricerca o generazione di immagini, modifica al catalogo, merge o deployment è autorizzato da questa fase.
