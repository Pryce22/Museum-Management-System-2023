from PyQt5 import QtCore, QtGui, QtWidgets

from attivita.view.VistaListaAttivita import show_lista_attivita
from prenotazioni.view.VistaSchermataPrenotazioni import *
import sys


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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(2, 1, 391, 131))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(2, 130, 391, 131))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(lambda: show_vista_schermata_prenotazioni(self.utente_attivo))
        self.pushButton.clicked.connect(lambda: show_lista_attivita())
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prenotazioni"))
        self.pushButton.setText(_translate("Form", "Attività disponibili"))
        self.pushButton_2.setText(_translate("Form", "Prenotazioni"))


def show_vista_prenotazioni(utente_attivo):
    ui = Ui_Form(utente_attivo)
    ui.setupUi(Form)
    Form.show()

    return ui


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
