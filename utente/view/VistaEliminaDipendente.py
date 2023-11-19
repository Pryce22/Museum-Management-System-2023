from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
from utente.controller.ControlloreGestioneUtenti import ControlloreGestioneUtenti


class Ui_VistaEliminaDipendente(object):

    def __init__(self):
        super(Ui_VistaEliminaDipendente).__init__()
        self.controller = ControlloreGestioneUtenti()

    def setupUi(self, VistaEliminaDipendente):
        VistaEliminaDipendente.setObjectName("VistaEliminaDipendente")
        VistaEliminaDipendente.resize(300, 180)
        self.label = QtWidgets.QLabel(VistaEliminaDipendente)
        self.label.setGeometry(QtCore.QRect(50, 30, 207, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(VistaEliminaDipendente)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 100, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(VistaEliminaDipendente)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 120, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton.clicked.connect(lambda: self.elimina_dipendenti_clicked())

        self.retranslateUi(VistaEliminaDipendente)
        QtCore.QMetaObject.connectSlotsByName(VistaEliminaDipendente)

    def retranslateUi(self, VistaEliminaDipendente):
        _translate = QtCore.QCoreApplication.translate
        VistaEliminaDipendente.setWindowTitle(_translate("VistaEliminaDipendente", "Elimina dipendente"))
        self.label.setText(_translate("VistaEliminaDipendente", "Dipendente da eliminare:"))
        self.pushButton.setText(_translate("VistaEliminaDipendente", "Elimina"))
        self.lineEdit.setPlaceholderText(_translate("VistaEliminaDipendente", "email"))

    def elimina_dipendenti_clicked(self):
        email_in = self.lineEdit.text()
        if email_in == "":
            self.show_popup(0, "Inserisci un' email!")
        else:
            if self.controller.elimina_utente(email_in):
                VistaEliminaDipendente.close()
            else:
                self.show_popup(0, "Dipendente non trovato!")

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


def show_elimina_dipendente(self):
    ui = Ui_VistaEliminaDipendente()
    ui.setupUi(VistaEliminaDipendente)
    VistaEliminaDipendente.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaEliminaDipendente = QtWidgets.QWidget()
