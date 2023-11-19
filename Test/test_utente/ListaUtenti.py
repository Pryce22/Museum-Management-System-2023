import os
import pickle
from PyQt5.QtWidgets import QMessageBox


class ListaUtenti:
    def __init__(self):
        super(ListaUtenti, self).__init__()
        self.lista_utenti = []

    def aggiungi_utente(self, utente):
        self.lista_utenti.append(utente)

    def elimina_utente(self, email_eliminare):
        if os.path.isfile('lista_utenti_salvata.pickle'):
            with open('lista_utenti_salvata.pickle', 'rb') as f:
                lista_clienti_salvata = pickle.load(f)
            self.lista_utenti = lista_clienti_salvata
        self.print_lista_utenti()
        for utente in self.lista_utenti:
            if utente.email == email_eliminare:
                self.lista_utenti.remove(utente)
                return True

    def get_lista_utenti(self):
        return self.lista_utenti

    def get_utente_by_index(self, index):
        return self.lista_utenti[index]

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Errore")
        msg.setText(text)
        x = msg.exec_()

    def print_lista_utenti(self):
        for utente in self.lista_utenti:
            print("Email: ", utente.email, "Password: ", utente.password)
