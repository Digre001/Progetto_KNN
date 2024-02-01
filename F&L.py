from DFInputer import dfInputer
from ReaderFactory import readerfactory

class DataSplitter:
    def __init__(self, df, label_column_name):
        # Inizializza gli attributi della classe con i valori forniti
        self.df = df
        self.label_column_name = label_column_name

    # Metodo per suddividere il dataframe in features (caratteristiche) e label
    def split(self):
        # Estrai le features dal dataframe escludendo la colonna delle label
        features = self.df.drop(self.label_column_name, axis=1)
        # Estrai le label dal dataframe utilizzando solo la colonna delle label
        labels = self.df[self.label_column_name]
        # Restituisci le features e le label come risultato della suddivisione
        return features, labels


