#cesar şifreleme programı
#Kavyeden girilen bir kelimeyi girilen anahtar değerine göre cesar şifreleme
#yöntemi ile Şifreler
metin=input("Şifrelenecek Metini Girinz:")
anahtar=int(input("Şifreleme Anahtarınız Girinz:"))

sifreliMetin=""
for herbirHarf in metin:
    harfinKodKarsiligi=ord(herbirHarf)
    sifreliHarfinKodKarsiligi=harfinKodKarsiligi+anahtar
    #Eğer Ascı Tablosunda rakamların dışına çıkılırsa burası devreye girer
    if sifreliHarfinKodKarsiligi>122:
        fark=sifreliHarfinKodKarsiligi-122
        sifreliHarfinKodKarsiligi=fark+96
    sifreliHarf=chr(sifreliHarfinKodKarsiligi)
    sifreliMetin=sifreliMetin+sifreliHarf
print(f"Şifresiz Kelime:{metin}")
print(f"Şifreli Kelime:{sifreliMetin}")

# Program Çalıştırıldığında Aşağıdaki Örnek Çıktıyı Vermektedir.
#Şifrelenecek Metini Girinz:arda
#Şifreleme Anahtarınız Girinz:5
#Şifresiz Kelime:arda
#Şifreli Kelime:fwif

