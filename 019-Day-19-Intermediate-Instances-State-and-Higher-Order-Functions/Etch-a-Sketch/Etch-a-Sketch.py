import turtle 
import random


trt = turtle.Turtle()
scr = turtle.Screen()
trt.speed('fastest')
trt.screen.bgcolor('lavender')
trt.shape('turtle')
trt.shapesize(4)
trt.pensize(15)

def move(direction):
    trt.setheading(direction)
    trt.fd(25)

def clear():
    trt.clear()
    trt.up()
    trt.home()
    trt.down()

scr.listen()
turtle.onkey(fun=lambda: move(0), key='Right')
turtle.onkey(fun=lambda: move(180), key='Left')
turtle.onkey(fun=lambda: move(90), key='Up')
turtle.onkey(fun=lambda: move(270), key='Down')

turtle.onkey(fun=clear, key='space')
scr.exitonclick()