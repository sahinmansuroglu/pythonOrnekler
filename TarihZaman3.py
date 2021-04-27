from datetime import  date
from datetime import time
from datetime import datetime
from datetime import  timedelta
from datetime import timezone

gunListesi=["Pazartesi", "Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
dogumTarihi=datetime(year=2006,month=10,day=13)
print(f"Doğum Tarihiniz:{dogumTarihi}")
kacinciGun=datetime.weekday(dogumTarihi)
print(f"Doğum günü:{gunListesi[kacinciGun]}")

