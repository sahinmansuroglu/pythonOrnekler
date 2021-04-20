# Lamba ile fonksiyon Tanımlama
topla=lambda sayi1,sayi2,sayi3:sayi1+sayi2+sayi3
ortalama=lambda a,b:(a+b)/2
def ortalama(a,b):
    return (a+b)/2

puanDurum=lambda puan: "Geçtiniz" if puan>=50 else "Kaldınız"

def puanDurum(puan):
    if puan>=50:
        return "Geçtiniz"
    else:
        return  "Kaldınız"


sayıDurum=lambda  sayi: "Çift" if sayi % 2==0 else " Tek"


print(sayıDurum(21))
