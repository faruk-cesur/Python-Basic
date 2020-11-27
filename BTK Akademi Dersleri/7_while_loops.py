sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile alt alta ekrana yazdırın.

uzunluk = 0
while uzunluk < len(sayilar):
    print(sayilar[uzunluk])
    uzunluk += 1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

start = int(input('Başlangıç sayısı: '))
end = int(input('Bitiş sayısı: '))

while start <= end:
    if(start % 2 == 1):
        print('TEK SAYILAR: ',start)
    start += 1


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

# For döngüsü
z = reversed(range(101))
for i in z:
    print(i)

# While Döngüsü
i = 100
while i > 0:
    print(i)
    i -= 1


# 4 : Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# Normal input ve sorted komutu ile:

sayi1 = int(input('1. Sayı: '))
sayi2 = int(input('2. Sayı: '))
sayi3 = int(input('3. Sayı: '))
sayi4 = int(input('4. Sayı: '))
sayi5 = int(input('5. Sayı: '))
listOfNumbers = [sayi1,sayi2,sayi3,sayi4,sayi5]
sortedNumbers = sorted(listOfNumbers)
print(sortedNumbers)

# While input ve sort komutu ile:

numbers = []
i = 1
while i <= 5:
    number = int(input('Bir Sayı Giriniz: '))
    numbers.append(number)
    i += 1
numbers.sort()
print(numbers)


# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayın
#    ürün sayısını kullanıcıya sorun
#    dictionary listesi yapısı (name,price) şeklinde olsun.
#    ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunlerListesi = {}

urunSayisi = int(input('KAÇ TANE ÜRÜN GİRİLECEK? => '))

x = 1
while x <= urunSayisi:
    isim  = input('ÜRÜN İSMİ : ')
    fiyat = float(input('ÜRÜN FİYATI : '))
    isimFiyat = {isim:fiyat}
    urunlerListesi.update(isimFiyat)
    print(urunlerListesi)
    x += 1