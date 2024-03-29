from Preprocessing.DFInputer import DfInputer
from Preprocessing.ReaderFactory import Readerfactory

class DataSplitter:
    def __init__(self, file_name):
        # Inizializza gli attributi della classe con i valori forniti
        self.file_name = file_name

    # Metodo per suddividere il dataframe in features (caratteristiche) e label
    def __split(self, df, label_column_name):
        # Estrai le features dal dataframe escludendo la colonna delle label
        features = df.drop(label_column_name, axis=1)
        # Estrai le label dal dataframe utilizzando solo la colonna delle label
        labels = df[label_column_name]
        # Restituisci le features e le label come risultato della suddivisione
        return self.__standardizazzione(features), labels
    
    def __standardizazzione(self, features):
        # standardizazzione delle sole features
        for column in features.columns:
            features[column] = (features[column] - features[column].mean()) / features[column].std()
        return features
    
    def process_data(self, method):
        # richiamo della metodo create_readr della classe readerfactory
        reader = Readerfactory.create_reader(self.file_name)
        # Utilizza reader per analizzare il file e ottenere un dataframe
        df = reader.parse(self.file_name)
        # Crea un'istanza di dfInputer con il dataframe ottenuto e utilizza il metodo specificato per gestire i valori mancanti
        df_ready = DfInputer(df).handle_missing_values(method)
        # Ottiene il nome dell'ultima colonna del dataframe
        nome = df_ready.columns[-1]
        # Chiama il metodo split per suddividere il dataframe in features e labels utilizzando il nome ottenuto come colonna delle label
        return self.__split(df_ready, nome)
