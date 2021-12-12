

from messageBox import MBox
from database import myDB
from view.Login import Ui_MainWindow
from ShowHomeAdmin import showHomeAdmin
import mysql.connector as sql
from PyQt5.QtWidgets import QTableWidgetItem

import sys
sys.path.append('../')


def updateClassInHomeAdmin(self):
    self.uic.Suggest.setColumnCount(2)
    self.uic.Suggest.setRowCount(10)
    cur = myDB.cursor()
    cur.execute("SELECT * FROM lop LIMIT 9")
    result = cur.fetchall()
    columns = 0
    for row in result:
        self.uic.Suggest.setItem(columns, 0, QTableWidgetItem(row[0]))
        self.uic.Suggest.setItem(columns, 1, QTableWidgetItem(row[1]))
        columns += 1


def clearContentsInHomeAdmin(self):
    self.uic.ID_lop_update.setText("")
    self.uic.ID_cau_hoi_update.setText("")
    self.uic.ten_lop_update.setText("")
