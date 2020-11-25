# 1 - Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

x = int(input('X değeri giriniz: '))
result = (-1 < x < 101)
print(result)

# 2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

x = int(input('X değeri giriniz: '))
result = (x > 0) and (x % 2 == 0)
print(result)

# 3- email ve parola bilgileri ile giriş kontrolü yapınız

mail = 'faruk@hotmail.com'
sifre = '123123'
girilenMail = input('Lütfen mail adresinizi girin : ').lower().strip()
girilenSifre = input('Lütfen şifrenizi girin : ').lower().strip()

if (girilenMail == mail) and (girilenSifre == sifre) : print('Giriş Başarılı!'.center(100,'*'))
else : print('Giriş Başarısız!'.center(100,'*'))

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

Sayi1 = int(input('1. değeri giriniz: '))
Sayi2 = int(input('2. değeri giriniz: '))
Sayi3 = int(input('3. değeri giriniz: '))

result = (Sayi1 > Sayi2 > Sayi3)


# 5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesapla
# eğer ortalama 50 ve üzerindeyse geçti değilse kaldı yazdır
# ortalama 50 olsa bile final notu en az 50 olmalı
# finalden 70 alındığında ortalamanın önem olmasın

vize1 = int(input('1. Vize Notu : '))
vize2 = int(input('2. Vize Notu : '))
final1 = int(input('Final Notu : '))

ortalama = (((((vize1+vize2)*0.60)/2) + (final1*0.40)))

result = ((ortalama >= 50) and (final1 >= 50)) or (final1 >= 70)
if result == True : print('Geçti')
else : print('Kaldı')

# 6- kişinin ad , kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
# formül : (Kilo / boy uzunluğunun karesi) 
# aşağıdaki tabloya göre kişi hangi gruba girmektedir?
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)

kisiAd = input('Adınız : ')
kisiKilo = int(input('Kilonuz : '))
kisiBoy = float(input('Boyunuz : '))

kiloIndeksi = kisiKilo / (kisiBoy**2)
print(kiloIndeksi)

zayif = []
normal = []
fazlaKilolu = []
sisman = []

if (kiloIndeksi >= 0) and (kiloIndeksi <= 18.40):print('Zayıf')
if (kiloIndeksi >= 18.40) and (kiloIndeksi <= 24.9):print('Normal')
if (kiloIndeksi >= 24.90) and (kiloIndeksi <= 29.9):print('Fazla Kilolu')
if (kiloIndeksi >= 29.9):print('Şişman (Obez)')