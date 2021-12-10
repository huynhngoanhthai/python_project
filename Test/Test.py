import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableWidgetItem
from SearchSmart import Ui_MainWindow
from database import myDB

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #code
        self.uic.KeyWord.textEdited.connect(self.SearchAI)
        self.uic.Search.clicked.connect(self.PrintTable)

    def PrintTable(self):
        self.uic.TableStudent.setRowCount(5)
        self.uic.TableStudent.setColumnCount(3)
        self.uic.TableStudent.setItem(2,2,QTableWidgetItem("123"))
    def SearchAI(self):
        

        try:
            cur = myDB.cursor()
            key = self.uic.KeyWord.text()
            query = "SELECT * FROM lop WHERE ten_lop LIKE '%{}%' LIMIT 5".format(key)
            cur.execute(query)
            result = cur.fetchall()
            print(result)

        except :
            print("Error database")



    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())