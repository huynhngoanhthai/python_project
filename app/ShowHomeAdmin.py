import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from PyQt5 import QtWidgets
from view.HomeAmin import Ui_MainWindow



def showHomeAdmin(self):
    self.main_win = QMainWindow()
    self.uic = Ui_MainWindow()
    self.uic.setupUi(self.main_win)
    self.main_win.show()
    
    # default is screen add Class
    self.uic.tab.setCurrentWidget(self.uic.Add)
    #code
    # add class
    self.uic.Clear.clicked.connect(self.clearContents)
    self.uic.AddClass.clicked.connect(self.addClass)
    # Update class
    self.uic.UpdateClass.clicked.connect(self.updateClass)


    

