import pandas as pd
import numpy as np

class Split_data:
    '''
        costruttore:
        features: sono i dati che verranno usati per addestrare e testare il modello
        target: sono i dati che utilizzeremo per verificare il training e per verificare il test
        train_size: percentuale di dati che verranno utilizzati per il metodo di holdout
        N_esperimenti: numero di esperimenti da fare per il leavePout corss validation
        '''
    def __init__(self, features: pd.DataFrame, target: pd.Series, train_size: int, N_esperimenti: int, p: int):
        self.features = features
        self.target = target
        self.train_size = train_size
        self.N_esperimenti=N_esperimenti
        self.p=p


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

    def split_Holdout(self):
        # Prendo gli indici dei dati per il training secondo una percentuale specificata in input
        X_train_indices = self.features.sample(frac=self.train_size).index

        #Usando gli indici ottenuti sopra, seleziono le righe corrispondenti dal DataFrame originale delle features
        X_train = self.features.loc[X_train_indices]

        # Prendo i dati per il test. Sono tutti i dati che non sono stati presi per il training
        # questo lo faccio tramite drop rimuovendoi dal DataFrame le righe selezionate per il training
        x_test = self.features.drop(X_train_indices)

        # Mi salvo le y di train corrispondenti alle x di train
        # selezionando i valori target corrispondenti algi indici delle righe selezionate per il training.
        Y_train = self.target.loc[X_train_indices]

        # Mi salvo le y di test corrispondenti alle x di test
        # rimuovendo dalla Series dei target gli indici delle righe corrispondenti a quelle selezionate per il training.
        y_test = self.target.drop(X_train_indices)

        return X_train, Y_train, x_test, y_test

    '''
           Questo metodo serve per splittare i dati nel metodo leave_p_out cross validation 
           dove tramite p so quante features usare per il test e poi attraverso tutte le combinazioni 
           degli indici del DataFrame si possiamo associare per ogni indice delle features a quelle target 
           andando a creare cosi tutte le combinazioni richieste tramite il valore N_esperimenti dato dall'utente
           per fare il numero di esperimenti richiesti

           --Return---
           X_TRAIN: dati per addestrare il modello
           Y_TRAIN: dati per addestrare il modello (risultato che conosco)
           x_TEST: dati per tetare il modello
           y_TEST: dati per testare il modello finale confrpntandolo con le uscite che mi restituisce il mio modello creato
           '''
    def slpit_leave_p_out(self):
        # creo in n il numero di righe del DataFrame delle features e in m le colonne.
        n = self.features.shape[0]

        # Inizializzo le variabili di output
        X_TRAIN, Y_TRAIN, X_TEST, Y_TEST = [], [], [], []

        # Voglio calcolare tutte le combinazioni degli indici senza duplicati in modo tale poi da costruire i set
        # di train e i set di test
        indici_totali = list(range(n))
        Combinazioni = tutte_le_combinazioni(indici_totali, self.p,self.N_esperimenti)

        # Limita il numero di combinazioni se specificato
        if self.N_esperimenti is not None and self.N_esperimenti < len(Combinazioni):
            Combinazioni = Combinazioni[:self.N_esperimenti]

        # Per ogni combinazione creo set di training e set di test
        for indici_test in Combinazioni:  # in ogni iterazione del ciclo, indici_test assume il valore di una diversa combinazione di indici ottenuta da Combinazioni

            # gli indici per il set di train vengono calcolati escludendo gli indici presenti in indici_test
            indici_train = [i for i in range(n) if i not in indici_test]

            # Crea le coppie di training e test set:
            # qui prendo gli indici corrispondendti a quelli per il train e vado a prendere i valori con questi stessi indici nel
            # data frame delle featurs e li metto nella colonna uno della variabile train_set e poi allo stesso modo
            # prendo gli stessi valori dal frame dei target con gli stessi indici degli indici_train e li metto nella seconda
            # colonna del train_set
            train_set = (self.features.iloc[indici_train], self.target.iloc[indici_train])

            # faccio allo stesso modo sopra soltanto usando gli indici_test
            test_set = (self.features.iloc[indici_test], self.target.iloc[indici_test])

            # qui aggiungo i valori ottenuti dentro le variabili X_train, Y_train ecc...
            X_TRAIN.append(train_set[0])
            Y_TRAIN.append(train_set[1])
            X_TEST.append(test_set[0])
            Y_TEST.append(test_set[1])

        return X_TRAIN, Y_TRAIN, X_TEST, Y_TEST


'''
questo metodo serve per calcolare tutte le combinazioni possibili dato il numero di gruppi
fornito dall'utente con il valore p, che in questo metodo verrà nominato k. Questo processo viene
effetutato grazie alla ricorsione del metodo che verrà chiamto esso stesso nel suo metodo.
(metodo ricorsivo).

Indici: è la variabile della lunghezza delle righe del Dataset delle features
k: lunghezza delle combinazioni desiderata
lunghezza_massima: mi esce da questo metodo ricorsivo dopo che ha trovato almeno N_esperimenti combinazioni 
    dove N_esperimenti viene inserito dall'utente
current=[]: vettore vuoto che verrà aggiornato ogni qualvolta rientro ovvero il vettore ricorsivo che non viene 
    specificato all'esterno
combinazioni_trovate: serve per confrontarlo con lunghezza massima in modo tale che qunado arriva allo stesso numero il
    metodo ricorsivo si fermi
'''
def tutte_le_combinazioni(indici, k,lunghezza_massima, indici_correnti=[], combinazioni_trovate=0):
    # Se troviamo il numero desiderato di combinazioni, interrompi la ricorsione
    if combinazioni_trovate >= lunghezza_massima:
        return []

    # Mescola gli indici in modo casuale
    shuffle_array(indici)

    # Questa condizione verifica se la lunghezza desiderata delle combinazioni è quella voluta (p). Quando k è zero,
    # significa che abbiamo raggiunto la lunghezza desiderata della combinazione, quindi restituiamo la lista contenente
    # la combinazione corrente. (ricordiamo è la combinazione degli indici del DataFrame
    if k == 0:
        return [indici_correnti]

    combinazioni = []
    for i, indici_interni in enumerate(indici):
        # creo una nuova variabile con gli indici rimanenti ovvero scarto l'indice che considero alla posizione i
        remaining_indices = indici[i + 1:]
        # Incrementa il numero di combinazioni trovate
        combinazioni_trovate += len(combinazioni)
        # inserisco dentro combinations la combinazioni di indice quando k arriverà a 0
        combinazioni.extend(tutte_le_combinazioni(remaining_indices, k - 1, lunghezza_massima,indici_correnti + [indici_interni],combinazioni_trovate))

    # Limita il numero di combinazioni trovate al massimo desiderato
    if combinazioni_trovate > lunghezza_massima:
        combinazioni = combinazioni[:lunghezza_massima]

    return combinazioni

'''
questo metodo mi riordina in modo casuale gli indici che gli verranno passati
    '''
def shuffle_array(arr):
    n = len(arr)
    for i in range(n):
        # Generate a random index j such that i <= j < n
        j = np.random.randint(i, n)
        # Swap elements at indices i and j
        arr[i], arr[j] = arr[j], arr[i]
    return arr