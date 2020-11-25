sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır?

for i in sayilar:
    if (i % 3 == 0):
        print(i)

# 2- Sayilar listesinde sayıların toplamı kaçtır?

toplam = 0
for i in sayilar:
     toplam += i
     print(i,toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.

for i in sayilar:
    if (i % 2 == 1):
        print('TEK SAYILAR: ',i,'KARESİ: ',i**2)
    else:
        print('ÇİFT SAYILAR: ',i,'KARESİ: ',i**2)




sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?

for i in sehirler:
    if (len(i) <= 5):
        print('5 Karakterden Kısa: ',i)
    else:
        print('5 Karakterden Uzun: ',i)



urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' },
]

# 5- Ürünlerin fiyatları toplamı nedir?

toplam = 0

for i in urunler:
    toplam += int(i['price'])
    print('FİYAT TOPLAMLARI: ',toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for i in urunler:
    if (int(i['price']) <= 5000):
        print('5000 TL VE ALTINDA OLAN ÜRÜNLER: ',i['name'],'// FİYAT: ',i['price'])
    else:
        print('5000 TL ÜSTÜNDE OLAN ÜRÜNLER: ',i['name'],'// FİYAT: ',i['price'])