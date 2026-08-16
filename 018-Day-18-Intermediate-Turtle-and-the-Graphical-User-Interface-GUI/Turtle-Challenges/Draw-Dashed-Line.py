from turtle import Turtle, Screen

trt = Turtle()
trt.shapesize(5, 5)

trt.color("BlueViolet")
trt.screen.bgcolor("CadetBlue3")
trt.pen(pensize=10)


def dash_40(pace):
    for _ in range(pace):
        # trt.color("CadetBlue3")
        # trt.fd(20)
        # trt.color("BlueViolet")
        # trt.fd(20)

        trt.up()
        trt.fd(30)
        trt.down()
        trt.fd(30)


def draw_dashed_line():
    dash_40(10)
    trt.rt(90)
    dash_40(10)
    for _ in range(4):
        trt.rt(90)
        dash_40(20)


draw_dashed_line()


ms = Screen()
ms.exitonclick()
