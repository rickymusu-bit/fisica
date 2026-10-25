# Revisione dell'allineamento delle tabelle di Stringhe

**25 ottobre 2026.** Audit dei **19 capitoli pubblicati** (pubblicazione.json).

**35 tabelle HTML** in 15 capitoli: **31** disallineate in **13** capitoli; **4** già centrate nei capitoli 8 e 9. I restanti 4 capitoli non contengono tabelle.

## Scelte grafiche

Tutte le intestazioni e le celle numeriche o con categorie brevi sono centrate. Le celle descrittive conservano l'allineamento a sinistra quando migliora la lettura: colonna «Perché» e regole operative nelle Cifre significative, «Che cosa comunica» in Errori e incertezza, descrizioni di forma e disposizione delle particelle negli Stati della materia, testi comparativi di Evaporazione/Ebollizione e condizioni della tabella dei calori latenti, etichette lunghe degli ordini di grandezza. I messaggi delle simulazioni su celle multiple restano a sinistra. Le didascalie non sono celle e mantengono il proprio stile.

Righe, colonne, valori, unità, formule e contenuti didattici non sono cambiati. Le date editoriali dei capitoli non vengono aggiornate da una modifica CSS. Le dispense escluse da pubblicazione.json non sono state modificate.

## File modificati

| HTML del capitolo | Tabelle | Versione | Bozza |
|---|---:|---|---|
| metodo_scientifico_it.html | 1 | v13 → v14 | solo stile (sorgenti diversi) |
| grandezze_fisiche_sistema_internazionale_it.html | 2 | v6 → v7 | allineata e versionata |
| potenze_dieci_notazione_scientifica_it.html | 3 | v7 → v8 | allineata e versionata |
| prefissi_sistema_internazionale_it.html | 8 | v5 → v6 | allineata e versionata |
| cifre_significative_it.html | 3 | v6 → v7 | allineata e versionata |
| strumenti_misura_it.html | 2 | v15 → v16 | allineata e versionata |
| errori_incertezza_misura_it.html | 4 | v14 → v15 | allineata e versionata |
| temperatura_equilibrio_termico_it.html | 1 | v6 → v7 | allineata e versionata |
| energia_interna_calore_specifico_it.html | 1 | v9 → v10 | allineata e versionata |
| dilatazione_termica_it.html | 2 | v5 → v6 | assente |
| stati_della_materia.html | 1 | v24 → v25 | allineata e versionata |
| passaggi_di_stato.html | 2 | v25 → v26 | allineata e versionata |
| conduzione_it.html | 1 | v11 → v12 | allineata e versionata |

## Verifiche

- Audit degli stili calcolati con Chromium a 390 e 1280 px prima delle correzioni.
- **Riesame Chromium superato** dopo le correzioni, a 390 e 1280 px: 35 tabelle, con allineamenti centrati e sole eccezioni discorsive previste.
- Confronto integrale con main superato: dopo aver normalizzato soltanto CSS, metadati di versione e attributi grafici, tutti i 13 capitoli corretti sono identici ai precedenti; gli altri 6 non sono stati modificati.
- Aggiunto il controllo permanente `verify_table_alignments` in `scripts/verify_stringhe_browser.py`: verifica tutti i 19 capitoli a 390 e 1440 px e rifiuta gli allineamenti non giustificati.
- Suite ordinaria (componenti, crediti, build e browser): da eseguire sulla PR.

**Nessuna integrazione in main né pubblicazione senza approvazione.**
