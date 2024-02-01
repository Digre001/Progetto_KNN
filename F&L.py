from DFInputer import dfInputer
from ReaderFactory import readerfactory
from input import Input

class DataSplitter:
    def __init__(self, file_name):
        # Inizializza gli attributi della classe con i valori forniti
        self.file_name = file_name
        self.input = Input()

    # Metodo per suddividere il dataframe in features (caratteristiche) e label
    def split(self, df, label_column_name):
        # Estrai le features dal dataframe escludendo la colonna delle label
        features = df.drop(label_column_name, axis=1)
        # Estrai le label dal dataframe utilizzando solo la colonna delle label
        labels = df[label_column_name]
        # Restituisci le features e le label come risultato della suddivisione
        return features, labels
    
    def process_data(self):
        reader = readerfactory.create_reader(self.file_name)
        df = reader.parse(self.file_name)
        method = self.input. # nome della variabile da chiamare che ora non ricordo 
        df_ready = dfInputer(df).handle_missing_values(method)
        nome = df_ready.columns[-1]
        return self.split(df_ready, nome)
