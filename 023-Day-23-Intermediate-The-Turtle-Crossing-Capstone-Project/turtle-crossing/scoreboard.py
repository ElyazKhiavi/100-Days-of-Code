import turtle

FONT = ("Courier", 50, "bold")
GAME_OVER_FONT = ("Courier", 200, "bold")

SCORE_BOARD_POSITION = (700, -880)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()
        self.update_level()

    def initialize(self):
        self.speed("fastest")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_BOARD_POSITION)

    def update_level(self, level=0):
        self.clear()
        self.write(f"Level: {level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.home()
        self.color("red")
        self.write("GAME OVER", move=False, align="center", font=GAME_OVER_FONT)
