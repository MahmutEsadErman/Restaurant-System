import sys
from datetime import datetime

from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QInputDialog
from PySide6.QtCore import QFile


class OrderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        self.k_adi = None
        if __name__ == "__main__":
            ui_file_name = "../uifolder/Order.ui"
        else:
            ui_file_name = "uifolder/Order.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        self.setCentralWidget(self.ui)
        ui_file.close()

        self.foods = []
        self.fiyatlar = []
        self.stoklar = []
        self.orders = []
        self.total_price = 0

        with open("database/urun_fiyat.txt", "r", encoding='utf-8') as file:
            for lines in file:
                bilgiler = lines.strip().split(" ")
                self.foods.append(bilgiler[0])
                self.fiyatlar.append(bilgiler[1])

        with open("database/stoklar.txt", "r", encoding='utf-8') as file:
            for lines in file:
                bilgiler = lines.strip().split(" ")
                self.stoklar.append(int(bilgiler[1]))

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
        self.ui.table.setRowCount(len(self.foods))
        self.ui.table.setColumnCount(3)
        self.ui.table.setHorizontalHeaderLabels(("Ürün", "Fiyat", "Adet"))

        # Set the table items
        for i in range(len(self.foods)):
            self.ui.table.setItem(i, 0, QTableWidgetItem(self.foods[i]))
            self.ui.table.setItem(i, 1, QTableWidgetItem(self.fiyatlar[i]))
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
            self.orders.append((self.ui.table.item(row, 0).text(),int(self.ui.table.item(row, 1).text()),quantity))

        # To show the selected rows in the selection label
        self.ui.selections_label.setText("Seçtiğiniz Ürünler: ")
        for i in self.row_colors_toggled:
            self.ui.selections_label.setText(self.ui.selections_label.text() + self.ui.table.item(i, 0).text() + ", ")

        # To show the total price in the total price label
        total_price = 0
        for i in self.row_colors_toggled:
            total_price += int(self.ui.table.item(i, 1).text()) * int(self.ui.table.item(i, 2).text())
        self.ui.total_price_label.setText("Toplam Fiyat: " + str(total_price) + " TL")
        self.total_price = total_price

    def siparisVer(self):

        for i, food in enumerate(self.foods):
            for order in self.orders:
                if food == order[0]:
                    if self.stoklar[i] - order[2] < 0:
                        return False
                    else:
                        self.stoklar[i] -= order[2]

        with open("database/stoklar.txt", "w", encoding='utf-8') as dosya:
            for i in range(len(self.stoklar)):
                dosya.write(self.foods[i] + " " + str(self.stoklar[i])+ "\n")

        siparisler = "-".join("-".join([order[0]] * order[2]) for order in self.orders)

        with open("database/siparisler.txt", "a", encoding='utf-8') as dosya:

            dosya.write(self.k_adi + "," + str(datetime.now().date()) + "," + str(datetime.now().strftime("%H:%M")) + "," +
                        siparisler + "," + str(self.total_price) + ",x,qwerty\n")

        with open("database/aktif_siparisler.txt", "a", encoding='utf-8') as dosya:

            dosya.write(self.k_adi + "," + "5" + str(datetime.now().date()) + "," + str(datetime.now().strftime("%H:%M")) +
                        "," + str(datetime.now().date()) + "," + str(datetime.now().strftime("%H:%M")) + "," +
                        siparisler + str(self.total_price) + "\n")

        with open("database/gelir.txt", "a", encoding='utf-8') as dosya:
            dosya.write(str(datetime.now().year) + " " + str(datetime.now().month) + " " + str(self.total_price) + "\n")

        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    sys.exit(app.exec())
