from datetime import  date
from datetime import time
from datetime import datetime
from datetime import  timedelta
from datetime import timezone

suan=datetime.now()# Bunun yerine datetime.today()

#1- Tüm tarih bilgisini (arih saat dakika sanine milisaniye) görüntüler
print(f"1-Şuan da tarih:{suan}")

#2- Sadece tarihi Görüntüler
bugun=date.today()
print(f"2-Şuan da tarih:{bugun}")

#3- Haftanın Kaçıncı Günü Olduğunu öğrenme
kacinci=date.weekday(bugun)
print(f"3-Bugun haftanın {kacinci+1}. günü")
