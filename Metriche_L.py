import pandas as pd

class Metriche:
    
    def __init__(self,y_test: pd.Series,previsioni: list):
        self.y_test=y_test
        self.previsioni=previsioni

    def calcolo_metriche(self):
        # calcolo la confusion Matrix:

        # Calcolo il valore True Negative della confusion matrix
        true_negative = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y == pred and pred == 2))

        # Calcolo il valore True Positive della confusion matrix
        true_positive = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y == pred and pred == 4))

        # Calcolo il valore False Positive della confusion matrix
        false_positive = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y != pred and pred == 2))

        # Calcolo il valore False Negative della confusion matrix
        false_negative = sum(1 for y, pred in zip(self.y_test, self.previsioni) if (y != pred and pred == 4))

    def salvare_metriche(self):
        pass

    def plot_metriche(self):
        pass