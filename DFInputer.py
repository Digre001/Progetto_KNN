from ReaderFactory import readerfactory

class dfInputer:
    '''
    Classe dataframeimputer che ha il compito di riempire i valori mancanti in un dataframe 
    '''
    def __init__(self, df):
        self.df = df

    def handle_missing_values(self, method):
        '''
        Metodo per riempire i valori mancanti di un dataframe con la moda della colonna corripondente
        '''
        if method == 'drop':
            self.df.dropna(inplace=True)
        elif method == 'mean':
            self.df.fillna(self.df.mean(), inplace=True)
        elif method == 'median':
            self.df.fillna(self.df.median(), inplace=True)
        elif method == 'mode':
            for col in self.df.columns:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
        return self.df

