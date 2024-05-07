import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox

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

        #  SET BUTTONS FUNCTIONS
        # Login Window
        self.loginWindow.ui.login_button.clicked.connect(self.login)
        self.loginWindow.ui.register_button.clicked.connect(lambda: self.gotoPage(self.registerWindow))
        # Register Window
        self.registerWindow.ui.signup_button.clicked.connect(self.register)
        self.registerWindow.ui.login_button.clicked.connect(lambda: self.gotoPage(self.loginWindow))
        # MainMenu Window
        self.mainmenu.ui.button1.clicked.connect(lambda: self.gotoPage(self.reservationWindow))
        self.mainmenu.ui.button2.clicked.connect(lambda: self.gotoPage(self.orderWindow))
        self.mainmenu.ui.button3.clicked.connect(lambda: self.gotoPage(self.historyWindow))
        self.mainmenu.ui.button4.clicked.connect(lambda: self.gotoPage(self.loginWindow))
        # Order Window
        self.orderWindow.ui.back_button.clicked.connect(lambda: self.gotoPage(self.mainmenu))
        # Reservation Window
        self.reservationWindow.ui.back_button.clicked.connect(lambda: self.gotoPage(self.mainmenu))
        # History Window
        self.historyWindow.back_button.clicked.connect(lambda: self.gotoPage(self.mainmenu))


    def register(self):
        if self.registerWindow.uyeOl():
            self.gotoPage(self.loginWindow)

    def login(self):
        if self.loginWindow.girisYap():
            self.gotoPage(self.mainmenu)
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

    def gotoPage(self, window):
        self.stackedWidget.setCurrentWidget(window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
