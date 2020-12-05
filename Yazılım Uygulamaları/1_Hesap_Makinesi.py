print("""
**************************************

Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi

**************************************
""")

sayi1 = float(input('1. Sayıyı Giriniz : '))
sayi2 = float(input('2. Sayıyı Giriniz : '))
islem = input('Yukarıdaki İşlemlerden Hangi İşlemi Uygulamak İstersiniz? : ')

if islem == '1':
    print(f'{sayi1} ile {sayi2} sayılarının toplamı = {sayi1 + sayi2} ')
elif islem == '2':
    print(f'{sayi1} ile {sayi2} sayısının arasındaki fark = {sayi1-sayi2} ')
elif islem == '3':
    print(f'{sayi1} ile {sayi2} sayılarının çarpımı = {sayi1 * sayi2} ')
elif islem == '4':
    print(f' {sayi1} sayısının {sayi2} sayısına bölümünde = {sayi1 / sayi2} sonucu gelir. ')
else:
    print('Geçersiz İşlem. Lütfen 1 ile 4 arasında bir işlem seçiniz!')