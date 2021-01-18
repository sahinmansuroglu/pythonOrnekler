# Cesar algoritması ile şifrelenmiş kelimeyi eski şifrelenmemiş haline getirir.


sifreliMetin=input("Şifresi Çözülecek Metini Girinz:")
anahtar=int(input("Şifreleme Anahtarınız Girinz:"))

gercekMetin=""
for herbirHarf in sifreliMetin:
    harfinKodKarsiligi=ord(herbirHarf)

    gercekHarf=chr(harfinKodKarsiligi-anahtar)
    gercekMetin=gercekMetin+gercekHarf
print(f"Şifreli Kelime:{sifreliMetin}")
print(f"Gerçek kelime:{gercekMetin}")

# Program çalıştırıldığında aşağıdaki gibi bir çıktı vermiştir.
# Şifresi Çözülecek Metini Girinz:dol
# Şifreleme Anahtarınız Girinz:3
# Şifreli Kelime:dol
# Gerçek kelime:ali
