import sys

from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, \
    QInputDialog
from PySide6.QtCore import QFile

# (WORK IN PROGRESS)
class ReportWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        if __name__ == "__main__":
            ui_file_name = "../uifolder/ProductManagement.ui"
        else:
            ui_file_name = "uifolder/ProductManagement.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        self.setCentralWidget(self.ui)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReportWindow()
    window.show()
    sys.exit(app.exec())
