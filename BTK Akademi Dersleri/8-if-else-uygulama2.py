# 1) Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
"""
sayi = int(input('Lütfen bir sayı girin : '))

if sayi >= 0 and sayi <= 100:
    print('Sayı 0-100 arasındadır!')
else: print('Sayı 0-100 arasında değil!')
"""

 # 2) Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""
sayi = float(input('Bir Sayı giriniz : '))

if (sayi > 0) and (sayi % 2 == 0):
     print('Sayı pozitif çift sayıdır!')
elif sayi == 0 :
    print('Sayı sıfır (Nötr)')
elif sayi < 0 :
    print('Sayı Negatiftir!')
elif (sayi > 0) and (not(sayi % 2 == 0)):
    print('Sayı pozitif ancak çift değil!')
elif (sayi % 2 == 0) and (not(sayi > 0)):
    print('Sayı çift ancak negatif!')
else: print('Girdiğiniz değer geçersiz!')
"""

# 3) email ve parola bilgileri ile giriş kontrolü yapınız
"""
email = 'farukces25@hotmail.com'
sifre = '29ko1k9o'

girisMail = input('Lütfen mail adresinizi giriniz: ').strip().lower()
girisSifre = input('Lütfen şifrenizi giriniz : ').strip().lower()

if      girisMail == email and girisSifre == sifre:
        print('Giriş Yaptınız!')
elif    (not (girisMail == email)) and (not(girisSifre == sifre)):
        print('Mail ve Şifre Yanlış!')
elif    (not (girisMail == email)) and (girisSifre == sifre):
        print('Mail Adresiniz Yanlış!')
elif    (girisMail == email) and (not(girisSifre == sifre)):
        print('Şifreniz Yanlış!')
else:   print('Hatalı Giriş Yaptınız!')

"""

"""
# 4) 22.10.2021 tarihinden bugünü çıkar ve gün farkını bul

import datetime

bugun = datetime.datetime.now()
emeklilik = datetime.datetime(2021,10,22)

fark = emeklilik - bugun
print(fark)
"""