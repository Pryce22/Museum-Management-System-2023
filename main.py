import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtWidgets

from utente.view.VistaAccesso import Ui_VistaAccesso, go_login_utente

if __name__ == '__main__':
    app = QApplication(sys.argv)
    go_login_utente()
    sys.exit(app.exec_())

