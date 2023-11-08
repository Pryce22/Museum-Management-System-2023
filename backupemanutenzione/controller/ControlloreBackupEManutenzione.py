from prenotazioni.model.DatabasePrenotazioni import *
from attivita.model.ListaAttivita import *
import datetime
class ControlloreBackupEManutenzione:

    def __init__(self, database):
        super(ControlloreBackupEManutenzione, self).__init__()
        self.DatabasePrenotazioni = database

    def aggiungi_nuove_prenotazioni (date):
        if DatabasePrenotazioni.database_prenotazioni.len() is 0:
            DatabasePrenotazioni.aggiungi_data_prenotabile(
                datetime.date.today(),
                ListaAttivita.get_attivita_by_ID(1),
                ListaAttivita.get_attivita_by_ID(1).n_posti)
        while DatabasePrenotazioni[-1].date is not datetime.date.today()+datetime.timedelta(days=30):
            if DatabasePrenotazioni[-1].date is not datetime.date.today():
                DatabasePrenotazioni.aggiungi_data_prenotabile(
                    datetime.date.today()+datetime.timedelta(days=1),
                    ListaAttivita.get_attivita_by_ID(1),
                    ListaAttivita.get_attivita_by_ID(1).n_posti)
            if DatabasePrenotazioni[-1].date.strftime("%w") is 1:
                DatabasePrenotazioni.aggiungi_data_prenotabile(
                    datetime.date.today()
                )