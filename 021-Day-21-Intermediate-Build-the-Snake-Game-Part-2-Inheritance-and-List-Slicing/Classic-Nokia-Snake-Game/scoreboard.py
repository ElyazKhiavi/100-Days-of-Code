# ScoreBoard
import turtle

ALIGNMENT = "center"
NORMAL_FONT = ("Courier", 38, "italic")
GAME_OVER_FONT = ("Courier", 60, "italic")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.set_screen()
        self.update_screen(self.score)

    def set_screen(self):
        self.speed("fastest")
        self.goto(x=-50, y=800)
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_screen(self, score):
        self.clear()
        self.write(f"Score: {score}", False, ALIGNMENT, NORMAL_FONT)

    def game_over(self):
        self.color('red')
        self.goto(0,0)
        self.write(f"GAME OVER", False, ALIGNMENT, GAME_OVER_FONT)

    def update_score(self, score):
        self.score = score
        self.update_screen(self.score)
