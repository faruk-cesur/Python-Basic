sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

uzunluk = 0
while uzunluk < len(sayilar):
    print(sayilar)
    uzunluk += len(sayilar)

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

start = int(input('Başlangıç sayısı: '))
end = int(input('Bitiş sayısı: '))

while start <= end:
    if(start % 2 == 1):
        print('TEK SAYILAR: ',start)
    start += 1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
x = 100
y = 1
