from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from utente.controller.ControlloreGestioneUtenti import *
import sys


class Ui_VistaInserisciDipendente(object):

    def __init__(self):
        super(Ui_VistaInserisciDipendente).__init__()
        self.controller = ControlloreGestioneUtenti()
    def setupUi(self, VistaInserisciDipendente):
        VistaInserisciDipendente.setObjectName("VistaInserisciDipendente")
        VistaInserisciDipendente.resize(300, 180)
        self.label = QtWidgets.QLabel(VistaInserisciDipendente)
        self.label.setGeometry(QtCore.QRect(60, 30, 207, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(VistaInserisciDipendente)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 100, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(VistaInserisciDipendente)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 120, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton.clicked.connect(lambda: self.clicked_inserisci_dipendente())

        self.retranslateUi(VistaInserisciDipendente)
        QtCore.QMetaObject.connectSlotsByName(VistaInserisciDipendente)

    def retranslateUi(self, VistaInserisciDipendente):
        _translate = QtCore.QCoreApplication.translate
        VistaInserisciDipendente.setWindowTitle(_translate("VistaInserisciDipendente", "Inserisci dipendente"))
        self.label.setText(_translate("VistaInserisciDipendente", "Dipendente da inserire"))
        self.pushButton.setText(_translate("VistaInserisciDipendente", "Inserisci"))
        self.lineEdit.setPlaceholderText(_translate("VistaInserisciDipendente", "email"))

    def clicked_inserisci_dipendente(self):
        email_in = self.lineEdit.text()
        if email_in == "":
            self.show_popup(0, "Inserisci un' email!")
        else:
            if self.controller.inserisci_dipendente(email_in):
                VistaInserisciDipendente.close()

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


def show_inserisci_dipendente():
    ui = Ui_VistaInserisciDipendente()
    ui.setupUi(VistaInserisciDipendente)
    VistaInserisciDipendente.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaInserisciDipendente = QtWidgets.QWidget()
