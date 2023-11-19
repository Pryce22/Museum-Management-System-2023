from prenotazioni.model.DatabasePrenotazioni import DatabasePrenotazioni


class ControllorePrenotazioniEffettuate:

    def __init__(self):
        super(ControllorePrenotazioniEffettuate, self).__init__()
        self.model = DatabasePrenotazioni()

    # ritorna la lista delle prenotazioni effettuate da un singolo utente
    def visualizza_lista_prenotazioni_per_email(self, utente_attivo):
        return self.model.visualizza_lista_prenotazioni_per_email(utente_attivo.email)

    # elimina la prenotazione selezionata dall'utente e salva il databse aggiornato
    def elimina_prenotazione(self, dati_prenotazione, utente_attivo):
        dati = dati_prenotazione.split("    ")
        for entry in self.model.get_database_prenotazioni():
            if entry.data.strftime("%d - %m -  %Y") == dati[0]:
                lista_email = entry.matrice_clienti[0]
                for email in lista_email:
                    if email == utente_attivo.email:
                        index = lista_email.index(email)
                        if (entry.matrice_clienti[1][index] == dati[1].split("  ")[0] and
                                entry.matrice_clienti[2][index] == dati[1].split("  ")[1] and
                                entry.attivita.titolo == dati[2]):
                            for i in range(3):
                                del entry.matrice_clienti[i][index]
                                self.model.save_data()

