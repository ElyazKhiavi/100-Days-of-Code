from turtle import Turtle, Screen

trt = Turtle()
trt.shapesize(2, 2)
trt.color("BlueViolet")
trt.screen.bgcolor("CadetBlue3")


def draw_square():
    trt.fd(400)
    trt.rt(90)
    trt.fd(400)
    for _ in range(4):
        trt.rt(90)
        trt.fd(800)


draw_square()


ms = Screen()
ms.exitonclick()
