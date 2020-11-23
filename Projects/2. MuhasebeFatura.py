faturalar = {}

def faturaIsleme():
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
    print(f' {faturaNo} NUMARALI FATURA SİSTEME KAYDEDİLDİ! '.center(100,'*'))
    print(faturalar)

faturaIsleme()
a = 3
while(a > len(faturalar)):
    faturaIsleme()

print(' FATURA İŞLEMLERİ KAYDEDİLDİ! '.center(100,'*'))