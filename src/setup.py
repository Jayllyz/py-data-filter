from PyQt5.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
)
from src.ui.dialog import Ui_MainWindow
from src.data import Data
from src.stats import Stats
from src.filter import Filter
import json
import copy


class Setup(Ui_MainWindow):
    def __init__(self, MainWindow: QMainWindow, ui: Ui_MainWindow):
        super().__init__()
        self.ui = ui
        self.MainWindow = MainWindow
        self.data_original = {}
        self.data_current = {}
        self.filter = None

    def setup(self):
        self.ui.inputFolder.setText(
            "D:/Dev Projects/py-data-filter/test_data/student.json"
        )
        self.ui.buttonFolder.clicked.connect(lambda: self.select_file())
        self.ui.buttonData.clicked.connect(lambda: self.process_data())
        self.ui.buttonShowData.clicked.connect(
            lambda: self.show_data(self.data_current)
        )
        self.ui.buttonShowStat.clicked.connect(lambda: self.show_stats())
        self.ui.buttonFilter.clicked.connect(lambda: self.show_filter_dialog())

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
        self.data_current = copy.deepcopy(self.data_original)
        self.filter = Filter(self, self.data_original)
        self.show_data(self.data_current)

    def show_data(self, data: dict):
        self.ui.dataOutput.setPlainText(json.dumps(data, indent=4))

    def show_stats(self):
        if not self.data_current:
            QMessageBox.warning(
                self.MainWindow, "Erreur", "Auncun fichier n'a été importé"
            )
            return
        data = Stats(self.ui).get_stats(self.data_current)
        self.show_data(data)

    def show_filter_dialog(self):
        if not self.data_original:
            QMessageBox.warning(
                self.MainWindow, "Erreur", "Veuillez récupérer les données"
            )
            return
        self.filter.show()
