

from messageBox import MBox
from database import myDB
from view.Login import Ui_MainWindow
from ShowHomeAdmin import showHomeAdmin
import mysql.connector as sql
from PyQt5.QtWidgets import QTableWidgetItem

import sys
sys.path.append('../')


def updateClassInHomeAdmin(self):
    try:
        idLop = self.uic.ID_lop_update.text().strip()
        if(idLop == ''):
            return MBox(0, "Error", "ID lop khong duoc rong", 16)
        tenLop = self.uic.ten_lop_update.text().strip()
        if(tenLop == ''):
            return MBox(0, "Error", "ID ten Lop khong duoc rong", 16)
        cur = myDB.cursor()
        query = "UPDATE lop SET ten_lop = '{}' WHERE ID_lop = '{}'".format(
            tenLop, idLop)

        cur.execute(query)
        MBox(0, "Successfully",
             "you updated ID_lop = {}, ten_lop = {}".format(idLop, tenLop), 64)
        myDB.commit()
        clearContentsUpdateInHomeAdmin(self)
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)
    # self.uic.Suggest.setColumnCount(2)
    # self.uic.Suggest.setRowCount(10)
    # cur = myDB.cursor()
    # cur.execute("SELECT * FROM lop LIMIT 9")
    # result = cur.fetchall()
    # columns = 0
    # for row in result:
    #     self.uic.Suggest.setItem(columns, 0, QTableWidgetItem(row[0]))
    #     self.uic.Suggest.setItem(columns, 1, QTableWidgetItem(row[1]))
    #     columns += 1


def clearContentsUpdateInHomeAdmin(self):
    self.uic.ID_lop_update.setText("")
    self.uic.ten_lop_update.setText("")
