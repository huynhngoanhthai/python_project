import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTableWidgetItem
from PyQt5 import QtWidgets
import mysql.connector as sql
#import file
import view.Login as Login
import view.HomeAdmin as HomeAdmin
from database import myDB
from messageBox import MBox


def mainUi():
    global ui
    ui = Login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.login.clicked.connect(loginUser)
    ui.password.returnPressed.connect(loginUser)
    ui.seePassword.clicked.connect(checkPassword)


def loginUser():
    try:
        cur = myDB.cursor()
        getUname = ui.uname.text().strip()  # GT
        getPassword = ui.password.text()

        if(getUname[0:2] == "GT"):
            cur.execute(
                "SELECT * FROM dmgv WHERE MaGV=%s AND Password=%s", (getUname, getPassword))
            result = cur.fetchall()
            if(result == []):
                return MBox(0, 'ERROR', "uname or password wrong", 16)
            return showHomeAdmin()

        cur.execute("SELECT * FROM dmsv WHERE MaSV=%s AND Password=%s",
                    (getUname, getPassword))
        result = cur.fetchall()
        if(result == []):
            MBox(0, 'ERROR', "uname or password wrong", 16)
        else:
            print("123")
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)


def checkPassword():
    if ui.seePassword.isChecked():
        ui.password.setEchoMode(QLineEdit.Normal)
    else:
        ui.password.setEchoMode(QLineEdit.Password)


def showHomeAdmin():
    global ui
    ui = HomeAdmin.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # default here add
    ui.tab.setCurrentWidget(ui.Add)
    # default ID is
    cur = myDB.cursor()
    cur.execute("SELECT max(MaCH) FROM dmch")
    result = cur.fetchall()[0][0]+1
    ui.IDAddQuestion.setText(str(result))
    # event clicked for button
    ui.AddQuestion.clicked.connect(addQuestion)
    ui.ClearQuestion.clicked.connect(ClearContentsAddQuestion)


def addQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.IDAddQuestion.text().strip()
        Question = ui.QLineAQuestion.text().strip()
        if Question == '':
            return MBox(0, "Error", "Question not empty", 16)
        OPA = ui.QLineAOPA.text().strip()
        if OPA == '':
            return MBox(0, "Error", "not empty", 16)
        OPB = ui.QLineAOPB.text().strip()
        if OPB == '':
            return MBox(0, "Error", "not empty", 16)
        OPC = ui.QLineAOPC.text().strip()
        if OPC == '':
            return MBox(0, "Error", "not empty", 16)
        OPD = ui.QLineAOPD.text().strip()
        if OPD == '':
            return MBox(0, "Error", "not empty", 16)
        Answer = ui.QLineAAnswer.text().strip()
        if Answer == '':
            return MBox(0, "Error", "not empty", 16)
        MaMH = ui.QLineAMaMH.text().strip()
        if MaMH == '':
            return MBox(0, "Error", "not empty", 16)

        query = "INSERT INTO dmch (MaCH, CauHoi, CauA,CauB,CauC,CauD,DapAn,MaMH) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)"
        cur.execute(query, (IDQuestion, Question,
                    OPA, OPB, OPC, OPD, Answer, MaMH))
        MBox(0, "Successfully", "Successfully", 32)
        myDB.commit()
        showHomeAdmin()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def ClearContentsAddQuestion():
    ui.QLineAQuestion.setText("")
    ui.QLineAOPA.setText("")
    ui.QLineAOPB.setText("")
    ui.QLineAOPC.setText("")
    ui.QLineAOPD.setText("")
    ui.QLineAAnswer.setText("")
    ui.QLineAMaMH.setText("")


if __name__ == "__main__":
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # mainUi()
    showHomeAdmin()
    sys.exit(app.exec())
