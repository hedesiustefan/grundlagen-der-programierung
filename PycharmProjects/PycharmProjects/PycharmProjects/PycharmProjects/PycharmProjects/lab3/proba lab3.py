import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
t.up()
t.pensize(3)
t.speed(5)
t2.up()
t2.pensize(3)
t2.speed(5)
t.goto(200,200)
t2.goto(-200,-200)
t.down()
t2.down()
#corpul casei
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
#usa 1
t.up()
t.goto(300,200)
t.left(135)
t.down()
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)
#usa 2
t2.up()
t2.goto(-100,-200)
t2.left(135)
t2.down()
t2.forward(75)
t2.right(90)
t2.forward(50)
t2.right(90)
t2.forward(75)

t.up()
t2.up()
#geam 1 si 2
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





turtle.done()