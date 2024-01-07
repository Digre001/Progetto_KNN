from input import Input # sto importando la classe Input per riprendere i valori immessi dall'utente per inizializzare lo spit del data set
# import il data set

class Split_Data():

    '''spiegazione classe'''

    def __init__(self):
        pass

    #prendo i dati del Data Base

    #Prendo i dati inseriti in input

    #se Holdout allora eseguo

    def Holdout(self):

        percentuale_test=1-self.train_size #cqalcolo la percentuale di test facendo 1 - la percentuale scelta dall'utente come percentale di training

        num_totale_dati = len(self.data) #calcolo numero totale di dati (righe del dataset)

        train_set = int(num_totale_dati * self.train_size) #calcolo il numero di righe usate per il training e creo il set di training

        test_set = num_totale_dati - train_set #calcolo numero di righe usate per il test e creo il set di test

    # se Leave-p-out Cross Validation eseguo

    def Leave_P_Out:
        pass
