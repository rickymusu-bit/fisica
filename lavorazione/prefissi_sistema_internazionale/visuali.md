# Progettazione — I prefissi del Sistema internazionale

Versione v5 — 23 ottobre 2026. Capitolo 4 di **Introduzione alla fisica e alla misura**.
[Bozza v3](bozza.md) pronta per la revisione; [schema corrente](risorse/schema-conversioni.svg) invariato. Le decisioni precedenti sono conservate nello [stato](stato.md) e in Git.

## Indicazioni correnti dell'utente

- Riutilizzare la tabella originale dei 24 prefissi e lo schema SCH-01 autorizzato.
- Testo introduttivo con numeri decimali e linguaggio concreto; nella tabella introduttiva affiancare valori decimali e potenze di dieci.
- Dalla sezione «Un prefisso è una potenza di dieci» usare le potenze dove utili, senza imporle a ogni numero.
- Presentare formula, significato dei simboli e procedura in modo esplicito, affiancandole alla spiegazione discorsiva.
- Aggiungere esempi svolti anche con unità derivate.
- Non riutilizzare la copertina del metro: l'utente fornirà un'immagine nuova. Non cercare o generare alternative.

## Impostazione e visuali

Apertura sul cambio di unità: 1 m = 100 cm = 1000 mm. Il numero cambia, la lunghezza resta la stessa. La tabella collega poi le scritture decimali alle potenze.

| ID | Materiale corrente | Funzione |
| --- | --- | --- |
| COP-01 | Segnaposto per nuova immagine dell'utente; soggetto, didascalia e alt da definire dopo la ricezione. | Copertina pertinente, distinta dalle figure interne |
| TAB-02 | Tre colonne: scrittura iniziale, valore in metri in forma decimale, valore in metri con potenza di dieci. | Collegare intuitivamente le due scritture |
| TAB-01 | Tabella originale dei 24 prefissi, nomi/simboli/esponenti e disposizione invariati. | Riferimento per gli esponenti p e q |
| SCH-01 | SVG km–m–mm e cm–mm–µm, frecce nei due versi e fattori in potenze. | Leggere conversioni dirette e inverse |
| TAB-03A | Equivalenze mg, g e kg. | Applicare i prefissi al grammo |
| TAB-03B | Lunghezza, area e volume, fattori 10⁻², 10⁻⁴ e 10⁻⁶. | Riconoscere l'effetto dell'esponente dell'unità |
| CONV-01–04 | Segnaposto di schemi numerici con dato, unità di arrivo e fattore prima dei calcoli. | Esplicitare l'impostazione dei quattro esempi |

Gli schemi CONV non rappresentano apparecchi o oggetti: sono passaggi di equivalenze fra quantità assegnate. Non richiedono nuove fotografie. Composizione dello schema SVG da conservare su ogni dispositivo, con ingrandimento del tema nella futura integrazione.

La vecchia scala illustrata yotta–yocto resta nel sorgente storico. La foto del metro appartiene al capitolo 2 e non è una risorsa del capitolo 4.

## Formula e procedura

Definire le unità di partenza e arrivo come 10ᵖ U e 10ᑫ U, con lo stesso riferimento U; poi presentare l'uguaglianza della grandezza e la formula:

**x_arrivo = x_partenza · 10^(p − q)**.

Definire x come valore numerico, p e q come esponenti dei prefissi; per l'unità senza prefisso usare zero. Procedura in quattro passi: identificare le unità, leggere gli esponenti, calcolare p − q e applicare il fattore, controllare unità/verso e conversione inversa.

Per unità elevate a n, usare **x_arrivo = x_partenza · 10^[n(p − q)]**. Per unità composte sostituire separatamente i fattori del numeratore e del denominatore. Le formule complete, con frazioni, sono nella bozza.

## Esempi richiesti

1. Pressione: 2,4 MPa = 2400 kPa, fattore 10³. Il prefisso agisce sull'intero pascal, già unità derivata.
2. Area: 250 cm² = 0,025 m², fattore 10⁻⁴.
3. Volume: 4,5 mm³ = 0,0045 cm³, fattore 10⁻³.
4. Densità: 1,2 g/cm³ = 1200 kg/m³, fattore ottenuto dal rapporto fra 10⁻³ e 10⁻⁶.

Ogni esempio contiene dati, esponenti, schema numerico previsto, calcolo, unità e interpretazione quantitativa. Dieci quesiti finali coprono anche formula e unità derivate; nessuna soluzione anticipata.

## Prossimo passo

Revisione della bozza v3 e ricezione della nuova copertina. Prima dell'HTML seguire approvazione del testo, stima e via previsti dal master. Manifest e sito pubblico invariati; PR #65 in bozza.
