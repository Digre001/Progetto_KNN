import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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




    '''
       In questo metodo le metriche calcolate precedentemente vengono salvate su un file questo file
       si chiamerà "Metriche.txt

      Le variabili da passare a questo metodo sono quelle calcolate con il metodo calcolo_matrix_metriche
      e sono:

       Accuracy_rate: ovvero la percentuale di predizioni corrette rispetto al totale delle predizioni

       Error_rate: ovvero la percentuale di predizioni errate rispetto al totale delle predizioni

       Sensitivity: la capacità del modello di predirre correttamente i valori positivi

       Specificity: la capacità del modello di predirre correttamente i valori negativi

       Geometric_mean: la media che bilancia valori positivi e negativi
       '''
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



    '''
        In questo metodo vengono plottate le metriche per ogni esperimento dell'holdout perhcè ho solo un 
        valore nella metrica e verrà rapressentato tramite un grafico a barre.
        La rappresentazione avviene tramite la libreria matplotlib.

        sarà usato anche per prottare la media delle metriche nel modello leave_p_out
        '''
    def plot_metriche_holdout_e_media(self, Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean):
        # questo vettore viene utilizzato per rappresentare le etichette sul grafico
        etichette = ['Accuracy Rate', 'Error Rate', 'Sensitivity', 'Specificity', 'Geometric Mean']

        # questo vettore invece viene utilizzato per rappresentare i valori del grafico corrispondenti alle etichette
        valori = [Accuracy_rate, Error_rate, Sensitivity, Specificity, Geometric_mean]

        # questo vettore viene utilizzato per determinare i colori delle varie barre del grafico
        colori = ['blue', 'green', 'red', 'yellow', 'orange']

        # Imposto la dimensione del grafico
        plt.figure(figsize=(10, 5))

        plt.bar(etichette, valori,
                color=colori)  # Creo il grafico a barre. In x metto le etichette, in y metto i valori
        plt.xlabel("Metriche")  # Imposto l'etichetta dell'asse x
        plt.ylabel("Valori")  # Imposto l'etichetta dell'asse y
        plt.title("Grafico delle metriche")  # Imposto il titolo del grafico
        plt.show()  # Mostro il grafico




        '''
            In questo metodo vengono plottate le metriche per ogni esperimento del leave_p_out dato che gli esperimenti qui 
            saranno maggiori andremo a plottare non più le metriche con il grafico a barre ma ogni valore della metrica 
            cporisponderà ad un punto ovvero un esperimento cosi da vedere l'andamento delle metriche nei diversi esperimenti
            ovvero cambiano i dati dei test e trianing.

            verrà plottato anche il grafico a barre rispetto alla media delle metriche.

            La rappresentazione avviene tramite la libreria matplotlib.
            '''
        def plot_metriche_leave_p_out(self, Accuracy_rate: list, Error_rate: list, Sensitivity: list, Specificity: list,
                                      Geometric_mean: list):
            # Imposto la dimensione del grafico
            plt.figure(figsize=(10, 5))

            # Con le seguenti operazioni plotto le metriche richieste
            if 1 in self.metriche_scelte:
                plt.plot(Accuracy_rate, marker='o', linestyle='solid', linewidth=2, markersize=5, color='blue',
                         label='Accuracy Rate')

            if 2 in self.metriche_scelte:
                plt.plot(Error_rate, marker='o', linestyle='solid', linewidth=2, markersize=5, color='green',
                         label='Error Rate')

            if 3 in self.metriche_scelte:
                plt.plot(Sensitivity, marker='o', linestyle='solid', linewidth=2, markersize=5, color='red',
                         label='Sensitivity')

            if 4 in self.metriche_scelte:
                plt.plot(Specificity, marker='o', linestyle='solid', linewidth=2, markersize=5, color='yellow',
                         label='Specificity')

            if 5 in self.metriche_scelte:
                plt.plot(Geometric_mean, marker='o', linestyle='solid', linewidth=2, markersize=5, color='orange',
                         label='Geometric Mean')

            plt.legend(loc='upper right')  # Imposto la posizione legenda nel grafico
            plt.xlabel("Esperimenti")  # Imposto il nome dell'etichetta dell'asse x
            plt.ylabel("Valori")  # Imposto il nome dell'etichetta dell'asse y
            plt.title("Andamento delle metriche")  # Imposto il titolo del grafico
            plt.tight_layout()  # Ottimizza la disposizione dei sottopannelli nel grafico per evitare sovrapposizioni

            # Mostro il grafico
            plt.show()