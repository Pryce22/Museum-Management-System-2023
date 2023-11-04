import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from attivita.controller.ControlloreListaAttivita import *


class Ui_Attivita(object):

    def __init__(self, attivita_selezionata):
        super().__init__()
        self.controller = ControlloreListaAttivita()
        self.attivita_selezionata = attivita_selezionata

    def setupUi(self, Attivita):
        Attivita.setObjectName("Attivita")
        Attivita.resize(513, 300)
        self.label_1 = QtWidgets.QLabel(Attivita)
        self.label_1.setGeometry(QtCore.QRect(170, 40, 328, 38))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setTextFormat(QtCore.Qt.PlainText)
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.label = QtWidgets.QLabel(Attivita)
        self.label.setGeometry(QtCore.QRect(20, 40, 57, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Attivita)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 105, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(Attivita)
        self.label_11.setGeometry(QtCore.QRect(170, 100, 68, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.splitter = QtWidgets.QSplitter(Attivita)
        self.splitter.setGeometry(QtCore.QRect(20, 161, 123, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.splitter.setFont(font)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_7 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.splitter_2 = QtWidgets.QSplitter(Attivita)
        self.splitter_2.setGeometry(QtCore.QRect(170, 160, 68, 101))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Attivita)
        QtCore.QMetaObject.connectSlotsByName(Attivita)

    def retranslateUi(self, Attivita):
        _translate = QtCore.QCoreApplication.translate
        Attivita.setWindowTitle(_translate("Attivita", "Attivita"))
        self.label_1.setText(_translate("Attivita", self.attivita_selezionata.titolo))
        self.label.setText(_translate("Attivita", "Titolo:"))
        self.label_5.setText(_translate("Attivita", "Descrizione:"))
        self.label_11.setText(_translate("Attivita", self.attivita_selezionata.descrizione))
        self.label_7.setText(_translate("Attivita", "Prezzo:"))
        self.label_8.setText(_translate("Attivita", "Giorno:"))
        self.label_9.setText(_translate("Attivita", "Orario:"))
        self.label_10.setText(_translate("Attivita", "Posti massimi:"))
        self.label_2.setText(_translate("Attivita", self.attivita_selezionata.prezzo)) #
        self.label_3.setText(_translate("Attivita", self.attivita_selezionata.giorno_della_settimana)) #
        self.label_4.setText(_translate("Attivita", self.attivita_selezionata.orario)) #
        self.label_6.setText(_translate("Attivita", str(self.attivita_selezionata.n_posti))) #

    def update_ui(self):
        self.label_1.setText(self.attivita_selezionata.titolo)
        self.label_11.setText(self.attivita_selezionata.descrizione)
        self.label_2.setText(self.attivita_selezionata.prezzo)
        self.label_3.setText(self.attivita_selezionata.giorno_della_settimana)
        self.label_4.setText(self.attivita_selezionata.orario)
        self.label_6.setText(str(self.attivita_selezionata.n_posti))


def show_attivita(attivita_selezionata):
    ui = Ui_Attivita(attivita_selezionata)
    ui.setupUi(Attivita)
    Attivita.show()
    # ui.update_ui()
    return ui


app = QtWidgets.QApplication(sys.argv)
Attivita = QtWidgets.QWidget()
