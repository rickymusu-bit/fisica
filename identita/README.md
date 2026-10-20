# Logo di Stringhe

Versione v8 — 20 ottobre 2026. La richiesta corrente aggiunge alla curva nera originale una curva con gradiente blu in opposizione di fase. Questa scelta aggiorna la precedente regola del logo monocromatico; Git conserva le versioni anteriori.

Percorsi stabili:

- `logo-materia-oscura.svg`: vettoriale animato autonomo, con due curve separate.
- `logo-materia-oscura.gif`: esportazione trasparente dello stesso disegno, 256 × 256 px, 80 fotogrammi a 20 fps, periodo 4 secondi.

## Geometria e movimento

Curva nera invariata: `r₁(θ,t)=104+20 cos(4θ) sin(2πt/4)`. Curva blu: `r₂(θ,t)=104−20 cos(4θ) sin(2πt/4)`. Stessa ampiezza e opposizione di fase; nessuna somma delle due curve, nessuna rotazione. Nodi fissi a 22,5° + k · 45°. Il tratto nero resta di 7 unità nel viewBox 320 × 320. La blu usa lo stesso spessore e gradiente `#83D4FA` → `#337CD8` → `#4140A3`. Nei punti e negli istanti in cui le curve coincidono, il tratto nero è sopra quello blu.

Il test conserva l’impronta SHA-256 della sequenza nera già approvata e verifica che la blu corrisponda a uno sfasamento di 16 campioni su 32. I controlli comuni `controlli-logo.js` fermano/riprendono entrambe le curve nello stesso SVG, con clic, Invio o Spazio. Con movimento ridotto la coppia è statica, mostrata nella configurazione di massima deformazione per mantenere entrambe le curve distinguibili. La superficie chiara dedicata al logo garantisce il contrasto anche nel tema scuro.

## Rigenerazione e incorporamento

`python3 scripts/logo_materia_oscura.py` rigenera lo SVG. `python3 scripts/logo_materia_oscura.py --gif` rigenera anche la GIF; l’esportazione usa Chromium/Playwright e Pillow, senza dipendenze aggiuntive per il sito.

`scripts/stringhe_theme.py` incorpora lo stesso SVG nella home, nel modello v14 e nelle sole nove copie pubblicabili. `scripts/sync_stringhe_theme.py` allinea modello, confronto e pagina crediti; il registro aggiorna l’inventario del nuovo SVG del modello. Non riscrivere i sorgenti degli articoli, sospesi compresi. Il logo precedente e il riferimento originale dell’utente restano recuperabili in Git e in `lavorazione/sito/risorse-originali/`.

Nella home il logo accompagna il titolo in un’unica card condivisa con la copertina fotografica, senza onde laterali. Su mobile la foto è sotto al titolo; su desktop è affiancata. Il contenitore della didascalia ha la stessa larghezza dell’immagine, così il suo bordo sinistro coincide sempre con quello della fotografia, senza ritagli né bande interne. Restano le altre scelte approvate: reticolo regolare e sinusoidi verticali di uguale ampiezza.
