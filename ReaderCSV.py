import pandas as pd
from ReaderFactory import Reader

class ReaderCSV(Reader):

    def parse(self, filename):
        
        df = pd.read_csv(filename)
        return df
    
