from PyQt5.QtWidgets import QDialog, QCheckBox, QVBoxLayout
from src.ui.filter import Ui_Dialog
import copy


class Filter:
    def __init__(self, parent, data_original: dict):
        self.data_original = data_original
        self.filter_dialog = QDialog()
        self.filter_ui = Ui_Dialog()
        self.parent = parent
        self.filter_ui.setupUi(self.filter_dialog)
        self.filter_ui.buttonApply.clicked.connect(lambda: self.apply())
        self.filter_ui.buttonCancel.clicked.connect(lambda: self.filter_dialog.close())

    def show(self):
        array_key = ""
        for key in self.data_original.keys():
            array_key = key

        if not self.filter_ui.widgetCheck.layout():
            self.filter_ui.comboBoxKey.addItem("")
            layout = QVBoxLayout()
            for key, value in self.data_original[array_key][0].items():
                checkbox = QCheckBox(key)
                checkbox.setChecked(True)
                layout.addWidget(checkbox)
                if isinstance(value, str) or isinstance(value, list):
                    self.filter_ui.comboBoxKey.addItem(key)

            self.filter_ui.widgetCheck.setLayout(layout)
        self.filter_dialog.show()

    def apply(self):
        array_key = ""
        for key in self.data_original.keys():
            array_key = key

        self.parent.data_current = copy.deepcopy(self.data_original)

        if self.filter_ui.comboBoxKey.currentText() != "":
            filtered_key = self.filter_ui.comboBoxKey.currentText()
            filtered_value = self.filter_ui.inputKey.text()

            if "," in filtered_value:
                filtered_value = filtered_value.split(",")
                filtered_value = [value.strip() for value in filtered_value]

            if isinstance(self.data_original[array_key][0][filtered_key], str):
                filtered_data = [
                    data
                    for data in self.parent.data_current[array_key]
                    if str(data[filtered_key]).lower() == str(filtered_value).lower()
                ]
            if isinstance(self.data_original[array_key][0][filtered_key], list):
                filtered_data = [
                    data
                    for data in self.parent.data_current[array_key]
                    if any(
                        str(fv).lower()
                        in [
                            str(v).lower()
                            for v in (
                                data[filtered_key]
                                if isinstance(data[filtered_key], list)
                                else [data[filtered_key]]
                            )
                        ]
                        for fv in (
                            filtered_value
                            if isinstance(filtered_value, list)
                            else [filtered_value]
                        )
                    )
                ]

            self.parent.data_current[array_key] = filtered_data

        for checkbox in self.filter_ui.widgetCheck.findChildren(QCheckBox):
            if not checkbox.isChecked():
                key = checkbox.text()
                for i, _ in enumerate(self.parent.data_current[array_key]):
                    del self.parent.data_current[array_key][i][key]

        self.filter_dialog.close()
        self.parent.show_data(self.parent.data_current)
