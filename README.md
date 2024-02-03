# Progetto_KNN

## Panoramica
Questo progetto implementa un classificatore k-Nearest Neighbors (k-NN) in Python, insieme a funzionalità di pre-elaborazione dei dati e valutazione del modello.
L'obiettivo è consentire agli utenti di caricare un dataset, gestire i valori mancanti, sviluppare un classificatore k-NN e valutarne le prestazioni utilizzando diverse metriche e metodi di validazione.

## Il programma consente agli utenti di specificare i seguenti parametri:
-   Gestione: chiede all'utente di scegleire il metodo piu appropriato da utilizare per la gestione dei dati mancati nel Dataframe (eliminaizone, media, moda, mediana)
-	Numero di vicini (k): chiede all'utente di inserire un numero intero per specificare il numero di vicini da studiare
-   Modello di valutazione (Holdout o Leave-p-out cross validattion): chiede all'utente di selesionare il modello di valutazione,"H" per Holdout e "L" per Leave-p-out cross validation 
-   Train size: nel caso di modello di valutazione Holdout, chiede all'utente di insere una percentuale float compresa tra 0 e 1 del database da usare nel training
-   Numero di campioni da studiare (p): nel caso di modello di valutaizone Leave-p-out Cross Validation, chiede all'utente di inserire un numero di campioni da studiare 
-   Numero di esperiemnti (K): nel caso di modello di valutaizone Leave-p-out Cross Validation, chiede all'utente di inserire il numero di ripetiizone del esperimento
-   Metriche da valutare: chiede al utente di scegliere quali metriche andare a studiare (Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean)

Gli input sono soggeti a dei controlli, (es. k deve essere un numero intero in caso contrario sara richiesto all'utente di reinserire un nuovo valre), tutti a parte p che richiede la consapevoleza del utente.

## Valutazione Individuale delle Sezioni di codice 

### Preprocessing 
Richieste del Data Preprocessing:
1. Caricare il dataset.
1. Gestire i valori mancanti in modo appropriato (scegliete il modo che preferite, non c'è una risposta corretta).
1. Dividere il dataset in features (variabili indipendenti) e target label (classe).

File Python utilizzati in questa sezione: ReaderCSV.py, ReaderFactory.py, DFInputer.py, F&L.py.
Per poter testare singolarmente questa parte del progetto è necessario apportare delle modifiche al file F&L.py:
- Eliminare l'import statement del file input alla riga 3 del codice: `from input import Input`, e di conseguenza tutte le righe associate a questa riga, come la riga 9 `self.input = Input()` e la riga 26 `method = self.input.Gestione`.
- Nella riga 28, togliere method e inserire tra virgolette una delle seguenti opzioni (drop, mean, median, mode). Ad esempio, `df_ready = dfInputer(df).handle_missing_values("mean")`.
- Aggiungere alla fine del codice le seguenti righe:
    - `a = DataSplitter('leggi.csv')`
    - `features, labels = a.process_data()`
    - `print("Features:\n", features)`
    - `print("Labels:\n", labels)`

### Knn 
Richieste per lo sviluppo del modello:
1. Sviluppare un classificatore k-nn da zero (senza utilizzare librerie esterne che abbiano già implementato il classificatore k-nn).
1. Per ogni campione dell'insieme di test, calcolare la distanza da tutti i campioni del set di training e identificare i k campioni più vicini, utilizzando la distanza euclidea.
1. Classificare ogni campione dell'insieme di test scegliendo l'etichetta più comune tra i k vicini. In caso di parità tra le etichette, scegliere in modo casuale.

Unico file python utilizato per questa sezione: M_Development.py
Per poter testare singolarmente questa parte del progetto è necessario apportare delle modifiche al file F&L.py:
