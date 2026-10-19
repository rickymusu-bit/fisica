# Stato — Crediti unificati

Versione v2 · 19 ottobre 2026 (Europe/Rome).

Approvazione esplicita «Vaai» alla proposta di un solo comando «Crediti e licenze» che apre sempre lo snapshot incorporato del documento, anche offline, con «Crediti di tutti gli articoli» verso la pagina generale. Include applicazione e aggiornamento pubblico della home e degli otto articoli ammessi, tema canonico v9 e istruzioni future. Master v63, terminologia v6.

Ramo tema/crediti-unificati derivato da main 8a7e6712b9235153aed1a8f1633a32e49f6ab4c8. Sorgenti storici/non pubblicati preservati byte per byte: il renderer conserva il loro componente preesistente. Registro unico, tutti gli avvisi e OFL integrale mantenuti. Link generale assoluto funziona anche dal file locale. Fallback senza JavaScript tramite ancora :target mantenuto. Versioni delle pagine coinvolte incrementate. Nessuna modifica al manifest di pubblicazione.

Implementazione e sei test del registro superati; build e controllo crediti superati. Controlli browser, confronto dei contenuti e pubblicazione in corso.

Controlli completati: dieci documenti con comando unico (home, otto articoli e modello), 15 documenti non pubblicati identici byte per byte al main precedente. Confronto di tutti gli avvisi e del testo OFL, immagini e contenuto esterno al componente: invariati salvo versioni/date e il controllo di esistenza di un elemento della vecchia copertina nella home, necessario per non generare un errore JS quando la foto non è disponibile offline. Sei test del registro superati.

Undici prove Chromium (tutti i documenti pubblici a 390 px, home/articolo 3 anche a 1280): HTML completo in memoria e rete disabilitata, apertura/chiusura X ed Esc, ritorno focus, link generale assoluto, zero richieste esterne e zero errori JS. Fallback senza JavaScript provato per home/articolo. Apertura diretta file: bloccata dalla policy del browser dell’ambiente; non dichiarata eseguita. Report verifiche.json. Anteprime dei crediti desktop/mobile ispezionate. Bozza HTML articolo 3 allineata alla v6 e verifiche statiche superate.

Prossimo passo: integrare il ramo e verificare il rilascio pubblico già autorizzato.

## Pubblicazione completata

PR #41 integrata al commit 99cf11eaeae430f5d6c2c5280eb54c13b8a94dd2; workflow Pages 39309524643 concluso con successo. Verifica HTTPS del 19 ottobre 2026, 19:18 UTC: home v23, otto articoli e pagina crediti v2, dieci risposte HTTP 200 identiche byte per byte ai documenti provati. Accesso unico e collegamento generale presenti su tutte le pagine interessate; report verifiche-pubbliche.json con versioni e SHA-256.

Link di consegna https://rickymusu-bit.github.io/fisica/?v=23 per richiamare la home aggiornata. Richiesta completata: stesso accesso online/offline, attribuzioni e OFL conservate integralmente, sorgenti esclusi invariati.
