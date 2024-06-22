from PyQt5.QtWidgets import QMainWindow, QDialog, QFileDialog
from src.ui.dialog import Ui_MainWindow
import json
import sys

class Setup(Ui_MainWindow):
    def __init__(self, MainWindow: QMainWindow, ui: Ui_MainWindow):
        super().__init__()
        self.ui = ui
        self.MainWindow = MainWindow

    def setup(self):
        main_container = self.MainWindow.centralWidget()
        self.ui.buttonFolder.clicked.connect(lambda: self.select_file())

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self.MainWindow, "Sélectionner un fichier", "", "Fichiers json (*.json);;Fichiers csv (*.csv)")
        if file:
            self.ui.inputFolder.setText(file)