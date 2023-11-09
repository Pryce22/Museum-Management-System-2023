from attivita import *
from prenotazioni.data import *
from prenotazioni.model.DatabasePrenotazioni import *
from attivita.model.ListaAttivita import *
import datetime
import pickle
import os.path


class ControlloreBackupEManutenzione:

    def __init__(self):
        super(ControlloreBackupEManutenzione, self).__init__()
        self.database = DatabasePrenotazioni()
        self.DatabasePrenotazioni = self.database.get_database_prenotazioni()
        self.lista = ListaAttivita()
        self.ListaAttivita = self.lista.get_lista_attivita()

    def aggiungi_nuove_prenotazioni(self):
        if len(self.DatabasePrenotazioni) == 0:
            self.database.aggiungi_data_prenotabile(
                datetime.date.today(),
                self.lista.get_attivita_by_ID(1),
                self.lista.get_attivita_by_ID(1).n_posti)
            print("Fatto")
        while len(self.DatabasePrenotazioni) > 0 and (self.database.return_last_date() < datetime.date.today() + datetime.timedelta(days=30)):
            if self.database.return_last_date() is not datetime.date.today():
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date() + datetime.timedelta(days=1),
                    self.lista.get_attivita_by_ID(1),
                    self.lista.get_attivita_by_ID(1).n_posti)
            if self.database.return_last_date().strftime("%w") == "2":
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(3),
                    self.lista.get_attivita_by_ID(3).n_posti
                )
            if self.database.return_last_date().strftime("%w") == "3":
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(5),
                    self.lista.get_attivita_by_ID(5).n_posti
                )
            if self.database.return_last_date().strftime("%w") == "4":
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(4),
                    self.lista.get_attivita_by_ID(4).n_posti
                )
            if (self.database.return_last_date().strftime("%w") == "6" or
                    self.database.return_last_date().strftime("%w") == "0"):
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(2),
                    self.lista.get_attivita_by_ID(2).n_posti
                )
