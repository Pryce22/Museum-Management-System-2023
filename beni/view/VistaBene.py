import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from beni.controller.ControlloreListaBeni import *
import requests


class Ui_VistaBene(object):

    def __init__(self, utente_attivo, bene, callback):
        super(Ui_VistaBene, self).__init__()
        self.controller = ControlloreListaBeni()
        self.utente_attivo = utente_attivo
        #self.image_url = url
        self.bene = bene
        self.callback = callback
    def setupUi(self, VistaBene):
        VistaBene.setObjectName("VistaBene")
        VistaBene.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(VistaBene)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 330, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 210, 401, 51))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setMaxLength(5000)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 400, 61, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(610, 70, 171, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 150, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 300, 141, 21))
        self.checkBox.setObjectName("checkBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 430, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 380, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 350, 141, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 460, 91, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        VistaBene.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VistaBene)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        VistaBene.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VistaBene)
        self.statusbar.setObjectName("statusbar")
        VistaBene.setStatusBar(self.statusbar)

        self.lineEdit_2.hide()
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_8.setReadOnly(True)
        self.comboBox.setEnabled(False)
        self.comboBox.setStyleSheet("QComboBox:disabled { color: black; }")
        self.checkBox.setEnabled(False)
        self.checkBox.setStyleSheet("QCheckBox:disabled { color: black; }")
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setStyleSheet("QCheckBox:disabled { color: black; }")

        if self.utente_attivo.is_dipendente or self.utente_attivo.is_direttore:
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setEnabled(True)
            self.pushButton.setGeometry(QtCore.QRect(670, 490, 121, 51))
            self.pushButton.setObjectName("pushButton")
            self.pushButton.setVisible(False)
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.setGeometry(QtCore.QRect(530, 490, 121, 51))
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(390, 490, 121, 51))
            self.pushButton_3.setObjectName("pushButton_3")
            self.pushButton_3.setEnabled(True)

            self.pushButton_2.clicked.connect(lambda: self.aggiorna_bene())
            self.pushButton.clicked.connect(lambda: self.conferma_aggiornamento_bene())
            self.pushButton_3.clicked.connect(lambda: self.elimina_bene())


        '''response = requests.get(self.image_url)
        image_data = response.content

        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image_data)

        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(610, 110, 171, 171))
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setObjectName("imageLabel")
        label.show()'''
        pixmap = QtGui.QPixmap(self.bene.immagine)
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(610, 110, 171, 171))
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setObjectName("imageLabel")
        label.show()

        self.retranslateUi(VistaBene)
        QtCore.QMetaObject.connectSlotsByName(VistaBene)
        self.retranslateUi(VistaBene)
        QtCore.QMetaObject.connectSlotsByName(VistaBene)

    def retranslateUi(self, VistaBene):
        _translate = QtCore.QCoreApplication.translate
        VistaBene.setWindowTitle(_translate("VistaBene", "Vista bene"))
        self.label_4.setText(_translate("VistaBene", "Descrizione"))
        self.label_6.setText(_translate("VistaBene", "Stato area"))
        self.label_3.setText(_translate("VistaBene", "Area"))
        self.label_5.setText(_translate("VistaBene", "Stato bene"))
        self.label.setText(_translate("VistaBene", "Nome"))
        self.comboBox.setItemText(0, _translate("VistaBene", "Area Geologica"))
        self.comboBox.setItemText(1, _translate("VistaBene", "Area Zoologica"))
        self.comboBox.setItemText(2, _translate("VistaBene", "Area Paleontologica"))
        self.comboBox.setItemText(3, _translate("VistaBene", "Area esposizione temporanee"))
        self.comboBox.setItemText(4, _translate("VistaBene", "Science room"))
        self.checkBox.setText(_translate("VistaBene", "Disponibile"))
        self.label_8.setText(_translate("VistaBene", "Data di aggiunta"))
        self.label_7.setText(_translate("VistaBene", "ID"))
        self.label_9.setText(_translate("VistaBene", "Bene"))
        self.checkBox_2.setText(_translate("VistaBene", "Disponibile"))
        self.label_2.setText(_translate("VistaBene", "Immagine"))
        if self.utente_attivo.is_dipendente:
            self.pushButton.setText(_translate("VistaBene", "Conferma"))
            self.pushButton_2.setText(_translate("VistaBene", "Aggiorna bene"))
            self.pushButton_3.setText(_translate("VistaBene", "Elimina bene"))


    def aggiorna_bene(self):
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_7.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit_8.setReadOnly(False)
        self.comboBox.setEnabled(True)
        self.checkBox.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.pushButton.setVisible(True)
        self.lineEdit_2.setPlaceholderText("Trascina un'immagine qui")
        self.lineEdit_2.setDragEnabled(True)
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.dragEnterEvent = self.dragEnterEvent
        self.lineEdit_2.dropEvent = self.dropEvent
        self.lineEdit_2.show()

    def elimina_bene(self):
        self.controller.elimina_bene(self.bene)
        self.callback()
        VistaBene.close()


    def conferma_aggiornamento_bene(self):
        nome_in = self.lineEdit.text()
        immagine_in = self.lineEdit_2.text()
        area_in = self.comboBox.currentText()
        descrizione_in = self.lineEdit_4.text()
        stato_in = self.checkBox.isChecked()
        stato_area_in = self.checkBox_2.isChecked()
        data_aggiunta_in = self.lineEdit_8.text()
        if self.controller.controlla_nome(nome_in) or nome_in == "":
            if nome_in == "":
                nome_in = self.bene
            if immagine_in == "":
                immagine_in = self.bene.immagine
            if descrizione_in == "":
                descrizione_in = self.bene.descrizione
            if data_aggiunta_in == "":
                data_aggiunta_in = self.bene.data_di_aggiunta
            self.controller.aggiorna_bene(self.bene.nome, nome_in, immagine_in, area_in, descrizione_in, stato_in, stato_area_in,data_aggiunta_in)
            self.show_popup(1, "Bene Aggiornato!")
            self.callback()
            VistaBene.close()
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

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = event.mimeData().urls()
        if files and files[0].isLocalFile():
            path = files[0].toLocalFile()
            self.lineEdit_2.setText(path)





def show_vista_bene(utente_attivo, bene, callback):
    ui = Ui_VistaBene(utente_attivo, bene, callback)
    ui.setupUi(VistaBene)
    VistaBene.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaBene = QtWidgets.QMainWindow()

