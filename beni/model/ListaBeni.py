import os
import pickle


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

    def cerca_bene_per_nome(self, nome):
        for b in self.get_lista_beni():
            if b.nome == nome:
                return b
        return None

    def aggiorna_bene(self, bene_vecchio, bene_aggiornato):
        self.elimina_bene(bene_vecchio)
        self.aggiungi_bene(bene_aggiornato)
        with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            pickle.dump(self.lista_beni, f)
        self.print_lista_beni()

    def get_lista_beni(self):
        if os.path.isfile('beni/data/lista_beni_salvata.pickle'):
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
                lista_beni_salvata = pickle.load(f)
            return lista_beni_salvata
        return self.lista_beni

    def print_lista_beni(self):
        for b in self.get_lista_beni():
            print("Nome: ", b.nome, "Immagine: ", b.immagine)



    def get_lista_nomi_beni(self):
        lista_nomi_beni = []
        if os.path.isfile('beni/data/lista_beni_salvata.pickle'):
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
                lista_beni_salvata = pickle.load(f)
                lista_beni_salvata = sorted(lista_beni_salvata, key=lambda x: x.id_bene)
                for bene in lista_beni_salvata:
                    lista_nomi_beni.append(bene.nome)
        return lista_nomi_beni
