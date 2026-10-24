# Standard per i visuali scientifici — Fisica

**Versione:** 1.0.0  
**Data:** 20 ottobre 2026  
**Ambito:** fotografie, illustrazioni, schemi, grafici e figure del sito didattico di fisica.

## 1. Scopo, precedenza e autorizzazioni

Evitare visuali scientificamente errati, ambigui, decorativi o con estetica artificiosa (“AI slop”). Questa guida integra, senza sostituire, `AGENTS.md`, `MASTER_PROMPT.md`, il tema e le regole di approvazione. In caso di conflitto prevalgono le regole superiori o più specifiche. **Non cercare, generare, sostituire, approvare autonomamente o pubblicare immagini senza l'autorizzazione richiesta dal workflow del master.** L'approvazione di questa guida non costituisce approvazione delle singole figure.

## 2. Principio fondamentale

Ogni visuale deve insegnare o chiarire un fenomeno identificabile. La correttezza scientifica, la leggibilità e l'accessibilità prevalgono sull'effetto scenografico. Evitare dettagli non motivati e semplificazioni fuorvianti. Preferire una figura semplice e rigorosa a una ricca e ambigua.

## 3. Scegliere lo strumento giusto

- **Fotografie:** per situazioni concrete, strumenti, oggetti, macchine e fenomeni osservabili; preferire foto reali approvate. Generare foto sintetiche soltanto su richiesta/autorizzazione.
- **SVG costruiti mediante codice:** per diagrammi di forze, vettori, traiettorie, sistemi di riferimento, circuiti, sezioni geometriche e relazioni spaziali. Usare coordinate e forme deterministiche, verificabili e modificabili.
- **Grafici da equazioni o dati:** realizzarli con codice e valori controllati (SVG/Canvas/librerie), non generativamente. Assi, unità, scale e andamento devono essere corretti.
- **Illustrazioni concettuali:** per modelli microscopici, sezioni, strutture interne e processi non fotografabili. Possono essere generate solo quando autorizzate e richiedono verifica scientifica.
- **Animazioni e simulazioni:** soltanto se richieste o previste dal workflow; esplicitare il modello fisico e verificarne il comportamento.

**Mai usare un generatore di immagini come fonte definitiva di geometrie, vettori, grafici o formule che richiedono esattezza.**

## 4. Fotografie autentiche: evitare l'estetica AI slop

Quando è autorizzata una fotografia sintetica, richiedere aspetto documentaristico/editoriale sobrio e scena fisicamente plausibile. Specificare:
- illuminazione coerente con sorgenti reali, ombre e riflessi credibili;
- bilanciamento del bianco naturale, saturazione e contrasto moderati;
- prospettiva, profondità di campo e nitidezza otticamente plausibili;
- materiali realistici, dettagli e irregolarità motivate dal contesto;
- composizione utile al fenomeno, non necessariamente centrata o simmetrica;
- disposizione funzionale degli oggetti, senza elementi ornamentali inventati.

Evitare per default: “8K”, “masterpiece”, “ultra detailed”, effetti cinematografici, controluce drammatici, glow, HDR esasperato, color grading arancione-turchese, superfici plasticose, levigatura, microcontrasto eccessivo, sfocature decorative, finti difetti analogici e immagini di repertorio generiche. L'obiettivo non è un'immagine imperfetta a caso, ma una scena realmente fotografabile.

Non presentare una foto generata come prova di un fenomeno realmente fotografato. Quando rilevante, distinguerla come ricostruzione/illustrazione.

## 5. Schemi e illustrazioni: stile scientifico

Usare una grafica da manuale scientifico moderno: essenziale, 2D quando sufficiente, linee precise, spessori uniformi, spaziatura equilibrata, fondo neutro/trasparente. Ricorrere al 3D esclusivamente quando la terza dimensione è necessaria alla comprensione.

Non introdurre gradienti ornamentali, pseudo-3D, bagliori, ombre decorative, particelle, frecce o connessioni fittizie. Non duplicare oggetti decorativi. Ogni dettaglio deve avere una funzione didattica.

- **Forze e vettori:** punto di applicazione, direzione e verso corretti; modulare la lunghezza in modo coerente con quanto rappresentato. Distinguere forza, velocità, accelerazione, moto e trasferimento energetico.
- **Oggetti e dispositivi:** struttura, collegamenti e proporzioni plausibili; se fuori scala, indicarlo quando necessario.
- **Modelli microscopici:** distinguere rappresentazioni convenzionali da fotografie o strutture letterali; evitare metafore che producano idee fisiche sbagliate.
- **Termodinamica:** non confondere calore, temperatura ed energia interna; rappresentare correttamente flussi, sistemi, sorgenti e trasformazioni.
- **Circuiti:** simboli e connessioni elettriche convenzionali, senza collegamenti impossibili.

## 6. Grafici e formule

Generare sempre grafici dalle grandezze, dai dati e/o dalle funzioni indicate. Verificare unità SI, scala, origine, dominio, andamento, intercette, limiti e significato fisico. Se grafico qualitativo, dichiararlo; non far apparire come misurati dati inventati. Le linee guida e i tratteggi devono aiutare la lettura, non introdurre ambiguità. Evitare etichette di punti superflue secondo il master.

Renderizzare le formule con strumenti tipografici affidabili: non affidare a un generatore d'immagini la scrittura di equazioni. Uniformarsi alla notazione del master, incluso **T** per temperatura, **ΔT** per differenza di temperatura, **t** e **Δt** per il tempo, e punto centrato esclusivamente per moltiplicazioni.

## 7. Palette e tema

Preferire una palette limitata e semanticamente coerente. Il gradiente blu del tema Stringhe appartiene all'interfaccia, non va applicato automaticamente ai dati o agli schemi. Nei visuali scientifici privilegiare colori piatti e sufficientemente contrastati, con associazioni stabili fra grandezze e colori nel contesto di ciascuna figura. Non attribuire un significato fisico universale e automatico a un colore. Non comunicare informazioni **solo** tramite colore: aggiungere etichette, tratti, simboli o pattern.

Non invertire indiscriminatamente fotografie e risorse scientifiche in dark mode. Fornire superfici di contrasto adeguate nel tema chiaro e scuro.

## 8. Testi, accessibilità e responsive

Usare poche etichette, brevi e chiare, con notazione corretta. Evitare sovrapposizioni. Predisporre testi alternativi che descrivano il contenuto fisico e didascalie solo quando aggiungono informazioni interpretative necessarie, senza descrivere l'ovvio. Considerare leggibilità su smartphone e in bianco e nero.

Come già stabilito in `AGENTS.md`, **non riorganizzare la struttura interna di schemi, grafici e tabelle in mobile**: conservare assi, disposizione e relazioni; usare ridimensionamento proporzionale e ingrandimento/scorrimento quando i dettagli diventano piccoli.

## 9. Workflow operativo Codex

1. Stabilire quale concetto fisico il visuale deve chiarire, la sua posizione nel capitolo e il motivo per cui serve.
2. Definire tipo di figura, fonte autorizzata, dati disponibili, eventuale semplificazione e contenuti obbligatori.
3. Applicare il workflow esistente per ricerca/scelta/approvazione delle immagini. Non trattare i diagrammi generati automaticamente come eccezione implicita all'approvazione.
4. Se SVG o grafico quantitativo, costruire il sorgente mediante codice e controllare dati e geometrie.
5. Se immagine generativa autorizzata, applicare le regole fotografiche/illustrative pertinenti; non inventare etichette tecniche.
6. Verificare scientificamente frecce, simboli, collegamenti, scale, grandezze, proporzioni e convenzioni; confrontare con il testo.
7. Verificare leggibilità in chiaro/scuro, smartphone, zoom e — quando pertinente — stampa in scala di grigi.
8. Registrare provenienza, licenza e crediti secondo `MASTER_PROMPT.md` e `risorse/crediti.json`, senza presumere diritti d'uso.
9. Presentare gli elementi previsti dal workflow per approvazione. Non fare merge su main né pubblicare senza l'approvazione specifica dell'anteprima richiesta da `AGENTS.md`.

## 10. Criteri di rifiuto

Rifare o scartare il visuale quando presenta: inesattezze fisiche, vettori/assi errati, unità sbagliate, oggetti impossibili, prospettiva incoerente, testo inventato, grafici non ricavati da dati/funzioni, elementi decorativi che sembrano avere significato fisico, contrasto insufficiente o somiglianza con immagine pubblicitaria artificiosa.

**Regola finale:** la qualità visiva non compensa mai un errore scientifico. L'aspetto deve essere il risultato della funzione didattica, non il suo sostituto.

### Soglia operativa per lo zoom — richiesta del 24 ottobre 2026

Valutare la figura alla larghezza effettiva su uno schermo da 320 px. Aggiungere lo zoom soltanto a grafici e schemi con scritte necessarie inferiori a 14 CSS px o dettagli indispensabili non distinguibili a quella dimensione; non basta che la figura sia un diagramma. Se contiene poche etichette, preferire una composizione leggibile senza zoom. Fotografie e copertine restano senza zoom. Per richiesta esplicita, i quattro bersagli del capitolo 7 e lo schema della parallasse del capitolo 6 non hanno zoom. Registrare il controllo nelle verifiche delle figure.


## Principio di economia informativa — 24 ottobre 2026

Ogni elemento testuale o visivo deve aggiungere informazione effettivamente utile. Assumere che il lettore sappia interpretare il contesto, osservare le immagini e ricavare inferenze elementari; non verbalizzare ciò che è già chiaramente visibile o appena spiegato. Non confondere completezza, rigore o accessibilità con ripetizione e puntualizzazione sistematica.

- **Testo:** eliminare frasi introduttive vuote, precisazioni ovvie, ripetizioni e digressioni che non cambiano la comprensione. Approfondire invece passaggi nuovi, difficili o controintuitivi.
- **Immagini, schemi e grafici:** usare solo etichette, frecce, legende, titoli interni e annotazioni necessari a riconoscere grandezze, leggere dati o evitare ambiguità. Non replicare nel visuale le spiegazioni del paragrafo.
- **Didascalie:** non descrivere banalmente ciò che è già riconoscibile. Aggiungere solo identificazioni non ovvie, relazioni significative, dati, condizioni o contesto interpretativo non ricavabili altrimenti. Omettere la didascalia descrittiva quando non serve; mantenere attribuzioni, informazioni obbligatorie e supporti di accessibilità nelle sedi appropriate.
- **Rigore e inclusione:** conservare unità, scale, simboli, ipotesi, condizioni di validità e avvertenze quando la loro omissione potrebbe produrre un errore o fraintendimento rilevante. Testi alternativi accessibili non vanno svuotati solo perché l'immagine è comprensibile a chi la vede.
- **Revisione:** per ogni frase, didascalia, etichetta e annotazione chiedersi: «Se la elimino, il lettore perde un'informazione importante o rischia un fraintendimento?». Se no, eliminarla.

Questo criterio vale anche per bozze, anteprime, materiali scaricabili e future revisioni, senza autorizzare modifiche ai capitoli già pubblicati o deroghe al workflow di approvazione.
