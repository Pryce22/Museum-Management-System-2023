import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from attivita.controller.ControlloreListaAttivita import *
from attivita.model.Attivita import *
from attivita.view.VistaAttivita import *


class Ui_VistaListaAttivita(object):
    def __init__(self):
        super(Ui_VistaListaAttivita, self).__init__()
        self.controller = ControlloreListaAttivita()
        self.list_model = None

    def setupUi(self, VistaListaAttivita):
        VistaListaAttivita.setObjectName("VistaListaAttivita")
        VistaListaAttivita.resize(600, 350)
        VistaListaAttivita.setFixedSize(600, 350)
        self.listView = QtWidgets.QListView(VistaListaAttivita)
        self.listView.setGeometry(QtCore.QRect(50, 90, 500, 221))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(VistaListaAttivita)
        self.label.setGeometry(QtCore.QRect(190, 30, 204, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        def popola_lista_attivita():
            lista_attivita = self.controller.get_lista_attivita()
            print(lista_attivita)
            attivita_names = list(set([attivita.titolo for attivita in lista_attivita]))
            self.list_model = QtCore.QStringListModel(attivita_names)
            self.listView.setModel(self.list_model)

        #popola_lista(self)
        popola_lista_attivita()
        #print(self.controller.get_lista_attivita())
        self.listView.doubleClicked.connect(lambda: self.doppio_click())
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.retranslateUi(VistaListaAttivita)
        QtCore.QMetaObject.connectSlotsByName(VistaListaAttivita)

    def retranslateUi(self, VistaListaAttivita):
        _translate = QtCore.QCoreApplication.translate
        VistaListaAttivita.setWindowTitle(_translate("VistaListaAttivita", "Lista attività"))
        self.label.setText(_translate("VistaListaAttivita", "Attività disponibili"))

    def doppio_click(self):
        index = self.listView.currentIndex()
        if index.isValid():
            nome_attivita = self.list_model.data(index, QtCore.Qt.DisplayRole)
            show_attivita(self.controller.get_attivita(nome_attivita))
            print("Titolo dell'oggetto selezionato:", self.controller.get_attivita(nome_attivita).titolo)
        else:
            print("Nessun elemento selezionato")

    def stampa_lista_attivita(self, list_model):
        for a in self.controller.get_lista_attivita():
            add_item_to_listview(a.titolo, list_model)


# Funzione per aggiungere un elemento alla QListView
def add_item_to_listview(text, list_model):
    item = QtGui.QStandardItem(text)
    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Imposta come non modificabile
    list_model.appendRow(item)


def popola_lista(self):
    self.controller.aggiungi_attivita(
        Attivita("Visita senza guida",
                 "Descrizione prima attivita",
                 "Lun-Dom",
                 1,
                 60,
                 "10:30",
                 "3€"))
    self.controller.aggiungi_attivita(
        Attivita("Visita guidata",
                 "Descrizione seconda attivita",
                 "Lun-Dom",
                 2, 60,
                 "10:30",
                 "4€"))
    self.controller.aggiungi_attivita(
        Attivita("Attività didattiche per gruppi classe presso il museo",
                 "Descrizione terza attivita",
                 "Lun-Dom",
                 3,
                 60,
                 "10:30",
                 "5€"))
    self.controller.aggiungi_attivita(
        Attivita("Attività didattiche per gruppi classe presso sede scolastica",
                 "Descrizione quarta attivita",
                 "Lun-Dom",
                 4, 60,
                 "10:30",
                 "6€"))
    self.controller.aggiungi_attivita(
        Attivita("Escursioni geologiche per gruppi classe presso Parco del Conero o Parco dei Monti Sibillini",
                 "Descrizione quinta attivita",
                 "Lun-Dom",
                 5,
                 60,
                 "10:30",
                 "6€"))


def show_lista_attivita():
    ui = Ui_VistaListaAttivita()
    ui.setupUi(VistaListaAttivita)

    #list_view = ui.listView
    #list_model = QtGui.QStandardItemModel()
    #list_view.setModel(list_model)

    #LA SEGUENTE FUNZIONE RIGENERA IL PICKLE CON LE ATTIVITA PREDEFINITE
    #ui.popola_lista()

    #inserisci elementi nella listView
    #ui.stampa_lista()


    VistaListaAttivita.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaListaAttivita = QtWidgets.QWidget()
