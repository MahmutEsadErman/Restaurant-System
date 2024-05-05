import sys

from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QInputDialog
from PySide6.QtCore import QFile

class ProductManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        if __name__ == "__main__":
            ui_file_name = "../uifolder/ProductManagement.ui"
        else:
            ui_file_name = "uifolder/ProductManagement.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        self.setCentralWidget(self.ui)
        ui_file.close()

        foods = ["börek", "çörek", "kebap"]
        fiyatlar = ["100", "50", "120"]

        # Set the table properties
        self.ui.table.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Set the column width (WIP)
        self.ui.table.setColumnWidth(0, 200)
        self.ui.table.setColumnWidth(1, 200)

        # Set the table headers
        self.ui.table.setRowCount(len(foods))
        self.ui.table.setColumnCount(3)
        self.ui.table.setHorizontalHeaderLabels(("Ürün", "Fiyat", "Adet"))

        # Set the table items
        for i in range(len(foods)):
            self.ui.table.setItem(i, 0, QTableWidgetItem(foods[i]))
            self.ui.table.setItem(i, 1, QTableWidgetItem(fiyatlar[i]))
            self.ui.table.setItem(i, 2, QTableWidgetItem(""))

        # Set button actions
        self.ui.add_button.clicked.connect(self.add_item)
        self.ui.remove_button.clicked.connect(self.remove_item)
        self.ui.save_button.clicked.connect(self.save_items)

    def add_item(self):
        self.ui.table.insertRow(self.ui.table.rowCount())

    def remove_item(self):
        self.ui.table.removeRow(self.ui.table.currentRow())

    # (WIP)
    def save_items(self):
        # Khalili
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductManagementWindow()
    window.show()
    sys.exit(app.exec())
