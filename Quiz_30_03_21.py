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
