#Kullanıcıdan istediği kadar not girebilmesini ve bunların ortalamalarını hesaplatabilmesini sağlayan prograö
girilenPuan=0
puanlarinToplami=0
girilenPuanAdedi=0

while(True):
    girilenPuanAdedi = girilenPuanAdedi + 1
    girilenPuan=int(input(f"{girilenPuanAdedi}. Puanınızı Giriniz:"))
    puanlarinToplami=puanlarinToplami+girilenPuan
    cevap=input("Devam Etmek istiyor musunuz?(E/H):")
    if cevap=="h" or cevap=="H":
        break
ortalama=puanlarinToplami/girilenPuanAdedi

print(f"{girilenPuanAdedi} tane puanın ortalaması:{ortalama}")
