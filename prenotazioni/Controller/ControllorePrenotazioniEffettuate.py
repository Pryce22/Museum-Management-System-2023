from prenotazioni.model.DatabasePrenotazioni import DatabasePrenotazioni


class ControllorePrenotazioniEffettuate:

    def __init__(self, utente_attivo):
        super(ControllorePrenotazioniEffettuate, self).__init__()
        self.utente_attivo = utente_attivo
        self.model = DatabasePrenotazioni()

    def visualizza_lista_prenotazioni_per_email(self):
        return self.model.visualizza_lista_prenotazioni_per_email(self.utente_attivo.email)
