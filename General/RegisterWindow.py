import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QFile


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the ui file
        if __name__ == "__main__":
            ui_file_name = "../uifolder/Register.ui"
        else:
            ui_file_name = "uifolder/Register.ui"
        ui_file = QFile(ui_file_name)
        self.ui = QUiLoader().load(ui_file)
        ui_file.close()
        self.setCentralWidget(self.ui)

        self.ui.signup_button.clicked.connect(lambda: self.uyeOl())

    def uyeOl(self):

        ad_soyad = self.ui.lineEdit.text()

        kullanici_adi = self.ui.lineEdit_5.text()

        e_posta = self.ui.lineEdit_4.text()

        cep_telefonu = self.ui.lineEdit_2.text()

        sifre = self.ui.lineEdit_3.text()

        k_adlari = []
        mailler = []
        numaralar = []

        with open("database/kullanicilar.txt", "r", encoding='utf-8') as dosya:
            for satir in dosya:
                bilgiler = satir.strip().split("-")
                k_adlari.append(bilgiler[1])
                mailler.append(bilgiler[2])
                numaralar.append(bilgiler[3])

        if kullanici_adi in k_adlari:
            QMessageBox.warning(self, "Uyarı", "Bu kullanıcı adı zaten alınmış.")
            return False
        elif e_posta in mailler:
            QMessageBox.warning(self, "Uyarı", "Bu E-posta zaten alınmış.")
            return False
        elif cep_telefonu in numaralar:
            QMessageBox.warning(self, "Uyarı", "Bu telefon numarası zaten alınmış.")
            return False

        else:
            with open("database/kullanicilar.txt", "a", encoding='utf-8') as dosya:
                dosya.write(ad_soyad + "-" + kullanici_adi + "-" + cep_telefonu + "-" + sifre + "\n")
            return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec())
