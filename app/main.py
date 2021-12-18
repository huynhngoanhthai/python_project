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
    # event clicked for button in add
    ui.QLineAMaMH.returnPressed.connect(addQuestion)
    ui.AddQuestion.clicked.connect(addQuestion)
    ui.ClearQuestion.clicked.connect(ClearContentsAddQuestion)
    # event clicked for button in Update
    ui.ClearUpdate.clicked.connect(ClearContentsUpdateQuestion)
    ui.QLineUIDCauHoi.returnPressed.connect(SuggestUpdateQuestion)
    ui.UpdateQuestion.clicked.connect(updateQuestion)
    # event clicked for button in Delete
    ui.ClearDelete.clicked.connect(ClearContentsDeleteQuestion)
    ui.QLineDIDCauHoi.returnPressed.connect(SuggestDeleteQuestion)
    ui.QLineDCauHoi.returnPressed.connect(SuggestDeleteQuestion)
    ui.DeleteQuestion.clicked.connect(deleteQuestion)


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
    ui.QLineUIDCauHoi.setText("")
    ui.QLineAQuestion.setText("")
    ui.QLineAOPA.setText("")
    ui.QLineAOPB.setText("")
    ui.QLineAOPC.setText("")
    ui.QLineAOPD.setText("")
    ui.QLineAAnswer.setText("")
    ui.QLineAMaMH.setText("")


def ClearContentsUpdateQuestion():
    ui.QLineUIDCauHoi.clear()
    ui.QLineUQuestion.clear()
    ui.QLineUOPA.clear()
    ui.QLineUOPB.clear()
    ui.QLineUOPC.clear()
    ui.QLineUOPD.clear()
    ui.QLineUAnswer.clear()
    ui.QLineUMaMH.clear()
    ui.QLineUIDCauHoi.setDisabled(False)
    ui.QTableUpdate.clearContents()


def SuggestUpdateQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineUIDCauHoi.text().strip()
        query = "SELECT * FROM dmch WHERE MaCH LIKE '%{}%' LIMIT 10;".format(
            IDQuestion)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 1:
            ui.QLineUIDCauHoi.setText(str(result[0][0]))
            ui.QLineUQuestion.setText(result[0][1])
            ui.QLineUOPA.setText(result[0][2])
            ui.QLineUOPB.setText(result[0][3])
            ui.QLineUOPC.setText(result[0][4])
            ui.QLineUOPD.setText(result[0][5])
            ui.QLineUAnswer.setText(result[0][6])
            ui.QLineUMaMH.setText(result[0][7])
            ui.QLineUIDCauHoi.setDisabled(True)
        ui.QTableUpdate.clearContents()
        ui.QTableUpdate.setColumnCount(8)
        ui.QTableUpdate.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableUpdate.setItem(columns, 0, QTableWidgetItem(str(row[0])))
            ui.QTableUpdate.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableUpdate.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableUpdate.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableUpdate.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableUpdate.setItem(columns, 5, QTableWidgetItem(row[5]))
            ui.QTableUpdate.setItem(columns, 6, QTableWidgetItem(row[6]))
            ui.QTableUpdate.setItem(columns, 7, QTableWidgetItem(row[7]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def updateQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineUIDCauHoi.text().strip()
        if IDQuestion == '':
            return MBox(0, "Error", "not empty", 16)
        if ui.QLineUIDCauHoi.isEnabled():
            return MBox(0, "Error", "you need block", 16)
        Question = ui.QLineUQuestion.text().strip()
        if Question == '':
            return MBox(0, "Error", "Question not empty", 16)
        OPA = ui.QLineUOPA.text().strip()
        if OPA == '':
            return MBox(0, "Error", "not empty", 16)
        OPB = ui.QLineUOPB.text().strip()
        if OPB == '':
            return MBox(0, "Error", "not empty", 16)
        OPC = ui.QLineUOPC.text().strip()
        if OPC == '':
            return MBox(0, "Error", "not empty", 16)
        OPD = ui.QLineUOPD.text().strip()
        if OPD == '':
            return MBox(0, "Error", "not empty", 16)
        Answer = ui.QLineUAnswer.text().strip()
        if Answer == '':
            return MBox(0, "Error", "not empty", 16)
        MaMH = ui.QLineUMaMH.text().strip()
        if MaMH == '':
            return MBox(0, "Error", "not empty", 16)
        query = "UPDATE dmch SET CauHoi=%s,CauA=%s,CauB=%s,CauC=%s,CauD=%s,DapAn=%s,MaMH=%s WHERE MaCH=%s"
        cur.execute(query, (Question,
                    OPA, OPB, OPC, OPD, Answer, MaMH, IDQuestion))
        MBox(0, "Successfully", "Successfully", 32)
        myDB.commit()
        ClearContentsUpdateQuestion()

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def ClearContentsDeleteQuestion():
    ui.QLineDCauHoi.clear()
    ui.QLineDIDCauHoi.clear()
    ui.QLineDCauHoi.setDisabled(False)
    ui.QLineDIDCauHoi.setDisabled(False)
    ui.QTableDelete.clearContents()


def SuggestDeleteQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineDIDCauHoi.text().strip()
        CauHoi = ui.QLineDCauHoi.text().strip()
        query = "SELECT * FROM dmch WHERE MaCH LIKE '%{0}%' AND CauHoi LIKE '%{1}%' LIMIT 15;".format(
                IDQuestion, CauHoi)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 1:
            ui.QLineDIDCauHoi.setText(str(result[0][0]))
            ui.QLineDCauHoi.setText(result[0][1])
            ui.QLineDIDCauHoi.setDisabled(True)
            ui.QLineDCauHoi.setDisabled(True)
        ui.QTableDelete.clearContents()
        ui.QTableDelete.setColumnCount(8)
        ui.QTableDelete.setRowCount(15)
        columns = 0
        for row in result:
            ui.QTableDelete.setItem(columns, 0, QTableWidgetItem(str(row[0])))
            ui.QTableDelete.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableDelete.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableDelete.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableDelete.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableDelete.setItem(columns, 5, QTableWidgetItem(row[5]))
            ui.QTableDelete.setItem(columns, 6, QTableWidgetItem(row[6]))
            ui.QTableDelete.setItem(columns, 7, QTableWidgetItem(row[7]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def deleteQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.QLineDIDCauHoi.text().strip()
        CauHoi = ui.QLineDCauHoi.text().strip()
        if ui.QLineDIDCauHoi.isEnabled() == True or ui.QLineDIDCauHoi.isEnabled() == True:
            return MBox(0, "Error", "You need block ", 16)

        cur.execute(
            "DELETE FROM dmch WHERE MaCH = %s AND CauHoi = %s", (IDQuestion, CauHoi))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        ClearContentsDeleteQuestion()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


if __name__ == "__main__":
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # mainUi()
    showHomeAdmin()
    sys.exit(app.exec())
