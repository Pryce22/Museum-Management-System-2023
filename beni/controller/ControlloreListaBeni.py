from beni.model.ListaBeni import *
import pickle
import os


class ControlloreListaBeni:
    def __init__(self):
        super(ControlloreListaBeni, self).__init__()
        self.model = ListaBeni()
        if os.path.isfile('beni/data/lista_beni_salvata.pickle') and os.path.getsize(
                'beni/data/lista_beni_salvata.pickle') > 0:
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
                lista_beni_salvata = pickle.load(f)
                if not self.model.lista_beni:  # Verifica se la lista è vuota
                    self.model.lista_beni = lista_beni_salvata

    def inserisci_bene(self, bene):
        if self.model.aggiungi_bene(bene):
            with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
                pickle.dump(self.model.lista_beni, f)

    def elimina_bene(self, bene):
        self.model.elimina_bene(bene)
        with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_beni, f)

    def cerca_bene_per_id(self, id_bene):
        for b in self.model.get_lista_beni():
            if b.id_bene == id_bene:
                return b
        return None

    def cerca_bene_per_nome(self, nome):
        for b in self.model.get_lista_beni():
            if b.nome == nome:
                return b
        return None

    def controlla_nome(self, nome):
        for b in self.model.get_lista_beni():
            if b.nome == nome:
                return False
            else:
                return True

    def crea_id_bene(self):
        id_bene = len(self.model.lista_beni) + 1
        return id_bene

    def ottieni_url_immagine_bene(self,nome):
        bene = self.cerca_bene_per_nome(nome)
        if bene:
            return bene.immagine
        return None


    def ottieni_beni_da_file(self):
        try:
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as file:
                beni = pickle.load(file)
                return beni
        except (FileNotFoundError, EOFError):
            return []

    #def filtra_per_stato(self, stato):
        #for b in self.model.get.lista_beni():

