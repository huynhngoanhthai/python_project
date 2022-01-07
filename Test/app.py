
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
    # database

    ui.NEXT.clicked.connect(adc)


def adc():
    print(ui.Answer.currentText())


if __name__ == "__main__":
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    showQuiz()
    sys.exit(app.exec())
