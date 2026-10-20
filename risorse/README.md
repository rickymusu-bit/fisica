# Crediti e licenze

Il registro autorevole è `crediti.json`. `crediti.html`, i riquadri incorporati degli HTML e `licenze/Lexend-OFL.txt` sono risultati generati: aggiornarli con `python3 scripts/credits.py --sync`, senza editarli separatamente. La build esegue gli stessi controlli di `--check` e rifiuta risultati non aggiornati. Nessuna richiesta di rete è necessaria su GitHub Pages.

`resources` contiene una scheda per fonte originale, con identificativo stabile, descrizione, autore, fonte, licenza e URL, modifiche, avvisi originali integrali (`notices`), provenienze documentali e impronte dei file quando disponibili. I campi null indicano dati non documentati: non completarli per deduzione. Le varianti degli avvisi conservano le modifiche relative ai singoli utilizzi. Le note generali originali restano schede prive di una fonte, senza inventare una corrispondenza individuale.

`documents` associa ciascun articolo alle schede e alla variante dell’avviso, con titolo e ancora stabili. `assets` deduplica le risorse effettivamente rilevate per SHA-256 dei byte incorporati, del codice SVG/canvas o dell’URL quando il file non è incorporato. Le occorrenze conservano articolo, descrizione, posizione e associazione alla scheda, se verificabile. L’inventario non implica una licenza. Comprende le anteprime di pausa/movimento ridotto e le immagini annidate nei documenti iframe. I file originali inutilizzati della lavorazione non diventano automaticamente risorse pubblicate.

Per un nuovo articolo utilizzare il tema v10 e specificare i metadati disponibili sulla figura o sull’immagine:

```html
<figure id="figura-1"
        data-credit-source="https://esempio.org/originale"
        data-credit-author="Nome documentato"
        data-credit-license="CC BY 4.0"
        data-credit-license-url="https://creativecommons.org/licenses/by/4.0/"
        data-credit-changes="Ridimensionamento, nessun ritaglio">
  <!-- immagine e didascalia scientifica -->
</figure>
```

Per riutilizzare una scheda è sufficiente `data-credit-id="credit-identificativo"`. `--sync` registra automaticamente nuovi documenti, metadati e occorrenze e genera gli accessi ai crediti. Le risorse senza metadati sono inventariate e segnalate per verifica: lo strumento non recupera né concede autorizzazioni. Verificare le condizioni originali, compresi crediti particolari e modifiche consentite, prima di dichiarare la conformità.

Le venti copertine condividono questo registro: `copertine/manifest.json` contiene i soli dati visivi e il rinvio `credit_id`. Il renderer ricava autore, fonte, licenza e modifiche dalla scheda centrale. I vecchi registri di lavorazione sono conservati come documentazione storica; non sono archivi da compilare nuovamente.

Gli articoli ammessi e la home mostrano un solo comando «Crediti e licenze», che apre la copia incorporata degli avvisi necessari. Il collegamento interno «Crediti di tutti gli articoli» apre la pagina generale online, anche da un file locale. Il dialogo funziona offline; senza JavaScript il collegamento rende il contenuto visibile mediante `:target`. Il copyright e la OFL di Lexend sono incorporati negli HTML che usano il font e distribuiti anche come file di testo. Gli HTML che non usano Lexend non ricevono una falsa attribuzione del font.

Una licenza con modalità particolari prevale sul tema: mantenere l’avviso richiesto vicino alla risorsa e registrare l’eccezione. La migrazione conserva tutte le formulazioni originali, incluse quelle personalizzate di Lipofsky Basketballphoto.com e © Raimond Spekking. Le fonti dei dati numerici e delle informazioni scientifiche specifiche appartengono ai crediti: conservarle con un riferimento al contenuto sostenuto, senza citazioni bibliografiche nel testo, nelle didascalie o nelle note. Per gli HTML confluiscono nel registro unico e negli accessi comuni; nelle bozze si raccolgono nel componente di servizio dei crediti in attesa della realizzazione. Spiegazioni e condizioni fisiche restano nel testo o nelle note. Non eliminare dati, immagini, formule o simulazioni.

La revisione del comando unico comprende home, otto articoli ammessi e modello canonico; non cambia `pubblicazione.json`. I documenti esclusi conservano invariati i loro componenti storici. La lista pubblica «Licenze e attribuzioni da verificare» distingue le provenienze mancanti dagli avvisi trasferiti; la migrazione tecnica non certifica i diritti di questi materiali.

## Crediti correnti e immagini rimosse

I crediti correnti devono riferirsi soltanto alle immagini e agli altri materiali ancora presenti nel documento. A ogni sostituzione o rimozione, aggiornare le associazioni del registro, la pagina generale e i crediti incorporati; eliminare dagli avvisi correnti i riferimenti a media non più usati. La pagina pubblica comprende soltanto i capitoli ammessi e la home. Conservare originali, schede e provenienze storiche nel registro, nei materiali di lavorazione e in Git, senza mostrarli come crediti dei capitoli attuali. Preservare le fonti dei dati e delle spiegazioni ancora utilizzati anche quando non sono associate a un’immagine. Eseguire il controllo delle associazioni con `scripts/credits.py --check` prima della consegna.

`sync_inventory` elimina automaticamente le associazioni dei media con impronte note che non hanno più occorrenze nei documenti correnti; `--check` rifiuta un registro che conserva tali associazioni. Le schede storiche non vengono cancellate. Le fonti testuali e gli avvisi generali privi di impronte richiedono un controllo di pertinenza e restano distinti dai media: la loro assenza dall’inventario delle immagini non ne autorizza la rimozione. I documenti esclusi mantengono invariati i crediti storici nei propri sorgenti e non compaiono nella pagina pubblica.
