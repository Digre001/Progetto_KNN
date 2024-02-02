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

        X_train: dati per addestrare il modello
        Y_train: dati per addestrare il modello (risultato che conosco)
        x_test: dati per tetare il modello
        y_test: dati per testare il modello finale confrpntandolo con le uscite che mi restituisce il mio modello creato
        '''

    def Split_Holdout(self, features: pd.DataFrame, target: pd.Series, train_size: int):
        # Prendo i dati per il training secondo una percentuale specificata in input
        X_train = self.features.sample(frac=self.train_size)
        # Prendo i dati per il test. Sono tutti i dati che non sono stati presi per il training
        x_test = self.features.drop(X_train.index)

        # Mi salvo le y di train corrispondenti alle x di train
        Y_train = self.target.drop(x_test.index)
        # Mi salvo le y di test corrispondenti alle x di test
        y_test = self.target.drop(X_train.index)

        return X_train, Y_train, x_test, y_test

    pass