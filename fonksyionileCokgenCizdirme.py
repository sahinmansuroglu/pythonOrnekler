import turtle as tospik
def cokgenCiz(uzunluk,kenarSayisi,cizgiRengi,dolgurengi):
    tospik.pencolor(cizgiRengi)
    tospik.fillcolor(dolgurengi)
    tospik.begin_fill()
    donmeAcisi=360/kenarSayisi
    for i in range(kenarSayisi):
        tospik.forward(uzunluk)
        tospik.left(donmeAcisi)
    tospik.end_fill()

def konumaGit(x,y):
    tospik.penup()
    tospik.goto(x,y)
    tospik.pendown()

kenarUzunlugu=int(tospik.Screen().textinput("Çokgen Çizme","Kenar Uzunluğu giriniz"))
kenarSayisi=int(tospik.Screen().textinput("Çokgen Çizme","Kenar sayısını giriniz"))
cizgiRengi=tospik.Screen().textinput("Çokgen Çizme","Çizgi Rengini giriniz")
dolguRengi=tospik.Screen().textinput("Çokgen Çizme","Dolgu Rengini giriniz")
konumX=int(tospik.Screen().textinput("Çizilecek Konum","X Konumu gir"))
konumY=int(tospik.Screen().textinput("Çizilecek Konum","Y Konumu gir"))
konumaGit(konumX,konumY)
cokgenCiz(kenarUzunlugu,kenarSayisi,cizgiRengi,dolguRengi)

tospik.mainloop()
