from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from src.ui.dialog import Ui_MainWindow
from src.data import Data
import json
import sys

class Setup(Ui_MainWindow):
    def __init__(self, MainWindow: QMainWindow, ui: Ui_MainWindow):
        super().__init__()
        self.ui = ui
        self.MainWindow = MainWindow
        self.data = {}

    def setup(self):
        self.ui.buttonFolder.clicked.connect(lambda: self.select_file())
        self.ui.buttonData.clicked.connect(lambda: self.process_data())

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self.MainWindow, "Sélectionner un fichier", "", "Fichiers json (*.json);;Fichiers csv (*.csv)")
        if file:
            self.ui.inputFolder.setText(file)

    def process_data(self):
        if not self.ui.inputFolder.text():
            QMessageBox.warning(self.MainWindow, "Erreur", "Veuillez sélectionner un fichier")
            return
        self.ui.dataOutput.clear()
        self.data = Data().process(self.ui.inputFolder.text())
        print(self.data)
        self.ui.dataOutput.setPlainText(json.dumps(self.data, indent=4))