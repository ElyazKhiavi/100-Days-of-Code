# finish_line.py
# ---------------
# Draws a checkered finish line at the top of the screen.

import turtle


class FinishLine(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.pensize(1)

        # Draw three rows of checkered pattern
        y_positions = [900, 870, 840]   # top three rows

        for row, y in enumerate(y_positions):
            self.goto(-900, y)
            for col in range(60):       # 60 squares per row (30 px each)
                if (row + col) % 2 == 0:
                    self.color("black")
                    self.pendown()
                    self.begin_fill()
                    for _ in range(4):
                        self.forward(30)
                        self.right(90)
                    self.end_fill()
                    self.penup()
                    self.forward(30)
                else:
                    self.penup()
                    self.forward(30)