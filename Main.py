from Evaluation import Evaluation
from input import Input 
from F_and_L import DataSplitter


if __name__ == '__main__':
    # Create instances of the Input and Preprocessing classes
    input= Input()
    preprocessing = DataSplitter('test.csv')

    # Ask the user for the evaluation method and metrics to use
    input_presi = input.user_input()
    N_esperimenti = input_presi['N_esperimenti']
    method = input_presi['Gestione']
    # Split the dataset into features and target label
    features, labels = preprocessing.process_data(method)
    
    # Ask the user for the percentage of data to use for training and the number of neighbors to consider
    train_size = input_presi['train_size']
    Modello_valutazione = input_presi['Modello_valutazione']
    p = input_presi['p']
    Metriche = input_presi['Metriche']
    k= input_presi['k']

    #  Create an instance of the Evaluation class to evaluate the model's performance
    Eval = Evaluation(features, labels, train_size, N_esperimenti, p, Metriche, k)

    if Modello_valutazione  == "h":
        Eval.valutazione_holdout()
    else:
        Eval.valutazione_leave_p_out()