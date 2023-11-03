class DataBaseEntry:

    def __init__(self, attivita, date, n_massimo):
        super(DataBaseEntry, self).__init__()
        self.attivita = attivita
        self.date = date
        self.matrice_clienti = [[] for _ in range(3)]
        self.n_massimo = n_massimo

    def get_numero_posti_prenotati(self):
        return len(self.matrice_clienti[0])  # Usiamo la lunghezza di una delle sottoliste

    def aggiungi_riga(self, utente_attivo_email, nome, cognome):
        riga = [utente_attivo_email, nome, cognome]
        if len(riga) == 3:
            for i in range(3):
                self.matrice_clienti[i].append(riga[i])


prova = DataBaseEntry("1", "20", 30)

prova.aggiungi_riga("Matteo@gmail.com", "Matteo", "Colletta")
prova.aggiungi_riga("Angjelo@gmail.com", "Angjelo", "Libosch")
prova.aggiungi_riga("Valério@gmail.com", "Valério", "Crocetti")

print(prova.matrice_clienti)

print(prova.get_numero_posti_prenotati())

