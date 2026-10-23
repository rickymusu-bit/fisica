# Errori e incertezza di misura

[EDITORIALE — Bozza v2, 23 ottobre 2026. Testo da approvare; visuali concordate con «Ok». Area: Introduzione alla fisica e alla misura.]

[COP-07 — Fotografia scelta dall'utente: TV noise.jpg. Intera, senza ritagli o zoom, non ripetuta nel corpo.]

*Rumore sullo schermo di un televisore analogico sintonizzato su un canale senza trasmissioni: i disturbi possono produrre variazioni nell'uscita di un dispositivo.*

## Lo stesso evento, letture diverse

Un cronometro mostra 2,40 s. Ripetendo la misura della durata di uno stesso evento potremmo ottenere letture un po' diverse, anche se il display continua a mostrare i centesimi di secondo. Da dove arrivano queste differenze? E, se il numero resta sempre uguale, possiamo essere sicuri di aver misurato bene?

La misura coinvolge lo strumento, il modo in cui lo usiamo e le condizioni della prova. Per separare questi contributi conviene distinguere due situazioni: le letture possono disperdersi in modo imprevedibile, oppure risultare spostate in modo simile rispetto a un riferimento. Le due cose possono anche accadere insieme.

[SCH-07-1 — Schema concordato con foto originale del cronometro, conservata intera e senza cambiare le cifre del display. Etichette esterne: “Evento di cui si misura la durata”; “Valore attribuito: 2,40 s”; “Incertezza assegnata: 0,09 s”; “Riferimento indipendente: 2,50 s”. Dati illustrativi. Nessun secondo dispositivo inventato. Le etichette descrivono l'esempio, non una misura documentata dalla fotografia. Collocare prima dei calcoli; richiamare lo stesso schema lungo la spiegazione.]

*Il risultato e il riferimento descrivono la durata dello stesso evento. Lo schema raccoglie i dati illustrativi usati nel confronto.*

Quando avviamo e fermiamo il cronometro a mano, il momento in cui premiamo il tasto non è identico a ogni prova. Queste variazioni possono contribuire agli **errori casuali**, che cambiano in modo imprevedibile fra misure ripetute. Ripetere ci aiuta a osservare la dispersione e a rendere il risultato meno dipendente da una singola lettura. Non elimina però ogni possibile spostamento.

Pensiamo ora a una bilancia il cui zero sia spostato: anche senza carico indica 2 g. Nelle condizioni considerate, le letture risultano maggiori di circa 2 g rispetto a quelle che otterremmo con lo zero corretto. Questo è un esempio di **errore sistematico**: un contributo che rimane costante o cambia in modo prevedibile. Ripetere la misura non lo cancella; occorre controllare lo zero, correggere la procedura o confrontare lo strumento con un riferimento.

[FIG-07-2 — Foto originale della bilancia digitale, intera e senza alterare il display. Lo zero spostato è una situazione ipotetica spiegata nel testo, non un difetto accertato dello strumento fotografato.]

*Il controllo dell'indicazione senza carico aiuta a individuare uno zero spostato prima di misurare.*

Diverso ancora è uno **sbaglio grossolano**: trascrivere 23,4 g invece di 32,4 g, confondere grammi e chilogrammi oppure usare il comando sbagliato. Qui non stiamo descrivendo una normale variazione fra letture, ma un problema nella procedura o nella registrazione. Un dato molto lontano dagli altri invita a controllare gli appunti e la prova; non si elimina automaticamente perché disturba il risultato.

## Punti raccolti e punti spostati

I bersagli permettono di vedere la differenza fra dispersione e spostamento. Immaginiamo che ogni punto rappresenti una lettura e che il centro indichi un riferimento noto. Punti molto vicini fra loro corrispondono a letture precise; per l'accuratezza conta anche la loro vicinanza al riferimento.

[FIG-07-1 — Infografica originale dei quattro bersagli A, B, C e D, senza ridisegno o modifica delle etichette. Verificare prima dell'HTML la leggibilità e i diritti.]

*In A i punti sono raccolti e centrati; in B raccolti ma spostati; in C dispersi attorno al centro; in D dispersi e spostati.*

Il gruppo B mostra perché una serie precisa può essere poco accurata. Aggiungere altri punti nello stesso gruppo renderebbe ancora più evidente la loro concentrazione, ma non li riporterebbe al centro. Analogamente, molte letture simili della bilancia con lo zero spostato non risolvono il problema dello zero.

Nel gruppo C, invece, le letture sono disperse, pur essendo distribuite attorno al riferimento. La dispersione è un'informazione utile, ma non basta per ricostruire ogni contributo alla misura. Per questo un risultato deve comunicare anche quanto è incerto.

## Che cosa significa il segno ±?

Dire soltanto “2,40 s” lascia aperta una domanda: con quale incertezza attribuiamo quel valore alla durata? L'**incertezza di misura** descrive la dispersione dei valori che possiamo attribuire alla grandezza sulla base delle informazioni disponibili. Per valutarla si considerano lo strumento, il metodo, le condizioni e, quando ci sono, le letture ripetute.

Una scrittura comune del risultato è:

\[
x=x_{\mathrm m}\pm U
\]

Il simbolo \(x\) indica la grandezza misurata; \(x_{\mathrm m}\) è il valore attribuito e \(U\) l'incertezza assoluta dichiarata, espressa nella stessa unità. Il segno ± indica un'estensione di ampiezza \(U\) da entrambi i lati del valore riportato. L'incertezza non dice da sola quanto siamo lontani da un riferimento.[^1]

Nel nostro esempio assegniamo, a scopo illustrativo, un'incertezza di 0,09 s al valore 2,40 s:

\[
t=(2{,}40\pm0{,}09)\,\mathrm{s}
\]

Questa scrittura associa al valore riportato un intervallo da 2,31 s a 2,49 s. Il numero 0,09 s è un dato dell'esempio: non lo stiamo ricavando dal passo del cronometro o da una serie di prove. Un display che mostra 0,01 s non autorizza ad assegnare automaticamente un'incertezza di 0,01 s, perché lascia fuori il contributo dell'operatore e le altre condizioni.

[TAB-07-1 — Prospetto concordato: valore attribuito, incertezza, riferimento ed errore. L'ultima riga anticipa il confronto spiegato nella sezione seguente.]

| Informazione | Valore nell'esempio | Che cosa comunica |
| --- | --- | --- |
| Valore attribuito alla durata | 2,40 s | Il valore riportato come risultato |
| Incertezza assoluta assegnata | 0,09 s | L'estensione dell'incertezza dichiarata |
| Riferimento indipendente | 2,50 s | Il valore con cui confrontare il risultato |
| Errore con segno | −0,10 s | Quanto il risultato è sotto il riferimento |

## Quanto ci siamo spostati dal riferimento?

Per calcolare un **errore di misura** serve un valore di riferimento. Supponiamo che un sistema indipendente e più affidabile attribuisca allo stesso evento la durata di 2,50 s. Possiamo allora confrontarla con i nostri 2,40 s. I due numeri riguardano la stessa grandezza e sono espressi nella stessa unità.

L'errore con segno è la differenza fra il valore attribuito e quello di riferimento:

\[
e=x_{\mathrm m}-x_{\mathrm{rif}}
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

L'errore assoluto dell'esempio, 0,10 s, è un po' maggiore dell'incertezza assegnata, 0,09 s. Il riferimento cade appena fuori dall'intervallo dichiarato: è un motivo per ricontrollare come abbiamo valutato la misura e quali contributi abbiamo considerato. Non basta da solo a identificare uno specifico errore sistematico.

Se invece mancasse il riferimento, non potremmo eseguire quella sottrazione né calcolare l'errore percentuale effettivo. Potremmo comunque stimare l'incertezza usando ciò che sappiamo dello strumento e della procedura. È questa la differenza fra le due domande: “di quanto differisce dal riferimento?” e “con quale incertezza attribuiamo questo valore alla grandezza?”.

## Domande di verifica

1. Nell'infografica dei bersagli, quale gruppo di punti è preciso ma poco accurato? Spiega con le parole “dispersione” e “riferimento”.
2. Se non conosci il valore di riferimento, puoi calcolare l'errore percentuale effettivo? Puoi comunque stimare l'incertezza? Motiva.
3. Vero o falso? «Ripetere molte volte una misura elimina anche uno zero spostato dello strumento». Spiega usando la bilancia.
4. Confronta una variazione imprevedibile nell'avvio del cronometro, uno zero spostato della bilancia e una trascrizione errata: a quale categoria appartiene ciascun caso e quale controllo sarebbe utile?
5. Che cosa significano i due numeri nella scrittura \(t=(2{,}40\pm0{,}09)\,\mathrm{s}\)? Perché non possiamo leggere automaticamente 0,09 s come l'errore effettivo?
6. Nel confronto dell'esempio, l'errore è −0,10 s. Che cosa comunica il segno meno? Quale informazione si perde passando al valore assoluto?
7. A parità di errore assoluto, se il valore di riferimento raddoppia, come cambia l'errore relativo? Motiva usando la formula.
8. Una lettura è molto lontana dalle altre. Scegli la risposta più ragionevole e motivala: eliminarla subito; considerarla automaticamente corretta; controllare procedura e registrazione prima di decidere.

## Note

[^1]: Il significato preciso dell'intervallo dipende da come è stata valutata e dichiarata l'incertezza. Il simbolo ± non garantisce da solo che il valore della grandezza sia certamente compreso fra i due estremi.

---

## Servizio editoriale — provenienza e verifiche

Questa sezione non appartiene al contenuto didattico visibile dell'HTML.
Fonte: `strumenti_errori_incertezza_it.html` v7, blob `1d65637b40f2af68e1e1ff55c7d1710259b6087b`, sezioni #errori e #confronto.
Quesiti originali 5 e 7 conservati integralmente come quesiti 1 e 2; aggiunti 3–8. Originali 1–4 al capitolo 6, originale 6 riservato all'8.
Conservati valori del confronto originale: 2,40 s, 2,50 s, −0,10 s, 0,04, 4%. Il risultato e U = 0,09 s sono assegnati per rendere il capitolo autonomo: nessun calcolo di media, semidispersione o stima complessiva dell'incertezza. I dati sono illustrativi, non misure realmente effettuate.
La comparazione |e| > U invita al controllo e non dimostra da sola un errore sistematico. Non viene attribuita una probabilità all'intervallo; la valutazione dell'incertezza del riferimento non è sviluppata in questo esempio introduttivo.
Riferimenti terminologici da associare ai crediti dell'HTML: JCGM 200:2012 (VIM), voci 2.16–2.20 e 2.26; JCGM 100:2008 (GUM); https://www.bipm.org/en/committees/jc/jcgm/publications . Indicazioni bibliografiche, non nuova verifica web.
Diritti delle foto e dei bersagli storici ancora da verificare nel registro e sulle fonti. Schema del cronometro descritto dal segnaposto, non ancora realizzato; nessuna immagine generata o alterata.
Impostazione visuale concordata con «Ok» nella PR #72. Testo v1 da approvare; nessun HTML, simulazione, merge o deployment avviato.

### Copertina scelta dall'utente — bozza v2

COP-07: [TV noise.jpg](https://commons.wikimedia.org/wiki/File:TV_noise.jpg); autore Mysid. Stato dei diritti verificato nella pagina Commons: Pubblico dominio per dichiarazione dell'autore (PD-self). [URL esatto fornito](https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a8/TV_noise.jpg/1920px-TV_noise.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail). Nessuna modifica richiesta: usare l'immagine intera, senza zoom; acquisizione e incorporamento del file nella fase HTML autorizzata. La copertina sostituisce la proposta del sismografo, che resta nel sorgente storico. Testo didattico invariato salvo la didascalia. La fotografia è descritta dalla scheda originale, senza dedurre prestazioni quantitative o cause fisiche non documentate.
