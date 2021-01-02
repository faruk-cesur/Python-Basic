bakiye = 5000

def anaMenu():
    while True:
        print('*'.center(100,'*'))
        print('BANKAMATİK [ANA MENÜ]'.center(100,' '))
        print('*'.center(100,'*'))
        print(f'\nİşlemler;\n\n1. Kartsız İşlemler\n2. Kartlı İşlemler\n3. Uygulamadan Çıkış Yap\n4. Uygulamayı Kim Yazdı?')
        islem = int(input('\nYapmak istediğiniz işlemi tuşlayınız: '))
        if islem == 1:
            kartsizIslemler()
        elif islem == 2:
            kartliIslemler()
        elif islem == 3:
            print('\nUygulamadan çıkış yapılıyor...\n')
            break
        elif islem == 4:
            print('\nBu uygulamanın geliştiricisi : Faruk CESUR\nİletişim: faruk-cesur@hotmail.com')
            input('\nAna menüye dönmek için bir tuşa basınız...')
        else:
            print('\n==> Geçersiz Giriş, Tekrar Giriş Yapınız!')
            input('\nAna menüye dönmek için bir tuşa basınız...')

def kartsizIslemler():
    while True:
        print('*'.center(100,'*'))
        print('BANKAMATİK [KARTSIZ İŞLEMLER]'.center(100,' '))
        print('*'.center(100,'*'))
        global telNo
        telNo = input('\nLütfen telefon numaranızı başında 0 olmadan 10 haneli şekilde giriniz.\n(Örnek: 5321504495)\n\nTelefon Numaranız:  '.strip())
        if len(telNo) > 10 or len(telNo) < 10:
            
        if telNo.isdigit():
            continue
        else:
            continue
        print(f'\nİşlemler;\n\n1. Para Çekme (SMS Onaylı)\n2. Para Yatırma\n3. Ana Menüye Geri Dön\n')
        islem = int(input('Yapmak istediğiniz işlemi tuşlayınız: '.lower().strip()))
        if islem == 1:
            paraCekme()
        elif islem == 2:
            paraYatirma()
        elif islem == 3:
            print('\nAna Menüye Geri Dönülüyor...\n')
            break
        else:
            kartsizIslemler()
            print('Geçersiz Giriş!')

def paraCekme():
    while True:
        global bakiye
        print('*'.center(100,'*'))
        print('BANKAMATİK KARTSIZ İŞLEMLER [PARA ÇEKME]'.center(100,' '))
        print('*'.center(100,'*'))
        tcNo = input('Lütfen T.C. Kimlik Numaranızı Giriniz: '.strip())
        if len(tcNo) > 11 or len(tcNo) < 11:
            print('\n11 Haneli olacak şekilde giriş yapınız.\n')
            paraCekme()
        sms = input(f'\nLütfen son dört hanesi {telNo[-4:]} ile biten numaranıza gelen SMS içindeki kodu giriniz.\nGerçek bir telefon olmadığı için "123456" giriniz: ')
        if sms == "123456":
            print(f'\nHoşgeldiniz,\nHesap Bakiyeniz: {bakiye} TL\n')
            cekilecek = int(input('\nÇekmek istediğiniz tutar: '))
            if bakiye < cekilecek:
                print('\nBakiye Yetersiz!\nLütfen en baştan giriş yapınız...\n')
                continue
            onay = int(input((f'Çekmek istediğiniz tutarı onaylıyor musunuz? ({cekilecek} TL)\n1. Onaylıyorum\n2. İptal Et\n')))
            if onay == 1:
                bakiye = bakiye - cekilecek
                print(f'Para çekme işlemi tamamlandı!\nKalan Bakiye: {bakiye} TL')
                break
            if onay == 2:
                print('\nİşlem iptal edildi!\nGiriş ekranına dönülüyor...\n')
                break
        else:
            print('\nSMS Kodunu yanlış girdiniz. Tekrar giriş yapınız!\n')
            continue

anaMenu()
