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

        # popola il list model utilizzando i dati delle attivitá della lista attivita'
        def popola_lista_attivita():
            lista_attivita = self.controller.get_lista_attivita()
            attivita_names = list(set([attivita.titolo for attivita in lista_attivita]))
            self.list_model = QtCore.QStringListModel(attivita_names)
            self.listView.setModel(self.list_model)

        # Usato solo per la generazione della lista
        # popola_lista(self)

        popola_lista_attivita()
        self.listView.doubleClicked.connect(lambda: self.doppio_click())
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.retranslateUi(VistaListaAttivita)
        QtCore.QMetaObject.connectSlotsByName(VistaListaAttivita)

    def retranslateUi(self, VistaListaAttivita):
        _translate = QtCore.QCoreApplication.translate
        VistaListaAttivita.setWindowTitle(_translate("VistaListaAttivita", "Lista attività"))
        self.label.setText(_translate("VistaListaAttivita", "Attività disponibili"))

    # funzione che legge l'input del mouse dell'utente e apre l'attivitá selezionata
    def doppio_click(self):
        index = self.listView.currentIndex()
        if index.isValid():
            nome_attivita = self.list_model.data(index, QtCore.Qt.DisplayRole)
            show_attivita(self.controller.get_attivita(nome_attivita))


# Funzione per aggiungere un elemento alla QListView
def add_item_to_listview(text, list_model):
    item = QtGui.QStandardItem(text)
    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Imposta come non modificabile
    list_model.appendRow(item)


# usato solo in caso di perdita di dati
def popola_lista(self):
    self.controller.aggiungi_attivita(
        Attivita("Visita senza guida",
                 "Semplice ingresso nel museo",
                 "Lun-Dom",
                 1,
                 60,
                 "10:30",
                 "3€"))
    self.controller.aggiungi_attivita(
        Attivita("Visita guidata",
                 "Itinerario gestito da una guida",
                 "Sab-Dom",
                 2,
                 30,
                 "10:30",
                 "4€"))
    self.controller.aggiungi_attivita(
        Attivita("Attività didattiche per gruppi classe presso il museo",
                 "Tour del museo per gruppi classe con esperimenti",
                 "Mar",
                 3,
                 30,
                 "10:30",
                 "5€"))
    self.controller.aggiungi_attivita(
        Attivita("Attività didattiche per gruppi classe presso sede scolastica",
                 "Esperimenti presso la sede scolastica del cliente",
                 "Gio",
                 4,
                 5,
                 "10:30",
                 "6€"))
    self.controller.aggiungi_attivita(
        Attivita("Escursioni geologiche per gruppi classe presso Parco del Conero o Parco dei Monti Sibillini",
                 "Aventura nei meandri dei Parchi Regionali",
                 "Mer",
                 5,
                 20,
                 "10:30",
                 "6€"))


def show_lista_attivita():
    ui = Ui_VistaListaAttivita()
    ui.setupUi(VistaListaAttivita)
    VistaListaAttivita.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
VistaListaAttivita = QtWidgets.QWidget()
