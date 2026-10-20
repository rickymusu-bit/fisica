# Revisione del tema Stringhe

Implementazione del piano del 20 ottobre 2026 sul ramo `design/stringhe-portale`, PR #43 in bozza. Il tema è una proposta completa da confrontare: la scelta A/A è stata approvata; la posizione dei bordi è ancora in prova. Nessun merge in main né deployment Pages.

## Configurazione ora adottata

L’utente ha scelto **onde verticali**, confermando reticolo regolare e ampiezze uguali. La disposizione è ora attiva nel tema comune e nel modello v12, non soltanto nella dimostrazione. Il corpo dell’articolo conserva un unico contenitore continuo, con curve ai due lati e margini dedicati; formule e figure non ricevono cornici decorative aggiuntive. I confronti e le considerazioni di prova sotto riportati documentano il percorso precedente.

Corpo continuo dell’articolo: [mobile chiaro](schermate/corpo-articolo-390-light.png), [mobile scuro](schermate/corpo-articolo-390-dark.png), [desktop chiaro](schermate/corpo-articolo-1440-light.png), [desktop scuro](schermate/corpo-articolo-1440-dark.png).


## Scelta ricevuta e nuova prova

L’utente ha approvato **reticolo regolare** e **sinusoidi di uguale ampiezza**. La nuova anteprima parte da queste impostazioni, con curve ai lati in verticale; il controllo Posizione permette di tornare al confronto orizzontale. Le altre varianti rimangono disponibili come riferimenti storici.

La disposizione laterale libera i bordi superiore e inferiore e accompagna bene le card alte. Richiede però spazio ai lati: riservati 36 px per lato, con fasce decorative di 24 px. Sui telefoni i pulsanti della dimostrazione sono in colonna per non comprimere le etichette. La posizione verticale resta una proposta da valutare.

Schermate: [mobile chiaro](schermate/laterali-390-light.png), [mobile scuro](schermate/laterali-390-dark.png), [desktop chiaro](schermate/laterali-1440-light.png), [desktop scuro](schermate/laterali-1440-dark.png).


## Scelte da valutare

| Opzione | Vantaggio | Compromesso |
| --- | --- | --- |
| Bordi A, ampiezze uguali | Coppia simmetrica, opposizione di fase immediatamente riconoscibile | Maggiore presenza visiva nelle card piccole |
| Bordi B, seconda ampiezza al 60% | La linea blu mantiene più risalto, cornice meno simmetrica | La seconda curva è meno evidente |
| Reticolo A, ortogonale | Regolare, discreto, semplice da leggere come sfondo | Più rigido |
| Reticolo B, lieve curvatura | Sfondo meno rigido, sempre astratto | Più percepibile nelle aree vuote grandi |
| Bordi soltanto sopra | Minor peso visivo nelle pagine di lettura | La superficie ha una cornice meno marcata |
| Bordi sopra e sotto | Più continuità sulle card | Ripetizione più evidente nei cataloghi lunghi |

I controlli del confronto sono indipendenti: bordi, reticolo, posizione e tema. Le due curve sono disegni separati, mai la loro somma. Nessuna animazione decorativa continua. Nessun significato fisico è attribuito al reticolo.

## Schermate comparabili

| Contesto | Bordi A / reticolo A | Bordi B / reticolo A | Bordi A / reticolo B | Bordi B / reticolo B |
| --- | --- | --- | --- | --- |
| Mobile chiaro | [AA](schermate/confronto-390-light-A-reticolo-A.png) | [BA](schermate/confronto-390-light-B-reticolo-A.png) | [AB](schermate/confronto-390-light-A-reticolo-B.png) | [BB](schermate/confronto-390-light-B-reticolo-B.png) |
| Mobile scuro | [AA](schermate/confronto-390-dark-A-reticolo-A.png) | [BA](schermate/confronto-390-dark-B-reticolo-A.png) | [AB](schermate/confronto-390-dark-A-reticolo-B.png) | [BB](schermate/confronto-390-dark-B-reticolo-B.png) |
| Desktop chiaro | [AA](schermate/confronto-1440-light-A-reticolo-A.png) | [BA](schermate/confronto-1440-light-B-reticolo-A.png) | [AB](schermate/confronto-1440-light-A-reticolo-B.png) | [BB](schermate/confronto-1440-light-B-reticolo-B.png) |
| Desktop scuro | [AA](schermate/confronto-1440-dark-A-reticolo-A.png) | [BA](schermate/confronto-1440-dark-B-reticolo-A.png) | [AB](schermate/confronto-1440-dark-A-reticolo-B.png) | [BB](schermate/confronto-1440-dark-B-reticolo-B.png) |

Home, catalogo e articolo hanno schermate autonome nella stessa cartella, in entrambi i temi a 390 e 1440 px. La pagina interattiva è `anteprima-bordi-stringhe.html` nella build e `lavorazione/sito/anteprima-bordi-stringhe.html` nel ramo sorgente.

## Origine, output e conservazione

- `index.html` conserva il catalogo editoriale; la home navigabile è generata dalla build, con il logo SVG originale e la raccolta casuale delle venti fotografie approvate.
- `identita/tema-stringhe.css`, `tema-init.js`, `tema-controlli.js` sono condivisi da portale, servizi, modello e copie degli articoli. Ogni HTML incorpora tema e comportamenti; nessun CDN.
- `riferimenti/TEMA_DISPENSE.html` v11 è aggiornato nel sorgente e resta autonomo: contiene logo, font, indice, note, zoom, crediti e selettore del tema già pronti per i futuri articoli.
- I nove sorgenti scientifici ammessi restano identici alla base Git; soltanto le copie in `_site` ricevono navigazione e tema. Test automatici confrontano integralmente il corpo scientifico, immagini e tracciati SVG. Anche i sette sorgenti sospesi e tutte le traduzioni restano identici; nessuna riammissione.
- `crediti.html` è rigenerato dal registro; `risorse/crediti.json` aggiorna soltanto l’inventario del logo incorporato nel modello, il cui nome accessibile ora usa Stringhe. Avvisi, fonti, autori e licenze restano conservati. La verifica dei diritti già aperta non è sostituita da questo restyling.
- `_site` è output non versionato; il workflow dedicato salva la sola anteprima nel ramo `stringhe-preview`. Le schermate sono aggiunte solo a questo output di anteprima, non alla pubblicazione ufficiale.

## Verifiche e limiti

`sync_stringhe_theme.py --check`, `credits.py --check`, build e dieci test automatici superati. Chromium controlla 15 pagine (portale, servizi, confronto, modello e nove articoli) a 320, 390, 768, 1024 e 1440 px, in chiaro e scuro: 150 combinazioni senza overflow orizzontale o errori JavaScript.

Verificate tutte le venti fotografie, tutte le nove destinazioni casuali, ricerca e filtro, tema persistente, cambio del tema di sistema in Automatico, storage bloccato, movimento ridotto, pausa da tastiera del logo, indice, note, zoom, crediti e download identico all’HTML navigabile. Verificati tema di sistema e crediti anche senza JavaScript.

Mobile e touch sono emulati in Chromium: non è dichiarata una prova su Android fisico. Il browser gestito locale vieta file:// con ERR_BLOCKED_BY_ADMINISTRATOR: verificato il documento in memoria con rete bloccata; il controllo file:// diretto è previsto in Actions con Chromium standard e il rapporto dichiara l’esito effettivo. Le pagine scaricate conservano SVG, font, contenuti e crediti incorporati; per i rimandi al portale serve una connessione.

Contrasto misurato sui testi della home: testo sul giallo 10,89:1; testi secondari 6,83:1 in chiaro e 7,54:1 in scuro; accento dei titoli 6,86:1 / 7,42:1. Verificato anche il focus e l’isolamento del selettore tema quando l’indice è aperto.

## Anteprima e verifica remota completate

[Home interattiva](https://raw.githack.com/rickymusu-bit/fisica/48494f222e1fef9faf3f25eb7faf7bc3e432e773/index.html) — [Confronto bordi e reticolo](https://raw.githack.com/rickymusu-bit/fisica/48494f222e1fef9faf3f25eb7faf7bc3e432e773/anteprima-bordi-stringhe.html).

Il servizio di anteprima può mostrare inizialmente «Open the page»: quel pulsante apre la pagina del ramo isolato. Il link usa un commit immutabile per evitare ambiguità di cache. Verificati via browser a 390 px il passaggio home → catalogo → Conduzione → home, la persistenza del tema e i controlli del confronto. L’HTML remoto coincide byte per byte con la build locale.

[Actions 39391624609](https://github.com/rickymusu-bit/fisica/actions/runs/39391624609) superata sul commit `3fab7a9`: componenti, crediti, build, dieci test, 150 combinazioni browser e prova **file:// diretta riuscita** in Chromium standard. Letto anche il rapporto nell’artefatto `confronti-stringhe`; nessun errore JavaScript. Il limite file:// riportato sopra riguarda soltanto il browser locale gestito. [Workflow anteprima 39391615879](https://github.com/rickymusu-bit/fisica/actions/runs/39391615879) riuscito; commit generato `48494f2`. PR #43 conservata in bozza.

Prima di una pubblicazione ufficiale restano la scelta dell’utente per bordi e reticolo, la valutazione da Android dell’anteprima e l’autorizzazione esplicita al merge/deployment.
