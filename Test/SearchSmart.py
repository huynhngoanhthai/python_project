# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchSmart.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.KeyWord = QtWidgets.QLineEdit(self.centralwidget)
        self.KeyWord.setGeometry(QtCore.QRect(250, 170, 251, 20))
        self.KeyWord.setObjectName("KeyWord")
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(250, 450, 75, 23))
        self.Search.setObjectName("Search")
        self.TableStudent = QtWidgets.QTableWidget(self.centralwidget)
        self.TableStudent.setGeometry(QtCore.QRect(200, 210, 381, 192))
        self.TableStudent.setObjectName("TableStudent")
        self.TableStudent.setColumnCount(0)
        self.TableStudent.setRowCount(0)
        self.TableStudent.horizontalHeader().setCascadingSectionResizes(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.Search.setText(_translate("MainWindow", "Search"))
