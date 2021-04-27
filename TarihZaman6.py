from datetime import datetime
from datetime import timedelta

bugun=datetime.today()
print(f"Bugun:{bugun}")

print(f"{bugun.strftime('%Y')}")# yılı Görüntüler
print(f"{bugun.strftime('%X')}")# Saati Görüntüler
print(f"{bugun.strftime('%d')}")# ayın kaçıncı günü
print(f"{bugun.strftime('%A')}")# gün ismini yazar
print(f"{bugun.strftime('%B')}")# ay ismini yazar
