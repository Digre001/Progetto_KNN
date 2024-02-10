from Preprocessing.readerCSV import ReaderCSV
# classe factory per creare oggetti reader in base all'estensione del file 
class Readerfactory:

    @staticmethod # utilizzo del metodo statico 
    def create_reader(filename):# Definisce un metodo statico chiamato create_reader che accetta un parametro chiamato filename
        '''
        questo metodo crea e restituisce un oggeto reader in base all'estensione del file.
        Se l'estensione del file .csv, crea un ReaderCSV
        Se l'estensione del file non è supportata, solleva un 'eccezione ValueError
        '''
      
        if filename.endswith('.csv'):
            return ReaderCSV()
        else:
            raise ValueError("invalid file type")
        