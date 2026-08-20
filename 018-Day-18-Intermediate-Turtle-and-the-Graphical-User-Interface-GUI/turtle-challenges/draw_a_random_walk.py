# Draw-a-Random-Walk.py

from turtle import Turtle, Screen
import random

trt = Turtle()
trt.screen.bgcolor("Black")
trt.shapesize(3,3)
trt.pen(pensize=30)
trt.speed('fastest')

colors = [
    "#FFD700",  # gold
    "#FF4500",  # orange red
    "#00FF7F",  # spring green
    "#00BFFF",  # deep sky blue
    "#FF69B4",  # hot pink
    "#ADFF2F",  # green yellow
    "#FF1493",  # deep pink
    "#7FFFD4",  # aquamarine
    "#FFA500",  # orange
    "#00FFFF",  # cyan
    "#FF00FF",  # magenta
    "#FFFF00",  # yellow
    "#FF6347",  # tomato
    "#40E0D0",  # turquoise
    "#FFDAB9",  # peach puff
    "#FFFFFF",  # white
    "#DA70D6",  # orchid
    "#F0E68C",  # khaki
]

moves = [0, 90, 180, 270]
last_move = None
for _ in range(200):
    trt.color(random.choice(colors))
    move = random.choice(moves)
    trt.rt(move)
    trt.fd(100)

    last_move = move



sc = Screen()
sc.exitonclick()
