import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from beni.controller.ControlloreListaBeni import *
from beni.view.VistaInserisciBene import *


class Ui_VistaListaBeniDipendente(object):

    def __init__(self,utente_attivo):
        super(Ui_VistaListaBeniDipendente, self).__init__()
        self.controller = ControlloreListaBeni()
        self.utente_attivo = utente_attivo
        self.list_model = None
    def setupUi(self, VistaListaBeniDipendente):
        VistaListaBeniDipendente.setObjectName("VistaListaBeniDipendente")
        VistaListaBeniDipendente.resize(858, 646)
        self.centralwidget = QtWidgets.QWidget(VistaListaBeniDipendente)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(650, 80, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 581, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 70, 211, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(170, 70, 191, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 120, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 110, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 180, 871, 431))
        self.listView.setObjectName("listView")
        VistaListaBeniDipendente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VistaListaBeniDipendente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 22))
        self.menubar.setObjectName("menubar")
        VistaListaBeniDipendente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VistaListaBeniDipendente)
        self.statusbar.setObjectName("statusbar")
        VistaListaBeniDipendente.setStatusBar(self.statusbar)
        def popola_listview():
            lista_beni = self.controller.model.get_lista_beni()
            bene_names = list(set([bene.nome for bene in lista_beni]))
            self.list_model = QtCore.QStringListModel(bene_names)
            self.listView.setModel(self.list_model)


        popola_listview()
        self.listView.doubleClicked.connect(lambda: self.item_clicked())

        self.pushButton_2.clicked.connect(lambda: show_inserisci_bene(self.utente_attivo))

        self.retranslateUi(VistaListaBeniDipendente)
        QtCore.QMetaObject.connectSlotsByName(VistaListaBeniDipendente)



    def retranslateUi(self, VistaListaBeniDipendente):
        _translate = QtCore.QCoreApplication.translate
        VistaListaBeniDipendente.setWindowTitle(_translate("VistaListaBeniDipendente", "Vista lista beni"))
        self.comboBox.setItemText(0, _translate("VistaListaBeniDipendente", "Area Geologica"))
        self.comboBox.setItemText(1, _translate("VistaListaBeniDipendente", "Area Zoologica"))
        self.comboBox.setItemText(2, _translate("VistaListaBeniDipendente", "Area Paleontologica"))
        self.comboBox.setItemText(3, _translate("VistaListaBeniDipendente", "Area esposizione temporanee"))
        self.comboBox.setItemText(4, _translate("VistaListaBeniDipendente", "Science room"))
        self.lineEdit.setPlaceholderText(_translate("VistaListaBeniDipendente", "Inserisci Nome o ID"))
        self.checkBox.setText(_translate("VistaListaBeniDipendente", "Beni Disponibili"))
        self.checkBox_2.setText(_translate("VistaListaBeniDipendente", "Beni Non Disponibili"))
        self.pushButton.setText(_translate("VistaListaBeniDipendente", "RICERCA"))
        self.label.setText(_translate("VistaListaBeniDipendente", "LISTA DEI BENI"))
        self.pushButton_2.setText(_translate("VistaListaBeniDipendente", "Inserisci Bene"))
        self.pushButton_3.setText(_translate("VistaListaBeniDipendente", "Stato Aree"))


    def item_clicked(self):
        index = self.listView.currentIndex()
        if index.isValid():
            item = self.list_model.data(index, QtCore.Qt.DisplayRole)
            print("Hai cliccato su:", item)
        else:
            print("Nessun elemento selezionato")




def show_listabeni_dipendente(utente_attivo):
    ui = Ui_VistaListaBeniDipendente(utente_attivo)
    ui.setupUi(VistaListaBeniDipendente)
    VistaListaBeniDipendente.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaListaBeniDipendente = QtWidgets.QMainWindow()

#sys.exit(app.exec_())
