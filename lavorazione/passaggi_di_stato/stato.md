# Stato — Passaggi di stato

Ultimo aggiornamento: 2026-10-17 23:29 (Europe/Rome). Master v53, letto con i riferimenti di stile. Ramo `revisione/materia-passaggi-capitoli`. Fonte v8 di `stati_della_materia_e_passaggi_di_stato.html`, blob `8ef5566c73f670dbf23b550e4e36a52cdb7ddfc2`. [Mappa iniziale della suddivisione](../stati_della_materia_e_passaggi_di_stato/proposta-editoriale.md).

## Ambito e approvazioni effettive

Capitolo sui sei passaggi di stato, scambi energetici, calore latente e curva dell’acqua. Tre applicazioni: sudore, pompa di calore e centrale PWR. **Un solo esempio svolto**, seguito da otto domande finali. Tema della v8 e separazione in due capitoli approvati. Apertura concreta sui cubetti che fondono, domanda su che cosa cambia e come viene usata l’energia ricevuta.

Testo approvato dall’utente prima degli adattamenti puntuali («Per i passaggi di stato va tutto bene»); P1 creato su sua richiesta. Materiali scelti acquisiti con fonti/licenze. Richieste successive applicate: eliminare frigorifero a favore della sola pompa di calore; usare il PWR; conservare lo sfondo della scultura; eliminare la foto della pentola; usare una massa da scultura intera, ipotizzata di 500 kg; infine **unificare i due svolgimenti nel calcolo completo dal ghiaccio a 0 °C al vapore a 100 °C**. Le scelte e queste revisioni sono autorizzate, senza nuova conferma dei medesimi file.

## Bozza e modello correnti

[Bozza completa](bozza.md). L’esempio unico comprende fusione a 0 °C, riscaldamento dell’acqua da 0 a 100 °C e vaporizzazione a 100 °C alla pressione atmosferica ordinaria. Massa 500 kg esplicitamente ipotizzata, non ricavata dalla fotografia. Trascurate dispersioni ed energia assorbita dalle attrezzature. Il calore specifico dell’acqua liquida è approssimato con 4180 J/(kg · K), spiegato insieme a Qr = m · c · ΔT e alla differenza di temperatura di 100 K.

Calcoli verificati: Qf = 500 · 334.000 = 167.000.000 J = 167 MJ; Qr = 500 · 4180 · 100 = 209.000.000 J = 209 MJ; Qv = 500 · 2.257.000 = 1.128.500.000 J = 1128,5 MJ. **Qtot = 1.504.500.000 J = 1504,5 MJ**, circa 1,50 miliardi di joule. Nessun riscaldamento iniziale del ghiaccio o surriscaldamento del vapore incluso. Domande 5 e 6 aggiornate su proporzionalità del totale e fase di riscaldamento omessa; nessuna soluzione nelle domande finali.

## Visuali disponibili e verifiche

[Registro visuali](visuali.md), [fonti/licenze/hash](risorse/materiali-scelti.json). C2 metallo fuso (Rajesh_India, CC BY-NC-ND 2.0; foto intera per uso non commerciale); P1 schema con frecce e variante mobile; P2–P8 immagini/GIF della v8; P9 curva qualitativa da adattare al telefono; A1 Jordan/sudore (credito «Lipofsky Basketballphoto.com», CC BY-SA 3.0); A2 pompa di calore (Wikideas1, CC0); A3 PWR (TVA, pubblico dominio), etichette inglesi spiegate e generatore elettrico distinto dal generatore di vapore.

E1: [schema completo unico](risorse/schema-esempio.svg), foto della scultura con sfondo conservato e quattro stati collegati da tre frecce energetiche. La richiesta esplicita sullo sfondo prevale sulla regola generale degli esercizi; nessuna rimozione eseguita. I byte della foto incorporata corrispondono alla foto scelta. Anteprima nel browser a 600 px ispezionata. Schemi precedenti separati sostituiti e recuperabili in Git. Foto della pentola esclusa dall’integrazione e dai crediti finali, conservata solo come riferimento. Nessun file ulteriore necessario.

Nessuna nuova simulazione: quelle microscopiche restano nel capitolo Stati della materia. Le verifiche iniziali dei singoli schemi sono state seguite dalle verifiche HTML registrate sotto. Nessuna pubblicazione.


## Via alla realizzazione

L’utente ha confermato «Ok procedi»: realizzazione dei due HTML autorizzata. HTML v9 integrati, verifiche in corso; nessuna pubblicazione. Peso iniziale: stati 6.270.253 byte, passaggi 20.808.247 byte. Richiesta autorizzazione puntuale per ottimizzare senza perdita le GIF del secondo capitolo, secondo il limite di 20 MB del master.

## Anteprima HTML realizzata — 2026-10-17 23:18 (Europe/Rome)

HTML v9 in `bozza.html`, copia con nome stabile alla radice del ramo di lavorazione; anteprime desktop/mobile salvate. Immagini incorporate, simulazioni particellari originali conservate e dotate di pausa, preferenza di movimento ridotto rispettata; curva selezionabile e PWR ingrandibile. Verifiche Chromium 390/1280 px e offline superate: immagini integre, nessun errore JavaScript, nessuna eccedenza orizzontale della pagina, 6/8 domande finali. Calcoli dell’esempio verificati: totale 1.504.500.000 J. Build locale superata, indice a 10 articoli e 12 casi di vecchi URL con query/frammenti verificati. Nessuna pubblicazione o modifica del workflow.

**Problema rilevato nella v9 (risolto dalla v10):** Stati della materia pesa 6.270.253 byte; Passaggi di stato pesa 20808480 byte, oltre il limite di 20.000.000 byte. Richiesta in chat approvazione per ottimizzare senza perdita copie delle tre GIF, conservando fotogrammi, colori e tempi; risposta non ancora ricevuta. File di Passaggi di stato consegnato come anteprima, non dichiarato definitivo conforme al peso. Le attribuzioni dei visuali ereditati incompleti sono dichiarate nei crediti; recuperata e verificata per hash la GIF di fusione (Moussa, pubblico dominio).

## Ottimizzazione autorizzata e applicata — 2026-10-17 23:29

Richiesta esplicita: «Fai entrambi i metodi su tutte le gif del capitolo passaggi di stato». Autorizzata riduzione sia della risoluzione sia dei fotogrammi delle tre GIF; non serve una nuova conferma della stessa modifica. Eseguita su copie, originali immutati. Dimensioni all’80%, circa due terzi dei fotogrammi; durata totale e loop preservati. Registro in `risorse/ottimizzazione-gif.json`; tabella in `visuali.md`. Tutti i fotogrammi decodificati corrispondono ai fotogrammi ricampionati e quantizzati attesi: nessuna scia dovuta alla codifica GIF. Confronti a metà animazione ispezionati.

HTML aggiornato a **v10**, sincronizzato con `bozza.html`, peso **14252684 byte**, sotto il limite di 20 MB e la soglia di avviso di 18 MB. Testo didattico confrontato automaticamente con v9: invariato. Crediti aggiornati con le elaborazioni. Build locale superata; dimensioni dei download ricalcolate. Prove Chromium offline a 390 e 1280 px: tre GIF caricate e animate (cambiamento dei fotogrammi verificato), nessuno scorrimento orizzontale della pagina o errore JavaScript; otto domande finali conservate. Anteprime desktop/mobile e indice aggiornati; home mostra 14,25 MB. Risultati in `risorse/verifica-gif-browser.json`. Restano dichiarati i crediti incompleti dei materiali ereditati dalla v8.

## Prossima operazione

Consegnare anteprima aggiornata e pesi. La revisione del peso è completata; pubblicazione non autorizzata e non eseguita.
