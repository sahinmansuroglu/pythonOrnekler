from datetime import datetime
from datetime import timedelta
gunListesi=["Pazartesi", "Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
bugun=datetime.today()

eklenecekTarih=timedelta(days=400)

yeniTarih=bugun+eklenecekTarih
print(f"Bugun Tarihi:{bugun.date()}")

kacinciGun=datetime.weekday(bugun)
print(f"Bugün günlerden {gunListesi[kacinciGun]} ")
print(f"400 Gün Sonra Yeni Tarih:{yeniTarih.date()}")

kacinciGun=datetime.weekday(yeniTarih)
print(f"400 Gün Sonra günlerden {gunListesi[kacinciGun]} ")
