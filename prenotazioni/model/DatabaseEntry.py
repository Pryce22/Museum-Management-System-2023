import datetime


class DataBaseEntry:

    def __init__(self, date, attivita, n_massimo):
        super(DataBaseEntry, self).__init__()
        self.attivita = attivita
        self.data = date
        self.matrice_clienti = [[] for _ in range(3)]
        self.n_massimo = n_massimo
        print(self.attivita.titolo)
        print(self.data)
        print(self.n_massimo)

    def get_numero_posti_prenotati(self):
        return len(self.matrice_clienti[0])  # Usiamo la lunghezza di una delle sottoliste

    def get_numero_massimo(self):
        return self.n_massimo

    def aggiungi_riga(self, utente_attivo_email, nome, cognome):
        riga = [utente_attivo_email, nome, cognome]
        if len(riga) == 3:
            for i in range(3):
                self.matrice_clienti[i].append(riga[i])
