import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtWidgets

from utente.view.VistaAccesso import Ui_VistaAccesso, mostra

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mostra()
    sys.exit(app.exec_())

