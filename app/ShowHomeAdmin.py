import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from PyQt5 import QtWidgets
from view.HomeAmin import Ui_MainWindow



def showHomeAdmin(self):
    self.main_win = QMainWindow()
    self.uic = Ui_MainWindow()
    self.uic.setupUi(self.main_win)
    self.main_win.show()
    #code
    self.uic.Clear.clicked.connect(self.clearContents)
    def clearContents():
        self.uic.ID_lop.setText("")
        self.uic.ID_cau_hoi.setText("")
        self.uic.ten_lop.setText("")

    

