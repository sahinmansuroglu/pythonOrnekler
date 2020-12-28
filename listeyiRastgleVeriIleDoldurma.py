from random import randint,seed
import time
adSoyadListesi=["Arda Turan","Goergoe Hagi","Radamel Falcao","Fernado Muslera","Emre Kılınç"]
dogumYeriListesi=["Ankara","Adana","Adıyaman","Mersin","İstanbul","İzmir"]
kisiselBilgi=["Ali","MErsin",25]
kisiListesi=[]
for i in range(30):
    seed(time.time()*i)


    kisiselBilgi[0]=adSoyadListesi[randint(0,4)]
    seed(time.time()*i)
    kisiselBilgi[1]=dogumYeriListesi[randint(0,4)]
    seed(time.time()*i)
    kisiselBilgi[2] =randint(20,40)
    print(f"Ad Soyad: {kisiselBilgi[0]}-Doğum Yeri: {kisiselBilgi[1]}-Yaş: {kisiselBilgi[2]}")
    kisiListesi.append(kisiselBilgi)


