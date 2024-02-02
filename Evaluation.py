# Importo le librerie necessarie
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Evaluation:
    def __init__(self, features: pd.DataFrame, target: pd.Series, train_size: int, N_esperimenti: int, k,
                 metriche_scelte: list):
        self.features = features
        self.target = target
        self.train_size = train_size
        self.N_esperimenti = N_esperimenti
        self.metriche_scelte = metriche_scelte
        self.k = k

    pass

