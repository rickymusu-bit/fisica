# Quattro alternative per tutti i livelli

24 ottobre 2026. PR #78, ramo feature/quiz-quattro-alternative-20261024. Nessuna pubblicazione ufficiale.

## Esito

Superati nel [workflow](https://github.com/rickymusu-bit/fisica/actions/runs/40103061944), sul commit `14366820a781cd27cebffecfdec31f1f228c51cf`:

- verifica di tema e crediti;
- build completa del sito;
- 24 test unitari, compresi accettazione di quattro opzioni e rifiuto di tre/cinque per ogni livello;
- suite browser desktop/mobile, nei due temi;
- quattro alternative nei quiz facili, medi e difficili;
- recupero delle sessioni precedenti con alternative, risposte e scadenze originali;
- avvio di nuovi quiz con quattro opzioni e salvataggio versione 2;
- controlli già presenti su timer, categorie, risultati e persistenza.

Superati localmente anche 6 test mirati e i controlli di sintassi JavaScript/Python. La prima simulazione dei salvataggi precedenti è stata corretta per inserire lo snapshot dopo l’uscita dal quiz attivo, evitando che il normale autosalvataggio della pagina lo sovrascrivesse. Non sono state cambiate le regole di gioco per superare il test.

## Anteprime

- [HTML autonomo](anteprima-categoria-unica.html), senza archivio reale.
- [Configurazione mobile scura](quiz-config-390-dark.png) e [chiara](quiz-config-390-light.png).
- [Configurazione desktop scura](quiz-config-1440-dark.png) e [chiara](quiz-config-1440-light.png).
- [Domanda recuperata con quattro alternative](quiz-ripresa-390.png).
- [Salvataggio bloccato](quiz-salvataggio-bloccato-390.png).

Le schermate usano fixture temporanee e non domande pubblicate. Il commit finale aggiunge solo rapporto, stato e schermate, lasciando invariato il codice verificato.

Ogni nuova domanda ha una risposta corretta e tre distrattori. Tempo, categorie e target dell’archivio non cambiano. Nessun dataset reale o capitolo modificato.
