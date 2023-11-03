import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from beni.controller.ControlloreListaBeni import *
from beni.model.Bene import *


class Ui_VistaInserisciBene(object):

    def __init__(self, utente_attivo):
        super(Ui_VistaInserisciBene, self).__init__()
        self.controller = ControlloreListaBeni()
        self.utente_attivo = utente_attivo


    def setupUi(self, VistaInserisciBene):
        VistaInserisciBene.setObjectName("VistaInserisciBene")
        VistaInserisciBene.resize(476, 504)
        self.centralwidget = QtWidgets.QWidget(VistaInserisciBene)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 171, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 200, 401, 51))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(20, 380, 61, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 380, 91, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 150, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 280, 141, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 330, 141, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 360, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 400, 121, 51))
        self.pushButton.setObjectName("pushButton")
        VistaInserisciBene.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VistaInserisciBene)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 22))
        self.menubar.setObjectName("menubar")
        VistaInserisciBene.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VistaInserisciBene)
        self.statusbar.setObjectName("statusbar")
        VistaInserisciBene.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(lambda: self.conferma_aggiunta())

        self.retranslateUi(VistaInserisciBene)
        QtCore.QMetaObject.connectSlotsByName(VistaInserisciBene)

        self.label_7.deleteLater()
        self.lineEdit_7.deleteLater()

    def retranslateUi(self, VistaInserisciBene):
            _translate = QtCore.QCoreApplication.translate
            VistaInserisciBene.setWindowTitle(_translate("VistaInserisciBene", "Inserisci bene"))
            self.comboBox.setItemText(0, _translate("VistaInserisciBene", "Area Geologica"))
            self.comboBox.setItemText(1, _translate("VistaInserisciBene", "Area Zoologica"))
            self.comboBox.setItemText(2, _translate("VistaInserisciBene", "Area Paleontologica"))
            self.comboBox.setItemText(3, _translate("VistaInserisciBene", "Area esposizione temporanee"))
            self.comboBox.setItemText(4, _translate("VistaInserisciBene", "Science room"))
            self.label.setText(_translate("VistaInserisciBene", "Nome"))
            self.checkBox.setText(_translate("VistaInserisciBene", "Disponibile"))
            self.checkBox_2.setText(_translate("VistaInserisciBene", "Disponibile"))
            self.label_2.setText(_translate("VistaInserisciBene", "URL immagine"))
            self.label_3.setText(_translate("VistaInserisciBene", "Area"))
            self.label_4.setText(_translate("VistaInserisciBene", "Descrizione"))
            self.label_5.setText(_translate("VistaInserisciBene", "Stato bene"))
            self.label_6.setText(_translate("VistaInserisciBene", "Stato area"))
            self.label_7.setText(_translate("VistaInserisciBene", "ID"))
            self.label_8.setText(_translate("VistaInserisciBene", "Data di aggiunta"))
            self.label_9.setText(_translate("VistaInserisciBene", "Inserisci bene"))
            self.pushButton.setText(_translate("VistaInserisciBene", "Conferma"))


    def conferma_aggiunta(self):
        nome_in = self.lineEdit.text()
        immagine_in = self.lineEdit_2.text()
        area_in = self.comboBox.currentText()
        descrizione_in = self.lineEdit_4.text()
        stato_in = self.checkBox.isChecked()
        stato_area_in = self.checkBox_2.isChecked()
        data_aggiunta_in = self.lineEdit_8.text()
        if nome_in == "" or immagine_in == "" or descrizione_in == "" or data_aggiunta_in == "":
            self.show_popup(0, "Compila tutti i campi per inserire il bene!")
        else:
                if self.controller.controlla_nome(nome_in):
                    id_bene_in = self.controller.crea_id_bene()
                    self.controller.inserisci_bene(Bene(nome_in, immagine_in, area_in,descrizione_in, stato_in,stato_area_in,id_bene_in,data_aggiunta_in))
                    self.show_popup(1, "Bene inserito!")
                    VistaInserisciBene.close()
                else:
                    self.show_popup(0, "Nome già presente!")


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


def show_inserisci_bene(utente_attivo):
    ui = Ui_VistaInserisciBene(utente_attivo)
    ui.setupUi(VistaInserisciBene)
    #ui.pushButton.clicked.connect(ui.conferma_aggiunta)
    VistaInserisciBene.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaInserisciBene = QtWidgets.QMainWindow()
