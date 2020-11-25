# 1 - girilen 2 sayıdan hangisi büyüktür?

sayi1 = int(input('1. Sayı : '))
sayi2 = int(input('2. Sayı : '))

print(sayi1 > sayi2)

# 2- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalam hesapla

vize1 = int(input('1. Vize : '))
vize2 = int(input('2. Vize : '))
final = int(input('Final Notu : '))

ortalama = (((((vize1+vize2)*60)/100) + ((final*40)/100))) /3
if ortalama >=50:print('Geçti')
else: print('Kaldı')

#3 girilen bir sayının tek mi çfit mi olduğunu yazdır

sayi = int(input('Sayı : '))
result =  (sayi %2 == 0)
if result == True : print('Sayı Çift')
else :print('Sayı Tek')

#4 girilen bir sayının negatif pozitif durumunu yazdır

sayi = int(input('Sayı gir: '))

if sayi < 0 : print('Sayı negatif')
if sayi == 0 : print('Sayı nötr')
if sayi > 0 : print('Sayı Pozitif')

# 5 - parola ve email bilgisini isteyip doğruluğunu kontrol ediniz

mail = 'faruk@hotmail.com'
sifre = '123123'


email = input('email adresiniz : ')
parola = input('Parolanız : ')

if email == mail and parola == sifre : print('Giriş yaptınız!')
else : print('Giriş başarısız!')