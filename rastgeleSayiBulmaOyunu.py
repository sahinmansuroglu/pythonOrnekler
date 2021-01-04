import random

rastgeleSayi=random.randint(0,100)
dogruTahminEdildi=False
for i in range(1,11):
    girilenSayi=int(input(f"{i}. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:"))

    if girilenSayi<rastgeleSayi:
        print("Lütfen Girdiğiniz Sayıyı Büyültün")
    elif girilenSayi>rastgeleSayi:
        print("Lütfen Girdiğiniz Sayıyı Küçültün")
    else:
        dogruTahminEdildi=True
        print("Tebrikler Sayıyı Tahmin Ettiniz")
        break

if dogruTahminEdildi==False:
    print("Üzgünüm Oyunu Kaybettiniz:")
    print(f"Bilgisayarın Tuttuğu sayı:{rastgeleSayi}")

# Program Çalıştırıldığında aşağıdaki sonuç Gözlemlenmiştir
# 1. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:50
# Lütfen Girdiğiniz Sayıyı Küçültün
# 2. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:25
# Lütfen Girdiğiniz Sayıyı Küçültün
# 3. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:10
# Lütfen Girdiğiniz Sayıyı Küçültün
# 4. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:1
# Lütfen Girdiğiniz Sayıyı Büyültün
# 5. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:5
# Lütfen Girdiğiniz Sayıyı Küçültün
# 6. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:3
# Lütfen Girdiğiniz Sayıyı Büyültün
# 7. Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:4
# Tebrikler Sayıyı Tahmin Ettiniz


