# ==================================================
# Ad Soyad      : Zeynep Bozkurt
# Öğrenci No    : 20253004020
# Tarih         : 22.11.2026
# Dosya         : hafta8_gorev2.py
# Açıklama      : Sayıları farklı sayı tabanlarına dönüştürür
#                 ve farklı tabanlardaki sayıları onluğa çevirir.
# ==================================================

# 16'lık sayı sisteminde kullanılabilecek rakamları tanımlar.
RAKAM = "0123456789ABCDEF"


# Onluk tabandaki sayıyı istenilen tabana dönüştürür.
def onluktan(n, taban):

    # Sayı sıfırsa doğrudan sıfır karakterini döndürür.
    if n == 0:
        return "0"

    sonuc = ""

    # Sayı sıfırdan büyük olduğu sürece kalanları hesaplar.
    while n > 0:
        kalan = n % taban

        # Kalan değerin karşılığını sonucun başına ekler.
        sonuc = RAKAM[kalan] + sonuc

        # Sayıyı tabana bölerek bir sonraki basamağa geçer.
        n = n // taban

    # Dönüştürülen sayıyı metin olarak döndürür.
    return sonuc


# Verilen tabandaki sayıyı onluk tabana dönüştürür.
def onluga(metin, taban):

    # Küçük harfleri büyük harfe dönüştürür.
    metin = metin.upper()

    sonuc = 0

    # Sayının her karakterini sırayla değerlendirir.
    for karakter in metin:

        # Karakterin sayı karşılığını bulur.
        deger = RAKAM.find(karakter)

        # Önceki sonucu tabanla çarpar ve yeni basamağı ekler.
        sonuc = sonuc * taban + deger

    # Onluk tabandaki sonucu döndürür.
    return sonuc


# Fonksiyonların farklı sayı tabanlarıyla test edilmesini sağlar.
print("İkilik:", onluktan(2026, 2))
print("Sekizlik:", onluktan(2026, 8))
print("Onaltılık:", onluktan(2026, 16))

print("7ea:", onluga("7ea", 16))
print("İkilikten:", onluga("11111101010", 2))
print("Sekizlikten:", onluga("3752", 8))
