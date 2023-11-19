import pickle
import unittest
from utente.model.Utente import Utente
from test.test_utente.ControlloreGestioneUtenti import ControlloreGestioneUtenti


class TestControlloreGestioneUtenti(unittest.TestCase):
    def setUp(self):
        # Questo metodo viene chiamato prima di ogni test
        self.controllore = ControlloreGestioneUtenti()

    def test_inserisci_elimina_cliente(self):
        email_cliente = "cliente@example.com"
        password_cliente = "password"

        # Inserisci un cliente
        if self.controllore.controlla_email(email_cliente):
            self.controllore.inserisci_utente(Utente(email_cliente, password_cliente, False, False))

        # Verifica che il cliente sia stato inserito correttamente
        self.assertEqual(self.controllore.trova_utente(email_cliente), email_cliente)

        # Elimina il cliente
        self.assertTrue(self.controllore.elimina_utente(email_cliente))

        # Verifica che il cliente sia stato eliminato correttamente
        self.assertEqual(self.controllore.trova_utente(email_cliente), "")


if __name__ == '__main__':
    unittest.main()
