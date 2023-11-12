from prenotazioni.model.DatabasePrenotazioni import DatabasePrenotazioni


class ControllorePrenotazioniEffettuate:

    def __init__(self):
        super(ControllorePrenotazioniEffettuate, self).__init__()
        self.model = DatabasePrenotazioni()

    def visualizza_lista_prenotazioni_per_email(self, utente_attivo):
        return self.model.visualizza_lista_prenotazioni_per_email(utente_attivo.email)
