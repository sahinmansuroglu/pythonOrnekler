import turtle as tospik
def konumaGit(x,y):
    tospik.penup()
    tospik.goto(x,y)
    tospik.pendown()
def cemberCiz():
    yariCap = int(tospik.Screen().textinput("Çember Çizme", "Yarıçap Uzunluğu giriniz"))
    cizgiRengi = tospik.Screen().textinput("Çember Çizme", "Çizgi Rengini giriniz")
    dolguRengi = tospik.Screen().textinput("Çember Çizme", "Dolgu Rengini giriniz")
    tospik.pencolor(cizgiRengi)
    tospik.fillcolor(dolguRengi)
    tospik.begin_fill()
    tospik.circle(yariCap,360)
    tospik.end_fill()
def sekilCiz(x,y):
    konumaGit(x,y)
    cemberCiz()
tospik.Screen().onclick(sekilCiz)
tospik.mainloop()
