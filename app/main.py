import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5 import QtWidgets
#import file
from ShowHomeAdmin import showHomeAdmin
from controller.loginController import loginUser, checkSeePassword
from controller.addClassController import clearContentsInHomeAdmin, addClassInHomeAdmin
from controller.updateClassController import updateClassInHomeAdmin
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
        return loginUser(self)

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
        return clearContentsInHomeAdmin(self)

    # code Default
    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
