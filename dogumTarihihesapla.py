from  datetime import date

dogumGun=int(input("Dogum Günüzü Giriniz"))
dogumAy=int(input("Dogum ayinizi Giriniz:"))
dogumYil=int(input("Dogum yılınızı Giriniz:"))

dogumTarihi=date(dogumYil,dogumAy,dogumGun)
bugun=date.today()

aradakiGunSayisi=(bugun-dogumTarihi).days

gunSayisi=aradakiGunSayisi
yil=gunSayisi//365
artanGunSayisi=gunSayisi%365
artaAySayisi=artanGunSayisi//30
print(f"{gunSayisi}: {yil} yil ve {artaAySayisi} aydir'dür ")


