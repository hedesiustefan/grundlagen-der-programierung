import turtle

def moveforward():
    turtle.forward(10)
    with open('save_commands.txt', 'a') as file:
        file.write("w")

def movebackwards():
    turtle.forward(-10)
    with open('save_commands.txt', 'a') as file:
        file.write("s")

def turnright():
    turtle.right(45)
    with open('save_commands.txt', 'a') as file:
        file.write("d")

def turnleft():
    turtle.left(45)
    with open('save_commands.txt', 'a') as file:
        file.write("a")

def lift():
    turtle.up()
    with open('save_commands.txt', 'a') as file:
        file.write("f")

def putdown():
    turtle.down()
    with open('save_commands.txt', 'a') as file:
        file.write("g")

def clear_screen():
    turtle.clear()
    with open('save_commands.txt', 'a') as file:
        file.write("c")



def draw():
    turtle.home()
    turtle.clear()
    turtle.onkey(moveforward, 'w')
    turtle.onkey(movebackwards, 's')
    turtle.onkey(turnright, 'd')
    turtle.onkey(turnleft, 'a')
    turtle.onkey(lift, 'f')
    turtle.onkey(putdown, 'g')
    turtle.onkey(clear_screen, 'c')
    turtle.onkey(exit, 'Return')
    turtle.listen()
    turtle.done()

