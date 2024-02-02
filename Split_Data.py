import pandas as pd


class Split_data:

    def __init__(self, features: pd.DataFrame, target: pd.Series, train_size: int, N_esperimenti: int, k):
        self.features = features
        self.target = target
        self.train_size = train_size
        self.N_esperimenti=N_esperimenti



    def Split_Holdout(self, features: pd.DataFrame, target: pd.Series, train_size: int):

        # Prendo i dati per il training secondo una percentuale specificata in input
        X_train = features.sample(frac=train_size)

        # Prendo i dati per il test. Sono tutti i dati che non sono stati presi per il training
        x_test = features.drop(X_train.index)

        Y_train = target.drop(x_test.index)  # Mi salvo le y di train corrispondenti alle x di train

        y_test = target.drop(X_train.index)  # Mi salvo le y di test corrispondenti alle x di test

        return X_train, Y_train, x_test, y_test

    pass