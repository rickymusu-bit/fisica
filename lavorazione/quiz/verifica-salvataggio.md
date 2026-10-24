# Verifica del salvataggio automatico

24 ottobre 2026. PR #77, senza pubblicazione ufficiale.

Implementazione: salvataggio locale dello stato attivo e del risultato; ripresa con gli stessi quesiti, alternative e scadenze. Una scelta provvisoria viene conservata ma non conteggiata come risposta confermata. Il tempo trascorso a pagina chiusa viene applicato al rientro.

Verifiche locali: sintassi JavaScript e Python; 4 test unitari del quiz superati. Suite browser ampliata con ricarica, Indietro, riapertura di scheda, scadenze offline, recupero del risultato, Nuovo quiz, archivio modificato, dati corrotti e salvataggio bloccato. Verifica completa in GitHub Actions da completare prima della consegna.

Anteprima autonoma aggiornata: `anteprima-categoria-unica.html`. Il sito non contiene domande reali; i test impiegano esclusivamente fixture temporanee. Le schermate di ripresa e avviso di storage saranno prodotte dal workflow.
