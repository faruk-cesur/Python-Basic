# For Döngüleri

# Dictionary üzerinde kullanımı

sozluk = {'Bir':1,'İki':2,'Üç':3,'Dört':4}
""",
print(sozluk)

for i in sozluk.values():  # Dictionary içindeki value'leri alır.
    print(i)

for i in sozluk.keys():    # Dictionary içindeki keyleri alır.
    print(i)

for i in sozluk.items():   # Dictionary içindeki hem keyleri hem valueleri yani itemleri alır.
    print(i)

for i,j in sozluk.items(): # Dictionary içindekileri ayrı ayrı almak için i,j,k,l vs. konur.
    print(i,j)
    """

faturalar = {}

faturaNo = input('Fatura Numarası: ')
faturaTarihi = input('Fatura Tarihi: ')
faturaCari = input('Cari Ünvan: ')
faturaMatrah = float(input('Fatura Matrah: '))
faturaKdv = int(input('KDV Oranı: '))
faturaGenelToplam = ((faturaMatrah * faturaKdv)/100) + faturaMatrah



faturalar.update({faturaNo: {
    'Fatura Tarihi':faturaTarihi,
    'Cari Ünvan':faturaCari,
    'Fatura Matrah':faturaMatrah,
    'KDV Oranı':faturaKdv,
    'Genel Toplam':faturaGenelToplam
}})

print(f'{faturaNo} NUMARALI FATURA SİSTEME KAYDEDİLDİ'.center(100,'*'))

for i in faturalar:
    faturalar.update({faturaNo: {
    'Fatura Tarihi':faturaTarihi,
    'Cari Ünvan':faturaCari,
    'Fatura Matrah':faturaMatrah,
    'KDV Oranı':faturaKdv,
    'Genel Toplam':faturaGenelToplam
}})

print(f'{faturaNo} NUMARALI FATURA SİSTEME KAYDEDİLDİ'.center(100,'*'))



print(faturalar)
