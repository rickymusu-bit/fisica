# Logo di Materia Oscura

Versione v1 · 18 ottobre 2026. Creato su richiesta esplicita dell’utente a partire dalla configurazione della stringa chiusa al centro in basso dell’immagine di riferimento. Posizione nella home scelta dall’utente: **accanto al titolo**. I file restano autonomi e riutilizzabili.

- **logo-materia-oscura.svg**: originale vettoriale animato, nero su fondo trasparente; nessun JavaScript o risorsa esterna.
- **logo-materia-oscura.gif**: esportazione animata trasparente, 256 × 256 px, 20 fotogrammi al secondo, 160 fotogrammi, ciclo di 8 secondi.
- **logo-materia-oscura-statico.svg**: versione fissa con quattro lobi orizzontali e verticali, per stampe o contesti senza animazione.

Il ciclo mostra una sola curva continua e chiusa: **cerchio → quattro lobi orizzontali e verticali → cerchio → quattro lobi diagonali → cerchio**. Non sovrapporre le configurazioni, aggiungere scie, sfumature o riempimenti. Nessun rettangolo di sfondo fa parte del logo. Il motivo a quadretti dell’anteprima serve soltanto a mostrare la trasparenza.

Lo SVG usa `viewBox="0 0 320 320"`, tratto nero di 7 unità, raccordi arrotondati e un ciclo dichiarativo SVG di 8 secondi. La deformazione è costruita con una curva polare a quattro lobi: il cambio di segno dell’ampiezza alterna le due orientazioni passando dal cerchio. Non è una misura sperimentale né una simulazione fisica quantitativa. In ogni momento è visibile una sola configurazione; con la preferenza di movimento ridotto lo SVG mostra un cerchio fermo.

Per inserirlo in un’altra pagina basta, per esempio:

```html
<img src="logo-materia-oscura.svg" width="96" height="96" alt="Materia Oscura">
```

Usare lo SVG quando possibile per mantenere il logo nitido a qualsiasi dimensione. La GIF offre una copia per le applicazioni che accettano animazioni raster. La home incorpora direttamente lo stesso SVG attraverso `scripts/home_italian.py`, così non dipende da una richiesta esterna e consente pausa/ripresa premendo il logo o usando la tastiera. Il tasto è attivato solo quando gli script sono disponibili; l’animazione SVG funziona anche senza di essi.

Il sorgente geometrico riproducibile è `scripts/logo_materia_oscura.py`: `python scripts/logo_materia_oscura.py` rigenera i due SVG. Se cambia il disegno, riesportare anche la GIF dallo SVG corrente e aggiornare il registro di verifica. La build incorpora il file animato corrente; le modifiche a `identita/` attivano il workflow Pages soltanto quando integrate in `main`.

Riferimento originale conservato senza modifiche in `lavorazione/sito/risorse-originali/riferimento-stringhe.jpg`; non fa parte del sito pubblico. Controlli e dimensioni effettive in `lavorazione/sito/verifica-logo.json`. Anteprima autonoma in `lavorazione/sito/anteprima-logo.html`.
