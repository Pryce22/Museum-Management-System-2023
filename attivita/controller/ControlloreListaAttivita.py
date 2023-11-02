from attivita.model.ListaAttivita import *
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
            print(lista_attivita_salvata)

        with open('attivita/data/lista_attivita_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_attivita, f)

    def get_lista_attivita(self):
        with open('attivita/data/lista_attivita_salvata.pickle', 'rb') as f:
            print(pickle.load(f))
            return pickle.load(f)


attivita_prova = ControlloreListaAttivita()
attivita_prova.get_lista_attivita()
