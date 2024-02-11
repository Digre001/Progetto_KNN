# Progetto_KNN

## Indice
- [Classificatore di Apprendimento Automatico per la Classificazione dei Tumori](#classificatore-di-apprendimento-automatico-per-la-classificazione-dei-tumori)
- [Configurazione dell'Ambiente](#configurazione-dellambiente)
- [Panoramica](#panoramica)
- [Requisiti di Input](#requisiti-di-input)
- [Output](#output)

## Classificatore di Apprendimento Automatico per la Classificazione dei Tumori
Benvenuti nella nostra repository per lo sviluppo di un classificatore di apprendimento automatico destinato a classificare i tumori come benigni o maligni in base alle caratteristiche specificate dall'utente. Il nostro obiettivo principale è costruire un robusto pipeline che addestri e valuti un modello in base alle caratteristiche fornite.

## Configurazione dell'Ambiente
Prima di eseguire il codice, è importante prendere alcune precauzioni e configurare correttamente l'ambiente. Seguire questi passaggi:
1. Creare un Ambiente Virtuale:
   - Aprire il terminale o il prompt dei comandi.
   - Eseguire il seguente comando per creare un ambiente virtuale chiamato "venv": `python -m venv venv`
2. Attivare l'Ambiente Virtuale:
   - Se si utilizza Windows: `.\venv\Scripts\activate`
   - Se si utilizza Unix o MacOS: `source ./venv/Scripts/activate`
3. Disattivare l'Ambiente (quando si ha finito):
   - Utilizzare il seguente comando per disattivare l'ambiente virtuale: `deactivate`
4. Installare le Dipendenze:
   - Dopo aver clonato il progetto ed attivato l'ambiente virtuale, installare le dipendenze richieste con: `pip install -r requirements.txt`
     Questo comando scarica tutti i moduli non standard necessari dall'applicazione.
5. Se la versione di Python utilizzata per generare l'ambiente virtuale non contiene una versione aggiornata di pip, aggiornare pip con: `pip install --upgrade pip`
  
Una volta configurato l'ambiente virtuale e installate le dipendenze, è possibile eseguire l'applicazione. Basta navigare fino al file `main.py` ed eseguirlo.

## Panoramica
Questo progetto si concentra su tre fasi principali:

- Preelaborazione dei Dati: Iniziamo caricando il dataset e gestendo i valori mancanti nel modo che riteniamo più opportuno. Successivamente, suddividiamo il dataset in caratteristiche (variabili indipendenti) ed etichette target (classi).

- Sviluppo del Modello: Qui sviluppiamo un classificatore k-nearest neighbors (k-NN) da zero, evitando l'uso di librerie esterne che implementano già il classificatore k-NN. Il classificatore calcola la distanza euclidea tra ogni campione nel set di test e tutti i campioni nel set di addestramento per identificare i k vicini. La classe per ciascun campione di test è determinata dall'etichetta più comune tra i suoi k vicini, con selezione casuale in caso di parità.

- Valutazione del Modello: Valutiamo le prestazioni del modello attraverso due approcci:
    1. Metodo Holdout, seguendo le percentuali specificate per la divisione dei dati di addestramento e test.
    1. Leave-p-out Cross Validation, in cui vengono lasciati fuori p campioni per il test e il modello viene addestrato sui campioni rimanenti, ripetendo questo processo per tutte le possibili combinazioni.

### Preelaborazione dei Dati
In questa sezione, descriviamo i passaggi di preelaborazione dei dati coinvolti nel nostro pipeline. Ci sono quattro file in questa sezione, che ora si trovano all'interno di una cartella chiamata "Preprocessing". Questi file facilitano il caricamento dei dati, assicurandosi che siano in formato CSV, e gestiscono i valori mancanti attraverso vari metodi (eliminazione, media, moda e mediana) scelti dall'input dell'utente. Una volta completato, i dati vengono divisi in caratteristiche ed etichette, seguito dalla normalizzazione delle caratteristiche.

Files in questa Sezione:

Preprocessing/ReaderCSV.py  
Preprocessing/ReaderFactory.py  
Preprocessing/DFInputer.py  
Preprocessing/F_and_L.py  

Questi passaggi di preelaborazione sono cruciali per preparare il dataset prima di addestrare il modello di apprendimento automatico. Aiutano a garantire l'integrità dei dati e migliorano le prestazioni del modello.

### Sviluppo del Modello 
In questa sezione, descriviamo il processo di sviluppo del modello, concentrando l'attenzione sulla creazione di un classificatore k-nearest neighbors (k-NN) implementato in un unico file. I file in questa sezione sono ora posizionati all'interno di una cartella chiamata "KNNalgorithm"

Files in questa Sezione:

KNNalgorithm/KNN.py

Questo file racchiude la logica principale del classificatore k-NN e serve da base per il nostro processo di sviluppo del modello. Sentiti libero di esplorare ed estendere questa implementazione per adattarla alle tue specifiche esigenze.

### Valutazione del Modello 
In questa sezione, elaboriamo il processo di valutazione del modello, inclusa la divisione dei dati, il calcolo delle metriche di valutazione e il metodo scelto per la convalida. I file in questa sezione sono ora posizionati all'interno di una cartella chiamata "Valutazione."

Files in questa Sezione:

Valutazione/Evaluation.py  
Valutazione/Metriche_L.py  
Valutazione/Split_Data.py

Assicurati di selezionare il metodo di convalida che meglio si adatta alle tue esigenze e alle caratteristiche del dataset. Sentiti libero di esplorare e personalizzare le metriche di valutazione e le tecniche di convalida come necessario per la tua specifica applicazione.

## Requisiti di Input
Prima di eseguire il modello di valutazione, gli utenti devono fornire determinati input. Ecco una descrizione dei requisiti di input richiesti:
1. Gestione dei Valori Mancanti (Gestione):
    - Gli utenti devono scegliere un metodo appropriato per gestire i valori mancanti:
        - Input: Valore intero che rappresenta il metodo selezionato (ad esempio, 1 per eliminazione, 2 per media, ecc.).
          
1. Numero di Vicini per KNN (k):
     - Gli utenti specificano il numero di vicini da considerare nell'algoritmo dei k-vicini più prossimi:
        - Input: Valore intero che rappresenta il numero di vicini (k).
Selezione del Modello di Valutazione (Modello_valutazione):

1. Gli utenti selezionano il modello di valutazione, sia Holdout che Leave-p-out Cross Validation:
   - Input: Singolo carattere che rappresenta il modello scelto (H per Holdout, L per Leave-p-out Cross Validation).
     
1. Dimensione del Set di Addestramento (train_size):
    - Per il metodo Holdout, gli utenti specificano la percentuale del dataset utilizzata per l'addestramento:
        -Input: Valore float compreso tra 0 e 1 che rappresenta la percentuale (ad esempio, 0.7 per 70%).
    -Se viene scelta la Leave-p-out Cross Validation, gli utenti specificano il numero di campioni da studiare:
        - Input: Valore intero che rappresenta il numero di campioni (p).
          
1. Numero di Esperimenti per Leave-p-out (N_esperimenti):
    - Se viene scelta la Leave-p-out Cross Validation, gli utenti specificano il numero di esperimenti da condurre:
        - Input: Valore intero che rappresenta il numero di esperimenti (K).
          
1. Selezione delle Metriche (Metriche):
    - Gli utenti selezionano le metriche di valutazione da utilizzare per valutare le prestazioni del modello:
        - Input: Possono essere scelte più metriche in base alla funzione implementata.
Gli utenti devono fornire questi input tramite i metodi di classe forniti. Assicurarsi che vengano forniti input corretti per facilitare una valutazione accurata delle prestazioni del modello.

## Output

Durante l'esecuzione del programma, vengono calcolate varie metriche per valutare le prestazioni del modello di classificazione. Di seguito sono elencate le metriche calcolate su un dataset di esempio ('breast_cancer.csv'):

1. Accuracy Rate: Questa metrica misura la percentuale di previsioni corrette rispetto al totale delle previsioni effettuate dal modello. In altre parole, rappresenta la precisione complessiva del modello nel classificare le istanze del dataset.

2. Error Rate: Questa metrica misura la percentuale di previsioni errate rispetto al totale delle previsioni effettuate dal modello. Complementa il Tasso di Accuratezza e fornisce una misura della percentuale di errori nelle classificazioni del modello.

3. Sensitivity: Nota anche come Tasso di Veri Positivi (TPR), questa metrica misura la capacità del modello di identificare correttamente le istanze positive (classe di interesse) rispetto al totale delle istanze positive nel dataset. Indica la proporzione di veri positivi rispetto al totale dei veri positivi.

4. Specificity: Nota anche come Tasso di Veri Negativi (TNR), questa metrica misura la capacità del modello di identificare correttamente le istanze negative rispetto al totale delle istanze negative nel dataset. Indica la proporzione di veri negativi rispetto al totale dei veri negativi.

5. Geometric Mean: Questa metrica calcola la radice quadrata del prodotto di Sensibilità e Specificità. È una misura della media geometrica tra queste due metriche e viene utilizzata per valutare l'equilibrio tra la capacità del modello di predire correttamente i valori positivi e negativi. Una Media Geometrica alta indica un buon equilibrio tra Sensibilità e Specificità.

Tutte queste metriche forniscono una panoramica completa delle prestazioni del modello di classificazione e vengono utilizzate per valutare diversi aspetti della sua capacità predittiva. Inoltre, sono disponibili grafici che mostrano la tendenza delle metriche durante gli esperimenti di valutazione. Ad esempio: il grafico delle metriche holdout mostra la distribuzione delle metriche per un singolo esperimento attraverso un grafico a barre delle metriche richieste; mentre il grafico delle metriche leave-p-out mostra la tendenza delle metriche su più esperimenti, e c'è anche un grafico a barre che mostra la media di tutte le metriche per tutti gli esperimenti.

### Cambiamenti e Variazioni nei Parametri
Gli output descritti sopra potrebbero variare a seconda di come vengono inseriti i parametri di input da parte dell'utente. Quelli che potrebbero portare a cambiamenti significativi nell'output del modello di classificazione potrebbero essere il k per lo studio dei vicini di KNN e il K per definire il numero di esperimenti da eseguire nel Leave_P_Out.

- Variando k per i Vicini di KNN, che determina il numero di vicini da considerare durante la classificazione di un punto, si può influenzare la complessità del modello e, di conseguenza, le prestazioni di classificazione.

   1. Riducendo il valore di k, il modello potrebbe diventare più sensibile ai dettagli locali dei dati. Ciò potrebbe portare a una maggiore variazione nelle previsioni, specialmente in presenza di dati rumorosi o di molti valori anomali.
   
   2. Aumentando il valore di k, il modello tende a generalizzare di più. In altre parole, il modello prende decisioni basate su un numero maggiore di punti dati, il che farebbe sì che il modello diventi meno sensibile ai dettagli locali, portando ad una diluizione dei confini decisionali tra le classi, compromettendo così le prestazioni del modello su dati più complessi e/o rumorosi.

- Variando K, ovvero il numero di Esperimenti da eseguire durante la cross-validation leave-p-out, potrebbe influenzare la robustezza della valutazione del modello.

   1. Riducendo il numero di esperimenti, si ottiene una stima delle prestazioni del modello basata su meno suddivisioni del dataset. Ciò potrebbe portare a una maggiore varianza nelle stime delle metriche di valutazione, poiché sono basate su un campione più piccolo di dati.
   
   2. Aumentando il numero di esperimenti, si ottiene una stima più robusta delle prestazioni del modello, basata su un numero maggiore di suddivisioni del dataset. Ciò potrebbe portare a una maggiore stabilità nelle stime delle metriche di valutazione, riducendo l'incertezza dovuta alla variabilità nei dati di addestramento e di test.
