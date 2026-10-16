# Stato — Pagina di benvenuto e GitHub Pages

Master iniziale consultato: v45; versione corrente v46 dopo la separazione del quiz. Ambito: indice dei materiali italiani e pubblicazione GitHub Pages del repository pubblico `rickymusu-bit/fisica`.

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
