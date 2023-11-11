# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaPrenotazioniEffettuate.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    def __init__(self, utente_attivo):
        super(Ui_MainWindow, self).__init__()
        self.utente_attivo = utente_attivo


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
        self.label.setGeometry(QtCore.QRect(20, 25, 200, 25))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prenotazioni Effettuate"))
        self.pushButton_scarica.setText(_translate("MainWindow", "Scarica Bilgietto"))
        self.label.setText(_translate("MainWindow", "Prenotazioni effettuate:"))
        self.pushButton_Elimina.setText(_translate("MainWindow", "Elimina Prenotazione"))


def show_vista_prenotazioni_effettuate(utente_attivo):
    ui = Ui_MainWindow(utente_attivo)
    ui.setupUi(MainWindow)
    MainWindow.show()

    return ui


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# sys.exit(app.exec_())
