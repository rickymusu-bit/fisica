# Terminologia del sito

Versione v7 — 19 ottobre 2026. Scelte approvate dall’utente: gerarchia e identità della home. Le richieste esplicite dell’utente sostituiscono il nome «Praticamente la Fisica» e il ritorno «← Tutti gli articoli» riportati in A6 del master v59; le altre etichette di A6 restano valide.

| Elemento | Nome da usare | Esempio |
| --- | --- | --- |
| Nome del sito e titolo della home | **Materia Oscura** | Materia Oscura |
| Sottotitolo della home | **Guida pratica per fare luce sulla Fisica** | Testo esatto, senza varianti |
| Raggruppamento di articoli per argomento | **Area tematica** | Materia e calore |
| Singolo contenuto autonomo | **Articolo** | Passaggi di stato |
| Parte interna di un articolo | **Sezione** | Applicazioni |

Nella home il comando che apre il catalogo rimane **Articoli**; il catalogo è organizzato per **aree tematiche**. Nella home mostrare soltanto il nome del raggruppamento, per esempio «Materia e calore», **senza scrivere esplicitamente «Area tematica»**. Il termine rimane utile per descrivere la gerarchia nei documenti editoriali. Il numero dei contenuti si esprime in articoli, per esempio «3 articoli».

Il collegamento di ritorno alla raccolta si chiama **← Articoli**, sia all’inizio sia alla fine del documento, su mobile e desktop. Conservare la destinazione `https://rickymusu-bit.github.io/fisica/#indice`.

La scritta sopra il titolo dell’articolo riporta **il nome esatto della sua area tematica nel catalogo della home**, per esempio «Materia e calore» per Stati della materia, Passaggi di stato e Irraggiamento. Mostrare solo il nome, senza il prefisso «Area tematica» e senza usare la dicitura generica «Fisica». Nel modello il testo «Nome dell’area tematica» è un segnaposto da sostituire, non una scritta da pubblicare. Entrambe le scelte fanno parte del tema comune v7 e valgono per gli articoli futuri e le revisioni autorizzate.

Per gli altri elementi continuano a valere i nomi approvati: **Indice dell’articolo**, **Articolo precedente**, **Articolo successivo**, **Note** e **Crediti e licenze**. Evitare «biblioteca» come etichetta alternativa del catalogo e «capitolo» nei comandi pubblici che indicano un articolo.

Applicare questa gerarchia alle nuove pagine e alle revisioni autorizzate; rispettare sempre le esclusioni di `pubblicazione.json`.

Titolo della pagina, titolo visibile e metadati descrittivi della home devono usare «Materia Oscura» e il sottotitolo esatto. Queste scelte valgono per le successive revisioni della home; non cambiano gli argomenti degli articoli.

Il **logo del sito** è esclusivamente l’onda stazionaria approvata, nera su trasparente, a quattro creste e ampiezza 20: `identita/logo-materia-oscura.svg` e `.gif`. Compare accanto al titolo nella home e nella barra in alto a sinistra degli articoli, secondo il componente del tema autonomo v7. Il simbolo φ e i precedenti tentativi non sono alternative del tema. I controlli di pausa/ripresa e movimento ridotto fanno parte della regola grafica.

Le attribuzioni sono centralizzate in `crediti.html` e nel registro unico secondo C1 del master v64. Il tema v10 prevede il solo comando «Crediti e licenze», che apre i crediti incorporati; al loro interno «Crediti di tutti gli articoli» apre la pagina generale, senza sezione finale visibile. Le licenze che richiedono un avviso vicino alla risorsa prevalgono sulla regola grafica.

Il punto centrato è riservato alla moltiplicazione matematica: mai usarlo come separatore, nemmeno tra versione e data. Il tema v10 usa il trattino lungo nel piè di pagina e i due punti nel titolo accessibile del logo.

## Nuova identità e navigazione — 20 ottobre 2026

Nome ufficiale del sito: **Stringhe**. Sottotitolo esatto: **L’essenziale della Fisica**.
La home è un portale con quattro accessi: Tutti gli articoli, Mi sento fortunato, Quiz e Lingua.
Il catalogo è una pagina indipendente `articoli.html`, con ricerca e filtro per area tematica;
la scelta casuale include soltanto gli articoli approvati in `pubblicazione.json`.
La pagina `quiz.html` è preparatoria finché il gioco non è integrato.
Ogni articolo pubblicato offre in testa: Home, Articoli, Scarica, Lingua; resta distinto l'indice interno.
Il tema visivo richiama stringhe vibranti con onde sottili e movimento rispettoso di
`prefers-reduced-motion`. Evitare che la metafora decorativa interferisca con schemi scientifici.
La build applica il tema condiviso tramite `scripts/strings_site.py`, senza aggiornare
i sorgenti degli articoli sospesi. La denominazione precedente e il logo storico
rimangono nei file già esistenti come materiale transitorio finché non sarà approvata
una migrazione dei sorgenti; il sito pubblicato e i nuovi materiali usano Stringhe.
