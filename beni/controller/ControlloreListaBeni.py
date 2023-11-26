from beni.model.ListaBeni import *
from beni.model.Bene import *
import pickle
import os
import sys


class ControlloreListaBeni:
    def __init__(self):
        super(ControlloreListaBeni, self).__init__()
        self.model = ListaBeni()
        if os.path.isfile('beni/data/lista_beni_salvata.pickle') and os.path.getsize('beni/data/lista_beni_salvata.pickle') > 0:
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
                lista_beni_salvata = pickle.load(f)
                if not self.model.lista_beni:
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

        return True

    def get_lista_nomi_beni(self):
        return self.model.get_lista_nomi_beni()

    def get_lista_beni(self):
        return self.model.get_lista_beni()

    def aggiorna_bene(self, nome_vecchio, nome, immagine, area, descrizione, stato, stato_area,id_bene, data_di_aggiunta):
        bene_aggiornato = Bene(nome,immagine,area, descrizione,stato,stato_area,id_bene,data_di_aggiunta)
        bene = self.cerca_bene_per_nome(nome_vecchio)
        self.model.aggiorna_bene(bene, bene_aggiornato)
        #self.inserisci_bene(bene)
        #self.elimina_bene(bene_vecchio)
        #with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            #pickle.dump(self.model.lista_beni, f)

    def get_lista_nomi_da_id_o_nome(self,nome_o_id):
        beni_corrispondenti = []

        for bene in sorted(self.get_lista_beni(), key=lambda x: (not x.stato_area and not x.stato, x.id_bene)):
            nome_bene = bene.nome.lower()
            id_bene = str(bene.id_bene).lower()

            if nome_o_id in nome_bene or nome_o_id in id_bene:
                beni_corrispondenti.append(bene.nome)
        return beni_corrispondenti

    def visualizza_lista_beni_per_stato(self, stato):
        beni_disponibili = []
        for bene in sorted(self.get_lista_beni(), key=lambda x: (not x.stato_area and not x.stato, x.id_bene)):
            if (bene.stato and bene.stato_area) == stato:
                beni_disponibili.append(bene.nome)
        return beni_disponibili

    def get_lista_nomi_per_area(self, area_selezionata):
        if area_selezionata.lower() == "tutte":
            #lista_beni = self.get_lista_beni()
            #sorted(lista_beni, key=lambda x: x.id_bene)
            return [bene.nome for bene in sorted(self.get_lista_beni(), key=lambda x: (not x.stato_area and not x.stato, x.id_bene))]
        beni_per_area = []
        for bene in sorted(self.get_lista_beni(), key=lambda x: (not x.stato_area and not x.stato, x.id_bene)):
            if bene.area == area_selezionata:
                beni_per_area.append(bene.nome)
        return beni_per_area

    def crea_id_bene(self):
        if len(self.get_lista_beni()) == 0:
            id_bene_nuovo = 1
        else:
            ultimo_bene = self.get_lista_beni()[-1]
            id_bene_nuovo = ultimo_bene.id_bene + 1
        return id_bene_nuovo

    def ottieni_path_immagine_bene(self,nome):
        bene = self.cerca_bene_per_nome(nome)
        if bene:
            return bene.immagine
        return None

    def salva_aree_e_loro_stati(self):
        aree_stato = {
            "Area Geologica": True,
            "Area Zoologica": True,
            "Area Paleontologica": True,
            "Area esposizione temporanee": True,
            "Science room": True
        }
        print(aree_stato)
        #os.makedirs(os.path.dirname('beni/data/aree_stato.pickle'), exist_ok=True)
        if os.path.isfile("beni/data/aree_stato.pickle"):
            with open("beni/data/aree_stato.pickle", 'wb') as file:
                pickle.dump(aree_stato, file)
            with open("beni/data/aree_stato.pickle", 'rb') as f:
                lista_aree = pickle.load(f)
                print(lista_aree)

    def carica_stato_aree(self):
        with open("beni/data/aree_stato.pickle", 'rb') as file:
            aree_stato = pickle.load(file)
            return aree_stato

    def cambia_disponibilita_aree(self,Geologica,Zoologica,Paleontologica,Esp_Temp,Science):
        aree_stato = self.carica_stato_aree()
        if Geologica:
            aree_stato["Area Geologica"] = True
        else:
            aree_stato["Area Geologica"] = False
        if Zoologica:
            aree_stato["Area Zoologica"] = True
        else:
            aree_stato["Area Zoologica"] = False
        if Paleontologica:
            aree_stato["Area Paleontologica"] = True
        else:
            aree_stato["Area Paleontologica"] = False
        if Esp_Temp:
            aree_stato["Area esposizione temporanee"] = True
        else:
            aree_stato["Area esposizione temporanee"] = False
        if Science:
            aree_stato["Science room"] = True
        else:
            aree_stato["Science room"] = False
        with open("beni/data/aree_stato.pickle", 'wb') as file:
            pickle.dump(aree_stato, file)
        self.cambia_disponibilita_aree_lista_beni()

    def stato_area(self, area_bene):
        with open("beni/data/aree_stato.pickle", 'rb') as file:
            aree_stato = pickle.load(file)
            for area, stato in aree_stato.items():
                if area_bene == area:
                    return stato

    def cambia_disponibilita_aree_lista_beni(self):
        with open("beni/data/aree_stato.pickle", 'rb') as file:
            aree_stato = pickle.load(file)
            lista_beni = self.get_lista_beni()
            for bene in lista_beni:
                for area, stato in aree_stato.items():
                    if bene.area == area:
                        bene.stato_area = stato
        with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            pickle.dump(lista_beni, f)

    def ottieni_beni_da_file(self):
        try:
            with open('beni/data/lista_beni_salvata.pickle', 'rb') as file:
                beni = pickle.load(file)
                return beni
        except (FileNotFoundError, EOFError):
            return []

    def get_cartella_immagini(self):
        file = os.path.abspath(__file__)
        application_path = os.path.dirname(os.path.dirname(file))
        images_folder = os.path.join(application_path, 'immagini beni')
        lista_immagini = [os.path.join(images_folder, file) for file in os.listdir(images_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        print(lista_immagini)
        return lista_immagini

    def sostituisci_immagini(self):
        lista_immagini = self.get_cartella_immagini()
        lista_beni = self.get_lista_beni()
        for immagine in lista_immagini:
            directory_immagine = os.path.split(immagine)[-1]

            for bene in lista_beni:
                directory_bene = os.path.split(bene.immagine)[-1]

                if directory_bene == directory_immagine:
                    bene.immagine = immagine
        with open('beni/data/lista_beni_salvata.pickle', 'wb') as f:
            pickle.dump(lista_beni, f)
