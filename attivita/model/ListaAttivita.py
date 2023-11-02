class ListaAttivita:

    def __init__(self):
        super(ListaAttivita, self).__init__()
        self.lista_attivita = []

    def get_attivita(self, attivita_selezionata):
        for attivita in self.lista_attivita:
            if attivita is attivita_selezionata:
                return attivita