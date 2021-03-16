# while dönüsü kullanılarak Kullancının geçerli puan girmesini ve bu puanların ortalamasını bulup ekrana yazdıran program


puan1=0
puan2=0
kalanDenemeSayisi=5
while(True):
    puan1=int(input("1. Puanınızı Giriniz:"))
    if puan1>=0 and puan1 <=100:
        print("Girilen Puan Geçerli")
        break
    else:
        kalanDenemeSayisi=kalanDenemeSayisi-1
        print("Geçersiz Puan! Tekrar Giriniz")
        if (kalanDenemeSayisi==0):
            print("Denem hakkınız son buldu: Otomatik olarak 50 puanı girildi..")
            puan1=50
            break
        else:
            print(f"{kalanDenemeSayisi} tane deneme hakkınız kaldı")

kalanDenemeSayisi=5
while(True):
    puan2=int(input("2. Puanınızı Giriniz:"))
    if puan2>=0 and puan2 <=100:
        print("Girilen Puan Geçerli")
        break
    else:
        kalanDenemeSayisi=kalanDenemeSayisi-1
        print("Geçersiz Puan! Tekrar Giriniz")
        if (kalanDenemeSayisi==0):
            print("Denem hakkınız son buldu: Otomatik olarak 50 puanı girildi..")
            puan2=50
            break
        else:
            print(f"{kalanDenemeSayisi} tane deneme hakkınız kaldı")
ortalama=(puan1+puan2)/2
print(f"Ortalama:{ortalama}")
