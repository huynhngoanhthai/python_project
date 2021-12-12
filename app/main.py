import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from PyQt5 import QtWidgets
import mysql.connector as sql
#import file
from controller.loginController import loginUser, checkSeePassword
from controller.addClassController import clearContentsInHomeAdmin, addClassInHomeAdmin
from controller.updateClassController import updateClassInHomeAdmin, clearContentsUpdateInHomeAdmin
from ShowHomeAdmin import showHomeAdmin
from view.Login import Ui_MainWindow
from database import myDB
from messageBox import MBox


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # code
        self.uic.login.clicked.connect(self.login)
        self.uic.password.returnPressed.connect(self.login)
        self.uic.seePassword.clicked.connect(self.checkPassword)
    # Login User

    def login(self):
        try:
            cur = myDB.cursor()
            getUname = self.uic.uname.text().strip()
            getPassword = self.uic.password.text()
            cur.execute(
                "SELECT * FROM User WHERE mssv=%s AND password=%s", (getUname, getPassword))
            result = cur.fetchall()
            if(result == []):
                MBox(0, 'ERROR', "uname or password wrong", 16)
            elif result[0][-1] == "TEACHER":
                showHomeAdmin(self)
            else:
                # for role = students
                print("123")
        except sql.Error as e:
            MBox(0, "Error", str(e), 32)

    def checkPassword(self):
        return checkSeePassword(self)

    # Home Admin
    def clearContents(self):
        return clearContentsInHomeAdmin(self)

    def addClass(self):
        return addClassInHomeAdmin(self)
    # Update Class

    def updateClass(self):
        return updateClassInHomeAdmin(self)

    def clearContentsUpdateClass(self):
        return clearContentsUpdateInHomeAdmin(self)
    # func Suggest where press Enter

    def PressEnterSuggestion(self):
        try:
            cur = myDB.cursor()
            idLop = self.uic.ID_lop_update.text().strip()
            query = "SELECT * FROM lop WHERE ID_lop LIKE '%{}%' LIMIT 4".format(
                idLop)
            cur.execute(query)
            result = cur.fetchall()
            self.uic.Suggest.setColumnCount(2)
            self.uic.Suggest.setRowCount(5)
            columns = 0
            for row in result:
                self.uic.Suggest.setItem(columns, 0, QTableWidgetItem(row[0]))
                self.uic.Suggest.setItem(columns, 1, QTableWidgetItem(row[1]))
                columns += 1
        except sql.Error as e:
            MBox(0, "Error", str(e), 32)
    # code Default

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
