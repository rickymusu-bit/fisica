# Archivio di Termologia — revisione completa

Versione v1 — 25 ottobre 2026 (Europe/Rome).

**Produzione completa: 300 domande, 100 per livello.** Sono approvate le 39 domande del campione e del primo lotto; le 261 nuove sono proposte per la revisione del docente. Il via «sta bene, crea tutte quelle rimanenti» autorizza l’intera produzione residua, senza pause fra i lotti; non attribuisce approvazioni preventive ai quesiti nuovi.

[Archivio completo compatibile con il sito](archivio.json). [Metadati di revisione e controlli numerici](revisione.json). [Rapporto delle verifiche](verifica-archivio.md).

Il file di importazione ha i soli sette campi previsti dal validatore. Non viene caricato dal sito pubblico: la collocazione è in lavorazione. Le domande già approvate conservano esattamente ID, contenuti, alternative e soluzioni.

| Livello | Conoscenza | Ragionamento | Calcolo | Totale | Approvate | Nuove proposte |
|---|---:|---:|---:|---:|---:|---:|
| Facile | 30 | 40 | 30 | 100 | 13 | 87 |
| Medio | 30 | 40 | 30 | 100 | 13 | 87 |
| Difficile | 30 | 40 | 30 | 100 | 13 | 87 |
| Totale | 90 | 120 | 90 | 300 | 39 | 261 |

Ogni domanda ha quattro alternative e una sola soluzione. I tempi stimati comprendono lettura, ragionamento, eventuale calcolo e scelta, con limite di 120 secondi. Sono stime progettuali, senza misure osservate in classe. Calcolatrice di base consentita; nessun prerequisito disciplinare esterno a Termologia, oltre a operazioni, proporzioni e conversioni di base.

## Lotti

- [Campione approvato, termo-001–termo-009](bozza.md).
- [Primo lotto approvato, termo-010–termo-039](lotto.md).

- [Lotto 2: 29 nuove proposte](lotti/lotto-02.md).
- [Lotto 3: 29 nuove proposte](lotti/lotto-03.md).
- [Lotto 4: 29 nuove proposte](lotti/lotto-04.md).
- [Lotto 5: 29 nuove proposte](lotti/lotto-05.md).
- [Lotto 6: 29 nuove proposte](lotti/lotto-06.md).
- [Lotto 7: 29 nuove proposte](lotti/lotto-07.md).
- [Lotto 8: 29 nuove proposte](lotti/lotto-08.md).
- [Lotto 9: 29 nuove proposte](lotti/lotto-09.md).
- [Lotto 10: 29 nuove proposte](lotti/lotto-10.md).

## Fonti e workflow

Sono stati usati i dieci capitoli pubblicati di Termologia verificati al commit `ef29a4fe630287c59d707abacd082e2fc0617691`, rimasto invariato all’avvio del lavoro: termodinamica e sistemi; temperatura ed equilibrio; energia interna, calore e calore specifico; bilancio termico; dilatazione; stati della materia; passaggi di stato; conduzione; convezione; irraggiamento. La [base documentale](bozza.md#base-documentale) conserva i collegamenti fissati alle fonti. Non sono stati utilizzati capitoli esclusi o bozze al posto delle fonti pubblicate.

Si applicano il master v69.15, il prompt v1.4.1 e il campione effettivamente approvato. Numeri molto piccoli o grandi sono in notazione scientifica se i prefissi SI non rendono la scrittura più chiara; dati, alternative e spiegazioni seguono la stessa regola.

I riferimenti servono alla revisione; nell’archivio tutti i quesiti hanno soltanto l’ID stabile `category: termologia`, senza classificazione dei capitoli o tag tecnici. Le riprese di uno stesso principio hanno operazioni o condizioni differenti; la verifica di similarità testuale è documentata nel rapporto, senza presentarla come prova automatica di varietà didattica.

La sezione 10, fase 4, del [prompt](../../../quiz/PROMPT_GENERAZIONE_DOMANDE.md) richiede la revisione del docente prima dell’uso. La produzione è completata; non viene dichiarato raggiunto il target di 300 domande approvate finché non sono approvate anche le 261 nuove. Merge e pubblicazione richiedono l’anteprima corrente nella successiva fase di integrazione.
