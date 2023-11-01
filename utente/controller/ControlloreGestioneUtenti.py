from utente.model.ListaUtenti import *
import pickle
import os


class ControlloreGestioneUtenti:
    def __init__(self):
        super(ControlloreGestioneUtenti, self).__init__()
        self.model = ListaUtenti()
        if os.path.isfile('utente/data/lista_utenti_salvata.pickle'):
            with open('utente/data/lista_utenti_salvata.pickle', 'rb') as f:
                lista_clienti_salvata = pickle.load(f)
            self.model.lista_utenti = lista_clienti_salvata

        with open('utente/data/lista_utenti_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_utenti, f)

        print("\nlista_utenti:")
        for u in self.model.get_lista_utenti():
            if u.is_direttore:
                tipo = "Direttore"
            elif u.is_dipendente:
                tipo = "Dipendente"
            else:
                tipo = "Cliente"
            print(u.email, u.password, tipo, sep="; ")

    def inserisci_utente(self, utente):
        self.model.aggiungi_utente(utente)
        with open('utente/data/lista_utenti_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_utenti, f)

    def elimina_utente(self, utente):
        if self.model.elimina_utente(utente):
            with open('utente/data/lista_utenti_salvata.pickle', 'wb') as f:
                pickle.dump(self.model.lista_utenti, f)
            sys.exit()

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

    def aggiorna_utente(self, email_vecchia, email_nuova, password_nuova):
        u = self.trova_utente(email_vecchia)
        u.email = email_nuova
        u.password = password_nuova
        with open('utente/data/lista_utenti_salvata.pickle', 'wb') as f:
            pickle.dump(self.model.lista_utenti, f)
