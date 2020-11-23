# Programlama Ödevi - Temel Python Objeleri ve Veri Yapıları

# Problem 1
# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. 
# Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
"""
a = float(input('1. Sayı : '))
b = float(input('2. Sayı : '))
c = float(input('3. Sayı : '))

sonuc = a*b*c
print(sonuc)

"""


# Problem 2
# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
isim = input('İsminiz : ')
boy = float(input('Boyunuz : '))
kilo = float(input('Kilonuz : '))

result = kilo / boy**2
print(result)

"""

# Problem 3
# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini 
# alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
kacYakiyor = float(input('Kilometre başına kaç kuruş yakıyor?'))
neKadarYolYapiyor = float(input('Kaç kilometre yol yapıyor? '))

odenecekTutar = kacYakiyor * neKadarYolYapiyor
print(odenecekTutar)

"""

# Problem 4
# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""
ad = input('Adınız : ')
soyad = input('Soyadınız : ')
numara = input('Numaranız : ')

print(f'Adınız ► {ad}\nSoyadınız ► {soyad}\nNumaranız ► {numara}')

"""

# Problem 5
# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
a = float(input('A sayısını girin : '))
b = float(input('B sayısını girin : '))
print (a,b)
liste = [a,b]
b = liste[0]
a = liste[1]

print(liste)
print(a,b)

"""

