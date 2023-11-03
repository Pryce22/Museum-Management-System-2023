import os
import pickle

from beni.model.Bene import *
class ListaBeni:
    def __init__(self):
        super(ListaBeni, self).__init__()
        self.lista_beni = []

    def aggiungi_bene(self, bene):
        if bene not in self.lista_beni:
            self.lista_beni.append(bene)
            return True
        else:
            return False

    def elimina_bene(self, bene_eliminare):
        for bene in self.lista_beni:
            if bene.id_bene == bene_eliminare.id_bene:
                self.lista_beni.remove(bene)
                return True
        return False

    def get_lista_beni(self):
        if os.path.isfile('beni/data/lista_beni_salvata.pickle'):
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
                lista_beni_salvata = pickle.load(f)
            return lista_beni_salvata
        return self.lista_beni

    def get_bene_by_index(self, index):
        return self.lista_beni[index]