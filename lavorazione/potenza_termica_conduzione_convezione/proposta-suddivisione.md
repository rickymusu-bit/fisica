# Proposta di suddivisione

18 ottobre 2026. **Impostazione aggiornata su richiesta dell’utente: due capitoli. Testi rivisti ancora da approvare.** Master v59, tema v7. Fonte: HTML unificato v7, blob `14e072ca077fc7887c86749df9c3ec1213735aa7`, main `8c071729b2bf577886e0227c383a0318c0eb5905`. Nessun HTML nuovo prodotto.

| Capitolo e futuro percorso | Provenienza | Contenuti e risorse conservati | Domande |
| --- | --- | --- | --- |
| Conduzione · `conduzione_it.html` | `#potenza` + `#conduzione`, primi due gruppi di domande | Breve sezione sulla potenza termica; zuppa e cucchiaio; reticolo animato; tabella λ con tutti gli otto materiali; video con miniatura e URL esatti; Fourier; muro e grafico corretto; caffettiera, vetrocamera, igloo, lingua sul palo gelato ed elettroni mobili. | 12 |
| Convezione · `convezione_it.html` | `#convezione`, terzo gruppo di domande | Stanza, densità e gravità; meccanismo naturale e forzato; atmosfera e rotazione; mantello prevalentemente solido; ventola del processore; radiatore, pompa, termostato, alette e ramo dell’abitacolo. | 7 |

## Scelta strutturale ricevuta

Il 18 ottobre 2026 alle 13:12 l’utente ha indicato di integrare la potenza termica come piccola sezione di Conduzione. La richiesta sostituisce la precedente pianificazione in tre capitoli, senza modificare il master e senza estendere questa scelta ad altri argomenti. La sezione introduce il significato di potenza e le due relazioni equivalenti prima di Fourier. Su successiva richiesta del 18 ottobre alle 13:17, l’esempio svolto delle due stufette è rimosso insieme ai suoi schemi e richiami visuali. I sei quesiti sulla potenza restano nei 12 finali di Conduzione. Non è previsto `potenza_termica_it.html` né una sua copertina. La scelta strutturale non approva automaticamente il nuovo testo o la realizzazione HTML.

## Bozze complete da esaminare

- [Conduzione](../conduzione/bozza.md): apertura sul manico che si scalda; meccanismo microscopico; breve sezione su energia, potenza e durata prima di Fourier; applicazioni; 12 domande finali, senza esempio svolto sulle stufette.
- [Convezione](../convezione/bozza.md): apertura sull’aria sopra il termosifone; teoria naturale e forzata; applicazioni atmosferiche, geologiche e tecniche; domande finali. Nessuna legge di Newton aggiunta automaticamente, perché assente dalla fonte approvata.

Su richiesta del 18 ottobre alle 13:18, il dissipatore è rimosso da Conduzione, insieme alla sua figura e al quesito dedicato. Resta trattato in Convezione, dove è già presente anche il quesito sul radiatore e sul processore. Le applicazioni opzionali sono proposte per conservare quanto già presente. Nessun nuovo capitolo di meteorologia o geologia, nessun riepilogo automatico, nessuna soluzione alle domande.

## Correzioni e adeguamenti proposti

- Nell’esercizio della parete, precisare che 20 °C e 0 °C sono le temperature delle **facce**, non automaticamente dell’aria: la legge di Fourier da sola non comprende gli scambi alle superfici. Numeri invariati.
- Specificare che P = Q/Δt indica la potenza media sull’intervallo. Distinguere potenza termica e potenza elettrica nominale con una nota breve.
- Interpretare discorsivamente λ, area, spessore e differenza di temperatura; conservare il profilo lineare soltanto nello spessore e il ΔT = 30 K del grafico approvato.
- Dare una base alla domanda esistente sul ventilatore: convezione ed evaporazione sono meccanismi diversi; l’aria mossa non è automaticamente più fredda. Nessun nuovo esercizio sul corpo umano.
- Conservare le 19 richieste rimaste dopo la rimozione del quesito sul dissipatore da Conduzione; eventuali riformulazioni in vero/falso motivati o scelta multipla richiedono approvazione della formulazione. Le bozze attuali mantengono il set storico, prevalentemente aperto.

## Applicazioni presenti dopo la rimozione del dissipatore

In Conduzione restano cinque casi applicativi: caffettiera, isolamento delle pareti (paragrafo che richiama lo schema del muro), vetrocamera, igloo, lingua sul palo gelato e ruolo degli elettroni mobili nella conduzione dei metalli. Quattro hanno un titolo dedicato; il caso delle pareti è sviluppato nel paragrafo seguente la caffettiera. Il cucchiaio nella zuppa resta la situazione iniziale della teoria, non un’ulteriore applicazione in questa sezione.

In Convezione restano quattro applicazioni nella sezione dedicata: atmosfera, mantello, raffreddamento del processore, radiatore dell’automobile. Il termosifone è il caso iniziale della teoria; contando anche quello, i casi concreti sono cinque. «Conduzione e convezione lavorano insieme» collega processore e radiatore, senza introdurre una sesta applicazione.

## Visuali, interazioni e copertine

[suddivisione.json](suddivisione.json) identifica le **15 immagini HTML**, compresa la miniatura video, con hash dei riferimenti incorporati, destinazione e hash dello script fisico. Le prime due immagini, relative alle stufette, sono conservate nella fonte ma escluse dal capitolo rivisto su richiesta del 18 ottobre alle 13:17. Originali e traduzioni restano in `risorse/` della fonte. Non si ripetono traduzioni o elaborazioni già approvate. Le licenze storiche non pienamente documentate restano da chiarire prima di una futura pubblicazione: non sono dichiarate verificate.

Servono due copertine distinte dalle figure interne. Nessuna ricerca o generazione è stata avviata. Proposte di soggetto da fornire/scegliere secondo C2:

- **C-C:** oggetto metallico riscaldato a un’estremità, diverso dal cucchiaio e dalle altre figure interne.
- **V-C:** moto di un fluido riscaldato, diverso dagli schemi e dalle fotografie interne.

L’utente può fornire immagini equivalenti pertinenti; un ritaglio di una figura interna non vale come copertina distinta.

La sola simulazione resta in Conduzione: 14 colonne e 5 righe di particelle oscillanti intorno a posizioni fisse, con ampiezza maggiore verso il lato caldo. È un modello qualitativo, non una soluzione numerica della diffusione termica. Conservare modello e script fisico; integrare pausa/ripresa e movimento ridotto senza cambiare il modello. Fattibilità alta; carico previsto basso, da verificare nel browser. Stima preliminare per estrazione, integrazione e verifica di questa sola interazione: 10–20 minuti, inclusi nella futura stima totale. Nessuna simulazione programmata in questa fase.

Video: miniatura e URL esatti della fonte, nessun player incorporato. Grafico del muro: stessi dati, assi e relazioni. Tutti i visuali conservano la composizione su mobile; usare l’ingrandimento con scorrimento del tema v7.

## Workflow successivo

1. Esaminare suddivisione e due bozze, raccogliere correzioni e copertine.
2. Dopo l’approvazione della bozza, presentare stima totale ripartita fra materiali, interazioni, impaginazione, verifiche e salvataggio; ottenere il via esplicito prima degli HTML, secondo B1.1–B2.
3. Realizzare un capitolo alla volta sul ramo dedicato con l’esatto tema autonomo v7: «Materia e calore», «← Articoli», logo definitivo con pausa, indice laterale, note collassabili e ritorni. Assegnare versioni e date interne al consolidamento.
4. Verificare correttezza, peso, autonomia, risorse, link e comandi, con confronto diretto al tema su desktop e smartphone. Registrare gli esiti nei file di stato.
5. Presentare gli HTML e le anteprime. Main, manifest e pubblicazione richiedono approvazione separata. Nessun ripristino dell’indirizzo storico unificato o dei vecchi reindirizzamenti.
