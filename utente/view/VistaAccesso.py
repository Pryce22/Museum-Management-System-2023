from PyQt5.QtWidgets import QMessageBox

from utente.controller.ControlloreGestioneUtenti import *
from utente.model.Utente import Utente
from home.view.VistaHomeCliente import *
from home.view.VistaHomeDirettore import *


class Ui_VistaAccesso(object):

    def __init__(self):
        super(Ui_VistaAccesso, self).__init__()
        self.utente_attivo = None
        self.controller = ControlloreGestioneUtenti()

    def setupUi(self, VistaAccesso):
        VistaAccesso.setObjectName("VistaAccesso")
        VistaAccesso.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VistaAccesso.sizePolicy().hasHeightForWidth())
        VistaAccesso.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(VistaAccesso)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(398, 0, 6, 600))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(140, 100, 83, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(120, 190, 140, 20))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 240, 140, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(534, 100, 112, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 190, 140, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(520, 240, 140, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(552, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        VistaAccesso.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VistaAccesso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        VistaAccesso.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VistaAccesso)
        self.statusbar.setObjectName("statusbar")
        VistaAccesso.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.clicked_login)
        self.pushButton_2.clicked.connect(self.clicked_signup)

        self.retranslateUi(VistaAccesso)
        QtCore.QMetaObject.connectSlotsByName(VistaAccesso)

    def retranslateUi(self, VistaAccesso):
        _translate = QtCore.QCoreApplication.translate
        VistaAccesso.setWindowTitle(_translate("VistaAccesso", "Accesso"))
        self.label_1.setText(_translate("VistaAccesso", "Login"))
        self.lineEdit_1.setPlaceholderText(_translate("VistaAccesso", "e-mail"))
        self.lineEdit.setPlaceholderText(_translate("VistaAccesso", "password"))
        self.pushButton.setText(_translate("VistaAccesso", "Login"))
        self.label_2.setText(_translate("VistaAccesso", "Sign Up"))
        self.lineEdit_2.setPlaceholderText(_translate("VistaAccesso", "e-mail"))
        self.lineEdit_3.setPlaceholderText(_translate("VistaAccesso", "password"))
        self.pushButton_2.setText(_translate("VistaAccesso", "Sign Up"))

    def clicked_login(self):
        email_in = self.lineEdit_1.text()
        password_in = self.lineEdit.text()
        if email_in == "" or password_in == "":
            self.show_popup(0, "Compila tutti i campi per il login!")
        else:
            if self.controller.trova_utente(email_in) == "":
                self.show_popup(0, "Account non trovato!")
            else:
                utente_trovato = self.controller.trova_utente(email_in)
                if utente_trovato.email == email_in and utente_trovato.password == password_in:
                    self.utente_attivo = utente_trovato
                    if self.utente_attivo.is_direttore:
                        show_home_direttore(self.utente_attivo)
                    else:
                        show_home_cliente(self.utente_attivo)
                    VistaAccesso.close()
                else:
                    self.show_popup(0, "Account non trovato!")

    def clicked_signup(self):
        email_in = self.lineEdit_2.text()
        password_in = self.lineEdit_3.text()
        if email_in == "" or password_in == "":
            self.show_popup(0, "Compila tutti i campi per il signup!")
        else:
            if self.controller.controlla_email(email_in):
                self.controller.inserisci_utente(Utente(email_in, password_in, False, False))
                self.show_popup(1, "Account registrato!")
            else:
                self.show_popup(0, "Email non valida!")

    def show_popup(self, n, text):
        msg = QMessageBox()
        if n == 0:
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Errore")
            msg.setText(text)
        elif n == 1:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Errore")
            msg.setText(text)
        x = msg.exec_()


def show_login_utente():
    import sys
    ui = Ui_VistaAccesso()
    ui.setupUi(VistaAccesso)
    VistaAccesso.show()
    sys.exit(app.exec_())


app = QtWidgets.QApplication(sys.argv)
VistaAccesso = QtWidgets.QMainWindow()
