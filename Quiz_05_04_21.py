#1. Ekrana 2 kez "Merhaba Dünya" yazdıran adı da ekranaMesajYaz olan
# bir fonksiyon tanımlayın ve bu fonksiyonu 4 kez çağırın.
def ekranaMesajYaz():
    print("Merhaba Dünya")
    print("Merhaba Dünya")


ekranaMesajYaz()
ekranaMesajYaz()
ekranaMesajYaz()
ekranaMesajYaz()

#2. "ad" isminde bir parametre alan ve ad'ın başına merhaba koyup
#ekrana yazdıran ekranaMesajYaz adında bir fonksiyon tanımlayınız
#ve fonksiyona 4 farklı isim stringi göndererek fonksiyonu çağırınız

def ekranaMesajYaz(ad):
    print(f"Merhaba {ad}")

ad1="serdar"
ad2="Selin"
ekranaMesajYaz(ad1)
ekranaMesajYaz(ad2)
ekranaMesajYaz("Mehmet")
ekranaMesajYaz("Ceren")

