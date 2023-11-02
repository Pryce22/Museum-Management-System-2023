class DataBaseEntry:

    def __init__(self, attivita, date, n_massimo):
        super(DataBaseEntry, self).__init__()
        self.attivita = attivita
        self.date = date
        self.matrice_clienti = [[] for _ in range(3)]
        self.n_massimo = n_massimo

    def get_numero_posti_prenotati(self):
        return len(self.matrice_clienti[0])  # Usiamo la lunghezza di una delle sottoliste

    def aggiungi_riga(self, riga):
        if len(riga) == 3:
            for i in range(3):
                self.matrice_clienti[i].append(riga[i])


database = DataBaseEntry("ciao", "peni", 5)
database.matrice_clienti.append(["ciao", "peni", 6])
print(database.matrice_clienti)