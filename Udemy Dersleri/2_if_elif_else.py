# Problem 1
# Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın 
# ve şu kurallara göre ekrana şu yazıları yazdırın.

# Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

# BKİ 18.5'un altındaysa -------> Zayıf

# BKİ 18.5 ile 25 arasındaysa ------> Normal

# BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

# BKİ 30'un üstündeyse -------------> Obez

boy = float(input('Boyunuzu metre cinsinden girin: '))
kilo = float(input('Kilonuzu KG cinsinden girin: '))

bki = kilo / boy**2

if (bki < 18.5) and (bki > 0):
    print('Zayıf (18.5 altında)')
elif bki >= 18.5 and bki <= 25:
    print('Normal (18.5 ile 25 arasında)')
elif bki >= 25 and bki <= 30:
    print('Fazla Kilolu (25 ile 30 arasında)')
elif bki < 0:
    print('Hesapta bir yanlışlık var! (Negatif Değer Çıkıyor)')
elif bki > 30:
    print('Obez (30 üstünde)')
else:
    print('Girdiğiniz Değerler Geçersiz!')



# Problem 2
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.    

a = int(input('A :'))
b = int(input('B :'))
c = int(input('C :'))


if a > b and a > c:
    print(f'A ({a}) en büyük sayıdır!')
elif b > a and b > c:
    print(f'B ({b}) en büyük sayıdır!')
elif c > a and c > b:
    print(f'C ({c}) en büyük sayıdır!')
else:
    print('Kodda veya girilen değerde bir problem var!')



#     Problem 3
# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

#     Vize1 toplam notun %30'una etki edecek.

#     Vize2 toplam notun %30'una etki edecek.

#     Final toplam notun %40'ına etki edecek.

#     Toplam Not >=  90 -----> AA
#     Toplam Not >=  85 -----> BA
#     Toplam Not >=  80 -----> BB
#     Toplam Not >=  75 -----> CB
#     Toplam Not >=  70 -----> CC
#     Toplam Not >=  65 -----> DC
#     Toplam Not >=  60 -----> DD
#     Toplam Not >=  55 -----> FD
#     Toplam Not <  55 -----> FF

vize1 = int(input('1. Vize Notu: '))
vize2 = int(input('2. Vize Notu: '))
final = int(input('Final Notu: '))

ortalama = (((vize1+vize2)*0.30) + (final*0.40))
if ortalama >= 90:
    print(f'ortalamanız {ortalama} ve notunuz = AA')
elif ortalama >= 85:
    print(f'ortalamanız {ortalama} ve notunuz = BA')
elif ortalama >= 80:
    print(f'ortalamanız {ortalama} ve notunuz = BB')
elif ortalama >= 75:
    print(f'ortalamanız {ortalama} ve notunuz = CB')
elif ortalama >= 70:
    print(f'ortalamanız {ortalama} ve notunuz = CC')
elif ortalama >= 65:
    print(f'ortalamanız {ortalama} ve notunuz = DC')
elif ortalama >= 60:
    print(f'ortalamanız {ortalama} ve notunuz = DD')
elif ortalama >= 55:
    print(f'ortalamanız {ortalama} ve notunuz = FD')
elif ortalama < 55:
    print(f'ortalamanız {ortalama} ve notunuz = FF')
else:
    print('Değer Geçersiz')

    