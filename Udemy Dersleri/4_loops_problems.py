# Problem 1

# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
# Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

# sayi = int(input('Bir Sayı Giriniz: '))

# toplam = 0

# for i in range(1,sayi):
#     if sayi % i == 0:
#         toplam += i

# if sayi == toplam:
#     print(f'{sayi} MÜKEMMEL SAYIDIR!') 
# else:
#     print(f'{sayi} MÜKEMMEL SAYI DEĞİLDİR!')


# Problem 2

# Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
# Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 
# 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya 
# "Armstrong" sayısı denir.
# Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

sayi2 = input('Bir Sayı Giriniz: ')

toplam = 0

for i in sayi2:
    toplam += int(i)**len(sayi2)

if toplam == int(sayi2):
    print(f'{sayi2} Armstrong Sayısıdır!')
else:
    print(f'{sayi2} Armstrong Sayısı Değildir!')


# Problem 3
# 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
# İpucu: İç içe 2 tane for döngüsü kullanın. 
# Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.










# Problem 4
# Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları 
# "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın 
# ve ekrana "toplam değişkenini" bastırın.
# İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.










# Problem 5
# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.







# Problem 6

# Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve 
# list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.
# Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. 
# Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.
# İpucu: Basit düşünmeye çalışın.