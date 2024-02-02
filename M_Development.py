import numpy as np # import della libreria numpy 
from input import Input
import random

class Knn:
    '''
    La classe Knn implementa un classificatore K-Nearest Neighbors (KNN).
    Parametri:
        - k: Numero di vicini più prossimi da considerare durante la fase di predizione.
    Metodi:
        - __init__(self, k): Costruttore che inizializza l'istanza della classe con il parametro k.
        - training(self, X, Y): Metodo per addestrare il modello KNN con dati di addestramento.
        - predizione(self, X): Metodo per fare previsioni su nuovi dati basandosi sui vicini più prossimi.
        - distanza_euclidea(self, x_1, x_2): Metodo per calcolare la distanza euclidea tra due vettori.
'''
    def __init__(self):
        self.input = Input()

    def training(self, X, Y):
        self.X_train = X
        self.Y_train = Y
    
    def predizione(self, X):
        # Inizializza una lista vuota per contenere le previsioni
        hope = []
        # Per ogni elemento in X (i dati per i quali vogliamo fare previsioni)
        for i in X:
            # Calcola le distanze euclidee tra l'elemento i e tutti i punti di addestramento in X_train
            distanza = [self.distanza_euclidea(i, j) for j in self.X_train]
            # Ottieni il valore di k da input
            k = self.input.k
            # Ottieni gli indici ordinati delle distanze più basse (i k vicini più prossimi)
            k_ordinati = np.argsort(distanza)[:k]
            # Ottieni i target corrispondenti agli indici ordinati
            k_vicini = [self.Y_train[a] for a in k_ordinati]
            # Conta le occorrenze di ciascun target tra i k vicini
            conta_vicini = {}
            for conta in k_vicini:
                if conta in conta_vicini:
                    conta_vicini[conta] += 1 
                else:
                    conta_vicini[conta] = 1
            # Trova il target più frequente tra i k vicini
            massimo_valore = max(conta_vicini.values())
            chiavi_massime = [chiave for chiave, valore in conta_vicini.items() if valore == massimo_valore]
            chiave_random = random.choice(chiavi_massime)
            # Aggiungi il target più frequente alla lista di previsioni (hope)
            hope.append(chiave_random)
        # Restituisci la lista di previsioni
        return hope
    
    # Calcolo della distanza euclidea tramite una funzione
    def distanza_euclidea(self,x_1, x_2):
        '''
        La distanza si calcola come la radice della somma dei quadrati delle differenze 
        La funzione restitursce la distanza calcolata 
        '''
        # Il calcolo avviene tramite l'ausilio della libreria numpy
        dist = np.sqrt(np.sum((x_1-x_2)**2)) 
        return dist 

