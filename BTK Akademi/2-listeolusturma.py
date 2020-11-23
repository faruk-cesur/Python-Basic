urunListesi = {}

urunStokKodu = input('Ürün Stok Kodu : ')
urunCinsi = input('Ürün Cinsi : ')
urunStok = float(input('Ürün Stok Miktarı : '))
urunMarka = input('Ürün Markası : ')
urunFiyat = float(input('Ürün Fiyatı : '))

urunListesi.update({urunStokKodu:{
    'Ürün Stok Kodu : ':urunStokKodu,
    'Ürün Cinsi : ':urunCinsi,
    'Ürün Stok Miktarı : ':urunStok,
    'Ürün Markası : ':urunMarka,
    'Ürün Fiyatı : ':urunFiyat
}})

print(' Ürün Girişi Başarılı! '.center(100,'*'))
print(' '.center(100,' '))

urunStokKodu = input('Ürün Stok Kodu : ')
urunCinsi = input('Ürün Cinsi : ')
urunStok = float(input('Ürün Stok Miktarı : '))
urunMarka = input('Ürün Markası : ')
urunFiyat = float(input('Ürün Fiyatı : '))

urunListesi.update({urunStokKodu:{
    'Ürün Stok Kodu : ':urunStokKodu,
    'Ürün Cinsi : ':urunCinsi,
    'Ürün Stok Miktarı : ':urunStok,
    'Ürün Markası : ':urunMarka,
    'Ürün Fiyatı : ':urunFiyat
}})

print(' Ürün Girişi Başarılı! '.center(100,'*'))
print(' '.center(100,' '))

urun = input('Görüntülemek İstediğiniz Ürünün Stok Kodunu Giriniz : ')
print(' '.center(100,' '))
print(urunListesi[urun])
print(' '.center(100,' '))
print(' Tüm Ürünlerin Listesi '.center(100,'*'))
print(' '.center(100,' '))
print(urunListesi)