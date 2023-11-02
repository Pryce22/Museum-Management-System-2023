from PyQt5 import QtCore, QtGui, QtWidgets
from informazioniecontatti.controller.ControlloreInformazioniEContatti import *
import sys


class Ui_InformazioniEContatti(object):

    def __init__(self, utente_attivo):
        super(Ui_InformazioniEContatti, self).__init__()
        self.controller = ControlloreInformazioniEContatti()
        self.utente_attivo = utente_attivo

    def setupUi(self, InformazioniEContatti):
        InformazioniEContatti.setObjectName("InformazioniEContatti")
        InformazioniEContatti.resize(898, 557)
        self.verticalLayoutWidget = QtWidgets.QWidget(InformazioniEContatti)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 901, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_informazioni = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_informazioni.setFont(font)
        self.label_informazioni.setObjectName("label_informazioni")
        self.verticalLayout.addWidget(self.label_informazioni)
        self.Text_informazioni = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.Text_informazioni.setFont(font)
        if not self.utente_attivo.is_direttore:
            self.Text_informazioni.setReadOnly(True)
        self.Text_informazioni.setObjectName("Text_informazioni")
        self.verticalLayout.addWidget(self.Text_informazioni)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_contatti = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_contatti.setFont(font)
        self.label_contatti.setObjectName("label_contatti")
        self.verticalLayout.addWidget(self.label_contatti)

        self.Text_contatti = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.Text_contatti.setFont(font)
        if not self.utente_attivo.is_direttore:
            self.Text_contatti.setReadOnly(True)
        self.Text_contatti.setObjectName("Text_contatti")
        self.verticalLayout.addWidget(self.Text_contatti)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        if self.utente_attivo.is_direttore:
            self.pushButton1 = QtWidgets.QPushButton(InformazioniEContatti)
            self.pushButton1.setGeometry(QtCore.QRect(0, 0, 300, 40))
            self.verticalLayout.addWidget(self.pushButton1)

        if self.utente_attivo.is_direttore:
            self.pushButton1.clicked.connect(lambda: self.aggiorna_informazioni_e_contatti_clicked
            (self.Text_informazioni.toPlainText(), self.Text_contatti.toPlainText()))

        self.retranslateUi(InformazioniEContatti)
        QtCore.QMetaObject.connectSlotsByName(InformazioniEContatti)

    def retranslateUi(self, InformazioniEContatti):
        _translate = QtCore.QCoreApplication.translate
        InformazioniEContatti.setWindowTitle(_translate("InformazioniEContatti", "Informazioni e contatti"))
        self.label_informazioni.setText(_translate("InformazioniEContatti", "Informazioni"))
        self.Text_informazioni.setPlainText(_translate("InformazioniEContatti", self.controller.get_informazioni()))
        self.label_contatti.setText(_translate("InformazioniEContatti", "Contatti"))
        self.Text_contatti.setPlainText(_translate("InformazioniEContatti", self.controller.get_contatti()))
        if self.utente_attivo.is_direttore:
            self.pushButton1.setText(_translate("InformazioniEContatti", "Aggiorna"))

    def aggiorna_informazioni_e_contatti_clicked(self, informazioni_aggiornate, contatti_aggiornati):
        self.controller.aggiorna_informazioni(informazioni_aggiornate)
        self.controller.aggiorna_contatti(contatti_aggiornati)


def show_vista_informazioni_e_contatti(utente_attivo):
    ui = Ui_InformazioniEContatti(utente_attivo)
    ui.setupUi(InformazioniEContatti)
    InformazioniEContatti.show()
    return ui


app = QtWidgets.QApplication(sys.argv)
InformazioniEContatti = QtWidgets.QWidget()
