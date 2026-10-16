# Stato — Pagina di benvenuto e GitHub Pages

Master consultato: v45. Ambito: indice dei materiali italiani e pubblicazione GitHub Pages del repository pubblico `rickymusu-bit/fisica`.

Autorizzazione: l’utente ha richiesto esplicitamente una pagina di benvenuto con indice solo dei materiali italiani e l’attivazione di GitHub Pages se il repository è pubblico. La visibilità pubblica è stata verificata. Questa richiesta è successiva alla migrazione e autorizza la pubblicazione ora.

Pagina corrente: `index.html`, HTML statico autonomo, senza immagini o dipendenze esterne. Catalogo: otto dispense, tutte verificate con `lang="it"`. Il quiz è escluso per richiesta esplicita successiva dell’utente. La pagina non è un nuovo capitolo didattico.

Pubblicazione: workflow `.github/workflows/pages.yml`, da `main`. `scripts/build_pages.py` controlla i riferimenti della pagina, verifica la lingua e prepara `_site/` con i soli HTML italiani collegati. Nomi e percorsi dei materiali sono conservati. Le traduzioni, il master e i documenti di lavorazione non fanno parte dell’artefatto del sito.

La realizzazione dei contenuti didattici esistenti resta invariata; nessun materiale su Drive viene modificato.

Quiz: escluso dall’indice e dall’artefatto del sito. I quattro file sono ora nel repository [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz), commit `f102b5583ff96c6574a32e32f20129535f6b9341`; gli hash sono stati verificati sul ramo remoto prima di rimuovere le copie dal repository di fisica. La cronologia conserva gli originali.

Verifiche locali: preparazione di nove HTML (indice più otto dispense), riferimenti esistenti, lingua italiana verificata e materiali originali identici tramite SHA-256. Nel browser Chromium sono stati verificati indice, assenza del quiz, navigazione da tastiera e ancore; nessun errore JavaScript e nessuno scorrimento laterale alle larghezze 1440 e 390 px. Anteprime desktop e smartphone ispezionate.

Attivazione GitHub Pages bloccata: la chiamata `POST /repos/rickymusu-bit/fisica/pages` con `build_type=workflow` è rifiutata con HTTP 403, «Resource not accessible by integration». Occorre impostare manualmente Settings → Pages → Source → GitHub Actions, oppure autorizzare la connessione alla gestione di Pages. La pagina e il workflow sono integrati in `main` tramite la PR #2. La preparazione del sito è riuscita anche su GitHub Actions; il deployment del run 38918981613 è fallito con 404 perché Pages non è abilitato. Verificare il deployment e i link online appena il servizio è abilitato. Non dichiarare il sito pubblicato prima della conferma del deployment.
