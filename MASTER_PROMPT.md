# PROMPT MASTER — PROCEDURA DI LAVORO

Aggiornamento: 17 ottobre 2026, ore 14:07 (Europe/Rome).

Questo documento governa pianificazione, decisioni, approvazioni e salvataggi del progetto «Materiale Didattico». Le regole specialistiche risiedono nei documenti seguenti. Applica soltanto le procedure pertinenti al compito; non aggiungere contenuti o lavorazioni perché una regola ne descrive la gestione.

| Fonte ufficiale | Ambito |
| --- | --- |
| [Master](MASTER_PROMPT.md) | Procedura di lavoro e manutenzione delle regole |
| [Contenuti e stile](riferimenti/CONTENUTI_E_STILE.md) | Destinatari, struttura, voce, formule e didascalie |
| [Tema grafico](riferimenti/TEMA_GRAFICO.md) | Aspetto e comportamento dell’interfaccia |
| [Requisiti tecnici](riferimenti/REQUISITI_TECNICI.md) | HTML, accessibilità tecnica, risorse, diritti, versioni e verifiche |

[AGENTS.md](AGENTS.md) indica quali fonti leggere per ogni attività. Lo stato corrente è in `lavorazione/<capitolo>/stato.md`; la cronologia è in Git.

<a id="p1"></a>
## P1. Richiesta e versione di partenza

Identifica argomento del singolo capitolo, risultato richiesto, file e versione da aggiornare. Usa i dati già disponibili; se manca l’argomento chiedilo prima di generare. Per un nuovo capitolo usa il riferimento grafico comune già approvato in [G1](riferimenti/TEMA_GRAFICO.md#g1). Non chiedere la lingua iniziale, già stabilita in [S2](riferimenti/CONTENUTI_E_STILE.md#s2).

Per una revisione parti dalla versione più recente disponibile e conserva le parti approvate. Se il file corrente non è accessibile o la sua identità è ambigua, chiarisci la situazione prima di modificarlo. Non ricostruire un’intera dispensa per una modifica locale.

Schema facoltativo per revisioni o richieste già definite; per nuove dispense segui prima [P2](MASTER_PROMPT.md#p2):
TITOLO / ARGOMENTI E CONTENUTI / ESEMPI DESIDERATI / IMMAGINI E INDICAZIONI / VIDEO E LINK / NOTE.
Per una revisione: FILE E VERSIONE / MODIFICA RICHIESTA / EVENTUALI VINCOLI.
Per una traduzione: FILE E VERSIONE / LINGUE / FILE SEPARATI O UNICO FILE.

<a id="p2"></a>
## P2. Workflow del singolo capitolo

1. Argomento e template. Definisci con l’utente il singolo argomento e i suoi confini; usa il riferimento grafico comune già approvato in [G1](riferimenti/TEMA_GRAFICO.md#g1), senza ripetere la richiesta del template. Non richiedere un piano generale dell’intera dispensa. Individua la domanda iniziale e il fenomeno centrale come base per progettare le visuali.

2. Progettazione delle parti visuali. Dopo aver definito l’argomento, proponi suggerimenti testuali su che cosa mostrare, a quale domanda risponde ciascun elemento e dove sarà utile. L’utente cerca, sceglie e fornisce i file; non cercarli né generarli autonomamente, secondo [P8](MASTER_PROMPT.md#p8). Raccogli anche le sue idee per animazioni e simulazioni. Per ogni simulazione valuta prima correttezza del modello, fattibilità tecnica, limiti, potenza di calcolo richiesta durante lo sviluppo e sul dispositivo di lettura, e tempo stimato di realizzazione; proponi alternative più leggere quando utili. Non inventare misure o garanzie di prestazione. Concorda visuali e comportamento delle simulazioni prima di progettare il testo; non programmare ancora. Valuta criticamente comprensibilità per il biennio, prerequisiti, progressione logica, carico cognitivo e ridondanze, motivando eventuali correzioni scientifiche.

3. Modifica e accettazione dei visuali. Dopo la scelta degli originali, discuti con l’utente quali modifiche servono: traduzioni, ritagli, frecce, legende, etichette o altri adattamenti pertinenti. Concorda gli interventi prima di eseguirli; per quelli complessi applica la stima e il via di [P3](MASTER_PROMPT.md#p3). Prepara e mostra i visuali modificati separatamente dall’HTML, conservando gli originali. Raccogli le correzioni e attendi l’accettazione dei risultati prima di creare l’HTML. La richiesta di una modifica autorizza a eseguirla, ma non equivale all’accettazione anticipata del risultato; un successivo via esplicito, riferito ai risultati mostrati, vale come accettazione senza richiedere una conferma duplicata. Se non servono modifiche, registra questa scelta e riusa gli originali approvati.

4. Progettazione del testo. Sulla base dell’argomento e delle visuali accettate, prepara una bozza completa del capitolo in chat o in un file separato. Segui [S1](riferimenti/CONTENUTI_E_STILE.md#s1) e lo stile da blog. Nel punto previsto per ciascun elemento visuale inserisci un segnaposto identificabile, per esempio [IMMAGINE 1 — soggetto e funzione], [GRAFICO 1 — grandezze e relazione] o [SIMULAZIONE 1 — comportamento e comandi]. Non realizzare ancora l’HTML o le simulazioni. Fai vedere il testo e raccogli l’approvazione; applica le correzioni prima di passare alla realizzazione.

5. Stima e conferma a partire. Dopo l’accettazione dei visuali modificati e l’approvazione della bozza, prima di chiedere il via alla creazione dell’HTML, comunica un intervallo di tempo stimato totale e la ripartizione tra ottimizzazione delle copie dei materiali, eventuali simulazioni, integrazione del testo e impaginazione HTML, verifiche e salvataggio. Distingui le attività già concluse da quelle ancora da svolgere. Esplicita ipotesi, dipendenze e incertezze; distingui il tempo di lavoro dall’attesa di file o risposte dell’utente. Attendi la conferma esplicita a partire secondo [P3](MASTER_PROMPT.md#p3).

6. Realizzazione e verifica. Solo dopo il via crea l’HTML con i visuali accettati e realizza le eventuali simulazioni approvate, sostituisci i segnaposto, verifica e salva secondo [T8](riferimenti/REQUISITI_TECNICI.md#t8). Per i capitoli successivi ripeti soltanto questo workflow sul capitolo interessato, preservando quelli approvati e il tema comune. Produci capitoli monografici autonomi secondo [S3](riferimenti/CONTENUTI_E_STILE.md#s3); per suddividere le dispense esistenti registra i contenuti di provenienza e aggiorna i collegamenti secondo [T7](riferimenti/REQUISITI_TECNICI.md#t7). Le revisioni circoscritte non richiedono di ripetere tutte le fasi.

<a id="p3"></a>
## P3. Stima e approvazione dei lavori complessi

Le operazioni semplici, come correggere una frase, aggiungere una regola o effettuare una piccola modifica locale, si eseguono direttamente. Per lavori complessi — nuova dispensa, nuovo esercizio, nuova simulazione o ristrutturazione sostanziale — prima dell’esecuzione comunica:

- risultato e ambito proposti;
- intervallo realistico di tempo e impegno di calcolo basso, medio o elevato;
- operazioni che giustificano tempo e calcolo, e principali incertezze;
- eventuali alternative più semplici, con differenze nel risultato e relative stime.

Fornisci la spiegazione all’inizio, prima della richiesta di approvazione. Non inventare quantità di calcolo, costi o tempi precisi; una stima non è una garanzia. Per lavori lunghi o onerosi presenta alternative prima dell’approvazione; anche per quelli moderati segnala possibilità di risparmio significativo senza compromettere l’obiettivo. Lascia scegliere all’utente: non avviare automaticamente l’alternativa più lunga o complessa.

Per un nuovo capitolo segui la sequenza e le approvazioni di [P2](MASTER_PROMPT.md#p2), compresa la fase separata di modifica e accettazione dei visuali prima dell’HTML. La valutazione iniziale delle simulazioni non autorizza a programmarle. Per gli altri lavori complessi presenta la stima e attendi conferma prima dell’esecuzione; sono ammessi i controlli preliminari rapidi necessari alla stima. Se una modifica apparentemente semplice diventa complessa o aumenta sostanzialmente il tempo o il calcolo rispetto allo scopo approvato, spiega il motivo, presenta alternative e stima aggiornata e attendi una nuova conferma.

<a id="p4"></a>
## P4. Ordine delle operazioni

1. Recupera la versione di partenza e i materiali già utilizzabili; individua le parti da cambiare.
2. Risolvi prima le scelte che possono causare rifacimenti: contenuti, dati, modello fisico e immagini. Chiedi solo le decisioni mancanti che incidono davvero sul risultato.
3. Per scelta, modifica e accettazione dei visuali segui [P2](MASTER_PROMPT.md#p2) e [P8](MASTER_PROMPT.md#p8), senza anticipare l’HTML.
4. Prepara il contenuto e i calcoli; per una simulazione verifica prima modello, movimento, comandi essenziali e bilancio, poi cura l’aspetto. Non rifinire a lungo una soluzione il cui modello deve ancora essere deciso.
5. Integra i materiali accettati nella struttura e nel tema approvati, un capitolo alla volta e soltanto dopo il via previsto da [P2](MASTER_PROMPT.md#p2).
6. Verifica quanto descritto in [T8](riferimenti/REQUISITI_TECNICI.md#t8), aggiorna la versione degli HTML o la data dei documenti di regole e consegna i file richiesti.

Una fase completata e approvata diventa la base delle successive. Non riaprirla senza una nuova richiesta o un problema concreto. L’ordine non autorizza lavorazioni estranee alla richiesta né ulteriori approvazioni automatiche per ogni passaggio.

<a id="p5"></a>
## P5. Limiti della ricerca, riuso e approvazioni

La ricerca deve avere un limite breve e proporzionato al compito, nel tempo o nel numero di tentativi. Se può incidere sensibilmente sulla durata, dichiaralo nella stima e concordalo. Punta inizialmente a poche immagini pertinenti, indicativamente due o tre, evitando raccolte estese inutili. Quando il limite è raggiunto, presenta ciò che hai trovato o spiega che cosa manca; concorda come continuare invece di prolungare autonomamente una ricerca onerosa. Se non esiste un’immagine adatta utilizzabile, applica la richiesta di fornitura prevista in [T3](riferimenti/REQUISITI_TECNICI.md#t3).

Prima di cercare, ridisegnare, tradurre o programmare, verifica se esiste un materiale già approvato riutilizzabile. Riusa immagini, grafica, schemi, formule, traduzioni e simulazioni quando sono coerenti con la richiesta e scientificamente corretti, rispettando il divieto di ripetere la copertina nel testo dello stesso capitolo previsto in [S3](riferimenti/CONTENUTI_E_STILE.md#s3). Non rigenerare immagini, ripetere traduzioni o riscrivere componenti soltanto per uniformarli a un nuovo metodo di lavoro.

Conserva un registro essenziale dei materiali approvati insieme ai file di lavoro: identificativo, soggetto, originale, eventuale versione modificata, fonte, autore, licenza, modifica eseguita, lingua e stato dell’approvazione. Aggiornalo quando serve senza produrre nuovi inventari a ogni piccola revisione. La dispensa finale deve comunque incorporare i materiali necessari e restare autonoma.

L’approvazione di una scelta resta valida. Gli originali forniti o già approvati non richiedono una nuova scelta, salvo cambiamenti sostanziali. Una traduzione di etichette, un ritaglio o un’altra modifica espressamente richiesta dall’utente è già autorizzata entro i limiti indicati: non chiedere nuovamente il permesso di eseguirla. Mostra e fai accettare il risultato secondo [P2](MASTER_PROMPT.md#p2) prima di inserirlo nell’HTML, segnalando eventuali effetti sulla comprensione. Per nuove immagini non ancora scelte, la ricerca o il comando generico di sostituzione non equivalgono all’approvazione di una proposta specifica.

<a id="p6"></a>
## P6. Modifiche circoscritte e aggiornamenti

Conserva testo, formule, dati, immagini, attività e stile che non sono coinvolti nella richiesta. Non cambiare il modello fisico per correggere solo l’aspetto di una simulazione. Se trovi un problema che richiede interventi più ampi, segnalalo e distinguilo dalla modifica richiesta.

Evita operazioni ripetute senza motivo: recuperi dello stesso file ancora corrente, ricerche già concluse, copie intermedie non utili, render e verifiche identici dopo controlli già superati. Conserva risultati e materiali intermedi riutilizzabili durante il lavoro. Il risparmio non deve eliminare controlli necessari né ridurre la qualità scientifica o la leggibilità.

Durante il lavoro comunica avvio, fasi principali concluse e verifiche in corso con aggiornamenti brevi e concreti. Non lasciare passare più di circa 60 secondi senza un aggiornamento per lavori lunghi. Per un lavoro breve bastano avvio e consegna. Al termine indica i file e il salvataggio Git; per gli HTML riporta anche la versione, spiegando in una frase il cambiamento principale. Se rilevi che il contesto diventa problematico per conservare istruzioni, decisioni o dettagli del lavoro, avvisa esplicitamente l’utente: «Il contesto sta diventando problematico: salvo lo stato del lavoro per poter proseguire senza perdere le decisioni approvate». Non dichiarare percentuali o token residui non misurabili e non garantire di anticipare ogni compattazione automatica. Salva lo stato secondo [P7](MASTER_PROMPT.md#p7) prima di proseguire con lavorazioni estese; se necessario proponi una nuova chat dello stesso progetto. Non attendere questo avviso per effettuare i salvataggi ai passaggi principali.

<a id="p7"></a>
## P7. Continuità e stato di lavoro

Usa preferibilmente una chat per capitolo. Prima di un nuovo lavoro leggi integralmente il master corrente, lo stato pertinente e i documenti necessari indicati in [AGENTS.md](AGENTS.md). Leggi in blocchi controllati, verificando copertura e assenza di troncamenti; se una lettura è troncata, recupera le parti mancanti. Ricava una checklist essenziale senza sostituire le fonti ufficiali. Conserva nel contesto soltanto le informazioni utili e recupera dai file i dettagli quando servono.

Per ciascun capitolo, quando ne inizia la progettazione, crea o riutilizza un unico file Markdown di stato con nome stabile `lavorazione/<capitolo>/stato.md`, nella cartella definita in [P9](MASTER_PROMPT.md#p9). Mantieni uno stato corrente sintetico, non un diario cumulativo; la cronologia dettagliata resta in Git. Registra: argomento e confini; fase corrente e ultimo aggiornamento; fonti consultate e checklist pertinente; data o identificativo Git di una regola soltanto quando serve a comprendere una decisione; domanda iniziale e template approvato; visuali con identificativi, funzione, collegamenti ai file e scelte approvate; simulazioni con modello, comandi, fattibilità, carico di calcolo e stime; bozza corrente con segnaposto; approvazioni effettivamente ricevute; lavoro completato, punti aperti e prossima operazione. Non attribuire all’utente approvazioni soltanto dedotte e non creare documenti vuoti prima che sia individuato un capitolo.

Aggiorna il documento nei passaggi decisivi: visuali concordate, bozza approvata, via alla realizzazione e conclusione, oltre che prima di un cambio di chat o quando emerge un problema di contesto. Non trascrivere ogni messaggio e non creare inventari o copie superflui. Durante la realizzazione salva anche l’HTML in lavorazione e le risorse necessarie a riprendere, in `lavorazione/<capitolo>/`, con bozza testuale in `bozza.md`, HTML corrente in `bozza.html` e risorse in `risorse/`, chiaramente distinti dalla versione ufficiale. Crea questi file soltanto quando esistono contenuti da conservare; mantieni i nomi stabili e affida le revisioni a Git. Salva dopo blocchi significativi di lavoro senza attendere la fine del capitolo. Un file incompleto non sostituisce mai l’HTML ufficiale verificato.

Alla ripresa recupera il master corrente, il documento di lavorazione e i file pertinenti, senza affidarti alla sola memoria della chat. Se una fonte pertinente è cambiata, controlla le differenze applicabili al lavoro; segnala incompatibilità che incidano su decisioni approvate. Riprendi dal prossimo passaggio registrato e conserva ciò che è già approvato. Per una nuova chat prepara un riepilogo essenziale con collegamenti, capitolo, fase, approvazioni e punti aperti. Verifica i salvataggi; se falliscono, dichiaralo e non presentare lo stato come conservato.

<a id="p8"></a>
## P8. Anteprime originali e scelta delle immagini

Prima di cercare o generare una nuova immagine per la dispensa, indica all’utente esattamente quali immagini servono e lascia che le cerchi e le fornisca personalmente. Non avviare autonomamente ricerche alternative né generazioni. Solo se l’utente comunica di non aver trovato una specifica immagine, concorda con lui se effettuare una ricerca sul web oppure generarla; genera soltanto su sua esplicita richiesta. Conserva priorità e fedeltà dei materiali forniti dall’utente. Per le immagini cercate sul web si applica la successiva procedura di anteprima e approvazione.

Per ogni immagine nuova cercata sul web, mostra un set distinto di alternative pertinenti e chiedi all’utente di scegliere una proposta o di fornire una propria immagine. Puoi raggruppare nella stessa richiesta più set, ma la scelta deve essere esplicita per ciascuna immagine. Identifica ogni proposta con numero e breve descrizione. Mostra sempre i file originali scaricati dal web, senza ritagli, rimozione dello sfondo, ricostruzioni o altre modifiche, e fornisci collegamenti per aprire o scaricare ogni originale. Non sostituire queste anteprime con versioni elaborate o generate.

Chiedi se le proposte vanno bene e attendi l’approvazione prima di aggiungerle alla dispensa o sostituire immagini esistenti. Un comando generico di cercare o cambiare immagine non approva la scelta specifica. Se mostri anche una versione modificata, affiancala al suo originale e distingui chiaramente le due.

Per le modifiche segui la fase separata di [P2](MASTER_PROMPT.md#p2) e la distinzione di [P5](MASTER_PROMPT.md#p5) tra autorizzazione a eseguire e accettazione del risultato. Mostra la versione modificata insieme all’originale, senza ripetere una scelta già approvata.

<a id="p9"></a>
## P9. Repository ufficiale e salvataggi

GitHub è la fonte ufficiale del progetto «Materiale Didattico»: repository https://github.com/rickymusu-bit/fisica, ramo di riferimento `main`. Lavora in un ramo dedicato derivato da `main`; verifica lo stato corrente del repository prima di modificare i file. Il master è `MASTER_PROMPT.md`; `AGENTS.md` impone la lettura del master e dello stato del capitolo prima di lavorare. La migrazione e il salvataggio nel ramo dedicato non equivalgono all’approvazione dei contenuti, all’unione nel ramo di riferimento o alla pubblicazione del sito.

Usa i nomi stabili e applica le regole sui collegamenti già pubblicati previste in [T7](riferimenti/REQUISITI_TECNICI.md#t7) quando cambia un percorso. Le dispense restano HTML autonomi; le traduzioni richieste restano distinte per lingua. Conserva nella destinazione ufficiale soltanto i risultati pertinenti al compito; non trasferire automaticamente nei lavori futuri dispense storiche o materiali estranei. Il quiz e i relativi materiali sono conservati separatamente nel repository https://github.com/rickymusu-bit/quiz; non fanno parte del sito delle dispense di fisica. Non convertire automaticamente le dispense in altri formati.

In `lavorazione/<capitolo>/stato.md` conserva un solo stato Markdown per capitolo, secondo [P7](MASTER_PROMPT.md#p7). Usa nomi stabili anche per `bozza.md`, `bozza.html` e `risorse/`; gli originali e i materiali di riferimento necessari alla ripresa appartengono alla lavorazione e non vanno aggiunti automaticamente alla destinazione degli HTML ufficiali. Aggiorna gli stessi file senza proliferare copie; Git conserva la cronologia. Non eliminare materiali unici o originali dell’utente e non inventare approvazioni mancanti.

Prima di una revisione verifica identità, contenuto e versione del file nel repository, perché l’utente può averlo aggiornato. Importa da fonti esterne soltanto materiali mancanti o effettivamente più recenti, confrontando contenuto, versione e provenienza; una sola data di modifica non risolve identità ambigue. Non sovrascrivere contenuti di identità incerta: conserva il file corrente e segnala il conflitto. Dopo la scrittura verifica percorso, nome, integrità e riuscita del salvataggio; registra le modifiche in Git e verifica l’eventuale caricamento remoto. La cronologia sostituisce le copie storiche di master e stati; le regole di versione interna degli HTML, data di aggiornamento dei documenti e approvazione restano valide.

Alla consegna fornisci il collegamento al ramo, al commit o ai file GitHub effettivamente salvati e verificati. Se il caricamento remoto fallisce, dichiaralo e fornisci il lavoro pronto, senza presentarlo come caricato. Non cambiare destinazione per aggirare un errore di accesso. Le fonti Drive della migrazione sono il master https://docs.google.com/document/d/1EA-rZut3LOfWJYeTZ3DQ0uArP8NNyTUZFOY4UgQGJBg/edit, i materiali https://drive.google.com/drive/folders/1ZbpsRZnrZCda3ZC1z54WId5qcsIL1TRE e la lavorazione https://drive.google.com/drive/folders/1LWZM2idyl7U89g1PvF4xcppsTQkyuhU_. Conserva questi materiali su Drive senza eliminarli. Non attivare né modificare la pubblicazione del sito durante la migrazione.

<a id="p10"></a>
## P10. Fonti ufficiali, manutenzione e cronologia

Ogni regola ha una sola collocazione ufficiale nella tabella iniziale. I quattro documenti sono complementari: ciascuno è autorevole per il proprio ambito. AGENTS indica che cosa leggere; gli esempi illustrano le regole; gli stati registrano fatti e approvazioni, senza introdurre norme generali.

In caso di conflitto con memorie, preferenze ricordate o conversazioni precedenti, valgono i documenti correnti nel rispettivo ambito. Le richieste esplicite dell’utente precisano scopo ed eccezioni del compito, senza estenderle ad altri lavori. Se due documenti correnti sono in conflitto, segnala la contraddizione e le alternative prima di risolverla; non scegliere in base alla data o a una presunta prevalenza universale del master.

Quando aggiungi o cambi una regola, aggiorna soltanto la sua sede ufficiale e i rimandi interessati. Conserva i vincoli non modificati dall’utente, evita copie della stessa prescrizione e aggiorna la data del documento interessato.

Il master ufficiale è `MASTER_PROMPT.md` nel repository GitHub `rickymusu-bit/fisica`, con percorso stabile. Il Google Doc di origine resta fonte storica della migrazione. I quattro documenti delle regole non usano versioni numeriche: ciascuno riporta soltanto data e ora dell’ultimo aggiornamento nel fuso Europe/Rome. Git conserva la cronologia e identifica ogni revisione, inclusi refusi e ripristini; non mantenere contatori o copie numerate. Negli stati richiama data o identificativo Git di una regola solo quando serve a documentare una decisione. Le versioni numeriche restano per gli HTML consegnati, secondo i [requisiti di versione](riferimenti/REQUISITI_TECNICI.md#t7).

<a id="p11"></a>
## P11. Riordino periodico dei documenti

Riesamina periodicamente i quattro documenti, soprattutto dopo aggiornamenti ampi, per individuare duplicazioni, contraddizioni, regole obsolete, formulazioni prolisse e dipendenze tra istruzioni. Il controllo non dipende da un numero di versioni. Per un riordino strutturale presenta una sintesi delle criticità e delle modifiche previste e ottieni l’approvazione prima di procedere; riutilizza quella già ricevuta per il lavoro corrente. Conserva tutti i vincoli funzionali ancora validi e non cambiarne il significato senza autorizzazione specifica. Verifica che la nuova struttura non introduca omissioni, incoerenze o cambiamenti involontari nel comportamento. Aggiorna soltanto data e ora dei documenti interessati e salva le modifiche in Git. Se emergono contraddizioni, segnala le alternative e attendi l’approvazione prima di risolverle; non scegliere autonomamente quale regola prevalga. Esegui un riordino completo soltanto su richiesta o in presenza di problemi strutturali rilevanti, seguendo queste approvazioni.

<a id="p12"></a>
## P12. Consegna e proporzione del lavoro

Alla consegna mostra soltanto i collegamenti alle versioni più recenti prodotte per il compito e riporta in una frase il cambiamento principale. Consegna solo i formati richiesti; i file di lavoro ausiliari non sono nuovi risultati da inviare automaticamente.

Applica soltanto le procedure pertinenti al lavoro richiesto. Preferisci una buona immagine accompagnata da testo breve e preciso quando è più chiara di una spiegazione lunga, senza ridurre la comprensibilità. Il percorso dello studente resta: osservare → chiedersi perché → leggere → interpretare → ragionare.
