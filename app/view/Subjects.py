# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Subjects.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1614, 922)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setEnabled(True)
        self.tab.setGeometry(QtCore.QRect(370, 250, 1181, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMinimumSize(QtCore.QSize(20, 20))
        self.tab.setBaseSize(QtCore.QSize(1000, 1000))
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setObjectName("tab")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.QLineAMaMH = QtWidgets.QLineEdit(self.Add)
        self.QLineAMaMH.setGeometry(QtCore.QRect(520, 160, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QLineAMaMH.setFont(font)
        self.QLineAMaMH.setObjectName("QLineAMaMH")
        self.QLineATenMH = QtWidgets.QLineEdit(self.Add)
        self.QLineATenMH.setGeometry(QtCore.QRect(520, 230, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QLineATenMH.setFont(font)
        self.QLineATenMH.setObjectName("QLineATenMH")
        self.QButtonAAdd = QtWidgets.QPushButton(self.Add)
        self.QButtonAAdd.setGeometry(QtCore.QRect(540, 390, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QButtonAAdd.setFont(font)
        self.QButtonAAdd.setObjectName("QButtonAAdd")
        self.QButtonAClear = QtWidgets.QPushButton(self.Add)
        self.QButtonAClear.setGeometry(QtCore.QRect(710, 390, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QButtonAClear.setFont(font)
        self.QButtonAClear.setObjectName("QButtonAClear")
        self.QBoxASoTiet = QtWidgets.QSpinBox(self.Add)
        self.QBoxASoTiet.setGeometry(QtCore.QRect(520, 300, 42, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QBoxASoTiet.setFont(font)
        self.QBoxASoTiet.setObjectName("QBoxASoTiet")
        self.label_5 = QtWidgets.QLabel(self.Add)
        self.label_5.setGeometry(QtCore.QRect(410, 160, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.Add)
        self.label_7.setGeometry(QtCore.QRect(410, 230, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Add)
        self.label_8.setGeometry(QtCore.QRect(410, 300, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Add)
        self.label_9.setGeometry(QtCore.QRect(490, 60, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tab.addTab(self.Add, "")
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.QButtonUUpdate = QtWidgets.QPushButton(self.Update)
        self.QButtonUUpdate.setGeometry(QtCore.QRect(320, 340, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonUUpdate.setFont(font)
        self.QButtonUUpdate.setObjectName("QButtonUUpdate")
        self.QButtonUClear = QtWidgets.QPushButton(self.Update)
        self.QButtonUClear.setGeometry(QtCore.QRect(430, 340, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonUClear.setFont(font)
        self.QButtonUClear.setObjectName("QButtonUClear")
        self.QTableUpdate = QtWidgets.QTableWidget(self.Update)
        self.QTableUpdate.setEnabled(True)
        self.QTableUpdate.setGeometry(QtCore.QRect(665, 140, 401, 291))
        self.QTableUpdate.setMinimumSize(QtCore.QSize(10, 20))
        self.QTableUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableUpdate.setAutoScrollMargin(16)
        self.QTableUpdate.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.QTableUpdate.setDragEnabled(True)
        self.QTableUpdate.setDragDropOverwriteMode(False)
        self.QTableUpdate.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.QTableUpdate.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.QTableUpdate.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.QTableUpdate.setGridStyle(QtCore.Qt.CustomDashLine)
        self.QTableUpdate.setObjectName("QTableUpdate")
        self.QTableUpdate.setColumnCount(3)
        self.QTableUpdate.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(2, item)
        self.QTableUpdate.horizontalHeader().setDefaultSectionSize(85)
        self.QTableUpdate.horizontalHeader().setMinimumSectionSize(24)
        self.QTableUpdate.verticalHeader().setDefaultSectionSize(1)
        self.label = QtWidgets.QLabel(self.Update)
        self.label.setGeometry(QtCore.QRect(800, 90, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Update)
        self.label_2.setGeometry(QtCore.QRect(330, 110, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.QLineUMaMH = QtWidgets.QLineEdit(self.Update)
        self.QLineUMaMH.setGeometry(QtCore.QRect(300, 170, 311, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUMaMH.setFont(font)
        self.QLineUMaMH.setObjectName("QLineUMaMH")
        self.QLineUTenMH = QtWidgets.QLineEdit(self.Update)
        self.QLineUTenMH.setGeometry(QtCore.QRect(300, 220, 311, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineUTenMH.setFont(font)
        self.QLineUTenMH.setObjectName("QLineUTenMH")
        self.label_18 = QtWidgets.QLabel(self.Update)
        self.label_18.setGeometry(QtCore.QRect(180, 170, 85, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Update)
        self.label_19.setGeometry(QtCore.QRect(180, 220, 85, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Update)
        self.label_20.setGeometry(QtCore.QRect(180, 270, 85, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.QBoxUSoTiet = QtWidgets.QSpinBox(self.Update)
        self.QBoxUSoTiet.setGeometry(QtCore.QRect(300, 270, 42, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QBoxUSoTiet.setFont(font)
        self.QBoxUSoTiet.setObjectName("QBoxUSoTiet")
        self.tab.addTab(self.Update, "")
        self.Delete = QtWidgets.QWidget()
        self.Delete.setObjectName("Delete")
        self.QButtonDClear = QtWidgets.QPushButton(self.Delete)
        self.QButtonDClear.setGeometry(QtCore.QRect(920, 130, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonDClear.setFont(font)
        self.QButtonDClear.setObjectName("QButtonDClear")
        self.QButtonDDelete = QtWidgets.QPushButton(self.Delete)
        self.QButtonDDelete.setGeometry(QtCore.QRect(920, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonDDelete.setFont(font)
        self.QButtonDDelete.setObjectName("QButtonDDelete")
        self.label_4 = QtWidgets.QLabel(self.Delete)
        self.label_4.setGeometry(QtCore.QRect(480, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.QTableDelete = QtWidgets.QTableWidget(self.Delete)
        self.QTableDelete.setEnabled(True)
        self.QTableDelete.setGeometry(QtCore.QRect(420, 120, 381, 351))
        self.QTableDelete.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.QTableDelete.setFont(font)
        self.QTableDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableDelete.setAutoScrollMargin(16)
        self.QTableDelete.setObjectName("QTableDelete")
        self.QTableDelete.setColumnCount(3)
        self.QTableDelete.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(2, item)
        self.QTableDelete.horizontalHeader().setDefaultSectionSize(101)
        self.QTableDelete.horizontalHeader().setMinimumSectionSize(24)
        self.QTableDelete.verticalHeader().setDefaultSectionSize(1)
        self.label_3 = QtWidgets.QLabel(self.Delete)
        self.label_3.setGeometry(QtCore.QRect(560, 90, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.Delete)
        self.label_6.setGeometry(QtCore.QRect(230, 90, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.QLineDMaMH = QtWidgets.QLineEdit(self.Delete)
        self.QLineDMaMH.setGeometry(QtCore.QRect(380, 90, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineDMaMH.setFont(font)
        self.QLineDMaMH.setObjectName("QLineDMaMH")
        self.QLineDTenMH = QtWidgets.QLineEdit(self.Delete)
        self.QLineDTenMH.setGeometry(QtCore.QRect(720, 90, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QLineDTenMH.setFont(font)
        self.QLineDTenMH.setDragEnabled(False)
        self.QLineDTenMH.setReadOnly(False)
        self.QLineDTenMH.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.QLineDTenMH.setObjectName("QLineDTenMH")
        self.QButtonDClear.raise_()
        self.QButtonDDelete.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.QLineDMaMH.raise_()
        self.QLineDTenMH.raise_()
        self.QTableDelete.raise_()
        self.tab.addTab(self.Delete, "")
        self.QButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.QButtonBack.setGeometry(QtCore.QRect(1370, 810, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QButtonBack.setFont(font)
        self.QButtonBack.setObjectName("QButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1614, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.QButtonUClear, self.QTableUpdate)
        MainWindow.setTabOrder(self.QTableUpdate, self.QLineUMaMH)
        MainWindow.setTabOrder(self.QLineUMaMH, self.QLineUTenMH)
        MainWindow.setTabOrder(self.QLineUTenMH, self.QButtonDClear)
        MainWindow.setTabOrder(self.QButtonDClear, self.QBoxUSoTiet)
        MainWindow.setTabOrder(self.QBoxUSoTiet, self.QButtonDDelete)
        MainWindow.setTabOrder(self.QButtonDDelete, self.QTableDelete)
        MainWindow.setTabOrder(self.QTableDelete, self.QLineDMaMH)
        MainWindow.setTabOrder(self.QLineDMaMH, self.QLineDTenMH)
        MainWindow.setTabOrder(self.QLineDTenMH, self.QButtonUUpdate)
        MainWindow.setTabOrder(self.QButtonUUpdate, self.QLineAMaMH)
        MainWindow.setTabOrder(self.QLineAMaMH, self.QLineATenMH)
        MainWindow.setTabOrder(self.QLineATenMH, self.QButtonAAdd)
        MainWindow.setTabOrder(self.QButtonAAdd, self.QButtonAClear)
        MainWindow.setTabOrder(self.QButtonAClear, self.QBoxASoTiet)
        MainWindow.setTabOrder(self.QBoxASoTiet, self.tab)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QButtonAAdd.setText(_translate("MainWindow", "Add"))
        self.QButtonAClear.setText(_translate("MainWindow", "Clear"))
        self.label_5.setText(_translate("MainWindow", "MaMH"))
        self.label_7.setText(_translate("MainWindow", "TenMH"))
        self.label_8.setText(_translate("MainWindow", "SoTiet"))
        self.label_9.setText(_translate("MainWindow", "THEM MON HOC"))
        self.tab.setTabText(self.tab.indexOf(self.Add), _translate("MainWindow", "Add"))
        self.QButtonUUpdate.setText(_translate("MainWindow", "Update"))
        self.QButtonUClear.setText(_translate("MainWindow", "Clear"))
        item = self.QTableUpdate.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaMH"))
        item = self.QTableUpdate.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TenMH"))
        item = self.QTableUpdate.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SoTiet"))
        self.label.setText(_translate("MainWindow", "SUGGEST"))
        self.label_2.setText(_translate("MainWindow", "Press Enter For Suggest"))
        self.label_18.setText(_translate("MainWindow", "MaMH"))
        self.label_19.setText(_translate("MainWindow", "TenMH"))
        self.label_20.setText(_translate("MainWindow", "SoTiet"))
        self.tab.setTabText(self.tab.indexOf(self.Update), _translate("MainWindow", "Update"))
        self.QButtonDClear.setText(_translate("MainWindow", "Clear"))
        self.QButtonDDelete.setText(_translate("MainWindow", "Delete"))
        self.label_4.setText(_translate("MainWindow", "Press Enter For Suggest"))
        item = self.QTableDelete.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaMH"))
        item = self.QTableDelete.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TenMH"))
        item = self.QTableDelete.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "SoTiet"))
        self.label_3.setText(_translate("MainWindow", "TEN MON HOC"))
        self.label_6.setText(_translate("MainWindow", "MA MON HOC"))
        self.QLineDMaMH.setPlaceholderText(_translate("MainWindow", "Ma Mon Hoc"))
        self.QLineDTenMH.setPlaceholderText(_translate("MainWindow", "Ten Mon Hoc"))
        self.tab.setTabText(self.tab.indexOf(self.Delete), _translate("MainWindow", "Delete"))
        self.QButtonBack.setText(_translate("MainWindow", "BACK TO LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
