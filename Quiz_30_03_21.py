#1  Girilen Sayı ile 1-10 arasındaki sayıların çarpımını alt alta yazan programı tasarlayınız
# For Döngüsü
while (True):
    girilenSayi=int(input("Lütfen 1- ile 10 arasında bir sayı giriniz:"))
    if (girilenSayi<=10 and girilenSayi>=1):
        for i in range(1,11):
            print(f"{girilenSayi}x{i}={i*girilenSayi}")
    else:
        print("Girilen Sayi 1 ile 10 arasında değildir")
#2  Girilen Sayı ile 1-10 arasındaki sayıların çarpımını alt alta yazan programı tasarlayınız
# While Döngüsü
while (True):
    girilenSayi=int(input("Lütfen 1 ile 10 arasında bir sayı giriniz:"))
    if (girilenSayi<=10 and girilenSayi>=1):
        i=1
        while i<=10:
            print(f"{girilenSayi}x{i}={i*girilenSayi}")
            i=i+1
    else:
        print("Girilen Sayi 1 ile 10 arasında değildir")

#3  Çarpım tablosunu hazırlayan programı tasarlayınız
for i in range(1,11):
    print(f"{i} sayısının çarpım tablosu")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
#4 Bilgisayardan rastgele 10 sayı üretmesini ve bunların toplamı ile ortalamasını
#hesaplatıp ekrana yazdırınız
import random
import time
print("Size 10 tane 1 ile 1000 arasında sayı üreteceğim")
toplam=0
for i in range(1,11):
    print(f"{i}. sayıyı üretiyorum..")
    time.sleep(2)
    rastgeleSayi=random.randint(1,1000)
    toplam=rastgeleSayi+toplam
    print(f"{rastgeleSayi} sayısını ürettim..")
    print("************************")
print("Toplam ve Ortalama hesaplatılıyor ")
time.sleep(3)
print(f"Urettiğim 10 sayının toplamı={toplam}")
print(f"Urettiğim 10 sayının ortalaması={toplam/10}")

#5 Bilgisayara 1 ile 10 arasında rastgele 5 adet sayı ürettiriniz:
# Üretilen sayıların içerisinde hiçbir zaman tekrar eden sayı olmayacak
import  random
sayiList=[]
i=1
while i<=5:
    uretilenSayi=random.randint(1,10)
    if uretilenSayi in sayiList:
        print(f"tekrarlı sayı:{uretilenSayi}")
    else:
        sayiList.append(uretilenSayi)
        i=i+1

print(sayiList)
