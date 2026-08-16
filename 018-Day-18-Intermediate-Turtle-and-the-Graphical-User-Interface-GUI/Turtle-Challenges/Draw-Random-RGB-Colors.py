# Draw-Random-Colors.py
import turtle
from turtle import Turtle, Screen
import random


def generate_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, g, b)


trt = Turtle()
turtle.colormode(255)
trt.screen.bgcolor(generate_color())
trt.shapesize(3, 3)
trt.pen(pensize=30)
trt.speed("fastest")


moves = [0, 90, 180, 270]
last_move = None
for _ in range(200):
    trt.color(generate_color())
    move = random.choice(moves)
    trt.rt(move)
    trt.fd(100)

    last_move = move


sc = Screen()
sc.exitonclick()
