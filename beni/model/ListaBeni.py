

class ListaBeni:
    def __init__(self):
        super(ListaBeni, self).__init__()
        self.lista_beni = []

    def aggiungi_bene(self, bene):
        self.lista_beni.append(bene)

    def elimina_bene(self, bene_eliminare):
        for bene in self.lista_beni:
            if bene.id_bene == bene_eliminare.id_bene:
                self.lista_beni.remove(bene)
                return True
        return False

    def get_lista_beni(self):
        return self.lista_beni

    def get_bene_by_index(self, index):
        return self.lista_beni[index]