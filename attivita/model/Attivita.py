class Attivita:

    def __init__(self, descrizione, giorno_della_settimana, ID_attivita, n_posti, orario, prezzo, titolo):
        super(Attivita, self).__init__()
        self.descrizione = descrizione
        self.giorno_della_settimana = giorno_della_settimana
        self.ID_attivita = ID_attivita
        self.n_posti = n_posti
        self.orario = orario
        self.prezzo = prezzo
        self.titolo = titolo
