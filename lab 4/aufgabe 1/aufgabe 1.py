import turtle
t = turtle.Turtle()


from alle_buchstaben import *
from costum_buchstben import *


sc = turtle.Screen()
sc.setup(500, 300)

# call methods
turtle.onkey(zen_forne(), 'space')
#turtle.onkey(fxn1, 'Right')
#turtle.onkey(fxn2, 'Left')

turtle.listen()
turtle.done()