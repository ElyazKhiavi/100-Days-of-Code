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
trt.speed("fastest")
trt.shapesize(2)
trt.pensize(5)


def draw_circles(gap):
    trt.color(generate_color())
    trt.circle(
        radius=300,
    )
    for _ in range(360/gap):
        trt.rt(gap)
        

draw_circles(5)

sc = Screen()
sc.exitonclick()
