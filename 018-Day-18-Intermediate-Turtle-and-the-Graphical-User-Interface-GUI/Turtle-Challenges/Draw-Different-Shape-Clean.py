from turtle import Turtle, Screen

trt = Turtle()
trt.screen.bgcolor("Black")
trt.pen(pensize=10)

trt.rt(-90)
trt.up()
trt.fd(500)
trt.down()
trt.rt(90)

colors = [
    "black",
    "red",
    "blue",
    "DarkOrchid",
    "DarkSlateBlue",
    "azure4",
    "DarkBlue",
    "CornflowerBlue",
    "coral4",
    "DarkOrange",
    "firebrick",
    "goldenrod",
    "green4",
    "hotpink",
    "indigo",
    "khaki4",
    "lightcoral",
    "maroon",
]


def draw_polygon_from_base(number_of_diagonals, pace):
    angle = 360 / number_of_diagonals
    trt.fd(pace / 2)
    for _ in range(number_of_diagonals - 1):
        trt.rt(angle)
        trt.fd(pace)
    trt.rt(angle)
    trt.fd(pace / 2)


for sides in range(3, 21):
    trt.color(colors[sides - 3])
    draw_polygon_from_base(sides, 100)


sc = Screen()
sc.exitonclick()
