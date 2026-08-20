# Million_Dollar_Dot_Panting
from turtle import Turtle, Screen
import turtle
import random

colors = [
    (54, 89, 131),      # slate blue
    (140, 26, 48),      # deep red
    (222, 206, 108),    # pale gold
    (132, 177, 202),    # powder blue
    (158, 46, 84),      # magenta plum
    (47, 55, 103),      # navy
    (208, 160, 82),     # ochre
    (146, 91, 40),      # burnt sienna
    (36, 130, 50),      # emerald
    (255, 106, 0),      # vivid orange
    (247, 0, 165),      # hot pink
    (70, 180, 180),     # turquoise
    (255, 237, 0),      # canary yellow
    (185, 55, 85),      # raspberry
    (0, 128, 128),      # teal
    (210, 180, 140),    # tan
    (100, 50, 150),     # violet
    (255, 69, 0),       # orange red
    (0, 100, 0),        # dark green
    (255, 255, 255),    # white (if you want white dots)
]


def get_color():
    return random.choice(colors)


trt = Turtle()
turtle.colormode(255)
trt.screen.bgcolor("lavender")
trt.up()
trt.hideturtle()

trt.rt(135)
trt.fd(700)
trt.rt(-135)

def turn_on_right():
    trt.dot(50, get_color())
    trt.rt(-90)
    trt.fd(113.1)
    trt.rt(-90)

def turn_on_left():
    trt.dot(50, get_color())
    trt.rt(90)
    trt.fd(113.1)
    trt.rt(90)

on_right = True
for _ in range (10):
    for _ in range(10):
        trt.dot(50, get_color())
        trt.fd(113.1)
    if on_right:
        turn_on_right()
        on_right=False
    else:
        turn_on_left()
        on_right = True

sc = Screen()
sc.exitonclick()
