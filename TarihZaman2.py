from datetime import  date
from datetime import time
from datetime import datetime
from datetime import  timedelta
from datetime import timezone

suan=datetime.now()# Bunun yerine datetime.today()
print(f"Bugun haftanın {datetime.weekday(suan)+1}. günü")
print(f"Yıl={suan.year}")
print(f"Ay={suan.month}")
print(f"Gün={suan.day}")
print(f"Saat={suan.hour}")
print(f"Dakika={suan.minute}")
print(f"Saniye={suan.second}")
