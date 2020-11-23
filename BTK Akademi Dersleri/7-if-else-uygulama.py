# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.

# name = input('İsminiz : ')
# age = int(input('Yaşınız : '))
# egitim = input('Eğitim Durumunuz Nedir?\n1- ilkokul\n2- lise\n3- üniversite\nLütfen üçünden birini yazınız! ').lower().strip()

# ehliyetKosuluYas = (age >= 18)
# ehliyetKosuluEgitim = (egitim == 'lise') or (egitim == 'üniversite')

# if ehliyetKosuluYas == True:
#     if ehliyetKosuluEgitim == True:
#         print('Ehliyet alma hakkınız var!')
#     else:
#         print('Eğitim durumunuz yeterli değil!')
# else:
#     print('Yaşınız yeterli değil!')


# 2- bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0-24   => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100  => 5

# yaziliNotu1 = int(input('1. Yazılı Notu : '))
# yaziliNotu2 = int(input('2. Yazılı Notu : '))
# sozluNotu = int(input('Sözlü Notu : '))

# ortalama = (yaziliNotu1 + yaziliNotu2 + sozluNotu) / 3

# if ortalama < 0:
#     print('HATA'.center(50,'*'))
# elif (ortalama >= 0) and (ortalama <= 24):
#     print('Alınan Not = 0')
# elif (ortalama >= 25) and (ortalama <= 44):
#     print('Alınan Not = 1')
# elif (ortalama >= 45) and (ortalama <= 54):
#     print('Alınan Not = 2')
# elif (ortalama >= 55) and (ortalama <= 69):
#     print('Alınan Not = 3')
# elif (ortalama >= 70) and (ortalama <= 84):
#     print('Alınan Not = 4')
# elif (ortalama >= 85) and (ortalama <= 100):
#     print('Alınan Not = 5')
# else:
#     print('Ortalama 100 üzerinde'.center(50,'*'))

# 3 - Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesapla
#     1. Bakım => 1. yıl
#     2. Bakım => 2. yıl
#     3. Bakım => 3. yıl
#     Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesapla

import datetime

tarih = input('Trafiğe Çıkış Tarihini 2020/10/11 Formatında Giriniz : ')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

trafiktekiZaman = simdi - trafigeCikis
print(trafiktekiZaman.days)

if trafiktekiZaman.days >= 365 and trafiktekiZaman.days <= 365*2:
    print('1. Bakım Zamanı Geldi!')
elif trafiktekiZaman.days >= 365*2 and trafiktekiZaman.days <= 365*3:
    print('2. Bakım Zamanı Geldi!')
elif trafiktekiZaman.days >= 365*3 and trafiktekiZaman.days <= 365*4:
    print('3. Bakım Zamanı Geldi!')
elif trafiktekiZaman.days < 365:
     print('İlk yılınız daha dolmadı!')
else: print('Bakım süreniz 4 yılın üstünde!')