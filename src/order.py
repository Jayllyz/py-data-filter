from PyQt5.QtWidgets import QDialog
from src.ui.order import Ui_Dialog
import copy


class Order:
    def __init__(self, parent):
        self.data_current = {}
        self.order_dialog = QDialog()
        self.order_ui = Ui_Dialog()
        self.parent = parent
        self.order_ui.setupUi(self.order_dialog)
        self.order_ui.buttonApply.clicked.connect(lambda: self.apply())
        self.order_ui.buttonCancel.clicked.connect(lambda: self.order_dialog.close())

    def show(self, data_current: dict):
        self.data_current = data_current
        array_key = ""
        for key in self.data_current.keys():
            array_key = key

        self.order_ui.comboBoxKey.clear()
        self.order_ui.comboBoxOrder.clear()

        self.order_ui.comboBoxOrder.addItem("ASC")
        self.order_ui.comboBoxOrder.addItem("DESC")

        for key in self.data_current[array_key][0].keys():
            self.order_ui.comboBoxKey.addItem(key)

        self.order_dialog.show()

    def apply(self):
        array_key = ""
        for key in self.data_current.keys():
            array_key = key

        self.parent.data_current = copy.deepcopy(self.data_current)

        if self.order_ui.comboBoxKey.currentText() != "":
            ordered_key = self.order_ui.comboBoxKey.currentText()
            ordered_order = self.order_ui.comboBoxOrder.currentText()

            if ordered_order == "ASC":
                if isinstance(self.data_current[array_key][0][ordered_key], list):
                    self.parent.data_current[array_key].sort(
                        key=lambda x: len(x[ordered_key]), reverse=False
                    )
                else:
                    self.parent.data_current[array_key].sort(
                        key=lambda x: x[ordered_key], reverse=False
                    )
            if ordered_order == "DESC":
                if isinstance(self.data_current[array_key][0][ordered_key], list):
                    self.parent.data_current[array_key].sort(
                        key=lambda x: len(x[ordered_key]), reverse=True
                    )
                else:
                    self.parent.data_current[array_key].sort(
                        key=lambda x: x[ordered_key], reverse=True
                    )

        self.order_dialog.close()
        self.parent.show_data(self.parent.data_current)
