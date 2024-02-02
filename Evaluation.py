# Importo le librerie necessarie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    def __init__(self, features: pd.DataFrame, target_lable: pd.Series, train_size: int, N_esperimenti: int, k,
                 metriche_scelte: list):
        self.features = features
        self.target = target_lable
        self.train_size = train_size
        self.N_esperimenti = N_esperimenti
        self.metriche_scelte = metriche_scelte
        self.k = k

    pass


    def valutazione_holdout(self):
        pass
