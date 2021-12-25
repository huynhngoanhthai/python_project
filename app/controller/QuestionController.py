from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit, QTableWidgetItem
from messageBox import MBox
from database import myDB
from main import isCheckedEmpty, showHomeQuestion, ui
import mysql.connector as sql
import sys
sys.path.append('../')


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


def ClearContentsAddQuestion():
    ui.QLineAQuestion.clear()
    ui.QLineAOPA.clear()
    ui.QLineAOPB.clear()
    ui.QLineAOPC.clear()
    ui.QLineAOPD.clear()
    ui.QLineAAnswer.clear()
    ui.QLineAMaMH.clear()
