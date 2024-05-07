import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, \
    QPushButton, QMessageBox, QAbstractItemView, QInputDialog


class HistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Geçmiş Siparişler")

        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Tarih, Ürünler, Yorum Butonu
        self.table.setHorizontalHeaderLabels(["Tarih", "Ürünler", "Yorum"])

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.cell_double_click_event)

        self.load_orders()  # Sipariş verilerini yükler

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def cell_double_click_event(self, row, column):
        QMessageBox.information(self, "Bilgi", self.table.item(row, column).text())

    def load_orders(self):
        # Örnek veriler
        #*********************
        orders = []

        with open("database/siparisler.txt", "r") as file:

            for satir in file:
                bilgiler = satir.split(" ")
                orders.append({"date": bilgiler[1], "items": bilgiler[4]})


        self.table.setRowCount(len(orders))
        for i, order in enumerate(orders):
            self.table.setItem(i, 0, QTableWidgetItem(order["date"]))
            self.table.setItem(i, 1, QTableWidgetItem(order["items"]))

            # Add Comment Button
            btn_comment = QPushButton('Yorum Yap')
            btn_comment.clicked.connect(lambda ch=True, row=i: self.make_comment(row, i, orders))
            self.table.setCellWidget(i, 2, btn_comment)

    # (WIP)
    def make_comment(self, row, i, orders):
        comment, ok = QInputDialog().getText(None, "Input Dialog", "Bir metin girin:")
        if ok and comment:
            self.table.setCellWidget(row, 2, None)
            self.table.setItem(row, 2, QTableWidgetItem(comment))

        #YORUMU YAPAN KULLANICI????????????
        # Save comment to the database
        with open("database/yorumlar.txt", "a") as file:
            file.write(orders[i]["date"] + "," + orders[i]["items"] + "," + comment+"\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HistoryWindow()
    window.show()
    sys.exit(app.exec())
