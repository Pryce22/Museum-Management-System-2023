from beni.model.ListaBeni import *
import pickle
import os


class ControlloreListaBeni:
    def __init__(self):
        super(ControlloreListaBeni, self).__init__()
        self.model = ListaBeni()
        if os.path.isfile('beni/data/lista_beni_salvata.pickle'):
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
                lista_beni_salvata = pickle.load(f)
            self.model.lista_beni = lista_beni_salvata

            with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
                pickle.dump(self.model.lista_beni, f)

    def inserisci_bene(self, bene):
        self.model.aggiungi_bene(bene)
        with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_beni, f)

    def elimina_bene(self, bene):
        self.model.elimina_bene(bene)
        with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_beni, f)

    def cerca_bene_per_id(self,id_bene):
        for b in self.model.get_lista_beni():
            if b.id_bene == id_bene:
                return b
        return ""

    def cerca_bene_per_nome(self,nome):
        for b in self.model.get_lista_beni():
            if b.nome == nome:
                return b
        return ""

    #def filtra_per_stato(self, stato):
        #for b in self.model.get.lista_beni():

