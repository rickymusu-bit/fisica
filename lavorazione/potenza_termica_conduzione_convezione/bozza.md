# Potenza termica e trasmissione del calore

Perché due stufette che trasferiscono la stessa energia possono scaldare in tempi diversi? Come passa il calore attraverso i materiali e perché l’aria in movimento può accelerarne il trasferimento?

## Potenza termica

Immagina due stufette che forniscono entrambe 120 kJ di energia a una stanza. La prima impiega 60 secondi, la seconda 120 secondi. La quantità di energia trasferita è identica, ma la rapidità del trasferimento cambia: la prima è più potente.

[IMMAGINE 01 — Stufetta A — esempio ipotetico: 120 kJ in 60 s, quindi 2 000 W.]

Didascalia: Stufetta A — esempio ipotetico: 120 kJ in 60 s, quindi 2 000 W.

[IMMAGINE 02 — Stufetta B — esempio ipotetico: 120 kJ in 120 s, quindi 1 000 W.]

Didascalia: Stufetta B — esempio ipotetico: 120 kJ in 120 s, quindi 1 000 W.

La potenza termica indica quanta energia termica viene trasferita nell'unità di tempo.

$$P=\frac{Q}{\Delta t}$$

P è la potenza termica in watt (W), Q è l’energia trasferita in joule (J) e Δt è il tempo in secondi (s). Un watt corrisponde a un joule trasferito ogni secondo.

### Potenza, energia e tempo

Una stufetta da 1 000 W in due ore trasferisce, se mantiene quella potenza, la stessa energia di una da 2 000 W in un'ora. Aumentare la potenza non significa necessariamente consumare più energia per ottenere un identico trasferimento: conta anche per quanto tempo il dispositivo funziona. L'energia elettrica consumata nella pratica può dipendere anche dalle perdite e dai sistemi di controllo.

$$Q=P\cdot\Delta t$$

Per capire come limitare le dispersioni bisogna studiare attraverso che cosa l'energia attraversa una parete. È il problema della conduzione.

## Conduzione termica

Se lasci un cucchiaio di metallo immerso in una zuppa calda, dopo un po’ si riscalda anche la parte del manico fuori dal liquido. L’energia si è propagata lungo il metallo senza che il cucchiaio si sia spostato da un’estremità all’altra.

[IMMAGINE 03 — Il cucchiaio metallico riceve energia dalla zuppa calda e la conduce lungo il manico.]

Didascalia: Il cucchiaio metallico riceve energia dalla zuppa calda e la conduce lungo il manico.

La conduzione è il trasferimento di energia termica attraverso un materiale dovuto alle interazioni microscopiche tra le sue parti, senza trasporto macroscopico complessivo della materia. Nei metalli contribuiscono in modo rilevante anche gli elettroni liberi.

### Che cosa accade tra le particelle?

Nella rappresentazione qui sotto le particelle del solido oscillano intorno a posizioni pressoché fisse. Nella zona calda l'agitazione è mediamente maggiore; attraverso le interazioni l'energia si trasferisce verso la zona fredda. Le particelle non viaggiano tutte da un'estremità all'altra.

[SIMULAZIONE 04 — Modello semplificato: oscillazioni più ampie dove il materiale è più caldo; energia trasferita mediamente verso la zona più fredda.]

Didascalia: Modello semplificato: oscillazioni più ampie dove il materiale è più caldo; energia trasferita mediamente verso la zona più fredda.

### Conducibilità termica

La conducibilità termica λ descrive l'attitudine di un materiale a condurre il calore: a parità delle altre condizioni, maggiore è λ, più facilmente passa l'energia. Si misura in W/(m·K).

| Materiale | λ indicativa [W/(m·K)] |
| --- | --- |
| Rame | 400 |
| Alluminio | 205 |
| Acciaio comune | 50 |
| Vetro | 1,0 |
| Acqua | 0,6 |
| Neve compattata | 0,1–0,5 |
| Legno | 0,12 |
| Aria ferma | 0,026 |

Valori orientativi: dipendono dalla composizione, dalla temperatura e dalle condizioni del materiale.

[VIDEO 05 — Video dell’esperimento: scegli la miniatura per aprirlo sulla piattaforma originale.]

Didascalia: Video dell’esperimento: scegli la miniatura per aprirlo sulla piattaforma originale.

### La legge di Fourier per una parete piana

Consideriamo una parete omogenea, piana, di spessore s, attraversata da un flusso termico in condizioni stazionarie. Se le temperature ai due lati restano costanti, la potenza condotta è:

$$P=\frac{\lambda\cdot A\cdot\Delta T}{s}$$

A è la superficie della parete, s lo spessore, ΔT la differenza tra le temperature delle due facce. Nel modello consideriamo una parete omogenea, con conducibilità costante e senza sorgenti di calore al suo interno. A regime stazionario il profilo di temperatura è lineare nello spessore. In un edificio reale la temperatura dell’aria può differire da quella della superficie: gli scambi con l’aria richiedono anche di considerare la convezione. La potenza aumenta quando aumentano conducibilità, superficie o differenza di temperatura; diminuisce aumentando lo spessore.

[IMMAGINE 06 — Sezione del muro: correggere il profilo rosso, facendo avvenire l’intera diminuzione di temperatura soltanto nello spessore della parete. Specificare che 20 °C e −10 °C sono le temperature delle due facce nel modello, non automaticamente quelle dell’aria. Grafico ricostruito e verificato, senza cambiare i dati.]

Didascalia: In una parete omogenea, a regime stazionario e con conducibilità costante, la temperatura varia linearmente da una faccia all’altra. Nell’esempio le facce sono mantenute a 20 °C e −10 °C: la differenza di temperatura è 30 K. La superficie A è perpendicolare al flusso di calore.

### La caffettiera sul fornello

La fiamma riscalda la base metallica della caffettiera. Il calore si propaga attraverso il corpo di alluminio, che è un buon conduttore; per questo la parte metallica diventa molto calda. Il manico è invece realizzato in un materiale che conduce molto meno: a parità di condizioni può restare relativamente più tiepido, permettendo di afferrarlo con maggiore sicurezza. Non significa però che sia sempre freddo: dopo un riscaldamento prolungato anche il manico può scottare.

[IMMAGINE 07 — Il corpo metallico trasferisce rapidamente energia, mentre il manico poco conduttore ostacola il passaggio del calore fino alla mano.]

Didascalia: Il corpo metallico trasferisce rapidamente energia, mentre il manico poco conduttore ostacola il passaggio del calore fino alla mano.

Nelle pareti di una casa, uno strato poco conduttore ostacola il passaggio del calore. Il modello della parete omogenea aiuta a capire perché il materiale e lo spessore influenzano le dispersioni; una parete reale con più strati richiede invece di considerare insieme le loro resistenze termiche. La sezione del muro già discussa è il riferimento per questo modello.

### Finestre con vetrocamera

Nel doppio vetro, due lastre sono separate da uno spazio sigillato che contiene aria o un gas poco conduttore. Quando l’intercapedine e le condizioni sono progettate correttamente, si riduce il trasferimento di calore rispetto a un vetro singolo. L’effetto non dipende dalla sola conduzione: possono contribuire anche irraggiamento e piccoli moti del gas; perciò non applichiamo direttamente la formula di Fourier della parete omogenea all’intera finestra.

[IMMAGINE 09 — Sezione della vetrocamera: usare l’originale inglese recuperato dalla figura 08, tradurre le etichette preservando frecce, griglia e disegno, senza caselle sovrapposte.]

Didascalia: Le due lastre di vetro sono separate da un’intercapedine sigillata che limita gli scambi termici. Il distanziatore mantiene la distanza tra le lastre; il materiale essiccante assorbe l’umidità residua.

### Un igloo isolato dalla neve

Le pareti di neve non sono una sorgente di calore. La neve contiene numerose piccole cavità d’aria: l’aria intrappolata e quasi immobile conduce poco, contribuendo all’isolamento. Uno spessore sufficiente riduce la velocità con cui l’energia termica abbandona l’interno, che può quindi restare meno freddo dell’esterno quando sono presenti sorgenti di calore. Non basta dire che la neve è fredda: conta soprattutto come ostacola il trasferimento.

[IMMAGINE 10 — Le pareti di neve contengono aria intrappolata e limitano le perdite di calore verso l’esterno.]

Didascalia: Le pareti di neve contengono aria intrappolata e limitano le perdite di calore verso l’esterno.

### Il metallo sembra più freddo del legno

Se un oggetto metallico e uno di legno rimangono a lungo nella stessa stanza, possono trovarsi alla medesima temperatura. Il metallo sembra spesso più freddo perché sottrae energia alla pelle più rapidamente. All’aperto, quando un metallo è sotto zero, l’umidità della pelle o della lingua può congelare a contatto con esso: ecco perché aderire a una superficie gelata è pericoloso e non va provato.

[IMMAGINE 12 — Il contatto con metallo molto freddo può sottrarre rapidamente energia alla pelle: non va imitato.]

Didascalia: Il contatto con metallo molto freddo può sottrarre rapidamente energia alla pelle: non va imitato.

### Dissipatore di un processore

Un processore funzionante libera energia termica in una zona piccola. La base del dissipatore metallico riceve questa energia e la conduce verso molte alette sottili. Le alette aumentano la superficie a contatto con l’aria e favoriscono la dispersione; la ventola, quando presente, aumenta il ricambio d’aria. Il percorso completo combina dunque conduzione nel metallo e convezione verso l’aria.

[IMMAGINE 13 — Il calore passa dal processore alla base e alle alette metalliche prima di essere ceduto all’aria.]

Didascalia: Il calore passa dal processore alla base e alle alette metalliche prima di essere ceduto all’aria.

## Convezione termica

In un fluido, cioè in un liquido o in un gas, l’energia può essere trasportata dal movimento di una parte del fluido stesso. Questo meccanismo di trasferimento del calore è la convezione. Non significa che il calore sia una sostanza che viaggia: è la materia in movimento che trasporta energia interna da una regione all’altra.

### Convezione naturale

Quando alcune zone di un fluido vengono riscaldate più di altre, spesso si formano differenze di densità. Sotto l’azione della gravità, la spinta di Archimede può mettere il fluido in movimento: quello relativamente meno denso tende a salire, mentre quello relativamente più denso tende a scendere. È il principio della convezione naturale, anche se la forma reale dei moti dipende dalla geometria e dalle condizioni.

### Il termosifone e l’aria della stanza

Il termosifone riscalda l’aria che si trova nelle sue vicinanze: l’aria tende a espandersi, diventa meno densa e sale. L’aria relativamente più fredda presente dall’altra parte della stanza può scendere e tornare vicino al radiatore, alimentando un moto di circolazione. La presenza di finestre, arredi e pareti modifica il percorso reale, che non è un circuito perfettamente regolare. Inoltre il termosifone cede energia alla stanza anche per irraggiamento.

[IMMAGINE 14 — In una stanza, l’aria calda sale vicino al termosifone, mentre altra aria relativamente fredda torna verso il basso.]

Didascalia: In una stanza, l’aria calda sale vicino al termosifone, mentre altra aria relativamente fredda torna verso il basso.

### Le grandi circolazioni dell’atmosfera terrestre

L’Equatore riceve mediamente più energia solare delle regioni polari. Il riscaldamento disuguale, insieme alla gravità, contribuisce a mettere in moto enormi masse d’aria: l’aria può salire nelle fasce più calde, muoversi in quota e ridiscendere altrove. La rotazione terrestre devia i venti e, con altri fattori, organizza la circolazione in grandi celle, come quelle di Hadley, Ferrel e polari. Quindi i venti planetari non derivano soltanto dalla semplice regola «l’aria calda sale».

[IMMAGINE 15 — Modello semplificato della circolazione atmosferica: il riscaldamento non uniforme e la rotazione terrestre contribuiscono a determinare le grandi fasce dei venti.]

Didascalia: Modello semplificato della circolazione atmosferica: il riscaldamento non uniforme e la rotazione terrestre contribuiscono a determinare le grandi fasce dei venti.

### Il mantello terrestre

Il mantello della Terra è costituito soprattutto da rocce solide, non da un oceano di magma liquido. Su tempi lunghissimi, però, il materiale può deformarsi e scorrere lentissimamente. Le differenze di temperatura e densità, insieme alla gravità, favoriscono i moti convettivi; le forze legate alle placche, come la discesa delle placche fredde in subduzione, sono importanti. Lo schema mostra un modello semplificato: questi movimenti sono molto più lenti delle correnti d’aria e non hanno necessariamente celle regolari.

[IMMAGINE 16 — Modello dei movimenti lenti nel mantello: le rocce solide possono scorrere nel corso di milioni di anni.]

Didascalia: Modello dei movimenti lenti nel mantello: le rocce solide possono scorrere nel corso di milioni di anni.

### Convezione forzata

In altri casi il movimento del fluido viene prodotto o intensificato da un dispositivo, per esempio una ventola o una pompa. Si parla allora di convezione forzata. Una ventola non produce da sola il raffreddamento: rinnova l’aria a contatto con la superficie e permette di trasferire energia più rapidamente, se le condizioni termiche sono favorevoli.

### Il raffreddamento del processore

Il processore cede energia termica al dissipatore metallico. La base riceve il calore e lo conduce fino alle alette, che moltiplicano la superficie di contatto con l’aria senza richiedere un blocco di metallo massiccio. La ventola mette in movimento aria relativamente più fresca fra le alette, sostituendo l’aria già riscaldata e favorendo la convezione forzata. Senza un adeguato contatto termico con il processore o senza sufficiente circolazione dell’aria, il raffreddamento è meno efficace.

[IMMAGINE 17 — La ventola spinge aria tra le numerose alette; il metallo trasferisce prima il calore dal processore verso l’esterno.]

Didascalia: La ventola spinge aria tra le numerose alette; il metallo trasferisce prima il calore dal processore verso l’esterno.

### Il radiatore dell’automobile

Nel motore a combustione si produce energia termica che non deve accumularsi eccessivamente. Una pompa fa circolare il liquido refrigerante nel motore e nel radiatore: il liquido caldo entra nel radiatore, scorre dentro tubi metallici e cede energia alle pareti e alle fitte alette. L’aria che attraversa il radiatore asporta energia; la ventola mantiene o aumenta il flusso anche quando l’auto è ferma o procede lentamente. Le alette aumentano enormemente la superficie di scambio. Il termostato regola il passaggio del liquido in funzione della temperatura. Il circuito del riscaldamento dell’abitacolo, visibile nello schema, è un ramo distinto del circuito di raffreddamento.

[IMMAGINE 18 — Il liquido refrigerante trasporta energia dal motore al radiatore. La ventola favorisce il passaggio dell’aria attraverso le alette, che aumentano la superficie di scambio.]

Didascalia: Il liquido refrigerante trasporta energia dal motore al radiatore. La ventola favorisce il passaggio dell’aria attraverso le alette, che aumentano la superficie di scambio.

### Conduzione e convezione lavorano insieme

Nel radiatore dell’automobile e nel dissipatore del computer, l’energia attraversa prima parti metalliche per conduzione e passa poi all’aria in movimento con la convezione. Le alette sono utili proprio perché consentono al metallo di essere a contatto con una superficie d’aria molto più estesa. Nei sistemi reali anche l’irraggiamento può contribuire agli scambi termici.

[Crediti delle immagini da conservare in un elemento collassabile prima del piè di pagina, senza introdurli nelle didascalie.]

[Piè di pagina: nuova versione v5 e data della revisione, assegnate solo al consolidamento.]
