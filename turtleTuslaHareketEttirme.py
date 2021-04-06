import turtle  as tospik

def ileri():
    tospik.forward(10)
def geri():
    tospik.backward(10)
def solaDon():
    tospik.left(90)
def sagaDon():
    tospik.right(90)

tospik.shape("turtle")
tospik.Screen().onkey(ileri,"w")
tospik.Screen().onkey(geri,"s")
tospik.Screen().onkey(solaDon,"a")
tospik.Screen().onkey(sagaDon,"d")

tospik.Screen().listen()
tospik.mainloop()
