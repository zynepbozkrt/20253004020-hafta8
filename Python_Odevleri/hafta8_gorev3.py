# ==================================================
# Ad Soyad      : Zeynep Bozkurt
# Öğrenci No    : 20253004020
# Tarih         : 22.11.2026
# Dosya         : hafta8_gorev3.py
# Açıklama      : Vigenère şifreleme yöntemi kullanılarak
#                 metinlerin şifrelenmesini ve çözülmesini sağlar.
# ==================================================


# Verilen metni anahtar kullanarak şifreler veya şifresini çözer.
def vigenere(metin, anahtar, yon=1):

    # Anahtarın boş olup olmadığını kontrol eder.
    if anahtar == "":
        raise ValueError("Anahtar boş olamaz")

    sonuc = ""
    j = 0

    # Metindeki karakterleri sırayla kontrol eder.
    for karakter in metin:

        # Büyük harfler için A harfini başlangıç noktası alır.
        if 'A' <= karakter <= 'Z':
            taban = ord('A')

        # Küçük harfler için a harfini başlangıç noktası alır.
        elif 'a' <= karakter <= 'z':
            taban = ord('a')

        # Harf olmayan karakterleri değiştirmeden sonuca ekler.
        else:
            sonuc += karakter
            continue

        # Anahtarın sıradaki harfini alır.
        # Anahtar biterse başa dönerek tekrar kullanır.
        anahtar_harfi = anahtar[j % len(anahtar)].upper()

        # Anahtar harfinin alfabedeki sayısal kaydırma değerini bulur.
        kaydirma = ord(anahtar_harfi) - ord('A')

        # Harfin yeni konumunu hesaplar.
        # yon=1 şifreleme, yon=-1 şifre çözme işlemini yapar.
        yeni_deger = (ord(karakter) - taban + yon * kaydirma) % 26

        # Hesaplanan yeni karakteri sonuca ekler.
        sonuc += chr(taban + yeni_deger)

        # Yalnızca harf işlendiğinde anahtar sırasını ilerletir.
        j += 1

    # Şifrelenmiş veya çözülmüş metni döndürür.
    return sonuc


# Şifreleme işlemini test eder.
print(vigenere("Attack at dawn", "LEMON"))

# Şifre çözme işlemini test eder.
print(vigenere("Lxfopv ef rnhr", "LEMON", -1))
