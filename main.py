import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from Login import Ui_MainWindow
from database import myDB



class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #code
        self.uic.login.clicked.connect(self.loginUser)
        self.uic.seePassword.clicked.connect(self.checkSeePassword)


    def loginUser(self):
        cur = myDB.cursor()
        getUname = self.uic.uname.text().strip()
        getPassword = self.uic.password.text()
        
        cur.execute("SELECT * FROM sinh_vien WHERE mssv=%s AND password=%s",(getUname,getPassword))
       
        result = cur.fetchall()
        if len(result):
            print ("Successfully logged in")
            for x in result:
                print(x)
        else:
            print("uname or password wrong")

    def checkSeePassword(self):
        if self.uic.seePassword.isChecked():
            self.uic.password.setEchoMode(QLineEdit.Normal)
        else:
            self.uic.password.setEchoMode(QLineEdit.Password)
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())