# Importo le librerie necessarie
import pandas as pd
import numpy as np
from Evalutation.Split_Data import Split_data
from KNNalgorithm.KNN import Knn
from Evalutation.Metriche_L import Metriche

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
    def __init__(self, features: pd.DataFrame, target_lable: pd.Series, train_size: int, N_esperimenti: int, p, metriche_scelte: list,k):
        self.features = features
        self.target = target_lable
        self.train_size = train_size
        self.N_esperimenti = N_esperimenti
        self.metriche_scelte = metriche_scelte
        self.p = p
        self.k = k

        #creo istanza per richiamare la classe Split_Data
        self.Split = Split_data(features, target_lable, train_size, N_esperimenti,p)


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
        X_train_array = X_train.to_numpy()
        Y_train_array = Y_train.to_numpy()
        x_test_array = x_test.to_numpy()
        y_test_array = y_test.to_numpy()
        #Alleno il mio modello richiamado il Knn e passandogli i dati di train
        Modello_knn=Knn(X_train_array,Y_train_array)

        #effettue le previsioni con il modello addestrato alla riga di codice sopra
        Previsioni=Modello_knn.predizione(x_test_array,self.k)

        #Istanzio il file per lavorare con le metriche
        C_Metriche=Metriche(y_test_array,Previsioni,self.metriche_scelte)

        #Calcolo le metriche
        Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean=C_Metriche.calcolo_matrix_metriche()

        #Salvo le metriche in un file .xlsx
        C_Metriche.salvare_metriche(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean)
        
        #plottare le metriche
        C_Metriche.plot_metriche_holdout_e_media(Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean)

    ''' 
        Il processo di valutazione Leave_P_Out Cross Validation consiste in:

        1. Specificare in input il numero di esperimenti (K) da effettuare (che corrisponderanno alle combinazioni da effettuare)
        2. Specificare in input il numero di feature che si vuole usare per i test per i dati di train e test
        3. Addestramento del modello: il modello viene addestrato quindi utilizzando X_train e Y_train
        4. Valutazione delle performance: il modello addestrato viene quindi valutato utilizzando i dati di test (y_test). 
            Le prestazione del modello vengono calcolate tramite diverse metriche scelte dall'utente
        5. Iterazioni multiple: il processo viene ripetuto piu volte (K volte), con nuove suddivisioni casuali del dataset, 
            per ottenere una stima più robusta della performance del modello. Infine le valutazioni multiple vengono aggregate 
            per ottenere una misura comune delle prestazioni del modello.
        6. Analisi dei risultati: si analizzano le metriche trovate per capire quanto il mio modello generalizza sui dati sconosciuti

    '''
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
            Modello_knn = Knn(X_train[_].to_numpy(), Y_train[_].to_numpy())

            # Effettuo la predizione con il modello allenato precedentemente
            Previsioni = Modello_knn.predizione(x_test[_].to_numpy(), self.k)

            # Istanzio il file per lavorare con le metriche
            C_Metriche = Metriche(y_test[_].to_numpy(), Previsioni, self.metriche_scelte)

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

        C_Metriche = Metriche(y_test[_], Previsioni, self.metriche_scelte)
        # richiamo il metodo che va a salvare le metriche calcolate, nel file Metriche.xlsx
        C_Metriche.salvare_metriche(Accuracy_rate_media, Error_rate_media, Sensitivity_media, Specificity_media,Geometric_mean_media)

        # richiamo il metodo che va a plottare l'andamento le metriche calcolate
        C_Metriche.plot_metriche_leave_p_out(Accuracy_rate_Lista, Error_rate_Lista, Sensitivity_Lista, Specificity_Lista,Geometric_mean_Lista)

        # richiamo il metodo che va a plottare la media delle metriche calcolata
        C_Metriche.plot_metriche_holdout_e_media(Accuracy_rate_media, Error_rate_media, Sensitivity_media, Specificity_media,Geometric_mean_media)