#1. Ekrana 2 kez "Merhaba Dünya" yazdıran adı da ekranaMesajYaz olan
# bir fonksiyon tanımlayın ve bu fonksiyonu 4 kez çağırın.
def ekranaMesajYaz():
    print("Merhaba Dünya")
    print("Merhaba Dünya")


ekranaMesajYaz()
ekranaMesajYaz()
ekranaMesajYaz()
ekranaMesajYaz()

#2. "ad" isminde bir parametre alan ve ad'ın başına merhaba koyup
#ekrana yazdıran ekranaMesajYaz adında bir fonksiyon tanımlayınız
#ve fonksiyona 4 farklı isim stringi göndererek fonksiyonu çağırınız

def ekranaMesajYaz(ad):
    print(f"Merhaba {ad}")

ad1="serdar"
ad2="Selin"
ekranaMesajYaz(ad1)
ekranaMesajYaz(ad2)
ekranaMesajYaz("Mehmet")
ekranaMesajYaz("Ceren")

#3.ad, soyad, dogumTarihi isminde 3 adet parametre alan
#mesajYaz adında bir fonksiyon tanımlayınız.
# Bu fonksiyon ekrana ad soyad'ın başına merhaba yazdıracak
# ve dogumtarihini kullanarak yasını hesaplatıp ekrana yazdıracak
# oluşturduğunuz fonksiyonu klavyeden girilen değerler ile çağırınız

def mesajYaz(ad,soyad,dogumTarihi):
    yas=2020-dogumTarihi
    print(f"Merhaba {ad} {soyad}")
    print(f"Yaşınız:{yas}")
# Fonksiyonun denemesi
mesajYaz("Şahin","Mansuroğlu",1982)

girilenAd=input("Adınızı Giriniz:")
girilenSoyad=input("Soyadınızı Giriniz:")
girilenYas=int(input("Doğum Tarihini Giriniz:"))

mesajYaz(girilenAd,girilenSoyad,girilenYas)

#4.Öyle bir fonksiyon tasarlayınız ki kaç tane parametre olarak ad gönderirsek
#herbirinin başına ayrı ayrı  merhaba yazmasını sağlayabilelim.
# bu fonksiyonu farklı sayıda parametre ile çağırınız

def mesajYaz(*adlar):
    for herbirAd in adlar:
        print(f"Merhaba {herbirAd}")



mesajYaz("ali","veli","serdar")
mesajYaz("ali","veli")

#5.Parametre(s1,s2) olarak aldığı 2 sayıyı toplayan topla2 adında bir fonskyion tanımlayınız.
#Parametr(s1,s2,s3) olarak aldığı 3 sayıyı toplayan topla3 adında ikinci bir fonskyion tanımlayınız.
#sonuçlar da fonksiyon içerisinde ekrana yazdırılsın
# tanımladığınızı bu 2 fonksiyonu tam sayılar gödererek çağırın
def topla2(s1,s2):
    sonuc=s1+s2
    print(f"2 Sayının Toplamı:{sonuc}")

def topla3(s1,s2,s3):
    sonuc=s1+s2+s3
    print(f"3 Sayının Toplamı:{sonuc}")

topla2(65,61)
topla2(25,33)
topla2(65,33)
topla3(98,65,312)
topla3(95,65,312)
