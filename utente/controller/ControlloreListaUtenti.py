from utente.model.ListaUtenti import *
import pickle
import os


class ControlloreListaUtenti:
    def __init__(self):
        super(ControlloreListaUtenti, self).__init__()
        self.model = ListaUtenti()
        if os.path.isfile('utente/data/lista_utenti_salvata.pickle'):
            with open('utente/data/lista_utenti_salvata.pickle', 'rb') as f:
                lista_clienti_salvata = pickle.load(f)
            self.model.lista_utenti = lista_clienti_salvata

            with open('utente/data/lista_utenti_salvata.pickle', 'wb') as f:
                pickle.dump(self.model.lista_utenti, f)

        print("\nlista_utenti:")
        for u in self.model.get_lista_utenti():
            print(u.email, u.password, sep="; ")

    def inserisci_utente(self, utente):
        self.model.aggiungi_utente(utente)
        with open('utente/data/lista_utenti_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_utenti, f)

    def elimina_utente(self, utente):
        self.model.elimina_utente(utente)
        with open('utente/data/lista_utenti_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_utenti, f)

    def controlla_email(self, email_in):
        for u in self.model.get_lista_utenti():
            if u.email == email_in:
                return False
        return True

    def trova_utente(self, email_in):
        for u in self.model.get_lista_utenti():
            if u.email == email_in:
                return u
        return ""

