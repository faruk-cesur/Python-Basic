x,y,z = 2,5,10
numbers = 1,5,7,10,6

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir

sayi1 = int(input('1. Sayı : '))
sayi2 = int(input('2. Sayı : '))

print(sayi1*sayi2 - (x+y+z))

# 2- y'nin x'e kalansız bölümünü hesapla

print(y//x)

# 3- x,y,z toplamımın mod 3 ü nedir

print((x+y+z)%3)

# 4- y'nin x. kuvvetini hesapla

print(y**x)

# 5- x,*y,z = numbers işlemine göre z 'nin küpü kaç

x,*y,z = numbers
print(z**3)

# 6- x,*y,z = numbers işlemine göre y nin değerli toplamı kaçtır

print(y[0]+y[1]+y[2])