import pandas as pd

'''
    Classe per la divisione dei dati per l'addestramento e la valutazione dei modelli HoldOut e Leave_P_Out.

    Il metdodo Split_Holdout che serve per splittare i dati che gli vengono formiti secondo una percentuale 
    definita in input dall'utente

    Il metodo Split_leave_p_out invece suddivide i dati per vari esperimenti sempre a seconda dell'utente e calcola 
    tutte le combinazioni possibili da fare con p gruppi di test inseriti dall'utente, il quale sono diversi 
    per ogni esperimento andando a vedere l'andamento di ogni esperimento come vaòutazione finale e 
    anche la media di tutte le valutazioni fatte

    '''

class Split_data:
    '''
        costruttore:
        features: sono i dati che verranno usati per addestrare e testare il modello
        target: sono i dati che utilizzeremo per verificare il training e per verificare il test
        train_size: percentuale di dati che verranno utilizzati per il metodo di holdout
        N_esperimenti: numero di esperimenti da fare per il leavePout corss validation
        '''
    def __init__(self, features: pd.DataFrame, target: pd.Series, train_size: int, N_esperimenti: int, p: int):
        self.features = features  # DataFrame contenente le caratteristiche dei dati
        self.target = target  # Serie contenente i valori target associati alle caratteristiche
        self.train_size = train_size  # Percentuale di dati da utilizzare per la divisione dei dati mediante holdout
        self.N_esperimenti = N_esperimenti  # Numero di esperimenti da eseguire per leave-P-out
        self.p = p  # Numero di gruppi di dati di test da utilizzare per ogni esperimento nella leave-P-out


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
combinazioni_trovate: serve per confrontarlo con lunghezza massima in modo tale che qunado arriva allo stesso numero il
    metodo ricorsivo si fermi
'''
def tutte_le_combinazioni(indici, k, lunghezza_massima, combinazioni_trovate=0):
    # Questa condizione verifica se la lunghezza desiderata delle combinazioni è quella voluta (p). Quando k è zero,
    # significa che abbiamo raggiunto la lunghezza desiderata della combinazione,
    if k == 0:
        return [[]] # Contiene una lista vuota cosi da interrompere la ricorsione

    # Se non ci sono più indici disponibili, interrompe la ricorsione è un controllo per interrompere la ricorsione
    # se si esagera nella ricerca di tutte le combinazioni possibili con pochi dati
    if len(indici) == 0:
        return []

    # Se troviamo il numero desiderato di combinazioni, interrompi la ricorsione
    if combinazioni_trovate >= lunghezza_massima:
        return []

    # Ricorsivamente, generiamo tutte le combinazioni di lunghezza k, sia includendo che non includendo il primo elemento da indici
    combinazioni = tutte_le_combinazioni(indici[1:], k, lunghezza_massima, combinazioni_trovate)
    combinazioni.extend([ [indici[0]] + comb for comb in tutte_le_combinazioni(indici[1:], k - 1, lunghezza_massima, combinazioni_trovate + len(combinazioni))])

    return combinazioni

