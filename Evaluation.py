# Importo le librerie necessarie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Split_Data import Split_data
from M_development import Knn
from Metriche_L import Metriche

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
    def __init__(self, features: pd.DataFrame, target_lable: pd.Series, train_size: int, N_esperimenti: int, p, metriche_scelte: list):
        self.features = features
        self.target = target_lable
        self.train_size = train_size
        self.N_esperimenti = N_esperimenti
        self.metriche_scelte = metriche_scelte
        self.p = p

        #creo istanza per richiamare la classe Split_Data
        self.Split = Split_data(features, target_lable, train_size, N_esperimenti,p)

    pass

    '''
        La valutazione holdout consiste in:
        1. Dividire i dati casualmente: viene specificata la percentuale di split in input (richiameremo spilt_data).
        2. Addestrare il modello: tramite X_train ed Y_train.
        3. Testare il modello: tramite x_test ed y_test.
        4. Valutare le performance: tramite le y_test valutare il modello e poi tramite specifiche metriche
            specificate dall'utente valutarne le prestazioni.
        5. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello 
            generalizza sui dati sconosciuti.
        6. plot delle metriche trtamite grafico a barre

        '''
    def valutazione_holdout(self):
        # richiamo il metodo che va a splittare i dati in dati di train e dati di test
        X_train, Y_train, x_test, y_test = self.Split.split_Holdout()

        #Alleno il mio modello richiamado il Knn e passandogli i dati di train
        Modello_knn=M_development(X_train,Y_train)

        #effettue le previsioni con il modello addestrato alla riga di codice sopra
        Previsioni=Modello_knn.predizione(x_test)

        #Istanzio il file per lavorare con le metriche
        C_Metriche=Metriche(y_test,Previsioni,self.metriche_scelte)

        #Calcolo le metriche
        Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean=C_Metriche.calcolo_matrix_metriche()

        #Salvo le metriche in un file .txt
        C_Metriche.salvare_metriche(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean)
        
        #plottare le metriche
        C_Metriche.plot_metriche_holdout_e_media(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean)

        

    def valutazione_leave_p_out(self):
        # Inizializzo le liste che conteranno i valori delle metriche calcolate per ogni iterazione
        Accuracy_rate_Lista = []
        Error_rate_Lista = []
        Sensitivity_Lista = []
        Specificity_Lista = []
        Geometric_mean_Lista = []

        # richiamo il metodo che va a splittare i dati in dati di train e dati di test
        X_train, Y_train, x_test, y_test = self.Split.slpit_leave_p_out()

        # il processo viene ripetuto N_esperimenti (K) volte decisi dall'utente
        for _ in range(self.N_esperimenti):
            # Alleno il modello fornendogli i dati di training
            Modello_knn = M_development(X_train[_], Y_train[_])

            # Effettuo la predizione con il modello allenato precedentemente
            Previsioni = Modello_knn.predizione(x_test[_])

            # Istanzio il file per lavorare con le metriche
            C_Metriche = Metriche(y_test[_], Previsioni, self.metriche_scelte)

            # richiamo il metodo che va a calcolare le metriche, passandogli i dati di test e le predizioni
            Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean = C_Metriche.calcolo_matrix_metriche()

            # Aggiungo i valori delle metriche calcolate, per questo esperimento, nelle liste
            Accuracy_rate_Lista.append(Accuracy_rate)
            Error_rate_Lista.append(Error_rate)
            Sensitivity_Lista.append(Sensitivity)
            Specificity_Lista.append(Specificity)
            Geometric_mean_Lista.append(Geometric_mean)

        # Calcolo i valori medi per ogni metrica calcolata nei K esperimetni
        Accuracy_rate_media = np.mean(Accuracy_rate_Lista)
        Error_rate_media = np.mean(Error_rate_Lista)
        Sensitivity_media = np.mean(Sensitivity_Lista)
        Specificity_media = np.mean(Specificity_Lista)
        Geometric_mean_media = np.mean(Geometric_mean_Lista)