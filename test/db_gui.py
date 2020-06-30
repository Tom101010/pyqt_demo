# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from test.db import create_db

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ld_db_create = QtWidgets.QLineEdit(self.centralwidget)
        self.ld_db_create.setGeometry(QtCore.QRect(320, 180, 241, 51))
        self.ld_db_create.setObjectName("ld_db_create")
        self.btn_db_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_db_create.setGeometry(QtCore.QRect(310, 260, 112, 34))
        self.btn_db_create.setObjectName("btn_db_create")
        ###############################
        self.btn_db_create.clicked.connect(lambda : create_db(self.ld_db_create.text()))
        ###############################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_db_create.setText(_translate("MainWindow", "Create"))
        self.ld_db_create.setText(_translate("MainWindow", "DataBase Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

