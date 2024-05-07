import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, \
    QPushButton, QMessageBox, QAbstractItemView, QInputDialog
from PySide6.QtCore import QThread, Signal


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
        self.table.setColumnCount(3)  # Tarih, Ürünler, Yorum Butonu
        self.table.setHorizontalHeaderLabels(["Saat", "Masa no", "Ürünler", "Bitirme"])

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.cell_double_click_event)

        # Back Button
        back_button = QPushButton("Geri dön")

        self.load_orders()  # Sipariş verilerini yükler

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

    def load_orders(self, data):
        # Örnek veriler !! Khalili bunu dosyadan okuyacak şekilde düzenlemek lazım
        data = orders = [
            {"date": "2023-05-01", "items": "Pizza, Kola"},
            {"date": "2023-05-02", "items": "Makarna, Su"},
            {"date": "2023-05-03", "items": "Salata, Ayran"},
            {"date": "2023-05-04", "items": "Kebap, Ayran"}
        ]

        self.table.setRowCount(len(data))
        for i, order in enumerate(data):
            self.table.setItem(i, 0, QTableWidgetItem(order["date"]))
            self.table.setItem(i, 1, QTableWidgetItem(order["items"]))

            # Add Comment Button
            btn_comment = QPushButton('Yorum Yap')
            btn_comment.clicked.connect(lambda ch=True, row=i: self.make_comment(row))
            self.table.setCellWidget(i, 2, btn_comment)

    # (WIP) KHALİLİ  Garsonun Sistemi belli bir saniyede bir güncellenecekki yeni siparişler gözüksün


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrdersWindow()
    window.show()
    sys.exit(app.exec())
