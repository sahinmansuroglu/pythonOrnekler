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
