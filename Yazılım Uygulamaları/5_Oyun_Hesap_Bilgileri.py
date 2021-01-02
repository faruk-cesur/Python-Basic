bnsHesaplar = {}
print(' Lütfen iki adet karakter bilgisi giriniz! '.center(100,'*'))

Nick = input('Nick : ')
AttackPower = int(input('Attack Power : '))
HmLevel = int(input('HM Level : '))

bnsHesaplar.update({'Karakter1':{
    'Nick':Nick,
    'Attack Power':AttackPower,
    'HM Level':HmLevel
}})

print(' 1. Karakter Bilgisi Girildi! '.center(100,'*')) # Karakter Bilgisi

Nick = input('Nick : ')
AttackPower = int(input('Attack Power : '))
HmLevel = int(input('HM Level : '))

bnsHesaplar.update({'Karakter2':{
    'Nick':Nick,
    'Attack Power':AttackPower,
    'HM Level':HmLevel
}})

print(' 2. Karakter Bilgisi Girildi! '.center(100,'*')) # Karakter Bilgisi
print('  '.center(100,' '))
print(' Girdiğiniz Karakter Bilgileri Aşağıda Sıralanmıştır! '.center(150,'*'))
print('  '.center(100,' '))
print(bnsHesaplar)
print('  '.center(100,' '))
print('Hangi Karakterin Bilgisini Sorgulamak İstersiniz? Alttaki İfadelerden Birini Yazın!\n• Karakter1\n• Karakter2')

print('  '.center(100,' '))
hesap = input(' = ')
print('  '.center(100,' '))
print('Görüntülediğiniz Hesabın Bilgileri Aşağıdadır'.center(100,'*'))
print('  '.center(100,' '))
print(bnsHesaplar[hesap])
print('  '.center(100,' '))
