# Stato — Crediti unificati

Versione v1 · 19 ottobre 2026 (Europe/Rome).

Approvazione esplicita «Vaai» alla proposta di un solo comando «Crediti e licenze» che apre sempre lo snapshot incorporato del documento, anche offline, con «Crediti di tutti gli articoli» verso la pagina generale. Include applicazione e aggiornamento pubblico della home e degli otto articoli ammessi, tema canonico v9 e istruzioni future. Master v63, terminologia v6.

Ramo tema/crediti-unificati derivato da main 8a7e6712b9235153aed1a8f1633a32e49f6ab4c8. Sorgenti storici/non pubblicati preservati byte per byte: il renderer conserva il loro componente preesistente. Registro unico, tutti gli avvisi e OFL integrale mantenuti. Link generale assoluto funziona anche dal file locale. Fallback senza JavaScript tramite ancora :target mantenuto. Versioni delle pagine coinvolte incrementate. Nessuna modifica al manifest di pubblicazione.

Implementazione e sei test del registro superati; build e controllo crediti superati. Controlli browser, confronto dei contenuti e pubblicazione in corso.

Controlli completati: dieci documenti con comando unico (home, otto articoli e modello), 15 documenti non pubblicati identici byte per byte al main precedente. Confronto di tutti gli avvisi e del testo OFL, immagini e contenuto esterno al componente: invariati salvo versioni/date e il controllo di esistenza di un elemento della vecchia copertina nella home, necessario per non generare un errore JS quando la foto non è disponibile offline. Sei test del registro superati.

Undici prove Chromium (tutti i documenti pubblici a 390 px, home/articolo 3 anche a 1280): HTML completo in memoria e rete disabilitata, apertura/chiusura X ed Esc, ritorno focus, link generale assoluto, zero richieste esterne e zero errori JS. Fallback senza JavaScript provato per home/articolo. Apertura diretta file: bloccata dalla policy del browser dell’ambiente; non dichiarata eseguita. Report verifiche.json. Anteprime dei crediti desktop/mobile ispezionate. Bozza HTML articolo 3 allineata alla v6 e verifiche statiche superate.

Prossimo passo: integrare il ramo e verificare il rilascio pubblico già autorizzato.
