# Stringhe

**L’essenziale della Fisica**

[Sito](https://rickymusu-bit.github.io/fisica/) — [Catalogo dei capitoli](https://rickymusu-bit.github.io/fisica/articoli.html) — [Crediti e licenze](https://rickymusu-bit.github.io/fisica/crediti.html)

Stringhe raccoglie capitoli visuali di fisica in italiano. I capitoli attuali appartengono alla macro categoria **Termologia**; elenco e ordine sono definiti in [`pubblicazione.json`](pubblicazione.json) e nel catalogo sorgente di [`index.html`](index.html).

La home offre **Tutti i capitoli**, **Mi sento fortunato** e **Quiz** nelle card; la barra superiore contiene soltanto lingua e tema chiaro/scuro. Il catalogo ha ricerca e filtro per area tematica; la scelta casuale comprende soltanto i capitoli pubblicati. Quiz presenta il futuro generatore di verifiche per argomento, distinto dal progetto nel repository [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz).

## Capitoli e tema comune

I capitoli sono HTML autonomi, con immagini, font e crediti incorporati. La barra comprende Home, Capitoli, Scarica, Indice, Lingua e il menu Chiaro/Scuro. Il tema predefinito è Scuro e la scelta dell’utente viene conservata quando lo storage è disponibile. I comandi mostrano il nome della funzione al passaggio del puntatore, al focus da tastiera e al tocco. Le figure ingrandibili usano un comando a icona in basso a sinistra, utilizzabile anche da tastiera e senza JavaScript.

Il riferimento grafico è [`riferimenti/TEMA_DISPENSE.html`](riferimenti/TEMA_DISPENSE.html); la terminologia corrente è in [`riferimenti/TERMINOLOGIA_SITO.md`](riferimenti/TERMINOLOGIA_SITO.md). Il logo circolare ha due curve in opposizione di fase, nera e blu, con pausa/ripresa e rispetto del movimento ridotto. I percorsi storici dei file del logo rimangono stabili; i dettagli sono in [`identita/README.md`](identita/README.md).

La copertina della home cambia casualmente tra le venti immagini scelte, con foto intera, testo alternativo e didascalia. Il registro unico delle attribuzioni è [`risorse/crediti.json`](risorse/crediti.json), descritto in [`risorse/README.md`](risorse/README.md). Gli avvisi e la licenza OFL di Lexend sono disponibili anche nelle copie scaricate. I crediti generali riconoscono l’aiuto di Codex e ChatGPT.

## Sviluppo e verifiche

Prima di lavorare leggere [`AGENTS.md`](AGENTS.md), [`MASTER_PROMPT.md`](MASTER_PROMPT.md) e lo stato pertinente in `lavorazione/`. Lavorare su un ramo dedicato e presentare l’anteprima corrente prima dell’integrazione e della pubblicazione.

```sh
python3 scripts/sync_stringhe_theme.py --check
python3 scripts/credits.py --check
python3 scripts/build_pages.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

`scripts/strings_site.py` genera portale, catalogo, pagina Quiz e navigazione comune. `scripts/build_pages.py` prepara `_site/` e verifica che catalogo e collegamenti rispettino il manifest. Per aggiungere o rimuovere un capitolo aggiornare insieme `pubblicazione.json`, il catalogo e i rimandi precedente/successivo. Le fonti scientifiche e gli originali restano nei materiali di lavorazione; documenti storici, traduzioni e capitoli esclusi conservano il proprio stato nel manifest.

Le componenti condivise sono in `identita/`; `scripts/sync_stringhe_theme.py` sincronizza modello, confronto e pagina dei crediti. Aggiornare le attribuzioni tramite il registro unico e il renderer, senza riscrivere manualmente gli avvisi generati o migrare in blocco i sorgenti esclusi.

## Pubblicazione

GitHub Pages pubblica da `main` attraverso [`.github/workflows/pages.yml`](.github/workflows/pages.yml), dopo l’approvazione esplicita dell’anteprima. L’integrazione delle modifiche pertinenti avvia il workflow **Pubblica Stringhe**; è disponibile anche da **Actions → Pubblica Stringhe → Run workflow**. Il sito pubblica soltanto i capitoli ammessi e i servizi previsti dalla build; le bozze di lavorazione restano nel repository.
