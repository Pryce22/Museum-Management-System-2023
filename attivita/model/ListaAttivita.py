import pickle
import os


class ListaAttivita:

    def __init__(self):
        super(ListaAttivita, self).__init__()
        self.lista_attivita = []

    # legge dal pickle la lista delle attivitá salvate e le assegna al modello
    def get_lista_attivita(self):
        if os.path.isfile('attivita/data/lista_attivita_salvata.pickle'):
            with open('attivita/data/lista_attivita_salvata.pickle', 'rb') as f:
                self.lista_attivita = pickle.load(f)
        return self.lista_attivita

    # ritorna l'istanza dell'attivitá selezionata
    def get_attivita(self, attivita_selezionata):
        for attivita in self.lista_attivita:
            if attivita is attivita_selezionata:
                return attivita

    # ritorna l'attivitá di cui é stato fornito l'id
    def get_attivita_by_ID(self, ID_attivita):
        for attivita in self.lista_attivita:
            if attivita.ID_attivita is ID_attivita:
                return attivita

    # aggiunge un'attivitá alla lista (usato solo in fase di inizializzazione)
    def aggiungi_attivita(self, attivita):
        self.lista_attivita.append(attivita)
        return True
