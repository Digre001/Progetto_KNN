from DFInputer import dfInputer
from ReaderFactory import readerfactory

class DataSplitter:
    def __init__(self, df, label_column_name):
        self.df = df
        self.label_column_name = label_column_name
 
    def split(self):
        features = self.df.drop(self.label_column_name, axis=1)
        labels = self.df[self.label_column_name]
        return features, labels


