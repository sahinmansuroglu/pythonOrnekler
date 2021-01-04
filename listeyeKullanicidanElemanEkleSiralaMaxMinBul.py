ls=[]
sayiAdedi=int (input("Kaç tane Sayı Girmek İstersiniz:"))

for i  in range(1,sayiAdedi+1):
    girilenSayi=int (input(f"{i}. Sayıyı Giriniz:"))
    ls.append(girilenSayi)
print(f"Sıralama Öncesi liste={ls}")
ls.sort()
print(f"Sıralama Sonrası liste={ls}")
enKucukSayi=ls[0]
enBuyukSayi=ls[-1]
print(f"Sayi listesinin En Büyük Elamanı:{enBuyukSayi}")
print(f"Sayi listesinin En Küçük Elamanı:{enKucukSayi}")

#Uygulamanın Çıktısı Aşağıdadır
# Kaç tane Sayı Girmek İstersiniz:10
# 1. Sayıyı Giriniz:65
# 2. Sayıyı Giriniz:96
# 3. Sayıyı Giriniz:85
# 4. Sayıyı Giriniz:15
# 5. Sayıyı Giriniz:45
# 6. Sayıyı Giriniz:36
# 7. Sayıyı Giriniz:74
# 8. Sayıyı Giriniz:98
# 9. Sayıyı Giriniz:25
# 10. Sayıyı Giriniz:75
# Sıralama Öncesi liste=[65, 96, 85, 15, 45, 36, 74, 98, 25, 75]
# Sıralama Sonrası liste=[15, 25, 36, 45, 65, 74, 75, 85, 96, 98]
# Sayi listesinin En Büyük Elamanı:98
# Sayi listesinin En Küçük Elamanı:15
