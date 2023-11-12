from attivita.model.ListaAttivita import *
from attivita.data import *
import os
import pickle


class ControlloreListaAttivita:

    def __init__(self):
        super(ControlloreListaAttivita).__init__()
        self.model = ListaAttivita()
        if os.path.isfile('attivita/data/lista_attivita_salvata.pickle'):
            with open('attivita/data/lista_attivita_salvata.pickle', 'rb') as f:
                lista_attivita_salvata = pickle.load(f)
            self.model.lista_attivita = lista_attivita_salvata

        with open('attivita/data/lista_attivita_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_attivita, f)

    def get_lista_attivita(self):
        return self.model.get_lista_attivita()

    def aggiungi_attivita(self, attivita):
        if self.model.aggiungi_attivita(attivita):
            with open('attivita/data/lista_attivita_salvata.pickle', 'wb') as f:
                pickle.dump(self.model.lista_attivita, f)

    def get_attivita(self, titolo_in):
        for a in self.model.get_lista_attivita():
            if titolo_in == a.titolo:
                return a
