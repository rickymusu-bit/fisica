# Tema grafico e interfaccia

Aggiornamento: 17 ottobre 2026, ore 14:07 (Europe/Rome).

Fonte ufficiale per aspetto e comportamento della pagina, comune alla home e ai capitoli. Conserva il riferimento grafico e le scelte di interfaccia approvati. Contenuti: [contenuti e stile](CONTENUTI_E_STILE.md). Realizzazione tecnica: [requisiti tecnici](REQUISITI_TECNICI.md). Procedura e approvazioni: [master](../MASTER_PROMPT.md).

<a id="g1"></a>
## G1. Tema comune approvato

Tutti i capitoli e la home del sito condividono il riferimento grafico approvato dall’utente: **Mac Template**, https://mac-template.webflow.io/. Questa scelta vale per tutti i capitoli esistenti e futuri e per la home; non chiedere nuovamente quale template usare, salvo richiesta di cambiarlo o un problema concreto di accesso al riferimento. Riprendi palette, tipografia, bordi, ombre nette e richiami alle finestre del sito di riferimento, mantenendo coerenza per larghezza di lettura, titoli, formule, immagini, didascalie, tabelle e comandi. Adatta il tema alla lettura didattica e ai dispositivi: evita di trasformare ogni paragrafo in un riquadro e conserva i colori scientificamente significativi di immagini e grafici. La scelta del tema non attesta che gli HTML esistenti siano già adeguati; la loro realizzazione o revisione segue [P2](../MASTER_PROMPT.md#p2)–[P3](../MASTER_PROMPT.md#p3).

L’adattamento approvato è la [pagina dimostrativa v6](../lavorazione/tema_grafico/anteprima.html): Mac, Lexend, indice laterale nativo e collegamenti «← Biblioteca». La sua approvazione grafica è distinta da quella dei contenuti. Il tema vale per home e capitoli; la scelta non richiede dipendenze da Webflow, importazione delle immagini dimostrative o filtri in scala di grigi sulle visuali didattiche.

<a id="g2"></a>
## G2. Palette, cornici e composizione

Superfici prevalentemente bianche e grigie (#c4c4c4), testo e bordi neri, titoli grandi e marcati, contorni netti e ombre sfalsate. Il riferimento originale usa spesso bordi di 4 px e ombre di 8 px; l’adattamento corrente usa bordi di 2–4 px secondo l’elemento. Finestre con barra superiore e pulsanti rettangolari richiamano un’interfaccia desktop classica. Le composizioni a due colonne diventano verticali sui dispositivi piccoli.

Usa le cornici in modo selettivo, senza una finestra per ogni paragrafo. Mantieni colori e dettagli scientificamente significativi di fotografie, grafici e schemi. Per ordine del capitolo e distribuzione delle visuali applica [S3](CONTENUTI_E_STILE.md#s3). Per la home conserva catalogo, collegamenti di lettura e download.

<a id="g3"></a>
## G3. Tipografia e lettura

Per la tipografia comune a home e capitoli, l’utente richiede attenzione alla leggibilità per persone con dislessia: privilegia un carattere con lettere ben distinguibili, testo allineato a sinistra senza giustificazione, interlinea comoda e spaziature regolari. Adatta la tipografia del tema Mac a questo requisito e registra qui il carattere scelto, senza presentare un singolo font come soluzione universale.

Carattere corrente: **Lexend**, variabile, con alternativa sans-serif ([progetto ufficiale](https://www.lexend.com/), [font e licenza SIL OFL 1.1](https://github.com/google/fonts/tree/main/ofl/lexend)). Il carattere Baloo Thambi 2 del sito originale non sostituisce Lexend nell’adattamento approvato.

Testo a sinistra senza giustificazione, corpo di 21 px su desktop e 19 px su smartphone, interlinea 1,65, spaziatura regolare e larghezza di lettura confortevole. Titoli senza compressione della distanza fra le lettere; evita lunghi tratti in corsivo o maiuscolo. Incorporamento e licenza del font seguono [T1](REQUISITI_TECNICI.md#t1) e [T3](REQUISITI_TECNICI.md#t3).

<a id="g4"></a>
## G4. Indice laterale

L’indice interno dei capitoli è una barra laterale a scomparsa, come in un lettore PDF, al posto dell’indice iniziale nel corpo della pagina. Un pulsante «Indice» nell’intestazione, accessibile anche durante lo scorrimento, apre il pannello inizialmente chiuso; ogni capitolo o sottoparte ha un id e una voce cliccabile. Evidenzia la sezione corrente senza affidarti al solo colore. Su smartphone il pannello si sovrappone alla pagina per preservare lo spazio di lettura. Consenti chiusura esplicita, con Esc e selezionando una voce; gestisci correttamente focus e navigazione da tastiera. Puoi inserire altri richiami discreti all’indice laterale.

Il catalogo della home resta distinto dall’indice interno. L’apertura e la chiusura esplicita del pannello devono funzionare anche senza JavaScript: usa `details` e `summary` nativi. Gli script migliorano focus, sezione corrente, chiusura dopo la scelta, Esc e clic esterno; quando non sono eseguiti si naviga con i collegamenti e si chiude con «Chiudi». Non dipendere da `dialog.showModal()`. Verifica anche il tocco emulato con script disabilitati, oltre alla sola larghezza dello schermo.

<a id="g5"></a>
## G5. Biblioteca e navigazione tra capitoli

Ogni nuovo capitolo deve includere due tasti «← Biblioteca»: uno all’inizio del documento e uno alla fine del contenuto, prima del piè di pagina. Realizzali come collegamenti HTML all’indice generale `https://rickymusu-bit.github.io/fisica/#indice`, così sono utilizzabili anche dalle copie HTML scaricate quando è disponibile Internet. Mantieni lo stile approvato, un’area cliccabile alta almeno 44 px, il focus visibile e l’uso da tastiera.

Alla fine di ogni capitolo inserisci i collegamenti «Capitolo precedente» e «Capitolo successivo», con il titolo della destinazione, seguendo l’ordine della Biblioteca in `index.html`. Nel primo capitolo ometti il precedente; nell’ultimo ometti il successivo, senza pulsanti disabilitati né ritorni ciclici. Mantieni collegamenti HTML nativi, percorsi stabili, area cliccabile di almeno 44 px, focus visibile e disposizione leggibile su smartphone. Quando aggiungi o riordini capitoli, aggiorna anche i collegamenti dei capitoli vicini; conserva i due tasti «← Biblioteca».

<a id="g6"></a>
## G6. Immagini ingrandibili e adattamento agli schermi

Progetta fin dall’inizio per smartphone, tablet, notebook e desktop. Mantieni una larghezza di lettura confortevole su desktop e font sufficientemente grandi. Le immagini rispettano almeno max-width:100% e height:auto, senza deformazioni. Su smartphone generalmente usa una sola immagine per riga con didascalia vicina; su schermi grandi puoi affiancare immagini o confronti quando è utile.

Per le immagini con scritte o dettagli che richiedono una vista più grande, prevedi un comando di ingrandimento reversibile. Il testo deve indicare l’azione disponibile: «Ingrandisci l’immagine» nella vista normale e «Rimpicciolisci l’immagine» nella vista ingrandita, tornando al testo iniziale dopo la chiusura. In alternativa usa un’icona di ingrandimento che cambi in quella di rimpicciolimento, con nome accessibile aggiornato alla stessa azione. Il comando deve funzionare su smartphone, da tastiera e anche senza JavaScript, mantenendo leggibilità e proporzioni dell’immagine.

Tabelle, formule e grafici devono adattarsi o avere scorrimento orizzontale. Per gli elementi ricostruiti, preferisci prima una riorganizzazione leggibile: disposizione verticale, elementi impilati, legenda spostata, etichette abbreviate senza cambiare significato o maggiore altezza. Non limitarti a rimpicciolire una composizione desktop. Usa lo scorrimento quando non esiste una soluzione migliore; la leggibilità prevale sulla disposizione originale.

<a id="g7"></a>
## G7. Movimento e comandi multimediali

GIF. Non aggiungere mai pulsanti o altri comandi per fermare, mettere in pausa o riavviare le GIF. La regola vale per tutte le GIF nelle dispense e nelle anteprime; i comandi delle simulazioni interattive restano distinti.

Per video e simulazioni applica [T6](REQUISITI_TECNICI.md#t6); i comandi delle simulazioni restano distinti dalle GIF. Per accessibilità e verifiche applica [T2](REQUISITI_TECNICI.md#t2) e [T8](REQUISITI_TECNICI.md#t8).
