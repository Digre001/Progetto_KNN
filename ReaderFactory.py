from ReaderCSV import ReaderCSV
# classe factori per creare oggetti reader in base all'estensione del file 
class ReaderFactory:

    @staticmethod # utilizo del metodo statico 
    def create_reader(filename):
        '''
        questo metodo crea e restituisce un oggeto reade in base all'estensione del file.
        Se l'estensione del file .csv, crea un ReaderCSV
        Se l'estensione del file non è supportata, solleva un 'eccezione Valie Error
        '''
      
        if filename.endswith('.csv'):
            return ReaderCSV()
        #aggiungere un valureerror?
        
