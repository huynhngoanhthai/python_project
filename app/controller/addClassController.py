import sys
sys.path.append('../')
import mysql.connector as sql
from ShowHomeAdmin import showHomeAdmin
from view.Login import Ui_MainWindow
from database import myDB
from messageBox import MBox


def clearContentsInHomeAdmin(self):
    self.uic.ID_lop.setText("")
    self.uic.ID_cau_hoi.setText("")
    self.uic.ten_lop.setText("")

def addClassInHomeAdmin(self):
    try:
        idLop = self.uic.ID_lop.text().strip()
        if(idLop == ''):
            return MBox(0,"Error","ID lop khong duoc rong",16)
        tenLop = self.uic.ten_lop.text().strip()
        if(tenLop == ''):
            return MBox(0,"Error","ID ten Lop khong duoc rong",16)
        idCauHoi = self.uic.ID_cau_hoi.text().strip()
        cur = myDB.cursor()
        query = "INSERT INTO lop (ID_lop, ten_lop, ID_cau_hoi) VALUES (%s, %s,%s)"
        cur.execute(query,(idLop,tenLop,idCauHoi))
        myDB.commit()
    except sql.Error as e:
        MBox(0,"Error",str(e),32)