import sys
from PyQt5 import QtWidgets
import see2


def mainUi():
    global ui
    ui = see2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


if __name__ == '__main__':
    ui = ''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainUi()
    sys.exit(app.exec())
