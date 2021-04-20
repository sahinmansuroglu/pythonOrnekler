# Fonksiyon  lambda kullanarak liste üzerinde işlemler Yapma
kisiListesi=[]
notListesi=[]
puanDurum=lambda puan: True if puan<50 else False
def ekle(ad,puan):
    kisiListesi.append(ad)
    notListesi.append(puan)

def listele(istek):
    for i in range(len(notListesi)):
        listedekiPuan=notListesi[i]
        sart=False
        if istek=="Geçenler":
            sart=not puanDurum(listedekiPuan)
        if istek=="Kalanlar":
            sart = puanDurum(listedekiPuan)
        if sart:
            print(f"{kisiListesi[i]}:{notListesi[i]}")
def kullanicidanAdvePuanAlArdindanKaydet():
    ad=input("Adınızı Giriniz:")
    puan=int(input("Notunuzu Giriniz:"))
    ekle(ad,puan)
    print(f"{ad} adlı kullanıcının {puan} puanı başarıyla eklendi..")
while(True):
    print("Seçiminiz")
    print("1-Ekleme")
    print("2-Geçenleri Listele")
    print("3-Kalanları Listele")
    print("0-Çıkış")
    secim=int(input("Seçiminizi Giriniz:"))
    if secim==0:
        print("Çıkış Yapıldı")
        break
    elif secim==1:
        kullanicidanAdvePuanAlArdindanKaydet()
    elif secim==2:
        listele("Geçenler")
    elif secim==3:
        listele("Kalanlar")
    



