import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, \
    QPushButton, QMessageBox, QAbstractItemView, QInputDialog
from PySide6.QtCore import QThread, Signal
from PySide6.QtCore import QTimer


class UpdateOrdersThread(QThread):
    data_read = Signal()

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            self.data_read.emit()
            self.wait(1)


class OrdersWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Siparişler")

        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Tarih, Ürünler
        self.table.setHorizontalHeaderLabels(["Saat", "Masa", "Ürünler", "Bitirme"])

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.cell_double_click_event)

        # Back Button
        back_button = QPushButton("Geri dön")

        self.load_orders()  # Sipariş verilerini yükler
        self.order_timer = QTimer(self)
        self.order_timer.timeout.connect(self.load_orders)
        self.order_timer.start(1000)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(back_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Start the thread
        self.update_orders_thread = UpdateOrdersThread()
        self.update_orders_thread.data_read.connect(self.load_orders())
        self.update_orders_thread.start()

    def cell_double_click_event(self, row, column):
        QMessageBox.information(self, "Bilgi", self.table.item(row, column).text())

    def load_orders(self):

        data = []
        with open("../database/aktif_siparisler.txt", "r", encoding='utf-8') as file:

            for satir in file:
                bilgiler = satir.strip().split(",")
                data.append({"date": bilgiler[5], "masa": bilgiler[1], "items": bilgiler[6]})

        self.table.setRowCount(len(data))
        for i, order in enumerate(data):
            self.table.setItem(i, 0, QTableWidgetItem(order["date"]))
            self.table.setItem(i, 1, QTableWidgetItem(order["masa"]))
            self.table.setItem(i, 2, QTableWidgetItem(order["items"]))

            # Add Comment Button
            btn_comment = QPushButton('Bitti')
            btn_comment.clicked.connect(lambda ch=True, row=i: self.make_comment(row))
            self.table.setCellWidget(i, 3, btn_comment)

    # (WIP) KHALİLİ  Garsonun Sistemi belli bir saniyede bir güncellenecekki yeni siparişler gözüksün

    def make_comment(self, row):
        orders = []
        with open("../database/aktif_siparisler.txt", "r", encoding='utf-8') as file:

            for satir in file:
                bilgiler = satir.strip().split(",")
                orders.append({"k_adi": bilgiler[0], "masa": bilgiler[1], "r_tarih": bilgiler[2], "r_saat": bilgiler[3],
                               "tarih": bilgiler[4], "saat": bilgiler[5], "items": bilgiler[6], "fiyat": bilgiler[7]})

            del orders[row]

        with open("../database/aktif_siparisler.txt", "w", encoding='utf-8') as file:
            for order in orders:

                order_line = ",".join([
                    order["k_adi"], order["masa"], order["r_tarih"], order["r_saat"],
                    order["tarih"], order["saat"], order["items"], order["fiyat"]
                ])
                file.write(order_line + "\n")
        self.load_orders()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrdersWindow()
    window.show()
    sys.exit(app.exec())
