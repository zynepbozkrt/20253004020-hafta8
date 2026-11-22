# ==================================================
# Ad Soyad      : Zeynep Bozkurt
# Öğrenci No    : 20253004020
# Tarih         : 22.11.2026
# Dosya         : hafta8_gorev5.py
# Açıklama      : Açıklama: Türkçe alfabeye göre kelime karşılaştırması
#                 yapan TrKelime sınıfının ve Roma rakamı dönüştürme
#                 fonksiyonlarının oluşturulması.
# ==================================================

ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"


class TrKelime:

    def __init__(self, metin):
        self.metin = metin.replace("I", "ı").replace("İ", "i").lower()
#Metni Türkçe kurallara göre küçültür.
    def __str__(self):
        return self.metin
#Kelimeyi metin olarak döndürür.
    def __len__(self):
        return len(self.metin)
# Kelimenin karakter sayısını döndürür.
    def __getitem__(self, indeks):
        return self.metin[indeks]
#İndeks veya dilim kullanarak karakter seçer.
    def __contains__(self, aranan):
        return aranan in self.metin
#Aranan metnin kelimede bulunup bulunmadığını kontrol eder.
    def __eq__(self, diger):
        if isinstance(diger, TrKelime):
            return self.metin == diger.metin
        return NotImplemented
#Eşitlik kontrolü yapar ve diğer nesne TrKelime değilse NotImplemented döndürür.
    def __lt__(self, diger):
        if not isinstance(diger, TrKelime):
            return NotImplemented
#Türkçe alfabeye göre kelime karşılaştırması yapar ve diğer nesne TrKelime değilse NotImplemented döndürür.
        for harf1, harf2 in zip(self.metin, diger.metin):
            sira1 = ALFABE.find(harf1)
            sira2 = ALFABE.find(harf2)

            if sira1 != sira2:
                return sira1 < sira2

        return len(self.metin) < len(diger.metin)

    def buyuk(self):
        return self.metin.replace("i", "İ").replace("ı", "I").upper()


k = TrKelime("İSTANBUL")

print("Kelime:", k)
print("Uzunluk:", len(k))
print("İçeriyor mu:", "tan" in k)
print("Büyük harf:", k.buyuk())
print("İndeks:", k[0])
print("Eşitlik:", TrKelime("Işık") == TrKelime("ışık"))

print("\nTürkçe sıralama testleri:")

print("çay < dağ:", TrKelime("çay") < TrKelime("dağ"))
print("ılık < iğne:", TrKelime("ılık") < TrKelime("iğne"))
print("ördek < pasta:", TrKelime("ördek") < TrKelime("pasta"))



ROMA_DEGERLERI = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}


def roma_cevir(sayi):
#Sayıyı Roma rakamına çevirir.
    if not isinstance(sayi, int) or isinstance(sayi, bool):
        raise ValueError("Sayı tam sayı olmalıdır.")

    if sayi < 1 or sayi > 3999:
        raise ValueError("Sayı 1 ile 3999 arasında olmalıdır.")

    sonuc = ""

    for roma, deger in ROMA_DEGERLERI.items():
        while sayi >= deger:
            sonuc += roma
            sayi -= deger

    return sonuc



def onluk_cevir(roma):
#Roma rakamını onluk sayıya çevirir.
    if not isinstance(roma, str) or not roma:
        raise ValueError("Geçerli bir Roma rakamı giriniz.")

    roma = roma.upper()

    if any(harf not in "IVXLCDM" for harf in roma):
        raise ValueError("Geçersiz Roma rakamı.")

    sonuc = 0
    i = 0

    while i < len(roma):

        if i + 1 < len(roma):
            mevcut = ROMA_DEGERLERI[roma[i]]
            sonraki = ROMA_DEGERLERI[roma[i + 1]]

            if sonraki > mevcut:
                sonuc += sonraki - mevcut
                i += 2
                continue

        sonuc += ROMA_DEGERLERI[roma[i]]
        i += 1

    if sonuc < 1 or sonuc > 3999 or roma_cevir(sonuc) != roma:
        raise ValueError("Geçersiz Roma rakamı.")

    return sonuc



print("\nRoma rakamı testleri:")

print("2026:", roma_cevir(2026))
print("1994:", roma_cevir(1994))
print("XLII:", onluk_cevir("XLII"))
print("\nGeçerli Roma rakamları:")

print(onluk_cevir("XLII"))
print(onluk_cevir("MMXXVI"))
print(onluk_cevir("MCMXCIV"))

print("\nGeçersiz Roma rakamları:")

for roma in ["IIII", "VX", "ABC"]:
    try:
        print(onluk_cevir(roma))
    except ValueError as hata:
        print(roma, ":", hata)