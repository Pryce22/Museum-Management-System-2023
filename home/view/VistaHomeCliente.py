import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VistaHomeCliente(object):
    def setupUi(self, VistaHomeCliente):
        VistaHomeCliente.setObjectName("VistaHomeCliente")
        VistaHomeCliente.resize(400, 281)
        self.pushButton_1 = QtWidgets.QPushButton(VistaHomeCliente)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 0, 200, 140))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(VistaHomeCliente)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 140, 200, 140))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(VistaHomeCliente)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 0, 200, 140))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(VistaHomeCliente)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 140, 200, 140))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(VistaHomeCliente)
        QtCore.QMetaObject.connectSlotsByName(VistaHomeCliente)

    def retranslateUi(self, VistaHomeCliente):
        _translate = QtCore.QCoreApplication.translate
        VistaHomeCliente.setWindowTitle(_translate("VistaHomeCliente", "Form"))
        self.pushButton_1.setText(_translate("VistaHomeCliente", "Utente"))
        self.pushButton_2.setText(_translate("VistaHomeCliente", "Beni"))
        self.pushButton_3.setText(_translate("VistaHomeCliente", "Prenotazioni"))
        self.pushButton_4.setText(_translate("VistaHomeCliente", "Informazioni e contatti"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    VistaHomeCliente = QtWidgets.QWidget()
    ui = Ui_VistaHomeCliente()
    ui.setupUi(VistaHomeCliente)
    VistaHomeCliente.show()
    sys.exit(app.exec_())

