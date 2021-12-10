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
        cur.execute("SELECT * FROM sinh_vien WHERE mssv=%s AND password=%s",(getUname,getPassword))
        result = cur.fetchall()
        if len(result):
           showHomeAdmin(self)
        else:
            MBox(0,'ERROR',"uname or password wrong",16)
            print("uname or password wrong")
def checkSeePassword(self):
        if self.uic.seePassword.isChecked():
            self.uic.password.setEchoMode(QLineEdit.Normal)
        else:
            self.uic.password.setEchoMode(QLineEdit.Password)