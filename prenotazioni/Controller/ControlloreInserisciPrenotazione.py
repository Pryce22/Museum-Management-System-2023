from prenotazioni.model.DatabasePrenotazioni import *


class ControlloreInserisciPrenotazione:

    def __init__(self):
        super(ControlloreInserisciPrenotazione, self).__init__()
        self.model = DatabasePrenotazioni()

    def get_data_prenotazione_per_attivita(self, attivita_selezionata):
        lista_date = self.model.get_date_per_attivita(attivita_selezionata)
        print(lista_date)
        return lista_date

    def get_database_prenotazioni(self):
        return self.model.get_database_prenotazioni()

    def get_posti_disponibili_per_data(self, data):
        for entry in self.model.get_database_prenotazioni():
            if entry.data == data:
                return entry.n_massimo - entry.get_numero_posti_prenotati()

    def inserisci_prenotazione(self, attivita_selezionata, data, nome, cognome, email):
        database = self.model.get_database_prenotazioni()
        for entry in database:
            if entry.data.strftime("%d - %m -  %Y") == data and entry.attivita.titolo == attivita_selezionata:
                entry.aggiungi_riga(email, nome, cognome)
                self.model.save_data()
