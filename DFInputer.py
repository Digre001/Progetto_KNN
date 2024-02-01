from ReaderFactory import readerfactory

class dfInputer:
    '''
    Classe dataframeimputer che ha il compito di riempire i valori mancanti in un dataframe 
    '''
    def __init__(self, df):
        self.df = df

    def impute_missing_values(self, df):
        '''
        Metodo per riempire i valori mancanti di un dataframe con la moda della colonna corripondente
        '''
        
        for col in df.columns:
            if df[col].isnull().any():
                mode_value = df[col].mode()[0] 
                df[col].fillna(mode_value, inplace=True)

        return df

