# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from attivita.model.Attivita import *


class Ui_Form(object):

    def __init__(self, attivita):
        super(Ui_Form, self).__init__()
        self.attivita = attivita

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 350)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Titolo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titolo.setFont(font)
        self.label_Titolo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titolo.setObjectName("label_Titolo")
        self.verticalLayout.addWidget(self.label_Titolo)
        self.label_Descrizione = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Descrizione.setFont(font)
        self.label_Descrizione.setObjectName("label_Descrizione")
        self.verticalLayout.addWidget(self.label_Descrizione)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.label_Prezzo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Prezzo.setFont(font)
        self.label_Prezzo.setObjectName("label_Prezzo")
        self.verticalLayout.addWidget(self.label_Prezzo)
        self.label_prezzo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_prezzo.setObjectName("label_prezzo")
        self.verticalLayout.addWidget(self.label_prezzo)
        self.label_Giorno = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Giorno.setFont(font)
        self.label_Giorno.setObjectName("label_Giorno")
        self.verticalLayout.addWidget(self.label_Giorno)
        self.label_giorno = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_giorno.setObjectName("label_giorno")
        self.verticalLayout.addWidget(self.label_giorno)
        self.label_Orario = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Orario.setFont(font)
        self.label_Orario.setObjectName("label_Orario")
        self.verticalLayout.addWidget(self.label_Orario)
        self.label_orario = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_orario.setObjectName("label_orario")
        self.verticalLayout.addWidget(self.label_orario)
        self.label_Posti_Max = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Posti_Max.setFont(font)
        self.label_Posti_Max.setObjectName("label_Posti_Max")
        self.verticalLayout.addWidget(self.label_Posti_Max)
        self.label_posti_max = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_posti_max.setObjectName("label_posti_max")
        self.verticalLayout.addWidget(self.label_posti_max)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Attività"))
        self.label_Titolo.setText(_translate("Form", "Titolo"))
        self.label_Descrizione.setText(_translate("Form", "Descrizione:"))
        self.plainTextEdit_2.setPlainText(self.attivita.descrizione)
        self.label_Prezzo.setText(_translate("Form", "Prezzo:"))
        self.label_prezzo.setText(_translate("Form", str(self.attivita.prezzo)))
        self.label_Giorno.setText(_translate("Form", "Giorno:"))
        self.label_giorno.setText(_translate("Form", self.attivita.giorno_della_settimana))
        self.label_Orario.setText(_translate("Form", "Orario:"))
        self.label_orario.setText(_translate("Form", self.attivita.orario))
        self.label_Posti_Max.setText(_translate("Form", "Posti massimi prenotabili:"))
        self.label_posti_max.setText(_translate("Form", str(self.attivita.n_posti)))


def show_attivita(attivita_selezionata):
    ui = Ui_Form(attivita_selezionata)
    ui.setupUi(Form)
    Form.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
