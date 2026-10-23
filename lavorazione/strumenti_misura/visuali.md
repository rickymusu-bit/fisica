# Capitolo 6 — Gli strumenti di misura: proposta
Versione v5 — 23 ottobre 2026 (Europe/Rome). Impostazione e visuali approvate con «Ok»; bozza testuale v4 con simulazione proposta.

## Domanda e confini
Una bilancia mostra molte cifre: basta questo per fidarsi della misura? Partire dal confronto fra lettura analogica e digitale, poi distinguere le caratteristiche che permettono di scegliere e usare uno strumento.
Fonte: `strumenti_errori_incertezza_it.html` v7, sezioni `#strumenti` e `#caratteristiche`; blob `1d65637b40f2af68e1e1ff55c7d1710259b6087b`.

## Progressione proposta
1. Analogico e digitale: lancetta e display, vantaggi e limiti; nessuna superiorità automatica del digitale.
2. Leggere una scala: osservazione frontale e parallasse. Conservare il disegno originale, senza ridisegnarlo.
3. Portata e intervallo: scala del voltmetro 0–15 V, scelta rispetto alla grandezza attesa. Non attribuire alla foto specifiche tecniche non documentate.
4. Prontezza: il termometro deve rispondere al cambiamento; la velocità con cui leggiamo le cifre non coincide con il tempo di risposta.
5. Risoluzione e sensibilità: distinguere il passo del display dalla risposta dello strumento. Esplicitare la relazione S = ΔI / Δx, con indicazione I, grandezza misurata x e unità dipendenti dalle due grandezze; frazione orizzontale nell'HTML. Conservare il confronto 2 mm per 1 °C / 1 mm per 1 °C. Il diverso uso scolastico di “sensibilità” va in una nota breve.
6. Precisione e accuratezza: letture vicine fra loro e vicinanza al riferimento sono proprietà diverse. Usare un prospetto di letture illustrative di una bilancia con riferimento dichiarato, non dati sperimentali reali. L'infografica dei bersagli resta nel capitolo 7 per interpretare dispersione e spostamento senza duplicarla.
7. Domande finali: conservare i quesiti originali 1–4; integrare confronti su risoluzione/sensibilità e precisione/accuratezza. Numero e formulazione definitivi nella bozza.

Classificazione degli errori, misure ripetute, media, semidispersione e incertezza appartengono al capitolo 7. Nel 6 il richiamo agli effetti sulla misura resta funzionale alle proprietà dello strumento.

## Visuali proposte
| ID | Materiale | Funzione e posizione |
| --- | --- | --- |
| COP-06 | Foto del doppio orologio atomico all'itterbio del NIST, scelta dall'utente | Copertina intera senza zoom, non ripetuta nel corpo; sostituisce la proposta del calibro |
| FIG-06-1 | Foto originali delle bilance analogica e digitale | Apertura: confrontare scala e display. Conservarle intere |
| FIG-06-2 | Disegno originale del parallasse | Lettura della scala: vista frontale e obliqua |
| FIG-06-3 | Foto originale del voltmetro 0–15 V | Portata e scelta dell'intervallo |
| FIG-06-4 | Foto originale del termometro | Prontezza e risposta del sensore; collegare anche il confronto sulla sensibilità senza attribuirlo al modello fotografato |
| FIG-06-5 | Foto originale del cronometro | Risoluzione visualizzata e limiti dell'azionamento manuale |
| TAB-06 | Nuovo prospetto numerico, concordato | Letture illustrative precise ma spostate rispetto a un riferimento, accanto alle bilance già presenti; nessun nuovo oggetto disegnato |

I materiali indicati sono già nel sorgente storico. Il riuso è stato approvato con «Ok»; resta necessaria la verifica delle licenze prima dell'integrazione. Nessuna ricerca o generazione avviata. I diritti individuali risultano non documentati nello snapshot dei crediti del sorgente: verificare le schede esistenti e le fonti prima dell'integrazione; non dedurre licenze. Se i materiali non sono utilizzabili, chiedere all'utente immagini pertinenti.
La dicitura “sensitivity” sul quadrante della bilancia analogica indica un passo di 20 g: spiegare la convenzione in nota, distinguendola dalla definizione metrologica. Non modificare le scritte nella fotografia.

Proposta iniziale senza simulazioni superata dalla successiva richiesta esplicita: aggiunta SIM-06, bilancia virtuale per esplorare le proprietà. Nessun video o esercizio svolto separato.

## Ripartizione dei quesiti originali
I quesiti 1, 2, 3 e 4 appartengono al capitolo 6. Il 5 sui bersagli e il 7 su errore/incertezza appartengono al 7. Il quesito originale 6 su media e semidispersione passa al capitolo 7, insieme a 5 e 7. Nessun quesito originale perso o duplicato.

Tema successivo: Stringhe comune, modello v24. Fonte delle regole: MASTER_PROMPT.md v69.11, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, docs/visual-guidelines.md v1.0.0.

## Copertina corrente scelta esplicitamente

COP-06: [Ytterbium Lattice Double Clock with Photons at NIST.jpg](https://commons.wikimedia.org/wiki/File:Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg), N. Phillips/NIST. Pubblico dominio: opera del governo federale statunitense, indicata PD-USGov su Commons. La richiesta diretta dell'utente sostituisce la proposta precedente del calibro. [File indicato dall'utente](https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7c/Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg/1920px-Ytterbium_Lattice_Double_Clock_with_Photons_at_NIST.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail). Conservare proporzioni e immagine intera, nessun ritaglio o zoom. Provenienza e diritti della copertina documentati; il punto aperto sui diritti riguarda ancora le immagini storiche del corpo. Nessuna immagine alternativa cercata o generata.

## Simulazione richiesta

[Specifica corrente](simulazione.md). Attività e segnaposto nella bozza v3; proprietà regolabili nel 6 e fisse nel 7. Stesso modello di base e stessa immagine pertinente della bilancia, da integrare dopo verifica dei diritti o scelta di una sostituzione fornita dall'utente. Nessuna immagine sostitutiva cercata o generata e nessuna programmazione avviata.

## Interfaccia e struttura aggiornate su richiesta

SIM-06: bilancia con pesetti di masse differenti; slider sotto la bilancia per le proprietà. SIM-07: bilancia a proprietà fisse, massa di riferimento nota e massa ignota, misure ripetute e grafico a punti sotto la bilancia. [Specifica corrente](simulazione.md). Nel 7 media, semidispersione, incertezza ed errore sono sviluppati in un unico capitolo; eliminata la precedente separazione con l'8. Il grafico distingue punti, media, riferimento, errore, estremi e fascia U; nessun valore di riferimento nascosto esposto per il campione ignoto.

Aggiunti nel 7 TAB-07-2 e GRAF-07-2 dal sorgente originale delle cinque letture. Nuove immagini necessarie per i pesetti da concordare/fornire, senza ricerca o generazione autonoma. Modelli numerici proposti e stima complessiva 2–3 ore da consolidare dopo la revisione dei testi. Nessun codice ancora realizzato.
