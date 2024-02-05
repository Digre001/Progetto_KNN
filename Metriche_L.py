import pandas as pd
import numpy as np

class Metriche:

    def __init__(self,y_test: pd.Series,previsioni: list):
        self.y_test=y_test
        self.previsioni=previsioni




    '''
            con questo metodo si vuole calcolare prima i valori della confuzion matrix secondo le rispettive norme del:
            vero positivo, vero negativo, falso positivo ed infine falso negativo; per andare poi, a calcolare, 
            attraverso questi vaolri, le metriche richieste che saranno poi specificate dall'utente. 

            le metriche calcolate saranno:

           - Accuracy Rate
           - Error Rate
           - Sensitivity
           - SpeciCicity
           - Geometric Mean
           '''
    def calcolo_matrix_metriche(self):
        # calcolo la confusion Matrix:

        # Calcolo il valore True Negative della confusion matrix
        vero_negativo = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y == pred and pred == 2))
        # (zip mi serve per combinare gli elementi y_test e conforntarli con le previsioni e lìif quindi mi fa il conteggio
        # in questo caso solo se y e pred coincidono con 2, quindi con 1 for y, ecc.. if ecc.. sto dicendo che mi genere un
        # 1 ogni qualvolta la condizione if è soddisfatta e poi con sum sommo tutti questi uni).

        # Calcolo il valore True Positive della confusion matrix
        vero_positivo = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y == pred and pred == 4))

        # Calcolo il valore False Positive della confusion matrix
        falso_positivo = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y != pred and pred == 2))

        # Calcolo il valore False Negative della confusion matrix
        falso_negativo = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y != pred and pred == 4))

        '''Calcolo effettivo delle metriche richieste mediante i valori della confusion matrix, precedentemente calcolati
                '''
        # Percentuale di predizioni corrette rispetto al totale delle predizioni
        Accuracy_rate = (vero_negativo + vero_positivo) / self.y_test.size

        # Percentuale di predizioni errate rispetto al totale delle predizioni
        Error_rate = (falso_positivo + falso_negativo) / self.y_test.size

        # Capacità del modello di predire correttamente i valori positivi
        Sensitivity = (vero_positivo) / (vero_positivo + falso_negativo)

        # Capacità del modello di predire correttamente i valori negativi
        Specificity = (vero_negativo) / (vero_negativo + falso_positivo)

        # Media che bilancia valori positivi e negativi
        Geometric_mean = np.sqrt((Sensitivity * Specificity))

        return Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean



    def salvare_metriche(self):
        pass

    def plot_metriche(self):
        pass