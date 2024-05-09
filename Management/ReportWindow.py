import sys

from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout

import Raporlar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


# (WORK IN PROGRESS)
class ReportWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.yillik_gelir_figure = Figure()
        Raporlar.yillik_gelir(self.yillik_gelir_figure, 2024)
        self.canvas = FigureCanvasQTAgg(self.yillik_gelir_figure)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReportWindow()
    window.show()
    sys.exit(app.exec())
