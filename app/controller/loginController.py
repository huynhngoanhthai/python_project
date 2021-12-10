from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from PyQt5 import QtWidgets
import sys
sys.path.append('../')
from ShowHomeAdmin import showHomeAdmin
from view.Login import Ui_MainWindow
from database import myDB
from messageBox import MBox


def loginUser(self):
        cur = myDB.cursor()
        getUname = self.uic.uname.text().strip()
        getPassword = self.uic.password.text()
        cur.execute("SELECT * FROM User WHERE mssv=%s AND password=%s",(getUname,getPassword))
        result = cur.fetchall()
        if result[0][-1]=="TEACHER":
            showHomeAdmin(self)
        if result[0][-1]=="STUDENT":
            print("123")
        else:
            MBox(0,'ERROR',"uname or password wrong",16)
def checkSeePassword(self):
        if self.uic.seePassword.isChecked():
            self.uic.password.setEchoMode(QLineEdit.Normal)
        else:
            self.uic.password.setEchoMode(QLineEdit.Password)