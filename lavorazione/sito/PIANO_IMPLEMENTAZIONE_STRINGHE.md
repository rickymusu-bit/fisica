# Stringhe — piano di implementazione per Codex

**Stato:** specifica approvata dall'utente per le funzionalità indicate; varianti grafiche dei bordi ancora da confrontare.
**Aggiornamento:** 20 ottobre 2026 — Italia (Europe/Rome).
**Repository:** `rickymusu-bit/fisica`.
**Ramo di lavoro attuale:** `design/stringhe-portale` (PR #43, bozza).
**Scopo di questo documento:** consegnare a Codex un elenco eseguibile di interventi sul portale, non richiedere la pubblicazione in `main`.

## Ambito globale del restyling — precisazione esplicita dell'utente

**Il nuovo stile NON riguarda soltanto la home.** Deve diventare il **tema grafico unico dell'intero sito Stringhe**: home, catalogo, pagina Quiz, pagine di servizio, **tutti gli articoli effettivamente pubblicati** e soprattutto il **modello sorgente comune per le dispense future** `riferimenti/TEMA_DISPENSE.html`. Questa richiesta sostituisce qualsiasi interpretazione del piano che limiti i cambiamenti a `index.html` o alle copie temporanee generate da `scripts/strings_site.py`.

- [ ] **Uniformare la grafica end-to-end**: palette grigio/gradiente blu/giallo luce, dark mode opzionale, reticolo tenue sullo sfondo esterno, sinusoidi decorative delle cornici, tipografia, spaziature, pulsanti, navigazione, dialog, pannelli laterali, note, credits e componenti condivisi, con variazioni appropriate tra pagine di lettura e pagine di navigazione.
- [ ] **Aggiornare il modello ufficiale `riferimenti/TEMA_DISPENSE.html`**: integrare token del tema, componenti visuali e comportamenti (incluso selettore chiaro/scuro/automatico), affinché Codex generi ogni nuovo articolo **già nello stile Stringhe**, senza doverlo trasformare successivamente durante la build.
- [ ] **Allineare il generatore `scripts/strings_site.py` al modello ufficiale**, evitando regole CSS e componenti in conflitto. Un articolo creato dal modello e la sua copia pubblicata devono avere la stessa identità visiva; mantenere intatti i contenuti scientifici e le risorse autonome/offline.
- [ ] **Applicare lo stile ai nove articoli attualmente ammessi** in `pubblicazione.json`, modificandone il tema nelle copie pubblicate o in modo controllato nei sorgenti ammessi, senza alterare testo, immagini, formule, simulazioni o struttura scientifica. Verificare ogni pagina su Android e desktop.
- [ ] **Esclusioni invariabili**: il restyling generale **NON autorizza** a toccare i file degli articoli sospesi né a pubblicarli. Per essi nessuna modifica automatica; saranno aggiornati solo dopo autorizzazione specifica quando verranno ripresi.
- [ ] **Decorazioni appropriate al contesto**: sulle pagine degli articoli usare il reticolo sullo sfondo esterno alle superfici di lettura, curve sui bordi di contenitori selezionati, senza mettere motivi sotto i paragrafi o interferire con formule/visuali. Dark mode completa anche per indice, note, ingrandimenti, navigazione tra articoli, crediti e download.
- [ ] **Aggiornare la documentazione e le regole operative** (`AGENTS.md`, `MASTER_PROMPT.md` se pertinente, `riferimenti/TERMINOLOGIA_SITO.md`, stato sito), eliminando conflitti tra «Materia Oscura» e «Stringhe» per il lavoro futuro. Conservare cronologia e precedenti approvazioni di contenuto; non riscrivere il master per iniziativa non pertinente.
- [ ] **Criterio di completamento**: non basta una home riuscita. Il lavoro sarà pronto per la revisione soltanto quando home, catalogo, Quiz, una rappresentanza delle pagine di servizio, **tutti i nove articoli pubblicabili** e il **modello ufficiale** saranno stilisticamente coerenti in light/dark mode, verificati su mobile/desktop e con build senza errori.

## Regole preliminari e ambito

- Prima di intervenire leggere `AGENTS.md`, `MASTER_PROMPT.md`, `pubblicazione.json`, `riferimenti/TERMINOLOGIA_SITO.md`, `identita/README.md` e `lavorazione/sito/stato.md`.
- Il nome ufficiale **Stringhe** e il sottotitolo esatto **L’essenziale della Fisica** sostituiscono le precedenti denominazioni del sito, nei soli elementi pertinenti all'identità e alla navigazione. Non riscrivere i contenuti didattici.
- La richiesta attuale dell'utente corregge la proposta iniziale del portale: **conservare il logo circolare animato originale e la copertina fotografica casuale**. Non sostituire il logo con onde lineari. I quattro pulsanti della nuova home sono già approvati.
- Gli articoli sospesi in `pubblicazione.json` non devono essere modificati, generati, linkati, reintrodotti o pubblicati. Non alterare i reindirizzamenti dismessi, l'ordine didattico e le licenze.
- Usare nomi di file stabili; Git conserva la cronologia. Conservare le dispense come HTML autonomi, con risorse incorporate e funzionamento offline dove previsto. Le modifiche di navigazione/tema possono essere applicate **alle sole copie di pubblicazione** mediante il generatore, evitando di riscrivere automaticamente gli HTML sorgenti.
- Sviluppare su branch dedicato e mantenere la PR in bozza fino a verifica e approvazione. **Non unire in `main`, non attivare un deployment pubblico** e non modificare il repository separato `rickymusu-bit/quiz` senza richiesta specifica.
- Centralizzare per quanto possibile identità, navigazione, temi e palette in `scripts/strings_site.py` e nei componenti comuni appropriati; evitare una seconda implementazione indipendente tra home e articoli.

## P0 — Identità visiva della home: ripristini obbligatori

- [ ] **P0.1 Ripristinare il logo approvato.** Nella home affiancare al titolo «Stringhe» l'onda circolare/corda chiusa **animata a quattro creste** già approvata. Riutilizzare **esattamente** `identita/logo-materia-oscura.svg`, con la GIF già esistente solo dove necessaria, e il controllo di pausa/ripresa di `identita/controlli-logo.js` o equivalente già verificato. Mantenere dimensione e posizionamento responsive e `prefers-reduced-motion`. Il nome storico nel percorso del file è un dettaglio interno: evitare rinominazioni che spezzino riferimenti. Non cambiare geometria, ampiezza, nodi o periodo dell'animazione.
- [ ] **P0.2 Mantenere il logo anche negli articoli.** Nella barra dei soli articoli pubblicabili conservare il componente circolare esistente, senza rimpiazzarlo con l'icona lineare provvisoria; verificare pausa/ripresa, controlli tastiera e accessibilità.
- [ ] **P0.3 Ripristinare la copertina fotografica variabile.** Usare le **20 fotografie già approvate** in `copertine/manifest.json`, scegliendone una casualmente all'apertura della home, con testo alternativo e didascalia corrispondenti. Conservare proporzioni e immagine intera: niente ritagli, distorsioni, scritte sovrapposte, immagini nuove o duplicazioni arbitrarie. Mantenere un fallback statico senza JS e tutti gli obblighi di attribuzione già registrati.
- [ ] **P0.4 Conservare i quattro accessi della home:** «Tutti gli articoli», «Mi sento fortunato», «Quiz», «Lingua». Restano le destinazioni e le funzioni concordate: catalogo separato e cercabile, scelta casuale esclusivamente tra articoli ammessi, pagina quiz preparatoria, selezione linguistica limitata alle lingue effettivamente pubblicate. Attualmente l'unica lingua pubblicata è l'italiano.
- [ ] **P0.5 Contenere la decorazione.** Le sinusoidi sui bordi non devono oscurare il logo circolare o entrare in competizione con la fotografia. Gerarchia di attenzione: titolo/logo, copertina, pulsanti, contenuti.

## P1 — Bordi sinusoidali: creare e confrontare due varianti

Realizzare una **pagina di confronto** `lavorazione/sito/anteprima-bordi-stringhe.html` (oppure un'anteprima equivalente nel ramo di sviluppo), accessibile sul browser e su Android. Deve mostrare **le stesse card e finestre**, con un controllo per commutare variante A/B e tema chiaro/scuro; le modifiche della dimostrazione non devono cambiare i contenuti. Non scegliere autonomamente una variante definitiva prima della valutazione dell'utente.

- [ ] **P1.1 Variante A — opposizione di fase, ampiezze uguali.** Due curve sinusoidali visibili e indipendenti, stesso periodo spaziale, centrate attorno allo stesso asse, con sfasamento `π` (180°), ampiezze `A₁ = A₂`. Esempio per il disegno: `y₁(x) = A sin(kx)`, `y₂(x) = -A sin(kx)`.
- [ ] **P1.2 Variante B — opposizione di fase, ampiezze diverse.** Stesso periodo e sfasamento `π`, ma `A₁ ≠ A₂`; per una prima comparazione proporre ad esempio `A₂ = 0,6 A₁`, mantenendo le due curve riconoscibili.
- [ ] **P1.3 Precisazione scientifica e grafica.** Le due curve devono essere **tracciate separatamente**, ad esempio con tonalità/trasparenze distinguibili, non visualizzate come risultante matematica. Infatti per ampiezze uguali la loro somma è nulla; per ampiezze diverse la somma è una sola sinusoide residua. Evitare di definire queste semplici coppie di curve «onde stazionarie» senza le necessarie condizioni fisiche.
- [ ] **P1.4 Testare il posizionamento:** (a) bordo superiore e inferiore della card con fianchi semplici; (b) solo bordo superiore. È possibile mostrare anche un campione con cornice completa molto tenue, ma le varianti A/B sulle due curve restano la priorità. La decorazione deve adattarsi alla larghezza delle card senza tagli bruschi degli estremi, deformazioni della sinusoide o overflow orizzontale. Preferire SVG e CSS condivisi anziché immagini raster. Non cambiare la struttura delle figure scientifiche.
- [ ] **P1.5 Applicazione selettiva.** Provare il motivo sulla hero, sui quattro pulsanti, sulle card del catalogo e sui box in evidenza. Valutare il risultato su schermi piccoli e grandi: non imporre automaticamente onde evidenti a tutte le finestre, ai grafici, ai sistemi di equazioni o alle figure.
- [ ] **P1.6 Accessibilità e prestazioni.** Elementi decorativi con `aria-hidden="true"`, nessun elemento che intercetti clic, focus o selezione del testo; contrasto adatto ai due temi, spessore leggibile su schermi ad alta densità, nessuna animazione continua dei bordi richiesta. Se si anima un dettaglio, prevedere `prefers-reduced-motion`.
- [ ] **P1.7 Decisione grafica.** Preparare screenshot mobile e desktop di entrambe le varianti nello stesso contesto, sia con tema chiaro sia con tema scuro. Registrare pro e contro e chiedere all'utente quale preferisce prima di fissare la scelta su tutto il sito.

## P2 — Dark mode opzionale, completa e persistente

- [ ] **P2.1 Aggiungere un controllo riconoscibile** nella navigazione del sito per scegliere **Automatico / Chiaro / Scuro**; su mobile usare un menu/tasto compatto. Non sostituire né eliminare i quattro pulsanti della home. Il controllo deve essere usabile da tastiera e avere etichetta accessibile.
- [ ] **P2.2 Default Automatico:** seguire `prefers-color-scheme` finché l'utente non seleziona esplicitamente chiaro o scuro. Consentire in ogni momento il ritorno ad Automatico.
- [ ] **P2.3 Preferenza persistente:** salvare l'override manuale in `localStorage` quando disponibile; gestire senza errori ambienti in cui lo storage è bloccato, incluso l'uso offline. Propagare la preferenza tra home, catalogo, quiz e articoli; non dipendere da cookie, account, backend o reti esterne.
- [ ] **P2.4 Applicare il tema prima del primo rendering**, per limitare il lampo della palette sbagliata. In modalità Automatico seguire anche i cambiamenti di preferenza del sistema durante la sessione. Senza JavaScript, il sito deve restare leggibile e rispettare il tema di sistema tramite CSS.
- [ ] **P2.5 Palette tramite variabili CSS condivise** (sfondo, superfici, testo, link, bordi, evidenziazioni, ombre, componenti, onde). La dark mode deve usare superfici scure non abbaglianti e colori delle sinusoidi abbastanza distinti, senza impiegare inversioni globali dell'HTML.
- [ ] **P2.6 Preservare scientificamente immagini, grafici e formule:** non invertire fotografie, diagrammi, scale cromatiche o termografie; assicurare che formule, etichette, tabelle e simulazioni siano leggibili. Se necessario mettere immagini con scritte scure su superfici chiare dedicate. L'SVG del logo esistente ha tratto nero: garantirne il contrasto anche in scuro senza modificarne la forma o interrompere l'animazione.
- [ ] **P2.7 Uniformità:** verificare home, `articoli.html`, `quiz.html`, tutte le copie di articoli pubblicabili, indice dell'articolo, menu lingua, pulsanti download, note collassabili, finestre di zoom e crediti. Il selettore lingua non deve promettere versioni non pubblicate.
- [ ] **P2.8 Confronti:** verificare le due varianti di bordo in entrambi i temi; stati hover/focus/active; contrasto indicativamente WCAG AA (testo normale almeno 4,5:1, ove applicabile); apertura da browser Android e desktop.

## Palette approvata e gerarchia dei pulsanti — aggiornamento del 20 ottobre 2026

**Decisione cromatica esplicita dell'utente.** Questa sezione precisa P1 e P2 e prevale sulle precedenti proposte cromatiche provvisorie.

- **Sfondo:** grigio chiaro neutro in modalità chiara (riferimento iniziale `#EDEDED`); grigio antracite in modalità scura, non nero assoluto. Le superfici delle finestre/card devono rimanere distinguibili dallo sfondo generale.
- **Gradiente blu = accento di tutto il sito:** passaggio azzurro → blu → indaco. Palette di partenza da verificare visivamente: `#83D4FA` → `#337CD8` → `#4140A3`. In dark mode possono essere usate varianti più luminose per il necessario contrasto. Definire token CSS riutilizzabili; evitare sfumature incoerenti tra componenti.
- **Bordi decorativi sinusoidali:** in entrambe le varianti A/B già previste, tracciare separatamente **una curva col gradiente blu** e **una curva monocromatica**: nera (o quasi nera) in light mode e bianca (o quasi bianca) in dark mode. Conservare opposizione di fase e differenze di ampiezza definite in P1. Non sommarle numericamente.
- **Pulsante principale «Tutti gli articoli»:** riempimento **giallo luce caldo `#FFD84D`** e testo/icona quasi neri (`#202637`). Il giallo richiama la luce e separa visivamente l'azione primaria dagli accenti blu. **Non usare uno sfondo blu dietro la linea in gradiente blu:** la decorazione perderebbe leggibilità. Non utilizzare testo bianco su fondo giallo né giallo puro `#FFFF00`.
- **Altri tre pulsanti:** «Mi sento fortunato», «Quiz», «Lingua» con superfici neutre (chiare in light mode, scure in dark mode), testi ad alto contrasto e **un piccolo dettaglio comune in gradiente blu** (per esempio linea/sinusoide inferiore). Non colorare stabilmente tutti e quattro i pulsanti con il gradiente.
- **Interazioni:** usare accenti blu per hover, focus e stato selezionato, ma garantire che siano comprensibili anche **senza hover su dispositivi touch Android**. Evidenziare sempre chiaramente lo stato di focus da tastiera. Il gradiente non deve essere l'unico mezzo di comunicazione dello stato.
- **Altri usi del gradiente blu, con moderazione:** sottolineature dei titoli di sezione, barra sottile sotto la navigazione, indicatori di selezione, bordi di card evidenziate e future barre di avanzamento nei quiz. Non applicare gradienti alle intere superfici di lettura, al testo corrente, alle formule o ai grafici scientifici. Conservare **«Stringhe» e il logo circolare** monocromatici, assicurando contrasto nella dark mode.
- **Dark mode:** mantenere il pulsante principale giallo (eventualmente una tonalità leggermente meno brillante se la verifica visiva lo richiede) con testo scuro; la sinusoide monocromatica diventa chiara, quella blu può schiarirsi. Sfondi scuri grigi e superfici differenziate; mai applicare inversione globale a fotografie, visuali scientifici o elementi grafici.
- **Criteri di accettazione:** screenshot light/dark della home e di almeno una card articolo, verifica del contrasto del testo sul giallo e delle sinusoidi sui fondi, resa su Android e desktop. Se il gradiente blu risulta poco visibile sul giallo, correggere spessore/valori di blu della sola linea decorativa senza rinunciare al giallo approvato.

**Regola compositiva:** grigio per la struttura, nero/bianco per la leggibilità, gradiente blu per l'identità grafica e giallo luce per l'azione principale. Non sostituire il logo circolare animato originale o la copertina fotografica variabile.

## P2-bis — Reticolo spazio-temporale leggero sullo sfondo (da confrontare)

**Decisione dell'utente:** aggiungere al tema di Stringhe un **reticolo leggero a maglie larghe**, ispirato ai sistemi di riferimento spazio-temporali. È una decorazione astratta, **non un diagramma di Minkowski scientifico**: non etichettare assi, coni di luce o coordinate e non suggerire proprietà fisiche che il disegno non rappresenta.

- [ ] **Variante A:** reticolo ortogonale semplice con linee sottili e maglie ampie (valore iniziale indicativo: 70–110 px su desktop; adeguare a mobile). Colore grigio leggermente distinto dallo sfondo, con contrasto molto basso.
- [ ] **Variante B:** stesso reticolo ma con accenno molto lieve di prospettiva/deformazione geometrica, senza prospettive vistose, distorsioni scientificamente fuorvianti, rumore visivo o perdita di regolarità. Preferire una curvatura controllata in SVG, senza animazioni.
- [ ] **Posizionamento:** applicare il reticolo **solo sullo sfondo generale** e nelle zone vuote intorno alle card. I pannelli di lettura, i testi lunghi, le formule, le figure, le fotografie e le schede dense devono mantenere superfici uniformi e opache; non sovrapporre linee ai contenuti.
- [ ] **Light mode:** base grigio chiaro come da palette approvata (riferimento `#EDEDED`) e tracciato appena più scuro.
- [ ] **Dark mode:** base grigio antracite, tracciato tenue appena più chiaro; non usare griglie bianche brillanti.
- [ ] **Gerarchia:** il reticolo resta l'elemento meno evidente. Priorità percettiva: logo circolare/titolo, fotografia variabile, pulsante principale giallo, pulsanti secondari, sinusoidi blu + nero/bianco, infine reticolo.
- [ ] **Implementazione:** CSS con due `linear-gradient` per la griglia ortogonale oppure SVG condiviso per la variante lievemente deformata; nessuna risorsa di rete o raster pesante, `pointer-events:none` per eventuali layer decorativi. Gestire viewport e scroll senza cuciture, moiré o overflow; in mobile attenuare l'intensità se necessario.
- [ ] **Confronto:** aggiungere le varianti reticolo A/B all'anteprima del tema, indipendenti dalle varianti A/B delle sinusoidi. Mostrare almeno: reticolo ortogonale/reticolo lieve deformazione, light/dark, smartphone/desktop e screenshot con testi lunghi. Se la griglia compete con leggibilità o decorazioni, ridurne il contrasto anziché sovrapporla alle card.
- [ ] **Approvazione:** non considerare selezionata una variante definitiva prima del confronto visivo con l'utente. Non cambiare `main` né pubblicare il sito durante questa fase.

## P3 — Chiarezza della funzione Quiz

- [ ] **P3.1 Correggere la presentazione di `quiz.html`.** «Quiz» significa **futuro generatore di quiz di verifica** per il singolo utente, con scelta degli argomenti da verificare. Testo provvisorio consigliato: «In futuro potrai generare quiz di verifica scegliendo gli argomenti su cui esercitarti.»
- [ ] **P3.2 Non integrare né menzionare come parte della funzione** «Chi vuol essere rimandato»: è **un progetto autonomo**, con repository `rickymusu-bit/quiz`, non il generatore del sito.
- [ ] **P3.3 Per questa iterazione realizzare solo la pagina di presentazione** del generatore futuro. Non inventare dataset, produzione automatica di domande, valutazioni, account o interfacce funzionanti non richieste. In una fase successiva si potrà progettare la selezione degli argomenti, delle domande e della difficoltà.

## P4 — Navigazione, funzionamento offline e architettura

- [ ] **P4.1 Conservare la navigazione concordata:** home, catalogo ricercabile e filtrabile, «Mi sento fortunato», quiz futuro, selettore lingua, più barra Home / Articoli / Scarica / Lingua e indice interno in ogni articolo.
- [ ] **P4.2 Correggere i collegamenti dell'anteprima** affinché la navigazione dall'articolo resti nel ramo `stringhe-preview` e non rientri erroneamente nel sito ufficiale. Preferire URL relativi quando appropriato, mantenendo i download HTML offline. Non spezzare gli URL già pubblicati.
- [ ] **P4.3 Consentire il download del documento HTML effettivamente navigabile**, verificandone autonomia e integrità in `file://`. La selezione tema su pagine scaricate deve degradare correttamente quando lo storage non è disponibile.
- [ ] **P4.4 Per la scelta casuale usare esclusivamente i file ammessi in `pubblicazione.json`;** il catalogo deve riflettere lo stesso insieme senza duplicati. Non generare collegamenti a file sospesi, traduzioni non pubblicate o vecchie dispense unificate.
- [ ] **P4.5 Mantenere font, licenze e crediti** secondo le regole già attive; non aggiungere dipendenze CDN per tema, logo, sinusoidi o font. Conservare la performance mobile e il comportamento con JS ridotto/non disponibile.
- [ ] **P4.6 Rendere le componenti condivise** per evitare divergenze tra `index.html`, `scripts/strings_site.py`, `riferimenti/TEMA_DISPENSE.html` e gli HTML futuri. Non applicare migrazioni massive non approvate agli articoli esclusi.

## P5 — Verifiche e consegna

- [ ] **P5.1 Eseguire** `python3 scripts/credits.py --check`, `python3 scripts/build_pages.py` e la suite pertinente di GitHub Actions; correggere gli errori senza rimuovere le verifiche o aggirare il manifest.
- [ ] **P5.2 Verificare su viewport** 320, 390, 768, 1024 e 1440 px: leggibilità, niente overflow orizzontale, logo e copertina visibili, didascalie corrette, pulsanti cliccabili, catalogo cercabile, barra articolo non sovrapposta, sinusoidi senza clipping.
- [ ] **P5.3 Verificare i tre temi** con e senza preferenza salvata, cambio di preferenza del sistema, navigazione tra pagine, aggiornamento della pagina, fallback senza JavaScript, `prefers-reduced-motion`, contrasto e navigazione da tastiera.
- [ ] **P5.4 Verificare la copertina random** su tutte le 20 possibilità, il fallback senza JS, l'accessibilità del logo e il suo toggle di pausa/ripresa.
- [ ] **P5.5 Verificare l'isolamento delle dispense:** nessuna alterazione dei contenuti scientifici, nessun sorgente escluso modificato, nessun nuovo HTML escluso pubblicato. Nella PR descrivere precisamente i file di origine e i file generati.
- [ ] **P5.6 Preparare un'anteprima visitabile da Android**, aggiornando il ramo `stringhe-preview` tramite il workflow dedicato; mostrare due varianti A/B e modalità chiaro/scuro. Considerare la cache del servizio di anteprima, con link a commit specifico quando necessario.
- [ ] **P5.7 Consegnare a revisione** una PR in bozza, screenshot delle due opzioni, esito dei test e limiti residui; **chiedere approvazione per la variante di bordo e per la pubblicazione**, senza fare merge autonomo.

## Ordine raccomandato per Codex

1. P0: ripristino logo circolare e copertina a rotazione, senza perdere i quattro pulsanti.
2. P3: rettifica del significato della sezione Quiz.
3. P1: prototipi affiancati A/B dei bordi sinusoidali.
4. P2: tema chiaro/scuro/automatico applicato anche ai prototipi.
5. P4: uniformazione navigazione e anteprima mobile/offline.
6. Applicare il tema scelto in `riferimenti/TEMA_DISPENSE.html` e a tutte le pagine e articoli pubblicabili; verificare che i nuovi articoli ereditino il tema.\n7. P5: test, schermate comparative e presentazione all'utente.
8. Solo dopo scelta esplicita dell'utente: adottare la variante definitiva e proporre l'integrazione in `main`.

**Definizione di completato per questa fase:** anteprima funzionante con logo originale, foto casuale e pulsanti conservati; due varianti di bordi effettivamente confrontabili in chiaro/scuro; tema opzionale persistente; Quiz presentato correttamente come futura funzione distinta; test superati. La pubblicazione in `main` non fa parte di questa fase.
