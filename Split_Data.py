import pandas as pd


class Split_data:
    '''
        costruttore:
        features: sono i dati che verranno usati per addestrare e testare il modello
        target: sono i dati che utilizzeremo per verificare il training e per verificare il test
        train_size: percentuale di dati che verranno utilizzati per il metodo di holdout
        N_esperimenti: numero di esperimenti da fare per il leavePout corss validation
        '''
    def __init__(self, features: pd.DataFrame, target: pd.Series, train_size: int, N_esperimenti: int, k):
        self.features = features
        self.target = target
        self.train_size = train_size
        self.N_esperimenti=N_esperimenti


    '''
        I valori che mi servono e che quindi voglio riutilizzare sono questi:
        (tramite return li inserisco nella variabile Split_Holdout)
        
        X_train_indices: con questo mi sto campionando una frazione tramite (train_size) degli indici del DataFrame features
            in questo caso utilizzo .index per restituirmi gli indici associati alle righe campionate in modo tale da 
            poter poi utilizzare le stesse righe associate alla loro target label. 

        X_train: dati per addestrare il modello
        Y_train: dati per addestrare il modello (risultato che conosco)
        x_test: dati per tetare il modello
        y_test: dati per testare il modello finale confrpntandolo con le uscite che mi restituisce il mio modello creato
        '''

    def Split_Holdout(self):
        # Prendo gli indici dei dati per il training secondo una percentuale specificata in input
        X_train_indices = self.features.sample(frac=self.train_size).index

        #Usando gli indici ottenuti sopra, seleziono le righe corrispondenti dal DataFrame originale delle features
        X_train = self.features.loc(X_train_indices)

        # Prendo i dati per il test. Sono tutti i dati che non sono stati presi per il training
        # questo lo faccio tramite drop rimuovendoi dal DataFrame le righe selezionate per il training
        x_test = self.features.drop(X_train_indices)

        # Mi salvo le y di train corrispondenti alle x di train
        # selezionando i valori target corrispondenti algi indici delle righe selezionate per il training.
        Y_train = self.target.loc(X_train_indices)

        # Mi salvo le y di test corrispondenti alle x di test
        # rimuovendo dalla Series dei target gli indici delle righe corrispondenti a quelle selezionate per il training.
        y_test = self.target.drop(X_train_indices)

        return X_train, Y_train, x_test, y_test






    def Slpit_leave_p_out(self):
        # creo in n il numero di righe del DataFrame delle features e in m le colonne.
        n, m = self.features.shape[0], self.features.shape[1]

        # Inizializzo le variabili di output
        X_TRAIN, Y_TRAIN, X_TEST, Y_TEST = [], [], [], []

        # Voglio calcolare tutte le combinazioni degli indici senza duplicati in modo tale poi da costruire i set
        #di train e i set di test
        indici_totali = list(range(n))
        Combinazioni = tutte_le_combinazioni(indici_totali, p)


def tutte_le_combinazioni(indici, k, current=[]):

        pass