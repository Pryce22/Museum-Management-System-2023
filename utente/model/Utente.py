class Utente:
    def __init__(self, email, password, is_dipendente, is_direttore):
        self.email = email
        self.password = password
        self.is_dipendente = is_dipendente
        self.is_direttore = is_direttore
