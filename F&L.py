from DFImputer import dfImputer
from ReaderFactory import readerfactory

class DataSplitter:
    def __init__(self, df, label_column_name):
        self.df = df
        self.label_column_name = label_column_name
'''
dataset['colonna_numerica'] = dataset['colonna_numerica'].fillna(dataset['colonna_numerica'].mean())

dataset = dataset.dropna(subset=['colonna_interessata'])

dataset['colonna_manca'] = dataset['colonna'].isnull()

X = dataset.drop('Class', axis=1) 
y = dataset['Class']  

'''

