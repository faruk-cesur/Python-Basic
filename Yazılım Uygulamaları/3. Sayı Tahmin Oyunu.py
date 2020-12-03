print('*'.center(100,'*'))
print("SAYI TAHMİN OYUNU GİRİŞ EKRANI".center(100,' '))
print('*'.center(100,'*'))
ad = input('Adınız: ')
print('*'.center(100,'*'))

while True:
    print('*'.center(100,'*'))
    print('SAYI TAHMİN OYUNU ANA MENÜ'.center(100,' '))
    print('*'.center(100,'*'))
    print(f'\nHoşgeldin {ad}, aşağıdaki işlemlerden hangisini yapmak istersin?\n\n1. Oyuna Başla!\n2. Nasıl Oynanır?\n3. Oyunu Kim Yaptı?\n4. Oyundan Çıkış Yap!\n')
    secim = int(input('Yapmak İstediğiniz İşlemin Numarasını Giriniz: '))
    if secim == 1:
        import random
        rastgeleSayi = random.randint(1,100)
        while True:
            hak = int(input('\nNot: 1-10 arası tahmin hakkı alabilirsiniz.\nAlmak İstediğim Tahmin Hakkı: '))
            can = hak
            if hak <= 0 or hak > 10:
                continue
            else:
                break

        while hak > 0:
            hak -= 1
            tahmin = int(input('Tahmin: '))
            if tahmin > rastgeleSayi:
                print(f'Tahmin Etmeniz Gereken Sayı Daha Düşük!\nKalan Tahmin Hakkınız: {hak}\n')
            elif tahmin < rastgeleSayi:
                print(f'Tahmin Etmeniz Gereken Sayı Daha Yüksek!\nKalan Tahmin Hakkınız: {hak}\n')
            elif tahmin == rastgeleSayi:
                print(f'\nTEBRİKLER!\n\nTahmininiz Doğru!\nSayı = {rastgeleSayi}\n{hak} Tahmin Hakkınız Daha Vardı!\nKazandığınız Puan = {hak * (100/can)}\n')
                input('Ana Menüye Dönmek İçin Bir Tuşa Basınız: ')
                break
        if hak == 0:
            print(f'\nKAYBETTİNİZ!\nTahmin Hakkınız Kalmadı!\nBulmanız Gereken Sayı: {rastgeleSayi}\n')
            input('Ana Menüye Dönmek İçin Bir Tuşa Basınız: ')
            continue


    elif secim == 2:
        print('\nNASIL OYNANIR?\n\nSİSTEME 1 İLE 100 ARASINDA RASTGELE BİR SAYI TANIMLANIR. SENİN GÖREVİN BU SAYIYI TAHMİN EDEREK BULMAK!\nOYUNA BAŞLAMADAN ÖNCE KAÇ ADET TAHMİN HAKKIN OLACAĞINI SEÇECEKSİN.\nSEÇEBİLECEĞİN TAHMİN HAKKI 1-10 ARASI OLACAKTIR.\nİLK SEFERDE DOĞRU TAHMİN EDERSEN 100 PUAN KAZANIRSIN.\nANCAK SAYIYI BULANA KADAR KULLANDIĞIN HER TAHMİN HAKKIN SENİN PUANINI DÜŞÜRECEKTİR!\n\n')
        print(int(input('Ana Menüye Dönmek İçin Bir Tuşa Basın: ')))
        continue
    elif secim == 3:
        print('\nOyunun Yapımcısı: Faruk CESUR\nİletişim: faruk-cesur@hotmail.com\n')
        print(int(input('Ana Menüye Dönmek İçin Bir Tuşa Basın: ')))
        continue
    elif secim == 4:
        print(f'\nOyundan Çıkış Yapılıyor...\nTekrar Bekleriz {ad} :)\n')
        break































# """
# import random
# rastgeleNumara = (random.randint(1,100))
# hak = 5


# while True:
#     print('''********************************************************************************************''')
#     if hak <= 0:
#         print(f'TAHMİN HAKKINIZ KALMADIĞI İÇİN KAYBETTİNİZ!\nTAHMİN ETMENİZ GEREKEN SAYI =  {rastgeleNumara} ')
#         break
#     if hak > 0:
#         tahmin = int(input('Tahmin: '))
#         if tahmin > rastgeleNumara:
#             hak -= 1
#             if hak <= 0:
#                 continue
#             else:
#                 print(f'1 hak kaybettiniz. {hak} adet hakkınız kaldı. Tahmin etmeniz gereken sayı daha KÜÇÜK!')
#         elif tahmin < rastgeleNumara:
#             hak -= 1
#             if hak <= 0:
#                 continue
#             else:
#                 print(f'1 hak kaybettiniz. {hak} adet hakkınız kaldı. Tahmin etmeniz gereken sayı daha BÜYÜK!')
#         elif tahmin == rastgeleNumara:
#             if hak == 5:
#                 print('İLK SEFERDE TAHMİN ETTİĞİNİZ İÇİN 100 PUAN KAZANDINIZ!')
#                 break
#             elif hak == 4:
#                 print('İKİNCİ SEFERDE TAHMİN ETTİĞİNİZ İÇİN 80 PUAN KAZANDINIZ!')
#                 break
#             elif hak == 3:
#                 print('ÜÇÜNCÜ SEFERDE TAHMİN ETTİĞİNİZ İÇİN 60 PUAN KAZANDINIZ!')
#                 break
#             elif hak == 2:
#                 print('DÖRDÜNCÜ SEFERDE TAHMİN ETTİĞİNİZ İÇİN 40 PUAN KAZANDINIZ!')
#                 break
#             elif hak == 1:
#                 print('BEŞİNCİ SEFERDE TAHMİN ETTİĞİNİZ İÇİN 20 PUAN KAZANDINIZ!')
#                 break

# """



