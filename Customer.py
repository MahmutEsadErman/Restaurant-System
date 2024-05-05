import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from General.LoginWindow import LoginWindow
from General.RegisterWindow import RegisterWindow
from Customer.MainMenu import MainMenu
from Customer.OrderWindow import OrderWindow
from Customer.ReservationWindow import ReservationWindow
from Customer.HistoryWindow import HistoryWindow
from Customer.PaymentWindow import PaymentWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Window Title
        self.setWindowTitle("Restoran Sistemi (Müşteri)")

        # Set initial windows size
        self.screenSize = QApplication.primaryScreen().size()
        self.resize(800, 640)

        # Move Window to Center
        self.move(self.screenSize.width() / 2, self.screenSize.height() / 2)

        # Setting Pages
        self.stackedWidget = QStackedWidget()
        self.loginWindow = LoginWindow()
        self.mainmenu = MainMenu()
        self.registerWindow = RegisterWindow()
        self.orderWindow = OrderWindow()
        self.reservationWindow = ReservationWindow()
        self.historyWindow = HistoryWindow()

        self.stackedWidget.addWidget(self.loginWindow)
        self.stackedWidget.addWidget(self.registerWindow)
        self.stackedWidget.addWidget(self.mainmenu)
        self.stackedWidget.addWidget(self.orderWindow)
        self.stackedWidget.addWidget(self.reservationWindow)
        self.stackedWidget.addWidget(self.historyWindow)
        self.stackedWidget.setCurrentWidget(self.loginWindow)

        # Add Stacked Widget to the layout
        self.setCentralWidget(self.stackedWidget)

        #  SET BUTTONS
        self.loginWindow.ui.login_button.clicked.connect(self.buttonFunctions)
        # self.loginWindow.ui.register_button.clicked.connect(self.buttonFunctions)
        # self.registerWindow.ui.register_button.clicked.connect(self.buttonFunctions)
        self.mainmenu.ui.button1.clicked.connect(self.buttonFunctions)
        self.mainmenu.ui.button2.clicked.connect(self.buttonFunctions)
        self.mainmenu.ui.button3.clicked.connect(self.buttonFunctions)
        self.reservationWindow.ui.exit_button.clicked.connect(self.buttonFunctions)
        self.orderWindow.ui.exit_button.clicked.connect(self.buttonFunctions)


    def buttonFunctions(self):
        button = self.sender()

        # PAGE WIDGETS
        if button.objectName() == "exit_button":
            self.stackedWidget.setCurrentWidget(self.mainmenu)
        if button.objectName() == "login_button":
            self.stackedWidget.setCurrentWidget(self.mainmenu)
        if button.objectName() == "button1":
            self.stackedWidget.setCurrentWidget(self.reservationWindow)
        if button.objectName() == "button2":
            self.stackedWidget.setCurrentWidget(self.orderWindow)
        if button.objectName() == "button3":
            self.stackedWidget.setCurrentWidget(self.historyWindow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
