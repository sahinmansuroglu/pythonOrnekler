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
