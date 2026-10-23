# Stato — Video YouTube su richiesta

Aggiornamento: 23 ottobre 2026 (Europe/Rome). Master v69.7; modello Stringhe v23.
Fase: implementazione completata, verifiche superate, anteprima di sviluppo pronta; PR #63 in bozza.

## Autorizzazione e ambito

Richiesta dell’utente: «Ok. Implementa tutte queste cose. Poi mettilo nelle regole. Poi ricontrolla tutti gli altri capitoli in cerca di video e aggiornali secondo le nuove regole».
Il comando autorizza il componente nel capitolo corrente, la modifica delle regole e la revisione circoscritta dei video degli altri capitoli, compresi i sorgenti storici e tradotti. Non autorizza merge o Pages: resta necessaria l’approvazione dell’anteprima corrente secondo AGENTS.md/B5. Il lavoro prosegue sul ramo dedicato derivato da main della PR #63.
Stima comunicata: 25–45 minuti, carico basso/moderato per browser e anteprime, senza simulazioni o immagini nuove.

## Componente e regole

Fonti uniche: scripts/youtube_videos.py, identita/youtube-videos.css e youtube-videos.js. Il renderer comune richiama il componente; modello autonomo v23 sincronizzato. Migrazione riproducibile con scripts/migrate_youtube_videos.py e controllo --check. Il generatore del capitolo 3 usa direttamente lo stesso componente, senza dipendere dalle vecchie miniature o da immagini nei sorgenti storici.

Prima del clic: titolo e icona costruita con CSS, nessuna miniatura o fotogramma, nessun iframe, API, richiesta o preconnessione a YouTube. «Carica il video» è un pulsante nativo utilizzabile da tastiera. Al clic crea un solo iframe youtube-nocookie.com con autoplay=0, playsinline=1, comandi nativi, schermo intero, referrer policy strict-origin-when-cross-origin. URL originali e timestamp conservati. Minimo del lettore 200 × 200 px; 16:9 quando lo spazio lo consente.

«Apri su YouTube» resta fuori dall’iframe e sempre disponibile. «Chiudi il lettore» elimina l’iframe, interrompe la riproduzione e riporta il focus al pulsante. Senza JavaScript rimangono titolo e collegamento esterno. Offline il clic mostra un avviso senza creare iframe. Se il servizio è bloccato o non consente l’incorporamento, il collegamento resta utilizzabile. Non promettere l’embed dai file locali né l’assenza di pubblicità, suggerimenti o trattamento di dati dopo il clic.

MASTER_PROMPT.md v69.7: C5 sostituito, D1 adeguato, richiamo in A6 e terminologia dei riquadri in A3. AGENTS.md richiama la nuova regola e il modello v23. I vecchi divieti di iframe YouTube e l’obbligo delle miniature sono superati dalla richiesta corrente.
Riferimenti ufficiali consultati: https://developers.google.com/youtube/player_parameters e https://support.google.com/youtube/answer/171780?hl=it .

## Audit e documenti aggiornati

Controllati tutti i 28 HTML di capitoli alla radice: sei con video YouTube, dieci occorrenze complessive. Nessun altro tag video o iframe remoto rilevato. [Inventario con URL e impronte](inventario.json).

| Documento | Video | Stato di pubblicazione conservato |
| --- | --- | --- |
| conduzione_it.html | 1 | Ammesso, revisione soltanto sul ramo |
| potenze_dieci_notazione_scientifica_it.html | 2 | Nuovo capitolo ancora fuori dal manifest |
| potenza_termica_conduzione_convezione_it.html | 1 | Sorgente escluso |
| sistema_internazionale_notazione_it.html | 2 | Sorgente escluso |
| sistema_internazionale_notazione_fr.html | 2 | Traduzione storica non pubblicata |
| sistema_internazionale_notazione_sq.html | 2 | Traduzione storica non pubblicata |

Conservati URL esatti, didascalie scientifiche, introduzioni e parti estranee ai video. Rimossi soltanto i vecchi inviti ad aprire la miniatura; testi del componente coerenti con la lingua del documento. Versioni interne incrementate senza aggiornare la data editoriale per questa modifica funzionale. Copie bozza.html correnti di Conduzione e capitolo 3 riallineate, insieme ai segnaposto video delle rispettive bozze testuali. I capitoli senza video sono byte per byte invariati. Manifest, ordine, catalogo e pubblicazione invariati; nessun vecchio indirizzo ripristinato.

Crediti: rimosse soltanto le occorrenze delle miniature non più utilizzate; schede e fonti storiche conservate. Snapshot degli interessati e pagina generale rigenerati dal registro. La pagina pubblica continua a comprendere soltanto home e capitoli ammessi. La copertina di Giove resta documentata. Non restano miniature senza attribuzione nei dieci riquadri migrati.

## Verifiche

- Tema canonico --check, credits.py --check e build Pages superati. Registro: 30 documenti, 148 schede, 221 asset.
- 17 test unitari superati, compresi tre nuovi test per URL/timestamp, rifiuto degli host non validi, assenza di media remoti iniziali, conservazione del link esatto e idempotenza.
- Browser specifico: 24 combinazioni (sei documenti, 390/1440 px, chiaro/scuro). Nessuna richiesta ai domini video prima del clic; iframe creato al clic, nessun autoplay, timestamp, minimo del player, fallback e chiusura/focus verificati. Nessun overflow o errore JavaScript. Tutti i documenti verificati anche senza JavaScript; offline e connessione bloccata provati. [Rapporto](verifiche.json).
- La verifica del ciclo iframe intercetta le richieste del player con una risposta di test; non certifica la riproduzione dei filmati. Le schermate mostrano esclusivamente i riquadri reali prima del clic, mai un lettore simulato. Il tentativo di leggere i metadati ufficiali oEmbed è stato bloccato dal proxy dell’ambiente con 403: [esiti](servizio.json). Non dichiarare una verifica della riproduzione remota che non è avvenuta.
- Suite completa del portale: 180 combinazioni pagina/viewport/tema e 20 copertine, nessun errore JavaScript. [Rapporto conservato](verifiche-portale.json); le schermate estranee a questa revisione non vengono riscritte nel repository.
- Conservazione delle parti estranee verificata contro il commit di partenza; per i cinque sorgenti precedenti il risultato deriva esattamente dal migratore, salvo versione e crediti. Manifest e 22 documenti senza video invariati.

Un primo controllo ha individuato un overflow del nuovo riquadro con il minimo di altezza del player: corretta la larghezza esplicita e il box sizing prima dei test finali. Migliorato il contrasto dell’icona. Per le acquisizioni fermato lo scorrimento animato del tema, senza modificare il comportamento del prodotto.

## Consegna e prossimo passaggio

[Pagina interattiva di revisione](index.html): tre video rappresentativi, collegamenti nei capitoli e schermate desktop/mobile. Tutti i sei documenti sono apribili dal ramo isolato. Generatore della pagina: scripts/preview_youtube_videos.py. La cartella di revisione non entra nell’output Pages.
Il nuovo standard è implementato e salvato sul ramo. Attendere l’approvazione della nuova anteprima prima di integrare main o pubblicare; non dedurla dall’autorizzazione a implementare. Il funzionamento del filmato sul servizio dipende dalle restrizioni di YouTube e dalla connessione; il link esterno resta il percorso alternativo.

Documento di partenza dell’audit: commit d8f1492 del ramo della PR #63; il manifest resta identico a questo riferimento. La verifica completa del portale è stata eseguita dopo l’ultima modifica del codice del lettore, con esito positivo. Le schermate dei riquadri sono state riacquisite con scorrimento fermo e ispezionate.

## Salvataggio remoto verificato

Implementazione caricata al commit dbde455d67ce42427e517ecdd3486381f7c79bfc della PR #63. [Anteprima interattiva corrente](https://raw.githack.com/rickymusu-bit/fisica/dbde455d67ce42427e517ecdd3486381f7c79bfc/lavorazione/sito/video_youtube/index.html). Pagina di revisione, capitolo 3 e Conduzione rispondono HTTPS 200 e sono identici byte per byte ai file locali verificati: [rapporto](verifica-online.json). Il controllo automatico remoto del portale è stato avviato da GitHub Actions; le verifiche locali complete sono già superate. Il salvataggio successivo di questo rapporto non cambia gli HTML o le schermate. Nessun Pages o merge eseguito.

## Pubblicazione approvata — 23 ottobre 2026

L’utente approva esplicitamente l’anteprima corrente con «Approvo. Fai la pr e pubblica». Autorizzati completamento e merge della PR #63 e deployment Pages; superata l’attesa di approvazione indicata nei resoconti precedenti. Nuovo capitolo HTML v4, contenuto didattico identico all’anteprima v3: aggiunto soltanto il rimando al capitolo successivo. Manifest v12 con 13 capitoli; inserimento al terzo posto dell’area introduttiva, catalogo e pagina dei crediti aggiornati. Navigazione reciproca con Sistema internazionale (v5) e Termodinamica (v13), con copie correnti riallineate e date editoriali conservate. Nessuna riammissione degli HTML storici o tradotti. Verificati contenuti identici al netto di versione/navigazione, navigazione dei 13 capitoli ed esclusioni. Tema, crediti, migrazione video --check, build e 17 test superati. Merge e verifica del deployment da completare.

Suite completa sulla configurazione di pubblicazione: **190 combinazioni pagina/viewport/tema e 20 copertine**, nessun errore JavaScript. Rapporto: `lavorazione/sito/video_youtube/verifiche-portale-pubblicazione.json`. Schermate di controllo temporanee conservate fuori dal repository per evitare riscritture di materiali estranei.

## Rilascio completato — 23 ottobre 2026

[PR #63](https://github.com/rickymusu-bit/fisica/pull/63) pronta e integrata al commit `ffc805cd0b9b82edc40775ffadd69f402f6183d6`, dopo il controllo remoto riuscito [39919713921](https://github.com/rickymusu-bit/fisica/actions/runs/39919713921). [Deployment Pages 39920157184](https://github.com/rickymusu-bit/fisica/actions/runs/39920157184) concluso con successo. [Capitolo pubblicato](https://rickymusu-bit.github.io/fisica/potenze_dieci_notazione_scientifica_it.html), HTML v4, terzo dell’area introduttiva.

Verifica HTTPS successiva al deployment: 17 URL pubblici (13 capitoli e quattro pagine di servizio) HTTP 200 e identici byte per byte alla build locale; 12 URL esclusi, storici o riservati all’anteprima rispondono HTTP 404. Navigazione reciproca dei 13 capitoli corretta; capitolo nuovo e Conduzione hanno rispettivamente due e un riquadro video, senza iframe iniziali. [Rapporto](https://github.com/rickymusu-bit/fisica/blob/main/lavorazione/sito/video_youtube/verifica-pubblicazione-online.json). Non restano attività di pubblicazione pendenti per questo incarico. La riproduzione remota dei filmati resta dipendente dal servizio YouTube; le verifiche non dichiarano un playback remoto non eseguito.
