# Centralizzazione dei crediti — resoconto

20 articoli HTML analizzati e modificati: cinque pubblicati, sette italiani sospesi e otto traduzioni conservate. Esaminato anche l’indirizzo storico dismesso, che non contiene un articolo né risorse e resta invariato. Aggiornate la home, il modello del tema v8, cinque bozze HTML esistenti e le istruzioni del progetto (master v60).

Il registro contiene **87 schede di provenienza** e **178 risorse uniche inventariate**, comprese risorse riutilizzate, font, SVG/canvas e anteprime statiche. I due conteggi hanno significati distinti: le schede comprendono anche avvisi generali preesistenti, mentre l’inventario identifica i contenuti effettivamente rilevati.

## Verifiche e limiti

- Sorgente scientifico, formule, immagini, animazioni e script originali dei 20 articoli confrontati con il commit di partenza e invariati.
- Conservate integralmente le 50 voci dei crediti degli articoli conformati, i due paragrafi di provenienza della vecchia Potenza termica, i 20 avvisi delle copertine, le provenienze nei commenti del codice e il copyright/OFL del font. Nessuna fonte bibliografica o scientifica rimossa.
- Build GitHub Pages riuscita: home, cinque articoli, pagina crediti, 20 copertine, logo, registro e licenza. Il manifest di pubblicazione non cambia; nessun indirizzo dismesso è ripristinato.
- Quattro test di regressione passati: deduplicazione e riuso fra articoli, modifiche associate al singolo utilizzo, preservazione dei media e della OFL, segnalazione delle licenze assenti senza invenzioni.
- 263 collegamenti/ancore locali verificati; nessuna sezione finale superflua; nessun ID duplicato nella pagina centrale.
- 18 prove Chromium: pagina a 320/390/768/1280 px senza overflow; media caricati nella home e nei cinque articoli; apertura/chiusura del dialogo, Esc e ritorno del focus; crediti autonomi con rete bloccata e JavaScript attivo/disattivato. Per il test offline l’HTML esatto è caricato in memoria: la navigazione file:// è vietata dalla configurazione del browser gestito e non viene dichiarata verificata.
- Verificati sulle fonti originali la formula di attribuzione personalizzata di Raimond Spekking, la politica Chandra e la licenza Flickr CC BY-NC-ND 2.0. Non è dichiarata una nuova verifica esterna integrale di tutte le licenze storiche.

## Diritti da verificare

La **verifica delle licenze non è conclusa**. Restano **14 schede** con documentazione incompleta e **56 risorse immagine** senza associazione individuale certa. Il secondo gruppo comprende anche materiali elaborati nel progetto per i quali manca una scheda individuale: non sono automaticamente dichiarati illeciti. Le risorse restano intatte, senza inventare licenze o autorizzazioni.

I casi comprendono GIF Tenor e miniatura NCSSM in Conduzione; animazione Sole–Terra–atmosfera, tostapane e schema di assorbimento in Irraggiamento; animazioni e fotografie storiche di Passaggi di stato; illustrazioni e fotografie dei documenti sospesi e tradotti. Gli avvisi generali e le indicazioni di modifiche sono conservati anche quando non risolvono da soli l’identità dei titolari.

L’elenco puntuale, con descrizioni, provenienze note e associazioni agli articoli, è nella sezione [Licenze e attribuzioni da verificare](../../crediti.html#da-verificare), nel [registro JSON](../../risorse/crediti.json) e nel [rapporto dei controlli](crediti-verifiche.json). Nessun credito obbligatorio noto è perso nel trasferimento; questo non colma le lacune preesistenti.

## Anteprima

[Pagina HTML](../../crediti.html) · [Desktop](anteprima-visuali/crediti-1280.png) · [Mobile](anteprima-visuali/crediti-390.png) · [Crediti autonomi](anteprima-visuali/crediti-autonomi-390.png).

## File creati o aggiornati

- `.github/workflows/pages.yml`
- `AGENTS.md`
- `MASTER_PROMPT.md`
- `README.md`
- `bilancio_conservazione_rendimento_it.html`
- `conduzione_it.html`
- `convezione_it.html`
- `copertine/manifest.json`
- `crediti.html`
- `grafici_piano_cartesiano_fr.html`
- `grafici_piano_cartesiano_it.html`
- `grafici_piano_cartesiano_sq.html`
- `index.html`
- `irraggiamento_it.html`
- `lavorazione/bilancio_conservazione_rendimento/stato.md`
- `lavorazione/conduzione/bozza.html`
- `lavorazione/conduzione/stato.md`
- `lavorazione/convezione/bozza.html`
- `lavorazione/convezione/stato.md`
- `lavorazione/grafici_piano_cartesiano/stato.md`
- `lavorazione/irraggiamento/bozza.html`
- `lavorazione/irraggiamento/stato.md`
- `lavorazione/lavoro_energie_potenza/stato.md`
- `lavorazione/metodo_scientifico/stato.md`
- `lavorazione/passaggi_di_stato/bozza.html`
- `lavorazione/passaggi_di_stato/stato.md`
- `lavorazione/potenza_termica_conduzione_convezione/realizza-capitoli.py`
- `lavorazione/potenza_termica_conduzione_convezione/stato.md`
- `lavorazione/sistema_internazionale_notazione/stato.md`
- `lavorazione/sito/anteprima-visuali/crediti-1280.png`
- `lavorazione/sito/anteprima-visuali/crediti-390.png`
- `lavorazione/sito/anteprima-visuali/crediti-autonomi-390.png`
- `lavorazione/sito/crediti-resoconto.md`
- `lavorazione/sito/crediti-verifiche.json`
- `lavorazione/sito/stato.md`
- `lavorazione/stati_della_materia/bozza.html`
- `lavorazione/stati_della_materia/stato.md`
- `lavorazione/strumenti_errori_incertezza/stato.md`
- `lavoro_energie_potenza_it.html`
- `licenze/Lexend-OFL.txt`
- `metodo_scientifico_fr.html`
- `metodo_scientifico_it.html`
- `metodo_scientifico_sq.html`
- `passaggi_di_stato.html`
- `potenza_termica_conduzione_convezione_it.html`
- `riferimenti/TEMA_DISPENSE.html`
- `riferimenti/TERMINOLOGIA_SITO.md`
- `risorse/README.md`
- `risorse/crediti.json`
- `scripts/build_pages.py`
- `scripts/credits.py`
- `scripts/home_covers.py`
- `scripts/home_italian.py`
- `scripts/test_credits.py`
- `sistema_internazionale_notazione_fr.html`
- `sistema_internazionale_notazione_it.html`
- `sistema_internazionale_notazione_sq.html`
- `stati_della_materia.html`
- `strumenti_errori_incertezza_fr.html`
- `strumenti_errori_incertezza_it.html`
- `strumenti_errori_incertezza_sq.html`
