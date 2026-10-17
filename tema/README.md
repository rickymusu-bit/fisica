# Sorgenti del tema

Le specifiche ufficiali di aspetto e comportamento sono in [TEMA_GRAFICO.md](../riferimenti/TEMA_GRAFICO.md). Questa cartella contiene la loro implementazione riutilizzabile:

- [capitolo.css](capitolo.css): stile del capitolo e dei comandi.
- [indice.js](indice.js): miglioramenti del pannello laterale quando JavaScript è disponibile.

Il [generatore di Irraggiamento](../lavorazione/irraggiamento/genera_capitolo.py) legge queste sorgenti e le incorpora nell’HTML. La navigazione tra capitoli è realizzata da [chapter_navigation.py](../scripts/chapter_navigation.py), che ricava l’ordine da `index.html`.

Le dispense consegnate non caricano questi file esterni: restano autonome. Gli HTML precedenti e la pagina dimostrativa conservano la loro implementazione incorporata; questa estrazione non ne attesta l’adeguamento al tema corrente.
