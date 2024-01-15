import numpy as np # import della libreria numpy 
from input import Input

class Knn:
    def __init__(self,k):
        self.k = k

    def training(self, X, Y):
        self.X_train = X
        self.Y_train = Y
    
    # Calcolo della distanza euclidea tramite una funzione
    def distanza_euclidea(self,x_1, x_2):
        '''
        La distanza si calcola come la radice della somma dei quadrati delle differenze 
        La funzione restitursce la distanza calcolata 
        '''
        # Il calcolo avviene tramite l'ausilio della libreria numpy
        dist = np.sqrt(np.sum((x_1-x_2)**2)) 
        return dist 

