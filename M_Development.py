import numpy as np # import della libreria numpy 

# Calcolo della distanza euclidea tramite una funzione
def distanza_euclidea(x_1, x_2):
    '''
    La distanza si calcola come la radice della somma dei quadrati delle differenze 
    La funzione restitursce la distanza calcolata 
    '''
    # Il calcolo avviene tramite l'ausilio della libreria numpy
    dist = np.sqrt(np.sum((x_1-x_2)**2)) 
    return dist 