from PyQt5 import QtWidgets
from src.ui.dialog import Ui_MainWindow
from src.setup import Setup
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    Setup(MainWindow, ui).setup()

    MainWindow.show()
    sys.exit(app.exec_())
