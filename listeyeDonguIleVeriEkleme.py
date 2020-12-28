
kisiListesi=[]
kisiselBilgi=["Görkem İnci", "Gümüşhane",15]

for i in range(5):
    kisiselBilgi[0]=input(f"{i+1}. kişinin adını giriniz:")
    kisiselBilgi[1]=input(f"{i+1}. kişinin Goğum Yerini giriniz:")
    kisiselBilgi[2] =int(input(f"{i + 1}. kişinin yaşını giriniz:"))
    kisiListesi.append(kisiselBilgi)

for herBirKisi in kisiListesi:
    print(f"Ad Soyad: {herBirKisi[0]}-Doğum Yeri: {herBirKisi[1]}-Yaş: {herBirKisi[2]}")
