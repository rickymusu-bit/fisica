# Stato — Passaggi di stato

## Nuovo ordine degli articoli — 18 ottobre 2026

Versione v20: aggiornata esclusivamente la navigazione al nuovo ordine Stati della materia → Passaggi di stato → Conduzione → Convezione → Irraggiamento. Testi, media, formule e script invariati. Modifica richiesta nella conversazione; verifiche condivise in [verifica-ordine-crediti.json](../sito/verifica-ordine-crediti.json). Pubblicazione in preparazione.

## Schema triangolare invariato su mobile — 18 ottobre 2026

**Pubblicato e verificato:** PR #30, merge `30e83a396a2a0accec04c03890d9dfec3cdfc252`, workflow Pages `39115320280` riuscito; home e Passaggi di stato HTTP 200 e identici byte per byte alla build verificata. Nessuna pubblicazione pendente.

Anteprima HTML interattiva e vista mobile consegnate prima della pubblicazione. Verifica del triangolo identico all’originale e del comando nativo di ingrandimento, con scorrimento interno e senza overflow della pagina.

Richiesta esplicita: conservare il triangolo su mobile, prevedere l’ingrandimento per le etichette e salvare la regola generale di struttura invariata dei visuali tra dispositivi. **Passaggi di stato v19**, home generata **v15**, tema autonomo **v7**, master consultato **v59**. Rimossa la sorgente verticale dal solo schema P1; anteprima e vista ingrandita incorporano lo stesso SVG triangolare approvato. Componente nativo del tema «Ingrandisci l’immagine», con regione scorrevole da tastiera e almeno 960 px. Nessun ridisegno, cambio di frecce, nomi o relazioni scientifiche. Regola salvata in AGENTS e nel modello autonomo; sostituisce le precedenti possibilità di riorganizzare i visuali di A6/C4 senza refactoring estraneo del master. Bozza HTML, bozza testuale e scheda dello schema sincronizzate. Verifiche e pubblicazione in `../sito/triangolo-mobile.json`.

## Navigazione breve e area tematica — 18 ottobre 2026

**Pubblicato e verificato:** PR #28, merge `2983c6f653c7c6052ab2db126ab7c1c079487c9d`, workflow Pages `39114531184` riuscito; home e tre articoli HTTP 200 e identici byte per byte alla build verificata. Nessuna pubblicazione pendente.

Controlli completati: 12 viste a 320/390/768/1280 px, ritorni al catalogo funzionanti, nessun overflow; anteprime HTML e immagini mobile/desktop consegnate prima della pubblicazione.

Richiesta esplicita: accorciare «Tutti gli articoli» su mobile, usare sopra il titolo il nome della macro categoria e salvare le regole. **Versione corrente v18**, tema autonomo **v6**, terminologia **v4**, master consultato **v59**. Entrambi i ritorni diventano «← Articoli» su ogni dispositivo, con destinazione invariata; sopra il titolo compare «Materia e calore», come nel catalogo della home. Regole salvate nel modello, in AGENTS e nella terminologia; bozza HTML sincronizzata. Contenuto didattico, logo, CSS, script e altri visuali invariati. Verifiche e pubblicazione registrate in `../sito/navigazione-categorie.json`.

## Logo definitivo e tema v5 — 18 ottobre 2026

Richiesta esplicita approvata: pubblicare il logo definitivo anche al posto dell’icona nella barra in alto a sinistra degli articoli e salvarlo come regola grafica. **Versione corrente v17**, master v59, modello autonomo **v5**. Sostituito il simbolo φ con lo SVG dell’onda stazionaria a quattro creste, ampiezza 20; controlli condivisi di pausa/ripresa e movimento ridotto. Testo «Fisica» e ritorno all’inizio conservati. CSS comuni riusati identici dal modello, nessun altro contenuto o visuale modificato in questa richiesta; bozza HTML sincronizzata.

Verifiche e anteprime in `../sito/logo-definitivo.json` e `../sito/anteprima-visuali/`. Nodi, tratto, periodo e geometria del logo approvato conservati; testi/immagini del corpo confrontati con il precedente e invariati. Sette articoli esclusi non modificati. Pubblicazione completata con PR #26, merge `4e6ba399b0798d16db55b443dd7740dd58154dfe` e workflow Pages `39113796714` riuscito. Verificato HTTP 200 e HTML online identico all’output approvato; logo definitivo presente. Report HTTPS in `../sito/logo-definitivo.json`.

## Traduzione del PWR e revisione visuale — 18 ottobre 2026

Versione corrente **v16**, master consultato integralmente **v59**, tema comune **v4**. L’utente ha approvato con «Va bene» la conversione all’originale SVG con etichette italiane, il confronto originale/derivato, il controllo mobile e la revisione degli altri visuali. File corrente `risorse/centrale-nucleare-it.svg`; originale TVA e precedente PNG conservati. Tradotte tutte le etichette, comprese generatore di vapore, generatore elettrico, tubazioni, torri di raffreddamento e sottostazione elettrica. Confronto automatico: **423 nodi geometrici identici**; circuiti, colori, proporzioni e frecce invariati.

Immagine sostituita nelle due occorrenze dell’HTML (panoramica e ingrandimento). Rimossa la nota ormai superflua che traduceva le scritte inglesi; 21 note, richiami successivi rinumerati e tutti i collegamenti verificati. Crediti e registro materiali aggiornati, bozza testuale e HTML sincronizzati. Peso **15,047,175 byte**; sotto 18 MB. CSS e JavaScript identici alla v15; tutte le altre immagini e i calcoli conservati.

Verificati in Chromium a 390/1280 px: caricamento offline delle immagini, apertura/chiusura e scorrimento dello zoom, assenza di overflow della pagina, con script attivi e bloccati. Anteprime in `../sito/anteprima-visuali/`; esiti in `risorse/verifica-centrale.json`. Revisione dell’editing degli altri visuali in `../sito/revisione-visuali.md`. L’utente ha poi escluso interventi sulle anatre e precisato che le traduzioni riguardano infografiche e schemi, non le scritte nelle fotografie; regola salvata in AGENTS.

**Stato:** correzioni approvate eseguite, anteprime pronte per la consegna. Ramo `correzione/visuali-centrale`, derivato da main. Nessuna unione in main né nuova pubblicazione: le precedenti versioni pubblicate restano online. Prossimo passaggio: consegnare confronto, articolo e home aggiornati.

## Terminologia e perimetro del sito — 2026-10-18 09:16 (Europe/Rome)

Versione corrente **v15**, master **v59**, tema comune **v4**. Richiesta approvata: terminologia unica Articoli / Tutti gli articoli / Indice dell’articolo / Articolo precedente e successivo / Crediti delle immagini. Aggiornati soltanto i tre articoli conformati: Stati della materia, Passaggi di stato e Irraggiamento. Navigazione in sequenza tra questi tre, senza collegamenti ai sette articoli sospesi. Testo didattico, note, immagini, formule, CSS e simulazioni invariati; modificati etichette, navigazione e metadati di versione. HTML di lavorazione sincronizzato. Configurazione operativa in `pubblicazione.json`; verifiche e anteprime in `lavorazione/sito/terminologia.json` e `lavorazione/sito/anteprima-*.png`. Pubblicato con la PR #22 e workflow Pages 39107141160 concluso con successo. Verificati HTTPS: home e tre articoli conformati HTTP 200, identici all’output approvato; sette articoli sospesi HTTP 404; due reindirizzamenti storici disponibili. Sorgenti esclusi ancora identici. Rapporto finale in `lavorazione/sito/terminologia.json`.

## Pubblicazione autorizzata — 2026-10-18 09:00 (Europe/Rome)

L’utente ha approvato le anteprime e richiesto esplicitamente «Ok ok pubblica». Autorizzata l’integrazione del ramo `revisione/materia-passaggi-capitoli` in main e la pubblicazione tramite il workflow Pages esistente: Stati della materia **v13**, Passaggi di stato **v14**, Irraggiamento **v6**. Contenuti approvati al commit `fc325c9ff17e7339a15b403a26b6a98a161e8332`; nessun cambiamento ai tre HTML durante la preparazione della pubblicazione. Master v58 consultato; build locale e copie esatte nell’output verificate. Home con i due capitoli separati e vecchi indirizzi conservati tramite reindirizzamento. Pubblicazione completata tramite PR #20, merge `fb44117ae488c2cded4eb2a0abdeca0002839083`; workflow Pages `39106119681` concluso con successo. Verificati via HTTPS home v8, Stati della materia v13, Passaggi di stato v14, Irraggiamento v6 e i due vecchi indirizzi: HTTP 200 e contenuti identici byte per byte all’output approvato. Esiti e hash in `lavorazione/stati_della_materia_e_passaggi_di_stato/pubblicazione.json`. Non restano passaggi di pubblicazione pendenti. Le indicazioni di mancata autorizzazione nei blocchi storici sottostanti sono superate da questa richiesta.

## Revisione corrente — 2026-10-18 01:30 (Europe/Rome)

Richiesta diretta: note collassabili, pulsanti «Biblioteca», riparazione dei modelli particellari e del grafico del calore latente, note anche per Irraggiamento. L’utente ha precisato che il problema si presenta nell’**anteprima dentro ChatGPT**. Master **v56** consultato integralmente; modello autonomo **v3**. Regole persistenti aggiornate in A6, AGENTS e STILE_DISPENSE. Note native `details`/`summary`, chiuse all’apertura, con richiami che aprono la sezione e ritorni. Etichetta «← Biblioteca» nei due collegamenti di ciascun capitolo e nel modello. Tema comune riusato integralmente, senza altre varianti grafiche.

**Versione corrente v14**, HTML e bozza sincronizzati. Dimensioni intrinseche dichiarate per le immagini, per riservare lo spazio ed evitare spostamenti durante i salti alle note. Curva di riscaldamento con cinque controlli radio nativi e CSS: selezione, descrizione ed evidenziazione funzionano anche con JavaScript disabilitato. Conservati andamento, etichette, testo dei cinque tratti e dati. Variante mobile del medesimo SVG con asse orizzontale più compatto e caratteri leggibili: tutti i tratti visibili senza scorrimento laterale. Nessuna modifica ai calcoli, al confronto con il consumo domestico, alle immagini/GIF già ottimizzate o alle applicazioni. 22 note, 23 richiami, 8 domande.

Peso corrente 14558814 byte, sotto 18 MB. Verifiche della revisione corrente: `../stati_della_materia_e_passaggi_di_stato/verifica-interazioni.json`; anteprime desktop/mobile aggiornate nella cartella del capitolo. Consegna per lettura; **nessuna pubblicazione né unione in main**. I paragrafi sottostanti conservano la cronologia; il presente blocco identifica lo stato corrente.

Ultimo aggiornamento: 2026-10-17 23:29 (Europe/Rome). Master v53, letto con i riferimenti di stile. Ramo `revisione/materia-passaggi-capitoli`. Fonte v8 di `stati_della_materia_e_passaggi_di_stato.html`, blob `8ef5566c73f670dbf23b550e4e36a52cdb7ddfc2`. [Mappa iniziale della suddivisione](../stati_della_materia_e_passaggi_di_stato/proposta-editoriale.md).

## Ambito e approvazioni effettive

Capitolo sui sei passaggi di stato, scambi energetici, calore latente e curva dell’acqua. Tre applicazioni: sudore, pompa di calore e centrale PWR. **Un solo esempio svolto**, seguito da otto domande finali. Tema della v8 e separazione in due capitoli approvati. Apertura concreta sui cubetti che fondono, domanda su che cosa cambia e come viene usata l’energia ricevuta.

Testo approvato dall’utente prima degli adattamenti puntuali («Per i passaggi di stato va tutto bene»); P1 creato su sua richiesta. Materiali scelti acquisiti con fonti/licenze. Richieste successive applicate: eliminare frigorifero a favore della sola pompa di calore; usare il PWR; conservare lo sfondo della scultura; eliminare la foto della pentola; usare una massa da scultura intera, ipotizzata di 500 kg; infine **unificare i due svolgimenti nel calcolo completo dal ghiaccio a 0 °C al vapore a 100 °C**. Le scelte e queste revisioni sono autorizzate, senza nuova conferma dei medesimi file.

## Bozza e modello correnti

[Bozza completa](bozza.md). L’esempio unico comprende fusione a 0 °C, riscaldamento dell’acqua da 0 a 100 °C e vaporizzazione a 100 °C alla pressione atmosferica ordinaria. Massa 500 kg esplicitamente ipotizzata, non ricavata dalla fotografia. Trascurate dispersioni ed energia assorbita dalle attrezzature. Il calore specifico dell’acqua liquida è approssimato con 4180 J/(kg · K), spiegato insieme a Qr = m · c · ΔT e alla differenza di temperatura di 100 K.

Calcoli verificati: Qf = 500 · 334.000 = 167.000.000 J = 167 MJ; Qr = 500 · 4180 · 100 = 209.000.000 J = 209 MJ; Qv = 500 · 2.257.000 = 1.128.500.000 J = 1128,5 MJ. **Qtot = 1.504.500.000 J = 1504,5 MJ**, circa 1,50 miliardi di joule. Nessun riscaldamento iniziale del ghiaccio o surriscaldamento del vapore incluso. Domande 5 e 6 aggiornate su proporzionalità del totale e fase di riscaldamento omessa; nessuna soluzione nelle domande finali.

## Visuali disponibili e verifiche

[Registro visuali](visuali.md), [fonti/licenze/hash](risorse/materiali-scelti.json). C2 metallo fuso (Rajesh_India, CC BY-NC-ND 2.0; foto intera per uso non commerciale); P1 schema con frecce e variante mobile; P2–P8 immagini/GIF della v8; P9 curva qualitativa da adattare al telefono; A1 Jordan/sudore (credito «Lipofsky Basketballphoto.com», CC BY-SA 3.0); A2 pompa di calore (Wikideas1, CC0); A3 PWR (TVA, pubblico dominio), etichette inglesi spiegate e generatore elettrico distinto dal generatore di vapore.

E1: [schema completo unico](risorse/schema-esempio.svg), foto della scultura con sfondo conservato e quattro stati collegati da tre frecce energetiche. La richiesta esplicita sullo sfondo prevale sulla regola generale degli esercizi; nessuna rimozione eseguita. I byte della foto incorporata corrispondono alla foto scelta. Anteprima nel browser a 600 px ispezionata. Schemi precedenti separati sostituiti e recuperabili in Git. Foto della pentola esclusa dall’integrazione e dai crediti finali, conservata solo come riferimento. Nessun file ulteriore necessario.

Nessuna nuova simulazione: quelle microscopiche restano nel capitolo Stati della materia. Le verifiche iniziali dei singoli schemi sono state seguite dalle verifiche HTML registrate sotto. Nessuna pubblicazione.


## Via alla realizzazione

L’utente ha confermato «Ok procedi»: realizzazione dei due HTML autorizzata. HTML v9 integrati, verifiche in corso; nessuna pubblicazione. Peso iniziale: stati 6.270.253 byte, passaggi 20.808.247 byte. Richiesta autorizzazione puntuale per ottimizzare senza perdita le GIF del secondo capitolo, secondo il limite di 20 MB del master.

## Anteprima HTML realizzata — 2026-10-17 23:18 (Europe/Rome)

HTML v9 in `bozza.html`, copia con nome stabile alla radice del ramo di lavorazione; anteprime desktop/mobile salvate. Immagini incorporate, simulazioni particellari originali conservate e dotate di pausa, preferenza di movimento ridotto rispettata; curva selezionabile e PWR ingrandibile. Verifiche Chromium 390/1280 px e offline superate: immagini integre, nessun errore JavaScript, nessuna eccedenza orizzontale della pagina, 6/8 domande finali. Calcoli dell’esempio verificati: totale 1.504.500.000 J. Build locale superata, indice a 10 articoli e 12 casi di vecchi URL con query/frammenti verificati. Nessuna pubblicazione o modifica del workflow.

**Problema rilevato nella v9 (risolto dalla v10):** Stati della materia pesa 6.270.253 byte; Passaggi di stato pesa 20808480 byte, oltre il limite di 20.000.000 byte. Richiesta in chat approvazione per ottimizzare senza perdita copie delle tre GIF, conservando fotogrammi, colori e tempi; risposta non ancora ricevuta. File di Passaggi di stato consegnato come anteprima, non dichiarato definitivo conforme al peso. Le attribuzioni dei visuali ereditati incompleti sono dichiarate nei crediti; recuperata e verificata per hash la GIF di fusione (Moussa, pubblico dominio).

## Ottimizzazione autorizzata e applicata — 2026-10-17 23:29

Richiesta esplicita: «Fai entrambi i metodi su tutte le gif del capitolo passaggi di stato». Autorizzata riduzione sia della risoluzione sia dei fotogrammi delle tre GIF; non serve una nuova conferma della stessa modifica. Eseguita su copie, originali immutati. Dimensioni all’80%, circa due terzi dei fotogrammi; durata totale e loop preservati. Registro in `risorse/ottimizzazione-gif.json`; tabella in `visuali.md`. Tutti i fotogrammi decodificati corrispondono ai fotogrammi ricampionati e quantizzati attesi: nessuna scia dovuta alla codifica GIF. Confronti a metà animazione ispezionati.

HTML aggiornato a **v10**, sincronizzato con `bozza.html`, peso **14252684 byte**, sotto il limite di 20 MB e la soglia di avviso di 18 MB. Testo didattico confrontato automaticamente con v9: invariato. Crediti aggiornati con le elaborazioni. Build locale superata; dimensioni dei download ricalcolate. Prove Chromium offline a 390 e 1280 px: tre GIF caricate e animate (cambiamento dei fotogrammi verificato), nessuno scorrimento orizzontale della pagina o errore JavaScript; otto domande finali conservate. Anteprime desktop/mobile e indice aggiornati; home mostra 14,25 MB. Risultati in `risorse/verifica-gif-browser.json`. Restano dichiarati i crediti incompleti dei materiali ereditati dalla v8.

## Prossima operazione

Consegnare anteprima aggiornata e pesi. La revisione del peso è completata; pubblicazione non autorizzata e non eseguita.

## Tema comune applicato — 2026-10-17 23:35 (Europe/Rome)

Richiesta esplicita dell’utente: «Ricordati di applicare il tema». Allineato al tema comune già presente in `irraggiamento_it.html` v4 e nella home: Lexend incorporato con licenza, grigio/nero, bordi netti, copertina e indice laterale accessibile. Il precedente riferimento al tema v8 è superato da questa richiesta. **Versione corrente v11**, peso 14500324 byte. Testo didattico di ogni sezione confrontato con il precedente e invariato; tutte le immagini e GIF hanno gli stessi byte incorporati. Modello particellare originale conservato. Tema applicato anche ai comandi, alle tabelle e alle formule; solo evidenziazione della curva adattata al tema, senza modifiche ai dati.

Verifiche Chromium offline a 390/1280 px superate: Lexend caricato, indice apribile e chiudibile con Escape e con i collegamenti, focus/inert ripristinati, immagini integre, comandi delle simulazioni/curva e ingrandimento PWR funzionanti; nessuna eccedenza orizzontale o errore JavaScript. HTML di lavoro sincronizzato e anteprime desktop/mobile aggiornate. Build locale superata. Registro comune `../stati_della_materia_e_passaggi_di_stato/verifica-tema.json`. Nessuna pubblicazione.

## Regole editoriali aggiornate — 18 ottobre 2026, ore 00:31 (Europe/Rome)

Master v54: l’utente segnala errori nel tema e richiede di salvare l’esatto tema grafico adottato come modello autonomo per i capitoli futuri: `riferimenti/TEMA_DISPENSE.html`. Il riferimento operativo è questo modello, non il file del capitolo sull’irraggiamento. A6 ora stabilisce il modello autonomo già scelto, il riuso di struttura/stili e il confronto desktop/mobile; rimossa la richiesta ripetuta del template. A4 impone notazione esponenziale e prefissi SI nei calcoli; A5 richiede un confronto quantitativo concreto per interpretare ogni risultato significativo degli esercizi. Aggiornati anche AGENTS.md e il riferimento linguistico pertinente.

Questa operazione salva le regole: non modifica gli HTML né attesta che le versioni correnti siano già conformi alla richiesta più rigorosa. Alla revisione dei capitoli applicare il modello grafico autonomo esatto, adeguare la scrittura dei calcoli e integrare il confronto finale, conservando visuali e risultati fisici approvati. Nessuna pubblicazione.

## Correzione secondo il modello autonomo e master v55 — 2026-10-18 00:49 (Europe/Rome)

L’utente ha autorizzato la correzione dei due capitoli, scelto il confronto con il consumo domestico e stabilito la nuova regola delle precisazioni nelle note a piè di pagina. **Versione corrente v12**, 14548325 byte, HTML di lavoro sincronizzato. CSS e JavaScript comuni riusati identici da `riferimenti/TEMA_DISPENSE.html`; rimosse le sovrascritture del tema. Struttura dei titoli, etichetta Fisica in copertina, cornici/overview delle figure, formule con etichetta e righe native, pulsanti, indice e navigazione ripresi dal modello. Gli stili aggiuntivi sono limitati ai componenti assenti dal modello: tabelle, canvas, curva, modello fisico e note. Foto scelte e GIF ridotte conservate nei byte originali incorporati. Modello particellare invariato, con controllo della pausa isolato dal codice del tema.

Precisazioni spostate nelle note al termine del contenuto, prima dei crediti; richiami numerati e collegamenti di ritorno. Nuova regola salvata nel master v55 e nei riferimenti/AGENTS. Dati e passaggi necessari alla spiegazione restano nel corpo. Sei/otto domande finali conservate.

Calcoli riscritti in notazione scientifica e con prefissi SI: 1,67 · 10⁸ J = 167 MJ; 2,09 · 10⁸ J = 209 MJ; 1,1285 · 10⁹ J = 1,1285 GJ. Totale non arrotondato 1,5045 · 10⁹ J, risultato circa **1,50 GJ**. Confronto scelto dall’utente: circa **418 kWh**, equivalenti a **2,6 mesi** del consumo elettrico domestico medio di **1.930 kWh/anno** (ARERA, dati 2024; Sintesi Relazione annuale 2025, p. 36, pagina PDF 38). Fonte, ambito, conversione e natura media del confronto nella nota; registro `risorse/confronto-consumo-domestico.json`. Non confondere il dato elettrico con consumi complessivi comprensivi di combustibili. Il modello della scultura ora è HTML leggibile a 390 px, con stessa foto integrale, stessi dati, quattro stati e tre frecce; lo SVG precedente resta una risorsa di riferimento. Ingrandimento PWR tramite il componente nativo del modello, sostituendo il dialogo personalizzato.

Verifiche: confronto automatico degli stili effettivi con il modello a 390/1280 px, CSS/JS comuni confrontati integralmente, immagini caricate offline, nessuna eccedenza orizzontale o errore JS, curve/pausa/ingrandimento funzionanti. Calcoli e tutti i 24 frammenti storici controllati. Formule prive di tagli sul telefono. Anteprime aggiornate; risultati in `../stati_della_materia_e_passaggi_di_stato/verifiche-finali.json`. Build locale superata, entrambi sotto 20 MB. Limiti di attribuzione dei materiali ereditati già dichiarati conservati. Nessuna pubblicazione.

## Prossima operazione corrente

Consegnare le anteprime revisionate per la lettura dell’utente. Nessuna pubblicazione o unione in main autorizzata.

Il componente Note con richiamo e ritorno è ora salvato nel modello autonomo **v2** per il riuso futuro. Nessuna modifica ai CSS o ai comandi dei componenti preesistenti; gli stili delle note, già verificati nel browser, sono centralizzati nel modello e incorporati identici nei due capitoli. La sola ricollocazione del CSS non cambia la resa. Pesi correnti: Stati della materia 6519356 byte; Passaggi di stato 14548360 byte.

## Rilettura completa delle precisazioni tecniche — 2026-10-18 00:56 (Europe/Rome)

Richiesta dell’utente: cercare ovunque nel testo le precisazioni troppo tecniche e spostarle nelle note. **Versione corrente v13**, 14553082 byte. Riletti teoria, applicazioni, didascalie ed esempio. Approfondimenti trasferiti, senza eliminare le informazioni: evaporazione-energia-molecole, pressione-ebollizione, cristalli-nuvole, ghiaccio-secco-nube, brinamento-solidificazione, significato-latente, convenzione-energia, ciclo-refrigerante, circuiti-pwr, etichette-pwr, intervalli-temperatura, confronti-intermedi, rapporto-riscaldamento-fusione, rapporto-vaporizzazione-riscaldamento. Nel corpo restano concetti fondamentali, significato delle formule, dati/calcoli e confronto finale con il consumo domestico. Le note ora sono 22, con 23 richiami; numerazione riordinata secondo la lettura, ritorni multipli per le note condivise.

Tema/CSS, JavaScript, immagini/GIF e tutte le formule confrontati con la versione precedente e identici. Nessuna modifica dei risultati numerici, del modello particellare, dei confini dei capitoli o delle domande finali. Bozza testuale e HTML sincronizzati. Verifica Chromium offline a 390/1280 px: immagini caricate, nessuna eccedenza orizzontale né errore JS, formule senza tagli; tutti i richiami e ritorni verificati su telefono. Sei/otto domande conservate; anteprime aggiornate. Build locale superata. Nessuna pubblicazione.

## Prossima operazione corrente

Consegna delle anteprime alleggerite, in attesa della lettura dell’utente. Nessuna pubblicazione autorizzata.
