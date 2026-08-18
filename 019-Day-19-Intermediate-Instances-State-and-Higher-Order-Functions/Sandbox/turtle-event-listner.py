from turtle import Turtle, Screen
import turtle
from random import randint


def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


trt = Turtle()
trt.hideturtle()
trt.pensize(15)
# turtle.colormode(255)
# trt.screen.bgcolor("lavender")
# trt.shapesize(3)
# trt.pensize(15)
# trt.speed("fastest")
# trt.shape("turtle")
# trt.color("darkgreen")


def move(direction):
    trt.tiltangle(direction)
    trt.setheading(direction)
    trt.fd(50)


sc = Screen()


sc.listen()
sc.onkey(fun=lambda: move(0), key="Right")
sc.onkey(fun=lambda: move(180), key="Left")
sc.onkey(fun=lambda: move(90), key="Up")
sc.onkey(fun=lambda: move(270), key="Down")


sc.onkey(fun=lambda: trt.fd(50), key="c")
sc.onkey(fun=lambda: trt.fd(-50), key="t")
sc.onkey(fun=lambda: trt.rt(10), key="n")
sc.onkey(fun=lambda: trt.lt(10), key="h")
sc.onkey(fun=turtle.resetscreen, key="x")


sc.exitonclick()
