# Revisione editoriale — materia e passaggi di stato

Proposta del 17 ottobre 2026. Master v53. Aggiornamento: l'utente ha risposto «Approvo» alla proposta di suddivisione e al tema attuale. I file delle nuove visuali restano da fornire; bozze complete scritte e da approvare.

## Fonte e risultato previsto

Fonte verificata: `stati_della_materia_e_passaggi_di_stato.html`, v8, 19.864.994 byte, blob Git `8ef5566c73f670dbf23b550e4e36a52cdb7ddfc2`, letto integralmente con parser `huge_tree=True`. Base del ramo: `d72296ad77a2ae92342386c7dfeb73cc1b44e736` (`main`).

Due HTML italiani autonomi, ciascuno con titolo, copertina, teoria e domande finali. Applicazioni ed esercizi svolti già presenti restano nel secondo capitolo, nell'ordine prescritto. Tema: conservare quello della v8, già documentato come approvato nello stato. Nessun nuovo tema, lingua o modello di simulazione.

| Contenuti della v8 | Destinazione proposta | Intervento |
| --- | --- | --- |
| Stati della materia: solidi, liquidi, gas e plasma | `stati_della_materia.html` | Riscrittura narrativa: proprietà osservabili → disposizione e movimento delle particelle → interpretazione |
| Simulazioni del moto molecolare | `stati_della_materia.html` | Distribuire i tre modelli vicino alle spiegazioni corrispondenti, conservando il modello fisico e verificando gli identificativi usati dallo script |
| Tabella delle proprietà | `stati_della_materia.html` | Conservare i contenuti pertinenti e renderla leggibile su telefono; evitare di ripetere tutta la teoria |
| Prime sei domande originali | Fine di `stati_della_materia.html` | Conservare i sei nuclei; alternare domanda aperta, previsione e vero/falso motivato |
| Passaggi di stato, mappa e trasformazioni | `passaggi_di_stato.html` | Un percorso continuo attraverso trasformazioni inverse e scambi di energia |
| Confronto evaporazione/ebollizione | `passaggi_di_stato.html` | Spiegare superficie, bolle e ruolo della pressione prima della tabella |
| Calore latente e curva di riscaldamento | `passaggi_di_stato.html` | Integrare Q = m · L nel ragionamento e spiegare assi, tratti inclinati e soste termiche |
| Applicazioni: sudore, frigoriferi/pompe di calore, centrali | Dopo la teoria di `passaggi_di_stato.html` | Sviluppare i tre casi già citati e associare immagini pertinenti, attualmente mancanti |
| Due esempi numerici già svolti | Dopo le applicazioni di `passaggi_di_stato.html` | Aggiungere situazione fisica illustrata, dati e ipotesi prima del calcolo; interpretare i risultati |
| Ultime otto domande originali | Fine di `passaggi_di_stato.html` | Conservare gli otto nuclei e variare le richieste di ragionamento; nessuna soluzione nelle domande finali |

Il calore latente resta nel capitolo sui passaggi di stato: quantifica lo stesso fenomeno, senza aprire un capitolo generale su calore, calorimetria o macchine termiche. La viscosità resta un confronto breve per capire i liquidi, senza introdurre una trattazione autonoma della fluidodinamica.

## Percorso del testo da scrivere dopo l'accordo sulle visuali

### Stati della materia

Apertura: il ghiaccio conserva la forma, mentre l'acqua si adatta al recipiente. Domanda centrale: come può la stessa sostanza presentare comportamenti così diversi? Collegare presto proprietà visibili e modello particellare, senza iniziare con un elenco di definizioni.

1. **Una forma che resiste.** Forma e volume del solido; particelle che vibrano, non immobili. Quarzo e vetro mostrano che essere solido non richiede un ordine cristallino a grande distanza.
2. **Scorrere senza disperdersi.** Nel liquido le particelle restano vicine ma cambiano vicini. L'olio introduce la resistenza allo scorrimento; distinguere viscosità e densità senza moltiplicare esempi non illustrati.
3. **Occupare lo spazio disponibile.** Distanze tra particelle, moto e comprimibilità dei gas; usare la mongolfiera come immagine di un involucro occupato dal gas, senza trasformarla in una digressione sul galleggiamento. Il fulmine introduce il plasma e le particelle cariche.
4. **Domande di verifica.** Sei quesiti sui sei nuclei originali: forma; cristallino/amorfismo; viscosità/densità; comprimibilità; lettura delle animazioni; plasma.

### Passaggi di stato

Apertura: i cubetti si sciolgono nel bicchiere, pur restando acqua. Domanda centrale: che cosa cambia nella sostanza e dove va l'energia che riceve? Usare la GIF esistente nel primo passaggio della spiegazione.

1. **Cambiare stato, restare la stessa sostanza.** Trasformazione fisica, mappa e versi degli scambi di energia; fusione e solidificazione come processi inversi.
2. **Un liquido può diventare gas in due modi.** Dalla goccia che diminuisce all'acqua che bolle: superficie e volume, evaporazione anche sotto la temperatura di ebollizione, bolle di vapore e pressione.
3. **Dal gas alle gocce o al ghiaccio.** Condensa sul vetro e nuvole; distinguere goccioline liquide da cristalli di ghiaccio. Ghiaccio secco e brina chiariscono i passaggi diretti tra solido e gas.
4. **Energia senza aumento di temperatura.** Curva dell'acqua a pressione atmosferica ordinaria e relazione del calore latente. Spiegare Q in joule, m in kilogrammi e L in J/kg, come energia necessaria per trasformare un kilogrammo. Interpretare la proporzionalità rispetto alla massa. Distinguere quantità assorbita e ceduta senza introdurre convenzioni di segno ambigue. Precisare che il calore latente di vaporizzazione dipende dalle condizioni: 2.257.000 J/kg è il valore vicino a 100 °C alla pressione atmosferica ordinaria, non quello da applicare automaticamente al sudore.
5. **Applicazioni.** Tre brevi sviluppi illustrati sui casi già presenti: evaporazione dalla pelle; evaporazione e condensazione nel circuito frigorifero e nella pompa di calore; acqua/vapore nel ciclo di una centrale. Non attribuire al solo cambiamento di stato il funzionamento completo di una macchina.
6. **Esercizi svolti.** Conservare 0,50 kg di ghiaccio a 0 °C e 0,20 kg di acqua all'ebollizione. Schema prima dei dati e del calcolo. Valori verificati: 167.000 J e 451.400 J. Escludere dal bilancio riscaldamento iniziale e dispersioni in modo esplicito e breve.
7. **Domande di verifica.** Otto quesiti sui nuclei originali: trasformazione fisica; lettura della mappa; evaporazione/ebollizione; nuvole; due calcoli; sudorazione; frigorifero. I due quesiti numerici coincidono oggi con gli svolgimenti: proporre una previsione o un confronto sui medesimi dati per richiedere ragionamento, anziché ripetere una soluzione appena letta.

## Visuali esistenti da riutilizzare

Gli indici seguenti sono quelli delle 13 immagini HTML nella fonte v8, a partire da zero. Non sono nomi di nuovi file.

| ID | Risorsa nella fonte | Collocazione e funzione |
| --- | --- | --- |
| M1–M2 | Immagini 0–1: quarzo e biglia di vetro | Confronto tra ordine cristallino e solido amorfo |
| M3 | Immagine 2: olio | Scorrimento e viscosità |
| M4 | Immagine 3: mongolfiera | Gas distribuito nel volume dell'involucro |
| M5 | Immagine 4: fulmine | Esempio di plasma |
| M6–M8 | Tre animazioni canvas e script esistenti | Moto nei tre stati, ciascuna vicino al testo pertinente; modelli qualitativi non in scala |
| P1 | Immagine 5: mappa dei passaggi | Relazioni tra stati e versi delle trasformazioni; mantenere lo schema scelto dall'utente |
| P2 | Immagine 6: GIF fusione | Apertura e spiegazione della fusione |
| P3–P4 | Immagini 7–8: GIF evaporazione ed ebollizione | Confronto dei fenomeni senza nuove animazioni |
| P5–P6 | Immagini 9–10: condensa e nuvole | Goccioline visibili e vapore invisibile |
| P7 | Immagine 11: ghiaccio secco | Sublimazione; spiegare la nube di goccioline senza confonderla con CO₂ visibile |
| P8 | Immagine 12: brina | Deposizione diretta da vapore a ghiaccio |
| P9 | Grafico SVG esistente | Curva di riscaldamento: ricostruzione adattata al telefono con assi e condizioni espliciti, andamento qualitativo senza inventare dati sperimentali |
| P10–P11 | Tabelle esistenti | Proprietà degli stati e confronto evaporazione/ebollizione, in HTML semantico |

Le didascalie saranno riscritte vicino alle figure. Rimuovere dalla mappa la frase sulla provenienza dall'utente. I crediti necessari restano separati e collassabili. Le attribuzioni attuali sono generiche e per due GIF mancano fonte e licenza: non dichiarare completata la verifica delle licenze; richiedere i riferimenti originali mancanti.

## Nuovi materiali da fornire o scegliere

Non sono state avviate ricerche o generazioni di immagini.

| ID | Soggetto richiesto | Domanda a cui risponde e posizione |
| --- | --- | --- |
| C1 | Foto di ghiaccio e acqua nello stesso recipiente, distinta da tutte le figure esistenti | Copertina esclusiva di Stati della materia: stessa sostanza, diversa capacità di mantenere la forma |
| C2 | Foto ravvicinata di una trasformazione, per esempio gocce di condensa su una bottiglia fredda, distinta dalla condensa già presente | Copertina esclusiva di Passaggi di stato: dove compare il liquido quando il vapore cambia stato? |
| A1 | Foto o illustrazione leggibile di pelle con gocce di sudore | Accanto all'applicazione: l'evaporazione sottrae energia alla pelle |
| A2 | Schema illustrato del circuito frigorifero, con evaporatore interno e condensatore esterno riconoscibili | Accanto all'applicazione: dove il refrigerante assorbe e dove cede energia? Può sostenere anche il confronto con la pompa di calore |
| A3 | Schema illustrato di un ciclo acqua-vapore di centrale, con generatore di vapore, turbina e condensatore | Accanto al caso già citato: il fluido cambia stato in punti diversi del ciclo |
| E1–E2 | Immagini di ghiaccio in un recipiente e di acqua riscaldata in un recipiente, con fondo trasparente per gli schemi degli svolgimenti | Prima dei calcoli: massa considerata, temperatura iniziale e freccia dell'energia ricevuta. Verificare prima se le GIF esistenti consentono una composizione conforme e leggibile; se il fondo non è eliminabile senza perdita di informazione, servono originali adatti |

Per ridurre la preparazione di nuovi materiali, l'alternativa da concordare è limitare le applicazioni a sudorazione e circuito frigorifero e trasformare i due svolgimenti in quesiti finali. Questo riduce i visuali richiesti ma modifica il contenuto esistente: non viene applicato senza una scelta dell'utente. Le due copertine restano necessarie.

## Collegamenti e controlli previsti nella realizzazione

- Conservare il percorso pubblico `stati_della_materia_e_passaggi_di_stato.html` come accesso ai due capitoli, con mappa diretta degli ancoraggi storici verso il capitolo pertinente. Verificare anche i vecchi nomi gestiti dagli script di pubblicazione: evitare catene di reindirizzamenti e perdita dei frammenti.
- Aggiornare i riferimenti all'HTML originario nell'indice e nei metadati di catalogo interessati; verificare ogni percorso prodotto senza avviare la pubblicazione.
- Due collegamenti all'indice generale per ciascun HTML; indici interni coerenti; crediti prima del piè di pagina; nessun selettore di lingua.
- Verificare dimensioni effettive dei due file con risorse incorporate; segnalazione a 18 MB, limite di 20 MB. Nessuna compressione delle immagini senza accordo.
- Verificare scientificamente testo, condizioni e calcoli; integrità delle immagini e del codice riutilizzato; lettura a 390 e 1440 px, tastiera, ancoraggi, funzionamento offline e animazioni.
- Salvare i due stati di capitolo quando i confini sono confermati, evitando di duplicare la cronologia della fonte. Aggiornare la lavorazione originaria come coordinamento della suddivisione.

## Stima e dipendenze

Intero lavoro rimanente stimato: 40–70 minuti di lavoro, esclusa l'attesa di immagini, fonti e approvazioni. Impegno di calcolo basso: nessuna nuova simulazione, nessuna generazione di immagini. Ripartizione orientativa: 5–10 minuti per verifica e preparazione dei materiali disponibili; 15–25 per riscrittura e correzioni della bozza; 10–20 per integrazione e impaginazione dei due HTML; 10–15 per controlli e salvataggio. L'alternativa ridotta sopra descritta può risparmiare circa 10–15 minuti e riduce le dipendenze dai nuovi materiali.

Testi completi ora disponibili: [Stati della materia](../stati_della_materia/bozza.md) e [Passaggi di stato](../passaggi_di_stato/bozza.md). Prossimo passaggio: sottoporre queste bozze con segnaposto all’approvazione secondo B1.1 e raccogliere i nuovi file visuali. Dopo l'approvazione della bozza, aggiornare la stima in base ai materiali effettivi e chiedere il via alla realizzazione HTML secondo B2. Questa proposta non è una dispensa completa e non sostituisce la v8.
