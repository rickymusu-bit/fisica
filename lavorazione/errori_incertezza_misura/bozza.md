# Errori e incertezza di misura

[EDITORIALE — Bozza v9, 24 ottobre 2026. Testo v4 approvato e realizzazione autorizzata con «Ok vai»; immagini sostitutive scelte dall’utente e integrate. Area: Introduzione alla fisica e alla misura.]

[COP-07 — Fotografia scelta dall'utente: TV noise.jpg. Intera, senza ritagli o zoom, non ripetuta nel corpo.]

*Rumore sullo schermo di un televisore analogico sintonizzato su un canale senza trasmissioni: i disturbi possono produrre variazioni nell'uscita di un dispositivo.*

## Lo stesso evento, letture diverse

Supponiamo di misurare con un cronometro la durata di un evento e di leggere 2,40 s. Ripetendo la misura della durata di uno stesso evento potremmo ottenere letture un po' diverse, anche se il display continua a mostrare i centesimi di secondo. Da dove arrivano queste differenze? E, se il numero resta sempre uguale, possiamo essere sicuri di aver misurato bene?

La misura coinvolge lo strumento, il modo in cui lo usiamo e le condizioni della prova. Per separare questi contributi conviene distinguere due situazioni: le letture possono disperdersi in modo imprevedibile, oppure risultare spostate in modo simile rispetto a un riferimento. Le due cose possono anche accadere insieme.

[SCH-07-1 — Cronometro digitale scelto dall’utente; fotografia intera, display azzerato conservato. I valori dell’esempio sono sviluppati nel testo, nella tabella e nel grafico.]

*La pressione manuale dei tasti può cambiare da una prova all’altra e contribuire alla dispersione dei tempi.*

Quando avviamo e fermiamo il cronometro a mano, il momento in cui premiamo il tasto non è identico a ogni prova. Queste variazioni possono contribuire agli **errori casuali**, che cambiano in modo imprevedibile fra misure ripetute. Ripetere ci aiuta a osservare la dispersione e a rendere il risultato meno dipendente da una singola lettura. Non elimina però ogni possibile spostamento.

Nel voltmetro della foto, con i morsetti scollegati, la lancetta si trova sotto lo zero anziché sullo zero. Uno spostamento di questo tipo porta a leggere valori più bassi di quelli che si otterrebbero con lo zero corretto. Questo è un esempio di **errore sistematico**: un contributo che rimane costante o cambia in modo prevedibile. Ripetere la misura non lo cancella; occorre controllare lo zero, correggere la procedura o confrontare lo strumento con un riferimento.

[FIG-07-2 — Voltmetro analogico scelto dall’utente, con lo zero spostato verso valori negativi; fotografia intera.]

*Lo zero spostato verso valori negativi abbassa le letture; ripetere la misura non corregge questo spostamento.*

Diverso ancora è uno **sbaglio grossolano**: trascrivere 23,4 g invece di 32,4 g, confondere grammi e chilogrammi oppure usare il comando sbagliato. Qui non stiamo descrivendo una normale variazione fra letture, ma un problema nella procedura o nella registrazione. Un dato molto lontano dagli altri invita a controllare gli appunti e la prova; non si elimina automaticamente perché disturba il risultato.

## Punti raccolti e punti spostati

I bersagli permettono di vedere la differenza fra dispersione e spostamento. Immaginiamo che ogni punto rappresenti una lettura e che il centro indichi un riferimento noto. Punti molto vicini fra loro corrispondono a letture precise; per l'accuratezza conta anche la loro vicinanza al riferimento.

[FIG-07-1 — Schema dei quattro bersagli ricreato su richiesta a partire dal riferimento Ossila, con etichette in italiano. A e C in alto, B e D in basso.]

*La precisione riguarda quanto i punti sono raccolti; l’accuratezza riguarda la loro vicinanza al riferimento centrale.*

Il gruppo B mostra perché una serie precisa può essere poco accurata. Aggiungere altri punti nello stesso gruppo renderebbe ancora più evidente la loro concentrazione, ma non li riporterebbe al centro. Analogamente, molte letture simili del voltmetro con lo zero spostato non risolvono il problema dello zero.

Nel gruppo C, invece, le letture sono disperse, pur essendo distribuite attorno al riferimento. La dispersione è un'informazione utile, ma non basta per ricostruire ogni contributo alla misura. Per questo un risultato deve comunicare anche quanto è incerto.

## Dalle letture alla media e alla semidispersione

Ripetiamo cinque volte la misura della durata di un evento nelle stesse condizioni, avviando e fermando a mano il cronometro. I tempi della tabella sono inventati per l'esempio: permettono di ragionare su una serie di letture senza presentarli come risultati di un esperimento realmente eseguito. Il passo visualizzato dal cronometro è 0,01 s.

[TAB-07-2 — Tabella originale delle cinque letture, trasferita dalla sezione #incertezza del sorgente storico.]

| Prova | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Tempo (s) | 2,31 | 2,37 | 2,40 | 2,43 | 2,49 |

Per ricavare un valore centrale calcoliamo la **media aritmetica**: sommiamo le letture e dividiamo per il loro numero. Se le letture sono \(t_1,\ldots,t_n\) e il loro numero è \(n\), scriviamo:

\[
\bar t=\frac{t_1+\ldots+t_n}{n}
\]

Il simbolo \(\bar t\), “t medio”, indica il risultato. Il numero \(n\) conta le letture e non ha unità: la media mantiene l'unità dei tempi. Per i cinque valori della tabella:

\[
\bar t=\frac{2{,}31+2{,}37+2{,}40+2{,}43+2{,}49}{5}\,\mathrm{s}=2{,}40\,\mathrm{s}
\]

Una media non descrive però quanto sono sparse le letture. La **semidispersione massima**, che indichiamo con \(d\), è metà della differenza fra il valore più alto e quello più basso:

\[
d=\frac{t_{\max}-t_{\min}}{2}
\]

I simboli \(t_{\max}\) e \(t_{\min}\) indicano gli estremi della serie. Se la distanza fra massimo e minimo raddoppia, anche \(d\) raddoppia. Per i dati della tabella:

\[
d=\frac{2{,}49-2{,}31}{2}\,\mathrm{s}=0{,}09\,\mathrm{s}
\]

La media è quindi 2,40 s, mentre l'intervallo fra le letture estreme è largo 0,18 s: la semidispersione ne è la metà. I 0,09 s sono nove volte il passo di 0,01 s del display. In questo caso la variabilità delle prove è più evidente del limite rappresentato dall'ultima cifra.

[GRAF-07-2 — Linea dei numeri originale della sezione #incertezza: cinque letture, media 2,40 s, estremi 2,31 s e 2,49 s; indicare d = 0,09 s come metà dell'ampiezza fra gli estremi. Trasferire il grafico senza il vecchio separatore puntiforme nel titolo. Distinto dal grafico interattivo della bilancia.]

*I punti rappresentano le cinque letture. La fascia va dal minimo al massimo; il tratto della media, in questo esempio simmetrico, cade a metà.*

Per calcolare queste due quantità:
1. Scrivi le letture nella stessa unità e conta quante sono.
2. Sommale e dividi per il loro numero per trovare la media.
3. Individua massimo e minimo, sottrai il minimo dal massimo e dividi per due.
4. Conserva i valori non arrotondati fino alla scrittura del risultato finale.

La semidispersione descrive gli estremi osservati, non la distanza fra la media e ciascun estremo. Qui i dati sono simmetrici, ma non accade in ogni serie. Ripetere aiuta a vedere la dispersione; non rivela da solo uno zero spostato o un ritardo che si ripete nello stesso modo.

## Che cosa significa il segno ±?

Dire soltanto “2,40 s” lascia aperta una domanda: con quale incertezza attribuiamo quel valore alla durata? L'**incertezza di misura** descrive la dispersione dei valori che possiamo attribuire alla grandezza sulla base delle informazioni disponibili. Per valutarla si considerano lo strumento, il metodo, le condizioni e, quando ci sono, le letture ripetute.

Quando usiamo la media delle letture, scriviamo il risultato nella forma:

\[
x=\bar x\pm U
\]

Il simbolo \(x\) indica la grandezza misurata; \(\bar x\) è il valore medio delle letture e \(U\) l'incertezza assoluta dichiarata, espressa nella stessa unità. Il segno ± indica un'estensione di ampiezza \(U\) da entrambi i lati del valore riportato. L'incertezza non dice da sola quanto siamo lontani da un riferimento.[^1]

Nel metodo scolastico semplificato usiamo la maggiore fra la semidispersione (d) e il passo leggibile (q) come stima didattica dell'incertezza:[^2]

\[
U=\max(d,q)
\]

La scrittura \(\max(d,q)\) significa “scegli il maggiore fra i due”. Se le letture coincidono e \(d=0\), il passo dello strumento continua a limitare la lettura. Per la tabella, 0,09 s è maggiore di 0,01 s: scegliamo quindi 0,09 s e scriviamo:

\[
t=(2{,}40\pm0{,}09)\,\mathrm{s}
\]

Questa scrittura associa al valore medio un intervallo da 2,31 s a 2,49 s, che in questo esempio coincide con gli estremi osservati. In una serie asimmetrica la fascia centrata sulla media e l'intervallo minimo–massimo possono essere diversi. Il display da solo non basta a stabilire l'incertezza: dobbiamo considerare anche come sono state effettuate le misure.

[TAB-07-1 — Prospetto concordato: valore attribuito, incertezza, riferimento ed errore. L'ultima riga anticipa il confronto spiegato nella sezione seguente.]

| Informazione | Valore nell'esempio | Che cosa comunica |
| --- | --- | --- |
| Valore medio della durata | 2,40 s | Il valore centrale riportato come risultato |
| Incertezza didattica stimata | 0,09 s | Il maggiore fra semidispersione e passo leggibile |
| Riferimento indipendente | 2,50 s | Il valore con cui confrontare il risultato |
| Errore con segno | −0,10 s | Quanto il risultato è sotto il riferimento |

## Quanto ci siamo spostati dal riferimento?

Per calcolare un **errore di misura** serve un valore di riferimento. Supponiamo che un sistema indipendente e più affidabile attribuisca allo stesso evento la durata di 2,50 s. Possiamo allora confrontarla con i nostri 2,40 s. I due numeri riguardano la stessa grandezza e sono espressi nella stessa unità. Il valore che confrontiamo con il riferimento è ora la media delle cinque letture.

L'errore con segno è la differenza fra il valore medio e quello di riferimento:

\[
e=\bar x-x_{\mathrm{rif}}
\]

Qui \(e\) è l'errore, mentre \(x_{\mathrm{rif}}\) è il riferimento. Un errore positivo indica un risultato maggiore del riferimento; uno negativo indica un risultato minore. Nel nostro confronto:

\[
e=2{,}40\,\mathrm{s}-2{,}50\,\mathrm{s}=-0{,}10\,\mathrm{s}
\]

Abbiamo dunque riportato una durata inferiore al riferimento di un decimo di secondo. Se ci interessa l'entità dello scarto senza il verso, prendiamo il **valore assoluto dell'errore**:

\[
|e|=0{,}10\,\mathrm{s}
\]

Per capire quanto pesa lo scarto rispetto alla durata di riferimento usiamo l'**errore relativo**, qui definito mediante il valore assoluto dello scarto:

\[
e_{\mathrm r}=\frac{|e|}{|x_{\mathrm{rif}}|}
\]

Il riferimento deve essere diverso da zero. Numeratore e denominatore hanno la stessa unità, che si semplifica: l'errore relativo è un numero senza unità. A parità di scarto assoluto, un riferimento doppio darebbe un errore relativo dimezzato. Nell'esempio:

\[
e_{\mathrm r}=\frac{0{,}10\,\mathrm{s}}{2{,}50\,\mathrm{s}}=0{,}04
\]

L'**errore percentuale** esprime lo stesso rapporto in percento:

\[
e_{\%}=e_{\mathrm r}\cdot100\%
\]

\[
e_{\%}=0{,}04\cdot100\%=4\%
\]

Lo scarto di 0,10 s è quindi il 4% dei 2,50 s di riferimento: equivale a un venticinquesimo di quella durata. L'errore con segno conserva l'informazione che abbiamo sottostimato il tempo; il valore relativo e la percentuale appena definiti descrivono l'entità dello scarto rispetto alla scala del confronto.

Per eseguire un confronto di questo tipo:
1. Verifica che risultato e riferimento riguardino la stessa grandezza e usa la stessa unità.
2. Sottrai il riferimento dal valore misurato per trovare l'errore con segno.
3. Prendi il valore assoluto per esprimere l'entità dello scarto.
4. Dividi per il valore assoluto del riferimento non nullo e, se serve, esprimi il rapporto in percento.

L'errore assoluto dell'esempio, 0,10 s, è un po' maggiore della stima didattica dell'incertezza, 0,09 s. Il riferimento cade appena fuori dall'intervallo dichiarato: è un motivo per ricontrollare come abbiamo valutato la misura e quali contributi abbiamo considerato. Non basta da solo a identificare uno specifico errore sistematico.

Se invece mancasse il riferimento, non potremmo eseguire quella sottrazione né calcolare l'errore percentuale effettivo. Potremmo comunque stimare l'incertezza usando ciò che sappiamo dello strumento e della procedura. È questa la differenza fra le due domande: “di quanto differisce dal riferimento?” e “con quale incertezza attribuiamo questo valore alla grandezza?”.

## Una massa nota e una massa da misurare

La bilancia virtuale ha proprietà fisse, riportate nella scheda dello strumento. Sono disponibili due campioni: uno ha una massa di riferimento nota, l'altro una massa da determinare. Per ciascuno puoi effettuare misure ripetute e registrare le letture in una serie separata.

[SIM-07 — Bilancia a proprietà fisse con campione A di riferimento 100 g e campione B di massa ignota; portata 500 g, passo 1 g, sensibilità del sensore dichiarata e non regolabile. Dati del modello simulati. Sotto la bilancia, grafico a punti delle letture, media e confronto con il riferimento per A; media, semidispersione e fascia ±U per B. Dettagli in simulazione.md; nessun codice ancora realizzato.]

Misura più volte la massa nota e calcola la media delle letture. Confrontandola con il riferimento puoi stimare l'errore del risultato medio; ogni singolo punto mostra invece una singola lettura. Lo scarto della media dal riferimento e la dispersione dei punti sono informazioni diverse: una serie può essere raccolta ma spostata.

Passa poi al campione ignoto. Calcola la media e la semidispersione, confronta quest'ultima con il passo leggibile e usa il criterio didattico appena descritto per proporre un'incertezza. Scrivi il risultato come valore medio ± incertezza, in grammi. Per questa attività la bilancia è regolata sullo zero; se il controllo con la massa nota suggerisce uno spostamento persistente, occorre controllare lo strumento prima di fidarsi della sola dispersione.

Il grafico sotto la bilancia mostra come si distribuiscono le letture. Per la massa nota puoi visualizzare riferimento, media e segmento dell'errore; per quella ignota, media e fascia dell'incertezza. Gli estremi osservati servono a leggere la semidispersione, mentre la fascia ±U è centrata sul valore medio: non sono necessariamente lo stesso intervallo. La massa nascosta non compare nel grafico, perché non la conosceresti durante una misura reale.

## Domande di verifica

1. Nell'infografica dei bersagli, quale gruppo di punti è preciso ma poco accurato? Spiega con le parole “dispersione” e “riferimento”.
2. Se non conosci il valore di riferimento, puoi calcolare l'errore percentuale effettivo? Puoi comunque stimare l'incertezza? Motiva.
3. Ricava dalla tabella la media e la semidispersione; poi spiega perché un display che mostra 0,01 s non basta a dichiarare un'incertezza di 0,01 s.
4. Vero o falso? «Ripetere molte volte una misura elimina anche uno zero spostato dello strumento». Spiega usando il voltmetro.
5. Confronta una variazione imprevedibile nell'avvio del cronometro, uno zero spostato del voltmetro e una trascrizione errata: a quale categoria appartiene ciascun caso e quale controllo sarebbe utile?
6. Che cosa significano i due numeri nella scrittura \(t=(2{,}40\pm0{,}09)\,\mathrm{s}\)? Perché non possiamo leggere automaticamente 0,09 s come l'errore effettivo?
7. Nel confronto dell'esempio, l'errore è −0,10 s. Che cosa comunica il segno meno? Quale informazione si perde passando al valore assoluto?
8. A parità di errore assoluto, se il valore di riferimento raddoppia, come cambia l'errore relativo? Motiva usando la formula.
9. Nella simulazione, quale confronto puoi fare per la massa nota che non puoi fare per quella ignota? Spiega come media, semidispersione e passo leggibile entrano invece nella stima dell'incertezza della massa ignota.

## Note

[^1]: Il significato preciso dell'intervallo dipende da come è stata valutata e dichiarata l'incertezza. Il simbolo ± non garantisce da solo che il valore della grandezza sia certamente compreso fra i due estremi.

[^2]: La regola del maggiore fra semidispersione e passo è una stima scolastica, non un calcolo generale dell'incertezza. Può lasciare fuori taratura, ambiente e altri contributi sistematici; non attribuisce una probabilità all'intervallo e non garantisce che contenga il valore di riferimento.

---

## Servizio editoriale — provenienza e verifiche

Questa sezione non appartiene al contenuto didattico visibile dell'HTML.
Bozza v4. Ultima richiesta: «No allora metti media e semi dispersione nel cap 7». Trasferiti qui i contenuti sulle misure ripetute, superando il precedente rinvio all'8: tabella e grafico originali delle cinque letture, media, semidispersione e regola scolastica del maggiore fra semidispersione e passo. Eliminato il capitolo autonomo sulle misure ripetute; piano aggiornato a undici capitoli, con i successivi rinumerati.
Fonte: strumenti_errori_incertezza_it.html v7, blob 1d65637b40f2af68e1e1ff55c7d1710259b6087b, sezioni #errori, #incertezza e #confronto. Quesiti originali 5, 7 e 6 conservati integralmente come domande 1, 2 e 3; 1–4 al capitolo 6. Totale nove quesiti nel 7.
Conservati i dati illustrativi originali: tempi 2,31 / 2,37 / 2,40 / 2,43 / 2,49 s; media 2,40 s; d = 0,09 s; q = 0,01 s; riferimento 2,50 s; errore −0,10 s; rapporto 0,04 e percentuale 4%. La stima dell'incertezza del cronometro è ora ricavata con il metodo scolastico descritto, non assegnata.
Verificare che il grafico distingua min–max, semidispersione, fascia centrata sulla media ed errore rispetto al riferimento; non imporre una distribuzione simmetrica alle nuove letture simulate. La regola U = max(d,q) è dichiarata didattica e non universale.
SIM-07 aggiornata alla richiesta di massa nota, massa ignota e grafico sotto la bilancia. Parametri numerici proposti nella specifica; un eventuale errore nullo della media resta valido. Bilancia regolata sullo zero nel modello corrente; nessun riferimento nascosto B visibile nei controlli o nel grafico.
Riferimenti terminologici da associare ai crediti: JCGM 200:2012 (VIM) e JCGM 100:2008 (GUM), https://www.bipm.org/en/committees/jc/jcgm/publications . La regola scolastica è ripresa dal sorgente storico, non attribuita a questi documenti come procedura generale.
COP-07 scelta dall'utente: [TV noise.jpg](https://commons.wikimedia.org/wiki/File:TV_noise.jpg), Mysid, pubblico dominio per dichiarazione dell'autore (PD-self), verificato nella pagina Commons. Usare l'immagine intera, senza ritagli o zoom. URL esatto fornito conservato in visuali.md.
Diritti delle foto del corpo e dei bersagli storici ancora da verificare; l'utente intende fornire immagini sostitutive con licenza. Copertina scelta e impostazione delle due attività autorizzate; testo aggiornato e dettagli del modello da revisionare. Nessun codice, HTML, merge o deployment avviato.

### Avvio autorizzato

«Ok vai» approva il testo corrente e autorizza realizzazione HTML e simulazioni secondo la proposta e la stima. Le immagini mancanti saranno fornite dall’utente; non dedurre scelte o licenze. Nessun merge o pubblicazione autorizzato.

### Bilancia e pesetti generati su richiesta

L’utente autorizza la generazione della bilancia e dei pesetti per le simulazioni. Nuovi originali preservati; immagini riutilizzate per lo stesso strumento nei due capitoli. I pesetti sono rappresentati anche sul piatto e la lettura è sovrapposta al display dallo script; per il campione ignoto il pesetto non ha massa scritta. Nessuna nuova didascalia.

## Immagini teoriche correnti

Scelte direttamente dall’utente: manometro MAXIMATOR (Photo by CEphoto, Uwe Aranas, CC BY-SA 3.0), termometro clinico (Jacek Halicki, CC BY-SA 4.0), cronometro (Lesselich, CC BY-SA 3.0). Bersagli ricreati su richiesta con geometria originale e scritte italiane, dal riferimento concettuale Ossila. Tutti i materiali del corpo ora disponibili; le annotazioni precedenti conservano la cronologia. Crediti e provenienze nel registro unico e negli snapshot offline.

Revisione corrente: errore sistematico illustrato dal voltmetro con lo zero spostato verso valori negativi fornito dall’utente, con testo e quesiti aggiornati. Credito: Желуденко Павло, CC BY 4.0.
