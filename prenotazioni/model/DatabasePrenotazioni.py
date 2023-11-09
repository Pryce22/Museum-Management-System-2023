import os.path
import pickle

from prenotazioni.model.DatabaseEntry import *
import datetime


class DatabasePrenotazioni:
    def __init__(self):
        super(DatabasePrenotazioni, self).__init__()
        self.database_prenotazioni = []

    def aggiungi_data_prenotabile(self, date, attivita, num):
        new_database_entry = DataBaseEntry(date, attivita, num)
        self.database_prenotazioni.append(new_database_entry)
        with open('prenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as f:
            pickle.dump(self.database_prenotazioni, f)
        print('data aggiunta')

    def elimina_data_prenotabile(self, data):
        for database_entry in self.database_prenotazioni:
            if database_entry.data is data:
                self.database_prenotazioni.remove(database_entry)
                with open('prenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as f:
                    pickle.dump(self.database_prenotazioni, f)

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
                if cliente.matrice_clienti[0] is email_utente:
                    lista_prenotazioni_email.append(cliente.matrice_clienti[[1], [2]])
        return lista_prenotazioni_email

    def return_last_date(self):
        database = self.get_database_prenotazioni()
        return database[-1].data

    def get_database_prenotazioni(self):
        if os.path.isfile('prenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('prenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.database_prenotazioni = pickle.load(f)
        return self.database_prenotazioni


'''def visualizza_date_prenotazioni(self, attivita):
    for prenotazione in self.database_prenotazioni:
        if prenotazione.attivita is attivita and self.visualizza_posti_disponibili(attivita):'''

