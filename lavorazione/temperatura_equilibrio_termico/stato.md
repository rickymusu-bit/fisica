# Stato — Temperatura ed equilibrio termico

Versione v7 · Aggiornamento: 19 ottobre 2026 (Europe/Rome).

## Ambito e riferimenti

Articolo 2 del [percorso approvato](../percorso_termodinamica.md): temperatura, equilibrio termico, principio zero, termometro e scale Celsius, Kelvin e Fahrenheit. Esclusi calorimetria, bilancio termico e sviluppo della dilatazione.

Ramo: `termodinamica/temperatura-equilibrio-termico`, derivato da main al commit `d6002b19007967e7ac4c0726b5c14e1a025494ef`. Nessuna modifica a main, manifest, home o articoli pubblicati/sospesi.

Letti integralmente MASTER_PROMPT.md v60 in blocchi senza troncamenti, AGENTS.md, STILE_DISPENSE.md v6, esempio_irraggiamento.md v2, piano e stato dell’articolo 1. Tema comune v8 già approvato; leggere integralmente `riferimenti/TEMA_DISPENSE.html` prima di impaginare.

## Approvazioni effettive

1. Richiesta iniziale: «Sul repo https://github.com/rickymusu-bit/fisica crea l’articolo 2 del piano».
2. Primo «Ok»: accettata la proposta delle visuali e del percorso iniziale.
3. Secondo «Ok»: approvata la bozza completa v1 in `bozza.md`.
4. Dopo la stima, l’utente ha fornito tre immagini precise e chiesto di adattare l’esempio della foto 1. Copertina storica scelta al posto del termometro meteorologico; medico che misura la temperatura al posto della sonda immersa; bevanda fredda con ghiaccio al posto del caffè. Autorizzati scelta di queste immagini e relativi adattamenti circoscritti, senza richiedere una nuova conferma.
5. L’utente ha poi sostituito espressamente la sola copertina con «Galileo Thermometer in Tokyo.jpg». Foto scaricata e ispezionata, nuova didascalia salvata; il resto del testo è invariato rispetto alla v2.
6. Ricevuto il via esplicito alla realizzazione HTML: «Procedi», dopo la stima e la scelta definitiva della copertina. Avviata la realizzazione autorizzata; main e pubblicazione restano distinti e non autorizzati.

## Fase corrente e risultato

Bozza v3 corrente: [bozza.md](bozza.md). Mantiene il testo approvato non coinvolto; adatta apertura, misura per contatto sulla paziente, didascalie, equilibrio con la bevanda fredda e domande 1 e 4. Nove domande finali senza soluzioni, tabella delle scale e due note.

Domanda guida conservata: «Quando possiamo fidarci della temperatura indicata da un termometro?». HTML autonomo v1 completato dopo il via esplicito; nessuna simulazione aggiunta. Le modifiche testuali e la scelta delle immagini sono espressamente richieste, non una nuova stesura da far approvare da capo.

Tre immagini correnti scaricate, ispezionate e salvate in `risorse/`; soggetti, URL ricevuti, fonti, autori, stato dei diritti, dimensioni e hash in [visuali.md](visuali.md) v4. Nessuna modifica delle immagini. Nessun materiale mancante.

- COP-01 corrente: termometro galileiano, Syced, CC0 1.0; 1920 × 2550 px, 536 878 byte. File completo scelto dall’utente, senza ritaglio o alterazione. Precedente incisione conservata come originale di lavorazione, non più usata.
- FIG-01: misura orale della temperatura, Roy Perry / National Library of Medicine; versione scelta 960 × 714 px, 138 572 byte. «No known copyright restrictions», distinto da CC0.
- FIG-02: bevanda con ghiaccio, Henryemix; versione scelta 1920 × 1280 px, 407 515 byte; CC0 1.0.
- TAB-01: confronto delle scale, già presente nella bozza approvata. Nessuna nuova simulazione o video.

Registro unico aggiornato mediante `data-credit-*` e `scripts/credits.py --sync`; tre schede associate senza risorse non documentate per questo articolo. Conservata l’esatta dichiarazione Flickr Commons per la foto clinica. Crediti e licenza OFL Lexend incorporati; nessun inventario concorrente.

## Controlli della revisione

- Foto controllate visivamente, soggetti coerenti; nessuna temperatura, diagnosi, misura o cronologia dedotta dalle fotografie.
- Per il termometro: equilibrio della parte sensibile con la zona del corpo misurata, senza presupporre temperatura uniforme in tutto il corpo.
- Per la bevanda: esplicitati ghiaccio visibile, fase successiva alla fusione, ambiente più caldo e a temperatura costante, al riparo dal Sole; nessuna anticipazione quantitativa del calore latente.
- Copertina corrente verificata visivamente: termometro galileiano con ampolle colorate. Nessuna misura numerica dedotta dalla foto; didascalia pertinente. Rimossa dalla bozza ogni descrizione della vecchia incisione.
- Foto complete, proporzioni e byte conservati; hash blob confrontati con quelli calcolati localmente prima del salvataggio.
- Testo approvato fuori dall’intervento conservato; formule e tabella non modificate. Segnaposto collegati a file reali.
- Le verifiche precedenti riguardavano la bozza; per la realizzazione HTML valgono i controlli documentati sotto.

## Stima e prossimo passo

Stima già comunicata: 30–50 minuti di lavoro complessivo per la realizzazione, esclusa l’attesa di file/risposte; materiali e crediti 5–10 minuti, impaginazione nel tema 15–25 minuti, controlli/anteprime/salvataggio 10–15 minuti. Calcolo basso, nessuna simulazione. Le immagini sono ora disponibili e la verifica preliminare è compiuta. Stima indicativa subordinata all’accesso operativo e all’esito delle verifiche.

Prossimo passo: presentare HTML e anteprime per la revisione del risultato. Via all’HTML già ricevuto e lavoro completato: non richiederlo nuovamente. Integrazione in main e pubblicazione restano distinte e non autorizzate.

L’accesso di rete dalla shell funziona usando i permessi di rete aggiuntivi dell’esecutore; con la sola sandbox predefinita il proxy non risulta raggiungibile. Non disattivare proxy o verifica TLS. Salvataggio ufficiale tramite connettore GitHub.


## Realizzazione completata — HTML v1

File finale: `temperatura_equilibrio_termico_it.html`, v1 · 19 ottobre 2026, 1 880 322 byte (1,88 MB decimali). Copia identica in `bozza.html`. Generatore riproducibile: `realizza.py`; dopo la generazione eseguire credits.py --sync e aggiornare la copia di lavorazione.

Tema autonomo v8 letto e riutilizzato. CSS comuni confrontati byte per byte con il modello, script comuni preservati integralmente; sole aggiunte specifiche per tabella scorrevole e frazioni inline. Tre fotografie incorporate confrontate byte per byte con i file scelti. Composizione completa conservata, copertina verticale senza ritaglio, nessun ingrandimento superfluo per le foto. Tre conversioni con frazioni orizzontali, tabella a quattro colonne invariata fra dispositivi, nove domande e due note collassabili con richiami univoci e ritorni.

Navigazione dalla nuova pagina verso il precedente già pubblicato (sistemi termodinamici) e il successivo attualmente disponibile (Stati della materia), con URL pubblici assoluti utilizzabili dalle copie scaricate. Nessun collegamento a un articolo ancora inesistente. Navigazione inversa, catalogo e manifest non aggiornati: spettano alla futura pubblicazione autorizzata.

Controlli superati: credits.py --check, build Pages (otto HTML già ammessi, nuovo articolo non pubblicato), git diff --check. Nessun sorgente sospeso, articolo esistente, tema o home modificato. La sola pagina dei crediti e il registro centrale cambiano per includere il nuovo articolo.

Verifiche Chromium a 1280 e 390 px: nessun errore JavaScript o richiesta di rete, nessun overflow della pagina, immagini/font caricati, indice con apertura/chiusura/Esc e selezione, note e ritorni, crediti offline con OFL, pausa/ripresa e movimento ridotto del logo. Indice e crediti verificati anche senza JavaScript. Tabella mobile larga 650 px dentro un contenitore di 296 px, scorrimento interno verificato; tre formule controllate senza overflow e ispezionate visivamente. IDs univoci e ancore risolte.

L’ambiente Chromium blocca l’apertura diretta di URL file: tramite policy; per le prove il medesimo HTML completo è stato caricato in memoria con rete disabilitata. Il ramo specifico dello script che riscrive il collegamento pubblico dei crediti con protocollo file: è quello canonico, preservato senza modifiche; non viene dichiarato verificato in questo ambiente. Report in `verifiche-browser.json`, controlli statici in `verifiche-finali.json`; anteprime desktop/mobile salvate nella lavorazione e ispezionate, incluse copertina, foto clinica, tabella e formule.

Il salvataggio nel ramo dedicato non equivale alla pubblicazione. Caricamento remoto verificato: commit di realizzazione `b526643501fa67724fe60c32f6831cfe8573caf4`, identico al riferimento del ramo su GitHub. PR in bozza aperta: https://github.com/rickymusu-bit/fisica/pull/37 . Nessuna integrazione o pubblicazione eseguita; prossimo passaggio: revisione dell’HTML e delle anteprime da parte dell’utente.
