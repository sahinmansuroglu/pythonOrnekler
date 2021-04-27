# Parametre olarak Aldığı Sayının faktöriyelini
# bulan programı recursive(Özyinelemeli) fonk. kullanarak Tasarlayınız.
def faktoriyel(sayi):
    if sayi==1:
        return 1
    return sayi*faktoriyel(sayi-1)

print(f"Sonuc:{faktoriyel(6)}")
