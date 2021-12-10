import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from PyQt5 import QtWidgets
#import file
from ShowHomeAdmin import showHomeAdmin
from controller.loginController import loginUser,checkSeePassword 
from view.Login import Ui_MainWindow
from database import myDB
from messageBox import MBox


class MainWindow:
    def __init__(self):
        
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #code
        self.uic.login.clicked.connect(self.login)
        self.uic.password.returnPressed.connect(self.login)
        self.uic.seePassword.clicked.connect(self.checkPassword)
    def login(self):
        cur = myDB.cursor()
        getUname = self.uic.uname.text().strip()
        getPassword = self.uic.password.text()
        cur.execute("SELECT * FROM User WHERE mssv=%s AND password=%s",(getUname,getPassword))
        result = cur.fetchall()
        if len(result):
           print(result[0][-1])
        else:
            MBox(0,'ERROR',"uname or password wrong",16)
    def checkPassword(self):
        if self.uic.seePassword.isChecked():
            self.uic.password.setEchoMode(QLineEdit.Normal)
        else:
            self.uic.password.setEchoMode(QLineEdit.Password)
    def clearContents(self):
        self.uic.ID_lop.setText("")
        self.uic.ID_cau_hoi.setText("")
        self.uic.ten_lop.setText("")
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())