# -*- coding: utf-8 -*-
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QMessageBox, QListView
from biglietto.controller.ControlloreBiglietto import ControlloreBiglietto
from prenotazioni.Controller.ControllorePrenotazioniEffettuate import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys


class Ui_MainWindow(object):

    def __init__(self, utente_attivo):
        super(Ui_MainWindow, self).__init__()
        self.utente_attivo = utente_attivo
        self.controller = ControllorePrenotazioniEffettuate()
        self.controller_biglietti = ControlloreBiglietto()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 580)
        MainWindow.setFixedSize(800, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 50, 761, 471))
        self.listView.setObjectName("listView")
        self.pushButton_scarica = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scarica.setGeometry(QtCore.QRect(110, 530, 200, 40))
        self.pushButton_scarica.setObjectName("pushButton_scarica")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 25, 250, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_Elimina = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Elimina.setGeometry(QtCore.QRect(500, 530, 200, 40))
        self.pushButton_Elimina.setObjectName("pushButton_Elimina")
        MainWindow.setCentralWidget(self.centralwidget)

        self.visualizza_prenotazioni_per_email()

        self.pushButton_Elimina.clicked.connect(lambda: self.elimina_prenotazione())
        self.pushButton_scarica.clicked.connect(lambda: self.scarica_biglietto())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prenotazioni Effettuate"))
        self.pushButton_scarica.setText(_translate("MainWindow", "Scarica Bilgietto"))
        self.label.setText(_translate("MainWindow", "Prenotazioni effettuate:"))
        self.pushButton_Elimina.setText(_translate("MainWindow", "Elimina Prenotazione"))

    # popola la listview con le prenotazioni effettuate dall'utente
    def visualizza_prenotazioni_per_email(self):
        model = QStringListModel()
        model.setStringList(self.controller.visualizza_lista_prenotazioni_per_email(self.utente_attivo))
        self.listView.setModel(model)
        self.listView.setEditTriggers(QListView.NoEditTriggers)

    # preleva i dati della prenotazione selezionata e genera il pdf del biglietto da scaricare
    def scarica_biglietto(self):
        if self.listView.currentIndex().data() == None:
            show_popup_errore_scarica()
            pass
        else:
            dati_prenotazione = self.listView.currentIndex().data().split("    ")
            self.controller_biglietti.scarica_biglietto(dati_prenotazione[0],
                                                        dati_prenotazione[2],
                                                        self.utente_attivo.email,
                                                        dati_prenotazione[1].split("  ")[0],
                                                        dati_prenotazione[1].split("  ")[1])

    # elimina la prenotazione selezionata dal DatabasePrenotazioni
    def elimina_prenotazione(self):
        self.controller.elimina_prenotazione(self.listView.currentIndex().data(), self.utente_attivo)
        show_popup_prenotazione_eliminata()
        self.visualizza_prenotazioni_per_email()


def show_vista_prenotazioni_effettuate(utente_attivo):
    ui = Ui_MainWindow(utente_attivo)
    ui.setupUi(MainWindow)

    MainWindow.show()

    return ui


def show_popup_errore_scarica():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Seleziona una prenotazione")
    msg.setWindowTitle("Errore")
    msg.exec_()

def show_popup_prenotazione_eliminata():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Prenotazione eliminata")
    msg.setWindowTitle("Conferma eliminazione")
    msg.exec_()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
