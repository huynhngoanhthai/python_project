
from database import myDB
import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QRadioButton, QTableWidgetItem
from PyQt5 import QtWidgets
import mysql.connector as sql
# file
import QUIZ as quiz
import see2
import ctypes  # An included library with Python install.


def MBox(buttonStyles: int, title: str, text: str, style: int):
    return ctypes.windll.user32.MessageBoxW(buttonStyles, text, title, style)


def showQuiz():
    global ui
    ui = quiz.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.count = 0
    # database
    MaMH = "a"
    cur = myDB.cursor()
    query = "SELECT * FROM dmch WHERE MaMH = %s "
    cur.execute(query, (MaMH,))
    ui.result = cur.fetchall()

    ui.Question.setText(ui.result[ui.count][1])
    for i in range(2, 6):
        ui.Answer.addItem(ui.result[ui.count][i])
    ui.count += 1
    ui.NEXT.clicked.connect(clickNext)


def clickNext():
    try:

        ui.Question.setText(ui.result[ui.count][1])
        ui.Answer.clear()
        for i in range(2, 6):
            ui.Answer.addItem(ui.result[ui.count][i])
        ui.count += 1
        ui.NEXT.clicked.connect(clickNext)
    except:
        ui.NEXT.setText("Finished!!")
        ui.NEXT.clicked.connect(showsee2)


def finishProgram():
    return MBox(0, "Error", "123", 32)


def showsee2():
    global ui
    ui = see2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


if __name__ == "__main__":
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    showQuiz()
    sys.exit(app.exec())
