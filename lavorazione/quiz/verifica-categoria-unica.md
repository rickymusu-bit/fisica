# Verifica del quiz a categoria unica

24 ottobre 2026. Modifiche preparate sul ramo feature/quiz-categoria-unica-20261024, senza pubblicazione.

- Superati localmente 4 test di regressione: rinomina dei capitoli senza effetti sugli ID; incoerenze e duplicati nel registro; accettazione di una sola categoria e rifiuto dello schema precedente; archivio assente e selettore esclusivo.
- Compilazione Python dei moduli modificati superata.
- Anteprima HTML autonoma generata con il renderer e il tema correnti in anteprima-categoria-unica.html. Come il sito reale, non contiene quesiti: le categorie restano indisponibili finché manca un archivio.
- Chromium non è disponibile in questo ambiente; il tentativo di installazione non ha fornito un archivio valido. Controlli visivi e funzionali browser da eseguire in GitHub Actions, dove lo script aggiornato usa dati effimeri senza pubblicarli.
- La suite completa di build, componenti, crediti e browser è affidata al workflow della PR; l’esito verrà registrato dopo l’esecuzione.

Il filtro usa un solo ID di categoria e la difficoltà selezionata. La vecchia proposta di tag multipli non è stata implementata. Nessun HTML didattico, manifest di pubblicazione o dataset reale modificato.
