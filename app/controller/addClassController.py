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
        cur = myDB.cursor()
        query = "INSERT INTO lop (ID_lop, ten_lop, ID_cau_hoi) VALUES (%s, %s,%s)"
        idLop = self.uic.ID_lop.text().strip() 
        tenLop = self.uic.ten_lop.text().strip()
        idCauHoi = self.uic.ID_cau_hoi.text().strip()
        cur.execute(query,(idLop,tenLop,idCauHoi))
        myDB.commit()
    except sql.Error as e:
        MBox(0,"Error",str(e),32)