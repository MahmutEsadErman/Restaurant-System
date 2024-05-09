import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem, \
    QPushButton, QMessageBox, QAbstractItemView, QInputDialog

from Customer.OrderWindow import OrderWindow


class HistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.k_adi = None

        self.setWindowTitle("Geçmiş Siparişler")

        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Tarih, Ürünler, Yorum Butonu
        self.table.setHorizontalHeaderLabels(["Tarih", "Ürünler", "Yorum", "Sipariş Durumu"])

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.cell_double_click_event)

        self.load_orders()  # Sipariş verilerini yükler

        # Back Button
        self.back_button = QPushButton("Geri dön")

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.back_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def cell_double_click_event(self, row, column):
        QMessageBox.information(self, "Bilgi", self.table.item(row, column).text())

    #!!!!!!!!!!!!!!!!!!!!!!!! Değiştirdiğim yerlere bundan koydum zaten git ten de bakabilirsin
    def load_orders(self):
        # Örnek veriler
        #*********************
        orders = []
        kullanici_orders = []
        with open("database/siparisler.txt", "r", encoding='utf-8') as file:

            for satir in file:
                bilgiler = satir.strip().split(",")
                map(str.rstrip, bilgiler)
                #!!!!!!!!!!!!!!!!!!!!!!!!
                orders.append({"k_adi": bilgiler[0], "date": bilgiler[1], "time": bilgiler[2], "items": bilgiler[3],
                               "fiyat": bilgiler[4], "yorum": bilgiler[5], "siparis": bilgiler[6]})
                if bilgiler[0] == self.k_adi:
                    kullanici_orders.append({"k_adi": bilgiler[0], "date": bilgiler[1], "time": bilgiler[2],
                                     "items": bilgiler[3], "fiyat": bilgiler[4], "yorum": bilgiler[5],
                                     "siparis": bilgiler[6]})

        self.table.setRowCount(len(kullanici_orders))
        for i, order in enumerate(kullanici_orders):

            self.table.setItem(i, 0, QTableWidgetItem(order["date"]))
            self.table.setItem(i, 1, QTableWidgetItem(order["items"]))

            if order["yorum"] == "x":
                # Add Comment Button
                btn_comment = QPushButton('Yorum Yap')
                btn_comment.clicked.connect(lambda ch=True, row=i: self.make_comment(row, orders, kullanici_orders))
                self.table.setCellWidget(i, 2, btn_comment)
            else:
                self.table.setItem(i, 2, QTableWidgetItem(order["yorum"]))

            #!!!!!!!!!!!!!!!!!!!!!!!!
            if order["siparis"] == "x":
                # Add Comment Button
                btn_comment = QPushButton('Siparis Yap')
                btn_comment.clicked.connect(lambda ch=True, row=i: self.give_order(row, orders))
                self.table.setCellWidget(i, 3, btn_comment)
            else:
                self.table.setItem(i, 3, QTableWidgetItem("Sipariş Yapıldı"))

    # (WIP) Khalili
    def make_comment(self, row, orders, kullanici_orders):
        comment, ok = QInputDialog().getText(None, "Input Dialog", "Bir metin girin:")
        if ok and comment:
            self.table.setCellWidget(row, 2, None)
            self.table.setItem(row, 2, QTableWidgetItem(comment))

        #YORUMU YAPAN KULLANICI????????????
        # Save comment to the database

        if kullanici_orders[row] in orders:
            row_index = orders.index(kullanici_orders[row])
            orders[row_index]["yorum"] = comment

        with open("database/siparisler.txt", "w", encoding='utf-8') as file:
            for j in range(len(orders)):
                file.write(orders[j]["k_adi"] + "," + orders[j]["date"] + "," + orders[j]["time"] + "," + orders[j][
                    "items"] + "," + orders[j]["fiyat"] + "," + orders[j]["yorum"] + ",hfffff\n")

    # (WIP) Khalili, Esadi
    # Buraya benim bakmam da gerekebilir Sen Bana haber verirsin Halil abi
    """"
    def give_order(self, row, orders):
        self.orderwindow = OrderWindow()
        self.orderwindow.show()
        self.orderwindow.ui.order_button.clicked.connect(lambda: self.orderwindow.hide())
        pass
    """

    def update_k_adi(self, k_adi):
        self.k_adi = k_adi
        self.load_orders()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HistoryWindow()
    window.show()
    sys.exit(app.exec())
