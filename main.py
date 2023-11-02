from PyQt5.QtWidgets import QApplication
from utente.view.VistaAccesso import *
from beni.model.Bene import Bene

if __name__ == '__main__':
    nuovo_bene = Bene("NomeBene", "Immagine", "Area", "Descrizione", "Stato", "StatoArea", "ID", "DataAggiunta")
    controllore = ControlloreListaBeni()
    controllore.inserisci_bene(nuovo_bene)

    app = QApplication(sys.argv)
    show_login_utente()
    sys.exit(app.exec_())



