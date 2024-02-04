# Importo le librerie necessarie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Split_Data import Split_data
from M_development import Knn

class Evaluation:
    '''
       costruttore:

       features : pandas.DataFrame (significa che la variabile feature deve essere passata come un DataFrame di pandas)
           sono i dati che verranno usati per addestrare e testare il modello

       target_lable : pandas.Series (significa che la variabile target deve essere passato come una lista/serie di pandas)
           sono i dati che utilizzeremo per verificare il training e per verificare il test

       train_size : int
           percentuale di dati che verranno utilizzati per il metodo di holdout

       N_esperimenti: int
           numero di esperimenti da fare per il leavePout corss validation

       metriche_scelte : list
           lista che contiene le metriche scelte dall'utente

       '''
    def __init__(self, features: pd.DataFrame, target_lable: pd.Series, train_size: int, N_esperimenti: int, K, metriche_scelte: list):
        self.features = features
        self.target = target_lable
        self.train_size = train_size
        self.N_esperimenti = N_esperimenti
        self.metriche_scelte = metriche_scelte
        self.K = K

        #creo istanza per richiamare la classe Split_Data
        self.Split = Split_data(features, target_lable, train_size, N_esperimenti,K)

    pass


    def valutazione_holdout(self):
        # richiamo il metodo che va a splittare i dati in dati di train e dati di test
        X_train, Y_train, x_test, y_test = self.Split.Split_Holdout()

        #Alleno il mio modello richiamado il Knn e passandogli i dati di train
        Modello_knn=M_development(X_train,Y_train)

        #effettue le previsioni con il modello addestrato alla riga di codice sopra
        Previsioni=Modello_knn.predizione(x_test)

        

    def valutazione_leave_p_out(self):
        pass