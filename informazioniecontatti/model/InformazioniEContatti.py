class InformazioniEContatti:

        def __init__ (self):
            super(InformazioniEContatti, self).__init__()
            self.informazioni = "informazioni_temp\n"
            self.contatti = "contatti_temp\n"

        def aggiorna_informazioni(self, informazioni_aggiornate):
            self.informazioni = informazioni_aggiornate

        def aggiorna_contatti(self, contatti_aggiornati):
            self.contatti = contatti_aggiornati

        def get_informazioni(self):
            return self.informazioni

        def get_contatti(self):
            return self.contatti