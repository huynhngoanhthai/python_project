# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1356, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setEnabled(True)
        self.tab.setGeometry(QtCore.QRect(0, 0, 1341, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setBaseSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tab.setFont(font)
        self.tab.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setObjectName("tab")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.QLineAMaSV = QtWidgets.QLineEdit(self.Add)
        self.QLineAMaSV.setGeometry(QtCore.QRect(210, 100, 391, 20))
        self.QLineAMaSV.setObjectName("QLineAMaSV")
        self.QLineAHoSV = QtWidgets.QLineEdit(self.Add)
        self.QLineAHoSV.setGeometry(QtCore.QRect(210, 130, 391, 20))
        self.QLineAHoSV.setObjectName("QLineAHoSV")
        self.QLineATenSV = QtWidgets.QLineEdit(self.Add)
        self.QLineATenSV.setGeometry(QtCore.QRect(210, 160, 391, 20))
        self.QLineATenSV.setObjectName("QLineATenSV")
        self.OpNAM = QtWidgets.QRadioButton(self.Add)
        self.OpNAM.setGeometry(QtCore.QRect(210, 190, 82, 17))
        self.OpNAM.setObjectName("OpNAM")
        self.OpNU = QtWidgets.QRadioButton(self.Add)
        self.OpNU.setGeometry(QtCore.QRect(320, 190, 82, 17))
        self.OpNU.setObjectName("OpNU")
        self.QDateANS = QtWidgets.QDateEdit(self.Add)
        self.QDateANS.setGeometry(QtCore.QRect(210, 220, 391, 22))
        self.QDateANS.setDateTime(QtCore.QDateTime(QtCore.QDate(2001, 11, 4), QtCore.QTime(0, 0, 0)))
        self.QDateANS.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 11, 30), QtCore.QTime(23, 59, 59)))
        self.QDateANS.setMaximumDate(QtCore.QDate(2020, 11, 30))
        self.QDateANS.setDate(QtCore.QDate(2001, 11, 4))
        self.QDateANS.setObjectName("QDateANS")
        self.QLineADC = QtWidgets.QLineEdit(self.Add)
        self.QLineADC.setGeometry(QtCore.QRect(210, 250, 391, 20))
        self.QLineADC.setObjectName("QLineADC")
        self.QLineALop = QtWidgets.QLineEdit(self.Add)
        self.QLineALop.setGeometry(QtCore.QRect(210, 280, 391, 20))
        self.QLineALop.setObjectName("QLineALop")
        self.label_5 = QtWidgets.QLabel(self.Add)
        self.label_5.setGeometry(QtCore.QRect(150, 100, 47, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.Add)
        self.label_7.setGeometry(QtCore.QRect(150, 130, 47, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.Add)
        self.label_8.setGeometry(QtCore.QRect(150, 160, 47, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Add)
        self.label_9.setGeometry(QtCore.QRect(150, 190, 47, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Add)
        self.label_10.setGeometry(QtCore.QRect(150, 220, 51, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Add)
        self.label_11.setGeometry(QtCore.QRect(150, 250, 47, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Add)
        self.label_12.setGeometry(QtCore.QRect(150, 280, 47, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Add)
        self.label_13.setGeometry(QtCore.QRect(660, 110, 401, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.QButtonAAddStudent = QtWidgets.QPushButton(self.Add)
        self.QButtonAAddStudent.setGeometry(QtCore.QRect(210, 340, 75, 23))
        self.QButtonAAddStudent.setObjectName("QButtonAAddStudent")
        self.QButtonAClear = QtWidgets.QPushButton(self.Add)
        self.QButtonAClear.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.QButtonAClear.setObjectName("QButtonAClear")
        self.QLineAEmail = QtWidgets.QLineEdit(self.Add)
        self.QLineAEmail.setGeometry(QtCore.QRect(210, 310, 391, 20))
        self.QLineAEmail.setObjectName("QLineAEmail")
        self.label_17 = QtWidgets.QLabel(self.Add)
        self.label_17.setGeometry(QtCore.QRect(150, 310, 47, 21))
        self.label_17.setObjectName("label_17")
        self.tab.addTab(self.Add, "")
        self.Update = QtWidgets.QWidget()
        self.Update.setObjectName("Update")
        self.QButtonUUpdate = QtWidgets.QPushButton(self.Update)
        self.QButtonUUpdate.setGeometry(QtCore.QRect(240, 410, 75, 23))
        self.QButtonUUpdate.setObjectName("QButtonUUpdate")
        self.QButtonUClear = QtWidgets.QPushButton(self.Update)
        self.QButtonUClear.setGeometry(QtCore.QRect(390, 410, 75, 23))
        self.QButtonUClear.setObjectName("QButtonUClear")
        self.QTableUpdate = QtWidgets.QTableWidget(self.Update)
        self.QTableUpdate.setEnabled(False)
        self.QTableUpdate.setGeometry(QtCore.QRect(585, 150, 731, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QTableUpdate.sizePolicy().hasHeightForWidth())
        self.QTableUpdate.setSizePolicy(sizePolicy)
        self.QTableUpdate.setMinimumSize(QtCore.QSize(731, 20))
        self.QTableUpdate.setMaximumSize(QtCore.QSize(731, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.QTableUpdate.setFont(font)
        self.QTableUpdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableUpdate.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.QTableUpdate.setDragEnabled(True)
        self.QTableUpdate.setDragDropOverwriteMode(False)
        self.QTableUpdate.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.QTableUpdate.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.QTableUpdate.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.QTableUpdate.setGridStyle(QtCore.Qt.CustomDashLine)
        self.QTableUpdate.setRowCount(1)
        self.QTableUpdate.setObjectName("QTableUpdate")
        self.QTableUpdate.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableUpdate.setHorizontalHeaderItem(7, item)
        self.QTableUpdate.horizontalHeader().setDefaultSectionSize(85)
        self.QTableUpdate.horizontalHeader().setMinimumSectionSize(24)
        self.QTableUpdate.verticalHeader().setDefaultSectionSize(1)
        self.label = QtWidgets.QLabel(self.Update)
        self.label.setGeometry(QtCore.QRect(720, 120, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Update)
        self.label_2.setGeometry(QtCore.QRect(250, 120, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.QLineUMaSV = QtWidgets.QLineEdit(self.Update)
        self.QLineUMaSV.setGeometry(QtCore.QRect(240, 160, 311, 20))
        self.QLineUMaSV.setObjectName("QLineUMaSV")
        self.QLineUHoSV = QtWidgets.QLineEdit(self.Update)
        self.QLineUHoSV.setGeometry(QtCore.QRect(240, 190, 311, 20))
        self.QLineUHoSV.setObjectName("QLineUHoSV")
        self.QLineUTenSV = QtWidgets.QLineEdit(self.Update)
        self.QLineUTenSV.setGeometry(QtCore.QRect(240, 220, 311, 20))
        self.QLineUTenSV.setObjectName("QLineUTenSV")
        self.label_18 = QtWidgets.QLabel(self.Update)
        self.label_18.setGeometry(QtCore.QRect(180, 160, 47, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Update)
        self.label_19.setGeometry(QtCore.QRect(180, 190, 47, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.Update)
        self.label_20.setGeometry(QtCore.QRect(180, 220, 47, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Update)
        self.label_21.setGeometry(QtCore.QRect(180, 250, 47, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Update)
        self.label_22.setGeometry(QtCore.QRect(180, 280, 47, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.Update)
        self.label_23.setGeometry(QtCore.QRect(180, 310, 47, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.Update)
        self.label_24.setGeometry(QtCore.QRect(180, 340, 47, 21))
        self.label_24.setObjectName("label_24")
        self.OpUPhai = QtWidgets.QComboBox(self.Update)
        self.OpUPhai.setGeometry(QtCore.QRect(240, 250, 69, 22))
        self.OpUPhai.setObjectName("OpUPhai")
        self.OpUPhai.addItem("")
        self.OpUPhai.addItem("")
        self.QDateUNgaySinh = QtWidgets.QDateEdit(self.Update)
        self.QDateUNgaySinh.setGeometry(QtCore.QRect(240, 280, 91, 22))
        self.QDateUNgaySinh.setDateTime(QtCore.QDateTime(QtCore.QDate(2001, 11, 4), QtCore.QTime(0, 0, 0)))
        self.QDateUNgaySinh.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(23, 59, 59)))
        self.QDateUNgaySinh.setDate(QtCore.QDate(2001, 11, 4))
        self.QDateUNgaySinh.setObjectName("QDateUNgaySinh")
        self.QLineUNoiSinh = QtWidgets.QLineEdit(self.Update)
        self.QLineUNoiSinh.setGeometry(QtCore.QRect(240, 310, 311, 20))
        self.QLineUNoiSinh.setObjectName("QLineUNoiSinh")
        self.QLineULop = QtWidgets.QLineEdit(self.Update)
        self.QLineULop.setGeometry(QtCore.QRect(240, 340, 311, 20))
        self.QLineULop.setObjectName("QLineULop")
        self.label_25 = QtWidgets.QLabel(self.Update)
        self.label_25.setGeometry(QtCore.QRect(180, 370, 47, 21))
        self.label_25.setObjectName("label_25")
        self.QLineUEmail = QtWidgets.QLineEdit(self.Update)
        self.QLineUEmail.setGeometry(QtCore.QRect(240, 370, 311, 20))
        self.QLineUEmail.setObjectName("QLineUEmail")
        self.tab.addTab(self.Update, "")
        self.Delete = QtWidgets.QWidget()
        self.Delete.setObjectName("Delete")
        self.QButtonDClear = QtWidgets.QPushButton(self.Delete)
        self.QButtonDClear.setGeometry(QtCore.QRect(930, 90, 75, 23))
        self.QButtonDClear.setObjectName("QButtonDClear")
        self.QButtonDDelete = QtWidgets.QPushButton(self.Delete)
        self.QButtonDDelete.setGeometry(QtCore.QRect(840, 90, 75, 23))
        self.QButtonDDelete.setObjectName("QButtonDDelete")
        self.label_4 = QtWidgets.QLabel(self.Delete)
        self.label_4.setGeometry(QtCore.QRect(530, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.QTableDelete = QtWidgets.QTableWidget(self.Delete)
        self.QTableDelete.setEnabled(False)
        self.QTableDelete.setGeometry(QtCore.QRect(300, 130, 821, 351))
        self.QTableDelete.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.QTableDelete.setFont(font)
        self.QTableDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableDelete.setAutoScrollMargin(16)
        self.QTableDelete.setObjectName("QTableDelete")
        self.QTableDelete.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableDelete.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableDelete.setHorizontalHeaderItem(7, item)
        self.QTableDelete.horizontalHeader().setDefaultSectionSize(101)
        self.QTableDelete.horizontalHeader().setMinimumSectionSize(24)
        self.QTableDelete.verticalHeader().setDefaultSectionSize(1)
        self.label_3 = QtWidgets.QLabel(self.Delete)
        self.label_3.setGeometry(QtCore.QRect(646, 90, 31, 21))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.Delete)
        self.label_6.setGeometry(QtCore.QRect(340, 90, 71, 20))
        self.label_6.setObjectName("label_6")
        self.QLineDMaSV = QtWidgets.QLineEdit(self.Delete)
        self.QLineDMaSV.setGeometry(QtCore.QRect(420, 90, 161, 20))
        self.QLineDMaSV.setObjectName("QLineDMaSV")
        self.QLineDTenSV = QtWidgets.QLineEdit(self.Delete)
        self.QLineDTenSV.setGeometry(QtCore.QRect(680, 90, 151, 20))
        self.QLineDTenSV.setDragEnabled(False)
        self.QLineDTenSV.setReadOnly(False)
        self.QLineDTenSV.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.QLineDTenSV.setObjectName("QLineDTenSV")
        self.QButtonDClear.raise_()
        self.QButtonDDelete.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.QLineDMaSV.raise_()
        self.QLineDTenSV.raise_()
        self.QTableDelete.raise_()
        self.tab.addTab(self.Delete, "")
        self.ShowAll = QtWidgets.QWidget()
        self.ShowAll.setObjectName("ShowAll")
        self.label_14 = QtWidgets.QLabel(self.ShowAll)
        self.label_14.setGeometry(QtCore.QRect(360, 120, 71, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.ShowAll)
        self.label_15.setGeometry(QtCore.QRect(660, 120, 31, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.ShowAll)
        self.label_16.setGeometry(QtCore.QRect(510, 80, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.QLineSAMaSV = QtWidgets.QLineEdit(self.ShowAll)
        self.QLineSAMaSV.setGeometry(QtCore.QRect(440, 120, 161, 20))
        self.QLineSAMaSV.setObjectName("QLineSAMaSV")
        self.QLineSATenSV = QtWidgets.QLineEdit(self.ShowAll)
        self.QLineSATenSV.setGeometry(QtCore.QRect(690, 120, 151, 20))
        self.QLineSATenSV.setDragEnabled(False)
        self.QLineSATenSV.setReadOnly(False)
        self.QLineSATenSV.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.QLineSATenSV.setObjectName("QLineSATenSV")
        self.QButtonShowAll = QtWidgets.QPushButton(self.ShowAll)
        self.QButtonShowAll.setGeometry(QtCore.QRect(860, 120, 75, 23))
        self.QButtonShowAll.setObjectName("QButtonShowAll")
        self.QButtonSAClear = QtWidgets.QPushButton(self.ShowAll)
        self.QButtonSAClear.setGeometry(QtCore.QRect(960, 120, 75, 23))
        self.QButtonSAClear.setObjectName("QButtonSAClear")
        self.QTableShowAll = QtWidgets.QTableWidget(self.ShowAll)
        self.QTableShowAll.setGeometry(QtCore.QRect(280, 160, 821, 351))
        self.QTableShowAll.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.QTableShowAll.setFont(font)
        self.QTableShowAll.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QTableShowAll.setAutoScrollMargin(16)
        self.QTableShowAll.setObjectName("QTableShowAll")
        self.QTableShowAll.setColumnCount(8)
        self.QTableShowAll.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.QTableShowAll.setHorizontalHeaderItem(7, item)
        self.QTableShowAll.horizontalHeader().setDefaultSectionSize(101)
        self.QTableShowAll.horizontalHeader().setMinimumSectionSize(24)
        self.QTableShowAll.verticalHeader().setDefaultSectionSize(1)
        self.tab.addTab(self.ShowAll, "")
        self.QButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.QButtonBack.setGeometry(QtCore.QRect(1250, 600, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.QButtonBack.setFont(font)
        self.QButtonBack.setObjectName("QButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpNAM.setText(_translate("MainWindow", "NAM"))
        self.OpNU.setText(_translate("MainWindow", "NU"))
        self.QDateANS.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.label_5.setText(_translate("MainWindow", "MaSV"))
        self.label_7.setText(_translate("MainWindow", "HoSV"))
        self.label_8.setText(_translate("MainWindow", "TenSV"))
        self.label_9.setText(_translate("MainWindow", "Phai"))
        self.label_10.setText(_translate("MainWindow", "Ngai Sinh"))
        self.label_11.setText(_translate("MainWindow", "noi Sinh"))
        self.label_12.setText(_translate("MainWindow", "Lop"))
        self.label_13.setText(_translate("MainWindow", "password của Sinh trùng với MaSV"))
        self.QButtonAAddStudent.setText(_translate("MainWindow", "Add"))
        self.QButtonAClear.setText(_translate("MainWindow", "Clear"))
        self.label_17.setText(_translate("MainWindow", "Email"))
        self.tab.setTabText(self.tab.indexOf(self.Add), _translate("MainWindow", "Add"))
        self.QButtonUUpdate.setText(_translate("MainWindow", "Update"))
        self.QButtonUClear.setText(_translate("MainWindow", "Clear"))
        item = self.QTableUpdate.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaSV"))
        item = self.QTableUpdate.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HoSV"))
        item = self.QTableUpdate.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TenSV"))
        item = self.QTableUpdate.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PHAI"))
        item = self.QTableUpdate.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NGAY SINH"))
        item = self.QTableUpdate.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NOI SINH"))
        item = self.QTableUpdate.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "LOP"))
        item = self.QTableUpdate.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "EMAIL"))
        self.label.setText(_translate("MainWindow", "SUGGEST"))
        self.label_2.setText(_translate("MainWindow", "Press Enter for suggest"))
        self.label_18.setText(_translate("MainWindow", "MaSV"))
        self.label_19.setText(_translate("MainWindow", "HoSV"))
        self.label_20.setText(_translate("MainWindow", "TenSV"))
        self.label_21.setText(_translate("MainWindow", "Phai"))
        self.label_22.setText(_translate("MainWindow", "Ngay Sinh"))
        self.label_23.setText(_translate("MainWindow", "Noi Sinh"))
        self.label_24.setText(_translate("MainWindow", "Lop"))
        self.OpUPhai.setItemText(0, _translate("MainWindow", "NAM"))
        self.OpUPhai.setItemText(1, _translate("MainWindow", "NU"))
        self.QDateUNgaySinh.setDisplayFormat(_translate("MainWindow", "d/M/yyyy"))
        self.label_25.setText(_translate("MainWindow", "Email"))
        self.tab.setTabText(self.tab.indexOf(self.Update), _translate("MainWindow", "Update"))
        self.QButtonDClear.setText(_translate("MainWindow", "Clear"))
        self.QButtonDDelete.setText(_translate("MainWindow", "Delete"))
        self.label_4.setText(_translate("MainWindow", "Press Enter for suggest"))
        item = self.QTableDelete.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaSV"))
        item = self.QTableDelete.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HoSV"))
        item = self.QTableDelete.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TenSV"))
        item = self.QTableDelete.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phai"))
        item = self.QTableDelete.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NgaySinh"))
        item = self.QTableDelete.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NoiSinh"))
        item = self.QTableDelete.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TenLop"))
        item = self.QTableDelete.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "TEN"))
        self.label_6.setText(_translate("MainWindow", "MA SINH VIEN"))
        self.QLineDMaSV.setPlaceholderText(_translate("MainWindow", "MA SINH VIEN"))
        self.QLineDTenSV.setPlaceholderText(_translate("MainWindow", "TEN SINH VIEN"))
        self.tab.setTabText(self.tab.indexOf(self.Delete), _translate("MainWindow", "Delete"))
        self.label_14.setText(_translate("MainWindow", "MA SINH VIEN"))
        self.label_15.setText(_translate("MainWindow", "TEN"))
        self.label_16.setText(_translate("MainWindow", "Press Enter for suggest"))
        self.QLineSAMaSV.setPlaceholderText(_translate("MainWindow", "MA SINH VIEN"))
        self.QLineSATenSV.setPlaceholderText(_translate("MainWindow", "TEN SINH VIEN"))
        self.QButtonShowAll.setText(_translate("MainWindow", "Show"))
        self.QButtonSAClear.setText(_translate("MainWindow", "Clear"))
        item = self.QTableShowAll.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MaSV"))
        item = self.QTableShowAll.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HoSV"))
        item = self.QTableShowAll.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TenSV"))
        item = self.QTableShowAll.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phai"))
        item = self.QTableShowAll.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NgaySinh"))
        item = self.QTableShowAll.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NoiSinh"))
        item = self.QTableShowAll.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TenLop"))
        item = self.QTableShowAll.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Email"))
        self.tab.setTabText(self.tab.indexOf(self.ShowAll), _translate("MainWindow", "ShowAll"))
        self.QButtonBack.setText(_translate("MainWindow", "BACK"))
