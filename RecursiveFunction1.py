# 1 ile Parametre olarak aldığı sayı arasındaki sayıların toplamını 
# bulan programı recursive(Özyinelemeli) fonk. kullanarak Tasarlayınız.
def topla(sayi):
    if sayi==1:
        return 1
    return sayi+topla(sayi-1)
    
print(f"Sonuc:{topla(5)}")
