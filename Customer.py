import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Window Title
        self.setWindowTitle("Restoran Sistemi")

        # Set initial windows size
        self.screenSize = QApplication.primaryScreen().size()

        # Move Window to Center
        self.move(self.screenSize.width() / 2, self.screenSize.height() / 2)

        # Setting Pages
        self.stackedWidget = QStackedWidget()
        # self.homepage = HomePage()
        # self.stackedWidget.addWidget(self.indicatorspage)
        # self.stackedWidget.setCurrentWidget(self.homepage)

        #  SET BUTTONS
        #  Main Window buttons



    def buttonFunctions(self):
        button = self.sender()

        # PAGE WIDGETS
        # if button.objectName() == "btn_targets_page":
        #     self.stackedWidget.setCurrentWidget(self.targetspage)
        #     self.label_top_info_2.setText("| Targets")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
