class DfInputer:
    '''
    Classe DfInputer che si occupa di gestire i valori mancanti in un dataframe.
    '''

    def __init__(self, df):
        '''
        Costruttore della classe. Inizializza l'istanza con un dataframe.
        '''
        self.df = df

    def handle_missing_values(self, method):
        '''
        Metodo per gestire i valori mancanti nel dataframe utilizzando il metodo specificato.
        Args:
            method (str): Il metodo da utilizzare per riempire i valori mancanti. Può essere 'drop', 'mean', 'median' o 'mode'.
        Returns:
            pandas.DataFrame: Il dataframe con i valori mancanti gestiti secondo il metodo specificato.
        '''
        if method == 'drop':
            # Rimuove le righe con valori mancanti
            self.df.dropna(inplace=True)
        elif method == 'mean':
            # Riempie i valori mancanti con la media della colonna corrispondente
            self.df.fillna(self.df.mean(), inplace=True)
        elif method == 'median':
            # Riempie i valori mancanti con la mediana della colonna corrispondente
            self.df.fillna(self.df.median(), inplace=True)
        elif method == 'mode':
            # Riempie i valori mancanti con la moda della colonna corrispondente
            for col in self.df.columns:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
        # Restituisce il dataframe con i valori mancanti gestiti
        return self.df

