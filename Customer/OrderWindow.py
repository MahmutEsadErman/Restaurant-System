import sys

from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QInputDialog
from PySide6.QtCore import QFile

class OrderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        if __name__ == "__main__":
            ui_file_name = "../uifolder/Order.ui"
        else:
            ui_file_name = "uifolder/Order.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        self.setCentralWidget(self.ui)
        ui_file.close()

        foods = []
        fiyatlar = []

        with open("database/urun_fiyat.txt", "r") as file:
            for lines in file:

                bilgiler = lines.split(" ")
                foods.append(bilgiler[0])
                fiyatlar.append(bilgiler[1])


        # Set the table properties
        self.ui.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set the column width (WIP)
        self.ui.table.setColumnWidth(0, 200)
        self.ui.table.setColumnWidth(1, 200)

        # Connect the cell double click event
        self.ui.table.cellDoubleClicked.connect(self.cell_double_click_event)

        # Set the table headers
        self.ui.table.setRowCount(len(foods))
        self.ui.table.setColumnCount(3)
        self.ui.table.setHorizontalHeaderLabels(("Ürün", "Fiyat", "Adet"))

        # Set the table items
        for i in range(len(foods)):
            self.ui.table.setItem(i, 0, QTableWidgetItem(foods[i]))
            self.ui.table.setItem(i, 1, QTableWidgetItem(fiyatlar[i]))
            self.ui.table.setItem(i, 2, QTableWidgetItem(""))

        # Dictionary to keep the toggled rows
        self.row_colors_toggled = {}

    def cell_double_click_event(self, row, column):

        if row in self.row_colors_toggled:
            # Bu satır zaten değiştirilmiş, eski haline döndür
            for j in range(self.ui.table.columnCount()):
                self.ui.table.item(row, j).setBackground(QColor(255, 255, 255))  # Beyaz renk
            self.ui.table.item(row, 2).setText("")  # Adet sütununu temizle
            del self.row_colors_toggled[row]  # Sözlükten satırı kaldır

        else:
            # Ask the user for the quantity
            quantity, ok = QInputDialog.getInt(self, "Ürün Adedi", "Ürünün Adedini Giriniz: ", 1, 1, 100, 1)
            # Bu satırın rengini değiştir
            for j in range(self.ui.table.columnCount()):
                self.ui.table.item(row, j).setBackground(QColor(173, 216, 230))  # Açık mavi renk
            self.ui.table.item(row, 2).setText(str(quantity))
            self.row_colors_toggled[row] = True  # Satırı değiştirildi olarak işaretle

        # To show the selected rows in the selection label
        self.ui.selections_label.setText("Seçtiğiniz Ürünler: ")
        for i in self.row_colors_toggled:
            self.ui.selections_label.setText(self.ui.selections_label.text()+self.ui.table.item(i, 0).text()+", ")

        # To show the total price in the total price label
        total_price = 0
        for i in self.row_colors_toggled:
            total_price += int(self.ui.table.item(i, 1).text()) * int(self.ui.table.item(i, 2).text())
        self.ui.total_price_label.setText("Toplam Fiyat: "+str(total_price)+" TL")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    sys.exit(app.exec())
