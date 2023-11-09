from PyQt5.QtWidgets import QApplication
from utente.view.VistaAccesso import *



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_login_utente()
    sys.exit(app.exec_())




