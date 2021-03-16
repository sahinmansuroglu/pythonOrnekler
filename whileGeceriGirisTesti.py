# while dönüsü kullanılarak Kullancının geçerli puan girmesini ve bu punaların ortalamasını bulup ekrana yazdıran program

puan1=0
puan2=0
while(True):
    puan1=int(input("1. Puanınızı Giriniz:"))
    if puan1>=0 and puan1 <=100:
        print("Girilen Puan Geçerli")
        break
    else:
        print("Geçersiz Puan! Tekrar Giriniz...")
while(True):
    puan2=int(input("2. Puanınızı Giriniz:"))
    if puan2>=0 and puan2 <=100:
        print("Girilen Puan Geçerli")
        break
    else:
        print("Geçersiz Puan! Tekrar Giriniz...")
ortalama=(puan1+puan2)/2
print(f"Ortalama:{ortalama}")
