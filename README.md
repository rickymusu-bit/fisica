# Praticamente la Fisica

Guida essenziale a tutto ciò che ci circonda.

**Sito:** https://rickymusu-bit.github.io/fisica/

La home italiana `index.html` raccoglie nove articoli per argomento, compreso Irraggiamento. Nella home italiana la barra superiore contiene soltanto il menu delle lingue. Il catalogo è inizialmente nascosto e si apre con «Esplora gli articoli»; gli indirizzi con `#indice` o l’ancora di un argomento lo aprono direttamente. Senza JavaScript il catalogo resta accessibile. I download mostrano un’icona e la dimensione del file (kB/MB decimali, byte esatti nel tooltip e nell’etichetta accessibile), calcolata durante la build. Le home francese e albanese, generate durante la build, mostrano ciascuna i quattro articoli già disponibili nella rispettiva lingua. Non vengono create traduzioni automatiche degli articoli.

La copertina viene scelta a caso tra le venti immagini di `copertine/`; viene mostrata con la sola didascalia, senza un titolo sovrapposto. I crediti sono accessibili nella sezione apribile della home.

GitHub Pages pubblica da `main` attraverso `.github/workflows/pages.yml`. Eseguire `python3 scripts/build_pages.py` per verificare i collegamenti e preparare `_site/`: le tre home, gli articoli nelle lingue previste e le copertine selezionate. I documenti di lavorazione non vengono pubblicati.

Per aggiornare l’elenco italiano, modificare `index.html`. Questo file resta il template condiviso; `scripts/home_italian.py` applica le modifiche di interfaccia alla sola home italiana durante la build, lasciando invariate le home francese e albanese. Per le home francese e albanese, aggiornare `lingue/home.json`, collegando soltanto versioni realmente presenti nel repository. Le home tradotte vengono generate da `scripts/home_languages.py`; la raccolta delle copertine è gestita da `scripts/home_covers.py` e dal relativo manifest.

Prima di lavorare leggere `MASTER_PROMPT.md`, `AGENTS.md` e lo stato pertinente in `lavorazione/`. Verificare la build prima di integrare le modifiche in `main`.

La pubblicazione è attiva con **Settings → Pages → Source → GitHub Actions**. Per avviarla manualmente usare **Actions → Pubblica Praticamente la Fisica → Run workflow** sul ramo `main`.

Il quiz resta separato nel repository [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz).
