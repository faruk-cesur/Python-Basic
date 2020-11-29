# Problem 1
# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
# Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

sayi = int(input('Bir Sayı Giriniz: '))

toplam = 0

for i in range(1,sayi):
    if sayi % i == 0:
        toplam += i

if sayi == toplam:
    print(f'{sayi} MÜKEMMEL SAYIDIR!') 
else:
    print(f'{sayi} MÜKEMMEL SAYI DEĞİLDİR!')


# Problem 2
# Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
# Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 
# 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

sayi = input('Bir Sayı Giriniz: ')

toplam = 0

for i in sayi:
    toplam += int(i)**len(sayi)

if toplam == int(sayi):
    print(f'{sayi} Armstrong Sayısıdır!')
else:
    print(f'{sayi} Armstrong Sayısı Değildir!')


# Problem 3
# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

for i in range(1,11):
    print('****************')
    for j in range(1,11):
        print(f'{i}x{j} = {i*j}')



# Problem 4
# Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları 
# "toplam" isimli bir değişkene ekleyin. Kullanıcı "1" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

print("""********************************
SAYI GİRME PROGRAMI
********************************""")
toplam = 0
while True:
    print(' ANA MENÜ '.center(50,'*'))
    islem = int(input('1. Programdan Çıkış Yap!\n2. Bir Sayı Gir!\n3. Toplamı Görüntüle!\n\nYapılacak İşlem Numarası: '))
    if islem == 1:
        print(f'\nToplam Sayı: {toplam}\n\nProgramdan Çıkış Yapılıyor...\n')
        break
    elif islem == 2:
        print(' SAYI GİRME EKRANI '.center(50,'*'))     
        sayi = int(input('Bir Sayı Giriniz: '))
        toplam += sayi
        print(f'\nToplam Sayı: {toplam}\n')
    elif islem == 3:
        print(' TOPLAM SAYI EKRANI '.center(50,'*'))
        print(f'\nToplam Sayı: {toplam}\n')
    else:
        print('Geçersiz Giriş Yaptınız. Lütfen 3 Seçenekten Birini Seçiniz!')



# Problem 5
# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.

for i in range(1,101):
    if(i%3 == 0):
        print("3'e bölünen sayılar: ",i)
    else:
        continue


# Problem 6
# list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atın.

liste = [i for i in range(1,101) if i % 2 == 0]

print(liste)