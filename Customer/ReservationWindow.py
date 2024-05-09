import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QFile


class ReservationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        if __name__ == "__main__":
            ui_file_name = "../uifolder/Reservation.ui"
        else:
            ui_file_name = "uifolder/Reservation.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        ui_file.close()
        self.setCentralWidget(self.ui)


    def end_reservation(self):
        #!!Khalili
        # Rezervasyon fonksiyonu


        ans = QMessageBox.question("Randevu", "Siparişinizi şimdi vermek ister misiniz?")
        if ans == QMessageBox.Yes:
            return True
        else:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationWindow()
    window.show()
    sys.exit(app.exec())
