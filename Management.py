import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from Customer.MainMenu import MainMenu
from General.LoginWindow import LoginWindow
from General.RegisterWindow import RegisterWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Window Title
        self.setWindowTitle("Restoran Sistemi (Yönetici)")

        # Set initial windows size
        self.screenSize = QApplication.primaryScreen().size()
        self.resize(800, 640)

        # Move Window to Center
        self.move(self.screenSize.width() / 2, self.screenSize.height() / 2)

        # Setting Pages
        self.stackedWidget = QStackedWidget()
        self.loginWindow = LoginWindow()
        self.registerWindow = RegisterWindow()
        self.mainmenu = MainMenu()

        self.stackedWidget.addWidget(self.loginWindow)
        self.stackedWidget.addWidget(self.registerWindow)
        self.stackedWidget.addWidget(self.mainmenu)
        self.stackedWidget.setCurrentWidget(self.loginWindow)

        # Add Stacked Widget to the layout
        self.setCentralWidget(self.stackedWidget)

        #  SET BUTTONS
        #  Main Window buttons
        self.loginWindow.ui.login_button.clicked.connect()

    def gotoPage(self, window):
        self.stackedWidget.setCurrentWidget(window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
