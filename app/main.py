from messageBox import MBox
from database import myDB
import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QRadioButton, QTableWidgetItem
from PyQt5 import QtWidgets
import mysql.connector as sql
# import file
import view.Login as Login
import view.HomeQuestion as HomeQuestion
import view.HomeTeacher as HomeTeacher
import view.HomeStudent as HomeStudent
import view.TakeTest as TakeTest
import view.Student as Student
import view.Subjects as Subjects


def mainUi():
    global ui
    ui = Login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()

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
            return showHomeTeacher(result)

        cur.execute("SELECT * FROM dmsv WHERE MaSV=%s AND Password=%s",
                    (getUname, getPassword))
        result = cur.fetchall()
        if(result == []):
            MBox(0, 'ERROR', "uname or password wrong", 16)
        else:
            showHomeStudent(result)
    except sql.Error as e:
        MBox(0, "Error", str(e), 32)


def checkPassword():
    if ui.seePassword.isChecked():
        ui.password.setEchoMode(QLineEdit.Normal)
    else:
        ui.password.setEchoMode(QLineEdit.Password)


def showHomeTeacher(info):
    global ui
    ui = HomeTeacher.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default name for GV
    ui.NAMEGV.setText(info[0][3])
    ui.QButtonCH.clicked.connect(showHomeQuestion)
    ui.QButtonSV.clicked.connect(showStudent)
    ui.QButtonMH.clicked.connect(showSubjects)


def showSubjects():
    global ui
    ui = Subjects.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default
    ui.tab.setCurrentWidget(ui.Add)
    ui.QButtonBack.clicked.connect(callBackShowHomeTeacher)
    # event clicked for button in add
    ui.QButtonAClear.clicked.connect(clearContentsAddSubjects)
    ui.QButtonAAdd.clicked.connect(addSubject)
    # event clicked for button in Update
    ui.QButtonUClear.clicked.connect(clearContentsUpdateSubjects)
    ui.QLineUMaMH.returnPressed.connect(suggestUpdateSubjects)
    ui.QButtonUUpdate.clicked.connect(updateSubject)
    # event clicked for button in DELETE
    ui.QButtonDClear.clicked.connect(clearContentsDeleteSubjects)
    ui.QLineDMaMH.returnPressed.connect(suggestDeleteSubjects)
    ui.QLineDTenMH.returnPressed.connect(suggestDeleteSubjects)
    ui.QButtonDDelete.clicked.connect(deleteSubject)


# Add subject


def clearContentsAddSubjects():
    ui.QLineAMaMH.clear()
    ui.QLineATenMH.clear()
    ui.QBoxASoTiet.setValue(0)


def addSubject():
    try:
        cur = myDB.cursor()
        MaMH = ui.QLineAMaMH.text().strip()
        TenMH = ui.QLineATenMH.text().strip()
        SoTiet = ui.QBoxASoTiet.text()
        if isCheckedEmpty(MaMH, TenMH, SoTiet) == False:
            return MBox(0, "Error", "Not empty", 32)

        query = "INSERT INTO dmmh (MaMH,TenMH,SoTiet) VALUES (%s,%s, %s) "
        cur.execute(query, (MaMH, TenMH, SoTiet))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        clearContentsAddSubjects()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# update


def clearContentsUpdateSubjects():
    ui.QLineUMaMH.clear()
    ui.QLineUTenMH.clear()
    ui.QBoxUSoTiet.setValue(0)
    ui.QLineUMaMH.setEnabled(True)


def suggestUpdateSubjects():
    try:
        cur = myDB.cursor()
        MaMH = ui.QLineUMaMH.text().strip()
        query = "SELECT * FROM dmmh WHERE MaMH LIKE '%{}%';".format(MaMH)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 1:
            ui.QLineUMaMH.setText(result[0][0])
            ui.QLineUTenMH.setText(result[0][1])
            ui.QBoxUSoTiet.setValue(result[0][2])
            ui.QLineUMaMH.setDisabled(True)

        ui.QTableUpdate.clearContents()
        ui.QTableUpdate.setColumnCount(3)
        ui.QTableUpdate.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableUpdate.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableUpdate.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableUpdate.setItem(columns, 2, QTableWidgetItem(str(row[2])))

            columns += 1
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def updateSubject():
    try:
        if ui.QLineUMaMH.isEnabled() == True:
            return MBox(0, "Error", "You need block ", 16)
        cur = myDB.cursor()
        MaMH = ui.QLineUMaMH.text().strip()
        TenMH = ui.QLineUTenMH.text().strip()
        SoTiet = ui.QBoxUSoTiet.text()
        if isCheckedEmpty(MaMH, TenMH, SoTiet) == False:
            return MBox(0, "Error", "not empty", 16)

        query = "UPDATE dmmh SET TenMH=%s,SoTiet=%s WHERE MaMH=%s"
        cur.execute(query, (TenMH, SoTiet, MaMH))
        myDB.commit()
        clearContentsUpdateSubjects()
        MBox(0, "Successfully", "Successfully", 32)
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


# Delete
def clearContentsDeleteSubjects():
    ui.QLineDMaMH.clear()
    ui.QLineDTenMH.clear()

    ui.QLineDMaMH.setEnabled(True)
    ui.QLineDTenMH.setEnabled(True)
    ui.QTableDelete.clearContents()


def suggestDeleteSubjects():
    try:
        query = ""
        cur = myDB.cursor()
        MaMH = ui.QLineDMaMH.text().strip()
        TenMH = ui.QLineDTenMH.text().strip()
        if MaMH == "":
            query = "SELECT * FROM dmmh WHERE  TenMH LIKE '%{}%';".format(
                TenMH)
        elif TenMH == '':
            query = "SELECT * FROM dmmh WHERE MaMH LIKE '%{}%';".format(MaMH)
        else:
            query = "SELECT * FROM dmmh WHERE  TenMH LIKE '%{}%' AND MaMH LIKE '%{}%';".format(
                TenMH, MaMH)

        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 1:
            ui.QLineDMaMH.setText(result[0][0])
            ui.QLineDTenMH.setText(result[0][1])
            ui.QLineDMaMH.setDisabled(True)
            ui.QLineDTenMH.setDisabled(True)
        ui.QTableDelete.clearContents()
        ui.QTableDelete.setColumnCount(3)
        ui.QTableDelete.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableDelete.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableDelete.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableDelete.setItem(columns, 2, QTableWidgetItem(str(row[2])))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def deleteSubject():
    try:
        if ui.QLineDMaMH.isEnabled() or ui.QLineDTenMH.isEnabled():
            return MBox(0, "Error", "you need block", 16)
        cur = myDB.cursor()
        MaMH = ui.QLineDMaMH.text().strip()
        TenMH = ui.QLineDTenMH.text().strip()

        query = "DELETE FROM dmmh WHERE MaMH = %s AND TenMH = %s"
        cur.execute(query, (MaMH, TenMH))
        myDB.commit()
        clearContentsDeleteSubjects()
        MBox(0, "Successfully", "Successfully", 32)
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# show Student


def callBackShowHomeTeacher():
    return showHomeTeacher([('', '', '', 'GIAO VIEN')])


def showStudent():
    global ui
    ui = Student.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default
    ui.QButtonBack.clicked.connect(callBackShowHomeTeacher)

    # event clicked for button in add
    ui.tab.setCurrentWidget(ui.Add)
    ui.QButtonAClear.clicked.connect(clearContentsAddStudent)
    ui.QButtonAAddStudent.clicked.connect(addStudent)
    ui.QLineALop.returnPressed.connect(addStudent)
    # event clicked for button in update
    ui.QLineUMaSV.returnPressed.connect(suggestUpdateStudent)
    ui.QButtonUClear.clicked.connect(clearContentsUpdateStudent)
    ui.QButtonUUpdate.clicked.connect(updateStudent)
    # event clicked for button in DELETE
    ui.QButtonDClear.clicked.connect(clearContentsDeleteStudent)
    ui.QLineDMaSV.returnPressed.connect(suggestDeleteStudent)
    ui.QLineDTenSV.returnPressed.connect(suggestDeleteStudent)

    ui.QButtonDDelete.clicked.connect(deleteStudent)
    # event clicked for button in Show All

    ui.QButtonSAClear.clicked.connect(clearContentsShowAllStudent)
    ui.QButtonShowAll.clicked.connect(suggestShowAllStudent)
    ui.QLineSAMaSV.returnPressed.connect(suggestDeleteStudent)
    ui.QLineSATenSV.returnPressed.connect(suggestDeleteStudent)


def clearContentsAddStudent():
    ui.QLineAMaSV.clear()
    ui.QLineAHoSV.clear()
    ui.QDateANS.setDate(date_changed("04/11/2001"))
    ui.QLineATenSV.clear()
    ui.QLineADC.clear()
    ui.QLineALop.clear()


def addStudent():
    try:
        MaSV = ui.QLineAMaSV.text()

        HoSV = ui.QLineAHoSV.text()

        TenSV = ui.QLineATenSV.text()

        Phai = ''
        if ui.OpNAM.isChecked():
            Phai = "NAM"
        elif ui.OpNU.isChecked():
            Phai = "NU"
        else:
            return MBox(0, "Error", "you need choose Phai", 16)

        NgaySinh = ui.QDateANS.text()
        NoiSinh = ui.QLineADC.text()

        Lop = ui.QLineALop.text()

        checked = isCheckedEmpty(MaSV, HoSV, TenSV, NgaySinh, NoiSinh, Lop)
        if not checked:
            return MBox(0, "Error", "not empty", 16)

        cur = myDB.cursor()
        cur.execute(
            "INSERT INTO dmsv (MaSV,Password,HoSV,TenSV,Phai,NgaySinh,NoiSinh,TenLop) VALUES (%s,%s, %s,%s,%s, %s,%s,%s) ",
            (MaSV, MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, Lop))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        clearContentsAddStudent()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


# update student
def clearContentsUpdateStudent():
    ui.QLineUMaSV.clear()
    ui.QLineUHoSV.clear()
    ui.QLineUTenSV.clear()
    ui.OpUPhai.setCurrentIndex(0)
    ui.QDateUNgaySinh.setDate(date_changed("04/11/2001"))
    ui.QLineUNoiSinh.clear()
    ui.QLineULop.clear()

    ui.QLineUMaSV.setDisabled(False)
    ui.QTableUpdate.clearContents()


def date_changed(day):
    newDay = day.split('/')
    return QDate(int(newDay[2]), int(newDay[1]), int(newDay[0]))


def suggestUpdateStudent():
    try:
        cur = myDB.cursor()
        MaSV = ui.QLineUMaSV.text().strip()
        query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' LIMIT 10;".format(
            MaSV)
        cur.execute(query)
        result = cur.fetchall()

        if len(result) == 1:
            ui.QLineUMaSV.setText(result[0][0])
            ui.QLineUHoSV.setText(result[0][2])
            ui.QLineUTenSV.setText(result[0][3])
            if result[0][4] == 'NAM':
                ui.OpUPhai.setCurrentIndex(0)
            else:
                ui.OpUPhai.setCurrentIndex(1)
            ui.QDateUNgaySinh.setDate(date_changed(result[0][5]))
            ui.QLineUNoiSinh.setText(result[0][6])
            ui.QLineULop.setText(result[0][7])
            ui.QLineUMaSV.setDisabled(True)

        ui.QTableUpdate.clearContents()
        ui.QTableUpdate.setColumnCount(7)
        ui.QTableUpdate.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableUpdate.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableUpdate.setItem(columns, 1, QTableWidgetItem(row[2]))
            ui.QTableUpdate.setItem(columns, 2, QTableWidgetItem(row[3]))
            ui.QTableUpdate.setItem(columns, 3, QTableWidgetItem(row[4]))
            ui.QTableUpdate.setItem(columns, 4, QTableWidgetItem(row[5]))
            ui.QTableUpdate.setItem(columns, 5, QTableWidgetItem(row[6]))
            ui.QTableUpdate.setItem(columns, 6, QTableWidgetItem(row[7]))
            columns += 1
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def isCheckedEmpty(*argv):
    #  argv is a tuple
    for item in argv:
        if item == '' or item == '0':
            return False
    return True


def updateStudent():
    try:
        cur = myDB.cursor()
        MaSV = ui.QLineUMaSV.text().strip()
        HoSV = ui.QLineUHoSV.text().strip()
        TenSV = ui.QLineUTenSV.text().strip()
        Phai = ui.OpUPhai.currentText()
        NgaySinh = ui.QDateUNgaySinh.text().strip()
        NoiSinh = ui.QLineUNoiSinh.text().strip()
        TenLop = ui.QLineULop.text().strip()
        checked = isCheckedEmpty(
            MaSV, HoSV, TenSV, Phai, NgaySinh, NoiSinh, TenLop)
        if not checked:
            return MBox(0, "Error", "not empty", 16)

        query = "UPDATE dmsv SET HoSV=%s,TenSV=%s,Phai=%s,NgaySinh=%s,NoiSinh=%s,TenLop=%s WHERE MaSV=%s"

        cur.execute(query, (HoSV, TenSV, Phai,
                    NgaySinh, NoiSinh, TenLop, MaSV))
        myDB.commit()
        clearContentsUpdateStudent()
        MBox(0, "Successfully", "Successfully", 32)

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# delete


def clearContentsDeleteStudent():
    ui.QLineDMaSV.clear()
    ui.QLineDTenSV.clear()

    ui.QTableDelete.clearContents()
    ui.QLineDMaSV.setEnabled(True)
    ui.QLineDTenSV.setEnabled(True)


def suggestDeleteStudent():
    try:
        query = ""
        cur = myDB.cursor()
        MaSV = ui.QLineDMaSV.text().strip()
        TenSV = ui.QLineDTenSV.text().strip()
        if MaSV == '':
            query = "SELECT * FROM dmsv WHERE TenSV LIKE '%{}%' LIMIT 10".format(
                TenSV)
        if TenSV == '':
            query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' LIMIT 10".format(
                MaSV)
        else:
            query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' AND TenSV LIKE '%{}%' LIMIT 10".format(
                MaSV, TenSV)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 1:
            ui.QLineDMaSV.setText(result[0][0])
            ui.QLineDTenSV.setText(result[0][3])
            ui.QLineDMaSV.setDisabled(True)
            ui.QLineDTenSV.setDisabled(True)
        ui.QTableDelete.clearContents()
        ui.QTableDelete.setColumnCount(7)
        ui.QTableDelete.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableDelete.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableDelete.setItem(columns, 1, QTableWidgetItem(row[2]))
            ui.QTableDelete.setItem(columns, 2, QTableWidgetItem(row[3]))
            ui.QTableDelete.setItem(columns, 3, QTableWidgetItem(row[4]))
            ui.QTableDelete.setItem(columns, 4, QTableWidgetItem(row[5]))
            ui.QTableDelete.setItem(columns, 5, QTableWidgetItem(row[6]))
            ui.QTableDelete.setItem(columns, 6, QTableWidgetItem(row[7]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def deleteStudent():
    try:
        if ui.QLineDMaSV.isEnabled() == True and ui.QLineDMaSV.isEnabled() == True:
            return MBox(0, "Error", "You need block ", 16)
        cur = myDB.cursor()
        MaSV = ui.QLineDMaSV.text().strip()
        TenSV = ui.QLineDTenSV.text().strip()
        cur.execute(
            "DELETE FROM dmsv WHERE MaSV = %s AND TenSV = %s", (MaSV, TenSV))
        myDB.commit()
        MBox(0, "Successfully", "Successfully", 32)
        clearContentsDeleteStudent()

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# Show All


def clearContentsShowAllStudent():
    ui.QLineSAMaSV.clear()
    ui.QLineSATenSV.clear()

    ui.QTableDelete.clearContents()
    ui.QLineSAMaSV.setEnabled(True)
    ui.QLineSATenSV.setEnabled(True)


def suggestShowAllStudent():
    try:
        query = ""
        cur = myDB.cursor()
        MaSV = ui.QLineSAMaSV.text().strip()
        TenSV = ui.QLineSATenSV.text().strip()
        if MaSV == '':
            query = "SELECT * FROM dmsv WHERE TenSV LIKE '%{}%' LIMIT 10".format(
                TenSV)
        if TenSV == '':
            query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' LIMIT 10".format(
                MaSV)
        else:
            query = "SELECT * FROM dmsv WHERE MaSV LIKE '%{}%' AND TenSV LIKE '%{}%' LIMIT 10".format(
                MaSV, TenSV)
        cur.execute(query)
        result = cur.fetchall()
        if len(result) == 1:
            ui.QLineSAMaSV.setText(result[0][0])
            ui.QLineSATenSV.setText(result[0][3])
            ui.QLineSAMaSV.setDisabled(True)
            ui.QLineSATenSV.setDisabled(True)
        ui.QTableShowAll.clearContents()
        ui.QTableShowAll.setColumnCount(7)
        ui.QTableShowAll.setRowCount(10)
        columns = 0
        for row in result:
            ui.QTableShowAll.setItem(columns, 0, QTableWidgetItem(row[0]))
            ui.QTableShowAll.setItem(columns, 1, QTableWidgetItem(row[2]))
            ui.QTableShowAll.setItem(columns, 2, QTableWidgetItem(row[3]))
            ui.QTableShowAll.setItem(columns, 3, QTableWidgetItem(row[4]))
            ui.QTableShowAll.setItem(columns, 4, QTableWidgetItem(row[5]))
            ui.QTableShowAll.setItem(columns, 5, QTableWidgetItem(row[6]))
            ui.QTableShowAll.setItem(columns, 6, QTableWidgetItem(row[7]))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)
# HomeQuestion


def showHomeQuestion():
    global ui
    ui = HomeQuestion.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default here add
    ui.tab.setCurrentWidget(ui.Add)
    ui.ButtonLogout.clicked.connect(mainUi)
    # default ID is
    cur = myDB.cursor()
    cur.execute("SELECT max(MaCH) FROM dmch")
    result = cur.fetchall()[0][0]+1
    ui.IDAddQuestion.setText(str(result))
    # event clicked for button in add
    ui.QLineAMaMH.returnPressed.connect(addQuestion)
    ui.AddQuestion.clicked.connect(addQuestion)
    ui.ClearQuestion.clicked.connect(clearContentsAddQuestion)
    # event clicked for button in Update
    ui.ClearUpdate.clicked.connect(clearContentsUpdateQuestion)
    ui.QLineUIDCauHoi.returnPressed.connect(suggestUpdateQuestion)
    ui.UpdateQuestion.clicked.connect(updateQuestion)
    # event clicked for button in Delete
    ui.ClearDelete.clicked.connect(clearContentsDeleteQuestion)
    ui.QLineDIDCauHoi.returnPressed.connect(suggestDeleteQuestion)
    ui.QLineDCauHoi.returnPressed.connect(suggestDeleteQuestion)
    ui.DeleteQuestion.clicked.connect(deleteQuestion)
    # event clicked for button in Show All list student
    ui.ButtonSAClear.clicked.connect(clearContentsShowAllQuestion)
    ui.QLineSAMaSV.returnPressed.connect(suggestShowAllQuestion)
    ui.QLineSATenSV.returnPressed.connect(suggestShowAllQuestion)
    ui.QLineSADiem.returnPressed.connect(suggestShowAllQueryQuestion)
    ui.ButtonSASearch.clicked.connect(suggestShowAllQueryQuestion)
# Add


def addQuestion():
    try:
        cur = myDB.cursor()
        IDQuestion = ui.IDAddQuestion.text().strip()
        Question = ui.QLineAQuestion.text().strip()

        OPA = ui.QLineAOPA.text().strip()

        OPB = ui.QLineAOPB.text().strip()

        OPC = ui.QLineAOPC.text().strip()

        OPD = ui.QLineAOPD.text().strip()

        Answer = ui.QLineAAnswer.text().strip()

        MaMH = ui.QLineAMaMH.text().strip()

        checked = isCheckedEmpty(IDQuestion, Question,
                                 OPA, OPB, OPC, OPD, Answer, MaMH)
        if not checked:
            return MBox(0, "Error", "not empty", 16)

        query = "INSERT INTO dmch (MaCH, CauHoi, CauA,CauB,CauC,CauD,DapAn,MaMH) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)"
        cur.execute(query, (IDQuestion, Question,
                    OPA, OPB, OPC, OPD, Answer, MaMH))
        MBox(0, "Successfully", "Successfully", 32)
        myDB.commit()
        showHomeQuestion()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def clearContentsAddQuestion():
    ui.QLineAQuestion.clear()
    ui.QLineAOPA.clear()
    ui.QLineAOPB.clear()
    ui.QLineAOPC.clear()
    ui.QLineAOPD.clear()
    ui.QLineAAnswer.clear()
    ui.QLineAMaMH.clear()

# Update


def clearContentsUpdateQuestion():
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


def suggestUpdateQuestion():
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
        if ui.QLineUIDCauHoi.isEnabled():
            return MBox(0, "Error", "you need block", 16)
        Question = ui.QLineUQuestion.text().strip()

        OPA = ui.QLineUOPA.text().strip()

        OPB = ui.QLineUOPB.text().strip()

        OPC = ui.QLineUOPC.text().strip()

        OPD = ui.QLineUOPD.text().strip()

        Answer = ui.QLineUAnswer.text().strip()

        MaMH = ui.QLineUMaMH.text().strip()

        checked = isCheckedEmpty(IDQuestion, Question,
                                 OPA, OPB, OPC, OPD, Answer, MaMH)
        if not checked:
            return MBox(0, "Error", "not empty", 16)

        query = "UPDATE dmch SET CauHoi=%s,CauA=%s,CauB=%s,CauC=%s,CauD=%s,DapAn=%s,MaMH=%s WHERE MaCH=%s"
        cur.execute(query, (Question,
                    OPA, OPB, OPC, OPD, Answer, MaMH, IDQuestion))
        MBox(0, "Successfully", "Successfully", 32)
        myDB.commit()
        clearContentsUpdateQuestion()

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# delete


def clearContentsDeleteQuestion():
    ui.QLineDCauHoi.clear()
    ui.QLineDIDCauHoi.clear()
    ui.QLineDCauHoi.setDisabled(False)
    ui.QLineDIDCauHoi.setDisabled(False)
    ui.QTableDelete.clearContents()


def suggestDeleteQuestion():
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
        clearContentsDeleteQuestion()
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


# ShowAll
def clearContentsShowAllQuestion():
    ui.QLineSAMaSV.clear()
    ui.QLineSATenSV.clear()
    ui.QLineSADiem.clear()
    ui.QLineSAMaMH.clear()
    ui.QLineSAMaSV.setDisabled(False)
    ui.QLineSATenSV.setDisabled(False)
    ui.QLineSATenSV.setDisabled(False)
    ui.QLineSAMaSV.setDisabled(False)
    ui.QTableShowAll.clearContents()


def suggestShowAllQuestion():
    try:
        cur = myDB.cursor()
        MaSV = ui.QLineSAMaSV.text().strip()
        TenSV = ui.QLineSATenSV.text().strip()
        query = "SELECT dmsv.MaSV,HoSV,TenSV,Phai,NgaySinh,NoiSinh,TenLop,dmkq.MaMH,Diem,TenMH,SoTiet FROM dmsv inner join dmkq on dmsv.MaSV = dmkq.MaSV  inner join dmmh on dmkq.MaMH = dmmh.MaMH WHERE dmsv.MaSV LIKE '%{0}%' AND TenSV LIKE '%{1}%'".format(
            MaSV, TenSV)
        cur.execute(query)
        result = cur.fetchall()

        ui.QTableShowAll.clearContents()
        ui.QTableShowAll.setColumnCount(11)
        ui.QTableShowAll.setRowCount(15)
        columns = 0
        Diem = ''
        for row in result:
            ui.QTableShowAll.setItem(columns, 0, QTableWidgetItem(str(row[0])))
            ui.QTableShowAll.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableShowAll.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableShowAll.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableShowAll.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableShowAll.setItem(columns, 5, QTableWidgetItem(row[5]))
            ui.QTableShowAll.setItem(columns, 6, QTableWidgetItem(row[6]))
            ui.QTableShowAll.setItem(columns, 7, QTableWidgetItem(row[7]))
            if row[8] != None:
                Diem = str(row[8])
            ui.QTableShowAll.setItem(columns, 8, QTableWidgetItem(Diem))
            ui.QTableShowAll.setItem(columns, 9, QTableWidgetItem(row[9]))
            ui.QTableShowAll.setItem(
                columns, 10, QTableWidgetItem(str(row[10])))
            columns += 1

    except sql.Error as e:
        MBox(0, "Error", str(e), 16)


def suggestShowAllQueryQuestion():
    try:
        cur = myDB.cursor()
        Diem = ui.QLineSADiem.text().strip()
        MaMH = ui.QLineSADiem.text().strip()
        query = "SELECT dmsv.MaSV,HoSV,TenSV,Phai,NgaySinh,NoiSinh,TenLop,dmkq.MaMH,Diem,TenMH,SoTiet FROM dmsv inner join dmkq on dmsv.MaSV = dmkq.MaSV  inner join dmmh on dmkq.MaMH = dmmh.MaMH WHERE Diem = %s or dmkq.MaMh = %s"
        cur.execute(query, (Diem, MaMH))
        result = cur.fetchall()
        ui.QTableShowAll.clearContents()
        ui.QTableShowAll.setColumnCount(11)
        ui.QTableShowAll.setRowCount(15)
        columns = 0
        rs = ''
        for row in result:
            ui.QTableShowAll.setItem(columns, 0, QTableWidgetItem(str(row[0])))
            ui.QTableShowAll.setItem(columns, 1, QTableWidgetItem(row[1]))
            ui.QTableShowAll.setItem(columns, 2, QTableWidgetItem(row[2]))
            ui.QTableShowAll.setItem(columns, 3, QTableWidgetItem(row[3]))
            ui.QTableShowAll.setItem(columns, 4, QTableWidgetItem(row[4]))
            ui.QTableShowAll.setItem(columns, 5, QTableWidgetItem(row[5]))
            ui.QTableShowAll.setItem(columns, 6, QTableWidgetItem(row[6]))
            ui.QTableShowAll.setItem(columns, 7, QTableWidgetItem(row[7]))
            if row[8] != None:
                rs = str(row[8])
            ui.QTableShowAll.setItem(columns, 8, QTableWidgetItem(rs))
            ui.QTableShowAll.setItem(columns, 9, QTableWidgetItem(row[9]))
            ui.QTableShowAll.setItem(
                columns, 10, QTableWidgetItem(str(row[10])))
            columns += 1
    except sql.Error as e:
        MBox(0, "Error", str(e), 16)

# -------------------------Student------------------------


def showHomeStudent(info):
    global ui
    # info1 ĐỂ GIỮ LẠI DỮ LIỆU XỬ LÍ DƯỚI CÁC HÀM DƯỚI
    global info1
    info1 = info
    ui = HomeStudent.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    # default tab1
    ui.student.setCurrentWidget(ui.studentprofile)
    # info Student Login
    ui.showmasv.setText(info1[0][0])
    ui.showhosv.setText(info1[0][1])
    ui.showtensv.setText(info1[0][2])
    ui.showphai.setText(info1[0][3])
    ui.showngaysinh.setText(info1[0][4])
    ui.shownoisinh.setText(info1[0][5])
    ui.showtenlop.setText(info1[0][6])
    ui.showpassword.setText(info1[0][7])
    # event clicked for button in THI

    ui.buttonvaothi.clicked.connect(adc)


def adc():
    MaMH = ui.inputmamh.text()
    showTakeTest(MaMH)


def showTakeTest(MaMH):
    # info1 ĐỂ GIỮ LẠI DỮ LIỆU XỬ LÍ DƯỚI CÁC HÀM DƯỚI
    global ui
    print(MaMH)
    ui = TakeTest.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    ui.tabWidget.setCurrentWidget(ui.tab)
    cur = myDB.cursor()
    query = "SELECT * FROM dmch WHERE MaMH = %s "
    cur.execute(query, (MaMH,))
    result = cur.fetchall()
    ui.DSDapAnDB = []
    for item in result:
        ui.DSDapAnDB.append(item[6])

    # cau hoi
    ui.question.setText(result[0][1])
    ui.question_2.setText(result[1][1])
    ui.question_3.setText(result[2][1])
    # ui.question_4.setText(result[3][1])
    # ui.question_5.setText(result[4][1])
    # ui.question_6.setText(result[5][1])
    # ui.question_7.setText(result[6][1])
    # ui.question_8.setText(result[7][1])
    # ui.question_9.setText(result[8][1])
    # ui.question_10.setText(result[9][1])

    # cau tra loi
    ui.A.setText(result[0][2])
    ui.A_2.setText(result[1][2])
    ui.A_3.setText(result[2][2])
    # ui.A_4.setText(result[3][2])
    # ui.A_5.setText(result[4][2])
    # ui.A_6.setText(result[5][2])
    # ui.A_7.setText(result[6][2])
    # ui.A_8.setText(result[7][2])
    # ui.A_9.setText(result[8][2])
    # ui.A_10.setText(result[9][2])

    # CÁC NÚT ĐÁP ÁN CỦA CÁC CÂU HỎI
    # CÂU 1
    ui.A.toggled.connect(onClicked)
    ui.B.toggled.connect(onClicked)
    ui.C.toggled.connect(onClicked)
    ui.D.toggled.connect(onClicked)
    # 2
    ui.A_2.toggled.connect(onClicked)
    ui.B_2.toggled.connect(onClicked)
    ui.C_2.toggled.connect(onClicked)
    ui.D_2.toggled.connect(onClicked)
    # 3
    ui.A_3.toggled.connect(onClicked)
    ui.B_3.toggled.connect(onClicked)
    ui.C_3.toggled.connect(onClicked)
    ui.D_3.toggled.connect(onClicked)
    # 4
    ui.A_4.toggled.connect(onClicked)
    ui.B_4.toggled.connect(onClicked)
    ui.C_4.toggled.connect(onClicked)
    ui.D_4.toggled.connect(onClicked)
    # 5
    ui.A_5.toggled.connect(onClicked)
    ui.B_5.toggled.connect(onClicked)
    ui.C_5.toggled.connect(onClicked)
    ui.D_5.toggled.connect(onClicked)
    # 6
    ui.A_6.toggled.connect(onClicked)
    ui.B_6.toggled.connect(onClicked)
    ui.C_6.toggled.connect(onClicked)
    ui.D_6.toggled.connect(onClicked)
    # 7
    ui.A_7.toggled.connect(onClicked)
    ui.B_7.toggled.connect(onClicked)
    ui.C_7.toggled.connect(onClicked)
    ui.D_7.toggled.connect(onClicked)
    # 8
    ui.A_8.toggled.connect(onClicked)
    ui.B_8.toggled.connect(onClicked)
    ui.C_8.toggled.connect(onClicked)
    ui.D_8.toggled.connect(onClicked)
    # 9
    ui.A_9.toggled.connect(onClicked)
    ui.B_9.toggled.connect(onClicked)
    ui.C_9.toggled.connect(onClicked)
    ui.D_9.toggled.connect(onClicked)
    # 10
    ui.A_10.toggled.connect(onClicked)
    ui.B_10.toggled.connect(onClicked)
    ui.C_10.toggled.connect(onClicked)
    ui.D_10.toggled.connect(onClicked)
    ui.finish.clicked.connect(ketQuaThi)


def onClicked():
    # info1 ĐỂ GIỮ LẠI DỮ LIỆU XỬ LÍ DƯỚI CÁC HÀM DƯỚI
    global diem
    diem = 0

    # TUI ĐANG CHO VÍ DỤ TẤT CẢ ĐÁP ÁN ĐÚNG LÀ A, NẾU SINH VIÊN CHECK A THÌ ĐƯỢC CỘNG 1 ĐIỂM
    if ui.A.isChecked():
        DapAn = ui.A.text()
        # [dp1,dp2,...]
        # ÔNG THAO TÁC VỚI DB GIÚP TUI
        diem += 1
        print(diem)
        # print(result)

    if ui.A_2.isChecked():
        DapAn = ui.A_2.text()
        diem += 1
        print(diem)
        # print(result)

    # câu 3
    if ui.A_3.isChecked():
        DapAn = ui.A_3.text()
        diem += 1
        print(diem)
        # print(result)

    # câu 4
    if ui.A_4.isChecked():
        DapAn = ui.A_4.text()
        diem += 1
        print(diem)
        # print(result)

    # câu 5
    if ui.A_5.isChecked():
        DapAn = ui.A_5.text()

        diem += 1
        print(diem)
        # print(result)

    # câu 6
    if ui.A_6.isChecked():
        DapAn = ui.A_6.text()

        diem += 1
        print(diem)
        # print(result)

    # câu 7
    if ui.A_7.isChecked():
        DapAn = ui.A_7.text()

        diem += 1
        print(diem)
        # print(result)

    # câu 8
    if ui.A_8.isChecked():
        DapAn = ui.A_8.text()

        diem += 1
        print(diem)
        # print(result)

    # câu 9
    if ui.A_9.isChecked():
        DapAn = ui.A_9.text()

        diem += 1
        print(diem)
        # print(result)

    # câu 10
    if ui.A_10.isChecked():
        DapAn = ui.A_10.text()

        diem += 1
        print(diem)
        # print(result)


def ketQuaThi():
    print(ui.DSDapAnDB)
    # ĐÂY LÀ ĐIỂM CỦA SINH VIÊN(info1). ÔNG THAO TÁC VỚI DB GIÚP TUI

    # global diem
    # cur = myDB.cursor()
    # info1[0][0] là mã sinh viên vừa mới hoàn thành bài thi
    # cur.execute('Update dmkq SET Diem = %d where MaSV = %s', diem, info1[0][0])
    # diem = cur.fetchall()

    # if diem == 10:
    #     print("ban xuat sac duoc: " + diem + " diem")
    # elif (diem < 10 and diem > 5):
    #     print("Can co gang them")
    # else:
    #     print("Ban can xem lai viec hoc")


if __name__ == "__main__":
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainUi()
    # showHomeTeacher(123)
    # showStudent()
    # showSubjects()
    # showTakeTest()
    # showHomeStudent()
    # showHomeQuestion()
    sys.exit(app.exec())
