import random
ls=[] # boş bir listeler oluşturuyor
toplam=0
for i in range(1,11):

    rastgeleSayi=random.randint(1,100) #Bilgisayar 1 ile 100 arası rastgele sayı üretir
    toplam=toplam+rastgeleSayi# Rastgele Sayıyı toplama ekler
    ls.append(rastgeleSayi)# Rastgele Sayıyı listeye ekler


print(f"Bilgisayarın listeye rastgeleAttiği Elemanlar")
print(ls)
print(f"Listedeki Elemanların Toplamı:{toplam}")
ortalama=toplam/len(ls)# toplamı eleman sayısına bölerek ortalamayı hesaplar
print(f"Listedeki Elemanların Ortalaması:{ortalama}")

# Program çalıştıgında aşağıdaki çıktıyı üretmiştir
# Bilgisayarın listeye rastgeleAttiği Elemanlar
# [39, 33, 43, 73, 64, 77, 94, 68, 15, 49]
# Listedeki Elemanların Toplamı:555
# Listedeki Elemanların Ortalaması:55.5
