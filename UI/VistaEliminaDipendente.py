# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VistaEliminaDipendente.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VistaEliminaDipendente(object):
    def setupUi(self, VistaEliminaDipendente):
        VistaEliminaDipendente.setObjectName("VistaEliminaDipendente")
        VistaEliminaDipendente.resize(300, 180)
        self.label = QtWidgets.QLabel(VistaEliminaDipendente)
        self.label.setGeometry(QtCore.QRect(50, 30, 207, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(VistaEliminaDipendente)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 100, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(VistaEliminaDipendente)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 120, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(VistaEliminaDipendente)
        QtCore.QMetaObject.connectSlotsByName(VistaEliminaDipendente)

    def retranslateUi(self, VistaEliminaDipendente):
        _translate = QtCore.QCoreApplication.translate
        VistaEliminaDipendente.setWindowTitle(_translate("VistaEliminaDipendente", "Elimina dipendente"))
        self.label.setText(_translate("VistaEliminaDipendente", "Dipendente da eliminare:"))
        self.pushButton.setText(_translate("VistaEliminaDipendente", "Elimina"))
        self.lineEdit.setPlaceholderText(_translate("VistaEliminaDipendente", "email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VistaEliminaDipendente = QtWidgets.QWidget()
    ui = Ui_VistaEliminaDipendente()
    ui.setupUi(VistaEliminaDipendente)
    VistaEliminaDipendente.show()
    sys.exit(app.exec_())
