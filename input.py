
class input:
    '''
    spiegazione della classe
    '''
    def __init__(self):
        '''
        Utiliziamo il costruttore della classe per inizializare i nostri valori di input:
        '''
        # Numero di vicini da utilizare nel Knn
        self.k=None
        # Scelta del modello di valutaozine
        self.Modello_valutazione=None
        #Dimensione del train size e di conseguenza del test size
        self.train_size=None
        # Se modello Leave-p-out Cross Validation e scelto allora decidere il numero di esperimenti 
        self.N_esperimenti=None
        # Metriche da valutare nel modello
        self.Metriche=None