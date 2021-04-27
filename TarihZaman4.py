from datetime import  date
from datetime import time
from datetime import datetime
from datetime import  timedelta
from datetime import timezone

gunListesi=["Pazartesi", "Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
dogumTarihi=datetime(year=2006,month=10,day=13)
bugun=datetime.today()
print(f"Doğum Tarihiniz:{dogumTarihi}")
print(f"Bugunun Tarihi:{bugun}")
yas=bugun-dogumTarihi
print(yas)
print(f"{yas.days} gün")
print(f"{yas.seconds} saniye")

