# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'see2.ui'
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
        self.test = QtWidgets.QStackedWidget(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(0, 0, 921, 641))
        self.test.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.test.setObjectName("test")
        self.page1 = QtWidgets.QWidget()
        self.page1.setEnabled(True)
        self.page1.setObjectName("page1")
        self.question = QtWidgets.QLabel(self.page1)
        self.question.setGeometry(QtCore.QRect(90, 70, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.question.setFont(font)
        self.question.setObjectName("question")
        self.A = QtWidgets.QRadioButton(self.page1)
        self.A.setGeometry(QtCore.QRect(90, 210, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A.setFont(font)
        self.A.setObjectName("A")
        self.B = QtWidgets.QRadioButton(self.page1)
        self.B.setGeometry(QtCore.QRect(90, 280, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B.setFont(font)
        self.B.setObjectName("B")
        self.C = QtWidgets.QRadioButton(self.page1)
        self.C.setGeometry(QtCore.QRect(90, 350, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C.setFont(font)
        self.C.setObjectName("C")
        self.D = QtWidgets.QRadioButton(self.page1)
        self.D.setGeometry(QtCore.QRect(90, 420, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D.setFont(font)
        self.D.setObjectName("D")
        self.test.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.C_2 = QtWidgets.QRadioButton(self.page2)
        self.C_2.setGeometry(QtCore.QRect(90, 350, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_2.setFont(font)
        self.C_2.setObjectName("C_2")
        self.D_2 = QtWidgets.QRadioButton(self.page2)
        self.D_2.setGeometry(QtCore.QRect(90, 420, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_2.setFont(font)
        self.D_2.setObjectName("D_2")
        self.question_2 = QtWidgets.QLabel(self.page2)
        self.question_2.setGeometry(QtCore.QRect(90, 70, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.question_2.setFont(font)
        self.question_2.setObjectName("question_2")
        self.A_2 = QtWidgets.QRadioButton(self.page2)
        self.A_2.setGeometry(QtCore.QRect(90, 210, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_2.setFont(font)
        self.A_2.setObjectName("A_2")
        self.B_2 = QtWidgets.QRadioButton(self.page2)
        self.B_2.setGeometry(QtCore.QRect(90, 280, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_2.setFont(font)
        self.B_2.setObjectName("B_2")
        self.test.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.C_3 = QtWidgets.QRadioButton(self.page3)
        self.C_3.setGeometry(QtCore.QRect(90, 350, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C_3.setFont(font)
        self.C_3.setObjectName("C_3")
        self.A_3 = QtWidgets.QRadioButton(self.page3)
        self.A_3.setGeometry(QtCore.QRect(90, 210, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A_3.setFont(font)
        self.A_3.setObjectName("A_3")
        self.D_3 = QtWidgets.QRadioButton(self.page3)
        self.D_3.setGeometry(QtCore.QRect(90, 420, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.D_3.setFont(font)
        self.D_3.setObjectName("D_3")
        self.question_3 = QtWidgets.QLabel(self.page3)
        self.question_3.setGeometry(QtCore.QRect(90, 70, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.question_3.setFont(font)
        self.question_3.setObjectName("question_3")
        self.B_3 = QtWidgets.QRadioButton(self.page3)
        self.B_3.setGeometry(QtCore.QRect(90, 280, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_3.setFont(font)
        self.B_3.setObjectName("B_3")
        self.test.addWidget(self.page3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.test.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.question.setText(_translate("MainWindow", "Câu 1: Ai là abc?"))
        self.A.setText(_translate("MainWindow", "A. bcd"))
        self.B.setText(_translate("MainWindow", "B. aab"))
        self.C.setText(_translate("MainWindow", "C. dca"))
        self.D.setText(_translate("MainWindow", "D. xyz"))
        self.C_2.setText(_translate("MainWindow", "C. ajs"))
        self.D_2.setText(_translate("MainWindow", "D. znx"))
        self.question_2.setText(_translate("MainWindow", "Câu 2: Cái gì là ijk?"))
        self.A_2.setText(_translate("MainWindow", "A. mno"))
        self.B_2.setText(_translate("MainWindow", "B. qyt"))
        self.C_3.setText(_translate("MainWindow", "C. dca"))
        self.A_3.setText(_translate("MainWindow", "A. bcd"))
        self.D_3.setText(_translate("MainWindow", "D. xyz"))
        self.question_3.setText(_translate("MainWindow", "Câu 3: Ai là 123456?"))
        self.B_3.setText(_translate("MainWindow", "B. aab"))
