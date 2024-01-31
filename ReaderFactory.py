from ReaderCSV import ReaderCSV

class ReaderFactory:

    @staticmethod
    def create_reader(filename):
      
        if filename.endswith('.csv'):
            return ReaderCSV()
        
