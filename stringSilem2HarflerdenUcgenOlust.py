#Bir kelimenin harfleri ile üçgen oluşturma
takim=input("Lütfen Takımınızı Giriniz:")
harfSayisi=len(takim)
for i in range(0,harfSayisi+1):
    print(takim[0:i])
