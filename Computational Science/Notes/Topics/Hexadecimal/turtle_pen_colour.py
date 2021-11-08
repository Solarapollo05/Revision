import turtle
import random

f_value = random.randint(100,200)
l_or_r = random.randint(0,360)


key = ""

myTurtle = turtle.Turtle()

myTurtle.pencolor("#000000")

myTurtle.fillcolor("#ae00ff")

myTurtle.pensize(10)
myTurtle.begin_fill()

for side in range (4):
    myTurtle.forward(f_value)
    myTurtle.right(l_or_r)
myTurtle.end_fill()
