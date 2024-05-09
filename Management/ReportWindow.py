import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QComboBox

from Management import Raporlar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


# (Still WORK IN PROGRESS)
class ReportWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.yillik_gelir = FigureCanvasQTAgg(Raporlar.yillik_gelir(2024))
        self.yillik_gider = FigureCanvasQTAgg(Raporlar.yillik_gider(2024))
        self.yillik_gelir_gider = FigureCanvasQTAgg(Raporlar.yillik_gelir_gider(2024))
        self.aylik_gelir = FigureCanvasQTAgg(Raporlar.aylik_gelir(2024, 5))

        self.yillik_gelir.setStyleSheet("background-color: red;")

        self.back_button = QPushButton("Geri dön")
        self.back_button.setMaximumSize(140, 50)
        self.combobox = QComboBox()
        self.plots = [self.yillik_gelir, self.yillik_gider, self.yillik_gelir_gider, self.aylik_gelir]
        plots_names = ["Yıllık Gelir", "Yıllık Gider", "Yıllık Gelir-Gider", "Aylık Gelir"]
        self.combobox.addItems(plots_names)
        self.combobox.currentIndexChanged.connect(self.change_plot)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.back_button)
        bottom_layout.addWidget(self.combobox)
        bottom_frame = QWidget()
        bottom_frame.setLayout(bottom_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(bottom_frame)
        self.main_layout.addWidget(self.yillik_gelir)
        self.last_plot = self.yillik_gelir

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def change_plot(self):
        self.main_layout.removeWidget(self.last_plot)
        self.main_layout.addWidget(self.plots[self.combobox.currentIndex()])
        self.last_plot = self.plots[self.combobox.currentIndex()]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReportWindow()
    window.show()
    sys.exit(app.exec())
