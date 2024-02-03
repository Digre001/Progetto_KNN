from DFInputer import dfInputer
from ReaderFactory import readerfactory

class DataSplitter:
    def __init__(self, file_name):
        # Inizializza gli attributi della classe con i valori forniti
        self.file_name = file_name

    # Metodo per suddividere il dataframe in features (caratteristiche) e label
    def split(self, df, label_column_name):
        # Estrai le features dal dataframe escludendo la colonna delle label
        features = df.drop(label_column_name, axis=1)
        # Estrai le label dal dataframe utilizzando solo la colonna delle label
        labels = df[label_column_name]
        # Restituisci le features e le label come risultato della suddivisione
        return features, labels
    
    def process_data(self):
        # richiamo della metodo create_reader della classe readerfactory
        reader = readerfactory.create_reader(self.file_name)
        # Utilizza reader per analizzare il file e ottenere un dataframe
        df = reader.parse(self.file_name)
        # Crea un'istanza di dfInputer con il dataframe ottenuto e utilizza il metodo specificato per gestire i valori mancanti
        df_ready = dfInputer(df).handle_missing_values("mean")  # Puoi scegliere tra drop, mean, median, mode
        # Ottiene il nome dell'ultima colonna del dataframe
        nome = df_ready.columns[-1]
        # Chiama il metodo split per suddividere il dataframe in features e labels utilizzando il nome ottenuto come colonna delle label
        return self.split(df_ready, nome)

# Aggiunte le seguenti righe alla fine del codice
a = DataSplitter('test.csv')
features, labels = a.process_data()
print("Features:\n", features)
print("Labels:\n", labels)

