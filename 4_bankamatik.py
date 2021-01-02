bakiye = 10_000


def anaMenu():
    while True:
        print("-".center(50, "-"))
        print("BANKAMATİK [ANA MENÜ]".center(50, " "))
        print("*".center(50, "*"))
        print(
            f"\nAna Menü İşlemler;\n\n1. Kartsız İşlemler\n2. Uygulamayı Kim Yazdı?\n3. Uygulamadan Çıkış Yap"
        )
        islem = int(input("\nYapmak istediğiniz işlemi tuşlayınız: "))
        if islem == 1:
            kartsizIslemler()
        elif islem == 2:
            print(
                "\nBu uygulamanın geliştiricisi : Faruk CESUR\nİletişim: faruk-cesur@hotmail.com"
            )
            input("\nAna menüye dönmek için bir tuşa basınız...")
        elif islem == 3:
            print("\nUygulamadan çıkış yapılıyor...\n")
            break
        else:
            print("\n==> Geçersiz Giriş, Tekrar Giriş Yapınız!")
            input("\nAna menüye dönmek için bir tuşa basınız...")


def kartsizIslemler():
    while True:
        print("-".center(50, "-"))
        print("BANKAMATİK [KARTSIZ İŞLEMLER]".center(50, " "))
        print("*".center(50, "*"))

        print(
            f"\nKartsız İşlemler;\n\n1. Para Çekme\n2. Para Yatırma\n3. Bakiye Sorgula\n4. Ana Menüye Geri Dön\n"
        )
        islem = int(input("Yapmak istediğiniz işlemi tuşlayınız: ".strip()))
        if islem == 1:
            paraCekme()
        elif islem == 2:
            paraYatirma()
        elif islem == 3:
            bakiyeSorgula()
        elif islem == 4:
            print("\nAna Menüye Geri Dönülüyor...\n")
            break
        else:
            kartsizIslemler()
            print("Geçersiz Giriş!")


def bakiyeSorgula():
    while True:
        global bakiye
        print("-".center(50, "-"))
        print("BANKAMATİK BAKİYE SORGULAMA".center(50, " "))
        print("*".center(50, "*"))
        print(" ".center(50, " "))
        tcNo = input("Lütfen 11 Haneli T.C. Kimlik Numaranızı Giriniz: ".strip())
        if len(tcNo) > 11 or len(tcNo) < 11 or tcNo.isdigit() == False:
            bakiyeSorgula()
        global telNo
        print(" ".center(50, " "))
        telNo = input(
            "\nLütfen telefon numaranızı başında 0 olmadan 10 haneli şekilde giriniz.\n(Örnek: 5321504495)\n\nTelefon Numaranız:  ".strip()
        )
        if len(telNo) > 10 or len(telNo) < 10 or telNo.isdigit() == False:
            bakiyeSorgula()
        else:
            print(f"Bakiyeniz: {bakiye} TL")


def bakiyeSorgulamaOnay():
    while True:
        global telNo
        global bakiye
        print(" ".center(50, " "))
        sms = input(
            f'\nLütfen son dört hanesi {telNo[-4:]} ile biten numaranıza gelen SMS içindeki kodu giriniz.\nGerçek bir telefon olmadığı için "123456" giriniz: '
        )
        if sms == "123456":
            print(f"\nHesap Bakiyeniz: {bakiye} TL\n")
        input("\nAna Menüye Dönmek İçin Bir Tuşa Basınız: ")
        anaMenu()


def paraCekme():
    while True:
        global bakiye
        print("-".center(50, "-"))
        print("BANKAMATİK KARTSIZ İŞLEMLER [PARA ÇEKME]".center(50, " "))
        print("*".center(50, "*"))
        print(" ".center(50, " "))
        tcNo = input("Lütfen 11 Haneli T.C. Kimlik Numaranızı Giriniz: ".strip())
        if len(tcNo) > 11 or len(tcNo) < 11 or tcNo.isdigit() == False:
            paraCekme()
        global telNo
        print(" ".center(50, " "))
        telNo = input(
            "\nLütfen telefon numaranızı başında 0 olmadan 10 haneli şekilde giriniz.\n(Örnek: 5321504495)\n\nTelefon Numaranız:  ".strip()
        )
        if len(telNo) > 10 or len(telNo) < 10 or telNo.isdigit() == False:
            paraCekme()
        else:
            paraCekmeOnay()


def paraCekmeOnay():
    while True:
        global telNo
        global bakiye
        print(" ".center(50, " "))
        sms = input(
            f'\nLütfen son dört hanesi {telNo[-4:]} ile biten numaranıza gelen SMS içindeki kodu giriniz.\nGerçek bir telefon olmadığı için "123456" giriniz: '
        )
        if sms == "123456":
            print(f"\nHoşgeldiniz,\nHesap Bakiyeniz: {bakiye} TL\n")
            cekilecek = int(input("\nÇekmek istediğiniz tutar: "))
            if bakiye < cekilecek:
                print("\nBakiye Yetersiz!\nLütfen en baştan giriş yapınız...\n")
                break
            onay = int(
                input(
                    f"Çekmek istediğiniz tutarı onaylıyor musunuz? ({cekilecek} TL)\n1. Onaylıyorum\n2. İptal Et\n"
                )
            )
            if onay == 1:
                bakiye = bakiye - cekilecek
                print(f"Para çekme işlemi tamamlandı!\nKalan Bakiye: {bakiye} TL")
                anaMenu()
            if onay == 2:
                print("\nİşlem iptal edildi!\nGiriş ekranına dönülüyor...\n")
                anaMenu()
        else:
            print("\nSMS Kodunu yanlış girdiniz. Tekrar giriş yapınız!\n")
            break


def paraYatirma():
    while True:
        global bakiye
        print("-".center(50, "-"))
        print("BANKAMATİK KARTSIZ İŞLEMLER [PARA YATIRMA]".center(50, " "))
        print("*".center(50, "*"))
        print(" ".center(50, " "))
        tcNo = input("\nLütfen 11 Haneli T.C. Kimlik Numaranızı Giriniz: ".strip())
        if len(tcNo) > 11 or len(tcNo) < 11 or tcNo.isdigit() == False:
            paraYatirma()
        global telNo
        print(" ".center(50, " "))
        telNo = input(
            "\nLütfen telefon numaranızı başında 0 olmadan 10 haneli şekilde giriniz.\n(Örnek: 5321504495)\n\nTelefon Numaranız:  ".strip()
        )
        if len(telNo) > 10 or len(telNo) < 10 or telNo.isdigit() == False:
            paraYatirma()
        else:
            paraYatirmaOnay()


def paraYatirmaOnay():
    while True:
        global telNo
        global bakiye
        print(" ".center(50, " "))
        sms = input(
            f'\nLütfen son dört hanesi {telNo[-4:]} ile biten numaranıza gelen SMS içindeki kodu giriniz.\nGerçek bir telefon olmadığı için "123456" giriniz: '
        )
        if sms == "123456":
            print(f"\nHoşgeldiniz,\nHesap Bakiyeniz: {bakiye} TL\n")
            yatacak = int(input("\nYatırmak istediğiniz tutar: "))
            onay = int(
                input(
                    f"Yatırmak istediğiniz tutarı onaylıyor musunuz? ({yatacak} TL)\n1. Onaylıyorum\n2. İptal Et\n"
                )
            )
            if onay == 1:
                bakiye = bakiye + yatacak
                print(f"Para Yatırma işlemi tamamlandı!\nBakiye: {bakiye} TL")
                anaMenu()
            if onay == 2:
                print("\nİşlem iptal edildi!\nGiriş ekranına dönülüyor...\n")
                anaMenu()
        else:
            print("\nSMS Kodunu yanlış girdiniz. Tekrar giriş yapınız!\n")
            break


anaMenu()
