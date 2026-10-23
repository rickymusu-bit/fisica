# Gli strumenti di misura

[EDITORIALE — Bozza v3, 23 ottobre 2026. Testo da approvare; visuali concordate con «Ok». I segnaposto descrivono i materiali da integrare dopo l'approvazione del testo. Area: Introduzione alla fisica e alla misura.]

[COP-06 — Fotografia scelta dall'utente: Ytterbium Lattice Double Clock with Photons at NIST.jpg. Intera, senza ritagli o zoom, non ripetuta nel corpo.]

*L'apparato di un doppio orologio atomico all'itterbio: anche la misura del tempo richiede uno strumento fisico e il controllo delle sue prestazioni.*

## Una lancetta o un display?

Appoggiamo un oggetto su una bilancia. Su un modello si muove una lancetta, su un altro compare un numero: il secondo sembra dirci subito tutto, fino all'ultima cifra. Ma avere più cifre basta per ottenere una misura migliore? Per rispondere dobbiamo capire come si legge lo strumento e che cosa può distinguere.

Nella bilancia **analogica**, il valore si ricava dalla posizione della lancetta su una scala graduata. Il movimento rende immediato seguire un aumento o una diminuzione; quando la lancetta cade fra due tacche, però, la lettura richiede una stima. Nella bilancia **digitale**, l'indicazione è un numero: leggerlo e trascriverlo è più comodo, ma l'ultima cifra può oscillare se il piatto vibra o il carico non è stabile. Entrambe trasformano un effetto fisico in un'indicazione che possiamo leggere.

[FIG-06-1a — Foto originale della bilancia analogica. Conservare intera; la foto della bilancia digitale accompagna TAB-06 più avanti.]

*La lancetta indica il valore sulla scala. Il quadrante riporta una portata di 5 kg e un passo indicato di 20 g.[^1]*

Per leggere una lancetta bisogna anche scegliere il punto di osservazione. Se indice e scala sono su piani diversi, guardare di lato cambia il loro allineamento apparente: è il **parallasse**. La lancetta non si è mossa, ma sembra corrispondere a un'altra tacca. Portare l'occhio davanti all'indice evita questo spostamento apparente. Se guardiamo sempre dallo stesso lato, anche lo spostamento tende a ripetersi nello stesso modo: è in questo senso sistematico.

[FIG-06-2 — Disegno originale del parallasse, senza ridisegno o modifica delle etichette.]

*La vista frontale permette di allineare correttamente indice e scala; le viste oblique suggeriscono letture diverse.*

## Quanto può misurare, e quanto rapidamente?

Prima della lettura viene una scelta: lo strumento è adatto alla grandezza che ci aspettiamo? La **portata** è il limite superiore dell'intervallo previsto per la misura. Una scala da 0 a 15 V non è adatta a una tensione attesa di 40 V: il valore sarebbe fuori scala. Occorre scegliere uno strumento o una portata compatibile con la tensione attesa, rispettando le indicazioni d'uso.

[FIG-06-3 — Foto originale del voltmetro con scala 0–15 V.]

*La scala arriva a 15 V. Eventuali selettori e specifiche determinano come va interpretata sullo strumento completo.*

Una portata molto grande non risolve ogni problema. Se l'intervallo rappresentato sulla stessa scala aumenta senza aumentare le suddivisioni, ogni divisione corrisponde a una variazione maggiore della grandezza. Per seguire variazioni piccole serve quindi controllare anche la finezza della lettura.

Un'altra caratteristica riguarda il tempo. Un termometro può mostrare i decimi di grado e impiegare comunque diversi istanti prima che l'indicazione si stabilizzi dopo il contatto con ciò che misura. La **prontezza** descrive quanto rapidamente lo strumento risponde a un cambiamento della grandezza. Leggere in fretta un display non significa che il sensore abbia già risposto.

[FIG-06-4 — Foto originale del termometro digitale; conservare il display originale.]

*Il sensore deve rispondere al cambiamento di temperatura. Il tempo necessario non si ricava dal numero di cifre del display.*

## Distinguere una variazione

Il cronometro della foto mostra i centesimi di secondo: l'ultima posizione visualizzata corrisponde a 0,01 s. Questo passo ci dice come cambia il numero sul display. La **risoluzione** è la più piccola variazione della grandezza misurata che produce un cambiamento distinguibile nell'indicazione; un display molto dettagliato, se instabile, può non consentire di distinguere variazioni altrettanto piccole.

[FIG-06-5 — Foto originale del cronometro, senza modificare le cifre mostrate.]

*Il display riporta i centesimi di secondo. Avviare e fermare il cronometro a mano introduce anche il contributo dell'operatore.*

La **sensibilità** risponde a una domanda diversa: quanto cambia l'indicazione quando cambia la grandezza misurata? Per descriverla confrontiamo le due variazioni:

\[
S=\frac{\Delta I}{\Delta x}
\]

Qui \(I\) è l'indicazione dello strumento e \(x\) la grandezza misurata; il simbolo \(\Delta\) indica una variazione. La sensibilità \(S\) esprime quindi la variazione dell'indicazione per ogni unità di variazione della grandezza. Le sue unità dipendono da ciò che confrontiamo.

In un termometro a colonna, per esempio, possiamo confrontare l'allungamento della colonna con la variazione di temperatura. A parità di aumento di temperatura, una colonna che si allunga di 2 mm per ogni grado Celsius risponde con uno spostamento doppio rispetto a una che si allunga di 1 mm. È più sensibile, ma per sapere quale piccola variazione riusciamo a leggere dobbiamo considerare anche scala e leggibilità. La sensibilità non coincide dunque con la risoluzione.[^1]

[PROSPETTO collegato a FIG-06-4 — Confronto concettuale del sorgente: termometro a colonna A, 2 mm per 1 °C; B, 1 mm per 1 °C. Dati illustrativi, non specifiche del termometro digitale fotografato. Nessuna nuova immagine di dispositivo; i valori affiancati esplicitano il confronto senza un esercizio separato.]

## Letture vicine, ma vicine a che cosa?

Torniamo alla bilancia digitale. Supponiamo di controllarla con un oggetto al quale un riferimento attendibile attribuisce una massa di 100 g. La tabella riporta tre possibili serie di letture: sono dati inventati per confrontare due proprietà, non risultati di un esperimento eseguito.

[FIG-06-1b — Foto originale della bilancia digitale accanto a TAB-06; nessun valore nuovo sovrapposto al display. La foto identifica lo strumento del confronto.]

[TAB-06 — Prospetto concordato. Condizione comune: stessa massa di riferimento, 100 g; tre letture per serie.]

| Serie | Prima lettura | Seconda lettura | Terza lettura |
| --- | --- | --- | --- |
| A | 100 g | 100 g | 100 g |
| B | 102 g | 102 g | 102 g |
| C | 98 g | 100 g | 102 g |

*Le serie A e B hanno letture raccolte; la serie B è spostata di 2 g rispetto al riferimento di 100 g. La serie C mostra una maggiore dispersione.*

La **precisione** riguarda la vicinanza fra letture ripetute nelle stesse condizioni. Le serie A e B sono entrambe molto raccolte alla risoluzione riportata. La serie C è meno precisa: le sue letture sono più disperse. La precisione, da sola, non ci dice però se lo strumento restituisce valori vicini al riferimento.

L'**accuratezza** riguarda proprio questa vicinanza. Le letture della serie B sono tutte maggiori del riferimento: uno spostamento di 2 g su 100 g corrisponde a un cinquantesimo della massa di riferimento. Ripetere la stessa lettura non basta a renderla accurata. Anche una serie dispersa come C può avere un valore centrale vicino al riferimento, senza diventare per questo precisa.

Portata adatta, risposta sufficientemente rapida e lettura fine ci aiutano quindi a misurare. Per valutare il risultato dobbiamo anche controllare la procedura e confrontare lo strumento con riferimenti attendibili. L'ultima cifra del display è solo una parte di questa informazione.

## Cambiare una proprietà alla volta

La bilancia virtuale permette di scegliere una massa campione nota e confrontare ciò che indica lo strumento con ciò che ci aspettiamo. Prima di cambiare una regolazione, prova a prevedere l'effetto: un passo più grande renderà più fine la lettura? Uno strumento più lento avrà già raggiunto l'indicazione finale quando registri il numero?

[SIM-06 — Bilancia virtuale con portata, risoluzione, prontezza e sensibilità regolabili; controlli separati per zero spostato e disturbi casuali. Massa campione nota, lettura e tabella. Pannello del segnale del sensore per la sensibilità: aumentando S aumenta il segnale per la stessa massa, non la massa stessa. Specifica in simulazione.md; nessun codice ancora realizzato.]

Modifica una sola proprietà, registra una lettura e confrontala con la precedente. Quando cambia la configurazione, inizia una nuova serie: mescolare misure ottenute con impostazioni diverse nasconderebbe proprio l'effetto che vuoi osservare. I valori sono simulati; la fotografia identifica lo strumento, senza documentare una prova reale.

## Domande di verifica

1. Quale vantaggio offre una lancetta quando una grandezza cambia? Quale vantaggio offre una lettura digitale? Indica un limite di ciascuna.
2. Osserva il disegno del parallasse: come devi posizionare l'occhio e perché una lettura sempre obliqua può produrre uno spostamento sistematico?
3. Il voltmetro della foto ha una scala da 0 a 15 V. Perché non sceglieresti quella scala per una tensione attesa di 40 V?
4. Un termometro indica i decimi di grado ma impiega tempo a stabilizzarsi. Quale caratteristica riguarda i decimi e quale riguarda il tempo di risposta?
5. Vero o falso? «Un display con più cifre garantisce sempre una misura più accurata». Motiva usando almeno due caratteristiche dello strumento.
6. Due termometri a colonna rispondono allo stesso aumento di temperatura con allungamenti diversi. Quale è più sensibile? Quale altra informazione ti serve per confrontarne la risoluzione?
7. Nella tabella, confronta le serie B e C: quale è più precisa? Perché questo confronto non basta a scegliere la serie più accurata?
8. Nella simulazione registra una lettura prima e una dopo la stabilizzazione. Quale proprietà spiega la differenza? Poi modifica soltanto la risoluzione: che cosa cambia e che cosa resta uguale?

## Note

[^1]: Nel linguaggio scolastico e su alcuni strumenti, “sensibilità” indica il più piccolo passo leggibile. Qui usiamo il significato metrologico di rapporto fra variazione dell'indicazione e variazione della grandezza. Sul quadrante della bilancia fotografata, “sensitivity” indica invece un passo di 20 g.

---

## Servizio editoriale — provenienza e verifiche

Questa sezione non appartiene al contenuto didattico visibile dell'HTML.
Fonte del testo e dei materiali: `strumenti_errori_incertezza_it.html` v7, blob `1d65637b40f2af68e1e1ff55c7d1710259b6087b`, sezioni #strumenti e #caratteristiche.
Quesiti originali 1–4 conservati integralmente; aggiunti 5–8. Il termine “sistematico” del quesito originale 2 indica qui uno spostamento che si ripete nello stesso modo; la classificazione degli errori resta al capitolo 7.
Aggiunti formula esplicita della sensibilità e prospetto illustrativo delle masse; confronto 2 mm / 1 mm già presente nel sorgente. Le foto non documentano i nuovi dati assegnati. Nessun calcolo della media o dell'incertezza.
Sorgente terminologico da associare ai crediti nell'HTML: JCGM 200:2012, International Vocabulary of Metrology, voci 2.13, 2.15, 4.1, 4.12, 4.14; https://www.bipm.org/en/committees/jc/jcgm/publications . Riferimento bibliografico indicato, non nuova verifica web delle licenze.
Licenze delle immagini storiche ancora da verificare sul registro e sulle fonti. Nessuna immagine cercata, generata o modificata. Il prospetto della sensibilità è testuale e non rappresenta nuovi dispositivi.
Visuali concordate con «Ok» dopo la proposta della PR #72; testo v1 da approvare. HTML, elaborazione delle visuali e pubblicazione non avviati.

### Copertina scelta dall'utente — bozza v2

COP-06: [Ytterbium Lattice Double Clock with Photons at NIST.jpg](https://commons.wikimedia.org/wiki/File:Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg); autore N. Phillips/NIST. Stato dei diritti verificato nella pagina Commons: Pubblico dominio: opera del governo federale statunitense, indicata PD-USGov su Commons. [URL esatto fornito](https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7c/Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg/1920px-Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail). Nessuna modifica richiesta: usare l'immagine intera, senza zoom; acquisizione e incorporamento del file nella fase HTML autorizzata. La copertina sostituisce la proposta del calibro, che resta nel sorgente storico. Testo didattico invariato salvo la didascalia. La fotografia è descritta dalla scheda originale, senza dedurre prestazioni quantitative o cause fisiche non documentate.

### Due simulazioni richieste — bozza v3

L'utente richiede una versione per le proprietà nel capitolo 6 e una a proprietà fisse per errore e incertezza nel 7. Inseriti attività narrativa, segnaposto e quesito finale coerente; i quesiti originali pertinenti restano integralmente conservati. Progettazione in [simulazione.md](simulazione.md). Nessun codice, nuovo HTML o elaborazione delle immagini. La richiesta definisce la distinzione fra le due versioni; i dettagli proposti e il testo aggiornato sono da revisionare prima della stima consolidata e del via alla realizzazione.
