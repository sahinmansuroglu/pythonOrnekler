#1...Listenin İçindeki elemanları alt alta yazdırma
adlar=["Arda","Ali","Mehmet", "Serkan","Erkan"]

for herBirAd in adlar:
    print(herBirAd)

#2...Kullanıcının girdiği ad'ın listede olup olmadığını bulan program

adlar=["Arda","Ali","Mehmet", "Serkan","Erkan","Sezgin"]

girilenAd=input("Aradığınız adı giriniz:")

if girilenAd in adlar:
    print("Girilen ad listede mevcut")
else:
    print("Girilen ad listede mevcut değil")

    
#3... bir kelimenin içerisindeki a harfi sayısını bulan program

kelime="Merhabalar"
aHarfiSayisi=0
for herbirHarf in kelime:
    if herbirHarf=="e":
        aHarfiSayisi=aHarfiSayisi+1
print(f"{aHarfiSayisi}")

#4.. birden fazla print ile metinleri yanyana yazdırma. 
print("a",end="")
print("l",end="")
print("i")

#5. bir cümlenin tüm karakterlerinin  arasına * karakteri koyan program
cumle="Selamar Bugün Nasılsınız?"


for herbirHarf in cumle:
    print(herbirHarf,end="*")
    
#6... Klavyeden girilen Cümlenin kelimlerini alta yazan ve kaç kelime bulunuduğunu hesaplayıp ekrana
#yazan programı tasarlayınız

cumle=input("Cümlenizi Giriniz:")

kelimeSayisi=1
for herbirHarf in cumle:
    print(herbirHarf,end="")
    if herbirHarf==" ":
        kelimeSayisi=kelimeSayisi+1
        print("")

print(f"\nKelime Sayısı={kelimeSayisi}")
#7.puan listesindeki zayıf notları ve adedini ekrana yazdırma
puanListesi=[45,65,77,88,23,89,78,67,56,76,87]
kalanNotSayisi=0
for herbirPuan in puanListesi:
    if herbirPuan<50:
        print(herbirPuan,end="_")
        kalanNotSayisi=kalanNotSayisi+1

print(f"\nBaşarısız Not Sayisi:{kalanNotSayisi}")

#8....puan listesindeki puanların ortalaması
puanListesi=[45,65,77,88,23,89,78,67,56,76,87]
puanToplam=0
for herbirPuan in puanListesi:
    puanToplam=puanToplam+herbirPuan

ortalama= puanToplam / len(puanListesi)
print(f"\n Ortalama:{ortalama}")

#8....puan listesindeki 3 Notuna karşılık kaç puan var bunu hesaplatın
puanListesi=[45,65,77,88,23,89,78,67,56,76,87]
adet=0
for herbirPuan in puanListesi:
    if herbirPuan>=60 and herbirPuan<=69:
        print(herbirPuan,end=" ")
        adet=adet+1
print(f"\n3 notuna karşılık gelen puan adedi:{adet}")#9....puan listesindeki  en büyük ve en küçük puanıu buludurm ekrana yazdıran program
puanListesi=[45,65,77,88,23,89,78,67,56,76,87]
enBuyukPuan=puanListesi[0]
enKucukPuan=puanListesi[0]
for herbirPuan in puanListesi:
    if herbirPuan>enBuyukPuan:
        enBuyukPuan=herbirPuan
    if herbirPuan<enKucukPuan:
        enKucukPuan=herbirPuan

print(f"Listedeki En Küçük Puan:{enKucukPuan}")
print(f"Listedeki En Büyük Puan:{enBuyukPuan}")




