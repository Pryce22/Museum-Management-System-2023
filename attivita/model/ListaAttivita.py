import pickle


class ListaAttivita:

    def __init__(self):
        super(ListaAttivita, self).__init__()
        self.lista_attivita = []

    def get_lista_attivita(self):
        with open('attivita/data/lista_attivita_salvata.pickle', 'rb') as f:
            self.lista_attivita = pickle.load(f)
        return self.lista_attivita

    def get_attivita(self, attivita_selezionata):
        for attivita in self.lista_attivita:
            if attivita is attivita_selezionata:
                return attivita

    def get_attivita_by_ID(self, ID_attivita):
        for attivita in self.lista_attivita:
            if attivita.ID_attivita is ID_attivita:
                return attivita

    def aggiungi_attivita(self, attivita):
        self.lista_attivita.append(attivita)
        return True

