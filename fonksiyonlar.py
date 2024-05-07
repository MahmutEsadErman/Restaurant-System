
#Ne zaman hata vereceğiz??????
def uyeOl():
    ad = input("Adınızı girin: ")
    soyad = input("Soyadınızı girin: ")

    ad_soyad = ad + " " + soyad

    kullanici_adi = input("Kullanıcı adınız: ")
    sifre = input("Şifreniz: ")

    with open("database/kullanicilar.txt", "a") as dosya:
        dosya.write(ad_soyad + "-" + kullanici_adi + "-" + sifre + "\n")

    print("Bilgiler başarıyla kaydedildi.")


def girisYap():

    kullanici_adi = input("Kullanıcı adınız: ")
    sifre = input("Şifreniz: ")

    with open("database/kullanicilar.txt", "r") as dosya:

        for satir in dosya:
            bilgiler = satir.strip().split("-")
            if bilgiler[1] == kullanici_adi and bilgiler[2] == sifre:
                return True

    return False


def fiyatBelirle():

    with open("database/urun_fiyat.txt", "r") as file:
        lines = file.readlines()

    yemek = input("Yemek: ")
    fiyat = input("Fiyat: ")

    updated_lines = []

    for line in lines:

        if yemek.lower() in line.lower():
            updated_lines.append(yemek.capitalize() + " " + fiyat + "\n")
        else:
            updated_lines.append(line)

    with open("database/urun_fiyat.txt", "w") as file:
        file.writelines(updated_lines)

    print("Fiyat Guncellendi")


def stokGuncelle():
    with open("database/stoklar.txt", "r") as file:
        lines = file.readlines()

    yemek = input("Yemek: ")
    adet = input("Adet: ")

    updated_lines = []

    for line in lines:

        if yemek.lower() in line.lower():
            updated_lines.append(yemek.capitalize() + " " + adet + "\n")
        else:
            updated_lines.append(line)

    with open("database/stoklar.txt", "w") as file:
        file.writelines(updated_lines)

    print("Stok Guncellendi")


def yeniUrunEkle():

    yemek = input("Yemek: ")
    fiyat = input("Fiyat:")
    adet = input("Adet: ")

    with open("database/stoklar.txt", "a") as file:

        file.write(yemek + " " + adet + "\n")
        print("Urun Eklendi")

    with open("database/urun_fiyat.txt", "a") as file:
        file.write(yemek + " " + fiyat + "\n")
