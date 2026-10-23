# Progettazione — I prefissi del Sistema internazionale

Versione v4 — 23 ottobre 2026. Capitolo 4 di **Introduzione alla fisica e alla misura**.
[Bozza v2](bozza.md) pronta per la revisione; [schema corrente](risorse/schema-conversioni.svg). La cronologia delle proposte è conservata in Git e nello [stato](stato.md).

## Scelte ricevute

L'utente ha richiesto di riutilizzare la tabella dei prefissi e di spiegare le conversioni tra prefissi. Con «Ok fai lo schema» ha autorizzato SCH-01.
La successiva richiesta impone le **potenze di 10 dovunque**, in continuità con il capitolo sulla notazione esponenziale. Tutti i fattori, le equivalenze e i passaggi numerici sono quindi espressi con potenze di 10, inclusi tabelle, schema, descrizioni accessibili e quesiti. La preferenza generale per i decimali moderati non si applica a queste conversioni.

## Filo della spiegazione

Aprire sul metro a nastro: 1 m = 10² cm = 10³ mm. Il numero cambia perché cambia l'unità scelta, mentre la lunghezza rimane la stessa.
Introdurre il prefisso come fattore esatto e interpretarlo mediante le potenze già incontrate nel capitolo precedente.

Spiegare conversioni in entrambi i versi, sostituendo il prefisso con la sua potenza oppure usando il rapporto dei fattori. Nei prodotti si sommano gli esponenti; nel rapporto si sottrae quello del prefisso di arrivo da quello di partenza. Non trattare tutte le righe della tabella come passi dello stesso valore.

Concludere con il grammo e con i prefissi nelle unità elevate a potenza. Nessuna digressione sulle cifre significative, video, simulazioni o nuova fotografia.

## Visuali nella bozza

| ID | Contenuto e posizione | Funzione |
| --- | --- | --- |
| COP-01 | Riuso integrale della [foto del metro](../grandezze_fisiche_sistema_internazionale/risorse/metro.jpg), già scelta nel capitolo 2. Solo in copertina; nessuna misura numerica dedotta dalla foto. | Contesto concreto per le suddivisioni dell'unità |
| TAB-01 | Tabella originale dei 24 prefissi, con multipli e sottomultipli affiancati, nomi, simboli ed esponenti invariati. | Collegare ogni prefisso al fattore esatto |
| TAB-02 | Equivalenze con il metro: km → 10³ m, m → 10⁰ m, cm → 10⁻² m, mm → 10⁻³ m, µm → 10⁻⁶ m. | Leggere il fattore del prefisso |
| SCH-01 | [SVG autonomo](risorse/schema-conversioni.svg) nella sezione delle conversioni. Sequenze km–m–mm e cm–mm–µm, con frecce nei due versi. | Riconoscere fattori diretti e reciproci come potenze di 10 |
| TAB-03A | Massa: 1 mg = 10⁻³ g = 10⁻⁶ kg, con righe dedicate a kg, g e mg. | Applicare i prefissi al grammo |
| TAB-03B | Lunghezza, area e volume: fattori 10⁻², (10⁻²)² = 10⁻⁴, (10⁻²)³ = 10⁻⁶. | Elevare a potenza anche il fattore del prefisso |

Nello schema i fattori sono · 10³ e · 10⁻³ per km–m–mm; · 10¹ e · 10⁻¹ per cm–mm; · 10³ e · 10⁻³ per mm–µm.
Gli esempi sono 2,5 km = 2,5 · 10³ m = 2,5 · 10⁶ mm e 3,2 cm = 3,2 · 10¹ mm = 3,2 · 10⁴ µm. Composizione stabile su ogni dispositivo, con ridimensionamento proporzionale e ingrandimento previsto dal tema.

La vecchia scala illustrata yotta–yocto resta conservata nel sorgente storico. Il nuovo schema numerico è originale e non ne ricostruisce l'immagine. Fonte normativa della tabella verificata: [BIPM, SI prefixes](https://www.bipm.org/en/measurement-units/si-prefixes).

## Conversioni e quesiti

La bozza include la conversione da 7,5 · 10² µm a millimetri mediante il fattore 10⁻³ e il controllo inverso con 10³. I coefficienti restano distinti dai fattori dei prefissi. Per leggere 4,7 · 10⁻⁵ m come 47 µm viene mostrato il passaggio attraverso 47 · 10⁻⁶ m.

Otto quesiti definiti nella [bozza](bozza.md), senza soluzioni: equivalenze, Mm/mm, conversione in micrometri, conversioni dirette e inverse, scelta del fattore, simboli, massa e area. Il quesito originale 6 è conservato nel n. 2; la parte sui prefissi dell'originale 5 prosegue nel n. 3. La parte scientifica/ingegneristica resta nel capitolo 3; il quesito originale 12 sulle cifre significative resta nel capitolo 5.

## Fase successiva

Rivedere e approvare la bozza v2. Prima della realizzazione HTML leggere il modello corrente, presentare la stima ripartita e attendere il via previsto dal master. Nessun merge o deployment autorizzato da questa revisione.
