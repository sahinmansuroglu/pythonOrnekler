//herbir kişi bilgisini ayrı ayrı ekrana yazdırır
kisilerinBilgileri="Ali,25,Mersin-Veli,35,Ankara-Can,23,Rize-Akın,25,Mersin"

kisiBilgiListesi=kisilerinBilgileri.split("-")
i=1
for herBirKisiKaydi in kisiBilgiListesi:
    kisiOzelBilgi=herBirKisiKaydi.split(",")
    print(f"{i}.Kişinin Bilgileri....")
    i+=1
    print(f"Ad:{kisiOzelBilgi[0]}\n"
          f"Yas:{kisiOzelBilgi[1]}\n"
          f"Dogum Yer:{kisiOzelBilgi[2]}")
