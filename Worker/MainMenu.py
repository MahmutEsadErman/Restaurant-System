import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        if __name__ == "__main__":
            ui_file_name = "../uifolder/Mainmenu.ui"
        else:
            ui_file_name = "uifolder/Mainmenu.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        ui_file.close()
        self.setCentralWidget(self.ui)

        # Set Button Texts
        self.ui.button1.setText("Güncel Siparişler")
        self.ui.button2.setText("Stok İşlemleri")
        self.ui.button3.hide()
        self.ui.button4.setText("Çıkış")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
