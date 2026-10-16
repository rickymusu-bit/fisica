# fisica

Materiali didattici di fisica di Riccardo Musumarra.

**Sito:** https://rickymusu-bit.github.io/fisica/

La pagina di benvenuto è `index.html`: raccoglie otto dispense in italiano, organizzate per argomento.

GitHub Pages pubblica da `main` attraverso `.github/workflows/pages.yml`. La preparazione del sito con `python3 scripts/build_pages.py` verifica i collegamenti dell'indice e la lingua degli HTML, poi copia in `_site/` soltanto i materiali collegati, mantenendo nomi e percorsi. Le traduzioni e i documenti di lavorazione restano nel repository.

Per aggiungere o aggiornare un materiale sul sito, modifica il collegamento in `index.html` e verifica la preparazione prima di integrare il lavoro in `main`.

Prima di lavorare leggi `MASTER_PROMPT.md`, `AGENTS.md` e lo stato pertinente in `lavorazione/`.

La pubblicazione è attiva con **Settings → Pages → Source → GitHub Actions**. Se non parte una pubblicazione automatica, esegui **Actions → Pubblica i materiali italiani → Run workflow** sul ramo `main`.

Il quiz è conservato separatamente in [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz) e non viene pubblicato sul sito delle dispense.
