#1. s1 ve s2 adında iki sayıyı paretmetre olarak alan topla adında bir fonksiyon tanımlayınız
# bu fonksiyon içerisinde s1 ve s2 toplayacak ve sonucu döndürecek.
# Ana programda bu fonksiyonu 2 sayıyı parametre olarak göndererek çağırınız ve dönen sonucu
# ekrana yazdırınız.
def topla(s1,s2):
    sonuc=s1+s2
    return sonuc

a=topla(95,36)
print(a)
print("Çıkış Yapılıyor")

#2. Geriye değer döndüren fonksiyonlar tanımlayarak
#Girilen 2 sayı uzerinde 4 işlem ve mod alma ve üst alma hesaplarını yaptırınız.
# Sonucu ise geriye Değer Döndürmeyen fonksiyon ile ekrana yazdırınız.
# fonksiyon Listesi Kullanılmadan yapılan uygulama

def topla(s1,s2):
    return  s1+s2
def cikart(s1,s2):
    return  s1-s2
def carp(s1,s2):
    return  s1*s2
def bol(s1,s2):
    return  s1/s2
def modAl(s1,s2):
    return  s1 % s2
def usAl(s1,s2):
    return s1**s2
def sonucuEkranaBas(islemAdi,sonuc):
    print(f"{islemAdi} işleminin Sonucu={sonuc}")
def menuBasveSecenegiDondur():
    print("İşlemler")
    print("1-Topla")
    print("2-Çıkart")
    print("3-Çarp")
    print("4-Böl")
    print("5-Mod Al")
    print("6-Üs Al")
    print("0-Çıkış")
    seciminiz=int(input("İşlem Seçiniz:"))
    return  seciminiz
def devamEtmekIcinEnteraBasma():
    input("Devam Etmek için Entera basınız.....")
def klavyedenSayiOkuVeDondur(metin):
    return  int(input(metin))
def secimeGoreHesaplamaYap(secim,s1,s2):
    if secim == 1:
        sonucuEkranaBas("Toplama",topla(s1, s2))
    elif secim == 2:
        sonucuEkranaBas("Çıkartma",cikart(s1, s2))
    elif secim == 3:
        sonucuEkranaBas("Çarpma",carp(s1, s2))
    elif secim == 4:
        sonucuEkranaBas("Bölme",bol(s1, s2))
    elif secim == 5:
        sonucuEkranaBas("Mod alma",modAl(s1, s2))
    else:
        sonucuEkranaBas("Üs Alma",usAl(s1, s2))
    devamEtmekIcinEnteraBasma()
    print("\n" * 10)

while True:
    secim=menuBasveSecenegiDondur()
    if secim>=0 and secim<=6:
        if secim==0:
            print("Program Sonlandırılıyor")
            break
        else:
            s1 = klavyedenSayiOkuVeDondur("1. Sayıyı Giriniz:")
            s2 = klavyedenSayiOkuVeDondur("2. Sayıyı Giriniz:")
            secimeGoreHesaplamaYap(secim,s1,s2)

    else:
        print("Lütfen 0 ile 6 arası değer giriniz!")

#3. Geriye değer döndüren fonksiyonlar tanımlayarak
#Girilen 2 sayı uzerinde 4 işlem ve mod alma ve üst alma hesaplarını yaptırınız.
# Sonucu ise geriye Değer Döndürmeyen fonksiyon ile ekrana yazdırınız.
#Fonksiyon adlarıdan liste oluşturarak tasarlayınız
def topla(s1,s2):
    return  s1+s2
def cikart(s1,s2):
    return  s1-s2
def carp(s1,s2):
    return  s1*s2
def bol(s1,s2):
    return  s1/s2
def modAl(s1,s2):
    return  s1 % s2
def usAl(s1,s2):
    return s1**s2
def sonucuEkranaBas(islemAdi,sonuc):
    print(f"{islemAdi} işleminin Sonucu={sonuc}")
def menuBasveSecenegiDondur():
    print("İşlemler")
    print("1-Topla")
    print("2-Çıkart")
    print("3-Çarp")
    print("4-Böl")
    print("5-Mod Al")
    print("6-Üs Al")
    print("0-Çıkış")
    seciminiz=int(input("İşlem Seçiniz:"))
    return  seciminiz
def devamEtmekIcinEnteraBasma():
    input("Devam Etmek için Entera basınız.....")
def klavyedenSayiOkuVeDondur(metin):
    return  int(input(metin))
def secimeGoreHesaplamaYap(secim,s1,s2):
    islemAdi=islemListesi[secim-1]
    sonuc=fonksiyonListesi[secim-1](s1,s2)
    sonucuEkranaBas(islemAdi,sonuc)

    devamEtmekIcinEnteraBasma()
    print("\n" * 10)
fonksiyonListesi=[topla,cikart,carp,bol,modAl,usAl]
islemListesi=["Toplama","Çıkartma","Çarpma","Bölme","Mod alma","Üs Alma"]
while True:
    secim=menuBasveSecenegiDondur()
    if secim>=0 and secim<=6:
        if secim==0:
            print("Program Sonlandırılıyor")
            break
        else:
            s1 = klavyedenSayiOkuVeDondur("1. Sayıyı Giriniz:")
            s2 = klavyedenSayiOkuVeDondur("2. Sayıyı Giriniz:")
            secimeGoreHesaplamaYap(secim,s1,s2)

    else:
        print("Lütfen 0 ile 6 arası değer giriniz!")
#4. Klavyeden girilen 2 sayı arasına dört işlem, mod alma  üs alma işlemlerinin
# tümünü yapıp
# sonuçlarını ekrana yazdırınız.
#Olabilecek En kısa yöntemle yapınız 
# 1. YOL
def topla(s1,s2):
    return  s1+s2
def cikart(s1,s2):
    return  s1-s2
def carp(s1,s2):
    return  s1*s2
def bol(s1,s2):
    return  s1/s2
def modAl(s1,s2):
    return  s1 % s2
def usAl(s1,s2):
    return s1**s2
s1=int(input("1. Sayıyı Giriniz:"))
s2=int(input("1. Sayıyı Giriniz:"))
print(f"Toplama işleminin Sonucu:{topla(s1,s2)}")
print(f"Çıkartma işleminin Sonucu:{cikart(s1,s2)}")
print(f"Çarpma işleminin Sonucu:{carp(s1,s2)}")
print(f"Bölme işleminin Sonucu:{bol(s1,s2)}")
print(f"Mod Alma işleminin Sonucu:{modAl(s1,s2)}")
print(f"ÜS alma işleminin Sonucu:{usAl(s1,s2)}")

#5. Klavyeden girilen 2 sayı arasına dört işlem, mod alma  üs alma işlemlerinin
# tümünü yapıp
# sonuçlarını ekrana yazdırınız.
# Olabilecek En kısa yöntemle yapınız
# 2. YOL
def topla(s1,s2):
    return  s1+s2
def cikart(s1,s2):
    return  s1-s2
def carp(s1,s2):
    return  s1*s2
def bol(s1,s2):
    return  s1/s2
def modAl(s1,s2):
    return  s1 % s2
def usAl(s1,s2):
    return s1**s2

fonksiyonListesi=[topla,cikart,carp,bol,modAl,usAl]
islemListesi=["Toplama","Çıkartma","Çarpma","Bölme","Mod alma","Üs Alma"]

s1=int(input("1. Sayıyı Giriniz:"))
s2=int(input("1. Sayıyı Giriniz:"))

for i in range(6):
    print(f"{islemListesi[i]} işleminin sonucu:{fonksiyonListesi[i](s1,s2)}")

#6. fonksiyon İsimlerinden liste oluşturma Örneği
def ekle():
    print("Ekleme İşlemi Fonksiyonu")

def sil():
    print("Silme İşlemi Fonksiyonu")
def guncelle():
    print("Güncelleme İşlemi Fonksiyonu")
def listeleme():
    print("Listeleme İşlemi Fonksiyonu")
while True:
    print("İşlemler..")
    print("0- Ekle \n1- Sil\n2- Güncelle \n3- Listeleme")
    seciminiz=int(input("Seçiminizi Giriniz(0-3):"))
    if seciminiz==4:
        break
    fonksiyonList=[ekle,sil,guncelle,listeleme]
    fonksiyonList[seciminiz]()
