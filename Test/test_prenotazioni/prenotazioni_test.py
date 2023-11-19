import unittest
from datetime import datetime
from biglietto.controller.ControlloreBiglietto import ControlloreBiglietto
from prenotazioni.model.DatabasePrenotazioni import DatabasePrenotazioni
from prenotazioni.Controller import ControlloreInserisciPrenotazione  # Replace with your actual module name


class TestControlloreInserisciPrenotazione(unittest.TestCase):

    def setUp(self):
        # Create instances of the classes needed for testing
        self.controller_inserisci = ControlloreInserisciPrenotazione.ControlloreInserisciPrenotazione()
        self.controller_biglietto = ControlloreBiglietto()
        self.database_prenotazioni = DatabasePrenotazioni().get_database_prenotazioni()

    def test_get_data_prenotazione_per_attivita(self):
        # testa il metodo per ottenere le date per una specfica attivita
        attivita = "Visita senza guida"
        result = self.controller_inserisci.get_data_prenotazione_per_attivita(attivita)
        print(result)
        self.assertIsInstance(result, list)

    def test_get_database_prenotazioni(self):
        # testa il metodo per ottenere il database delle prenotazioni
        result = self.controller_inserisci.get_database_prenotazioni()
        self.assertIsInstance(result, list)

    def test_get_posti_disponibili_per_data(self):
        # testa il metodo per ottenere i posti disponibili per una data specifica
        date = datetime.today()
        result = self.controller_inserisci.get_posti_disponibili_per_data(date)
        self.assertIsInstance(result, int)

    def test_inserisci_prenotazione(self):
        # Assegna dei valori di prova alle variabili da passare alla funzione
        attivita = "Visita senza guida"
        data = datetime.today()
        nome = "Nome"
        cognome = "Cognome"
        email = "nome.cognome@example.com"

        # Esegui il test
        self.controller_inserisci.inserisci_prenotazione(attivita, data, nome, cognome, email)

        self.assertIsInstance(len(self.database_prenotazioni), int)


if __name__ == '__main__':
    unittest.main()
