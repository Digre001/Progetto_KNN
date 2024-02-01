import pandas as pd

class readerCSV:
    '''
    Implementazione della classe ReaderCSV.
    il suo unico compito è leggere file CSV, trasformali in Dataframe e restituirli pronti per il preprocessing.
    '''

    def parse(self, filename):
        '''
        Implementaizone concreda del metodo "prase" che riceve in input il nume del file CSV da leggere 
        e restituisce un Dataframe pronto per il pre-processing
        '''
        
        df = pd.read_csv(filename)
        return df
    
