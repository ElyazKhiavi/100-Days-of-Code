import turtle


class Divider(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("white")
        self.pensize(15)
        self.penup()
        self.draw_dotted_line()

    def draw_dotted_line(self):
        self.setheading(270)
        self.fd(1000)
        self.setheading(90)
        for pace in range(0,2000,50):
            self.fd(50)
            if self.isdown():
                self.penup()
            else:
                self.pendown()