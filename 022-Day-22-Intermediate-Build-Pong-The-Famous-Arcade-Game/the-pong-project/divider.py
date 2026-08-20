import turtle


class Divider(turtle.Turtle):
    def __init__(self):
        self.color("white")
        self.hideturtle()
        self.pensize(15)
        self.penup()
        self.draw_dotted_line()

    def draw_dotted_line(self):
        pass