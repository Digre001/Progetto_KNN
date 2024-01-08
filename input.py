
class Input:
    '''
    spiegazione della classe
    '''
    def __init__(self):
        '''
        Utiliziamo il costruttore della classe per inizializare i nostri valori di input:
        '''
        # Numero di vicini da utilizare nel Knn
        self.k = None
        # Scelta del modello di valutaozine
        self.Modello_valutazione = None
        #Dimensione del train size e di conseguenza del test size
        self.train_size = None
        # Se modello Leave-p-out Cross Validation e scelto allora decidere il numero di esperimenti 
        self.N_esperimenti = None
        # Metriche da valutare nel modello
        self.Metriche = None

    def user_input(self):
        '''
        Questa funzione chiede all'utente di inserire gli input inizializzati in precedenza tramite diverse metodologie:
        - k: Richiede un valore intero per k utilizzando il comando int input.
        - Modello_valutazione: Richiede l'inserimento di un modello di valutazione, eliminando gli spazi e convertendo le lettere maiuscole in minuscole.
        - train_size: Richiede un valore float compreso tra 0 e 1 per la percentuale del dataset utilizzata per il training.
        - N_esperimenti: Richiede un valore intero in input.
        - Metriche: Richiama una funzione per la selezione delle metriche.
        '''
        self.k = int(input("Inserire il numero di vicini da studiare nel Knn (k): "))
        uscita=False
        while not uscita:
            #Utilizza un ciclo while per garantire il corretto inserimento del modello di valutazione 
            self.Modello_valutazione=input("Seleziona il modello di valutazione (Holdout o Leave-p-out Cross Validation): ").lower().strip()
            if self.Modello_valutazione == "holdout":
                while True:
                        #Utilizza un secondo ciclo while per garantire il corretto inserimento della variabile train_size compresa tra 0 e 1
                        self.train_size = float(input("Inserire e del dataset utilizata per il training (es. 0.7 per 70%): "))
                        if ( 0 <= self.train_size <= 1 ):
                            #uscita dal primo while tramite variabile uscita e dal secondo tramite break
                            uscita=True
                            break
                        else:
                            print("Errore: inserire un valore valido compreso tra 0 e 1. Riprova.")
            elif self.Modello_valutazione == "leave-p-outcrossvalidation":
                self.N_esperimenti=int(input("Inserire il numero di esperimenti (K): "))
                uscita= True
            else:
                print ("Errore: il modello di valutazione non è adatto (Holdout o Leave-p-out Cross Validation). Riprovare")
        # Richiama la funzione Metriche per la selezione delle metriche (da implementare, considerando una scelta multipla)
        self.Metriche=self.Selzione_metriche() 
        return {
            'k': self.k,
            'Modello_valutazione': self.Modello_valutazione,
            'train_size': self.train_size,
            'N_esperimenti': self.N_esperimenti,
            'Metriche': self.Metriche
        }
    
    def Selzione_metriche(self):
        print("Selezionare le metriche da valutare:\n1. Accuracy Rate\n2. Error Rate\n3. Sensitivity\n4. Specificity\n5. Geometric Mean")
        associazione = {
            1: 'Accuracy Rate',
            2: 'Error Rate',
            3: 'Sensitivity',
            4: 'Specificity',
            5: 'Geometric Mean'
        }
        while True:
            scelta = input("Inserire il numero corrispondete alla metrica (separare con una virgola in caso di scelta multipla): ")
            lista_scelta = [int(numero) for numero in scelta.split(',')]
            if all (0 < numero < 6 for numero in lista_scelta):
                metriche_selezionate = [associazione[numero] for numero in lista_scelta]
                break
            else:
                print("Errore: inserire un valore valido. Riprova.")
        return metriche_selezionate


            

if __name__ == "__main__":
    x=Input()
    x.user_input()
    print (f"{x.k} {x.Modello_valutazione}{x.train_size}{x.Metriche}")
    
