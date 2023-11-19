from attivita.model.ListaAttivita import *
from attivita.data import *
import os
import pickle


class ControlloreListaAttivita:

    # inizializzazione con lettura del file pickle
    def __init__(self):
        super(ControlloreListaAttivita).__init__()
        self.model = ListaAttivita()
        if os.path.isfile('attivita/data/lista_attivita_salvata.pickle'):
            with open('attivita/data/lista_attivita_salvata.pickle', 'rb') as f:
                lista_attivita_salvata = pickle.load(f)
            self.model.lista_attivita = lista_attivita_salvata

        with open('attivita/data/lista_attivita_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_attivita, f)

    # chiama la funzione del modello e ritorna la lista delle attivitá
    def get_lista_attivita(self):
        return self.model.get_lista_attivita()

    # aggiunge un'attivitá alla lista (viene usato solo in caso di perdita di dati)
    def aggiungi_attivita(self, attivita):
        if self.model.aggiungi_attivita(attivita):
            with open('attivita/data/lista_attivita_salvata.pickle', 'wb') as f:
                pickle.dump(self.model.lista_attivita, f)

    # restituisce l'attivitá di cui é stato fornito il titolo
    def get_attivita(self, titolo_in):
        for a in self.model.get_lista_attivita():
            if titolo_in == a.titolo:
                return a
