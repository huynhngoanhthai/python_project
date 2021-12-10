

from PyQt5.QtWidgets import QTableWidgetItem

import sys
sys.path.append('../')
import mysql.connector as sql
from ShowHomeAdmin import showHomeAdmin
from view.Login import Ui_MainWindow
from database import myDB
from messageBox import MBox


def updateClassInHomeAdmin(self):
    self.uic.Suggest.setColumnCount(3)
    self.uic.Suggest.setRowCount(10)
    cur = myDB.cursor()
    cur.execute("SELECT * FROM lop LIMIT 9")
    result = cur.fetchall()
    columns = 0
    for row in result:
        self.uic.Suggest.setItem(columns,0,QTableWidgetItem(row[0]))
        self.uic.Suggest.setItem(columns,1,QTableWidgetItem(row[1]))
        self.uic.Suggest.setItem(columns,2,QTableWidgetItem(row[2]))
        columns+=1