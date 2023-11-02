import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from informazioniecontatti.view.VistaInformazioniEContatti import show_vista_informazioni_e_contatti
from utente.view.VistaGestioneUtente import *
from utente.view.VistaGestioneUtente import show_gestione_utente
from utente.view.VistaInserisciDipendente import *
from utente.view.VistaEliminaDipendente import *


class Ui_VistaHomeDirettore(object):

    def __init__(self, utente_attivo):
        super(Ui_VistaHomeDirettore).__init__()
        self.utente_attivo = utente_attivo

    def setupUi(self, VistaHomeDirettore):
        VistaHomeDirettore.setObjectName("VistaHomeDirettore")
        if self.utente_attivo.is_direttore:
            VistaHomeDirettore.resize(400, 421)
        else:
            VistaHomeDirettore.resize(400, 281)
        self.pushButton_1 = QtWidgets.QPushButton(VistaHomeDirettore)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 0, 200, 140))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_4 = QtWidgets.QPushButton(VistaHomeDirettore)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 140, 200, 140))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(VistaHomeDirettore)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 0, 200, 140))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(VistaHomeDirettore)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 140, 200, 140))
        self.pushButton_2.setObjectName("pushButton_2")
        if self.utente_attivo.is_direttore:
            self.pushButton_5 = QtWidgets.QPushButton(VistaHomeDirettore)
            self.pushButton_5.setGeometry(QtCore.QRect(200, 280, 200, 140))
            self.pushButton_5.setObjectName("pushButton_5")
            self.pushButton_6 = QtWidgets.QPushButton(VistaHomeDirettore)
            self.pushButton_6.setGeometry(QtCore.QRect(0, 280, 200, 140))
            self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_1.clicked.connect(lambda: show_gestione_utente(self.utente_attivo))
        self.pushButton_4.clicked.connect(lambda: show_vista_informazioni_e_contatti(self.utente_attivo))
        if self.utente_attivo.is_direttore:
            self.pushButton_5.clicked.connect(lambda: show_elimina_dipendente(self))
            self.pushButton_6.clicked.connect(lambda: show_inserisci_dipendente())



        self.retranslateUi(VistaHomeDirettore)
        QtCore.QMetaObject.connectSlotsByName(VistaHomeDirettore)

    def retranslateUi(self, VistaHomeDirettore):
        _translate = QtCore.QCoreApplication.translate
        VistaHomeDirettore.setWindowTitle(_translate("VistaHomeDirettore", "Form"))
        self.pushButton_1.setText(_translate("VistaHomeDirettore", "Utente"))
        self.pushButton_4.setText(_translate("VistaHomeDirettore", "Informazioni e contatti"))
        self.pushButton_3.setText(_translate("VistaHomeDirettore", "Prenotazioni"))
        self.pushButton_2.setText(_translate("VistaHomeDirettore", "Beni"))
        if self.utente_attivo.is_direttore:
            self.pushButton_5.setText(_translate("VistaHomeDirettore", "Elimina dipendenti"))
            self.pushButton_6.setText(_translate("VistaHomeDirettore", "Aggiungi dipendente"))


def show_home_direttore(utente_attivo):
    ui = Ui_VistaHomeDirettore(utente_attivo)
    ui.setupUi(VistaHomeDirettore)
    VistaHomeDirettore.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaHomeDirettore = QtWidgets.QWidget()
