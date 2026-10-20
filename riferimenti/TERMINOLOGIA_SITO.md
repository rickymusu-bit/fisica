# Terminologia del sito

Versione v8 — 20 ottobre 2026. La specifica `lavorazione/sito/PIANO_IMPLEMENTAZIONE_STRINGHE.md` e la richiesta corrente sostituiscono le precedenti denominazioni dell’interfaccia. Le approvazioni di contenuto e la cronologia restano conservate in Git e negli stati.

| Elemento | Nome corrente |
| --- | --- |
| Sito | **Stringhe** |
| Sottotitolo | **L’essenziale della Fisica** |
| Raggruppamento | Area tematica |
| Contenuto autonomo | Articolo |
| Parte di un articolo | Sezione |
| Catalogo separato e ricercabile | Tutti gli articoli |
| Ritorno al catalogo dagli articoli | ← Articoli |
| Comando interno | Indice |
| Titolo dell’indice aperto | Indice dell’articolo |
| Navigazione in sequenza | Articolo precedente / Articolo successivo |
| Attribuzioni | Crediti e licenze |

La home conserva i quattro accessi Tutti gli articoli / Mi sento fortunato / Quiz / Lingua. La scelta casuale e il catalogo comprendono esattamente gli articoli ammessi da `pubblicazione.json`; la sola lingua disponibile è Italiano. Il selettore del tema è un controllo separato: Automatico / Chiaro / Scuro.

La pagina Quiz presenta esclusivamente il futuro generatore di quiz di verifica sugli argomenti scelti dall’utente. Non integra né presenta come propria funzione il progetto autonomo «Chi vuol essere rimandato».

La barra degli articoli conserva Home / Articoli / Scarica / Lingua, il tema e l’indice interno. Online usare collegamenti relativi a `index.html`, `articoli.html`, `crediti.html` per mantenere il ramo corrente. Nei documenti scaricati `data-site-path` e il componente comune forniscono il fallback a `https://rickymusu-bit.github.io/fisica/`. Non ripristinare gli indirizzi dismessi.

La scritta sopra il titolo dell’articolo è il nome esatto dell’area tematica nel catalogo. Nella home mostrare soltanto il nome del raggruppamento, senza ripetere «Area tematica». Note, Ingrandisci l’immagine, Torna all’inizio e Crediti di tutti gli articoli conservano le etichette approvate.

Il modello canonico è `riferimenti/TEMA_DISPENSE.html` v12. Riutilizza i componenti incorporati del tema Stringhe, derivati da `identita/tema-stringhe.css`, `tema-init.js`, `tema-controlli.js` tramite `scripts/stringhe_theme.py`. Il generatore e il modello devono restare allineati (`scripts/sync_stringhe_theme.py --check`). Le onde decorative sono due curve distinte in opposizione di fase, non una risultante né un’onda stazionaria scientifica. Scelta dell’utente: reticolo regolare e sinusoidi di uguale ampiezza. Approvata la disposizione verticale ai lati delle card e dell’unico contenitore continuo del corpo degli articoli. Le alternative restano nella pagina di confronto storico.

Il logo rimane esattamente l’onda circolare animata a quattro creste, nodi fissi e ampiezza 20: `identita/logo-materia-oscura.svg`, con GIF solo dove necessaria. Il nome storico dei file non cambia. Pausa/ripresa e movimento ridotto sono obbligatori; garantire contrasto in entrambi i temi senza modificare la geometria. Le venti fotografie approvate rimangono intere e casuali, con didascalie e alt coerenti.

Crediti centralizzati nel registro unico e snapshot autonomi offline; OFL incorporata. Nessuna sostituzione di avvisi di licenza o fonti scientifiche. Il punto centrato è riservato alla moltiplicazione, mai ai separatori dell’interfaccia. Gli articoli esclusi e i loro sorgenti non ricevono questo aggiornamento.
