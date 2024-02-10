from Evalutation.Evaluation import Evaluation
from INPUT.input import Input
from Preprocessing.F_and_L import DataSplitter

# Crea un'istanza della classe Input
input_instance = Input()

# Crea un'istanza della classe DataSplitter e passa il nome del file CSV
preprocessing = DataSplitter('breast_cancer.csv')

# Ottieni l'input dall'utente
input_taken = input_instance.user_input()

# Estrai le informazioni necessarie dall'input utente
N_esperimenti = input_taken['N_esperimenti']
method = input_taken['Gestione']
train_size = input_taken['train_size']
Modello_valutazione = input_taken['Modello_valutazione']
p = input_taken['p']
Metriche = input_taken['Metriche']
k = input_taken['k']

# Preprocessa i dati utilizzando il metodo specificato
features, labels = preprocessing.process_data(method)

# Crea un'istanza della classe Evaluation con le caratteristiche e le etichette pre-elaborate
Eval = Evaluation(features, labels, train_size, N_esperimenti, p, Metriche, k)

# Valuta il modello utilizzando Holdout o Leave-p-out a seconda della scelta dell'utente
if Modello_valutazione == "h":
    Eval.valutazione_holdout()
else:
    Eval.valutazione_leave_p_out()

