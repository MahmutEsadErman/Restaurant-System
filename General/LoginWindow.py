import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        if __name__ == "__main__":
            ui_file_name = "../uifolder/Login.ui"
        else:
            ui_file_name = "uifolder/Login.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        ui_file.close()
        self.setCentralWidget(self.ui)

        self.ui.login_button.clicked.connect(lambda : print("Login"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
