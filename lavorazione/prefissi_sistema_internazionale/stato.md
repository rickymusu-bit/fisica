# Stato — I prefissi del Sistema internazionale

Versione v4 — 23 ottobre 2026 (Europe/Rome).

## Incarico e fase corrente

Richiesta: «Sviluppa il capitolo 4 del piano di lavorazione per l'introduzione alla fisica nel mio repository di fisica».
Il [piano editoriale](../introduzione_fisica_misura/piano.md) identifica il capitolo come **I prefissi del Sistema internazionale**.
Argomento, posizione e tema Stringhe comune sono già definiti. La richiesta avvia lo sviluppo editoriale; non documenta una scelta delle nuove visuali né approvazioni della bozza, dell'HTML o della pubblicazione.

Fase corrente: **bozza v2 completa da approvare**, con tabella riutilizzata e schema SCH-01 realizzato su richiesta esplicita. [Bozza corrente](bozza.md), [schema SVG](risorse/schema-conversioni.svg). Nessuna realizzazione HTML del capitolo o pubblicazione avviata. Le annotazioni iniziali riportate sotto conservano la storia della progettazione e sono superate dagli avanzamenti finali.

Ramo dedicato: `lavorazione/prefissi-sistema-internazionale`, derivato da main al commit `d5688f6af867cd85bcdb8f975ddb538e3f3c1130`.
Alla verifica iniziale dell'albero completo di main e dei rami con nome contenente «prefissi» non risultano una lavorazione o un ramo preesistenti per questo capitolo.

## Fonti e identità del materiale

- Regole: `MASTER_PROMPT.md` **v69.7**, letto integralmente in blocchi; `AGENTS.md`; `riferimenti/STILE_DISPENSE.md` v6; `riferimenti/esempio_irraggiamento.md` v2; `docs/visual-guidelines.md` v1.0.0.
- Sorgente: `sistema_internazionale_notazione_it.html`, sezione `#prefissi`, blob `61a32e96afce2136af8669b1544a02e9d751018d`. Metadato document-version v10 e piè di pagina v12 non allineati: per questa progettazione l'identità è fissata dal blob; non correggere il sorgente storico nell'ambito del nuovo capitolo.
- Letti lo stato del sorgente, il manifest `pubblicazione.json` v12 e la bozza corrente del capitolo 3 per la continuità e la ripartizione dei quesiti.
- Lo stato del capitolo 2 documenta la fotografia `../grandezze_fisiche_sistema_internazionale/risorse/metro.jpg`: Nenad Stojkovic, CC BY 2.0, già scelta dall'utente e verificata in quel lavoro. Per un eventuale riuso associare la scheda esistente del registro unico al nuovo capitolo, senza duplicarla.
- Fonte normativa da consultare nella stesura: [BIPM, SI Brochure](https://www.bipm.org/en/publications/si-brochure), tabella dei prefissi e regole dei simboli. In questa fase non si dichiara eseguita una nuova consultazione esterna.

## Confini e domanda iniziale

Domanda proposta: «La stessa lunghezza può essere scritta come 1 m, 100 cm oppure 1000 mm: perché cambia il numero, mentre la lunghezza rimane la stessa?».
Usare la fotografia del metro come contesto, senza attribuirle una misura numerica non verificata.

Il capitolo spiega il prefisso come fattore decimale esatto, multipli e sottomultipli, simboli e maiuscole, conversioni anche tra due unità prefissate e scelta di una scrittura leggibile.
Conservare i 24 prefissi del sorgente, compresi quetta, ronna, ronto e quecto; dare maggiore spazio nell'esposizione ai prefissi di uso comune.
Spiegare il caso della massa: il kg è unità di base, ma i prefissi si applicano al grammo.
Includere un breve passaggio sul prefisso quando l'unità è elevata a potenza, per evitare di estendere erroneamente il fattore lineare ad aree e volumi.

Richiamare le potenze del capitolo 3 soltanto quanto serve alle equivalenze. Non ripetere il capitolo sul SI e non anticipare conteggio, arrotondamento o regole delle cifre significative del capitolo 5, strumenti, errori o propagazione delle incertezze. Nessuna digressione sui prefissi binari.

## Corrispondenza con il sorgente

| Contenuto originale | Destinazione nel capitolo 4 |
| --- | --- |
| Apertura di #prefissi, km e mm, M e m, prefisso unito al simbolo | Sviluppo narrativo e lettura dei simboli |
| Scala illustrata yotta–yocto | Conservare nel sorgente; riuso nel nuovo capitolo da valutare secondo la proposta |
| Tabella dei 24 prefissi, inclusi quelli del 2022 | Tabella completa conservata, con contenuti e simboli controllati |
| Conversioni 2,5 km e 0,8 µm | Conservare nella spiegazione delle equivalenze |
| Prefissi del grammo e relazione mg–g–kg | Passaggio sulla massa |
| Quesito originale 6, Mm e mm | Conservare integralmente nelle domande del nuovo capitolo |
| Parte sui prefissi del quesito originale 5 | Riprendere soltanto il collegamento 47 · 10⁻⁶ m = 47 µm; la trasformazione scientifica/ingegneristica è già nel capitolo 3 |
| Quesito originale 12, fattore 100 e cifre significative | Resta assegnato al capitolo 5; qui spiegare solo l'esattezza del fattore |

Le altre domande originali restano negli altri capitoli: non ricopiarle per aumentare il numero dei quesiti.

## Visuali e scelte aperte

Proposta dettagliata in [visuali.md](visuali.md):
COP-01, riuso della foto del metro già scelta, soltanto in copertina;
TAB-01, tabella completa dei prefissi;
TAB-02, confronto di scritture equivalenti;
SCH-01, schema numerico dei passaggi di conversione;
TAB-03, confronto dei fattori per lunghezza, area e volume.

La scala illustrata originale si ferma a yotta/yocto, mentre la tabella è aggiornata ai 24 prefissi. La provenienza della scala non è documentata nel sorgente. Proposta: affidare tabella e conversioni a elementi numerici autonomi, conservando l'originale nel sorgente senza modificarlo. Questa scelta editoriale resta da concordare; nessun ridisegno dell'immagine è stato eseguito.

Nessuna nuova fotografia necessaria nell'impostazione consigliata; nessuna immagine cercata, scaricata o generata. Nessuna simulazione proposta: tabelle e schema statico sono sufficienti e non richiedono comandi aggiuntivi.

## Lavoro completato e verifiche

Identificati piano, sorgente e confini; verificati simboli, 24 fattori del prospetto originale e relazioni numeriche previste nella proposta.
Controllata la continuità con il capitolo 3 e la distinzione dal capitolo 5.
Preparati proposta visuale, stato e aggiornamento circoscritto del piano. Verificare il salvataggio remoto dei tre Markdown prima della consegna.

Questa fase modifica solo documenti editoriali: nessun HTML, registro dei crediti, manifest o contenuto pubblicato viene aggiornato. Non sono necessarie build o prove nel browser; non vengono dichiarate verifiche HTML.

Checklist: A1–A5 (livello, monograficità, notazione e quesiti), B1.1–B2 (visuali prima della bozza; approvazione e via prima dell'HTML), B4–B6 (riuso, stato e salvataggio), C1–C4 (immagini, fonti, tabelle e composizione stabile), D1–D2.1 e AGENTS.md (verifiche pertinenti, ramo dedicato, PR in bozza, nessun merge o deployment senza approvazione corrente).

Prossimo passo: revisione e approvazione della bozza v2. Prima dell'HTML leggere il modello Stringhe corrente, presentare la stima ripartita e attendere il via previsto dal master.

## Integrazione richiesta — conversioni tra prefissi

L'utente scrive: «Aggiungi anche come convertire tra prefissi. Riutilizza la tabella dei prefissi. A che schema ti riferisci?».
Registrati il riuso della tabella esistente e l'ampliamento delle conversioni tra due prefissi. Proposta v2: uso dei fattori della tabella, passaggio per l'unità di riferimento e lettura diretta della differenza degli esponenti; conversioni cm–mm e µm–mm in entrambi i versi, oltre a km–mm. Aggiornato il quesito 4 per verificare la conversione tra due prefissi e il controllo inverso.

Chiarito che SCH-01 è una sequenza numerica con frecce e fattori, per esempio km → m → mm, non una nuova tabella. La richiesta di chiarimento non approva né rifiuta lo schema. Registrata l'alternativa di spiegare i medesimi passaggi nel calcolo accanto alla tabella, senza figura separata. Nessuna nuova visuale realizzata e nessuna approvazione estesa automaticamente a copertina, bozza o HTML.

Verificate le equivalenze 3,2 cm = 32 mm, 750 µm = 0,750 mm e 2,5 km = 2 500 000 mm, le rispettive conversioni inverse e il segno della differenza degli esponenti. Master su main ancora v69.7, blob invariato rispetto alla lettura precedente. Aggiornati soltanto i tre Markdown della progettazione, nella stessa PR #65 in bozza.

## Schema richiesto e bozza v1 — 23 ottobre 2026

L'utente autorizza espressamente lo schema con «Ok fai lo schema». Questa indicazione supera lo stato opzionale/non approvato registrato prima: SCH-01 è realizzato in `risorse/schema-conversioni.svg`. Riuso della tabella dei prefissi già richiesto nel messaggio precedente. La foto del metro resta quella già scelta e documentata per il capitolo 2; nessuna ricerca o sostituzione fotografica.

Schema costruito come SVG autonomo con titolo e descrizione accessibili, fondo bianco e colori piatti. Due sequenze: km–m–mm con fattori 1000 e reciproci; cm–mm–µm con fattori 10, 1000 e reciproci. Esempi numerici distinti, frecce nei due versi, nessun fattore affidato al solo colore. Composizione stabile; nell'HTML futuro applicare l'ingrandimento del tema su mobile.

Preparata [bozza v1](bozza.md): apertura sul cambio di unità, tabella originale dei 24 prefissi, simboli, conversioni per passaggio intermedio e differenza degli esponenti, grammo, aree e volumi, otto domande senza soluzioni. Conservate le conversioni del sorgente; schema collocato nella spiegazione. Non è una bozza HTML e non implica approvazione del testo o della pubblicazione.

Controllo scientifico: consultata la pagina ufficiale [BIPM, SI prefixes](https://www.bipm.org/en/measurement-units/si-prefixes) e confrontati i 24 simboli/esponenti. Verificati fattori, risultati e conversioni inverse con aritmetica decimale esatta; controllate potenze di area/volume e otto quesiti. SVG valido come XML, renderizzato in Chromium a 960 e 390 px: nessuna etichetta fuori dal viewBox, nessun overflow nella prova responsive con ridimensionamento proporzionale. Ispezionate entrambe le schermate: a 390 px è necessario l'ingrandimento previsto dal tema; non dichiarare che le scritte ridotte bastino alla lettura. Nessuna prova HTML completa o build del sito dichiarata.

Schema originale numerico, senza risorse esterne o licenze di immagini da dedurre. La bozza conserva le fonti nella sezione di servizio; registro unico e crediti del nuovo capitolo saranno aggiornati nella realizzazione. Salvare e rileggere sul ramo gli stessi file della PR #65, senza merge né deployment.

## Revisione v2 — potenze di 10 in tutto il capitolo

Richiesta esplicita dell'utente: «visto che questo capitolo viene dopo quello sulla notazione esponenziale, devi assolutamente usare le potenze di 10 dovunque».

Applicata al capitolo la notazione con potenze di 10 in tutte le conversioni, nei fattori diretti e inversi, nelle equivalenze numeriche, nelle tabelle (anche massa e unità elevate a potenza), nei quesiti pertinenti e nello schema, compresa la descrizione accessibile. Questa scelta specifica supera per il capitolo 4 la preferenza generale di A4 per i numeri decimali moderati; non modifica il master o gli altri capitoli. La tabella originale dei 24 prefissi resta invariata.

Esplicitati somma degli esponenti nelle conversioni successive, differenza degli esponenti nel rapporto dei prefissi e prodotto degli esponenti per area/volume. Schema aggiornato sullo stesso percorso, con fattori 10³ e 10⁻³, 10¹ e 10⁻¹; esempi 2,5 km = 2,5 · 10³ m = 2,5 · 10⁶ mm e 3,2 cm = 3,2 · 10¹ mm = 3,2 · 10⁴ µm. Bozza v2 sullo stesso percorso, otto quesiti conservati e adattati nella notazione.

Verificati con aritmetica decimale fattori, risultati e inverse, esponenti di area/volume e assenza dei vecchi fattori decimali nel contenuto didattico. Schema XML valido, renderizzato e ispezionato a 960 e 390 px senza tagli o overflow; ingrandimento da mantenere nell'HTML futuro per la lettura mobile. Modello, foto, geometria dello schema e argomenti non interessati conservati. Non necessaria una build del sito per Markdown e SVG; nessuna verifica HTML completa dichiarata. Revisione da rileggere sul ramo prima della consegna; PR #65 in bozza, nessun merge o deployment.
