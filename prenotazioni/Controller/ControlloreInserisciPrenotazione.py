from biglietto.controller.ControlloreBiglietto import *
from prenotazioni.model.DatabasePrenotazioni import *


class ControlloreInserisciPrenotazione:

    def __init__(self):
        super(ControlloreInserisciPrenotazione, self).__init__()
        self.model = DatabasePrenotazioni()
        self.controller = ControlloreBiglietto()

    # ritorna una lista di date in funzione dell'attivitá selezionata
    def get_data_prenotazione_per_attivita(self, attivita_selezionata):
        lista_date = self.model.get_date_per_attivita(attivita_selezionata)
        print(lista_date)
        return lista_date

    # ritorna la lista di DatabaseEntry corrente
    def get_database_prenotazioni(self):
        return self.model.get_database_prenotazioni()

    # visualizza i posti disponibili per una certa data prenotabile
    def visualizza_posti_disponibili(self, data):
        for entry in self.model.get_database_prenotazioni():
            if entry.data == data:
                return entry.n_massimo - entry.get_numero_posti_prenotati()

    # inserisce una prenotazione nel DatabasePrenotazioni in funzione dei dati forniti e
    # invia un biglietto per e-mail dell'utente con il pdf del biglietto
    def inserisci_prenotazione(self, attivita_selezionata, data, nome, cognome, email):
        database = self.model.get_database_prenotazioni()
        self.controller.invia_biglietto_per_email(email, data, attivita_selezionata, nome, cognome)
        for entry in database:
            if entry.data.strftime("%d - %m -  %Y") == data and entry.attivita.titolo == attivita_selezionata:
                entry.aggiungi_riga(email, nome, cognome)
                print(entry.matrice_clienti[0][0])

                self.model.save_data()
