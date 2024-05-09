import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, \
    QPushButton, QMessageBox, QAbstractItemView, QHeaderView
from PySide6.QtCore import QTimer


class OrdersWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Siparişler")

        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Tarih, Ürünler
        self.table.setHorizontalHeaderLabels(["Saat", "Masa", "Ürünler", "Bitirme"])

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.cell_double_click_event)

        # Back Button
        self.back_button = QPushButton("Geri dön")


        self.load_orders()  # Sipariş verilerini yükler
        self.order_timer = QTimer(self)
        self.order_timer.timeout.connect(self.load_orders)
        self.order_timer.start(1000)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.back_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def cell_double_click_event(self, row, column):
        QMessageBox.information(self, "Bilgi", self.table.item(row, column).text())

    def load_orders(self):
        data = []
        with open("database/aktif_siparisler.txt", "r", encoding='utf-8') as file:

            for satir in file:
                bilgiler = satir.strip().split(",")
                #map(str.rstrip, bilgiler)
                if bilgiler[4] != "x":
                    data.append({"date": bilgiler[5], "masa": bilgiler[1], "items": bilgiler[6]})

        self.table.setRowCount(len(data))
        for i, order in enumerate(data):
            self.table.setItem(i, 0, QTableWidgetItem(order["date"]))
            self.table.setItem(i, 1, QTableWidgetItem(order["masa"]))
            self.table.setItem(i, 2, QTableWidgetItem(order["items"]))

            # Add Comment Button
            btn_finalize = QPushButton('Bitti')
            btn_finalize.clicked.connect(lambda ch=True, row=i: self.finalize_order(row))
            self.table.setCellWidget(i, 3, btn_finalize)

    # (WIP) KHALİLİ  Garsonun Sistemi belli bir saniyede bir güncellenecekki yeni siparişler gözüksün
    # Bitti butonuna basıldığında siparişin bitirilmesini sağlar
    def finalize_order(self, row):
        with open("database/aktif_siparisler.txt", "r", encoding='utf-8') as file:
            orders = [line.strip().split(",") for line in file]

        order_to_remove = (self.table.item(row, 0).text(),  # date
                           self.table.item(row, 1).text(),  # masa
                           self.table.item(row, 2).text())  # items

        for order in orders:
            if (order[5], order[1], order[6]) == order_to_remove:
                orders.remove(order)
                break

        with open("database/aktif_siparisler.txt", "w", encoding='utf-8') as dosya:
            for order in orders:
                dosya.write(",".join(order) + "\n")

        self.load_orders()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrdersWindow()
    window.show()
    sys.exit(app.exec())
