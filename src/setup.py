from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from src.ui.dialog import Ui_MainWindow
from src.data import Data
from src.stats import Stats
import json


class Setup(Ui_MainWindow):
    def __init__(self, MainWindow: QMainWindow, ui: Ui_MainWindow):
        super().__init__()
        self.ui = ui
        self.MainWindow = MainWindow
        self.data_original = {}
        self.data_current = {}

    def setup(self):
        self.ui.buttonFolder.clicked.connect(lambda: self.select_file())
        self.ui.buttonData.clicked.connect(lambda: self.process_data())
        self.ui.buttonShowData.clicked.connect(
            lambda: self.show_data(self.data_current)
        )
        self.ui.buttonShowStat.clicked.connect(lambda: self.show_stats())

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self.MainWindow,
            "Sélectionner un fichier",
            "",
            "Fichiers json (*.json);;Fichiers csv (*.csv)",
        )
        if file:
            self.ui.inputFolder.setText(file)

    def process_data(self):
        if not self.ui.inputFolder.text():
            QMessageBox.warning(
                self.MainWindow, "Erreur", "Veuillez sélectionner un fichier"
            )
            return
        self.ui.dataOutput.clear()
        self.data_original = Data().process(self.ui.inputFolder.text())
        self.data_current = self.data_original
        self.show_data(self.data_current)

    def show_data(self, data: dict):
        self.ui.dataOutput.setPlainText(json.dumps(data, indent=4))

    def show_stats(self):
        data = Stats(self.ui).get_stats(self.data_current)
        self.show_data(data)
