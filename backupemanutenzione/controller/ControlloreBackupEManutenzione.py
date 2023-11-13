from attivita import *
from prenotazioni.data import *
from utente.data import *
from beni.data import *
from informazioniecontatti.data import *
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
            if self.database.return_last_date().strftime("%w") == "6" or self.database.return_last_date().strftime("%w") == "0":
                self.database.aggiungi_data_prenotabile(
                    self.database.return_last_date(),
                    self.lista.get_attivita_by_ID(2),
                    self.lista.get_attivita_by_ID(2)
                )

    def elimina_prenotazioni_scadute(self):
        for prenotazione in self.DatabasePrenotazioni:
            if prenotazione.data < datetime.date.today():
                self.database.elimina_data_prenotabile(prenotazione)

    def copia_lista_utenti(self):
        with open("utente/data/lista_utenti_salvata.pickle", 'rb') as f:
            lista_utenti_backup = pickle.load(f)
        with open('backupemanutenzione/data/lista_utenti_backup.pickle', "wb") as g:
            pickle.dump(lista_utenti_backup, g)
            return lista_utenti_backup

    def copia_lista_beni(self):
        with open('beni/data/lista_beni_salvata.pickle', 'rb') as f:
            lista_beni_backup = pickle.load(f)
        with open('backupemanutenzione/data/lista_beni_backup.pickle', "wb") as g:
            pickle.dump(lista_beni_backup, g)
            return lista_beni_backup

    def copia_lista_prenotazioni(self):
        with open('prenotazioni/data/lista_prenotazioni_salvata.pickle', 'rb') as f:
            lista_prenotazioni_backup = pickle.load(f)
        with open('backupemanutenzione/data/lista_prenotazioni_backup.pickle', "wb") as g:
            pickle.dump(lista_prenotazioni_backup, g)
            return lista_prenotazioni_backup

    def copia_informazioni_e_contatti(self):
        informazioni_e_contatti_backup = []
        with open('informazioniecontatti/data/informazioni_salvate.pickle', 'rb') as f:
            informazioni_e_contatti_backup.append(pickle.load(f))
        with open('informazioniecontatti/data/contatti_salvati.pickle', 'rb') as h:
            informazioni_e_contatti_backup.append(pickle.load(h))
        with open('backupemanutenzione/data/informazioni_e_contatti_backup.pickle', "wb") as g:
            pickle.dump(informazioni_e_contatti_backup, g)
            return informazioni_e_contatti_backup

    def save_data(self):
        if os.path.isfile('backupemanutenzione/data/backup_completo.pickle'):
            with open('backupemanutenzione/data/backup_completo.pickle', 'wb') as f:
                dati_backup = [self.copia_lista_utenti(),
                               self.copia_lista_beni(),
                               self.copia_lista_prenotazioni(),
                               self.copia_informazioni_e_contatti()]
                pickle.dump(dati_backup, f)
