# Proposta di suddivisione

18 ottobre 2026. **Impostazione aggiornata su richiesta dell’utente: due capitoli. Testi rivisti ancora da approvare.** Master v59, tema v7. Fonte: HTML unificato v7, blob `14e072ca077fc7887c86749df9c3ec1213735aa7`, main `8c071729b2bf577886e0227c383a0318c0eb5905`. Nessun HTML nuovo prodotto.

| Capitolo e futuro percorso | Provenienza | Contenuti e risorse conservati | Domande |
| --- | --- | --- | --- |
| Conduzione · `conduzione_it.html` | `#potenza` + `#conduzione`, primi due gruppi di domande | Breve sezione sulla potenza termica; zuppa e cucchiaio; schema statico degli elettroni mobili da scegliere; tabella λ con tutti gli otto materiali; video con miniatura e URL esatti; Fourier; muro e grafico corretto; caffettiera, vetrocamera, igloo, lingua sul palo gelato ed elettroni mobili. | 12 |
| Convezione · `convezione_it.html` | `#convezione`, terzo gruppo di domande | Stanza, densità e gravità; meccanismo naturale e forzato; uccelli veleggiatori nelle termiche e celle convettive solari; ventola del processore; radiatore, pompa, termostato, alette e ramo dell’abitacolo. | 7 |

## Scelta strutturale ricevuta

Il 18 ottobre 2026 alle 13:12 l’utente ha indicato di integrare la potenza termica come piccola sezione di Conduzione. La richiesta sostituisce la precedente pianificazione in tre capitoli, senza modificare il master e senza estendere questa scelta ad altri argomenti. La sezione introduce il significato di potenza e le due relazioni equivalenti prima di Fourier. Su successiva richiesta del 18 ottobre alle 13:17, l’esempio svolto delle due stufette è rimosso insieme ai suoi schemi e richiami visuali. I sei quesiti sulla potenza restano nei 12 finali di Conduzione. Non è previsto `potenza_termica_it.html` né una sua copertina. La scelta strutturale non approva automaticamente il nuovo testo o la realizzazione HTML.

## Bozze complete da esaminare

- [Conduzione](../conduzione/bozza.md): apertura sul manico che si scalda e meccanismo microscopico; conducibilità; sezioni «Conduttori termici» e «Isolanti termici» con applicazioni integrate; breve potenza termica e legge di Fourier; 12 domande finali, senza esempio svolto sulle stufette.
- [Convezione](../convezione/bozza.md): apertura sull’aria sopra il termosifone; teoria naturale e forzata; aquila nelle termiche e applicazioni tecniche; domande finali. Nessuna legge di Newton aggiunta automaticamente, perché assente dalla fonte approvata.

Su richiesta del 18 ottobre alle 13:18, il dissipatore è rimosso da Conduzione, insieme alla sua figura e al quesito dedicato. Resta trattato in Convezione, dove è già presente anche il quesito sul radiatore e sul processore. Le applicazioni sono integrate nelle sezioni su conduttori e isolanti per richiesta esplicita dell’utente del 18 ottobre alle 13:25; questa scelta specifica sostituisce la precedente sezione separata «Applicazioni» in Conduzione, senza modificare il master o altri capitoli. Nessun nuovo capitolo di meteorologia o geologia, nessun riepilogo automatico, nessuna soluzione alle domande.

## Correzioni e adeguamenti proposti

- Nell’esercizio della parete, precisare che 20 °C e 0 °C sono le temperature delle **facce**, non automaticamente dell’aria: la legge di Fourier da sola non comprende gli scambi alle superfici. Numeri invariati.
- Specificare che P = Q/Δt indica la potenza media sull’intervallo. Distinguere potenza termica e potenza elettrica nominale con una nota breve.
- Interpretare discorsivamente λ, area, spessore e differenza di temperatura; conservare il profilo lineare soltanto nello spessore e il ΔT = 30 K del grafico approvato.
- Dare una base alla domanda esistente sul ventilatore: convezione ed evaporazione sono meccanismi diversi; l’aria mossa non è automaticamente più fredda. Nessun nuovo esercizio sul corpo umano.
- Conservare le 18 richieste attuali, dopo la rimozione del quesito sul dissipatore da Conduzione e la sostituzione dei due quesiti atmosferico/oceanico con quello sull’aquila; eventuali riformulazioni in vero/falso motivati o scelta multipla richiedono approvazione della formulazione. Le bozze attuali mantengono il set storico, prevalentemente aperto.

## Applicazioni presenti dopo la rimozione del dissipatore

In Conduzione restano cinque casi applicativi, organizzati per funzione dei materiali:

- **Conduttori termici:** elettroni mobili e confronto sperimentale dei metalli; lingua sul palo gelato; corpo metallico della caffettiera. La caffettiera collega anche la funzione isolante del manico, con una sola figura.
- **Isolanti termici:** definizione come materiali a bassa conducibilità, che rallentano il trasferimento senza annullarlo; ruolo dell’aria intrappolata; isolamento delle pareti, vetrocamera e igloo.

La distinzione usa la conducibilità, senza fissare una soglia universale né presentare l’isolante come una sorgente di calore. La tabella dei materiali resta il confronto quantitativo comune. La breve sezione sulla potenza termica e la legge di Fourier seguono le due sezioni, per quantificare ciò che è stato osservato. Il cucchiaio resta la situazione iniziale della teoria. Il contributo degli elettroni mobili è spiegato nella sezione sui conduttori e non ripetuto nell’applicazione del palo.

In Convezione restano tre applicazioni nella sezione dedicata: aquila nelle termiche, raffreddamento del processore e radiatore dell’automobile. Il termosifone resta il caso iniziale della teoria. Gli esempi di convezione naturale sono dunque termosifone e aquila; circolazione atmosferica globale e correnti marine sono ritirate dalla bozza su scelta esplicita del 18 ottobre alle 16:42.

## Visuali, interazioni e copertine

[suddivisione.json](suddivisione.json) identifica le **15 immagini HTML**, compresa la miniatura video, con hash dei riferimenti incorporati, destinazione e hash dello script fisico. Le prime due immagini, relative alle stufette, sono conservate nella fonte ma escluse dal capitolo rivisto su richiesta del 18 ottobre alle 13:17. Originali e traduzioni restano in `risorse/` della fonte. Non si ripetono traduzioni o elaborazioni già approvate. Le licenze storiche non pienamente documentate restano da chiarire prima di una futura pubblicazione: non sono dichiarate verificate.

Servono due copertine distinte dalle figure interne. Nessuna ricerca o generazione è stata avviata. Proposte di soggetto da fornire/scegliere secondo C2:

- **C-C:** oggetto metallico riscaldato a un’estremità, diverso dal cucchiaio e dalle altre figure interne.
- **V-C:** moto di un fluido riscaldato, diverso dagli schemi e dalle fotografie interne.

L’utente può fornire immagini equivalenti pertinenti; un ritaglio di una figura interna non vale come copertina distinta.

**Nessuna simulazione dell’agitazione termica è più prevista**, su richiesta del 18 ottobre alle 13:31. Il modello e lo script originali restano conservati nella fonte e in Git; l’hash nell’inventario identifica la provenienza, non un’interazione da integrare. Le vibrazioni atomiche restano spiegate brevemente: la distinzione fra conduttori e isolanti non elimina questo contributo fisico.

È previsto lo **schema statico E-1** nella sezione sui conduttori: reticolo atomico, elettroni mobili, lato caldo/freddo e freccia del trasferimento netto di energia. Non suggerire che tutti gli elettroni scorrano ordinatamente verso il freddo. La struttura rimane uguale su ogni dispositivo. Schema da scegliere/fornire secondo C2 prima della realizzazione; nessuna ricerca, generazione o ricostruzione autonoma avviata. Non vale la precedente stima di integrazione della simulazione: la stima totale verrà presentata dopo l’approvazione della bozza e la scelta dello schema.

## Stato della revisione stilistica

Il 18 ottobre 2026 alle 13:36 l’utente ha richiesto i testi completi riscritti secondo i riferimenti stilistici. Riletti STILE_DISPENSE.md v6 ed esempio_irraggiamento.md v2; riscritta integralmente la prosa didattica di entrambi i capitoli. Le domande conservano le richieste già pianificate (12 e 7), con sole correzioni di punteggiatura. Verificati apertura concreta, nessi causali, sviluppo dei termini, interpretazione delle formule, note essenziali, figure e didascalie. I testi sono proposte da esaminare, non bozze già approvate. Nessun HTML realizzato.

Video: miniatura e URL esatti della fonte, nessun player incorporato. Grafico del muro: stessi dati, assi e relazioni. Tutti i visuali conservano la composizione su mobile; usare l’ingrandimento con scorrimento del tema v7.

## Workflow successivo

1. Esaminare suddivisione e due bozze, raccogliere correzioni e copertine.
2. Dopo l’approvazione della bozza, presentare stima totale ripartita fra materiali, interazioni, impaginazione, verifiche e salvataggio; ottenere il via esplicito prima degli HTML, secondo B1.1–B2.
3. Realizzare un capitolo alla volta sul ramo dedicato con l’esatto tema autonomo v7: «Materia e calore», «← Articoli», logo definitivo con pausa, indice laterale, note collassabili e ritorni. Assegnare versioni e date interne al consolidamento.
4. Verificare correttezza, peso, autonomia, risorse, link e comandi, con confronto diretto al tema su desktop e smartphone. Registrare gli esiti nei file di stato.
5. Presentare gli HTML e le anteprime. Main, manifest e pubblicazione richiedono approvazione separata. Nessun ripristino dell’indirizzo storico unificato o dei vecchi reindirizzamenti.

## Sostituzione concordata — 18 ottobre 2026, ore 15:38

Le correnti marine sostituiscono integralmente il mantello nella bozza di Convezione, nel quesito 3 e nella nota 3. Distinti temperatura/salinità/densità e ruolo dei venti, con fonti NOAA in nota. Serve la nuova immagine M-1 della circolazione oceanica, da scegliere/fornire; lo schema storico del mantello resta conservato ma escluso dalla nuova bozza. Nessuna sostituzione delle altre applicazioni.

## Scelta corrente degli esempi naturali — 18 ottobre 2026, ore 16:42

L’utente sceglie termosifone e aquila. Il termosifone rimane apertura della teoria; l’aquila nelle termiche sostituisce le due applicazioni sulla circolazione atmosferica globale e sulle correnti marine. Anche i due quesiti relativi sono sostituiti da un solo quesito sull’aquila: 6 domande in Convezione, 12 in Conduzione. La domanda naturale/forzata richiama ora termosifone e aquila. Nuova immagine richiesta N-1: aquila con ali distese in una termica, terreno visibile e spazio per frecce esplicative. Il precedente segnaposto M-1 è ritirato; immagini atmosferiche e del mantello conservate tra le risorse storiche, escluse dal nuovo capitolo. Gli aggiornamenti storici precedenti non descrivono più la selezione corrente.

## Aggiornamento corrente — 18 ottobre 2026, ore 17:24

Copertine scelte dall’utente: takoyaki per Conduzione, Convection-cells.jpg per Convezione. Per gli uccelli fornite due fotografie alternative, da scegliere; testo esteso a molte specie veleggiatrici. Aggiunta su richiesta l’applicazione sulle celle convettive del Sole, con fonti NASA, nuovo quesito e immagine S-1 da fornire distinta dalla copertina: 7 quesiti di Convezione, 12 di Conduzione. Gli esempi naturali correnti sono termosifone, uccelli nelle termiche e Sole. Le precedenti descrizioni a due soli esempi sono superate da questa richiesta. Materiali e licenze nei piani visuali e in suddivisione.json; binari originali ispezionati localmente, non dichiarati caricati nel repository. Rimangono E-1, S-1 e scelta N-1 A/B. Nessun HTML, main o pubblicazione modificati.
