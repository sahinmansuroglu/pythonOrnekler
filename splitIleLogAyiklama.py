# log kayıtları listesinden herhangi bir kişinin girdiği siteleri ve giriş tarihi ayıklayıp ekrana yazdıran program
# bunun için de iç içe 2 adet split kullanıldı
# ilk split ile bir kişinin kaydı bulundu
# ikinci split ile de herbir kaydın adres tarih ve ad bilgileri ayrıldı

logKayit="Ali:www.google.com:21.03.2021," \
         "veli:www.meb.gov.tr:22.04.2021," \
         "Arda:www.abc.com:15.03.2021," \
         "Ali:www.oyun.com:12.04.2021," \
         "Erkan:www.xyz.com:01.05.2021," \
         "Ali:www.haberler.com:23.03.2021"

logKayitList=logKayit.split(",")

kayitSayisi=0
while True:
    kayitSayisi = 0
    aranacakAd=input("Aranacak Adı Giriniz:")
    if aranacakAd=="x":
        break
    for herbirKayit in logKayitList:
        kisiKayitList=herbirKayit.split(":")
        ad=kisiKayitList[0]
        girilenSite=kisiKayitList[1]
        girilenTarih=kisiKayitList[2]
        if ad==aranacakAd:
            kayitSayisi+=1

            print(f"{ad} adlı kisi  {girilenSite} sitesine {girilenTarih} tarihinde girmiştir..")


    if kayitSayisi==0:
        print(f"{aranacakAd} adlı kişinin log kayıtlarında bilgisi yoktur")
    else:
        print(f"{aranacakAd} adlı kişinin {kayitSayisi} tane kaydı vardır.")
print("Çıkış Yapıldı..")

# Örnek Çıktı:
# Aranacak Adı Giriniz:Ahmet
# Ahmet adlı kişinin log kayıtlarında bilgisi yoktur
# Aranacak Adı Giriniz:Arda
# Arda adlı kisi  www.abc.com sitesine 15.03.2021 tarihinde girmiştir..
# Arda adlı kişinin 1 tane kaydı vardır.
# Aranacak Adı Giriniz:Ali
# Ali adlı kisi  www.google.com sitesine 21.03.2021 tarihinde girmiştir..
# Ali adlı kisi  www.oyun.com sitesine 12.04.2021 tarihinde girmiştir..
# Ali adlı kisi  www.haberler.com sitesine 23.03.2021 tarihinde girmiştir..
# Ali adlı kişinin 3 tane kaydı vardır.
# Aranacak Adı Giriniz:Erkan
# Erkan adlı kisi  www.xyz.com sitesine 01.05.2021 tarihinde girmiştir..
# Erkan adlı kişinin 1 tane kaydı vardır.
# Aranacak Adı Giriniz:x
# Çıkış Yapıldı..
