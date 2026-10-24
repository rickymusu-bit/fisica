# Verifica del quiz a categoria unica

24 ottobre 2026. PR #77, ramo feature/quiz-categoria-unica-20261024. Nessuna pubblicazione ufficiale.

## Esito

Superati i controlli del workflow [Verifica portale Stringhe](https://github.com/rickymusu-bit/fisica/actions/runs/40099155010), sul codice del commit `957bafe785d9f3872151efa24ca66446f9a7ae00`:

- sincronizzazione del tema e verifica dei crediti;
- build completa del sito (22 pagine HTML e 20 copertine);
- 23 test unitari, inclusi i nuovi controlli del registro e dello schema;
- suite Chromium desktop e mobile emulato, temi chiaro/scuro, interazioni e copie offline;
- scelta esclusiva della categoria, isolamento categoria/difficoltà, quantità 1–30, indisponibilità al cambio livello, risposte e salti, risultato e scadenza di 120 secondi anche al livello difficile.

Superati localmente anche 5 test mirati e la compilazione Python dei moduli modificati. La verifica nel browser è stata eseguita in GitHub Actions. Il primo tentativo aveva un confronto di test influenzato dal maiuscolo CSS; il confronto ora legge il contenuto testuale senza trasformazioni grafiche. Nessun difetto di estrazione è emerso.

## Anteprime

- [HTML autonomo](anteprima-categoria-unica.html): generato dal renderer e dal tema correnti. Riproduce il sito reale senza archivio, quindi le categorie non sono ancora avviabili.
- [Mobile scuro](quiz-config-390-dark.png), [mobile chiaro](quiz-config-390-light.png).
- [Desktop scuro](quiz-config-1440-dark.png), [desktop chiaro](quiz-config-1440-light.png).

Le schermate mostrano la selezione attiva usando esclusivamente fixture temporanee dei test. Queste domande non sono salvate nell’archivio né pubblicate. Le modifiche finali a rapporto, stato e schermate non cambiano il codice verificato.

Il filtro usa un solo ID stabile di categoria e la difficoltà selezionata. La proposta di tag multipli è superata. Nessun capitolo didattico, manifest di pubblicazione o dataset reale modificato.
