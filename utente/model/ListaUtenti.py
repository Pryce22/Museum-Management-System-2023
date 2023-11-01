class ListaUtenti:
    def __init__(self):
        super(ListaUtenti, self).__init__()
        self.lista_utenti = []

    def aggiungi_utente(self, utente):
        self.lista_utenti.append(utente)

    def elimina_utente(self, utente_eliminare):
        for utente in self.lista_utenti:
            if utente.email == utente_eliminare.email:
                self.lista_utenti.remove(utente)
                return True
        return False

    def get_lista_utenti(self):
        return self.lista_utenti

    def get_utente_by_index(self, index):
        return self.lista_utenti[index]
