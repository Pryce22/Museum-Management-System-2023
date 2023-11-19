import os.path
import pickle

from prenotazioni.model.DatabaseEntry import *


class DatabasePrenotazioni:
    def __init__(self):
        super(DatabasePrenotazioni, self).__init__()
        self.database_prenotazioni = []

    # aggiunge una DatabaseEntry in funzione dei parametri forniti
    def aggiungi_data_prenotabile(self, date, attivita, num):
        new_database_entry = DataBaseEntry(date, attivita, num)
        self.database_prenotazioni.append(new_database_entry)
        self.save_data()

    # elimina una DatabaseEntry da DatabasePrenotazioni in funzione della data fornita
    def elimina_data_prenotabile(self, data):
        for database_entry in self.database_prenotazioni:
            if database_entry is data:
                self.database_prenotazioni.remove(database_entry)
                self.save_data()

    # visualizza i posti disponibili di una data attivitá
    def visualizza_posti_disponibili(self, attivita):
        for data_prenotabile in self.database_prenotazioni:
            if data_prenotabile.attivita is attivita:
                n_posti = data_prenotabile.n_massimo - data_prenotabile.get_numero_posti_prenotati
                if n_posti > 0:
                    return n_posti
                else:
                    return False

    # crea e ritorna una lista di prenotazioni in funzione dell'email dell'utente attivo
    def visualizza_lista_prenotazioni_per_email(self, email_utente):
        lista_prenotazioni_per_email = []
        for entry in self.get_database_prenotazioni():
            lista_email = entry.matrice_clienti[0]
            for email in lista_email:
                if email == email_utente:
                    index = lista_email.index(email)
                    lista_prenotazioni_per_email.append(entry.data.strftime("%d - %m -  %Y") +
                                                        "    " +
                                                        entry.matrice_clienti[1][index] +
                                                        "  " +
                                                        entry.matrice_clienti[2][index] +
                                                        "    " +
                                                        entry.attivita.titolo)
        return lista_prenotazioni_per_email

    # ritorna l'ultima data presente in DatabasePrenotazioni
    def return_last_date(self):
        database = self.get_database_prenotazioni()
        return database[-1].data

    # ritorna la lista delle DatabaseEntry presente in DatabasePrenotazioni leggendola dal pickle
    def get_database_prenotazioni(self):
        if os.path.isfile('prenotazioni/data/lista_prenotazioni_salvata.pickle'):
            with open('prenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
                self.database_prenotazioni = pickle.load(f)
        return self.database_prenotazioni

    # ritorna una lista di date in funzione dell'attivitá richiesta
    def get_date_per_attivita(self, attivita_selezionata):
        database = self.get_database_prenotazioni()
        lista_date_per_attivita = []
        for entry in database:
            if (entry.attivita.titolo == attivita_selezionata and
                    entry.get_numero_posti_prenotati() < entry.attivita.n_posti):
                lista_date_per_attivita.append(entry.data)
        return lista_date_per_attivita

    # salva i dati nel pickle
    def save_data(self):
        with open('prenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as f:
            pickle.dump(self.database_prenotazioni, f)
