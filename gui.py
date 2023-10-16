# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 324)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_config_name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_config_name.setObjectName("lineEdit_config_name")
        self.gridLayout_3.addWidget(self.lineEdit_config_name, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_Interface = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Interface.setObjectName("groupBox_Interface")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_Interface)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_Interface)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_Interface)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_Interface)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_Address_1 = QtWidgets.QLineEdit(self.groupBox_Interface)
        self.lineEdit_Address_1.setObjectName("lineEdit_Address_1")
        self.gridLayout.addWidget(self.lineEdit_Address_1, 1, 1, 1, 1)
        self.lineEdit_Address_2 = QtWidgets.QLineEdit(self.groupBox_Interface)
        self.lineEdit_Address_2.setObjectName("lineEdit_Address_2")
        self.gridLayout.addWidget(self.lineEdit_Address_2, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_Interface)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_DNS = QtWidgets.QLineEdit(self.groupBox_Interface)
        self.lineEdit_DNS.setObjectName("lineEdit_DNS")
        self.gridLayout.addWidget(self.lineEdit_DNS, 2, 1, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_Interface, 1, 0, 1, 1)
        self.groupBox_Peer_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Peer_2.setObjectName("groupBox_Peer_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Peer_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_Peer_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_PublicKey = QtWidgets.QLineEdit(self.groupBox_Peer_2)
        self.lineEdit_PublicKey.setObjectName("lineEdit_PublicKey")
        self.gridLayout_2.addWidget(self.lineEdit_PublicKey, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_Peer_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_AllowedIPs = QtWidgets.QLineEdit(self.groupBox_Peer_2)
        self.lineEdit_AllowedIPs.setObjectName("lineEdit_AllowedIPs")
        self.gridLayout_2.addWidget(self.lineEdit_AllowedIPs, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_Peer_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_Endpoint = QtWidgets.QLineEdit(self.groupBox_Peer_2)
        self.lineEdit_Endpoint.setObjectName("lineEdit_Endpoint")
        self.gridLayout_2.addWidget(self.lineEdit_Endpoint, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_Peer_2, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 3, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Имя конфигурации:"))
        self.groupBox_Interface.setTitle(_translate("MainWindow", "[Interface]"))
        self.label_3.setText(_translate("MainWindow", "PrivateKey = "))
        self.label_4.setText(_translate("MainWindow", "Address = "))
        self.label_5.setText(_translate("MainWindow", "DNS = "))
        self.groupBox_Peer_2.setTitle(_translate("MainWindow", "[Peer]"))
        self.label_6.setText(_translate("MainWindow", "PublicKey = "))
        self.label_7.setText(_translate("MainWindow", "AllowedIPs = "))
        self.label_8.setText(_translate("MainWindow", "Endpoint = "))
        self.pushButton.setText(_translate("MainWindow", "Создать конфиг"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())