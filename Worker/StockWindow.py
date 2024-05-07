import sys

from PySide6.QtGui import QColor, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QInputDialog, QItemDelegate
from PySide6.QtCore import QFile

class StockWindow(QMainWindow):
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

        # Hide the buttons
        self.ui.add_button.hide()
        self.ui.remove_button.hide()

        #************************
        foods = []
        adetler = []

        with open("../database/urun_fiyat.txt", "r") as file:
            for lines in file:
                bilgiler = lines.split(" ")
                foods.append(bilgiler[0])

        with open("../database/stoklar.txt", "r") as file:
            for lines in file:
                adetler.append(lines.split(" ")[1])

        #***************************

        # Set the table properties
        self.ui.table.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Set the column width (WIP)
        self.ui.table.setColumnWidth(0, 200)
        self.ui.table.setColumnWidth(1, 200)

        # Set the table headers
        self.ui.table.setRowCount(len(foods))
        self.ui.table.setColumnCount(2)
        self.ui.table.setHorizontalHeaderLabels(("Ürün", "Adet"))

        # Set the table items
        for i in range(len(foods)):
            self.ui.table.setItem(i, 0, QTableWidgetItem(foods[i]))
            self.ui.table.setItem(i, 1, QTableWidgetItem(adetler[i]))

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

        with open("../database/stoklar.txt", "w") as stoklar_file:
            with open("../database/urun_fiyat.txt", "w") as fiyatlar_file:
                for i in range(self.ui.table.rowCount()):
                    urun = self.ui.table.item(i, 0).text().rstrip()
                    fiyat = self.ui.table.item(i, 1).text().rstrip()
                    adet = self.ui.table.item(i, 2).text().rstrip()

                    stoklar_file.write(f"{urun} {adet}\n")
                    fiyatlar_file.write(f"{urun} {fiyat}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockWindow()
    window.show()
    sys.exit(app.exec())