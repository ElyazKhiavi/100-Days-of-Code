# scoreboard

import turtle

FONT = ("Arcade", 80, "italic")
GAME_OVER_FONT = ("Arcade", 200, "BOLD")
ALIGNMENT = "center"
SIDE = 120
UP = 800


class Scoreboard(turtle.Turtle):
    """Score board it cane be set to left or right"""

    def __init__(self, left=False):
        super().__init__()
        self.score = 0
        self.coordinate = (SIDE, UP)
        self.color("blue")
        self.left_side = left
        if self.left_side:
            self.color("red")
            self.coordinate = (-SIDE, UP)
        self.set_screen()


    def set_screen(self):
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(self.coordinate)
        self.update_score(self.score)

    def update_screen(self, score):
        self.clear()
        self.write(score, False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0,0)
        if self.left_side:
            self.write('LEFT PLAYER WINS', False, ALIGNMENT, FONT)
            return
        self.write('RIGHT PLAYER WIN', False, ALIGNMENT, FONT)
        
    def update_score(self, score):
        self.score = score
        self.update_screen(self.score)
