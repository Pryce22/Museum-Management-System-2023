from Test.test_utente.ListaUtenti import *
import pickle
import os
import unittest
from utente.model.Utente import Utente


class ControlloreGestioneUtenti:
    def __init__(self):
        super(ControlloreGestioneUtenti, self).__init__()
        self.model = ListaUtenti()
        self.pickle_path_test = 'lista_utenti_salvata.pickle'

        if os.path.isfile(self.pickle_path_test):
            with open(self.pickle_path_test, 'rb') as f:
                lista_clienti_salvata = pickle.load(f)
            self.model.lista_utenti = lista_clienti_salvata

        with open(self.pickle_path_test, 'wb') as f:
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
        with open(self.pickle_path_test, 'wb') as f:
            pickle.dump(self.model.lista_utenti, f)

    def elimina_utente(self, email_in):
        if self.model.elimina_utente(email_in):
            with open(self.pickle_path_test, 'wb') as f:
                pickle.dump(self.model.lista_utenti, f)
            return True

    def controlla_email(self, email_in):
        #if '@' in email_in and '.' in email_in:
            for u in self.model.get_lista_utenti():
                if u.email == email_in:
                    return False
            return True
        #else:
            #return False

    def trova_utente(self, email_in):
        for u in self.model.get_lista_utenti():
            print("u.email: ", u.email)
            if u.email == email_in:
                return u.email
        return ""

    def aggiorna_utente(self, email_vecchia, email_nuova, password_nuova):
        u = self.trova_utente(email_vecchia)
        u.email = email_nuova
        u.password = password_nuova
        with open(self.pickle_path_test, 'wb') as f:
            pickle.dump(self.model.lista_utenti, f)

    def inserisci_dipendente(self, email_in):
        if email_in == "":
            self.show_popup(0, "Compila tutti i campi per il signup!")
        else:
            if self.controlla_email(email_in):
                self.inserisci_utente(Utente(email_in, email_in, True, False))
                self.show_popup(1, "Account registrato!")
                return True
            else:
                self.show_popup(0, "Email non valida!")

    def show_popup(self, n, text):
        msg = QMessageBox()
        if n == 0:
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Errore")
            msg.setText(text)
        elif n == 1:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Errore")
            msg.setText(text)
        x = msg.exec_()


class TestControlloreGestioneUtenti(unittest.TestCase):
    def setUp(self):
        # Questo metodo viene chiamato prima di ogni test
        self.controllore = ControlloreGestioneUtenti()

    def test_inserisci_elimina_cliente(self):
        email_cliente = "cliente@example.com"
        password_cliente = "password"

        # Inserisci un cliente
        cliente = Utente(email_cliente, password_cliente, False, False)
        self.controllore.inserisci_utente(cliente)

        # Verifica che il cliente sia stato inserito correttamente
        self.assertFalse(self.controllore.controlla_email(email_cliente))
        self.assertEqual(self.controllore.trova_utente(email_cliente), cliente)

        # Elimina il cliente
        self.assertTrue(self.controllore.elimina_utente(email_cliente))

        # Verifica che il cliente sia stato eliminato correttamente
        self.assertTrue(self.controllore.controlla_email(email_cliente))
        self.assertEqual(self.controllore.trova_utente(email_cliente), "")


if __name__ == '__main__':
    unittest.main()
