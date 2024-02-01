
class selection:

    def __init__(self):
        pass

    def Selzione_metriche(self):
        '''
        Questa funzione permette all'utente di selezionare le metriche di valutazione.
        Restituisce una lista di metriche associate ai numeri inseriti dall'utente.
        '''
        print("Selezionare le metriche da valutare:\n1. Accuracy Rate\n2. Error Rate\n3. Sensitivity\n4. Specificity\n5. Geometric Mean")
        # Dizionario che associa i numeri alle metriche
        associazione = {
            1: 'Accuracy Rate',
            2: 'Error Rate',
            3: 'Sensitivity',
            4: 'Specificity',
            5: 'Geometric Mean'
        }
        while True:
            scelta = input("Inserire il numero corrispondete alla metrica (separare con una virgola in caso di scelta multipla): ")
            # Converte i numeri da stringa a intero e li mette in una lista
            lista_scelta = [int(numero) for numero in scelta.split(',')]
            # Verifica che i numeri siano compresi tra 1 e 5
            if all (0 < numero < 6 for numero in lista_scelta):
                metriche_selezionate = [associazione[numero] for numero in lista_scelta]
                break
            else:
                print("Errore: inserire un valore valido. Riprova.")
        return metriche_selezionate
    
    def Gestione_valori_mancanti(self):
        '''
        Questa funzione permette all'utente di selezionare la gestione dei valori mancanti.
        Restituisce una stringa che rappresenta la scelta dell'utente.
        '''
        print("Selezionare la gestione dei valori mancanti:\n1. Eliminazione\n2. Media\n3. Mediana\n4. Moda")
        # Dizionario che associa i numeri alle metriche
        associazione = {
            1: 'Eliminazione',
            2: 'Media',
            3: 'Mediana',
            4: 'Moda'
        }
        while True:
            scelta = int(input("Inserire il numero corrispondete alla gestione dei valori mancanti: "))
            # Verifica che i numeri siano compresi tra 1 e 4
            if 0 < scelta < 5:
                gestione_selezionata = associazione[scelta]
                break
            else:
                print("Errore: inserire un valore valido. Riprova.")
        return gestione_selezionata