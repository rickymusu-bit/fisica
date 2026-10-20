# Stato — Home e GitHub Pages

## Scelta corrente approvata — onde verticali

L’utente ha confermato «Ok scelgo le onde verticali», dopo aver chiarito che il corpo dell’articolo è una sola superficie di lettura. Configurazione adottata: reticolo regolare, sinusoidi di uguale ampiezza e disposizione verticale sui lati. Applicata al tema condiviso di home, catalogo, Quiz, crediti, nove copie ammesse e modello v12. Il testo degli articoli rimane in un solo contenitore, con due fasce decorative continue e spazio riservato alla lettura; nessuna divisione in card di sezione.

Verificati allineamento del modello, crediti, build, dieci test e 150 combinazioni pagina/viewport/tema, oltre alla geometria delle fasce laterali. Confermati i nove sorgenti scientifici invariati. Schermate aggiornate anche per il corpo continuo dell’articolo. Master aggiornato limitatamente alla scelta grafica, v66; i sorgenti scientifici, i sospesi, le traduzioni, il manifest e il logo restano invariati. Scelta grafica approvata, pubblicazione ufficiale non richiesta: PR #43 ancora in bozza, main e Pages non modificati.


## Prova corrente — sinusoidi verticali ai lati delle card

L’utente ha scelto esplicitamente reticolo regolare (A) e sinusoidi di uguale ampiezza (A), chiedendo di provare la disposizione verticale ai lati. La pagina di confronto parte ora da queste scelte e dai lati verticali, con possibilità di tornare a sopra/sotto o solo sopra. Stessa geometria, periodo e palette: SVG trasposto, senza deformazioni. Fasce laterali di 24 px, spazio riservato al testo e sfumatura alle estremità; su smartphone i pulsanti della dimostrazione sono in colonna per conservare lo spazio di lettura.

La prova resta circoscritta al confronto; il sito e il modello conservano la disposizione orizzontale fino alla valutazione dell’utente. I componenti condivisi includono anche la variante laterale. Nessun sorgente scientifico, articolo sospeso, manifest o originale del logo modificato. PR #43 ancora in bozza, nessuna pubblicazione in main autorizzata.


## Lavorazione corrente — Stringhe globale, 20 ottobre 2026

Richiesta esplicita: applicare `PIANO_IMPLEMENTAZIONE_STRINGHE.md` nel ramo design, identificato dal piano come `design/stringhe-portale` (PR #43, bozza). Master consultato v64; aggiornamento circoscritto a v65 per identità, tema e navigazione, senza revisione dei contenuti didattici. Questa lavorazione non eredita le autorizzazioni di pubblicazione dei blocchi storici sottostanti.

Tema condiviso completo per home, catalogo, Quiz preparatorio, crediti, nove copie pubblicabili e modello autonomo v11. Ripristinati logo circolare originale e copertina casuale; quattro accessi conservati; Quiz descritto come futuro generatore di verifica. Aggiunti Automatico / Chiaro / Scuro persistenti, senza dipendenze esterne, e confronto indipendente dei bordi A/B, reticolo A/B e posizione delle curve. Il campione A visualizzato inizialmente resta provvisorio. Navigazione relativa online e fallback pubblico dalle copie scaricate.

I nove sorgenti ammessi, i sette sospesi, le traduzioni, il manifest e i due file grafici del logo rimangono identici alla base Git. Le modifiche agli articoli riguardano soltanto `_site`. Il modello è realmente aggiornato e sincronizzato con le componenti canoniche. Il registro conserva le attribuzioni e aggiorna il solo inventario del logo del modello.

Verificati crediti, sincronizzazione modello, build, dieci test e 150 combinazioni browser pagina/viewport/tema. Venti foto e nove destinazioni casuali provate. Nessun overflow o errore JavaScript. Chromium con mobile/touch emulato; Android fisico non disponibile. File:// bloccato dalla policy locale, documento autonomo verificato in memoria con rete bloccata; Actions esegue anche la prova diretta e ne registra l’esito. Dettagli, pro/contro e schermate in [confronto-stringhe.md](confronto-stringhe.md) e [verifica-stringhe.json](verifica-stringhe.json).

Consegna pronta: commit implementativo `3fab7a9`, Actions 39391624609 e anteprima 39391615879 riuscite. Nel rapporto CI anche file:// diretto è verificato, con 150 combinazioni e nessun errore JavaScript. Anteprima immutabile al commit `48494f222e1fef9faf3f25eb7faf7bc3e432e773` di `stringhe-preview`, collegamenti e schermate nel confronto. Provata anche la navigazione remota mobile fino a Conduzione e ritorno alla home; tema persistente. PR #43 in bozza. Prossimo passo: attendere la scelta esplicita su bordi e reticolo. Nessun merge o deployment del sito ufficiale autorizzato da questo incarico.


## Pubblicazione autorizzata — centralizzazione dei crediti

L’utente ha richiesto esplicitamente «Pubblica le modifiche». Autorizzate integrazione della PR #35 in main e pubblicazione tramite il workflow Pages esistente. Questa richiesta supera lo stato precedente di sola bozza; il manifest resta invariato. Si pubblicano le modifiche già verificate al commit `dce6358370806d393292aced65870f2294b357ef`, conservando pubblicamente la lista delle verifiche di licenza aperte. La pubblicazione non certifica i diritti mancanti. Pubblicazione completata e verificata: PR #35 integrata nel commit `bfe24eb80403dc6ca6cc9a1300163409d0892b8c`; [workflow Pages 39167838089](https://github.com/rickymusu-bit/fisica/actions/runs/39167838089) concluso con successo. Home, cinque articoli, pagina crediti, archivio JSON e OFL: HTTP 200 e contenuti identici byte per byte alla build verificata. Sette articoli esclusi e due indirizzi dismessi: HTTP 404. Esiti e hash nella proprietà `publication` di `crediti-verifiche.json`. Nessuna operazione di pubblicazione pendente; restano le verifiche dei diritti già segnalate.

## Centralizzazione dei crediti — 18 ottobre 2026

Richiesta esplicita eseguita sul ramo `crediti/centralizzazione`, base `ae721d0b10e4ab648da56f8ec9ae6926c91b3e72`: 20 articoli HTML analizzati e modificati, comprese traduzioni e sorgenti sospesi limitatamente ai crediti; manifest di pubblicazione invariato. Nessuna riammissione, merge o pubblicazione autorizzati da questa lavorazione. Tema v8 e master v60; modifica del master circoscritta alle regole dei crediti, senza refactoring generale estraneo alla richiesta.

Registro unico `risorse/crediti.json`, pagina statica `crediti.html`, snapshot autonomi offline e file OFL. 87 schede di provenienza e 178 risorse uniche inventariate. Le 20 copertine rinviano al registro centrale; rimosso il renderer delle sezioni finali e aggiornato il generatore storico. Cinque bozze HTML esistenti sincronizzate conservando i rispettivi collegamenti originali.

Confronto dei 20 sorgenti scientifici, dei media e degli script originali: invariati; 50 voci originali degli elenchi preservate integralmente, oltre ai due paragrafi di provenienza di Potenza termica, ai crediti delle 20 copertine, alle provenienze nel codice e al copyright/OFL. Build Pages: sette HTML (home, cinque articoli e crediti), 20 copertine, registro e licenza. Quattro regressioni e 18 prove browser; 263 link/ancore locali validi. Offline provato con HTML autonomo caricato in memoria e rete bloccata, con e senza JavaScript: l’apertura file:// è vietata dal browser gestito e non viene dichiarata verificata.

La verifica dei diritti NON è conclusa: 14 schede richiedono verifica, oltre a 56 risorse immagine senza associazione individuale certa. Nessun avviso noto è stato eliminato. Verificati nuovamente il testo personalizzato di © Raimond Spekking, la politica Chandra e la licenza Flickr CC BY-NC-ND 2.0. Dati mancanti non inventati, risorse non sostituite. [Rapporto](crediti-verifiche.json), [resoconto ed elenco file](crediti-resoconto.md), [anteprima desktop](anteprima-visuali/crediti-1280.png), [mobile](anteprima-visuali/crediti-390.png).

Prossimo passo: esaminare la proposta e risolvere le verifiche dei diritti riportate; il ramo è predisposto per revisione, senza modificare main o il sito pubblico.

## Ordine degli articoli e nuovi crediti — 18 ottobre 2026

Catalogo e navigazione aggiornati alla sequenza Stati della materia → Passaggi di stato → Conduzione → Convezione → Irraggiamento. Manifest v4, home generata v17; Conduzione e Convezione v4, Passaggi di stato v20 e Irraggiamento v11. Richiesta diretta dell’utente; sette HTML esclusi invariati. Build locale riuscita, anteprime e verifica browser prima del deploy. [Rapporto](verifica-ordine-crediti.json). Tre nuove fotografie Commons con licenze documentate; la GIF Tenor scelta non documenta una licenza libera specifica e conserva l’avvertenza nei crediti.

Pubblicato e verificato: [PR #34](https://github.com/rickymusu-bit/fisica/pull/34), merge `bc642106b06eb050a8f32c4197b5098f586556d2`; [workflow Pages riuscito](https://github.com/rickymusu-bit/fisica/actions/runs/39164627993). Catalogo e quattro articoli aggiornati rispondono HTTP 200 e coincidono byte per byte con i file controllati. [Verifica online](verifica-ordine-crediti-online.json). Nessun passaggio di pubblicazione aperto.

## Schema triangolare invariato su mobile — 18 ottobre 2026

**Pubblicato e verificato:** PR #30, merge `30e83a396a2a0accec04c03890d9dfec3cdfc252`, workflow Pages `39115320280` riuscito; home e Passaggi di stato HTTP 200 e identici byte per byte alla build verificata. Nessuna pubblicazione pendente.

Anteprima HTML interattiva e vista mobile consegnate prima della pubblicazione. Verifica del triangolo identico all’originale e del comando nativo di ingrandimento, con scorrimento interno e senza overflow della pagina.

Richiesta esplicita: conservare il triangolo su mobile, prevedere l’ingrandimento per le etichette e salvare la regola generale di struttura invariata dei visuali tra dispositivi. **Passaggi di stato v19**, home generata **v15**, tema autonomo **v7**, master consultato **v59**. Rimossa la sorgente verticale dal solo schema P1; anteprima e vista ingrandita incorporano lo stesso SVG triangolare approvato. Componente nativo del tema «Ingrandisci l’immagine», con regione scorrevole da tastiera e almeno 960 px. Nessun ridisegno, cambio di frecce, nomi o relazioni scientifiche. Regola salvata in AGENTS e nel modello autonomo; sostituisce le precedenti possibilità di riorganizzare i visuali di A6/C4 senza refactoring estraneo del master. Bozza HTML, bozza testuale e scheda dello schema sincronizzate. Verifiche e pubblicazione in `triangolo-mobile.json`.

## Navigazione breve e area tematica — 18 ottobre 2026

**Pubblicato e verificato:** PR #28, merge `2983c6f653c7c6052ab2db126ab7c1c079487c9d`, workflow Pages `39114531184` riuscito; home e tre articoli HTTP 200 e identici byte per byte alla build verificata. Nessuna pubblicazione pendente.

Controlli completati: 12 viste a 320/390/768/1280 px, ritorni al catalogo funzionanti, nessun overflow; anteprime HTML e immagini mobile/desktop consegnate prima della pubblicazione.

Richiesta esplicita eseguita: due collegamenti «← Articoli» in ogni articolo e nome esatto dell’area tematica della home sopra il titolo («Materia e calore» per i tre attuali). Tema autonomo **v6** con segnaposto «Nome dell’area tematica»; regole operative in AGENTS e `riferimenti/TERMINOLOGIA_SITO.md` **v4**, che sostituiscono il precedente ritorno di A6 del master v59. Master conservato senza refactoring estraneo alla richiesta. Home generata **v14**, Stati della materia **v16**, Passaggi di stato **v18**, Irraggiamento **v9**. Sette articoli esclusi invariati. Report verifiche e pubblicazione: `navigazione-categorie.json`.

## Logo definitivo, tema comune e pubblicazione autorizzata — 18 ottobre 2026

L’utente ha approvato l’onda stazionaria con ampiezza 20 e richiesto esplicitamente: eliminare gli altri tentativi, pubblicarla nella home e al posto dell’icona nella barra in alto a sinistra degli articoli, salvare la scelta come regola grafica. **Pubblicazione autorizzata**, compresi il logo definitivo e le correzioni già pronte e approvate nel ramo corrente.

Unici file grafici correnti `identita/logo-materia-oscura.svg` e `.gif`, identici byte per byte alla versione stazionaria approvata. Rimossi 25 file dei tentativi precedenti, i generatori superati e l’archivio locale a otto lobi; riferimento originale dell’utente preservato. Generatore unico autonomo `scripts/logo_materia_oscura.py`; controlli comuni `identita/controlli-logo.js` incorporati identici nei documenti. In Git resta recuperabile la storia, senza alternative attive nell’albero corrente.

**Tema autonomo v5**: componente del logo nella barra degli articoli, SVG a 44 px, pulsante di pausa/ripresa da clic o tastiera, rispetto del movimento ridotto. Il collegamento «Fisica» continua a riportare all’inizio. Regola salvata nel modello `riferimenti/TEMA_DISPENSE.html`, in AGENTS, `identita/README.md` v5 e `riferimenti/TERMINOLOGIA_SITO.md` v3; A6 del master v59 rende già vincolante l’uso del modello autonomo aggiornato. Nessun refactoring del master incluso.

Home generata **v13** (template v10), Stati della materia **v15**, Passaggi di stato **v17**, Irraggiamento **v8**. HTML di lavorazione sincronizzati. Solo i tre articoli conformati sono aggiornati; sette sorgenti sospesi verificati identici a main. Corpo didattico e altre immagini confrontati con l’inizio di questa richiesta e invariati. La traduzione SVG della centrale PWR già approvata è conservata in Passaggi di stato. Build: soltanto home e tre articoli, venti copertine e i due file pubblici del logo sotto `identita/`; nessun indirizzo dismesso ripristinato.

Verifiche browser: 28 viste a 320/390/768/1280 px, script attivi/bloccati, movimento normale/ridotto, pausa/ripresa da tastiera, indice, controlli e assenza di overflow/errori JavaScript. CSS e controlli condivisi identici al modello v5, documenti autonomi, altri visuali preservati. Report `logo-definitivo.json`; verifica del modello e hash `verifica-logo.json`. Anteprime home/articoli in `anteprima-visuali/`, anteprima autonoma unica `anteprima-logo.html`.

**Pubblicazione completata e verificata:** anteprime consegnate prima del merge, PR #26 integrata nel commit `4e6ba399b0798d16db55b443dd7740dd58154dfe`; workflow Pages `39113796714` riuscito. Home (anche URL radice), tre articoli e due file autonomi del logo HTTP 200, identici byte per byte all’output approvato; nove indirizzi dismessi e sette percorsi dei tentativi HTTP 404. Esiti HTTPS e hash in `logo-definitivo.json`. Regola grafica e rimozione dei tentativi completate; nessuna operazione di pubblicazione pendente.

## Ampiezza di oscillazione raddoppiata — 18 ottobre 2026

Richiesta esplicita: «Ok raddoppia l’ampiezza di oscillazione». La versione corrente della GIF/SVG stazionaria usa **A = 20**, prima A = 10; raggio di riferimento 104, quattro creste, nodi angolari fissi, periodo 4 s e tratto di 7 unità conservati. Il fattore temporale del generatore è moltiplicato per due senza alterare la geometria di riferimento o le proposte precedenti. Modello corrente: `r(θ,t)=104+20 cos(4θ) sin(2πt/T)`.

Rigenerati gli stessi file stabili `identita/logo-materia-oscura-onda-stazionaria.svg` e `.gif`, l’anteprima HTML e le immagini desktop/mobile. Rapporto fra gli spostamenti massimi misurati prima/dopo: **2,0**. Raggi estremi 84 e 124; nodi fermi, nessuna rotazione, ritorni al cerchio identici, GIF trasparente e loop continuo di 80 fotogrammi verificati. Controlli d’accessibilità dell’anteprima nuovamente superati. Registro aggiornato `verifica-logo-onda-stazionaria.json`; specifiche in `identita/README.md` v4 e relativo richiamo in AGENTS. Errore massimo dell’interpolazione temporale ora inferiore a 0,10 unità del viewBox.

Home, logo già integrato e dieci articoli conservati invariati. Master v59 e vincoli già consultati restano invariati. Ramo dedicato corrente `correzione/visuali-centrale`, derivato da main. **Ampiezza raddoppiata, risultati verificati e pronti alla consegna; nessuna unione in main o pubblicazione.**

## Correzione finale: onda sinusoidale stazionaria — 18 ottobre 2026

L’utente corregge il modello: «L’onda sì è sinusoidale ma è un’onda stazionaria, non progressiva». Restano quattro creste dalla richiesta precedente. Realizzati i file autonomi `identita/logo-materia-oscura-onda-stazionaria.svg` e `.gif`, nero su trasparente, singolo contorno visibile, nodi angolari fermi e ventri oscillanti; nessuna rotazione. La specifica progressiva e quella a otto lobi sono superate per la nuova consegna.

Modello `r(θ,t)=104+10 cos(4θ) sin(2πt/T)`, con `T=4 s`. Otto nodi fissi a 22,5° + k · 45°; quattro creste nei massimi di deformazione. La curva passa per il cerchio due volte per periodo e inverte il segno dello spostamento nei ventri. Fattore sinusoidale campionato in 32 intervalli nello SVG, errore sullo spostamento inferiore a 0,05 unità. Generatore `scripts/logo_onda_stazionaria.py`; funzione geometrica precedente condivisa tramite un parametro temporale opzionale, senza cambiare l’uscita predefinita della proposta progressiva.

GIF 256 × 256 px, 80 fotogrammi a 20 fps, ciclo di 4 s. Verificati nove istanti: nodi entro 0,08 unità dalle coordinate fisse, spostamento dei ventri e sua inversione, quattro creste alle deformazioni massime, ritorni al cerchio identici pixel per pixel. Verificati trasparenza, soli pixel opachi neri, durata e raccordo continuo della GIF; anteprima a script attivi/bloccati con movimento normale/ridotto, pausa/ripresa da tastiera e assenza di overflow. Esiti, pesi e hash in `verifica-logo-onda-stazionaria.json`.

Indicazioni aggiornate in AGENTS e in `identita/README.md` v3, conservando la provenienza delle proposte superate. Anteprima autonoma `anteprima-logo-onda-stazionaria.html`; immagini in `anteprima-visuali/logo-onda-stazionaria-*`. Home v12, logo attualmente integrato e dieci sorgenti degli articoli verificati invariati. Master v59 invariato, già letto integralmente. Ramo corrente derivato da main `correzione/visuali-centrale`. **GIF stazionaria completata e verificata; nessuna sostituzione nella home, unione in main o pubblicazione.**

## Correzione: sinusoide progressiva con quattro creste — 18 ottobre 2026

Richiesta esplicita successiva all’interruzione: «Non ci devono essere lobi ma una sinusoide che viaggia in un cerchio chiuso. Rifai la gif con 4 creste (n=2 closed loop)». La proposta a otto lobi è superata. Realizzati `identita/logo-materia-oscura-onda-progressiva.svg` e `.gif`: una sola linea nera e trasparente, quattro creste che avanzano in senso orario, ampiezza costante e deformazione contenuta. Non si passa globalmente dal cerchio a una figura lobata. Profilo circolare `r(θ,t)=104+10 cos(4θ−2πt/T)`, periodo `T=4 s`; l’indice n della richiesta non viene presentato come convenzione universale.

GIF autonoma 256 × 256 px, 80 fotogrammi a 20 fps, ciclo continuo. SVG senza script, con alternativa ferma per la preferenza di movimento ridotto. Generatore dedicato `scripts/logo_onda_progressiva.py`; il generatore del logo precedente è ripristinato identico a HEAD, così non si conserva come scelta corrente la variante interrotta. Indicazioni del nuovo modello salvate in AGENTS e in `identita/README.md` v2.

Verificati quattro massimi radiali a sette istanti, raggi minimo/massimo invariati (94/114), avanzamento angolare di 22,5° al secondo, trasparenza, soli pixel opachi neri, durata e raccordo del loop GIF senza salto. Anteprima a script attivi e bloccati, movimento normale/ridotto, comandi da tastiera e nessuna eccedenza orizzontale; rapporto `verifica-logo-onda-progressiva.json`. Anteprima autonoma `anteprima-logo-onda-progressiva.html`, immagini `anteprima-visuali/logo-onda-progressiva-*`.

Home v12, logo già integrato e dieci sorgenti degli articoli invariati byte per byte: questa richiesta riguarda la nuova GIF, non dispone una sostituzione nella home. La variante a otto lobi generata prima dello stop, non salvata su GitHub, è conservata come lavoro locale superato in `/workspace/varianti-logo-superate/otto-lobi/`; nessun originale dell’utente eliminato. Le indicazioni storiche sottostanti sulla variante a otto lobi sono superate.

Ramo corrente derivato da main `correzione/visuali-centrale`, master v59 invariato e già letto integralmente. **Correzione realizzata e verificata, pronta per la consegna; nessuna unione in main né pubblicazione.**

## Variante autonoma a otto lobi — 18 ottobre 2026

Richiesta esplicita: «Bellissimo. Riesci a farne un altro con 8 lobi?». Creato un secondo logo con lo stesso tratto nero, sfondo trasparente e ciclo di 8 secondi: cerchio → otto lobi → cerchio → otto lobi sfalsati di 22,5° → cerchio. Una sola curva chiusa visibile, nessuna sovrapposizione. File autonomi `identita/logo-materia-oscura-otto-lobi.svg`, `.gif` e `-statico.svg`; specifiche aggiunte a `identita/README.md` v2. Home v12 e logo originale a quattro lobi conservati byte per byte; nessuna sostituzione richiesta o effettuata.

Riutilizzato il generatore esistente aggiungendo `--lobes 8`, con maggiore risoluzione geometrica per gli otto lobi. Il valore predefinito rimane quattro: entrambe le uscite SVG precedenti sono identiche byte per byte. GIF trasparente 256 × 256 px, 160 fotogrammi a 20 fps, ciclo di 8 s. Verificati otto massimi radiali in entrambe le configurazioni, tre ritorni al cerchio identici pixel per pixel, trasparenza, soli pixel opachi neri e durata della GIF; anteprima con script attivi/bloccati, movimento normale/ridotto, comandi da tastiera e nessun overflow su smartphone. Esiti, pesi e hash in `verifica-logo-otto-lobi.json`; anteprima autonoma `anteprima-logo-otto-lobi.html`, immagini in `anteprima-visuali/logo-otto-lobi-*`.

Master v59 letto integralmente. Nessuna modifica agli articoli, alla home o ai file del logo originale; sorgenti verificati contro HEAD. Ramo corrente `correzione/visuali-centrale`, derivato da main, senza unione in main né nuova pubblicazione. **Variante completata e pronta per la consegna come SVG/GIF autonomi.**

## Logo animato di Materia Oscura — 18 ottobre 2026

Richiesta esplicita: usare come riferimento la stringa chiusa della figura centrale in basso dell’immagine `14936.jpg`; nero su trasparente, senza sovrapporre le configurazioni. Ciclo autorizzato **cerchio → quattro lobi orizzontali/verticali → cerchio → quattro lobi diagonali → cerchio**. Alla domanda sul posizionamento l’utente ha scelto **accanto al titolo**, chiedendo anche il salvataggio autonomo per usi futuri.

Realizzati `identita/logo-materia-oscura.svg` (SVG dichiarativo autonomo, 16.793 byte), `logo-materia-oscura.gif` (256 × 256 px, 160 fotogrammi, 20 fps, 8 s, 158.933 byte) e una variante SVG statica. Specifiche e modalità di riuso in `identita/README.md`; generatore geometrico `scripts/logo_materia_oscura.py`. Riferimento JPEG conservato byte per byte in `risorse-originali/riferimento-stringhe.jpg`, escluso dalla build. Nessuna ricerca di immagini, sovrapposizione di curve, scia o colore aggiunto.

**Home corrente v12** (template v9): logo accanto al titolo, SVG originale incorporato durante la build. Premere il logo mette in pausa/riprende; tasto accessibile da tastiera, descrizione aggiornata e preferenza di movimento ridotto rispettata. Senza script il logo resta animato tramite SVG nativo; con movimento ridotto viene mostrato un solo cerchio fermo. Una sola curva visibile in ogni modalità. Titolo, sottotitolo, catalogo, copertine e articoli conservati. Workflow esteso a `identita/**` per gli aggiornamenti futuri, senza pubblicazione ora.

Verifiche in `verifica-logo.json`: quattro fasi a 0/2/4/6/8 s; tre cerchi identici pixel per pixel; trasparenza e soli pixel neri opachi della GIF; SVG animato caricato come normale immagine; 12 viste della home a 320/390/1280 px con script attivi/bloccati e movimento normale/ridotto, pausa/ripresa da tastiera e catalogo, senza overflow o errori JavaScript. Tutti e dieci i sorgenti degli articoli identici all’inizio della richiesta; output sempre home e tre articoli, senza reindirizzamenti.

Anteprima interattiva autonoma `anteprima-logo.html`, home `_site/index.html`; immagini in `anteprima-visuali/home-logo-mobile.png`, `home-logo-desktop.png` e `logo-anteprima.png`. Il motivo a quadretti dell’anteprima non è incorporato nei file del logo. Master v59 letto integralmente; ramo corrente derivato da main `correzione/visuali-centrale`. **Realizzazione completata, anteprime pronte; nessuna unione in main o nuova pubblicazione.** Prossimo passaggio: consegnare anteprime e file riutilizzabili.

## Identità della home — 18 ottobre 2026

Richiesta esplicita: titolo «Materia Oscura», sottotitolo «Guida pratica per fare luce sulla Fisica», nessuna etichetta visibile «Area tematica» nella home; salvare le scelte come regole. **Home corrente v11** (template v8). Aggiornati h1, titolo della pagina e metadati descrittivi; catalogo con il solo nome «Materia e calore». Rimossi markup e CSS dell’etichetta. Regole correnti in `riferimenti/TERMINOLOGIA_SITO.md` **v2**, richiamate in AGENTS; identità riportata anche nel README. Il nuovo nome è un’eccezione esplicita dell’utente rispetto al vecchio nome in A6 del master v59; nessun refactoring generale del master incluso in questa modifica circoscritta.

Master v59 e stato letti integralmente. Ramo di lavorazione corrente `correzione/visuali-centrale`, derivato da main; nessuna modifica ai dieci sorgenti degli articoli rispetto all’inizio di questa richiesta. Centrale italiana e altre correzioni precedenti conservate. Build con home e tre articoli, nessun indirizzo dismesso ripristinato. Verifiche Chromium a 320/390/1280 px: titolo, sottotitolo, metadati, apertura/chiusura del catalogo e assenza di overflow; esiti in `identita-home.json`. Anteprima HTML `_site/index.html`; immagini aggiornate `anteprima-visuali/home-desktop.png`, `home-mobile.png`, `catalogo-desktop.png`, `catalogo-mobile.png`.

**Stato:** modifiche completate e anteprima pronta. Nessuna nuova pubblicazione né unione in main. Le versioni pubblicate restano invariate. Prossimo passaggio: consegnare l’anteprima e il salvataggio GitHub.

## Area tematica e recupero dell’editing visuale — 18 ottobre 2026

Gerarchia approvata con «Va bene»: **Area tematica → Articolo → Sezione**, salvata in `riferimenti/TERMINOLOGIA_SITO.md` e richiamata da AGENTS. Home generata **v10** (template v7): il gruppo «Materia e calore» ora esplicita «Area tematica»; comando «Articoli», tre contenuti e tema conservati. Dimensioni dei download ricalcolate dalla build. PWR tradotto nell’articolo Passaggi di stato **v16**, dopo proposta e approvazione dell’editing; confronto originale/derivato incluso. Inventario di revisione dei tre articoli in `revisione-visuali.md`. Successiva indicazione dell’utente: nessuna modifica alla termografia delle anatre; tradurre soltanto infografiche e schemi, senza estendere la regola alle scritte fotografiche. Regola salvata in AGENTS.

Build: soltanto home e tre articoli; nessun reindirizzamento ripristinato. Sette sorgenti congelati verificati identici a main. Stati della materia v14 e Irraggiamento v7 invariati integralmente. Verifiche home/PWR a 390 e 1280 px con script attivi e bloccati, nessun overflow o errore JavaScript. Anteprime in `anteprima-visuali/`; rapporto `../passaggi_di_stato/risorse/verifica-centrale.json`.

Ramo `correzione/visuali-centrale`, derivato da main. **Anteprima pronta, nessuna nuova pubblicazione né unione in main.** Consegna automatica dell’anteprima prima della pubblicazione secondo B5; i tre articoli pubblicati restano nelle versioni precedenti. Master v59 conservato; la gerarchia approvata integra operativamente A6 nel riferimento dedicato.

## Rimozione dei vecchi collegamenti — 2026-10-18 09:23 (Europe/Rome)

Richiesta esplicita dell’utente: «Non lo fare. Cancella i vecchi link degli articoli non conformati». Rimossi anche i due reindirizzamenti di compatibilità della precedente dispensa unificata dalla pubblicazione; la build non li copia più e rifiuta un elenco di reindirizzamenti non vuoto. Manifest v2, regola operativa in AGENTS e README aggiornati. Home e tre articoli conformati restano identici; i sette sorgenti sospesi restano conservati e invariati. Il master v59, letto integralmente, prevede già in D2 l’eccezione per la rimozione esplicita dei vecchi indirizzi. Nessuna modifica editoriale o al tema. Output previsto: soltanto home e tre articoli, senza altre pagine HTML. Pubblicazione completata con PR #24, merge 45c97e64b16430570e80251d0714f40ceb93d2c0 e workflow Pages 39107547399 riuscito. Verificati via HTTPS tutti i nove indirizzi dismessi: HTTP 404; home e tre articoli: HTTP 200 e copie identiche all’output approvato. Sorgenti conservati invariati. Esiti in `rimozione-link.json`. Nessun reindirizzamento rimane pubblicato. I blocchi storici che indicano reindirizzamenti mantenuti sono superati da questa richiesta.

## Terminologia unica e articoli conformati — 2026-10-18 09:16 (Europe/Rome)

L’utente ha approvato il vocabolario proposto e chiesto di salvare la regola e aggiornare il sito. Successivamente ha disposto: «Togli dalla pubblicazione gli articoli che non abbiamo conformato e lasciali fuori da ogni aggiornamento». Sono ammessi soltanto Stati della materia, Passaggi di stato e Irraggiamento; i sette sorgenti esclusi, elencati in `pubblicazione.json`, sono conservati identici e non vengono aggiornati. L’esclusione comprende catalogo, download e output Pages, con verifica successiva HTTP 404 per i vecchi indirizzi. Nessuna modifica agli stati o alle bozze dei sette articoli congelati.

Master v59 e AGENTS aggiornati; modello autonomo v4 con nomi coerenti. Home pubblicabile v9, soli tre articoli e pulsanti Scarica con dimensioni reali. Articoli v14/v15/v7, etichette e navigazione allineate. Build controllata tramite elenco ammessi, confronto del catalogo, controllo dei collegamenti e pulizia dell’output; il manifest attiva il workflow Pages quando cambia. I due reindirizzamenti storici della materia restano pubblicati per compatibilità. Ramo `sito/terminologia-coerente`, derivato da main; pubblicazione autorizzata dalla richiesta di aggiornare il sito. Pubblicato con la PR #22 e workflow Pages 39107141160 concluso con successo. Verificati HTTPS: home e tre articoli conformati HTTP 200, identici all’output approvato; sette articoli sospesi HTTP 404; due reindirizzamenti storici disponibili. Sorgenti esclusi ancora identici. Rapporto finale in `lavorazione/sito/terminologia.json`.

Rapporto corrente: `terminologia.json`; anteprime della home e dell’indice a 390/1280 px nella cartella. Il tema e la regola di esclusione sono permanenti; per riammettere un articolo sospeso occorre una richiesta esplicita dell’utente.

## Pubblicazione autorizzata — 2026-10-18 09:00 (Europe/Rome)

L’utente ha approvato le anteprime e richiesto esplicitamente «Ok ok pubblica». Autorizzata l’integrazione del ramo `revisione/materia-passaggi-capitoli` in main e la pubblicazione tramite il workflow Pages esistente: Stati della materia **v13**, Passaggi di stato **v14**, Irraggiamento **v6**. Contenuti approvati al commit `fc325c9ff17e7339a15b403a26b6a98a161e8332`; nessun cambiamento ai tre HTML durante la preparazione della pubblicazione. Master v58 consultato; build locale e copie esatte nell’output verificate. Home con i due capitoli separati e vecchi indirizzi conservati tramite reindirizzamento. Pubblicazione completata tramite PR #20, merge `fb44117ae488c2cded4eb2a0abdeca0002839083`; workflow Pages `39106119681` concluso con successo. Verificati via HTTPS home v8, Stati della materia v13, Passaggi di stato v14, Irraggiamento v6 e i due vecchi indirizzi: HTTP 200 e contenuti identici byte per byte all’output approvato. Esiti e hash in `lavorazione/stati_della_materia_e_passaggi_di_stato/pubblicazione.json`. Non restano passaggi di pubblicazione pendenti. Le indicazioni di mancata autorizzazione nei blocchi storici sottostanti sono superate da questa richiesta.

Aggiornamento: 17/10/2026 19:53 (Europe/Rome).

## Preferenza permanente — anteprima del sito

Richiesta esplicita dell’utente: fornire sempre l’anteprima dopo ogni modifica al sito. Regola registrata nel master v53, sezione B5: anteprima HTML interattiva e immagini delle parti modificate, con vista mobile quando pertinente, prima della pubblicazione e senza una richiesta separata. Per la home v7 l’anteprima è stata preparata e consegnata; l’utente ha autorizzato esplicitamente la pubblicazione della PR #19 con «Ok pubblica».

## Revisione corrente — home italiana v7

Correzione richiesta: Marco Polo è una piattaforma petrolifera offshore, non una nave. Aggiornati didascalia, testo alternativo e titolo interno nel manifest e nei dati della home. Fotografia, crediti e licenza conservati. Versione dell’output aggiornata a v7. L’utente ha scelto esplicitamente «Pannello laterale apribile da Articoli». Realizzato un dialog nativo laterale: comando Articoli in alto a sinistra, Italiano in alto a destra, rimosso Esplora e il suo blocco inferiore. Elenco raggruppato con download e dimensioni reali; chiusura con ×, Esc o clic sullo sfondo. Focus confinato nel dialog e restituito al comando alla chiusura, scorrimento della pagina bloccato durante l’apertura, supporto alle ancore già pubblicate. Senza JavaScript il catalogo è visibile in pagina.

Verifiche completate: build con dieci HTML italiani e venti copertine; Chromium a 320, 390, 768, 1024 e 1440 px; apertura da tastiera, focus, chiusura con tutti e tre i metodi, ritorno al comando, ancore dirette, download confrontato byte per byte e dimensioni dei nove file; nessun overflow o errore JavaScript; fallback senza JavaScript. Controllati visivamente pannello mobile e desktop. Manifest e dati della home coerenti per Marco Polo; immagine, crediti e licenza conservati. README aggiornato.

Fase: modifiche completate e verificate nel ramo `home/copertina-marco-polo`; anteprima consegnata e pubblicazione autorizzata dall’utente con «Ok pubblica». Integrare la PR #19 e verificare il workflow Pages e la home online. La pubblicazione precedente della v6 è conclusa con successo (PR #18, workflow 39055028249).

## Revisione precedente — home italiana v6

Richiesta aggiornata: «Togli proprio le altre lingue, lascia solo il selettore della lingua in alto a destra con solo l’italiano». Rimossi dal template i collegamenti francese e albanese. La build pubblica esclusivamente la home e i nove articoli italiani, con venti copertine: non genera le home tradotte né copia gli articoli tradotti. I sorgenti delle traduzioni restano conservati nel repository e non vengono pubblicati. Il selettore nativo in alto a destra mantiene la sola voce Italiano. Conservate tutte le modifiche già richieste: rimozione Indice, catalogo al clic, icona e peso effettivo dei download. Master consultato: v52; modifica locale autorizzata secondo B2.

Verifiche: build completa con dieci HTML tutti lang=it, assenza di home e articoli fr/sq nell’output; selettore con una sola voce Italiano; Chromium desktop e smartphone, catalogo inizialmente nascosto, apertura e focus da tastiera, ancore e download. Aggiornato README. Ramo dedicato `home/esplora-download`, PR #18. L’utente ha autorizzato esplicitamente la pubblicazione con «Pubblica»: integrazione in main e deployment tramite il workflow Pages esistente autorizzati; verificare il completamento delle Actions e la home online.

---

## Stato precedente e autorizzazioni

Home `index.html` v4: «Praticamente la Fisica», sottotitolo «Guida essenziale a tutto ciò che ci circonda», tema Mac approvato e Lexend incorporato. Nessun nome o cognome dell’utente nei testi o nei metadati della home; terminologia «articoli» e «argomenti».

Ultima richiesta esplicita: «pubblica l’irraggiamento. poi togli i titoli alle immagini della copertina della home:bastano le didascalie. sempre nella home: la barra superiore usala per l’indice e la selezione della lingua, togli le scritte ripetitive e inutili che ci sono adesso».

Irraggiamento aggiunto come nono articolo italiano, con lettura e download. Si parte dal file approvato del ramo `istruzioni/tema-mac`: contenuto conservato, meta autore rimosso e versione v4. Il precedente articolo Potenza termica usa la v7 pronta nello stesso ramo, con navigazione precedente/successivo; rispetto alla v6 di main cambiano soltanto versione, data e navigazione. [Stato dell’irraggiamento](../irraggiamento/stato.md).

## Home e lingue

Barra superiore persistente con due menu HTML nativi: Indice e lingua. Eliminati il nome del sito e l’etichetta Fisica ripetuti nella barra, l’indice separato nel catalogo e il piè di pagina ripetitivo. Con JavaScript i menu si chiudono con Esc, clic esterno o scelta della sezione; senza script restano utilizzabili tramite summary e collegamenti nativi.

Italiano, francese e albanese sono le lingue già presenti nel repository. La home italiana mostra nove articoli; `index_fr.html` e `index_sq.html`, generati durante la build, mostrano ciascuno i quattro articoli esistenti nella rispettiva lingua. `lingue/home.json` contiene interfaccia, titoli e descrizioni del catalogo e didascalie tradotte. Gli articoli tradotti non sono modificati né generati automaticamente. Il nome del sito resta Praticamente la Fisica.

## Copertine e attribuzioni

Venti copertine fornite e scelte dall’utente, conservate in `copertine/` con manifest, fonti, autori, licenze e hash dei file recuperati. Foto intere, ridimensionate e convertite in WebP senza ritagli. La copertina cambia casualmente a ogni caricamento, con uguale probabilità e possibili ripetizioni. È caricata soltanto la foto scelta; senza JavaScript compare la prima; in caso di errore viene provata la successiva.

Rimossa la barra con il titolo della foto: restano immagine, didascalia e testo alternativo. Crediti di tutte le immagini in una sezione apribile, con indicazione della foto corrente. La raccolta non contiene la precedente foto Super-Kamiokande; i relativi vincoli di autorizzazione riguardano la precedente selezione, conservata nella cronologia Git. Nessuna richiesta esterna per foto o font durante la visita.

## Build, verifiche e pubblicazione

Build verificata: venti HTML (tre home e diciassette articoli: nove italiani, quattro francesi, quattro albanesi), venti copertine, manifest e `.nojekyll`. Il quiz e i documenti di lavorazione restano esclusi. `scripts/home_covers.py` genera la copertina e i crediti; `scripts/home_languages.py` genera le home tradotte; `scripts/build_pages.py` verifica percorsi e lingua prima della copia. Cartelle `copertine/` e `lingue/` e relativi renderer attivano il workflow Pages.

Controlli in [verifiche-home.json](verifiche-home.json): home a 320, 390, 768, 1024 e 1440 px senza overflow, menu persistenti, focus e tastiera; tutte e venti le scelte della copertina con didascalia e crediti coerenti; navigazione delle tre lingue con e senza JavaScript, collegamenti reali agli articoli nella lingua corretta. Irraggiamento verificato a 390 e 1440 px: immagini caricate, indice nativo, assenza di richieste esterne e di errori JavaScript, navigazione dal precedente. Contenuto confrontato integralmente con il sorgente approvato, salvo meta autore e versione. Build e controllo delle differenze superati.

Fase: realizzazione conclusa e verificata, pubblicazione richiesta tramite il workflow Pages esistente dopo l’integrazione in main. Stato del deployment consultabile nelle Actions. Git conserva la cronologia delle versioni precedenti.

## 20 ottobre 2026 — piano Stringhe per Codex, non ancora realizzato

L'utente ha confermato la navigazione della home con quattro accessi e corretto la proposta grafica: conservare il logo circolare animato approvato vicino al titolo «Stringhe», conservare la foto di copertina casuale, testare due bordi formati da sinusoidi sovrapposte in opposizione di fase (ampiezze uguali/diverse). Richiesta la modalità scura **opzionale**. La sezione «Quiz» del sito è un futuro **generatore di quiz di verifica su argomenti scelti dall'utente**, non il progetto separato «Chi vuol essere rimandato».

Specifiche complete salvate in `lavorazione/sito/PIANO_IMPLEMENTAZIONE_STRINGHE.md` sul ramo `design/stringhe-portale`, collegato alla PR #43. Stato: **pianificato, da implementare e confrontare**. Non risulta approvata nessuna delle due varianti grafiche come definitiva; il sito pubblico rimane fuori da questa fase.
