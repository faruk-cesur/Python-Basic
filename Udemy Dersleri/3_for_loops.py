# For Döngüleri

# Dictionary üzerinde kullanımı

sozluk = {'Bir':1,'İki':2,'Üç':3,'Dört':4}

print(sozluk)

for i in sozluk.values():  # Dictionary içindeki value'leri alır.
    print(i)

for i in sozluk.keys():    # Dictionary içindeki keyleri alır.
    print(i)

for i in sozluk.items():   # Dictionary içindeki hem keyleri hem valueleri yani itemleri alır.
    print(i)

for i,j in sozluk.items(): # Dictionary içindekileri ayrı ayrı almak için i,j,k,l vs. konur.
    print(i,j)

