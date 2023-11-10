from prenotazioni.model.DatabasePrenotazioni import *


class ControlloreInserisciPrenotazione:

    def __init__(self):
        super(ControlloreInserisciPrenotazione, self).__init__()
        self.model = DatabasePrenotazioni()

    def get_data_prenotazione_per_attivita(self, attivita_selezionata):
        for data_prenotabile in self.model.get_database_prenotazioni():
            if data_prenotabile.attivita is attivita_selezionata and data_prenotabile.get_numero_posti_prenotati:
                return data_prenotabile.data


