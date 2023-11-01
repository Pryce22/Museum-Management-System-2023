class InformazioniEContatti:
    def __init__(self):
        super(InformazioniEContatti, self).__init__()
        self.informazioni = "Orari di apertura:\nIl museo è aperto e disponibile tutti i giorni dalle 8:30 alle 19:30"
        self.contatti = "Angjelo Libofsha -  S11048126@studenti.univpm.it\nValerio Crocetti   -  S1103351@studenti.univpm.it\nMatteo Colletta   -  S1105265@studenti.univpm.it"

    def aggiorna_informazioni(self, informazioni_aggiornate):
        self.informazioni = informazioni_aggiornate

    def aggiorna_contatti(self, contatti_aggiornati):
        self.contatti = contatti_aggiornati

    def get_informazioni(self):
        return self.informazioni

    def get_contatti(self):
        print("y")
        return self.contatti
