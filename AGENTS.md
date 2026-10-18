# Istruzioni per il progetto

Prima di lavorare leggi integralmente `MASTER_PROMPT.md` e lo stato del capitolo in `lavorazione/<capitolo>/stato.md`. Se lo stato manca, crealo quando il capitolo è identificato, secondo B6; non dedurre approvazioni.

Lavora in un ramo dedicato derivato da `main`. Aggiorna lo stato ai passaggi decisivi e prima di interrompere. GitHub è la fonte ufficiale e Git conserva la cronologia.

Usa nomi stabili senza versione né data e applica le regole del master per i collegamenti già pubblicati. Confronta identità e versione prima di importare o sostituire; segnala i conflitti incerti senza sovrascrivere. Rispetta il workflow di approvazione del master. Durante la migrazione non eliminare materiali su Drive e non attivare o modificare la pubblicazione del sito.

Per struttura e monograficità di tutti i capitoli applica A3 del master; per domande finali, didascalie e precisione proporzionata applica A5, C3 e A1. La revisione degli HTML esistenti deve registrare la suddivisione e verificarne i collegamenti, senza considerare automaticamente completato l'adeguamento.

Prima di scrivere o rivedere il testo delle dispense leggi anche `riferimenti/STILE_DISPENSE.md` e `riferimenti/esempio_irraggiamento.md`, richiamati in A2. Il riferimento comprende la spiegazione discorsiva e l'interpretazione delle formule secondo A4.

Per impaginare o rivedere gli HTML applica automaticamente l’esatto tema grafico comune salvato nel modello autonomo `riferimenti/TEMA_DISPENSE.html`, già approvato, secondo A6 del master; non chiedere di scegliere nuovamente il template. Nei calcoli applica notazione esponenziale e prefissi SI secondo A4; interpreta i risultati degli esercizi con i confronti concreti previsti da A5.

Usa le note a piè di pagina soprattutto per alleggerire il testo: seleziona precisazioni brevi e utili, elimina ripetizioni di testo/didascalie, puntualizzazioni superflue e approfondimenti troppo tecnici, secondo A1. Mantieni le note collassabili, inizialmente chiuse, con richiami e ritorni cliccabili e versione/data separate nel piè di pagina, secondo A6.

Il nome «← Tutti gli articoli» dei collegamenti alla home e il componente delle note collassabili sono parti integranti del tema comune secondo A6: applicali automaticamente insieme al modello autonomo in ogni capitolo futuro e nelle revisioni che lo adottano.

Per le etichette usa il vocabolario unico di A6. Prima di aggiornare o pubblicare leggi `pubblicazione.json`: modifica soltanto gli articoli conformati ammessi; conserva invariati ed escludi da ogni aggiornamento gli articoli sospesi, salvo richiesta esplicita dell’utente, secondo D2.1.

Non pubblicare né ripristinare vecchi indirizzi o reindirizzamenti degli articoli esclusi e della precedente dispensa unificata: l’utente ne ha richiesto esplicitamente la rimozione. Il manifest di pubblicazione conserva l’elenco degli indirizzi dismessi.

Per la home usa il titolo esatto **Materia Oscura** e il sottotitolo **Guida pratica per fare luce sulla Fisica**, anche nei metadati pertinenti: questa nuova richiesta esplicita dell’utente sostituisce il precedente nome del sito riportato in A6. La gerarchia editoriale resta **Area tematica → Articolo → Sezione**, ma nella home mostra soltanto il nome del gruppo (per esempio «Materia e calore»), senza l’etichetta «Area tematica». Applica `riferimenti/TERMINOLOGIA_SITO.md` v2 insieme alle altre etichette di A6, senza aggiornare i sorgenti esclusi.

Traduci le etichette delle infografiche e degli schemi quando richiesto; questa regola non si estende alle scritte presenti nelle fotografie, comprese le termografie. La foto delle anatre mantiene la scala originale: l’utente ha escluso la conversione.

Il logo di Materia Oscura è la stringa chiusa nera su fondo trasparente salvata in `identita/logo-materia-oscura.svg`; specifiche e copie per il riuso in `identita/README.md`. Nella home sta accanto al titolo. Conserva una sola curva visibile e il ciclo cerchio → quattro lobi orizzontali/verticali → cerchio → quattro lobi diagonali → cerchio; non sovrapporre le configurazioni dell’immagine di riferimento.

Ultima correzione del logo: l’utente richiede una **sinusoide stazionaria con quattro creste su una curva chiusa**, con nodi angolari fissi e ventri oscillanti, senza propagazione o rotazione. I file correnti autonomi sono `identita/logo-materia-oscura-onda-stazionaria.svg` e `.gif`, descritti in `identita/README.md` v4. La precedente richiesta progressiva è superata; non riprendere la proposta a otto lobi. La home mantiene il file precedente finché non viene richiesta la sostituzione.
