# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeTeacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 599)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        MainWindow.setDockNestingEnabled(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NAMEGV = QtWidgets.QLabel(self.centralwidget)
        self.NAMEGV.setGeometry(QtCore.QRect(360, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.NAMEGV.setFont(font)
        self.NAMEGV.setObjectName("NAMEGV")
        self.QButtonSV = QtWidgets.QPushButton(self.centralwidget)
        self.QButtonSV.setGeometry(QtCore.QRect(260, 190, 211, 23))
        self.QButtonSV.setObjectName("QButtonSV")
        self.QButtonMH = QtWidgets.QPushButton(self.centralwidget)
        self.QButtonMH.setGeometry(QtCore.QRect(260, 220, 211, 23))
        self.QButtonMH.setObjectName("QButtonMH")
        self.QButtonCH = QtWidgets.QPushButton(self.centralwidget)
        self.QButtonCH.setGeometry(QtCore.QRect(260, 250, 211, 23))
        self.QButtonCH.setObjectName("QButtonCH")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label.setText(_translate("MainWindow", "welcom "))
        self.NAMEGV.setText(_translate("MainWindow", "GIAO VIEN"))
        self.QButtonSV.setText(_translate("MainWindow", "Thêm SV"))
        self.QButtonMH.setText(_translate("MainWindow", "Thêm môn học"))
        self.QButtonCH.setText(_translate("MainWindow", "thêm câu hỏi"))
