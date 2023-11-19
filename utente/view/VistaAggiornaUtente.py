from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from utente.controller.ControlloreGestioneUtenti import ControlloreGestioneUtenti
import sys


class Ui_VistaAggiornaUtente(object):

    def __init__(self, utente_attivo, callback):
        super(Ui_VistaAggiornaUtente).__init__()
        self.controller = ControlloreGestioneUtenti()
        self.utente_attivo = utente_attivo
        self.callback = callback

    def setupUi(self, VistaAggiornaUtente):
        VistaAggiornaUtente.setObjectName("VistaAggiornaUtente")
        VistaAggiornaUtente.resize(290, 150)
        self.label_1 = QtWidgets.QLabel(VistaAggiornaUtente)
        self.label_1.setGeometry(QtCore.QRect(30, 20, 82, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(VistaAggiornaUtente)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(VistaAggiornaUtente)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(VistaAggiornaUtente)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_1 = QtWidgets.QPushButton(VistaAggiornaUtente)
        self.pushButton_1.setGeometry(QtCore.QRect(190, 100, 81, 31))
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_1.clicked.connect(lambda: self.aggiorna_utente(self.utente_attivo))

        self.retranslateUi(VistaAggiornaUtente)
        QtCore.QMetaObject.connectSlotsByName(VistaAggiornaUtente)

    def retranslateUi(self, VistaAggiornaUtente):
        _translate = QtCore.QCoreApplication.translate
        VistaAggiornaUtente.setWindowTitle(_translate("VistaAggiornaUtente", "Aggiorna utente"))
        self.label_1.setText(_translate("VistaAggiornaUtente", "Email:"))
        self.label_2.setText(_translate("VistaAggiornaUtente", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("VistaAggiornaUtente", "Nuova email"))
        self.lineEdit_2.setPlaceholderText(_translate("VistaAggiornaUtente", "Nuova password"))
        self.pushButton_1.setText(_translate("VistaAggiornaUtente", "Conferma"))

    #Aggiorna i dati nella vista dell'area personale dell'utente
    def aggiorna_utente(self, utente_attivo):
        ok = True
        email_nuova = utente_attivo.email
        password_nuova = utente_attivo.password
        if self.lineEdit.text() != "":
            if self.controller.controlla_email(self.lineEdit.text()):
                email_nuova = self.lineEdit.text()
            else:
                ok = False
                self.show_popup(0, "Email già esistente!")
        if self.lineEdit_2.text() != "":
            password_nuova = self.lineEdit_2.text()
        if ok:
            self.controller.aggiorna_utente(utente_attivo.email, email_nuova, password_nuova)
            self.utente_attivo.email = email_nuova
            self.utente_attivo.password = password_nuova
            self.show_popup(1, "Utente aggiornato.")
            self.callback()
            VistaAggiornaUtente.close()

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


def show_aggiorna_utente(utente_attivo, callback):
    ui = Ui_VistaAggiornaUtente(utente_attivo, callback)
    ui.setupUi(VistaAggiornaUtente)
    VistaAggiornaUtente.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaAggiornaUtente = QtWidgets.QWidget()

