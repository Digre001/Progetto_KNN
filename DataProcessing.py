import pandas as pd

percorso_file = '/Desktop/progetto-programmazione/breast_cancer.xlsx'

dataset = pd.read_excel(percorso_file)  
print(dataset.head())

dataset['colonna_numerica'] = dataset['colonna_numerica'].fillna(dataset['colonna_numerica'].mean())

dataset = dataset.dropna(subset=['colonna_interessata'])

dataset['colonna_manca'] = dataset['colonna'].isnull()

X = dataset.drop('Class', axis=1) 
y = dataset['Class']  



