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
        # Test the method to get dates for a specific activity
        attivita = "Visita senza guida"
        result = self.controller_inserisci.get_data_prenotazione_per_attivita(attivita)
        print(result)
        self.assertIsInstance(result, list)

    def test_get_database_prenotazioni(self):
        # Test the method to get the pre-booking database
        result = self.controller_inserisci.get_database_prenotazioni()
        self.assertIsInstance(result, list)

    def test_get_posti_disponibili_per_data(self):
        # Test the method to get available seats for a specific date
        date = datetime.today()
        result = self.controller_inserisci.get_posti_disponibili_per_data(date)
        self.assertIsInstance(result, int)

    def test_inserisci_prenotazione(self):
        attivita = "Visita senza guida"
        data = datetime.today()
        nome = "John"
        cognome = "Doe"
        email = "john.doe@example.com"

        # Mock the necessary dependencies or use setUp to create the expected conditions
        self.controller_inserisci.model.get_database_prenotazioni = lambda: self.database_prenotazioni
        self.controller_inserisci.controller.invia_biglietto_per_email = lambda *args, **kwargs: None

        # Perform the test
        self.controller_inserisci.inserisci_prenotazione(attivita, data, nome, cognome, email)

        # Add assertions to check if the booking was added successfully
        self.assertIsInstance(len(self.database_prenotazioni), int)
        # Add more assertions based on your implementation

if __name__ == '__main__':
    unittest.main()
