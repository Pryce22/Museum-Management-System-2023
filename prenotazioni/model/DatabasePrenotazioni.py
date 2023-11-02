from prenotazioni.model.DatabaseEntry import *

class DatabasePrenotazioni:
    def __init__(self):
        super(DatabasePrenotazioni, self).__init__()
        self.database_prenotazioni = []

    def aggiungi_data_prenotabile(self, date, attivita, num):
        new_database_entry = DataBaseEntry(date, attivita, num)
        self.database_prenotazioni.append(new_database_entry)

    def visualizza_posti_disponibili(self, attivita):
        for data_prenotabile in self.database_prenotazioni:
            if data_prenotabile.attivita is attivita:
                n_posti = data_prenotabile.n_massimo - data_prenotabile.get_numero_posti_prenotati
                if n_posti > 0:
                    return n_posti
                else:
                    return False

    def visualizza_lista_prenotazioni_per_email(self, email_utente):
        lista_prenotazioni_email = [[], []]
        for prenotazione in self.database_prenotazioni:
            for cliente in prenotazione.lista_clienti:
                if cliente[0] is email_utente:
                    lista_prenotazioni_email.append(cliente[[1], [2]])
        return lista_prenotazioni_email
