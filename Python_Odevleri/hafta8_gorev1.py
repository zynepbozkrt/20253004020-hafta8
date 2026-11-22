# ==================================================
# Ad Soyad      : Zeynep Bozkurt
# Öğrenci No    : 20253004020
# Tarih         : 22.11.2026
# Dosya         : hafta8_gorev1.py
# Açıklama      : E-posta adreslerinin belirlenen kurallara
#                 uygun olup olmadığını kontrol eder.
# ==================================================


# E-posta adresinin geçerli olup olmadığını kontrol eder.
def eposta_denetle(adres):

    # Adreste tam olarak bir tane @ işareti bulunmasını kontrol eder.
    if adres.count("@") != 1:
        return "Tam olarak bir @ olmalı"

    # @ işaretinin konumunu bulur.
    konum = adres.find("@")

    # Adresi kullanıcı adı ve alan adı olarak ikiye ayırır.
    kullanici = adres[:konum]
    alan = adres[konum + 1:]

    # Kullanıcı adının boş olup olmadığını kontrol eder.
    if kullanici == "":
        return "Kullanıcı adı boş olamaz"

    # Kullanıcı adının nokta ile başlayıp bitmesini engeller.
    if kullanici.startswith(".") or kullanici.endswith("."):
        return "Nokta ile başlayamaz/bitemez"

    # Kullanıcı adındaki karakterlerin geçerliliğini kontrol eder.
    for karakter in kullanici:
        if not (karakter.isalnum() or karakter in "._-"):
            return f"Geçersiz karakter: '{karakter}'"

    # Alan adında en az bir nokta bulunmasını kontrol eder.
    if alan.find(".") == -1:
        return "Alan adı hatalı"

    # Alan adının nokta ile başlayıp bitmesini engeller.
    if alan.startswith(".") or alan.endswith("."):
        return "Alan adı hatalı"

    # E-posta adresinde art arda iki nokta bulunmasını engeller.
    if adres.find("..") != -1:
        return "Ardışık iki nokta kullanılamaz"

    # Bütün kontroller başarılıysa geçerli sonucunu döndürür.
    return "Geçerli"


# Fonksiyonun farklı e-posta adresleriyle test edilmesini sağlar.
print(eposta_denetle("ece.yilmaz@nisantasi.edu.tr"))
print(eposta_denetle("ece@@mail.com"))
print(eposta_denetle("ece yilmaz@mail.com"))
print(eposta_denetle(".ece@mail.com"))
print(eposta_denetle("ece.@mail.com"))
print(eposta_denetle("ece@mail"))
print(eposta_denetle("ece@.mail.com"))
print(eposta_denetle("ece@mail.com."))
print(eposta_denetle("ece..yilmaz@mail.com"))
print(eposta_denetle("ece@mail..com"))