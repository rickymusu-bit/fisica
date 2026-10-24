# Verifica del salvataggio automatico

24 ottobre 2026. PR #77, senza pubblicazione ufficiale.

## Esito

Superati build completa, controlli del tema e dei crediti, 23 test unitari e suite Chromium desktop/mobile nel [workflow](https://github.com/rickymusu-bit/fisica/actions/runs/40101691256), sul commit `26fc64f33512df91a0fceff1c4a5c9f22d153e52`.

Verificati:

- ricarica con stessi quesiti, alternative, risposte confermate e scadenze;
- conservazione della scelta provvisoria senza conteggiarla come risposta data;
- uscita e ritorno tramite Indietro;
- chiusura e riapertura della scheda nello stesso profilo;
- applicazione delle scadenze trascorse a pagina chiusa, fino al risultato;
- recupero del risultato e cancellazione con Nuovo quiz;
- recupero dello snapshot anche se l’archivio del sito non è più disponibile;
- gestione di salvataggi corrotti o di versione incompatibile;
- salvataggio bloccato: avviso visibile e quiz utilizzabile in memoria.

Superati localmente anche i controlli di sintassi JavaScript/Python e 4 test unitari mirati. I test browser usano esclusivamente fixture temporanee, non domande pubblicate.

## Anteprime

[HTML autonomo](anteprima-categoria-unica.html), senza archivio reale.

[Sessione recuperata su mobile](quiz-ripresa-390.png): domanda 2 di 3, una risposta confermata e scelta corrente ripristinata.

[Salvataggio bloccato su mobile](quiz-salvataggio-bloccato-390.png): avviso visibile, senza impedire la prosecuzione.

Le schermate sono generate con dati di collaudo. Il commit finale aggiunge solo rapporto, stato e schermate, lasciando invariato il codice verificato.

## Limiti

Il salvataggio è locale e riferito allo stesso indirizzo e profilo del browser. Non viene trasferito tra dispositivi e può essere eliminato cancellando i dati del sito o terminando una sessione privata. Il tempo continua a scorrere fuori dalla pagina. Non è un sistema contro manipolazioni intenzionali dei dati locali o dell’orologio.
