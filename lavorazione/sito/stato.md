# Stato — Pagina di benvenuto e GitHub Pages

Master consultato: v45. Ambito: indice dei materiali italiani e pubblicazione GitHub Pages del repository pubblico `rickymusu-bit/fisica`.

Autorizzazione: l’utente ha richiesto esplicitamente una pagina di benvenuto con indice solo dei materiali italiani e l’attivazione di GitHub Pages se il repository è pubblico. La visibilità pubblica è stata verificata. Questa richiesta è successiva alla migrazione e autorizza la pubblicazione ora.

Pagina corrente: `index.html`, HTML statico autonomo, senza immagini o dipendenze esterne. Catalogo: otto dispense, tutte verificate con `lang="it"`. Il quiz è escluso per richiesta esplicita successiva dell’utente. La pagina non è un nuovo capitolo didattico.

Pubblicazione: workflow `.github/workflows/pages.yml`, da `main`. `scripts/build_pages.py` controlla i riferimenti della pagina, verifica la lingua e prepara `_site/` con i soli HTML italiani collegati. Nomi e percorsi dei materiali sono conservati. Le traduzioni, il master e i documenti di lavorazione non fanno parte dell’artefatto del sito.

La realizzazione dei contenuti didattici esistenti resta invariata; nessun materiale su Drive viene modificato.

Quiz: escluso dall’indice e dall’artefatto del sito. I quattro file sono preparati nel repository locale `/workspace/quiz`, con hash e provenienza, ma la creazione di `rickymusu-bit/quiz` è stata rifiutata da GitHub con «Resource not accessible by integration (createRepository)». In attesa di una destinazione remota accessibile, gli originali in `fisica/quiz/` non vengono rimossi.

Verifiche locali: preparazione di nove HTML (indice più otto dispense), riferimenti esistenti, lingua italiana verificata e materiali originali identici tramite SHA-256. Nel browser Chromium sono stati verificati indice, assenza del quiz, navigazione da tastiera e ancore; nessun errore JavaScript e nessuno scorrimento laterale alle larghezze 1440 e 390 px. Anteprime desktop e smartphone ispezionate.

Attivazione GitHub Pages bloccata: la chiamata `POST /repos/rickymusu-bit/fisica/pages` con `build_type=workflow` è rifiutata con HTTP 403, «Resource not accessible by integration». Occorre impostare manualmente Settings → Pages → Source → GitHub Actions, oppure autorizzare la connessione alla gestione di Pages. Il codice è pronto per l’integrazione in `main`; verificare il deployment e i link online appena il servizio è abilitato. Non dichiarare il sito pubblicato prima della conferma del deployment.
