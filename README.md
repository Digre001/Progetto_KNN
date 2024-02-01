# Progetto_KNN

# Panoramica
Questo progetto implementa un classificatore k-Nearest Neighbors (k-NN) in Python, insieme a funzionalità di pre-elaborazione dei dati e valutazione del modello.
L'obiettivo è consentire agli utenti di caricare un dataset, gestire i valori mancanti, sviluppare un classificatore k-NN e valutarne le prestazioni utilizzando diverse metriche e metodi di validazione.

# Il programma consente agli utenti di specificare i seguenti parametri:
-	Numero di vicini (k): chiede all'utente di inserire un numero intero per specificare il numero di vicini da studiare
-   Modello di valutazione (Holdout o Leave-p-out cross validattion): chiede all'utente di selesionare il modello di valutazione,"H" per Holdout e "L" per Leave-p-out cross validation 
-   Train size: nel caso di modello di valutazione Holdout, chiede all'utente di insere una percentuale float compresa tra 0 e 1 del database da usare nel training
-   Numero di campioni da studiare (p): nel caso di modello di valutaizone Leave-p-out Cross Validation, chiede all'utente di inserire un numero di campioni da studiare 
-   Numero di esperiemnti (K): nel caso di modello di valutaizone Leave-p-out Cross Validation, chiede all'utente di inserire il numero di ripetiizone del esperimento
-   Metriche da valutare: chiede al utente di scegliere quali metriche andare a studiare (Accuracy Rate, Error Rate, Sensitivity, Specificity, Geometric Mean)

Gli input sono soggeti a dei controlli, (es. k deve essere un numero intero in caso contrario sara richiesto all'utente di reinserire un nuovo valre), tutti a parte p che richiede la consapevoleza del utente.



