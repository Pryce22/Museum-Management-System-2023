# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaInformazioniEContattiDipendente.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InformazioniEContattiDipendente(object):
    def setupUi(self, InformazioniEContattiDipendente):
        InformazioniEContattiDipendente.setObjectName("InformazioniEContattiDipendente")
        InformazioniEContattiDipendente.resize(898, 557)
        self.verticalLayoutWidget = QtWidgets.QWidget(InformazioniEContattiDipendente)
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
        '''if utente_attivo.is_direttore = False:
            self.Text_informazioni.setReadOnly(True)'''
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
        '''if utente_attivo.is_direttore = False:
            self.Text_informazioni.setReadOnly(True)'''
        self.Text_contatti.setObjectName("Text_contatti")
        self.verticalLayout.addWidget(self.Text_contatti)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(InformazioniEContattiDipendente)
        QtCore.QMetaObject.connectSlotsByName(InformazioniEContattiDipendente)

    def retranslateUi(self, InformazioniEContattiDipendente):
        _translate = QtCore.QCoreApplication.translate
        InformazioniEContattiDipendente.setWindowTitle(_translate("InformazioniEContattiDipendente", "Informazioni e contatti"))
        self.label_informazioni.setText(_translate("InformazioniEContattiDipendente", "Informazioni"))
        self.Text_informazioni.setPlainText(_translate("InformazioniEContattiDipendente", "Orari di apertura:\n"
"Il museo è aperto e disponibile tutti i giorni dalle 8:30 alle 19:30"))
        self.label_contatti.setText(_translate("InformazioniEContattiDipendente", "Contatti"))
        self.Text_contatti.setPlainText(_translate("InformazioniEContattiDipendente", "Angjelo Libofsha -  S11048126@studenti.univpm.it\n"
"Valerio Crocetti   -  S1103351@studenti.univpm.it\n"
"Matteo Colletta   -  S1105265@studenti.univpm.it"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InformazioniEContattiDipendente = QtWidgets.QWidget()
    ui = Ui_InformazioniEContattiDipendente()
    ui.setupUi(InformazioniEContattiDipendente)
    InformazioniEContattiDipendente.show()
    sys.exit(app.exec_())