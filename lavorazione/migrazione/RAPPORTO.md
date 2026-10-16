# Migrazione di Materiale Didattico

Aggiornamento: 2026-10-16 16:42 (Europe/Rome). Repository: `rickymusu-bit/fisica`. Ramo ufficiale: [main](https://github.com/rickymusu-bit/fisica/tree/main).

La [pull request #1 verso main](https://github.com/rickymusu-bit/fisica/pull/1) raccoglie la migrazione e la successiva semplificazione dei rami, autorizzata dall’utente. `main` e `codex` erano identici al commit `7d60be70c0d2c5af95b31a804973299c7c98650f`; non c’erano modifiche da riconciliare. I materiali ufficiali sono reperibili in `main`; il master v45 indica `main` come riferimento per i futuri rami temporanei.

La migrazione è stata sviluppata originariamente in `migrazione/materiale-didattico-drive`, derivato da `codex`. I riferimenti a `codex`, v43 e v44 nelle sezioni e nei manifest sottostanti descrivono le verifiche storiche della migrazione e non la configurazione corrente. La cronologia conserva tutte le versioni; la v45 modifica soltanto numero, data, ora e i due riferimenti al ramo in D2.1. I nove stati dei materiali registrano correttamente la v44 consultata durante l’importazione.

Prima dell’integrazione sono stati verificati GitHub Pages disattivato, nessun workflow Actions, nessun deployment e nessun ambiente configurato. Le impostazioni di pubblicazione restano invariate. Il precedente blocco HTTP 403 è risolto.

## Fonti e confronto

- [Master Google Doc v43](https://docs.google.com/document/d/1EA-rZut3LOfWJYeTZ3DQ0uArP8NNyTUZFOY4UgQGJBg/edit): accessibile; testo completo di 53.679 byte. Lettura tramite fetch ed esportazione `text/plain` identiche byte per byte.
- [Materiali](https://drive.google.com/drive/folders/1ZbpsRZnrZCda3ZC1z54WId5qcsIL1TRE): master, 16 HTML, cartella `quiz` e cartella di lavorazione.
- [Quiz](https://drive.google.com/drive/folders/1Kz7zJJGu53ek18EE9G5NP1pUcfPp1L7C): 2 HTML, 1 JSON e 1 TXT.
- [Lavorazione](https://drive.google.com/drive/folders/1LWZM2idyl7U89g1PvF4xcppsTQkyuhU_): accessibile e vuota. Non esistono bozze o stati Drive da trasferire.

L’inventario include tutte le sottocartelle scoperte. Le tre liste sono state rilette a fine importazione e risultano identiche. Il ramo `codex` conteneva soltanto `README.md`, mantenuto invariato: nessun HTML da sostituire e nessun conflitto di identità. Tutti i 20 materiali risultavano mancanti; nessun materiale più vecchio ha sostituito file del repository. Nomi originali e struttura `quiz/` sono conservati.

## Trasferimento successivo del quiz

Su richiesta dell’utente, i quattro materiali originariamente in `quiz/` sono stati trasferiti nel repository [rickymusu-bit/quiz](https://github.com/rickymusu-bit/quiz), verificati byte per byte nel commit `f102b5583ff96c6574a32e32f20129535f6b9341` e rimossi dall’albero corrente di fisica. La cronologia di fisica conserva gli originali; l’inventario della migrazione sottostante descrive la copia iniziale, prima di questa separazione. Le otto dispense italiane costituiscono il sito di fisica; il quiz non è pubblicato da questo repository.

## File importati

18 HTML, 1 JSON e 1 TXT: **60.424.211 byte** complessivi. Ogni file è copiato integralmente, senza conversioni o modifiche didattiche.

| Percorso | Byte | Modifica Drive (UTC) |
| --- | ---: | --- |
| [potenza_termica_conduzione_convezione_it_v4_20261016.html](../../potenza_termica_conduzione_convezione_it_v4_20261016.html) | 5627829 | 2026-10-16T07:32:29.119Z |
| [stati_della_materia_e_passaggi_di_stato_v6_20261016.html](../../stati_della_materia_e_passaggi_di_stato_v6_20261016.html) | 19863151 | 2026-10-16T06:25:40.172Z |
| [bilancio_conservazione_rendimento_it_v9_20261013.html](../../bilancio_conservazione_rendimento_it_v9_20261013.html) | 1009728 | 2026-10-13T18:18:10.125Z |
| [metodo_scientifico_fr_v5_20261013.html](../../metodo_scientifico_fr_v5_20261013.html) | 1468039 | 2026-10-13T18:18:01.056Z |
| [strumenti_errori_incertezza_fr_v4_20261013.html](../../strumenti_errori_incertezza_fr_v4_20261013.html) | 1278289 | 2026-10-13T18:17:56.660Z |
| [grafici_piano_cartesiano_sq_v5_20261013.html](../../grafici_piano_cartesiano_sq_v5_20261013.html) | 804572 | 2026-10-13T18:17:52.329Z |
| [sistema_internazionale_notazione_sq_v8_20261013.html](../../sistema_internazionale_notazione_sq_v8_20261013.html) | 826975 | 2026-10-13T18:17:47.995Z |
| [strumenti_errori_incertezza_sq_v4_20261013.html](../../strumenti_errori_incertezza_sq_v4_20261013.html) | 1277865 | 2026-10-13T18:17:44.085Z |
| [grafici_piano_cartesiano_fr_v5_20261013.html](../../grafici_piano_cartesiano_fr_v5_20261013.html) | 804878 | 2026-10-13T18:17:12.164Z |
| [metodo_scientifico_sq_v5_20261013.html](../../metodo_scientifico_sq_v5_20261013.html) | 1467912 | 2026-10-13T18:17:08.230Z |
| [sistema_internazionale_notazione_it_v8_20261013.html](../../sistema_internazionale_notazione_it_v8_20261013.html) | 828177 | 2026-10-13T18:17:03.729Z |
| [sistema_internazionale_notazione_fr_v8_20261013.html](../../sistema_internazionale_notazione_fr_v8_20261013.html) | 827784 | 2026-10-13T18:16:59.957Z |
| [metodo_scientifico_it_v5_20261013.html](../../metodo_scientifico_it_v5_20261013.html) | 1467999 | 2026-10-13T18:16:55.557Z |
| [strumenti_errori_incertezza_it_v4_20261013.html](../../strumenti_errori_incertezza_it_v4_20261013.html) | 1279166 | 2026-10-13T18:16:50.883Z |
| [grafici_piano_cartesiano_it_v5_20261013.html](../../grafici_piano_cartesiano_it_v5_20261013.html) | 804753 | 2026-10-13T18:16:45.993Z |
| [lavoro_energie_potenza_it_v8_20261013.html](../../lavoro_energie_potenza_it_v8_20261013.html) | 12105085 | 2026-10-13T18:16:42.093Z |
| [quiz/Template_dataset_quiz_argomenti_v1_20261008.json](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Template_dataset_quiz_argomenti_v1_20261008.json) | 6126 | 2026-10-14T07:02:51.146Z |
| [quiz/Prompt_generazione_dataset_quiz_v1_20261008.txt](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Prompt_generazione_dataset_quiz_v1_20261008.txt) | 9714 | 2026-10-14T07:02:47.260Z |
| [quiz/Chi_vuol_essere_rimandato_regole_v9_20261008.html](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Chi_vuol_essere_rimandato_regole_v9_20261008.html) | 2305334 | 2026-10-14T07:02:44.399Z |
| [quiz/Chi_vuol_essere_rimandato_quiz_v3_20261008.html](https://github.com/rickymusu-bit/quiz/blob/f102b5583ff96c6574a32e32f20129535f6b9341/Chi_vuol_essere_rimandato_quiz_v3_20261008.html) | 6360835 | 2026-10-14T07:02:40.085Z |

Il [manifest](inventario.json) registra ID e URL della fonte, data, dimensione, SHA-256 locale, esito del confronto e destinazione di ogni materiale. [fonti-drive.json](fonti-drive.json) conserva l’inventario delle cartelle.

## Master e organizzazione nella migrazione v44

- `MASTER_PROMPT.md` v44 deriva dal testo v43 effettivamente recuperato. Il commit `e67f267599826221c963f4730e5e4d80069541bd` conserva la v43 integrale, inclusi BOM e terminatori originali.
- Tutte le 29 intestazioni/sezioni sono presenti. Dieci sostituzioni circoscritte, registrate in [modifiche-master.json](modifiche-master.json), interessano intestazione, B6, D2, D2.1 e il riferimento alla cronologia in D3.1. Il testo al di fuori di tali sostituzioni è identico, normalizzati BOM e terminatori di riga.
- Parti didattiche A e C, workflow B1–B5, controlli D1 e prevalenza D3 invariati; approvazione della bozza e via alla realizzazione restano obbligatori secondo il master. Versione interna progressiva, data e ora Europe/Rome preservate.
- GitHub è la fonte ufficiale secondo le nuove regole; la destinazione definitiva dei file è `main`, tramite la PR #1. Git conserva la cronologia; gli stati usano nomi Markdown stabili.
- Creati `AGENTS.md` e nove stati di importazione: otto argomenti e quiz. Nessuna approvazione pregressa è stata dedotta, nessuna nuova bozza generata. `lavorazione/README.md` descrive dove conservare `bozza.md`, `bozza.html` e `risorse/` quando esistono contenuti effettivi.

## Verifiche e problemi rimasti

Tutti i 20 file hanno dimensione uguale a quella dichiarata da Drive e contenuto identico ai download; SHA-256 locali registrati. Il connettore non espone i checksum remoti richiesti: non viene dichiarato un confronto crittografico con un hash fornito da Google. Nessun duplicato byte per byte, nessuna collisione di percorso o serie con stessa lingua/versione. Italiano, francese e albanese sono varianti distinte.

UTF-8 leggibile per tutti i file, JSON valido, 18 HTML con doctype e chiusura completa. Verificati riferimenti HTML, URL CSS, iframe `srcdoc`, ancore, file locali e **168 risorse base64**. Non risultano file locali mancanti né collegamenti di navigazione interni mancanti. Rimane un riferimento CSS a `#arrowHead` senza definizione nel file sugli stati della materia: la classe `.arrow-line` compare solo nella regola CSS e non è usata nel documento. Anomalia preesistente, conservata e non corretta durante il trasferimento.

Il file `stati_della_materia_e_passaggi_di_stato_v6_20261016.html` pesa **19.863.151 byte**, sopra la soglia di attenzione di 18 MB e sotto il limite di 20 MB del master. Nessuna compressione o modifica delle immagini è stata eseguita.

Controllati 23 URL esterni: 18 restituiscono HTTP 200; un URL ONU restituisce 403, tre URL YouTube sono bloccati dal proxy con 403 e Openclipart va in timeout. Non è stato possibile confermare la disponibilità di questi cinque collegamenti; non sono stati sostituiti. Un HTTP 200 non certifica la correttezza scientifica del contenuto o l’effettiva riproducibilità di un video. Gli esiti puntuali sono riportati sotto e in [verifiche.json](verifiche.json).

Non sono state eseguite prove visuali su browser/dispositivi né verifiche scientifiche o nuove approvazioni dei contenuti: questa migrazione conserva gli HTML integralmente. Non erano disponibili originali separati o registri di approvazione nella lavorazione Drive; questa assenza è riportata negli stati e non impedisce la copia dei materiali presenti.

| Esito HTTP | Collegamento | Nota |
| --- | --- | --- |
| 200 | https://afdc.energy.gov/fuels/properties?properties=chemical_structure | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://commons.wikimedia.org/wiki/File:Electric-wire-rope-hoist.jpg | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://commons.wikimedia.org/wiki/File:Pumped_Storage_Hydroelectric_Power_Plant_01-ja.svg | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://creativecommons.org/licenses/by-sa/4.0/ | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://creativecommons.org/licenses/by/4.0/ | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://fsr.eui.eu/wp-content/uploads/160502Fornelli.pdf | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| non verificabile | https://openclipart.org/detail/62857/perspective-wooden-crate | The read operation timed out |
| 200 | https://pacompendium.com/running/ | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10818145/ | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://science.gsfc.nasa.gov/attic/cosmicopia.gsfc.nasa.gov/qa_sun.html | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://www.fia.com/news/new-era-competition-fia-showcases-future-focused-formula-1-regulations-2026-and-beyond | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://www.openpowerlifting.org/u/nathanbaptist | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://www.terna.it/it/sistema-elettrico/statistiche/pubblicazioni-statistiche | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://www.terna.it/it/sistema-elettrico/statistiche/pubblicazioni-statistiche/r/nguarda | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 403 | https://www.un.org/en/observances/end-nuclear-tests-day/history | errore HTTP; non prova da solo che il contenuto non esista |
| 200 | https://www.vestas.com/en/energy-solutions/offshore-wind-turbines/V236-15MW | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://www.vestas.com/en/media/company-news/2022/vestas--v236-15-0-mw-prototype-wind-turbine-produces-fi-c3691167 | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| 200 | https://www.wartsila.com/media/news/12-09-2006-the-world%27s-most-powerful-engine-enters-service | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| non verificabile | https://www.youtube.com/watch?v=0fKBhvDjuy0 | <urlopen error Tunnel connection failed: 403 Forbidden> |
| non verificabile | https://www.youtube.com/watch?v=oSCX78-8-q0 | <urlopen error Tunnel connection failed: 403 Forbidden> |
| 200 | https://x.com/elonmusk/status/2012500968571637891 | Risposta HTTP ricevuta; contenuto non validato semanticamente. |
| non verificabile | https://youtu.be/Sdpcjm2vmLY?is=jQY0_qg6RCA-Pd_9 | <urlopen error Tunnel connection failed: 403 Forbidden> |

## Ripresa e consegna

Per riprendere il lavoro usa `main` e crea un ramo temporaneo per il compito:

```sh
git clone https://github.com/rickymusu-bit/fisica.git
cd fisica
git switch main
git pull --ff-only
git switch -c lavoro/nome-compito
```

Leggi `MASTER_PROMPT.md` e lo stato del capitolo pertinente prima di lavorare. `AGENTS.md` prescrive ora rami temporanei derivati da `main`. L’unione nel ramo ufficiale segue le approvazioni richieste dal master e dall’utente. I rami `codex` e `migrazione/materiale-didattico-drive` sono superflui dopo l’integrazione, purché tutti i loro commit siano raggiungibili da `main`.

Nessun materiale è stato eliminato o modificato su Drive. Nessuna impostazione o file di pubblicazione del sito è stato attivato o modificato.
