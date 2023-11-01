import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtWidgets
from listautenti.model.ListaUtenti import *

from utente.view.VistaAccesso import *
from utente.model.Utente import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_login_utente()
    '''
    app = QtWidgets.QApplication(sys.argv)
    VistaAccesso = QtWidgets.QMainWindow()
    ui = Ui_VistaAccesso()
    ui.setupUi(VistaAccesso)
    VistaAccesso.show()
    '''
    sys.exit(app.exec_())

