import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from PyQt5 import QtWidgets
import mysql.connector as sql
#import file
import view.Login as Login
import view.HomeAdmin as HomeAdmin
from database import myDB
from messageBox import MBox


# class MainWindow:
#     def __init__(self):
#         self.main_win = QMainWindow()
#         self.uic = Ui_MainWindow()
#         self.uic.setupUi(self.main_win)
#         # code
#         self.uic.login.clicked.connect(self.login)
#         self.uic.password.returnPressed.connect(self.login)
#         self.uic.seePassword.clicked.connect(self.checkPassword)
#     # Login User

#     def login(self):
#         try:
#             cur = myDB.cursor()
#             getUname = self.uic.uname.text().strip()
#             getPassword = self.uic.password.text()
#             cur.execute(
#                 "SELECT * FROM User WHERE mssv=%s AND password=%s", (getUname, getPassword))
#             result = cur.fetchall()
#             if(result == []):
#                 MBox(0, 'ERROR', "uname or password wrong", 16)
#             elif result[0][-1] == "TEACHER":
#                 showHomeAdmin(self)
#             else:
#                 # for role = students
#                 print("123")
#         except sql.Error as e:
#             MBox(0, "Error", str(e), 32)

#     def checkPassword(self):
#         return checkSeePassword(self)

#     # Home Admin
#     def clearContents(self):
#         return clearContentsInHomeAdmin(self)

#     def addClass(self):
#         return addClassInHomeAdmin(self)
#     # Update Class

#     def updateClass(self):
#         return updateClassInHomeAdmin(self)

#     def clearContentsUpdateClass(self):
#         return clearContentsUpdateInHomeAdmin(self)
#     # func Suggest where press Enter

#     def PressEnterSuggestion(self):
#         try:
#             cur = myDB.cursor()
#             idLop = self.uic.ID_lop_update.text().strip()
#             query = "SELECT * FROM lop WHERE ID_lop LIKE '%{}%' LIMIT 4".format(
#                 idLop)
#             cur.execute(query)
#             result = cur.fetchall()
#             self.uic.Suggest.setColumnCount(2)
#             self.uic.Suggest.setRowCount(5)
#             columns = 0
#             for row in result:
#                 self.uic.Suggest.setItem(columns, 0, QTableWidgetItem(row[0]))
#                 self.uic.Suggest.setItem(columns, 1, QTableWidgetItem(row[1]))
#                 columns += 1
#         except sql.Error as e:
#             MBox(0, "Error", str(e), 32)
#     # code Default

#     def show(self):
#         self.main_win.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_win = MainWindow()
#     main_win.show()
#     sys.exit(app.exec())


def mainUi():
    global ui
    ui = Login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.login.clicked.connect(loginUser)
    ui.password.returnPressed.connect(loginUser)
    ui.seePassword.clicked.connect(checkPassword)


def loginUser():
    try:
        cur = myDB.cursor()
        getUname = ui.uname.text().strip()  # GT
        print(getUname[0:2])
        getPassword = ui.password.text()
        cur.execute("SELECT * FROM User WHERE mssv=%s AND password=%s",
                    (getUname, getPassword))
        result = cur.fetchall()
        if(result == []):
            MBox(0, 'ERROR', "uname or password wrong", 16)
        elif result[0][-1] == "TEACHER":
            # showHomeAdmin
            showHomeAdmin()
        else:
            # showHomeStudent
            print("123")
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)


def checkPassword():
    if ui.seePassword.isChecked():
        ui.password.setEchoMode(QLineEdit.Normal)
    else:
        ui.password.setEchoMode(QLineEdit.Password)


def showHomeAdmin():
    global ui
    ui = HomeAdmin.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.tab.setCurrentWidget(ui.Add)
    # add
    ui.Clear.clicked.connect(clearContents)
    ui.AddClass.clicked.connect(addClass)
    # Update
    ui.UpdateClass.clicked.connect(updateClass)
    ui.ID_lop_update.returnPressed.connect(PressEnterSuggestion)
    ui.Clear_update.clicked.connect(clearContentsUpdateClass)
    # Delete


def clearContents():
    ui.ID_lop.setText("")
    ui.ID_cau_hoi.setText("")
    ui.ten_lop.setText("")

# -------------------addbbdsuus---------------------------------------------


def addClass():
    try:
        idLop = ui.ID_lop.text().strip()
        if(idLop == ''):
            return MBox(0, "Error", "ID lop khong duoc rong", 16)
        tenLop = ui.ten_lop.text().strip()
        if(tenLop == ''):
            return MBox(0, "Error", "ID ten Lop khong duoc rong", 16)
        cur = myDB.cursor()
        query = "INSERT INTO lop (ID_lop, ten_lop) VALUES (%s, %s)"
        cur.execute(query, (idLop, tenLop))
        myDB.commit()
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)


def clearContentsUpdateClass():
    ui.ID_lop_update.setText("")
    ui.ten_lop_update.setText("")
    # comment test


def updateClass():
    try:
        idLop = ui.ID_lop_update.text().strip()
        if(idLop == ''):
            return MBox(0, "Error", "ID lop khong duoc rong", 16)
        tenLop = ui.ten_lop_update.text()
        if(tenLop == ''):
            return MBox(0, "Error", "ten Lop khong duoc rong", 16)
        cur = myDB.cursor()
        query = "UPDATE lop SET ten_lop = '{}' WHERE ID_lop = '{}'".format(
            tenLop, idLop)

        cur.execute(query)
        MBox(0, "Successfully",
             "you updated ID_lop = {}, ten_lop = {}".format(idLop, tenLop), 64)
        myDB.commit()
        clearContentsUpdateClass()
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)


def PressEnterSuggestion():
    try:
        cur = myDB.cursor()
        idLop = ui.ID_lop_update.text().strip().upper()
        query = "SELECT * FROM lop WHERE ID_lop LIKE '%{}%' LIMIT 4".format(
            idLop)
        cur.execute(query)
        result = cur.fetchall()
        ui.Suggest.setColumnCount(2)
        ui.Suggest.setRowCount(5)
        columns = 0
        for row in result:
            ui.Suggest.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.Suggest.setItem(columns, 1, QTableWidgetItem(row[1]))
            columns += 1
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)


if __name__ == "__main__":
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainUi()
    sys.exit(app.exec())
