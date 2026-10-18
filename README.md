# Praticamente la Fisica

Guida essenziale a tutto ciò che ci circonda.

**Sito:** https://rickymusu-bit.github.io/fisica/

La home italiana `index.html` raccoglie dieci articoli per argomento, compreso Irraggiamento. La barra superiore contiene il selettore della lingua in alto a destra, con la sola voce «Italiano». Il comando «Articoli» in alto a sinistra apre un pannello laterale con il catalogo, chiudibile con ×, Esc o clic fuori dal pannello; gli indirizzi con `#indice` o l’ancora di un argomento lo aprono direttamente. Senza JavaScript il catalogo resta accessibile. I download mostrano un’icona e la dimensione del file (kB/MB decimali, byte esatti nel tooltip e nell’etichetta accessibile), calcolata durante la build. Il sito pubblica soltanto contenuti in italiano.

La copertina viene scelta a caso tra le venti immagini di `copertine/`; viene mostrata con la sola didascalia, senza un titolo sovrapposto. I crediti sono accessibili nella sezione apribile della home.

GitHub Pages pubblica da `main` attraverso `.github/workflows/pages.yml`. Eseguire `python3 scripts/build_pages.py` per verificare i collegamenti e preparare `_site/`: la home italiana, i dieci articoli italiani, i reindirizzamenti della dispensa suddivisa e le copertine selezionate. I documenti di lavorazione non vengono pubblicati.

Per aggiornare l’elenco italiano, modificare `index.html`. `scripts/home_italian.py` genera il pannello laterale e i comandi durante la build; la raccolta delle copertine è gestita da `scripts/home_covers.py` e dal relativo manifest. I materiali delle altre lingue restano conservati nel repository, esclusi dalla pubblicazione.

Prima di lavorare leggere `MASTER_PROMPT.md`, `AGENTS.md` e lo stato pertinente in `lavorazione/`. Verificare la build prima di integrare le modifiche in `main`.

La pubblicazione è attiva con **Settings → Pages → Source → GitHub Actions**. Per avviarla manualmente usare **Actions → Pubblica Praticamente la Fisica → Run workflow** sul ramo `main`.

Il quiz resta separato nel repository [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz).
