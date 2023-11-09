import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from beni.controller.ControlloreListaBeni import *

class Ui_StatoAree(object):

    def __init__(self, utente_attivo,callback):
        super(Ui_StatoAree, self).__init__()
        self.controller = ControlloreListaBeni()
        self.utente_attivo = utente_attivo
        self.callback = callback

    def setupUi(self, StatoAree):
        StatoAree.setObjectName("StatoAree")
        StatoAree.resize(465, 391)
        self.centralwidget = QtWidgets.QWidget(StatoAree)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(320, 90, 91, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(320, 140, 91, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(320, 190, 81, 18))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(320, 240, 81, 18))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(320, 290, 91, 18))
        self.checkBox_5.setObjectName("checkBox_5")
        StatoAree.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatoAree)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 22))
        self.menubar.setObjectName("menubar")
        StatoAree.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StatoAree)
        self.statusbar.setObjectName("statusbar")
        StatoAree.setStatusBar(self.statusbar)
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(350, 320, 90, 35))
        self.push_button.setObjectName("push_button")

        self.disponibilita_aree()

        self.push_button.clicked.connect(lambda: self.cambia_disponibilita_aree())

        self.retranslateUi(StatoAree)
        QtCore.QMetaObject.connectSlotsByName(StatoAree)

    def retranslateUi(self, StatoAree):
        _translate = QtCore.QCoreApplication.translate
        StatoAree.setWindowTitle(_translate("StatoAree", "Stato aree"))
        self.label.setText(_translate("StatoAree", "Stato Aree"))
        self.label_2.setText(_translate("StatoAree", "Area Geologica"))
        self.label_3.setText(_translate("StatoAree", "Area Zoologica"))
        self.label_4.setText(_translate("StatoAree", "Area Paleontologica"))
        self.label_5.setText(_translate("StatoAree", "Area esposizione temporanee"))
        self.label_6.setText(_translate("StatoAree", "Science room"))
        self.checkBox.setText(_translate("StatoAree", "Disponibile"))
        self.checkBox_2.setText(_translate("StatoAree", "Disponibile"))
        self.checkBox_3.setText(_translate("StatoAree", "Disponibile"))
        self.checkBox_4.setText(_translate("StatoAree", "Disponibile"))
        self.checkBox_5.setText(_translate("StatoAree", "Disponibile"))
        self.push_button.setText(_translate("StatoAree","Conferma"))

    def disponibilita_aree(self):
        aree_stato = self.controller.carica_stato_aree()
        self.checkBox.setChecked(aree_stato.get("Area Geologica"))
        self.checkBox_2.setChecked(aree_stato.get("Area Zoologica"))
        self.checkBox_3.setChecked(aree_stato.get("Area Paleontologica"))
        self.checkBox_4.setChecked(aree_stato.get("Area esposizione temporanee"))
        self.checkBox_5.setChecked(aree_stato.get("Science room"))

    def cambia_disponibilita_aree(self):
        self.controller.cambia_disponibilita_aree(self.checkBox.isChecked(), self.checkBox_2.isChecked(), self.checkBox_3.isChecked(), self.checkBox_4.isChecked(), self.checkBox_5.isChecked())
        self.callback()
        StatoAree.close()

def show_stato_aree(utente_attivo,callback):
    ui = Ui_StatoAree(utente_attivo,callback)
    ui.setupUi(StatoAree)
    StatoAree.show()
    return ui

app = QtWidgets.QApplication(sys.argv)
StatoAree = QtWidgets.QMainWindow()

#sys.exit(app.exec_())
