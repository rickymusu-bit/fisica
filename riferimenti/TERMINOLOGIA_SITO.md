# Terminologia del sito

Versione v10 — 20 ottobre 2026. La specifica `lavorazione/sito/PIANO_IMPLEMENTAZIONE_STRINGHE.md` e la richiesta corrente sostituiscono le precedenti denominazioni dell’interfaccia. Le approvazioni di contenuto e la cronologia restano conservate in Git e negli stati.

| Elemento | Nome corrente |
| --- | --- |
| Sito | **Stringhe** |
| Sottotitolo | **L’essenziale della Fisica** |
| Raggruppamento | Area tematica |
| Contenuto autonomo | Capitolo |
| Parte di un capitolo | Sezione |
| Catalogo separato e ricercabile | Tutti i capitoli |
| Ritorno al catalogo dai capitoli | ← Capitoli |
| Comando interno | Indice |
| Titolo dell’indice aperto | Indice del capitolo |
| Navigazione in sequenza | Capitolo precedente / Capitolo successivo |
| Attribuzioni | Crediti e licenze |

La home conserva tre accessi: Tutti i capitoli / Mi sento fortunato / Quiz. La lingua resta soltanto nel menu superiore. Novità sostituisce Esplora e Da leggere: tre capitoli ordinati per data editoriale decrescente, a pari data prima quelli più avanti nel catalogo. Ogni card riporta titolo e data, senza numerazione. La scelta casuale e il catalogo comprendono esattamente i capitoli ammessi da `pubblicazione.json`; la sola lingua disponibile è Italiano. Il tema usa un menu Chiaro / Scuro, con icona luna o sole, con default Scuro e preferenza esplicita persistente. Il sistema non cambia la scelta; senza storage o JavaScript resta il default scuro.

La pagina Quiz presenta esclusivamente il futuro generatore di quiz di verifica sugli argomenti scelti dall’utente. Non integra né presenta come propria funzione il progetto autonomo «Chi vuol essere rimandato».

La barra dei capitoli conserva Home / Capitoli / Scarica / Lingua, il tema e l’indice interno. Online usare collegamenti relativi a `index.html`, `articoli.html`, `crediti.html` per mantenere il ramo corrente. Nei documenti scaricati `data-site-path` e il componente comune forniscono il fallback a `https://rickymusu-bit.github.io/fisica/`. Non ripristinare gli indirizzi dismessi.

La scritta sopra il titolo del capitolo è il nome esatto dell’area tematica nel catalogo. Nella home mostrare soltanto il nome del raggruppamento, senza ripetere «Area tematica». Note, Ingrandisci l’immagine, Torna all’inizio e Crediti di tutti i capitoli conservano le etichette approvate.

Il modello canonico è `riferimenti/TEMA_DISPENSE.html` v19. Riutilizza i componenti incorporati del tema Stringhe, derivati da `identita/tema-stringhe.css`, `tema-init.js`, `tema-controlli.js` tramite `scripts/stringhe_theme.py`. Il generatore e il modello devono restare allineati (`scripts/sync_stringhe_theme.py --check`). Le onde decorative sono due curve distinte in opposizione di fase, non una risultante né un’onda stazionaria scientifica. Scelta dell’utente: reticolo regolare e sinusoidi di uguale ampiezza. Approvata la disposizione verticale ai lati delle card e dell’unico contenitore continuo del corpo dei capitoli. Le alternative restano nella pagina di confronto storico.

Il logo mantiene la curva circolare nera originale a quattro creste, nodi fissi e ampiezza 20, affiancata ora da una seconda curva in gradiente blu, di uguale ampiezza e in opposizione di fase. Stesso periodo di quattro secondi e nessuna rotazione. Percorsi stabili `identita/logo-materia-oscura.svg` e `.gif`; entrambi aggiornati dalla richiesta esplicita dell’utente. Pausa/ripresa e movimento ridotto si applicano alle due curve. Nella home titolo, logo e copertina condividono una sola card, senza onde decorative ai lati. Fotografia sotto al titolo su mobile e affiancata su desktop; didascalia sempre allineata al bordo sinistro dell’immagine visibile. Le venti fotografie restano intere e casuali, con didascalie e alt coerenti.

Crediti centralizzati nel registro unico e snapshot autonomi offline; OFL incorporata. Nessuna sostituzione di avvisi di licenza o fonti scientifiche. Il punto centrato è riservato alla moltiplicazione, mai ai separatori dell’interfaccia. I capitoli esclusi e i loro sorgenti non ricevono questo aggiornamento.

Richiesta finale: nessuna scritta sopra «Stringhe» nella home; sottotitolo blu nel tema chiaro e scuro. I percorsi storici e la chiave `articoli` del manifest restano invariati. Ogni pubblicazione su main e Pages richiede l’approvazione esplicita dell’anteprima corrente, secondo B5. Le autorizzazioni precedenti non valgono per revisioni successive.

Titolo, copertina e corpo del capitolo formano una superficie continua: niente divisore, niente rientro del corpo e nessuna interruzione delle onde laterali. Lingua IT e menu del tema restano allineati agli altri comandi.
