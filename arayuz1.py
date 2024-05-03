import tkinter as tk
from tkinter import messagebox
import datetime


# Kullanıcılar.txt dosyasını kontrol etme
def verify_customer_login(username, password):
    try:
        with open("database/kullanicilar.txt", "r") as file:
            users = file.readlines()
            for user in users:
                user_info = user.strip().split("-")
                if username == user_info[1] and password == user_info[2]:
                    return True
    except FileNotFoundError:
        with open("database/kullanicilar.txt", "w") as file:
            pass
    return False

# Kullanıcıları.txt dosyasına kaydetme
def save_new_customer(full_name, username, password):
    with open("database/kullanicilar.txt", "a") as file:
        file.write(f"{full_name}-{username}-{password}\n")
    messagebox.showinfo("Kayıt Başarılı", "Başarıyla kaydedildi!")

# Ana menü
def main_menu():
    clear_frame()
    tk.Button(frame, text="Yönetim Girişi", command=admin_login_screen).pack(fill='x')
    tk.Button(frame, text="Müşteri Girişi", command=customer_menu).pack(fill='x')
    tk.Button(frame, text="Çalışan Girişi", command=employee_login_screen).pack(fill='x')

# Yönetim giriş ekranı
def admin_login_screen():
    clear_frame()
    tk.Label(frame, text="Yönetim Girişi", font=('Helvetica', 14)).pack()
    tk.Label(frame, text="Kullanıcı Adı:").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()
    tk.Label(frame, text="Şifre:").pack()
    password_entry = tk.Entry(frame, show='*')
    password_entry.pack()
    tk.Button(frame, text="Giriş Yap", command=lambda: verify_admin(username_entry.get(), password_entry.get())).pack()
    tk.Button(frame, text="Geri", command=main_menu).pack()

# Ana menü fonksiyonları
def fiyatlari_belirle():
    # Fiyat güncelleme penceresi
    def guncelle():
        with open("database/urun_fiyat.txt", "w") as dosya:
            for urun, entry in urun_fiyat_entries.items():
                yeni_fiyat = entry.get()
                dosya.write(f"{urun} {yeni_fiyat}\n\n")
        messagebox.showinfo("Başarılı", "Fiyatlar güncellendi.")
        fiyat_penceresi.destroy()

    fiyat_penceresi = tk.Toplevel()
    fiyat_penceresi.title("Fiyatları Belirle")

    urun_fiyat_entries = {}
    with open("database/urun_fiyat.txt", "r") as dosya:
        for satir in dosya:
            if satir.strip():
                urun, fiyat = satir.split()
                tk.Label(fiyat_penceresi, text=f"{urun} mevcut fiyat: {fiyat}").pack()
                entry = tk.Entry(fiyat_penceresi)
                entry.pack()
                urun_fiyat_entries[urun] = entry

    tk.Button(fiyat_penceresi, text="Güncelle", command=guncelle).pack()

def yorumlari_oku():
    yorum_penceresi = tk.Toplevel()
    yorum_penceresi.title("Yorum ve Şikayetleri Oku")
    with open("database/yorumlar.txt", "r") as dosya:
        for satir in dosya:
            if satir.strip():
                tk.Label(yorum_penceresi, text=satir.strip()).pack()

def stok_goruntule():
    stok_penceresi = tk.Toplevel()
    stok_penceresi.title("Stokları Görüntüle")
    with open("database/stoklar.txt", "r") as dosya:
        for satir in dosya:
            if satir.strip():
                tk.Label(stok_penceresi, text=satir.strip()).pack()


def gelir_gider_raporunu_gor():
    # Bu fonksiyon gelir-gider raporunu gösterecek.
    pass

def yemek_populerligini_gor():
    # Bu fonksiyon yemek popülerliğini gösterecek.
    pass

def raporlari_goruntule():
    # Raporları göstermek için bir pencere aç
    report_window = tk.Toplevel(frame)
    report_window.title("Raporlar")

    # Gelir-Gider Raporunu Göster butonu
    tk.Button(report_window, text="Gelir-Gider Raporunu Gör", command=gelir_gider_raporunu_gor).pack(fill='x', padx=20, pady=10)

    # Yemek Popülerliğini Gör butonu
    tk.Button(report_window, text="Yemek Popülerliğini Gör", command=yemek_populerligini_gor).pack(fill='x', padx=20, pady=10)


# Yönetim menüsü
def admin_menu():
    clear_frame()
    tk.Label(frame, text="Yönetim Menüsü", font=('Helvetica', 16)).pack()
    # Yönetim menüsü butonları burada olacak
    tk.Button(frame, text="Fiyatları Belirle", command=fiyatlari_belirle).pack(fill='x')
    tk.Button(frame, text="Yorum ve Şikayetleri Oku", command=yorumlari_oku).pack(fill='x')
    tk.Button(frame, text="Raporları Görüntüle", command=raporlari_goruntule).pack(fill='x')
    tk.Button(frame, text="Stok Görüntüle", command=stok_goruntule).pack(fill='x')
    tk.Button(frame, text="Çıkış Yap", command=main_menu).pack(fill='x')

# Müşteri menüsü
def customer_menu():
    clear_frame()
    tk.Button(frame, text="Üye Ol", command=customer_register).pack(fill='x')
    tk.Button(frame, text="Giriş Yap", command=customer_login).pack(fill='x')
    tk.Button(frame, text="Geri", command=main_menu).pack(fill='x')

# Çalışan giriş ekranı
def employee_login_screen():
    clear_frame()
    tk.Label(frame, text="Çalışan Girişi", font=('Helvetica', 14)).pack()
    tk.Label(frame, text="Kullanıcı Adı:").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()
    tk.Label(frame, text="Şifre:").pack()
    password_entry = tk.Entry(frame, show='*')
    password_entry.pack()
    tk.Button(frame, text="Giriş Yap", command=lambda: verify_employee(username_entry.get(), password_entry.get())).pack()
    tk.Button(frame, text="Geri", command=main_menu).pack()

# Çalışan menüsü
def employee_menu():
    clear_frame()
    tk.Label(frame, text="Çalışan Menüsü", font=('Helvetica', 16)).pack()
    # Çalışan menüsü butonları burada olacak
    tk.Button(frame, text="Rezervasyonları Görüntüle", command=view_reservations_orders).pack(fill='x')
    tk.Button(frame, text="Stok Sayısını Güncelle", command=update_stock).pack(fill='x')
    tk.Button(frame, text="Çıkış Yap", command=main_menu).pack(fill='x')

# Stokları güncelleme fonksiyonu
def update_stock():
    # Ürünleri okuyup göstermek için bir pencere aç
    stock_window = tk.Toplevel(frame)
    stock_window.title("Stok Güncelleme")

    # 'stoklar.txt' dosyasını oku
    with open('database/stoklar.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    products = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2:
            product = " ".join(parts[:-1])
            quantity = int(parts[-1])
            products[product] = quantity

    # Her ürün için giriş alanları oluştur
    entries = {}
    for product, quantity in products.items():
        row = tk.Frame(stock_window)
        row.pack(fill='x', padx=5, pady=5)

        tk.Label(row, text=f"{product} ({quantity} mevcut):", anchor='w').pack(side='left')

        # Satın alınan adet
        qty_entry = tk.Entry(row, width=5)
        qty_entry.pack(side='left', padx=5)

        # Toplam fiyat
        price_entry = tk.Entry(row, width=10)
        price_entry.pack(side='left', padx=5)

        entries[product] = (qty_entry, price_entry)

    def submit_changes():
        # Güncelleme işlemlerini uygula
        with open('database/stoklar.txt', 'w', encoding='utf-8') as file:
            for product, (qty_entry, price_entry) in entries.items():
                try:
                    purchased_qty = int(qty_entry.get())
                    total_price = float(price_entry.get())
                    new_qty = products[product] + purchased_qty
                    file.write(f"{product} {new_qty}\n")
                except ValueError:
                    continue  # Hatalı girişleri atla

        # Ay-harcama kaydı ekle
        with open('database/gider.txt', 'a', encoding='utf-8') as file:
            month = datetime.datetime.now().strftime("%B")
            for _, (qty_entry, price_entry) in entries.items():
                try:
                    total_price = float(price_entry.get())
                    if total_price > 0:
                        file.write(f"{month}-{total_price}\n")
                except ValueError:
                    continue  # Hatalı girişleri atla

        stock_window.destroy()  # Pencereyi kapat

    # Güncelleme butonu
    submit_btn = tk.Button(stock_window, text="Güncelle", command=submit_changes)
    submit_btn.pack(pady=10)

# Eksik çalışan fonksiyonları
def view_reservations_orders():
    pass

# Üye olma ekranı
def customer_register():
    clear_frame()
    tk.Label(frame, text="Üye Ol", font=('Helvetica', 14)).pack()
    tk.Label(frame, text="Ad Soyad:").pack()
    full_name_entry = tk.Entry(frame)
    full_name_entry.pack()
    tk.Label(frame, text="Kullanıcı Adı:").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()
    tk.Label(frame, text="Şifre:").pack()
    password_entry = tk.Entry(frame, show='*')
    password_entry.pack()
    tk.Button(frame, text="Kaydet", command=lambda: save_new_customer(full_name_entry.get(), username_entry.get(), password_entry.get())).pack()
    tk.Button(frame, text="Geri", command=customer_menu).pack()

# Müşteri giriş ekranı
def customer_login():
    clear_frame()
    tk.Label(frame, text="Giriş Yap", font=('Helvetica', 14)).pack()
    tk.Label(frame, text="Kullanıcı Adı:").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()
    tk.Label(frame, text="Şifre:").pack()
    password_entry = tk.Entry(frame, show='*')
    password_entry.pack()
    tk.Button(frame, text="Giriş Yap", command=lambda: login_customer(username_entry.get(), password_entry.get())).pack()
    tk.Button(frame, text="Geri", command=customer_menu).pack()

# Müşteri başarılı giriş ekranı
def customer_logged_in_menu():
    clear_frame()
    tk.Label(frame, text="Müşteri Menüsü", font=('Helvetica', 16)).pack()
    # Müşteri menüsü butonları burada olacak
    tk.Button(frame, text="Rezervasyon Yap", command=lambda: None).pack(fill='x')
    tk.Button(frame, text="Sipariş Ver", command=lambda: None).pack(fill='x')
    tk.Button(frame, text="Geçmişi Görüntüle", command=lambda: None).pack(fill='x')
    tk.Button(frame, text="Çıkış Yap", command=main_menu).pack(fill='x')

# Ekranı temizleme
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

# Admin giriş doğrulama
def verify_admin(username, password):
    if username == 'admin' and password == '1234':
        admin_menu()
    else:
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya şifre yanlış!")

# Çalışan giriş doğrulama
def verify_employee(username, password):
    if username == 'eleman' and password == '1234':
        employee_menu()
    else:
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya şifre yanlış!")

# Müşteri giriş doğrulama
def login_customer(username, password):
    if verify_customer_login(username, password):
        customer_logged_in_menu()
    else:
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya şifre yanlış ya da kullanıcı mevcut değil!")

# Programın ana bloğu
def main():
    root = tk.Tk()
    root.title("Sistem Giriş Ekranı")

    global frame
    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10)

    main_menu()

    root.mainloop()

# Uygulamayı başlat
if __name__ == "__main__":
    main()
