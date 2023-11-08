from attivita import *
from prenotazioni.model.DatabasePrenotazioni import *
from attivita.model.ListaAttivita import *
import datetime


class ControlloreBackupEManutenzione:

    def __init__(self):
        super(ControlloreBackupEManutenzione, self).__init__()
        self.database = DatabasePrenotazioni()
        self.DatabasePrenotazioni = self.database.database_prenotazioni
        self.lista = ListaAttivita()
        self.ListaAttivita = self.lista.get_lista_attivita()

    def aggiungi_nuove_prenotazioni(self):
        if len(self.DatabasePrenotazioni) == 0:
            self.database.aggiungi_data_prenotabile(
                datetime.date.today(),
                self.lista.get_attivita_by_ID(1),
                self.lista.get_attivita_by_ID(1).n_posti)
        while len(self.DatabasePrenotazioni) > 0 and self.DatabasePrenotazioni[-1].date is not datetime.date.today() + datetime.timedelta(days=30):
            if self.DatabasePrenotazioni[-1].date is not datetime.date.today():
                self.database.aggiungi_data_prenotabile(
                    datetime.date.today() + datetime.timedelta(days=1),
                    self.lista.get_attivita_by_ID(1),
                    self.lista.get_attivita_by_ID(1).n_posti)
            if self.DatabasePrenotazioni[-1].data.strftime("%w") == 2:
                self.database.aggiungi_data_prenotabile(
                    self.DatabasePrenotazioni.return_last_date(),
                    self.lista.get_attivita_by_ID(3),
                    self.lista.get_attivita_by_ID(3).n_posti
                )
            if self.DatabasePrenotazioni[-1].data.strftime("%w") == 3:
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(5),
                    self.lista.get_attivita_by_ID(5).n_posti
                )
            if self.DatabasePrenotazioni[-1].data.strftime("%w") == 4:
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(4),
                    self.lista.get_attivita_by_ID(4).n_posti
                )
            if (self.DatabasePrenotazioni[-1].data.strftime("%w") == 6 or
                    self.DatabasePrenotazioni[-1].data.strftime("%w") == 0):
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(2),
                    self.lista.get_attivita_by_ID(2).n_posti
                )


prova = ControlloreBackupEManutenzione()

prova.aggiungi_nuove_prenotazioni()
print(prova.DatabasePrenotazioni)
