from PyQt5 import QtCore, QtGui, QtWidgets
from prenotazioni.view.VistaAggiungiPrenotazione import *
import sys

from prenotazioni.view.VistaPrenotazioniEffettuate import show_vista_prenotazioni_effettuate


class Ui_Form(object):

    def __init__(self, utente_attivo):
        super(Ui_Form, self).__init__()
        self.utente_attivo = utente_attivo

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 265)
        Form.setFixedSize(395, 265)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.pushButton_inserisci = QtWidgets.QPushButton(Form)
        self.pushButton_inserisci.setGeometry(QtCore.QRect(2, 0, 390, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_inserisci.sizePolicy().hasHeightForWidth())
        self.pushButton_inserisci.setSizePolicy(sizePolicy)
        self.pushButton_inserisci.setObjectName("pushButton_inserisci")
        self.pushButton_effettuate = QtWidgets.QPushButton(Form)
        self.pushButton_effettuate.setGeometry(QtCore.QRect(2, 130, 390, 130))
        self.pushButton_effettuate.setFlat(False)
        self.pushButton_effettuate.setObjectName("pushButton_effettuate")

        self.pushButton_inserisci.clicked.connect(lambda: show_vista_aggiungi_prenotazione(self.utente_attivo))
        self.pushButton_effettuate.clicked.connect(lambda: show_vista_prenotazioni_effettuate(self.utente_attivo))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestisci Prenotazioni"))
        self.pushButton_inserisci.setText(_translate("Form", "Inserisci Prenotazione"))
        self.pushButton_effettuate.setText(_translate("Form", "Prenotazioni Effettuate"))


def show_vista_schermata_prenotazioni(utente_attivo):
    ui = Ui_Form(utente_attivo)
    ui.setupUi(Form)
    Form.show()

    return ui


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
