# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAmin.ui'
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
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(60, 30, 731, 521))
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setObjectName("tab")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.Clear = QtWidgets.QPushButton(self.Add)
        self.Clear.setGeometry(QtCore.QRect(310, 300, 75, 23))
        self.Clear.setObjectName("Clear")
        self.AddClass = QtWidgets.QPushButton(self.Add)
        self.AddClass.setGeometry(QtCore.QRect(150, 300, 75, 23))
        self.AddClass.setObjectName("AddClass")
        self.ID_lop = QtWidgets.QLineEdit(self.Add)
        self.ID_lop.setGeometry(QtCore.QRect(150, 110, 231, 20))
        self.ID_lop.setObjectName("ID_lop")
        self.ten_lop = QtWidgets.QLineEdit(self.Add)
        self.ten_lop.setGeometry(QtCore.QRect(150, 150, 231, 20))
        self.ten_lop.setObjectName("ten_lop")
        self.ID_cau_hoi = QtWidgets.QLineEdit(self.Add)
        self.ID_cau_hoi.setGeometry(QtCore.QRect(150, 180, 231, 20))
        self.ID_cau_hoi.setObjectName("ID_cau_hoi")
        self.tab.addTab(self.Add, "")
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.UpdateClass = QtWidgets.QPushButton(self.Update)
        self.UpdateClass.setGeometry(QtCore.QRect(30, 220, 75, 23))
        self.UpdateClass.setObjectName("UpdateClass")
        self.Clear_update = QtWidgets.QPushButton(self.Update)
        self.Clear_update.setGeometry(QtCore.QRect(250, 220, 75, 23))
        self.Clear_update.setObjectName("Clear_update")
        self.Suggest = QtWidgets.QTableWidget(self.Update)
        self.Suggest.setGeometry(QtCore.QRect(365, 80, 221, 192))
        self.Suggest.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Suggest.setObjectName("Suggest")
        self.Suggest.setColumnCount(2)
        self.Suggest.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Suggest.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Suggest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Suggest.setHorizontalHeaderItem(1, item)
        self.ID_lop_2 = QtWidgets.QLineEdit(self.Update)
        self.ID_lop_2.setGeometry(QtCore.QRect(30, 90, 301, 20))
        self.ID_lop_2.setObjectName("ID_lop_2")
        self.Ten_lop_update = QtWidgets.QLineEdit(self.Update)
        self.Ten_lop_update.setGeometry(QtCore.QRect(30, 130, 301, 20))
        self.Ten_lop_update.setObjectName("Ten_lop_update")
        self.ID_cau_hoi_update = QtWidgets.QLineEdit(self.Update)
        self.ID_cau_hoi_update.setGeometry(QtCore.QRect(30, 170, 301, 20))
        self.ID_cau_hoi_update.setObjectName("ID_cau_hoi_update")
        self.tab.addTab(self.Update, "")
        self.Delete = QtWidgets.QWidget()
        self.Delete.setObjectName("Delete")
        self.tab.addTab(self.Delete, "")
        self.ShowAll = QtWidgets.QWidget()
        self.ShowAll.setObjectName("ShowAll")
        self.tab.addTab(self.ShowAll, "")
        self.AddStudent = QtWidgets.QWidget()
        self.AddStudent.setObjectName("AddStudent")
        self.tab.addTab(self.AddStudent, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.AddClass.setText(_translate("MainWindow", "Add"))
        self.ID_lop.setPlaceholderText(_translate("MainWindow", "ID_lop"))
        self.ten_lop.setPlaceholderText(_translate("MainWindow", "ten_lop"))
        self.ID_cau_hoi.setPlaceholderText(_translate("MainWindow", "ID_cau_hoi"))
        self.tab.setTabText(self.tab.indexOf(self.Add), _translate("MainWindow", "Add"))
        self.UpdateClass.setText(_translate("MainWindow", "Update"))
        self.Clear_update.setText(_translate("MainWindow", "Clear"))
        item = self.Suggest.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Suggest.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID_lop"))
        item = self.Suggest.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ten_lop"))
        self.tab.setTabText(self.tab.indexOf(self.Update), _translate("MainWindow", "Update"))
        self.tab.setTabText(self.tab.indexOf(self.Delete), _translate("MainWindow", "Delete"))
        self.tab.setTabText(self.tab.indexOf(self.ShowAll), _translate("MainWindow", "ShowAll"))
        self.tab.setTabText(self.tab.indexOf(self.AddStudent), _translate("MainWindow", "AddStudent"))
