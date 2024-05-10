import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, \
    QPushButton, QMessageBox, QAbstractItemView, QHeaderView
from PySide6.QtCore import QTimer


class CancelWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Siparişler")

        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Tarih, Ürünler
        self.table.setHorizontalHeaderLabels(["Tarih", "Saat", "İşlem"])

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
        orders = []
        kullanici_orders = []
        with open("database/siparisler.txt", "r", encoding='utf-8') as file:

            for satir in file:
                bilgiler = satir.strip().split(",")
                #map(str.rstrip, bilgiler)
                # !!!!!!!!!!!!!!!!!!!!!!!!
                orders.append({"k_adi": bilgiler[0], "date": bilgiler[1], "time": bilgiler[2], "items": bilgiler[3],
                               "fiyat": bilgiler[4], "yorum": bilgiler[5]})
                if orders[0] == self.k_adi:
                    kullanici_orders.append({"k_adi": bilgiler[0], "date": bilgiler[1], "time": bilgiler[2],
                                             "items": bilgiler[3], "fiyat": bilgiler[4], "yorum": bilgiler[5]})

        self.table.setRowCount(len(kullanici_orders))
        for i, order in enumerate(kullanici_orders):
            self.table.setItem(i, 0, QTableWidgetItem(order["date"]))
            self.table.setItem(i, 1, QTableWidgetItem(order["time"]))

            if order["items"] == "x":
            # Add Comment Button
                btn_finalize = QPushButton('Rezervasyonu İptal Et')
                btn_finalize.clicked.connect(lambda ch=True, row=i: self.finalize_order(row))
                self.table.setCellWidget(i, 2, btn_finalize)
            else:
                btn_finalize = QPushButton('Rezervasyonu İptal Et')
                btn_finalize.clicked.connect(lambda ch=True, row=i: self.finalize_order(row))
                self.table.setCellWidget(i, 2, btn_finalize)

    # (WIP) KHALİLİ  Garsonun Sistemi belli bir saniyede bir güncellenecekki yeni siparişler gözüksün
    # Bitti butonuna basıldığında siparişin bitirilmesini sağlar
    def finalize_order(self, row):
        with open("database/aktif_siparisler.txt", "r", encoding='utf-8') as file:
            orders = [line.strip().split(",") for line in file]

        order_to_remove = (self.table.item(row, 0).text(),  # date
                           self.table.item(row, 1).text())  # items

        for order in orders:
            if (order[2], order[3]) == order_to_remove:

                with open("database/siparisler.txt", "a", encoding='utf-8') as dosya:
                    dosya.write(order[0] + "," + order[1] + "," + order[2] + "," + order[3] + "," + order[4] + ",x\n")

                orders.remove(order)
                break

        with open("database/aktif_siparisler.txt", "w", encoding='utf-8') as dosya:
            for order in orders:
                dosya.write(",".join(order) + "\n")

        self.load_orders()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CancelWindow()
    window.show()
    sys.exit(app.exec())