# Quiz di Termologia — campione per la revisione

Versione v1 — 24 ottobre 2026. **Proposto, in attesa di revisione e approvazione del docente.**

Categoria unica: `termologia`. Destinatari di progetto: biennio degli istituti tecnici, 14–16 anni. Strumento consentito: calcolatrice di base. Nessun prerequisito disciplinare esterno ai capitoli consultati; si usano le operazioni e le conversioni di base previste dal master.

Si applicano MASTER_PROMPT.md v69.15 (D2.2), il prompt di generazione v1.4.0 e le specifiche quiz v2.3.0. Questo è il campione iniziale della fase 1: non sostituisce il target di 300 domande approvate per Termologia. Il file [campione.json](campione.json) contiene soltanto gli otto campi previsti dal validatore, in un oggetto `questions`; non è caricato nell’archivio pubblico `quiz/domande.json`.

## Distribuzione e avanzamento

| Livello | Conoscenza | Ragionamento | Calcolo | Proposte | Approvate |
|---|---:|---:|---:|---:|---:|
| Facile | 1 | 1 | 1 | 3 | 0 |
| Medio | 1 | 1 | 1 | 3 | 0 |
| Difficile | 1 | 1 | 1 | 3 | 0 |
| Totale | 3 | 3 | 3 | 9 | 0 |

La distribuzione del campione è intenzionalmente di 3 domande per tipo e 3 per livello. Per i lotti successivi il riferimento resta 30 conoscenza, 40 ragionamento e 30 calcolo per livello, adattabile ai contenuti. Il campione potrà concorrere al totale solo dopo l’approvazione, mantenendo gli ID senza duplicazioni.

I tempi sotto indicati comprendono lettura, soluzione e scelta: sono stime prudenti, non misure osservate. Difficoltà e tempi richiedono calibrazione con gli studenti; nessuna domanda è presentata come già approvata o sperimentata.

## Schede di revisione

### termo-001 — Facile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 35 secondi.

**Competenza e argomenti:** Distinguere sistema chiuso e sistema isolato.

**Riferimenti consultati:** [La termodinamica e i sistemi termodinamici](../../../termodinamica_sistemi_it.html). § 2 e § 5.

**Conoscenze richieste:** Classificazione dei sistemi in base agli scambi di materia ed energia.

**Informazioni fornite:** Nessuna proprietà particolare di materiali o dispositivi.

Quale descrizione identifica un sistema termodinamico chiuso?

- **A.** Può scambiare materia, ma non energia, con l’ambiente.
- **B.** Può scambiare energia, ma non materia, con l’ambiente.
- **C.** Non può scambiare né materia né energia con l’ambiente.
- **D.** Può scambiare sia materia sia energia con l’ambiente.

**Risposta corretta: B.** Un sistema chiuso conserva la materia entro il confine, ma può scambiare energia. L’assenza di entrambi gli scambi identifica invece un sistema isolato.

**Distrattori:** A inverte i due scambi; C confonde chiuso e isolato; D descrive un sistema aperto.

**Motivo del livello:** Richiede di riconoscere una definizione fondamentale.

### termo-002 — Facile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 50 secondi.

**Competenza e argomenti:** Applicare il modello microscopico di un gas a un’espansione.

**Riferimenti consultati:** [Stati della materia](../../../stati_della_materia.html). § 3.

**Conoscenze richieste:** Un gas occupa lo spazio disponibile; comprimibilità e distanza fra particelle.

**Informazioni fornite:** Due camere rigide, una inizialmente vuota; assenza di perdite e temperatura mantenuta costante.

Due camere rigide sono collegate da una valvola: una contiene un gas, l’altra è vuota. Si apre la valvola senza perdite e mantenendo costante la temperatura. Dopo che il gas si è distribuito, che cosa è cambiato?

- **A.** Le particelle sono diventate più grandi e occupano entrambe le camere.
- **B.** Sono comparse nuove particelle che riempiono la seconda camera.
- **C.** Le particelle sono rimaste nella prima camera, alla stessa distanza media.
- **D.** Le stesse particelle occupano entrambe le camere, con distanza media maggiore.

**Risposta corretta: D.** Il gas si distribuisce nel volume disponibile. Il numero di particelle resta uguale, ma il volume occupato aumenta: cresce la loro distanza media, non la loro dimensione.

**Distrattori:** A attribuisce l’espansione alla dimensione delle particelle; B confonde aumento di volume e aumento di materia; C assegna al gas un volume proprio.

**Motivo del livello:** Basta una conseguenza diretta del modello delle particelle.

**Trasferimento al contesto:** La valvola rende disponibile uno spazio prima inaccessibile: occorre prevedere una distribuzione, anziché descrivere la compressione nella siringa del capitolo.

### termo-003 — Facile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 55 secondi.

**Competenza e argomenti:** Calcolare il calore assorbito senza cambiamenti di stato.

**Riferimenti consultati:** [Energia interna, calore e calore specifico](../../../energia_interna_calore_specifico_it.html). § 5.

**Conoscenze richieste:** Q = m · c · ΔT; una differenza di 10 °C equivale a 10 K.

**Informazioni fornite:** Massa, calore specifico costante e aumento di temperatura; nessun cambiamento di stato.

Un blocco di massa 0,50 kg ha calore specifico costante c = 400 J/(kg · K). Assorbe calore e la sua temperatura aumenta di 10 K, senza cambiamenti di stato. Quanto calore assorbe?

- **A.** 2000 J
- **B.** 200 J
- **C.** 20 000 J
- **D.** 4000 J

**Risposta corretta: A.** Q = m · c · ΔT = 0,50 · 400 · 10 J = 2000 J, cioè 2,0 kJ.

**Distrattori:** B omette il fattore ΔT; C sposta di una posizione la virgola nel prodotto; D omette la massa.

**Motivo del livello:** Si applica direttamente una relazione con unità coerenti.

### termo-004 — Media, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 55 secondi.

**Competenza e argomenti:** Distinguere evaporazione ed ebollizione per sede e condizioni.

**Riferimenti consultati:** [Passaggi di stato](../../../passaggi_di_stato.html). § 2 e nota sulla pressione.

**Conoscenze richieste:** Evaporazione superficiale; bolle di vapore nell’ebollizione; dipendenza della temperatura di ebollizione dalla pressione.

**Informazioni fornite:** Nessun dato esterno.

Quale confronto tra evaporazione ed ebollizione è corretto?

- **A.** L’evaporazione forma bolle anche all’interno; l’ebollizione avviene alla superficie anche sotto la temperatura di ebollizione.
- **B.** L’evaporazione e l’ebollizione avvengono entrambe a qualsiasi temperatura, indipendentemente dalla pressione esterna.
- **C.** L’evaporazione avviene alla superficie anche sotto la temperatura di ebollizione; l’ebollizione forma bolle anche all’interno.
- **D.** L’evaporazione avviene solo alla temperatura di ebollizione; l’ebollizione avviene alla superficie senza formare bolle interne.

**Risposta corretta: C.** L’evaporazione può avvenire dalla superficie anche sotto la temperatura di ebollizione. Nell’ebollizione si formano bolle di vapore anche all’interno; la temperatura a cui avviene dipende dalla pressione.

**Distrattori:** A scambia i due fenomeni; B elimina le condizioni di ebollizione e il ruolo della pressione; D attribuisce a ciascuno proprietà dell’altro.

**Motivo del livello:** Occorre distinguere due trasformazioni verso lo stesso stato evitando di attribuire a entrambe le condizioni dell’ebollizione.

### termo-005 — Media, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 65 secondi.

**Competenza e argomenti:** Separare temperatura e rapidità dello scambio termico quando il verso del flusso si inverte.

**Riferimenti consultati:** [Temperatura ed equilibrio termico](../../../temperatura_equilibrio_termico_it.html); [Conduzione](../../../conduzione_it.html). Temperatura § 2; Conduzione § 2 e nota sul tatto.

**Conoscenze richieste:** Verso del calore; conducibilità e sensazione al tatto.

**Informazioni fornite:** Oggetti entrambi a 40 °C, pelle inizialmente a 32 °C; a parità di contatto il metallo trasferisce energia più rapidamente.

Un oggetto di metallo e uno di legno sono entrambi a 40 °C. La pelle è inizialmente a 32 °C. Nei primi istanti di contatto il metallo trasferisce energia alla pelle più rapidamente del legno. Quale previsione è corretta?

- **A.** Il metallo può sembrare più caldo, pur avendo la stessa temperatura del legno.
- **B.** Il metallo deve avere una temperatura maggiore, perché trasferisce energia più rapidamente.
- **C.** Il metallo può sembrare più freddo, perché un buon conduttore sottrae sempre energia alla pelle.
- **D.** I due oggetti devono dare la stessa sensazione, perché hanno la stessa temperatura.

**Risposta corretta: A.** Entrambi cedono energia alla pelle, inizialmente più fredda. Il trasferimento più rapido dal metallo può farlo sembrare più caldo: la sensazione non misura direttamente la temperatura.

**Distrattori:** B identifica rapidità e temperatura; C attribuisce al conduttore un verso fisso dello scambio; D ignora la dinamica del contatto.

**Motivo del livello:** Collega il verso del trasferimento alla diversa rapidità, invertendo la situazione degli oggetti più freddi della pelle.

**Trasferimento al contesto:** Si applica al contatto con superfici più calde della pelle il modello usato nel capitolo per spiegare anche il metallo apparentemente freddo.

### termo-006 — Media, calcolo

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 75 secondi.

**Competenza e argomenti:** Calcolare una variazione di lunghezza e convertirla in millimetri.

**Riferimenti consultati:** [La dilatazione termica](../../../dilatazione_termica_it.html). § 1, legge lineare e nota di validità.

**Conoscenze richieste:** ΔL = α · L₀ · ΔT; differenza di temperatura; conversione da metri a millimetri.

**Informazioni fornite:** Lunghezza iniziale, temperature, coefficiente costante e dilatazione libera.

Una barra lunga 2,0 m a 20 °C viene portata a 70 °C ed è libera di dilatarsi. Assumi α = 0,000012 K⁻¹ costante. Di quanto aumenta la lunghezza?

- **A.** 0,12 mm
- **B.** 1,2 mm
- **C.** 12 mm
- **D.** 120 mm

**Risposta corretta: B.** ΔT = 70 °C − 20 °C = 50 K. ΔL = 0,000012 · 2,0 · 50 m = 0,0012 m = 1,2 mm.

**Distrattori:** A, C e D rappresentano errori di un fattore 10 o 100 nella conversione o nella posizione della virgola.

**Motivo del livello:** Richiede di ricavare ΔT e convertire il risultato, oltre ad applicare la legge.

### termo-007 — Difficile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 80 secondi.

**Competenza e argomenti:** Riconoscere condizioni e temperature pertinenti alla legge di Fourier della parete.

**Riferimenti consultati:** [Conduzione](../../../conduzione_it.html). § 4, legge di Fourier e nota sul modello.

**Conoscenze richieste:** Legge di Fourier; regime stazionario; distinzione tra temperature delle facce e dell’aria.

**Informazioni fornite:** Parete piana omogenea, conducibilità costante e trasferimento perpendicolare alle facce.

Per una parete piana omogenea, con conducibilità costante e trasferimento perpendicolare alle facce, quale scelta permette di applicare il modello di Fourier con profilo lineare della temperatura nello spessore?

- **A.** Assumere regime stazionario e assenza di sorgenti interne; usare sempre le temperature dell’aria ai due lati.
- **B.** Trascurare le sorgenti interne; usare le temperature delle facce anche mentre la parete accumula energia.
- **C.** Assumere regime stazionario; usare le temperature delle facce anche con produzione di energia dentro la parete.
- **D.** Assumere regime stazionario e assenza di sorgenti interne; usare le temperature delle due facce.

**Risposta corretta: D.** Il modello lineare richiede regime stazionario e assenza di sorgenti interne, oltre alle condizioni già date. ΔT riguarda le due facce della parete: gli scambi fra aria e superfici possono rendere diverse le temperature dell’aria.

**Distrattori:** A sostituisce le temperature delle facce con quelle dell’aria; B ammette accumulo durante il transitorio; C elimina l’ipotesi di assenza di sorgenti interne.

**Motivo del livello:** La risposta richiede il controllo congiunto delle condizioni del modello e del significato di ΔT, anziché il solo ricordo della formula.

### termo-008 — Difficile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 90 secondi.

**Competenza e argomenti:** Individuare vie di scambio residue e conseguenze di una modifica selettiva.

**Riferimenti consultati:** [Conduzione](../../../conduzione_it.html); [Convezione](../../../convezione_it.html); [Irraggiamento](../../../irraggiamento_it.html). Conduzione § 1 e § 3; Convezione § 1; Irraggiamento § 4 e § 5.3.

**Conoscenze richieste:** Conduzione nei solidi; convezione come trasporto di materia; scambio radiativo e bassa emissività.

**Informazioni fornite:** Sensore più caldo della custodia, intercapedine vuota, supporti invariati; rivestimento con bassa emissività infrarossa e confronto alle stesse temperature.

Un sensore caldo è sospeso con supporti solidi dentro una custodia più fredda. Nell’intercapedine c’è il vuoto. Si rivestono soltanto le superfici affacciate con uno strato a bassa emissività infrarossa, lasciando invariati i supporti. Confrontando le due configurazioni alle stesse temperature, che cosa ci si aspetta?

- **A.** La conduzione nei supporti diminuisce; lo scambio radiativo resta uguale; la convezione è assente.
- **B.** La convezione nell’intercapedine diminuisce; lo scambio radiativo e la conduzione nei supporti restano uguali.
- **C.** Lo scambio radiativo diminuisce; la conduzione nei supporti resta uguale; la convezione è assente.
- **D.** Lo scambio radiativo si annulla; la conduzione nei supporti diminuisce; la convezione resta presente.

**Risposta corretta: C.** La bassa emissività riduce lo scambio radiativo fra le superfici. Nel vuoto non c’è fluido che trasporti energia per convezione. I supporti solidi restano una via di conduzione: il loro contributo non cambia nel confronto alle stesse temperature.

**Distrattori:** A assegna alla finitura superficiale un effetto sui supporti; B introduce convezione nel vuoto; D confonde riduzione e annullamento e attribuisce effetti ai percorsi invariati.

**Motivo del livello:** Coordina tre meccanismi e distingue l’effetto sullo scambio radiativo da ciò che resta invariato nei supporti.

**Trasferimento al contesto:** Occorre valutare una modifica limitata a un solo percorso di scambio e riconoscere il ponte termico residuo nei supporti, senza concludere che il vuoto isoli da tutto.

### termo-009 — Difficile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 115 secondi.

**Competenza e argomenti:** Verificare la fusione completa prima di calcolare la temperatura di equilibrio.

**Riferimenti consultati:** [Il bilancio termico](../../../bilancio_termico_it.html); [Passaggi di stato](../../../passaggi_di_stato.html); [Energia interna, calore e calore specifico](../../../energia_interna_calore_specifico_it.html). Bilancio § 2 e § 3; Passaggi § 4; Energia § 5.

**Conoscenze richieste:** Conservazione dell’energia; Q = m · L; Q = m · c · ΔT; massa totale dopo la fusione.

**Informazioni fornite:** Masse e temperature iniziali, acqua pura a pressione atmosferica, c e L; scambi esterni e contributo del recipiente trascurabili.

In un recipiente si mescolano 0,20 kg d’acqua a 60 °C e 0,10 kg di ghiaccio a 0 °C. Trascurando recipiente e scambi con l’ambiente, quale temperatura di equilibrio si raggiunge? Considera acqua pura a pressione atmosferica, c = 4200 J/(kg · K) costante e calore latente di fusione L = 334 kJ/kg.

- **A.** Circa 13,5 °C
- **B.** Circa 20,2 °C
- **C.** Circa 40 °C
- **D.** 0 °C

**Risposta corretta: A.** Raffreddandosi fino a 0 °C, l’acqua può cedere 0,20 · 4200 · 60 J = 50,4 kJ. Per fondere il ghiaccio servono 0,10 · 334 kJ = 33,4 kJ: fonde tutto. Restano 17,0 kJ per riscaldare 0,30 kg d’acqua. Ogni kelvin richiede 0,30 · 4200 J = 1260 J: l’aumento è circa 13,5 K e T finale è circa 13,5 °C.

**Distrattori:** B riscalda con l’energia residua soltanto gli 0,20 kg iniziali; C ignora il calore latente e fa la media pesata; D assume che la presenza iniziale di ghiaccio imponga sempre 0 °C.

**Motivo del livello:** Richiede di scegliere la sequenza fisica: confrontare l’energia disponibile con quella di fusione, poi riscaldare tutta l’acqua con l’energia residua.

## Base documentale

Sono stati letti i dieci capitoli pubblicati della categoria, elencati sotto. Non sono stati utilizzati capitoli esclusi dal manifest né bozze come sostituti dei sorgenti pubblicati. Le fonti si riferiscono al commit [ef29a4f](https://github.com/rickymusu-bit/fisica/commit/ef29a4fe630287c59d707abacd082e2fc0617691); i percorsi in tabella identificano le fonti della revisione, senza diventare chiavi dell’archivio.

| Capitolo | Sorgente verificato |
|---|---|
| La termodinamica e i sistemi termodinamici | [termodinamica_sistemi_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/termodinamica_sistemi_it.html) |
| Temperatura ed equilibrio termico | [temperatura_equilibrio_termico_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/temperatura_equilibrio_termico_it.html) |
| Energia interna, calore e calore specifico | [energia_interna_calore_specifico_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/energia_interna_calore_specifico_it.html) |
| Il bilancio termico | [bilancio_termico_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/bilancio_termico_it.html) |
| La dilatazione termica | [dilatazione_termica_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/dilatazione_termica_it.html) |
| Stati della materia | [stati_della_materia.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/stati_della_materia.html) |
| Passaggi di stato | [passaggi_di_stato.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/passaggi_di_stato.html) |
| Conduzione | [conduzione_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/conduzione_it.html) |
| Convezione | [convezione_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/convezione_it.html) |
| Irraggiamento | [irraggiamento_it.html](https://github.com/rickymusu-bit/fisica/blob/ef29a4fe630287c59d707abacd082e2fc0617691/irraggiamento_it.html) |

## Verifiche e decisione richiesta

Controllo scientifico svolto su tutte le domande: soluzione, unicità della risposta nelle condizioni date, plausibilità dei distrattori, prerequisiti, unità e arrotondamenti. Non sono emerse domande duplicate. Nel quesito termo-009 il valore di c è fornito e arrotondato a 4200 J/(kg · K); non si richiede di ricordare il valore tabulato nel capitolo.

Controlli tecnici superati: validatore corrente dell’archivio, tre quesiti per livello e uno per combinazione tipo/livello, quattro opzioni distinte per quesito, ID univoci, categoria registrata, collegamenti locali e ricalcolo dei tre quesiti numerici. Superati anche i cinque test esistenti di `scripts/test_quiz.py` e `git diff --check`. Non è stata eseguita la build del sito: sono cambiati soltanto materiali di lavorazione, senza modificare l’interfaccia o l’archivio pubblico.

Il docente deve rivedere formulazioni, distrattori, difficoltà e plausibilità dei tempi, in particolare i quesiti difficili. La richiesta di approvazione prima dei lotti deriva dalla sezione 10, fase 2, di [PROMPT_GENERAZIONE_DOMANDE.md](../../../quiz/PROMPT_GENERAZIONE_DOMANDE.md): «Il docente valuta correttezza, chiarezza, distrattori, livello e plausibilità dei due minuti per i propri studenti» e «conserva il campione approvato». L’approvazione didattica del campione non autorizza automaticamente altri lotti, merge o pubblicazione.

