# Stato — Pagina di benvenuto e GitHub Pages

Master iniziale consultato: v45; versione corrente v49 dopo la rimozione dei reindirizzamenti richiesta dall’utente. Ambito: indice dei materiali italiani e pubblicazione GitHub Pages del repository pubblico `rickymusu-bit/fisica`.

Autorizzazione: l’utente ha richiesto esplicitamente una pagina di benvenuto con indice solo dei materiali italiani e l’attivazione di GitHub Pages se il repository è pubblico. La visibilità pubblica è stata verificata. Questa richiesta è successiva alla migrazione e autorizza la pubblicazione ora.

Pagina corrente: `index.html`, HTML statico autonomo, senza immagini o dipendenze esterne. Catalogo: otto dispense, tutte verificate con `lang="it"`. Il quiz è escluso per richiesta esplicita successiva dell’utente. La pagina non è un nuovo capitolo didattico.

Pubblicazione: workflow `.github/workflows/pages.yml`, da `main`. `scripts/build_pages.py` controlla i riferimenti della pagina, verifica la lingua e prepara `_site/` con i soli HTML italiani collegati. Nomi e percorsi dei materiali sono conservati. Le traduzioni, il master e i documenti di lavorazione non fanno parte dell’artefatto del sito.

La realizzazione dei contenuti didattici esistenti resta invariata; nessun materiale su Drive viene modificato.

Quiz: escluso dall’indice e dall’artefatto del sito. I quattro file sono ora nel repository [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz), commit `f102b5583ff96c6574a32e32f20129535f6b9341`; gli hash sono stati verificati sul ramo remoto prima di rimuovere le copie dal repository di fisica. La cronologia conserva gli originali.

Verifiche locali: preparazione di nove HTML (indice più otto dispense), riferimenti esistenti, lingua italiana verificata e materiali originali identici tramite SHA-256. Nel browser Chromium sono stati verificati indice, assenza del quiz, navigazione da tastiera e ancore; nessun errore JavaScript e nessuno scorrimento laterale alle larghezze 1440 e 390 px. Anteprime desktop e smartphone ispezionate.

Pubblicazione completata: [sito delle dispense](https://rickymusu-bit.github.io/fisica/), HTTPS attivo, source GitHub Actions. L’utente ha abilitato Pages nelle impostazioni dopo il blocco iniziale dell’API. Il [workflow 38919369107](https://github.com/rickymusu-bit/fisica/actions/runs/38919369107), commit `a57bb06607ec2cbdcd1caabe63955d57625622f6`, ha completato preparazione e deployment con esito positivo.

Verifiche online: homepage e otto dispense rispondono HTTP 200 e il loro SHA-256 coincide con il repository. Il quiz, una traduzione francese, il master e lo stato di lavorazione rispondono HTTP 404, come previsto dalla pubblicazione selettiva. Nel browser Chromium online sono stati verificati indice, assenza del quiz, navigazione per argomenti e adattamento a smartphone senza scorrimento laterale; nessun errore JavaScript. Gli esiti sono in `verifiche-online.json`.

Fase: completata. Ultimo aggiornamento: 2026-10-16 16:54 (Europe/Rome). Prossima operazione: per ogni nuova dispensa italiana aggiorna il relativo collegamento in `index.html`, prepara il sito e verifica il deployment automatico dopo l’integrazione in `main`. Il quiz resta nel proprio repository e non viene pubblicato sul sito di fisica.

## Download delle dispense

Richiesta dell’utente: consentire ai visitatori di scaricare le dispense. Aggiunti otto collegamenti «Scarica HTML» con nomi di file originali, accanto ai collegamenti di lettura. Non vengono duplicate o modificate le dispense. L’attributo HTML `download` usa URL dello stesso sito, senza JavaScript o servizi esterni. Verificati otto download reali nel browser, con nomi corretti e contenuti identici byte per byte agli originali; verificati inoltre attivazione da tastiera e layout senza scorrimento laterale a 390, 768, 1024 e 1440 px. Gli originali e i percorsi restano invariati. La pubblicazione aggiornata segue il workflow automatico dopo l’integrazione in `main`. Aggiornamento: 2026-10-16 17:03 (Europe/Rome).


## Revisione editoriale delle dispense

Aggiornamento: 2026-10-16 18:50 (Europe/Rome). Master v46. Revisione richiesta dall’utente e autorizzata con «Vai»: otto nuove versioni italiane, 118 quesiti conservati nelle sezioni finali, correzioni delle immagini e del grafico sul calore. `index.html` aggiorna lettura e download. `site-redirects.json` e `scripts/build_pages.py` generano otto pagine di reindirizzamento dai precedenti URL, conservando query e frammenti; le vecchie versioni integrali restano nella cronologia Git.

Build verificata con nove HTML correnti e otto reindirizzamenti. Le prove browser e gli otto download effettivi sono in [revisione-blog-browser.json](../revisione-blog-browser.json); i file sono identici alle nuove versioni controllate. Nessun quiz o traduzione aggiunto. Pubblicazione completata e verificata: commit `6cac15c15571f6ed7e21f41d91bf659fb99475d2`, [workflow riuscito](https://github.com/rickymusu-bit/fisica/actions/runs/38935850257). Homepage, nuove dispense e reindirizzamenti sono identici ai file verificati; master, lavorazione, traduzione campione e quiz rispondono 404. [Rapporto online](revisione-blog-online.json). Il browser online dell’ambiente non ha superato il controllo del certificato; le prove browser complete sono locali sugli stessi file. Le richieste HTTPS di confronto hanno mantenuto attiva la verifica TLS. Nessun intervento pendente.

Conclusione della revisione: 2026-10-16 19:00 (Europe/Rome). Per il prossimo lavoro partire da `main`; i rami temporanei possono essere rimossi soltanto dopo averne verificato l’integrazione.


## Tasto per tornare all’indice

Aggiornamento: 2026-10-16 19:30 (Europe/Rome). Richiesta esplicita dell’utente. Inseriti due collegamenti all’indice generale in ogni dispensa italiana, all’inizio e alla fine. Destinazione `https://rickymusu-bit.github.io/fisica/#indice`, valida anche dalle copie scaricate. Versioni, letture e download aggiornati secondo D2; sedici URL precedenti reindirizzati direttamente alle versioni attuali, senza catene. Master v46 invariato. Modifica completata e verificata: [esiti](ritorno-indice.json). Test a 1440 e 390 px senza overflow, tasti di almeno 44 px, focus visibile e ritorno tramite Invio e clic. La homepage pubblica è stata sostituita con una copia locale soltanto nel test di navigazione; la destinazione HTTPS reale viene controllata alla pubblicazione. File sotto 20 MB; nessuna immagine aggiunta o compressa. Pubblicazione automatica tramite il workflow Pages da `main`, come richiesto dall’utente.


## Regola per i capitoli futuri

Aggiornamento: 2026-10-16 19:40 (Europe/Rome). L’utente richiede che i tasti appena introdotti siano presenti in tutti i capitoli futuri. Regola consolidata nel [master](../../MASTER_PROMPT.md) **v47**, sezione A6: ritorno all’indice generale all’inizio e prima del piè di pagina, collegamento HTTPS utilizzabile anche dai file scaricati con Internet, stile approvato, area di almeno 44 px e focus da tastiera visibile. D1 richiama il controllo dei tasti. Tutte le altre regole e intestazioni del master sono preservate e il confronto inverso delle tre modifiche è identico alla v46. Intervento concluso; nessun HTML o file di pubblicazione modificato. Per i nuovi capitoli applicare A6 durante la realizzazione e D1 prima della consegna.


## Nomi stabili e versioni interne

Aggiornamento: 2026-10-16 21:16 (Europe/Rome). L’utente autorizza i nomi stabili per tutti i file del repository: rinominate 16 dispense (8 italiane e 8 traduzioni), con contenuto e versione interna identici. Master aggiornato a v48; AGENTS allineato. Indice e download puntano ai nomi stabili; 24 indirizzi italiani precedenti reindirizzati direttamente, mantenendo query e frammento. Le traduzioni restano nel repository e non vengono pubblicate. Master, stati e risorse avevano già nomi senza versioni o date e mantengono i percorsi. Gli inventari e gli esiti storici conservano i nomi effettivamente verificati allora; i collegamenti Markdown correnti sono aggiornati. [Mappa e integrità](nomi-stabili.json). Rinomina completata e verificata: identità SHA-256 dei 16 file, collegamenti locali, build selettiva in italiano, otto letture dall’indice, otto download reali con nomi stabili e otto reindirizzamenti con query e frammenti conservati. La build controlla tutte le 24 destinazioni, senza catene. Indice verificato a 1440 e 390 px. Pubblicazione tramite il workflow Pages dopo l’integrazione in `main`.


## Rimozione dei reindirizzamenti

Aggiornamento: 2026-10-16 21:24 (Europe/Rome). L’utente richiede esplicitamente di cancellare i reindirizzamenti perché i vecchi link non sono stati condivisi. Rimossi i 24 alias, la mappa `site-redirects.json` e la relativa generazione dalla build. Master v49 e AGENTS allineati all’eccezione esplicita. La build pubblica soltanto `index.html` e le otto dispense italiane con nomi stabili; HTML, versioni e download non modificati. I riferimenti ai reindirizzamenti negli inventari precedenti descrivono le verifiche storiche e non la configurazione corrente. Verifica locale: artefatto composto da nove HTML correnti e `.nojekyll`, senza vecchi nomi. Pubblicazione tramite il workflow Pages da `main`; verificare HTTP 404 sui 24 vecchi percorsi e HTTP 200 sui nove attuali.


## Tema Mac applicato alla home

Aggiornamento: 17 ottobre 2026. Richiesta esplicita: «Applica il nuovo tema alla home».

Realizzato `index.html` v1 nel ramo dedicato `tema/home-mac`, derivato da `main` (`55f9360fe17a5d058b60650c7a41606686c17543`). Riferimento: tema e anteprima v6 approvati in `istruzioni/tema-mac` (`cc7ab4aad36c88e4fda6ee1ad59208cfd88bca36`). Applicati palette bianca/grigia, bordi neri, ombre nette, intestazioni delle finestre e Lexend incorporato con licenza SIL OFL 1.1. Conservati integralmente i testi, le ancore, gli otto collegamenti di lettura e gli otto download di main. Le altre lavorazioni presenti in istruzioni/tema-mac restano nel loro ramo.

Controlli Chromium superati a 320, 390, 768, 1024 e 1440 px: font incorporato caricato, nessuno scorrimento orizzontale, ancore native, salto al catalogo tramite tastiera, otto coppie lettura/download e pulsanti di almeno 44 px. Provato con JavaScript disabilitato; nessuna dipendenza esterna. Tutte le destinazioni risultano presenti nell’albero main; attributi dei link e testo originale confrontati e identici. Ispezionate le anteprime a 390 e 1440 px. Esiti in `verifiche-home.json`. Non ripetuti download delle dispense, i cui file e collegamenti sono invariati.

Fase: modifica verificata e pronta per revisione tramite pull request. La pubblicazione segue il workflow esistente dopo l’integrazione in main.
