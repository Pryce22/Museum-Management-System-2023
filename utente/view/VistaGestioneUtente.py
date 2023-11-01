from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from utente.controller.ControlloreGestioneUtenti import *
from utente.view.VistaAggiornaUtente import *


class Ui_VistaUtente(object):

    def __init__(self, utente_attivo):
        super(Ui_VistaUtente, self).__init__()
        self.utente_attivo = utente_attivo
        self.controller = ControlloreGestioneUtenti()

    def setupUi(self, VistaUtente):
        VistaUtente.setObjectName("VistaUtente")
        VistaUtente.resize(300, 200)
        self.label_1 = QtWidgets.QLabel(VistaUtente)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 82, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(VistaUtente)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 86, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(VistaUtente)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 82, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(VistaUtente)
        self.label_4.setGeometry(QtCore.QRect(120, 60, 82, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        if not self.utente_attivo.is_direttore:
            self.pushButton_1 = QtWidgets.QPushButton(VistaUtente)
            self.pushButton_1.setGeometry(QtCore.QRect(30, 140, 91, 41))
            self.pushButton_1.setObjectName("pushButton_1")
            if not self.utente_attivo.is_dipendente:
                self.pushButton_2 = QtWidgets.QPushButton(VistaUtente)
                self.pushButton_2.setGeometry(QtCore.QRect(140, 140, 91, 41))
                self.pushButton_2.setObjectName("pushButton_2")
        if self.utente_attivo.is_dipendente:
            self.label_5 = QtWidgets.QLabel(VistaUtente)
            self.label_5.setGeometry(QtCore.QRect(20, 100, 114, 23))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(16)
            font.setBold(False)
            font.setWeight(50)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(VistaUtente)
            self.label_6.setGeometry(QtCore.QRect(140, 100, 82, 23))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label_6")

        if not self.utente_attivo.is_direttore:
            self.pushButton_1.clicked.connect(lambda: show_aggiorna_utente(self.utente_attivo))
            if not self.utente_attivo.is_dipendente:
                self.pushButton_2.clicked.connect(lambda: self.controller.elimina_utente(self.utente_attivo))

        self.retranslateUi(VistaUtente)
        QtCore.QMetaObject.connectSlotsByName(VistaUtente)

    def retranslateUi(self, VistaUtente):
        _translate = QtCore.QCoreApplication.translate
        VistaUtente.setWindowTitle(_translate("VistaUtente", "Gestione utente"))
        self.label_1.setText(_translate("VistaUtente", "Email:"))
        self.label_2.setText(_translate("VistaUtente", "Password:"))
        self.label_3.setText(_translate("VistaUtente", self.utente_attivo.email))
        self.label_4.setText(_translate("VistaUtente", self.utente_attivo.password))
        if not self.utente_attivo.is_direttore:
            self.pushButton_1.setText(_translate("VistaUtente", "Aggiorna"))
            if not self.utente_attivo.is_dipendente:
                self.pushButton_2.setText(_translate("VistaUtente", "Elimina"))
        if self.utente_attivo.is_dipendente:
            self.label_5.setText(_translate("VistaUtente", "Tipo account:"))
            self.label_6.setText(_translate("VistaUtente", self.tipo_account()))

    def tipo_account(self):
        if self.utente_attivo.is_direttore:
            return "Direttore"
        if self.utente_attivo.is_dipendente:
            return "Dipendente"
        else:
            return "Cliente"


def show_gestione_utente(utente_attivo):
    ui = Ui_VistaUtente(utente_attivo)
    ui.setupUi(VistaGestioneUtente)
    VistaGestioneUtente.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaGestioneUtente = QtWidgets.QWidget()
