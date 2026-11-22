# ==================================================
# Ad Soyad      : Zeynep Bozkurt
# Öğrenci No    : 20253004020
# Tarih         : 22.11.2026
# Dosya         : hafta8_gorev4.py
# Açıklama      : Kesirleri sadeleştiren ve kesirler üzerinde
#                 matematiksel işlemler gerçekleştiren bir sınıf oluşturur.
# ==================================================


# İki sayının en büyük ortak bölenini hesaplar.
def ebob(a, b):
    # Öklid algoritması ile EBOB değerini bulur.
    while b != 0:
        a, b = b, a % b

    # Sonucun pozitif olmasını sağlar.
    return abs(a)


# Kesir işlemlerini gerçekleştiren sınıf.
class Kesir:

    # Kesrin pay ve payda değerlerini oluşturur ve sadeleştirir.
    def __init__(self, pay, payda):

        # Paydanın sıfır olmasını engeller.
        if payda == 0:
            raise ValueError("Payda sıfır olamaz")

        # Payda negatifse işareti paya aktarır.
        if payda < 0:
            pay = -pay
            payda = -payda

        # Pay ve paydanın EBOB değerini hesaplar.
        ortak = ebob(pay, payda)

        # Kesri en sade hâline getirir.
        self.pay = pay // ortak
        self.payda = payda // ortak

    # Kesri ekrana yazdırılabilecek metin hâline getirir.
    def __str__(self):
        # Payda 1 ise yalnızca payı döndürür.
        if self.payda == 1:
            return str(self.pay)

        # Pay ve paydayı kesir biçiminde döndürür.
        return f"{self.pay}/{self.payda}"

    # İki kesri toplar ve yeni bir kesir döndürür.
    def __add__(self, diger):
        yeni_pay = self.pay * diger.payda + diger.pay * self.payda
        yeni_payda = self.payda * diger.payda
        return Kesir(yeni_pay, yeni_payda)

    # İki kesri çıkarır ve yeni bir kesir döndürür.
    def __sub__(self, diger):
        yeni_pay = self.pay * diger.payda - diger.pay * self.payda
        yeni_payda = self.payda * diger.payda
        return Kesir(yeni_pay, yeni_payda)

    # İki kesri çarpar ve yeni bir kesir döndürür.
    def __mul__(self, diger):
        yeni_pay = self.pay * diger.pay
        yeni_payda = self.payda * diger.payda
        return Kesir(yeni_pay, yeni_payda)

    # Bir kesri başka bir kesre böler.
    def __truediv__(self, diger):

        # Sıfıra bölme hatasını kontrol eder.
        if diger.pay == 0:
            raise ZeroDivisionError("Sıfıra bölme yapılamaz")

        yeni_pay = self.pay * diger.payda
        yeni_payda = self.payda * diger.pay
        return Kesir(yeni_pay, yeni_payda)

    # İki kesrin eşit olup olmadığını kontrol eder.
    def __eq__(self, diger):
        return self.pay * diger.payda == diger.pay * self.payda

    # Bir kesrin diğerinden küçük olup olmadığını kontrol eder.
    def __lt__(self, diger):
        return self.pay * diger.payda < diger.pay * self.payda

    # Bir kesrin diğerinden küçük veya eşit olup olmadığını kontrol eder.
    def __le__(self, diger):
        return self.pay * diger.payda <= diger.pay * self.payda

    # Kesri ondalık sayı biçimine dönüştürür.
    def __float__(self):
        return self.pay / self.payda


# 1'den 10'a kadar olan kesirlerin çarpımını hesaplar.
carpim = Kesir(1, 1)

for n in range(2, 11):
    # Her adımda yeni kesir oluşturup çarpıma ekler.
    terim = Kesir(n - 1, n)
    carpim = carpim * terim

print("Çarpım:", carpim)


# Beş farklı kesir oluşturur.
k1 = Kesir(3, 7)
k2 = Kesir(5, 12)
k3 = Kesir(2, 5)
k4 = Kesir(4, 9)
k5 = Kesir(3, 8)

# En büyük kesri bulmak için ilk kesri başlangıç kabul eder.
en_buyuk = k1

# Diğer kesirleri sırayla karşılaştırır.
if en_buyuk < k2:
    en_buyuk = k2

if en_buyuk < k3:
    en_buyuk = k3

if en_buyuk < k4:
    en_buyuk = k4

if en_buyuk < k5:
    en_buyuk = k5

# Bulunan en büyük kesri ekrana yazdırır.
print("En büyük:", en_buyuk)


# Kesir sınıfının özel metotlarını test eder.
print("Eşitlik:", Kesir(6, 8) == Kesir(3, 4))
print("Bölme:", Kesir(3, 4) / Kesir(3, 8))
print("Toplama:", Kesir(1, 2) + Kesir(1, 3))
print("Çıkarma:", Kesir(1, 2) - Kesir(1, 3))
print("Çarpma:", Kesir(1, 2) * Kesir(1, 3))
print("Küçük mü:", Kesir(1, 3) < Kesir(1, 2))
print("Küçük veya eşit mi:", Kesir(1, 2) <= Kesir(2, 4))
print("Ondalık:", float(Kesir(3, 4)))
