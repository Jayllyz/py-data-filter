from PyQt5.QtWidgets import (
    QDialog,
    QCheckBox,
    QVBoxLayout,
)
from src.ui.filter import Ui_Dialog
import copy


class Filter:
    def __init__(self, parent, data_original: dict):
        self.data_original = data_original
        self.filter_dialog = QDialog()
        self.filter_ui = Ui_Dialog()
        self.parent = parent
        self.filtered_data = []
        self.filter_ui.setupUi(self.filter_dialog)
        self.filter_ui.buttonApply.clicked.connect(lambda: self.apply())

    def show(self):
        array_key = ""
        for key in self.data_original.keys():
            array_key = key

        if not self.filter_ui.widgetCheck.layout():
            layout = QVBoxLayout()
            for key in self.data_original[array_key][0].keys():
                checkbox = QCheckBox(key)
                checkbox.setChecked(True)
                layout.addWidget(checkbox)

            self.filter_ui.widgetCheck.setLayout(layout)
        self.filter_dialog.show()

    def apply(self):
        array_key = ""
        for key in self.data_original.keys():
            array_key = key

        self.parent.data_current = copy.deepcopy(self.data_original)

        for checkbox in self.filter_ui.widgetCheck.findChildren(QCheckBox):
            if not checkbox.isChecked():
                key = checkbox.text()
                for i, _ in enumerate(self.parent.data_current[array_key]):
                    del self.parent.data_current[array_key][i][key]

        self.filter_dialog.close()
        self.parent.show_data(self.parent.data_current)
