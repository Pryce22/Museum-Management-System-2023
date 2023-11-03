import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from beni.controller.ControlloreListaBeni import *


class Ui_VistaListaBeniCliente(object):
    def __init__(self, utente_attivo):
        super(Ui_VistaListaBeniCliente, self).__init__()
        self.controller = ControlloreListaBeni()
        self.utente_attivo = utente_attivo
        self.list_model = None
    def setupUi(self, VistaListaBeniCliente):
        VistaListaBeniCliente.setObjectName("VistaListaBeniCliente")
        VistaListaBeniCliente.resize(857, 645)
        self.centralwidget = QtWidgets.QWidget(VistaListaBeniCliente)
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
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 591, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 70, 181, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 70, 171, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 20, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 180, 871, 431))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 120, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        VistaListaBeniCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VistaListaBeniCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 22))
        self.menubar.setObjectName("menubar")
        VistaListaBeniCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VistaListaBeniCliente)
        self.statusbar.setObjectName("statusbar")
        VistaListaBeniCliente.setStatusBar(self.statusbar)

        #aggiunta selezione beni dalla lista

        def popola_listview():
            print("4")
            lista_beni = self.controller.model.get_lista_beni()
            print("5")
            bene_names = list(set([bene.nome for bene in lista_beni]))
            print("6")
            self.list_model = QtCore.QStringListModel(bene_names)
            self.listView.setModel(self.list_model)


        popola_listview()
        self.listView.doubleClicked.connect(lambda: self.item_clicked())
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #


        self.retranslateUi(VistaListaBeniCliente)
        QtCore.QMetaObject.connectSlotsByName(VistaListaBeniCliente)

    def retranslateUi(self, VistaListaBeniCliente):
        _translate = QtCore.QCoreApplication.translate
        VistaListaBeniCliente.setWindowTitle(_translate("VistaListaBeniCliente", "Vista lista beni"))
        self.comboBox.setItemText(0, _translate("VistaListaBeniCliente", "Area Geologica"))
        self.comboBox.setItemText(1, _translate("VistaListaBeniCliente", "Area Zoologica"))
        self.comboBox.setItemText(2, _translate("VistaListaBeniCliente", "Area Paleontologica"))
        self.comboBox.setItemText(3, _translate("VistaListaBeniCliente", "Area esposizione temporanee"))
        self.comboBox.setItemText(4, _translate("VistaListaBeniCliente", "Science room"))
        self.lineEdit.setPlaceholderText(_translate("VistaListaBeniCliente", "Inserisci Nome o ID"))
        self.checkBox.setText(_translate("VistaListaBeniCliente", "Beni Disponibili"))
        self.checkBox_2.setText(_translate("VistaListaBeniCliente", "Beni Non Disponibili"))
        self.pushButton.setText(_translate("VistaListaBeniCliente", "RICERCA"))
        self.label.setText(_translate("VistaListaBeniCliente", "LISTA DEI BENI"))



    def item_clicked(self):
        index = self.listView.currentIndex()
        if index.isValid():
            item = self.list_model.data(index, QtCore.Qt.DisplayRole)
            print("Hai cliccato su:", item)
        else:
            print("Nessun elemento selezionato")

def show_listabeni_cliente(utente_attivo):
    ui = Ui_VistaListaBeniCliente(utente_attivo)
    ui.setupUi(VistaListaBeniCliente)
    VistaListaBeniCliente.show()
    return ui





app = QtWidgets.QApplication(sys.argv)
VistaListaBeniCliente = QtWidgets.QMainWindow()

#sys.exit(app.exec_())
