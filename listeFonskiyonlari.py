
sayilar=[]
sayilar.append(16) # 16 sayısı sayılar listesinin sonuna eklenir
sayilar.append(10) # 10 sayısı sayılar listesinin sonuna eklenir
sayilar.append(7)   # 7 sayısı sayılar listesinin sonuna eklenir
sayilar.append(25) # 25 sayısı sayılar listesinin sonuna eklenir

print(f"1- 4 Adet Eleman Ekleme Sonrası Liste:{sayilar}")
sayilar.insert(2,45)# 1 ile 2 index numaralı elemanların arasına 45 eklenir
print(f"2- Araya Eleman Ekleme Sonrası Liste:{sayilar}")
ls=[8,6,3,8,10,7]
sayilar.extend(ls) # ls listesi sayılar listesinin sonuna eklenir
print(f"3- Extend ile ekleme Sonrası Liste:{sayilar}")
sayilar.pop(2)# pop il2 2 index numaralı eleman listeden silinir
sayilar.pop()# pop ile listenin son elemanı silinir.
print(f"4- Pop ile Silme Sonrası Liste:{sayilar}")
sayilar.remove(8)# değeri 8 olan elemanı listeden siler
print(f"4- Remove ile Silme Sonrası Liste:{sayilar}")
adet=sayilar.count(10)# listede kaç tane 10 elemanı var onu verir
print(f"5- Listedeki 10 değerli  Eleman Sayısı:{adet}")
sayilar.sort() # Sayılar listesini küçükten büyüğe sıralıyor
print(f"6- Sort İle Sıralama Sonrası Liste:{sayilar}")
sayilar.reverse()# Sayılar listesi ters düz eder
print(f"7- Reverse İle ters çevirme Sonrası Liste:{sayilar}")

# Program Çalıştırıldığında Aşağıdaki Çıktıyı Vermektedir.
# 1- 4 Adet Eleman Ekleme Sonrası Liste:[16, 10, 7, 25]
# 2- Araya Eleman Ekleme Sonrası Liste:[16, 10, 45, 7, 25]
# 3- Extend ile ekleme Sonrası Liste:[16, 10, 45, 7, 25, 8, 6, 3, 8, 10, 7]
# 4- Pop ile Silme Sonrası Liste:[16, 10, 7, 25, 8, 6, 3, 8, 10]
# 4- Remove ile Silme Sonrası Liste:[16, 10, 7, 25, 6, 3, 8, 10]
# 5- Listedeki 10 değerli  Eleman Sayısı:2
# 6- Sort İle Sıralama Sonrası Liste:[3, 6, 7, 8, 10, 10, 16, 25]
# 7- Reverse İle ters çevirme Sonrası Liste:[25, 16, 10, 10, 8, 7, 6, 3]
