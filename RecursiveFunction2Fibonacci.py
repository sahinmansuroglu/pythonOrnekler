# Parametre olarak Aldığı Sayının faktöriyelini
# bulan programı recursive(Özyinelemeli) fonk. kullanarak Tasarlayınız.
def fibonacci(sayi):
    if sayi==1:
        return 1
    elif sayi==2:
        return 1
    else:
        return fibonacci(sayi-1)+fibonacci(sayi-2)

print(f"Sonuc:{fibonacci(7)}")
