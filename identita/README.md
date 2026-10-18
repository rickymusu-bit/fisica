# Logo definitivo di Materia Oscura

Versione v5 · 18 ottobre 2026. Scelta approvata dall’utente, che ha richiesto di eliminare gli altri tentativi, pubblicarla nella home e sostituire l’icona in alto a sinistra negli articoli. È una regola del tema comune **v5**, salvato in `riferimenti/TEMA_DISPENSE.html`.

I soli file grafici correnti sono:

- **logo-materia-oscura.svg**: originale vettoriale animato, autonomo e senza script esterni.
- **logo-materia-oscura.gif**: copia animata trasparente, 256 × 256 px, 80 fotogrammi a 20 fps, periodo di 4 secondi.

Una sola curva nera su sfondo trasparente, senza riempimenti, scie o configurazioni sovrapposte. Onda sinusoidale **stazionaria**, quattro creste, nodi angolari fissi e ventri oscillanti, nessuna rotazione. Ampiezza definitiva **20**, raggio di riferimento 104 e tratto di 7 unità nel viewBox 320 × 320. Non ridurre l’ampiezza né riprendere le proposte progressive o a otto lobi. Il motivo a quadretti dell’anteprima serve soltanto a mostrare la trasparenza.

Il logo compare accanto al titolo nella home e al posto del simbolo φ nella barra in alto a sinistra di ogni articolo conformato. Il modello autonomo conserva l’esatto componente da riusare nei capitoli futuri: SVG incorporato, pulsante per pausa/ripresa e movimento ridotto, dimensioni responsive. Il collegamento «Fisica» accanto al logo continua a riportare all’inizio dell’articolo.

I controlli comuni sono in `controlli-logo.js`, incorporati identici nella home e nel tema. Si può fermare/riprendere il logo con clic, Invio o Spazio. Con movimento ridotto parte fermo; senza script lo SVG mantiene l’animazione nativa e l’alternativa ferma prevista dalla preferenza di movimento. Gli articoli restano autonomi e offline. I sette sorgenti esclusi da `pubblicazione.json` non ricevono aggiornamenti.

Modello geometrico: `r(θ,t)=104+20 cos(4θ) sin(2πt/T)`, `T=4 s`. Nodi a 22,5° + k · 45°. Il fattore temporale è campionato in 32 intervalli, con errore sullo spostamento inferiore a 0,10 unità. Generatore unico `scripts/logo_materia_oscura.py`: eseguire `python scripts/logo_materia_oscura.py` per rigenerare lo SVG, poi riesportare la GIF dallo stesso originale se si modifica il disegno.

La build pubblica soltanto questa coppia di file sotto `identita/`. I tentativi precedenti e i loro generatori/anteprime sono rimossi dall’albero corrente; quelli già salvati restano recuperabili in Git, senza ripristinarli come alternative attive. Il riferimento originale dell’utente resta conservato in `lavorazione/sito/risorse-originali/riferimento-stringhe.jpg`, non pubblicato.

Anteprima unica: `lavorazione/sito/anteprima-logo.html`. Verifica del modello e hash dei file: `lavorazione/sito/verifica-logo.json`; controlli di integrazione e pubblicazione: `lavorazione/sito/logo-definitivo.json`.
