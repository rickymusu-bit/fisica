# Temperatura ed equilibrio termico

Bozza v1 · 19 ottobre 2026. Testo da approvare; segnaposto visuali da sostituire prima dell’HTML.

[IMMAGINE COP-01 — Fotografia di un termometro meteorologico in un contesto reale, con scala leggibile. Originale da ricevere. Copertina non ripetuta nel corpo.]

Didascalia proposta: La scala del termometro permette di esprimere con un numero la temperatura dell’ambiente.

## Quando possiamo fidarci del termometro?

Immergiamo un termometro in una bevanda e osserviamo la lettura. Nei primi istanti il valore può cambiare, poi si stabilizza. La bevanda era già lì, ma lo strumento ha avuto bisogno di tempo: quando possiamo fidarci della temperatura indicata?

[IMMAGINE FIG-01 — Termometro o sonda immerso in acqua, con la parte sensibile lontana dal fondo e dalle pareti. Originale da ricevere; nella foto non saranno aggiunti valori o andamenti temporali non documentati.]

Didascalia proposta: La parte sensibile del termometro è immersa nel liquido. Per misurarne la temperatura bisogna attendere che strumento e liquido raggiungano l’equilibrio termico.

Prima dell’immersione, il termometro può trovarsi a una temperatura diversa da quella della bevanda. Il contatto permette un trasferimento di energia dal corpo a temperatura maggiore a quello a temperatura minore, e anche la temperatura dello strumento cambia. Se la bevanda è più calda, il termometro si riscalda; se è più fredda, si raffredda. Il cambiamento della lettura accompagna questo avvicinamento.

La **temperatura** è la grandezza fisica che permette di confrontare lo stato termico dei corpi e prevedere il verso di questo trasferimento. La indichiamo con il simbolo **T**. Due corpi possono essere fatti di materiali diversi e avere dimensioni molto diverse, ma trovarsi alla stessa temperatura.

## Arrivare alla stessa temperatura

Quando due corpi a temperature diverse vengono messi in contatto termico, tendono a raggiungere una temperatura comune. Se non intervengono altri cambiamenti, la differenza si riduce fino a scomparire. Si parla allora di **equilibrio termico**: i corpi hanno la stessa temperatura e non c’è più un trasferimento netto di energia tra loro dovuto a una differenza di temperatura.

Questo è il motivo per cui occorre attendere prima di leggere un termometro per contatto. All’inizio lo strumento sta ancora cambiando temperatura; all’equilibrio, la sua temperatura coincide con quella del corpo con cui è in contatto. Per ottenere una misura utile, il termometro deve inoltre alterare il meno possibile ciò che misura: uno strumento molto ingombrante rispetto alla quantità di liquido potrebbe modificarne sensibilmente la temperatura.

[IMMAGINE FIG-02 — Riutilizzo concordato della fotografia del caffè conservata in ../termodinamica_sistemi/risorse/caffe.jpg. Nessuna temperatura ricavata dall’immagine.]

Didascalia proposta: Una bevanda calda lasciata in una stanza tende alla temperatura dell’ambiente circostante.

La bevanda non scambia energia soltanto con il termometro. Anche la tazza e l’ambiente circostante partecipano agli scambi: se la stanza rimane alla stessa temperatura, col tempo la bevanda tende a raggiungerla. Per questo una lettura che smette di cambiare non basta, da sola, a garantire l’equilibrio: occorre che la parte sensibile sia collocata correttamente e che lo strumento abbia avuto il tempo di rispondere.

## Il principio che rende possibile la misura

Come possiamo confrontare due corpi senza metterli direttamente in contatto tra loro? Possiamo usare lo stesso termometro, attendendo ogni volta l’equilibrio. Se i due corpi portano il termometro alla stessa temperatura, concludiamo che hanno la stessa temperatura anche tra loro.

Questa proprietà è espressa dal **principio zero della termodinamica**: se un corpo A è in equilibrio termico con un corpo C e un corpo B è in equilibrio termico con lo stesso corpo C, allora A e B sono in equilibrio termico tra loro. Il corpo C può essere proprio il termometro. Il principio permette quindi di attribuire alla temperatura un significato comune, confrontabile attraverso uno strumento.

Per trasformare questo confronto in una lettura numerica si sfrutta una proprietà del termometro che cambia con la temperatura. In un termometro a liquido cambia il livello nella colonnina; in una sonda elettronica può cambiare la resistenza elettrica di un sensore. La **taratura** stabilisce la corrispondenza tra quella proprietà e i valori della scala. Il tipo di sensore può cambiare, mentre resta la necessità di una relazione affidabile tra ciò che lo strumento rileva e la temperatura.

## Tre scale per la stessa temperatura

Il numero indicato da un termometro dipende dalla scala adottata. Nella vita quotidiana usiamo soprattutto i **gradi Celsius**, con simbolo **°C**. Nella scala Celsius, la fusione del ghiaccio avviene intorno a 0 °C e l’ebollizione dell’acqua intorno a 100 °C, alla pressione atmosferica standard.[^1]

L’unità di temperatura del Sistema internazionale è invece il **kelvin**, con simbolo **K**, senza il segno di grado. La scala Kelvin parte dallo **zero assoluto**, che corrisponde a −273,15 °C. È il limite inferiore della temperatura nella trattazione che stiamo usando; non va interpretato come la condizione in cui ogni movimento microscopico scompare.[^2]

Un intervallo di un kelvin ha la stessa ampiezza di un intervallo di un grado Celsius. Cambia l’origine della scala: a 0 °C corrispondono 273,15 K. Per passare da una lettura Celsius a una lettura Kelvin basta quindi aggiungere 273,15 al valore numerico:

\[
\frac{T}{\mathrm{K}}
=
\frac{T}{^\circ\mathrm{C}}+273{,}15
\]

Qui \(T/\mathrm{K}\) indica il valore numerico della temperatura espresso in kelvin e \(T/^\circ\mathrm{C}\) quello espresso in gradi Celsius. I due membri descrivono la stessa temperatura con unità diverse. Lo scarto tra le due letture resta sempre uguale, qualunque sia la temperatura considerata; nella conversione inversa si sottrae 273,15.

[TABELLA TAB-01 — Corrispondenze delle tre scale. Stessa struttura su desktop e smartphone; dati sotto riportati, da realizzare come tabella HTML semantica.]

| Riferimento | Celsius | Kelvin | Fahrenheit |
| --- | ---: | ---: | ---: |
| Zero assoluto | −273,15 °C | 0 K | −459,67 °F |
| Fusione del ghiaccio[^1] | circa 0 °C | circa 273,15 K | circa 32 °F |
| Temperatura di 20 °C | 20 °C | 293,15 K | 68 °F |
| Ebollizione dell’acqua[^1] | circa 100 °C | circa 373,15 K | circa 212 °F |

Didascalia proposta: Ogni riga indica la stessa temperatura nelle tre scale. Tra fusione del ghiaccio ed ebollizione dell’acqua, l’intervallo è circa 100 °C, 100 K oppure 180 °F.

La scala **Fahrenheit**, ancora comune negli Stati Uniti, usa i **gradi Fahrenheit**, con simbolo **°F**. Qui cambiano sia l’origine sia l’ampiezza del grado: all’intervallo tra 0 °C e 100 °C corrisponde quello tra 32 °F e 212 °F. Cento gradi Celsius di differenza equivalgono dunque a centottanta gradi Fahrenheit di differenza.

Per convertire una lettura Celsius in Fahrenheit bisogna tener conto di entrambi i cambiamenti:

\[
\frac{T}{^\circ\mathrm{F}}
=
\frac{9}{5}\cdot\frac{T}{^\circ\mathrm{C}}+32
\]

Il fattore \(\frac{9}{5}\) tiene conto della diversa ampiezza dei gradi; il termine 32 sposta l’origine. Per tornare dai Fahrenheit ai Celsius si procede nell’ordine inverso:

\[
\frac{T}{^\circ\mathrm{C}}
=
\frac{5}{9}\cdot
\left(\frac{T}{^\circ\mathrm{F}}-32\right)
\]

Le scale assegnano numeri diversi allo stesso stato termico. La tabella mostra, per esempio, che 20 °C, 293,15 K e 68 °F identificano la stessa temperatura: cambiare scala non significa riscaldare o raffreddare il corpo.

La distinzione diventa particolarmente utile quando leggiamo una **differenza di temperatura**, indicata con **ΔT**. Per Celsius e kelvin non bisogna aggiungere 273,15 a una differenza: lo spostamento dell’origine si cancella confrontando due letture. Per Fahrenheit rimane invece il fattore \(\frac{9}{5}\), perché l’ampiezza del grado è diversa. Un aumento di 10 °C corrisponde così a un aumento di 10 K oppure di 18 °F.

## Domande di verifica

1. Un termometro inizialmente alla temperatura della stanza viene immerso in acqua più fredda. Come prevedi che cambi la lettura? Che cosa deve accadere perché lo strumento e l’acqua siano in equilibrio termico?
2. **Vero o falso? Motiva.** Due corpi in equilibrio termico devono avere le stesse dimensioni ed essere fatti dello stesso materiale.
3. Due corpi A e B, confrontati separatamente con lo stesso termometro, lo portano alla medesima temperatura di equilibrio. Che cosa permette di concludere il principio zero?
4. Una sonda mostra un valore che non cambia, ma la parte sensibile è appoggiata alla parete del recipiente. Questa sola osservazione garantisce che il valore rappresenti la temperatura del liquido? Spiega.
5. **Scegli e motiva.** Una temperatura di 0 °C corrisponde a: A) 0 K; B) 273,15 K; C) −273,15 K. Perché lo zero Celsius non coincide con lo zero assoluto?
6. Nella tabella, 20 °C e 68 °F rappresentano temperature diverse? Come lo stabilisci?
7. **Vero o falso? Motiva.** Se la temperatura aumenta di 10 °C, aumenta di 283,15 K.
8. Un termometro indica 30 °C. Converti la lettura in kelvin e in gradi Fahrenheit, mostrando i passaggi. Poi indica a quanti kelvin e a quanti gradi Fahrenheit corrisponde un aumento di 5 °C.
9. **Vero o falso? Motiva.** All’equilibrio termico i corpi non possiedono più energia.

## Note

[^1]: I riferimenti dell’acqua sono indicati alla pressione atmosferica standard, pari a 101 325 Pa, per acqua pura. La temperatura di ebollizione cambia con la pressione.

[^2]: Il limite inferiore non significa arresto completo del moto microscopico: questa immagine sarebbe incompatibile con la descrizione quantistica della materia.
