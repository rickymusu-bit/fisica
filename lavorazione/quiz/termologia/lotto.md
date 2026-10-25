# Quiz di Termologia — primo lotto

Versione v1 — 25 ottobre 2026 (Europe/Rome). **30 quesiti approvati dall’utente con «sta bene, crea tutte quelle rimanenti».**

Campione di riferimento: [campione approvato](bozza.md), commit `db41942ebd320a5284baa8cbf0973f7e065513d9`, con conferma dell’utente «PROCEDI» e integrazione sulla notazione dei numeri molto grandi. Si applicano il master v69.15 e il prompt v1.4.1. Fonti: i dieci capitoli pubblicati consultati e fissati nel [campione](bozza.md#base-documentale), commit `ef29a4fe630287c59d707abacd082e2fc0617691`; nessuna variazione di main rilevata all’avvio.

Categoria unica `termologia`. Destinatari: biennio, 14–16 anni. Calcolatrice di base consentita. Prerequisiti esterni: soltanto operazioni, proporzioni e conversioni di base. [lotto.json](lotto.json) usa lo schema corrente con i soli sette campi dei quesiti; i metadati didattici restano in questo documento.

| Livello | Conoscenza | Ragionamento | Calcolo | Totale |
|---|---:|---:|---:|---:|
| Facile | 3 | 4 | 3 | 10 |
| Medio | 3 | 4 | 3 | 10 |
| Difficile | 3 | 4 | 3 | 10 |
| Totale | 9 | 12 | 9 | 30 |

I tempi comprendono lettura, ragionamento, calcoli e scelta e sono stime orientative, non misure osservate. Il lotto mantiene 120 secondi come limite per ogni quesito. Per numeri molto piccoli o molto grandi si usa a · 10ⁿ quando i prefissi SI non rendono la scrittura più leggibile; per esempio α = 1,2 · 10⁻⁵ K⁻¹, mentre un’energia di 144 kJ resta espressa con il prefisso.

## Schede di revisione

### termo-010 — Facile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 35 secondi.

**Riferimenti:** [energia_interna_calore_specifico_it.html](../../../energia_interna_calore_specifico_it.html).

**Conoscenze richieste e argomenti:** Capacità termica e unità J/K.

**Informazioni fornite:** Nessun dato esterno.

La capacità termica di un corpo esprime l’energia da trasferire come calore per aumentare di un kelvin la temperatura. Qual è la sua unità?

- **A.** W/K
- **B.** J/kg
- **C.** J/(kg · K)
- **D.** J/K

**Risposta corretta: D.** La capacità termica C riguarda il corpo intero e si misura in J/K. J/(kg · K) è invece l’unità del calore specifico.

**Distrattori:** B confonde capacità termica e calore latente specifico; C sceglie il calore specifico; A confonde energia e potenza.

**Motivo del livello:** Riconosce il significato di una grandezza fondamentale.

### termo-011 — Facile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 35 secondi.

**Riferimenti:** [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Nomi e versi dei passaggi di stato.

**Informazioni fornite:** Si tratta di un passaggio diretto.

Come si chiama il passaggio diretto da gas a solido?

- **A.** Brinamento
- **B.** Sublimazione
- **C.** Condensazione
- **D.** Solidificazione

**Risposta corretta: A.** Il brinamento porta direttamente dal gas al solido. La sublimazione è il passaggio inverso; condensazione e solidificazione coinvolgono lo stato liquido.

**Distrattori:** C introduce un liquido come stato finale; D parte dal liquido; B inverte il verso.

**Motivo del livello:** Richiama una trasformazione fondamentale.

### termo-012 — Facile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 35 secondi.

**Riferimenti:** [convezione_it.html](../../../convezione_it.html).

**Conoscenze richieste e argomenti:** Origine del movimento nella convezione forzata.

**Informazioni fornite:** Una pompa mette in moto il liquido.

Una pompa fa circolare un liquido che trasporta energia fra due zone. Come si classifica questo trasporto?

- **A.** Convezione forzata, perché il moto è prodotto dalla pompa.
- **B.** Conduzione, perché si muove un liquido.
- **C.** Convezione naturale, perché il liquido trasporta energia.
- **D.** Irraggiamento, perché l’energia cambia zona.

**Risposta corretta: A.** La materia in movimento trasporta energia: è convezione. Poiché il movimento è imposto da una pompa, si parla di convezione forzata.

**Distrattori:** B confonde trasporto di materia e conduzione; C ignora la causa del moto; D confonde lo spostamento dell’energia con radiazione.

**Motivo del livello:** Identifica il meccanismo che produce il movimento.

### termo-013 — Facile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 45 secondi.

**Riferimenti:** [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Sosta termica nella fusione di una sostanza pura.

**Informazioni fornite:** Acqua pura, pressione atmosferica costante, ghiaccio già in fusione.

Due masse diverse di ghiaccio puro stanno fondendo a pressione atmosferica costante. Quella maggiore deve raggiungere una temperatura di fusione più alta?

- **A.** No: per fondere la massa maggiore serve meno energia.
- **B.** No: cambia l’energia necessaria, non la temperatura di fusione.
- **C.** Sì: una massa maggiore ha sempre temperatura maggiore.
- **D.** Sì: la temperatura di fusione cresce con la massa.

**Risposta corretta: B.** Nelle stesse condizioni la temperatura di fusione è la stessa. Una massa maggiore richiede invece più energia per completare il passaggio di stato.

**Distrattori:** D e C rendono la temperatura dipendente dalla quantità; A inverte la dipendenza dell’energia dalla massa.

**Motivo del livello:** Applica direttamente la sosta termica.

**Trasferimento al contesto:** Confronto fra dimensione del campione e proprietà della trasformazione, senza usare una curva di riscaldamento.

### termo-014 — Facile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 45 secondi.

**Riferimenti:** [irraggiamento_it.html](../../../irraggiamento_it.html).

**Conoscenze richieste e argomenti:** Assorbimento, riflessione e trasmissione.

**Informazioni fornite:** Pannelli opachi, stessa radiazione incidente.

Due pannelli opachi ricevono la stessa energia radiante E. Le frazioni riflesse soddisfano r₁ > r₂. Quale confronto riguarda le energie assorbite Q₁ e Q₂?

- **A.** Entrambi ne assorbono la stessa quantità.
- **B.** Il primo non ne assorbe mai.
- **C.** Il primo ne assorbe di meno.
- **D.** Il primo ne assorbe di più.

**Risposta corretta: C.** Un pannello opaco non trasmette la radiazione considerata: l’energia incidente si divide fra riflessa e assorbita. Aumentando la quota riflessa, diminuisce quella assorbita.

**Distrattori:** D inverte la relazione; A ignora la riflessione; B confonde una quota maggiore con riflessione totale.

**Motivo del livello:** Una sola deduzione dalla ripartizione della radiazione.

**Trasferimento al contesto:** La previsione riguarda l’energia assorbita, senza assumere uguali temperature finali o capacità termiche.

### termo-015 — Facile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 45 secondi.

**Riferimenti:** [conduzione_it.html](../../../conduzione_it.html); [temperatura_equilibrio_termico_it.html](../../../temperatura_equilibrio_termico_it.html).

**Conoscenze richieste e argomenti:** Verso del trasferimento e isolamento termico.

**Informazioni fornite:** Bottiglia fredda in ambiente caldo, involucro che riduce gli scambi.

Una bottiglia fredda viene avvolta in un materiale isolante e lasciata in una stanza più calda. Qual è l’effetto dell’involucro?

- **A.** Impedisce alla bottiglia di possedere energia interna.
- **B.** Fa uscire più rapidamente energia dalla bevanda.
- **C.** Rallenta l’ingresso di energia dall’ambiente.
- **D.** Produce energia che raffredda la bevanda.

**Risposta corretta: C.** L’energia tende a passare dall’ambiente più caldo alla bottiglia. L’isolante rallenta questo trasferimento e quindi il riscaldamento.

**Distrattori:** A confonde isolamento ed energia posseduta; D attribuisce produzione di freddo all’isolante; B inverte il verso.

**Motivo del livello:** Applica il verso del calore a una bevanda fredda.

**Trasferimento al contesto:** Uso dell’isolante per conservare una temperatura inferiore a quella esterna.

### termo-016 — Facile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 50 secondi.

**Riferimenti:** [energia_interna_calore_specifico_it.html](../../../energia_interna_calore_specifico_it.html).

**Conoscenze richieste e argomenti:** C = m · c; proprietà del corpo e del materiale.

**Informazioni fornite:** Acqua nello stesso stato e alla stessa temperatura.

Una quantità d’acqua di massa m e temperatura iniziale T viene divisa in due porzioni di masse uguali m₁ = m₂, ciascuna pari a metà di m, alla stessa temperatura T. Rispetto all’acqua prima della divisione, come cambiano le proprietà di ciascuna porzione?

- **A.** La capacità termica si dimezza e il calore specifico resta uguale.
- **B.** Capacità termica e calore specifico si dimezzano.
- **C.** La capacità termica resta uguale e il calore specifico si dimezza.
- **D.** Capacità termica e calore specifico restano uguali.

**Risposta corretta: A.** C = m · c: dimezzare la massa dimezza C. Il calore specifico c riguarda il materiale e resta lo stesso nelle condizioni date.

**Distrattori:** B tratta c come proprietà estensiva; C scambia i ruoli di D e c; D ignora la riduzione di massa.

**Motivo del livello:** Segue direttamente l’effetto della massa su C.

**Trasferimento al contesto:** La divisione materiale del campione distingue proprietà del corpo e proprietà della sostanza.

### termo-017 — Facile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 45 secondi.

**Riferimenti:** [temperatura_equilibrio_termico_it.html](../../../temperatura_equilibrio_termico_it.html).

**Conoscenze richieste e argomenti:** Conversione fra Celsius e kelvin.

**Informazioni fornite:** Temperatura di 25 °C.

Una sonda indica una temperatura Celsius T_°C = 25 °C. Qual è la stessa temperatura in kelvin T_K?

- **A.** 298,15 K
- **B.** 248,15 K
- **C.** 25 K
- **D.** 273,15 K

**Risposta corretta: A.** Per la temperatura assoluta si aggiunge 273,15 al valore Celsius: 25 + 273,15 = 298,15 K.

**Distrattori:** B sottrae il valore Celsius; C confonde temperatura e intervallo; D omette i 25 gradi.

**Motivo del livello:** Una sola conversione diretta.

### termo-018 — Facile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 50 secondi.

**Riferimenti:** [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Q = m · L.

**Informazioni fornite:** Massa e calore latente; ghiaccio già a 0 °C.

Quanta energia Q serve per fondere completamente ghiaccio puro di massa m = 0,050 kg, già alla temperatura T = 0 °C? Il calore latente specifico di fusione è L = 334 kJ/kg e la pressione atmosferica è costante.

- **A.** 167 kJ
- **B.** 0 kJ
- **C.** 6,68 kJ
- **D.** 16,7 kJ

**Risposta corretta: D.** Q = m · L = 0,050 · 334 kJ = 16,7 kJ. La temperatura iniziale è già quella di fusione: serve il solo contributo latente.

**Distrattori:** C divide impropriamente il valore numerico; A sbaglia la virgola della massa; B identifica temperatura costante ed energia nulla.

**Motivo del livello:** Un solo prodotto, con unità coerenti.

### termo-019 — Facile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 45 secondi.

**Riferimenti:** [conduzione_it.html](../../../conduzione_it.html).

**Conoscenze richieste e argomenti:** Q = P · Δt.

**Informazioni fornite:** Potenza termica costante e durata in secondi.

Un dispositivo trasferisce energia termica con potenza costante P = 800 W per un intervallo di tempo Δt = 180 s. Quanta energia Q trasferisce?

- **A.** 4,44 kJ
- **B.** 980 kJ
- **C.** 0,144 kJ
- **D.** 144 kJ

**Risposta corretta: D.** Q = P · Δt = 800 · 180 J = 144 000 J = 144 kJ.

**Distrattori:** A divide potenza e tempo e altera l’unità; C omette il fattore 1000 nella conversione; B somma dati di grandezze diverse.

**Motivo del livello:** Applica direttamente energia uguale potenza per durata.

### termo-020 — Media, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 55 secondi.

**Riferimenti:** [stati_della_materia.html](../../../stati_della_materia.html).

**Conoscenze richieste e argomenti:** Viscosità e densità come proprietà distinte.

**Informazioni fornite:** Nessuna proprietà di uno specifico liquido.

Quale affermazione distingue correttamente densità e viscosità di un liquido?

- **A.** La densità è massa per volume; la viscosità descrive la resistenza allo scorrimento.
- **B.** Una densità maggiore implica sempre una viscosità maggiore.
- **C.** La densità misura la resistenza allo scorrimento; la viscosità la massa per volume.
- **D.** La viscosità è la massa totale del liquido; la densità dipende solo dal recipiente.

**Risposta corretta: A.** La densità collega massa e volume. La viscosità riguarda la resistenza allo scorrimento: una proprietà non determina automaticamente l’altra.

**Distrattori:** C scambia le definizioni; B introduce una dipendenza universale inesistente; D confonde proprietà e quantità totale.

**Motivo del livello:** Distingue proprietà spesso confuse.

### termo-021 — Media, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 65 secondi.

**Riferimenti:** [irraggiamento_it.html](../../../irraggiamento_it.html); [temperatura_equilibrio_termico_it.html](../../../temperatura_equilibrio_termico_it.html).

**Conoscenze richieste e argomenti:** Termografia, emissività e riflessione.

**Informazioni fornite:** Due superfici con diversa finitura, stessa temperatura reale.

Due superfici alla stessa temperatura hanno finiture diverse e appaiono differenti in una termografia. Quale affermazione è corretta?

- **A.** La superficie meno luminosa ha smesso di emettere radiazione.
- **B.** La termocamera rileva soltanto luce visibile riflessa.
- **C.** Emissione e riflessione possono produrre segnali diversi anche alla stessa temperatura.
- **D.** La superficie più luminosa è necessariamente più calda.

**Risposta corretta: C.** Una termocamera rileva radiazione infrarossa. Finiture diverse modificano emissione e riflessione: segnali differenti non dimostrano da soli temperature reali differenti.

**Distrattori:** D identifica segnale e temperatura senza controllare la superficie; B confonde infrarosso e visibile; A interpreta un segnale minore come emissione nulla.

**Motivo del livello:** Distingue misura indiretta e grandezza da misurare.

### termo-022 — Media, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 55 secondi.

**Riferimenti:** [temperatura_equilibrio_termico_it.html](../../../temperatura_equilibrio_termico_it.html).

**Conoscenze richieste e argomenti:** Principio zero ed equilibrio termico.

**Informazioni fornite:** A e B sono ciascuno in equilibrio con C nelle condizioni considerate.

A e B sono ciascuno in equilibrio termico con C. Quale conclusione esprime il principio zero?

- **A.** A e B possiedono la stessa energia interna.
- **B.** A e B hanno la stessa temperatura.
- **C.** Fra A e C non può mai essere stata trasferita energia.
- **D.** A e B hanno necessariamente la stessa massa.

**Risposta corretta: B.** Il principio zero permette di concludere che A e B sono in equilibrio termico fra loro e quindi hanno la stessa temperatura. Non impone uguaglianza di massa o energia interna.

**Distrattori:** A e D aggiungono uguaglianze non richieste; C confonde equilibrio presente e assenza di scambi precedenti.

**Motivo del livello:** Richiede distinguere equilibrio termico e uguaglianza di energia.

### termo-023 — Media, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 70 secondi.

**Riferimenti:** [dilatazione_termica_it.html](../../../dilatazione_termica_it.html); [convezione_it.html](../../../convezione_it.html).

**Conoscenze richieste e argomenti:** Massimo di densità dell’acqua a circa 4 °C; confronto di densità nella convezione naturale.

**Informazioni fornite:** Acqua dolce, pressione atmosferica; strato superficiale riscaldato da 2 a 4 °C su acqua a 2 °C.

In un recipiente l’acqua dolce ha temperatura iniziale T_i = 2 °C. Si riscalda lentamente solo lo strato superiore fino alla temperatura finale T_s = 4 °C, mentre l’acqua sottostante resta alla temperatura T_b = 2 °C. A pressione atmosferica, quale tendenza ha lo strato superiore rispetto all’acqua sottostante?

- **A.** Resta alla stessa densità perché è ancora liquido.
- **B.** Diventa più denso e tende a scendere.
- **C.** Diventa meno denso e tende a salire.
- **D.** Si solidifica perché la densità aumenta.

**Risposta corretta: B.** Tra 2 e 4 °C l’acqua si contrae e diventa più densa. Lo strato superiore tende quindi a scendere: in questo intervallo non vale la previsione generica che il riscaldamento renda sempre meno denso un fluido.

**Distrattori:** C estende il comportamento ordinario all’intervallo anomalo; A ignora la dilatazione; D confonde variazione di densità e cambiamento di stato.

**Motivo del livello:** Collega anomalia dell’acqua e moto per differenza di densità.

**Trasferimento al contesto:** Si riscalda dall’alto nell’intervallo anomalo, invece di descrivere il raffreddamento del lago.

### termo-024 — Media, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 65 secondi.

**Riferimenti:** [termodinamica_sistemi_it.html](../../../termodinamica_sistemi_it.html); [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Confine del sistema e condensazione.

**Informazioni fornite:** Recipiente sigillato integro; sistema comprende pareti e tutto il contenuto.

In un recipiente sigillato una parte del vapore condensa sulle pareti interne. Il sistema comprende recipiente e tutto il contenuto. La condensazione rende il sistema aperto?

- **A.** Sì, perché il vapore scompare dal gas.
- **B.** No, perché il cambiamento avviene all’interno senza materia che attraversi il confine.
- **C.** Sì, perché le gocce trasportano energia alle pareti.
- **D.** No, perché un sistema con pareti non può mai essere aperto.

**Risposta corretta: B.** La materia passa dal gas al liquido restando all’interno. La classificazione dipende dagli scambi attraverso il confine scelto, non dai cambiamenti interni.

**Distrattori:** A scambia un passaggio interno con una perdita; C confonde energia e materia; D considera decisiva la presenza di pareti.

**Motivo del livello:** Richiede distinguere trasferimento interno e scambio attraverso il confine.

**Trasferimento al contesto:** Si deve scegliere il confine complessivo per interpretare una redistribuzione interna fra stati.

### termo-025 — Media, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 65 secondi.

**Riferimenti:** [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** La temperatura di ebollizione dipende dalla pressione; sosta termica.

**Informazioni fornite:** Acqua pura, pressione minore costante con ebollizione a 90 °C, riscaldamento uniforme.

In una prova a pressione costante l’acqua pura ha temperatura di ebollizione T_eb = 90 °C. Si continua a fornire energia mentre rimangono sia liquido sia vapore in ebollizione. Che cosa si prevede?

- **A.** La temperatura scende perché ogni vaporizzazione raffredda sempre il liquido.
- **B.** La temperatura resta circa 90 °C perché non viene più assorbita energia.
- **C.** La temperatura resta circa 90 °C e aumenta la massa trasformata in vapore.
- **D.** La temperatura deve salire fino a 100 °C prima di produrre altro vapore.

**Risposta corretta: C.** Alla pressione della prova, 90 °C è la temperatura di ebollizione. L’energia aggiunta sostiene la vaporizzazione finché rimane liquido, senza imporre un aumento fino a 100 °C.

**Distrattori:** D usa 100 °A indipendentemente dalla pressione; A estende il raffreddamento evaporativo all’ebollizione riscaldata; B confonde sosta termica e scambio nullo.

**Motivo del livello:** Applica la curva di riscaldamento a condizioni diverse da quelle ordinarie.

**Trasferimento al contesto:** La sosta termica viene prevista a una pressione diversa senza richiedere dati esterni sulla pressione.

### termo-026 — Media, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 65 secondi.

**Riferimenti:** [convezione_it.html](../../../convezione_it.html); [temperatura_equilibrio_termico_it.html](../../../temperatura_equilibrio_termico_it.html).

**Conoscenze richieste e argomenti:** Convezione forzata e verso dello scambio.

**Informazioni fornite:** Sonda asciutta a 20 °C, aria a 35 °C; si isola il contributo convettivo.

Una sonda asciutta ha temperatura iniziale T_s = 20 °C e si trova in aria alla temperatura T_a = 35 °C. Una ventola rinnova più rapidamente l’aria sulla sonda. Considerando soltanto la convezione, quale effetto è coerente?

- **A.** La sonda deve raggiungere una temperatura inferiore a 20 °C.
- **B.** La sonda non scambia energia, perché manca evaporazione.
- **C.** La sonda può riscaldarsi più rapidamente verso la temperatura dell’aria.
- **D.** La sonda viene raffreddata, perché ogni ventola produce aria fredda.

**Risposta corretta: C.** L’aria è più calda della sonda e le cede energia. Il ricambio può rendere più rapido lo scambio: la ventola non ne inverte il verso.

**Distrattori:** D e A attribuiscono alla ventola produzione di freddo; B rende necessaria l’evaporazione per ogni scambio.

**Motivo del livello:** Distingue aumento dello scambio e raffreddamento.

**Trasferimento al contesto:** Il dispositivo chiamato comunemente di raffreddamento viene impiegato con aria più calda del corpo.

### termo-027 — Media, calcolo

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 80 secondi.

**Riferimenti:** [conduzione_it.html](../../../conduzione_it.html).

**Conoscenze richieste e argomenti:** Fourier e conversione centimetri-metri.

**Informazioni fornite:** λ, area, spessore, temperature delle facce; regime stazionario senza sorgenti.

Una lastra piana omogenea ha conducibilità termica λ = 0,030 W/(m · K), area A = 2,0 m² e spessore s = 4,0 cm. Le temperature delle facce sono T₁ = 30 °C e T₂ = 10 °C. In regime stazionario e senza sorgenti interne, quale potenza termica P attraversa la lastra?

- **A.** 0,30 W
- **B.** 30 W
- **C.** 300 W
- **D.** 3,0 W

**Risposta corretta: B.** Lo spessore è 0,040 m e ΔT = 20 K. Il prodotto λ · A · ΔT vale 1,2 W · m. Ripartito sullo spessore di 0,040 m dà una potenza di 30 W.

**Distrattori:** A usa 4 come spessore in metri; D e C rappresentano errori di conversione di un fattore 10.

**Motivo del livello:** Occorre scegliere ΔT delle facce e convertire lo spessore.

### termo-028 — Media, calcolo

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 80 secondi.

**Riferimenti:** [bilancio_termico_it.html](../../../bilancio_termico_it.html); [energia_interna_calore_specifico_it.html](../../../energia_interna_calore_specifico_it.html).

**Conoscenze richieste e argomenti:** Bilancio termico con uguale c e masse diverse.

**Informazioni fornite:** Masse, temperature; niente dispersioni o cambiamenti di stato.

Si mescolano una porzione d’acqua di massa m₁ = 0,15 kg e temperatura iniziale T₁ = 80 °C e una di massa m₂ = 0,45 kg e temperatura iniziale T₂ = 20 °C. Trascurando recipiente e dispersioni e assumendo uguale calore specifico c costante, qual è la temperatura finale T_f?

- **A.** 65 °C
- **B.** 50 °C
- **C.** 35 °C
- **D.** 40 °C

**Risposta corretta: C.** Il bilancio pesa le temperature con le masse: i contributi numerici sono 0,15 · 80 = 12 e 0,45 · 20 = 9. La loro somma 21, distribuita sulla massa totale 0,60 kg, dà 35 °C.

**Distrattori:** B fa la media aritmetica; A scambia i pesi delle masse; D assegna pesi non coerenti con il rapporto 1 a 3.

**Motivo del livello:** Sceglie una media pesata invece di quella aritmetica.

### termo-029 — Media, calcolo

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 65 secondi.

**Riferimenti:** [energia_interna_calore_specifico_it.html](../../../energia_interna_calore_specifico_it.html).

**Conoscenze richieste e argomenti:** Q = C · ΔT e temperatura finale.

**Informazioni fornite:** C costante, calore assorbito, temperatura iniziale e assenza di cambiamenti di stato.

Un corpo ha temperatura iniziale T_i = 15 °C e assorbe calore Q = 3,0 kJ senza cambiare stato. La sua capacità termica costante è C = 120 J/K. Quale temperatura finale T_f raggiunge?

- **A.** −10 °C
- **B.** 375 °C
- **C.** 25 °C
- **D.** 40 °C

**Risposta corretta: D.** 3,0 kJ corrispondono a 3000 J. Ogni kelvin richiede 120 J, quindi l’aumento è 25 K. La temperatura finale è 15 °C + 25 °C = 40 °C.

**Distrattori:** C confonde variazione e temperatura finale; B moltiplica impropriamente i dati; A sottrae la variazione nonostante l’assorbimento.

**Motivo del livello:** Ricava prima la variazione, poi la temperatura finale.

### termo-030 — Difficile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 80 secondi.

**Riferimenti:** [energia_interna_calore_specifico_it.html](../../../energia_interna_calore_specifico_it.html).

**Conoscenze richieste e argomenti:** Condizioni di definizione del calore specifico dei gas.

**Informazioni fornite:** La tabella riporta c a pressione costante.

Una tabella riporta il calore specifico di un gas a pressione costante. Quale uso del dato è giustificato?

- **A.** Usarlo per una vaporizzazione a temperatura costante al posto del calore latente.
- **B.** Usarlo per qualsiasi trasformazione del gas purché la massa sia nota.
- **C.** Usarlo per un riscaldamento a pressione costante nell’intervallo di validità indicato.
- **D.** Usarlo a volume costante perché il calore specifico dipende solo dalla sostanza.

**Risposta corretta: C.** Per i gas il calore specifico dipende dalle condizioni della trasformazione. Il valore a pressione costante non si trasferisce automaticamente al caso a volume costante e non sostituisce un calore latente.

**Distrattori:** B e D ignorano le condizioni del dato; A confonde riscaldamento e cambiamento di stato.

**Motivo del livello:** Riconosce un limite essenziale di un dato tabulato.

### termo-031 — Difficile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** specifico. **Tempo stimato:** 85 secondi.

**Riferimenti:** [irraggiamento_it.html](../../../irraggiamento_it.html).

**Conoscenze richieste e argomenti:** Distinzione fra emissione e potenza netta; condizioni della formula con ambiente uniforme.

**Informazioni fornite:** Un corpo esposto anche a radiazione solare diretta.

Nel modello di scambio radiativo netto, le temperature del corpo e dell’ambiente uniforme sono T e T_a; nella formula compare T⁴ − T_a⁴. Se sul corpo arriva anche radiazione solare diretta, come va trattata?

- **A.** Va sostituita alla potenza emessa, che diventa nulla alla luce del Sole.
- **B.** Va considerata separatamente, contando soltanto la frazione effettivamente assorbita.
- **C.** È già inclusa automaticamente nella temperatura dell’aria circostante.
- **D.** Va aggiunta tutta, compresa la frazione riflessa, alla potenza assorbita.

**Risposta corretta: B.** La formula descrive lo scambio con le superfici circostanti a temperatura uniforme. Il contributo solare diretto va trattato a parte e solo la frazione assorbita entra nell’energia acquistata dal corpo.

**Distrattori:** A annulla impropriamente l’emissione; C confonde ambiente radiativo e temperatura dell’aria; D include energia riflessa come assorbita.

**Motivo del livello:** Richiede riconoscere ciò che il modello include e ciò che deve restare separato.

### termo-032 — Difficile, conoscenza

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 80 secondi.

**Riferimenti:** [stati_della_materia.html](../../../stati_della_materia.html); [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Solido amorfo, fusione netta e condizioni delle soste termiche.

**Informazioni fornite:** Confronto fra vetro e cristallo puro.

Perché non si può applicare automaticamente al vetro il modello della fusione a temperatura costante di un cristallo puro?

- **A.** Il vetro non assorbe energia mentre viene riscaldato.
- **B.** Il vetro è già liquido perché non possiede ordine periodico a grande distanza.
- **C.** Ogni solido cristallino fonde senza ricevere energia.
- **D.** Il vetro è amorfo e si ammorbidisce gradualmente, pur essendo un solido.

**Risposta corretta: D.** La struttura amorfa non rende il vetro un liquido. Il suo ammorbidimento graduale non corrisponde alla fusione netta descritta per un cristallo puro nelle condizioni date.

**Distrattori:** B identifica solidità e ordine cristallino; A nega lo scambio energetico; C nega l’energia latente.

**Motivo del livello:** Distingue proprietà macroscopica di solido e ordine microscopico, evitando un’estensione indebita del modello.

### termo-033 — Difficile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 90 secondi.

**Riferimenti:** [bilancio_termico_it.html](../../../bilancio_termico_it.html); [conduzione_it.html](../../../conduzione_it.html).

**Conoscenze richieste e argomenti:** Bilancio di tre corpi e distinzione fra velocità dello scambio ed equilibrio finale.

**Informazioni fornite:** Capacità termiche costanti C, C e 2C; sistema isolato senza cambiamenti di stato.

Tre corpi hanno temperature iniziali T₁ = 10 °C, T₂ = 40 °C e T₃ = 70 °C. Le capacità termiche sono C₁ = C, C₂ = C e C₃ = 2C, costanti. Sono posti in contatto in un sistema isolato, senza cambiamenti di stato. Il secondo corpo si riscalda o si raffredda all’equilibrio finale?

- **A.** Non si può stabilire senza conoscere le conducibilità dei tre corpi.
- **B.** Resta a 40 °C, perché questa è la media delle temperature estreme.
- **C.** Si riscalda, perché la temperatura finale è pesata maggiormente dal corpo caldo.
- **D.** Si raffredda, perché il corpo a 10 °C ha il maggiore salto termico.

**Risposta corretta: C.** A 40 °C il corpo freddo richiederebbe C · 30 K, mentre quello caldo cederebbe 2C · 30 K. Resta energia per portare l’equilibrio sopra 40 °C: il corpo intermedio si riscalda. Le conducibilità influenzano i tempi, non il bilancio finale nelle ipotesi date.

**Distrattori:** D ignora le capacità termiche; B usa una media non pesata; A confonde durata ed equilibrio.

**Motivo del livello:** Coordina tre contributi energetici e distingue un fattore dinamico da uno che fissa l’equilibrio.

**Trasferimento al contesto:** Lo scambio del corpo intermedio va dedotto dal bilancio degli altri due, senza presumere un verso dal solo valore iniziale.

### termo-034 — Difficile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 90 secondi.

**Riferimenti:** [dilatazione_termica_it.html](../../../dilatazione_termica_it.html); [temperatura_equilibrio_termico_it.html](../../../temperatura_equilibrio_termico_it.html).

**Conoscenze richieste e argomenti:** Dilatazione relativa di liquido e recipiente; lettura termometrica.

**Informazioni fornite:** Liquido e volume interno del recipiente hanno lo stesso coefficiente volumico, costante nello stesso intervallo.

Si costruisce un termometro a liquido. Nell’intervallo considerato il liquido e il volume interno del recipiente hanno coefficienti di dilatazione volumica uguali, β_l = β_r. Riscaldandoli uniformemente, che cosa accade al livello rispetto alle tacche solidali al recipiente?

- **A.** Scende, perché il recipiente si dilata mentre il liquido resta invariato.
- **B.** Sale come in ogni termometro, perché il liquido si dilata.
- **C.** Sale il doppio, perché si sommano le dilatazioni del liquido e del recipiente.
- **D.** Resta circa sulla stessa tacca, perché manca la dilatazione relativa.

**Risposta corretta: D.** Il liquido e lo spazio che lo contiene crescono della stessa frazione. Nel modello non compare volume in eccesso rispetto alle tacche: la sola dilatazione del liquido non basta a produrre una lettura variabile.

**Distrattori:** B considera solo il liquido; A lo considera indeformabile; C somma contributi che vanno confrontati.

**Motivo del livello:** Controlla se il meccanismo di misura produce un segnale quando cambiano insieme due parti.

**Trasferimento al contesto:** Un materiale ipotetico con uguale espansione del contenitore mette alla prova il principio di funzionamento dello strumento.

### termo-035 — Difficile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 90 secondi.

**Riferimenti:** [convezione_it.html](../../../convezione_it.html); [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Convezione con aria più calda della pelle; evaporazione e bilancio complessivo.

**Informazioni fornite:** Aria più calda della pelle, pelle bagnata; la ventola aumenta sia convezione sia evaporazione.

L’aria è più calda della pelle bagnata. Accendendo una ventola aumentano sia lo scambio convettivo sia l’evaporazione. Senza conoscere l’entità dei due contributi, che cosa si può concludere?

- **A.** La pelle si riscalda certamente, perché l’aria è più calda.
- **B.** La convezione apporta energia e l’evaporazione la sottrae; il risultato complessivo resta da valutare.
- **C.** Nessun trasferimento avviene, perché i due effetti sono opposti.
- **D.** La pelle si raffredda certamente, perché aumenta l’evaporazione.

**Risposta corretta: B.** L’aria più calda cede energia alla pelle per convezione. L’evaporazione sottrae energia. Sapere che entrambi gli effetti aumentano non permette di stabilire quale prevalga.

**Distrattori:** D e A selezionano un solo contributo; C confonde opposizione dei segni e uguaglianza delle quantità.

**Motivo del livello:** Distingue contributi energetici concorrenti senza inferire un segno totale non determinato.

**Trasferimento al contesto:** Una modifica unica intensifica due processi di segno opposto: la risposta corretta riconosce l’informazione mancante.

### termo-036 — Difficile, ragionamento

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 90 secondi.

**Riferimenti:** [dilatazione_termica_it.html](../../../dilatazione_termica_it.html); [conduzione_it.html](../../../conduzione_it.html); [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Congelamento, densità e conduzione.

**Informazioni fornite:** Lago dolce sufficientemente profondo; ghiaccio superficiale, nessuna generalizzazione a ogni lago.

In un lago d’acqua dolce sufficientemente profondo si forma uno strato di ghiaccio superficiale. Quale spiegazione distingue correttamente il galleggiamento del ghiaccio dal suo effetto sull’acqua sottostante?

- **A.** Il ghiaccio è meno denso dell’acqua liquida e galleggia; lo strato superficiale rallenta gli scambi termici.
- **B.** Il ghiaccio è più denso e galleggia; produce energia che mantiene liquida l’acqua sottostante.
- **C.** Il ghiaccio galleggia perché è un isolante; la densità non influisce sulla sua posizione.
- **D.** Il ghiaccio galleggia perché cede calore; poi impedisce completamente ogni dispersione.

**Risposta corretta: A.** La minore densità del ghiaccio spiega il galleggiamento. Il rallentamento degli scambi aiuta a conservare acqua liquida sotto lo strato, senza annullare le perdite o produrre calore.

**Distrattori:** C scambia isolamento e causa del galleggiamento; D attribuisce galleggiamento al flusso termico e isolamento perfetto; B inverte le densità e inventa una sorgente.

**Motivo del livello:** Separa cause della posizione del ghiaccio e del rallentamento del raffreddamento sottostante.

**Trasferimento al contesto:** Occorre distinguere due effetti dello stesso strato, anziché assegnarli a un’unica proprietà.

### termo-037 — Difficile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 110 secondi.

**Riferimenti:** [conduzione_it.html](../../../conduzione_it.html); [passaggi_di_stato.html](../../../passaggi_di_stato.html).

**Conoscenze richieste e argomenti:** Fourier, Q = P · Δt e calore latente.

**Informazioni fornite:** Strato omogeneo in regime stazionario; tutta l’energia condotta fonde ghiaccio già a 0 °C; dati espliciti.

Uno strato piano ha conducibilità termica λ = 0,050 W/(m · K), area A = 0,20 m² e spessore s = 0,020 m. Le temperature delle facce sono mantenute a T₁ = 40 °C e T₂ = 0 °C. In regime stazionario tutta l’energia condotta fonde ghiaccio già alla temperatura T_g = 0 °C. Quanta massa m fonde nell’intervallo di tempo Δt = 300 s? Il calore latente specifico di fusione è L = 334 kJ/kg.

- **A.** Circa 6,0 g
- **B.** Circa 18 g
- **C.** Circa 60 g
- **D.** Circa 180 g

**Risposta corretta: B.** Il prodotto λ · A · ΔT vale 0,40 W · m: sullo spessore di 0,020 m corrisponde a P = 20 W. In 300 s passano 6000 J = 6,0 kJ. Ogni grammo richiede 0,334 kJ per fondere: si ottengono circa 18 g.

**Distrattori:** A tratta il numero di kJ come grammi; C usa 100 J/g al posto di L; D sbaglia di un fattore 10 la massa.

**Motivo del livello:** Collega potenza, durata e massa trasformata in tre passaggi brevi.

### termo-038 — Difficile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 110 secondi.

**Riferimenti:** [passaggi_di_stato.html](../../../passaggi_di_stato.html); [energia_interna_calore_specifico_it.html](../../../energia_interna_calore_specifico_it.html).

**Conoscenze richieste e argomenti:** Riscaldamento del solido, fusione, riscaldamento del liquido.

**Informazioni fornite:** Acqua pura a pressione atmosferica; c costanti forniti; niente dispersioni.

Quanta energia Q serve per portare ghiaccio di massa m = 0,10 kg dalla temperatura iniziale T_i = −10 °C ad acqua liquida alla temperatura finale T_f = 20 °C, a pressione atmosferica e senza dispersioni? I calori specifici di ghiaccio e acqua sono c_g = 2100 J/(kg · K) e c_a = 4200 J/(kg · K); il calore latente specifico di fusione è L = 334 kJ/kg.

- **A.** 12,6 kJ
- **B.** 43,9 kJ
- **C.** 41,8 kJ
- **D.** 33,4 kJ

**Risposta corretta: B.** Per scaldare il ghiaccio fino a 0 °C servono 0,10 · 2100 · 10 J = 2,1 kJ. La fusione richiede 33,4 kJ. Scaldare l’acqua fino a 20 °C richiede 0,10 · 4200 · 20 J = 8,4 kJ. Totale: 43,9 kJ.

**Distrattori:** D conta solo la fusione; C omette il riscaldamento del ghiaccio; A usa il calore specifico dell’acqua per tutto l’intervallo e omette la fusione.

**Motivo del livello:** Sceglie e somma tre contributi di natura diversa.

### termo-039 — Difficile, calcolo

**Categoria:** `termologia`. **Prerequisiti:** trasversale. **Tempo stimato:** 110 secondi.

**Riferimenti:** [bilancio_termico_it.html](../../../bilancio_termico_it.html); [energia_interna_calore_specifico_it.html](../../../energia_interna_calore_specifico_it.html).

**Conoscenze richieste e argomenti:** Bilancio con due materiali e capacità termica del recipiente.

**Informazioni fornite:** Masse, calori specifici costanti, capacità termica della tazza e temperature; sistema isolato senza cambiamenti di stato.

Un blocco ha massa m_b = 0,20 kg, calore specifico c_b = 900 J/(kg · K) e temperatura iniziale T_b = 80 °C. Viene immerso in acqua di massa m_a = 0,10 kg e temperatura iniziale T_a = 20 °C, dentro una tazza di temperatura iniziale T_t = 20 °C e capacità termica C = 120 J/K. Il calore specifico dell’acqua è c_a = 4200 J/(kg · K). Senza dispersioni o cambiamenti di stato, qual è la temperatura finale T_f?

- **A.** 35 °C
- **B.** 38 °C
- **C.** 60 °C
- **D.** 50 °C

**Risposta corretta: A.** Le capacità termiche sono 180 J/K per il blocco, 420 J/K per l’acqua e 120 J/K per la tazza. Il blocco cede 180 · (80 − T_f) J; acqua e tazza assorbono insieme 540 · (T_f − 20) J. Il bilancio dà 720 · T_f = 25 200, quindi T_f = 35 °C.

**Distrattori:** B trascura la tazza; D fa la media non pesata delle due temperature; C pesa con le sole masse ignorando materiali e tazza.

**Motivo del livello:** Imposta il bilancio di tre parti con pesi termici differenti.

## Revisione e integrazione

Ogni quesito è stato risolto e confrontato con il campione per evitare duplicati e semplici sostituzioni numeriche. Alcuni principi ricorrono con operazioni diverse: termo-018 applica direttamente il calore latente, mentre termo-037 lo collega alla conduzione e termo-038 distingue tre fasi termiche. Le fonti riguardano soltanto Termologia; le proprietà particolari e i dati necessari sono dichiarati nei quesiti.

Il lotto è stato approvato dal docente, che ha autorizzato la produzione di tutte le domande rimanenti. I 30 record restano invariati rispetto al commit `03ab66243a60bdd93decdb4227e1c9dd435616b5`; la conferma non approva preventivamente i quesiti nuovi. Resta da verificare con gli studenti la calibrazione dei livelli e dei tempi stimati. I risultati automatici e i conteggi sono registrati nel file [di stato](../stato.md). Merge e pubblicazione restano subordinati all’anteprima corrente.
