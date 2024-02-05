import pandas as pd
import numpy as np

class Metriche:

    def __init__(self,y_test: pd.Series,previsioni: list,metriche_scelte: list):
        self.y_test=y_test
        self.previsioni=previsioni
        self.metriche_scelte = metriche_scelte



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

        # vado ad inizializzare le variabili che conterranno le metriche cosi calcolo solo quelle necessarie richieste
        # dall'utente lasciando le altre vuote e pasandole vuote
        Accuracy_rate = 0
        Error_rate = 0
        Sensitivity = 0
        Specificity = 0
        Geometric_mean = 0

        # Creo codizioni il quale mi dice se calcolare tale metriche o meno:
        if 1 in self.metriche_scelte:
            # Percentuale di predizioni corrette rispetto al totale delle predizioni
            Accuracy_rate = (vero_negativo + vero_positivo) / self.y_test.size

        if 2 in self.metriche_scelte:
            # Percentuale di predizioni errate rispetto al totale delle predizioni
            Error_rate = (falso_positivo + falso_negativo) / self.y_test.size

        if 3 in self.metriche_scelte:
            # Capacità del modello di predire correttamente i valori positivi
            Sensitivity = (vero_positivo) / (vero_positivo + falso_negativo)

        if 4 in self.metriche_scelte:
            # Capacità del modello di predire correttamente i valori negativi
            Specificity = (vero_negativo) / (vero_negativo + falso_positivo)

        if 5 in self.metriche_scelte:
            # Media che bilancia valori positivi e negativi
            Geometric_mean = np.sqrt((Sensitivity * Specificity))

        return Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean



    def salvare_metriche(self, Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean):
        # Apro il file Metriche.txt
        with open('Calcolo_Metriche.txt', 'w') as file:
            # Ci scrivo dentro le metriche calcolate
            file.write('Accuracy Rate: ' + str(Accuracy_rate) + '\n')
            file.write('Error Rate: ' + str(Error_rate) + '\n')
            file.write('Sensitivity: ' + str(Sensitivity) + '\n')
            file.write('Specificity: ' + str(Specificity) + '\n')
            file.write('Geometric Mean: ' + str(Geometric_mean) + '\n')

        # Chiudo il file Metriche.txt
        file.close()  # Chiudo il file Metriche.txt

    def plot_metriche(self):
        pass