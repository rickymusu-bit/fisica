# Materia Oscura

Guida pratica per fare luce sulla Fisica.

**Sito:** https://rickymusu-bit.github.io/fisica/

La home italiana `index.html` raccoglie soltanto i tre articoli conformati: Stati della materia, Passaggi di stato e Irraggiamento. La barra superiore contiene il selettore della lingua in alto a destra, con la sola voce «Italiano». Il comando «Articoli» in alto a sinistra apre un pannello laterale con il catalogo, chiudibile con ×, Esc o clic fuori dal pannello; gli indirizzi con `#indice` o l’ancora di un argomento lo aprono direttamente. Senza JavaScript il catalogo resta accessibile. I download mostrano «Scarica», un’icona e la dimensione del file (kB/MB decimali, byte esatti nel tooltip e nell’etichetta accessibile), calcolata durante la build. Il sito pubblica soltanto contenuti in italiano.

La copertina viene scelta a caso tra le venti immagini di `copertine/`; viene mostrata con la sola didascalia, senza un titolo sovrapposto. I crediti sono accessibili nella sezione apribile della home.

GitHub Pages pubblica da `main` attraverso `.github/workflows/pages.yml`. Eseguire `python3 scripts/build_pages.py` per verificare i collegamenti e preparare `_site/`: la home italiana, i tre articoli conformati e le copertine selezionate. I documenti di lavorazione non vengono pubblicati.

Per aggiornare l’elenco italiano, rispettare `pubblicazione.json` e modificare `index.html` in modo coerente. I sette articoli sospesi restano conservati nel repository, esclusi dalla pubblicazione e da ogni aggiornamento fino a richiesta esplicita dell’utente. La build rifiuta cataloghi o collegamenti verso articoli non ammessi. `scripts/home_italian.py` genera il pannello laterale e i comandi durante la build; la raccolta delle copertine è gestita da `scripts/home_covers.py` e dal relativo manifest. I materiali delle altre lingue restano conservati nel repository, esclusi dalla pubblicazione.

Prima di lavorare leggere `MASTER_PROMPT.md`, `AGENTS.md` e lo stato pertinente in `lavorazione/`. Verificare la build prima di integrare le modifiche in `main`.

La pubblicazione è attiva con **Settings → Pages → Source → GitHub Actions**. Per avviarla manualmente usare **Actions → Pubblica Praticamente la Fisica → Run workflow** sul ramo `main`.

Il quiz resta separato nel repository [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz).

La terminologia della navigazione è definita nel master e nel modello autonomo: «Articoli» per la raccolta, «← Tutti gli articoli» per tornarvi, «Indice» e «Indice dell’articolo» per il contenuto aperto, «Articolo precedente/successivo», «Note», «Crediti delle immagini» e «Licenza del carattere».

I vecchi indirizzi della dispensa unificata sono dismessi e non vengono più pubblicati o reindirizzati. Sono registrati nel manifest soltanto per verificarne l’assenza dal sito.

Identità e terminologia approvate della home in `riferimenti/TERMINOLOGIA_SITO.md`: titolo «Materia Oscura», sottotitolo «Guida pratica per fare luce sulla Fisica»; i gruppi mostrano soltanto il proprio nome, senza l’etichetta «Area tematica».

Il logo animato accanto al titolo è una stringa chiusa nera su fondo trasparente, con pausa/ripresa e rispetto del movimento ridotto. SVG animato, SVG statico e GIF riutilizzabili sono salvati in [`identita/`](identita/README.md); la home incorpora lo stesso originale vettoriale durante la build.
