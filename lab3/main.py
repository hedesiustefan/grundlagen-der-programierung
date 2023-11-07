
import turtle
t = turtle.Turtle()
t2 = turtle.Turtle()


def rechteck():
    t2.hideturtle()
    t.reset()
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)

    t.up()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)

    t.down()
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)



def herz():
    t2.hideturtle()
    t.speed(2)
    def curve():
        for i in range(200):
            t.right(1)
            t.forward(1)

    def heart():
        t.fillcolor('red')
        t.begin_fill()

        t.left(140)
        t.forward(113)

        curve()
        t.left(120)
        curve()
        t.forward(112)

        t.end_fill()

    heart()




def hauser():
    t.up()
    t.pensize(3)
    t.speed(5)
    t2.up()
    t2.pensize(3)
    t2.speed(5)
    t.goto(200, 200)
    t2.goto(-200, -200)
    t.down()
    t2.down()
    # corpul casei
    i = 0
    for i in range(2):
        t.forward(200)
        t2.forward(200)
        t.left(90)
        t2.left(90)
        t.forward(100)
        t2.forward(100)
        t.left(90)
        t2.left(90)
        i += 1
    # acoperis 1
    t.up()
    t.right(90)
    t.backward(100)
    t.left(135)
    t.down()
    t.forward(141)
    t.right(90)
    t.forward(141)
    # acoperis 2
    t2.up()
    t2.right(90)
    t2.backward(100)
    t2.left(135)
    t2.down()
    t2.forward(141)
    t2.right(90)
    t2.forward(141)
    # usa 1
    t.up()
    t.goto(300, 200)
    t.left(135)
    t.down()
    t.forward(75)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(75)
    # usa 2
    t2.up()
    t2.goto(-100, -200)
    t2.left(135)
    t2.down()
    t2.forward(75)
    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.forward(75)

    t.up()
    t2.up()
    # geam 1 si 2
    t.left(90)
    t.backward(125)
    t.left(90)
    t.forward(25)
    t.right(90)

    t2.left(90)
    t2.backward(125)
    t2.left(90)
    t2.forward(25)
    t2.right(90)

    t.down()
    t2.down()

    for i in range(4):
        t.forward(50)
        t2.forward(50)
        t.left(90)
        t2.left(90)
        i += 1


while True:
    print("Give a number:")
    print("1) Rechtecke")
    print("2) Herz")
    print("3) Hauser")
    print("4) Reset")

    wahl = input("Ihre Auswahl (1-4): ")

    if wahl == '1':
        rechteck()
    if wahl == '2':
        herz()
    if wahl == '3':
        t2 = turtle.Turtle()
        hauser()
    elif wahl == '4':
        t.reset()
        t2.reset()
    else:
        print("pick another number")


turtle.done()