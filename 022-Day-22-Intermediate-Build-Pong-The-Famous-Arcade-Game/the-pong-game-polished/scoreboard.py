import turtle

FONT = ("Courier", 80, "italic")
GAME_OVER_FONT = ("Courier", 200, "bold")
ALIGNMENT = "center"
SIDE_X = 120
UP_Y = 800


class Scoreboard(turtle.Turtle):
    """Displays a player's score. left=True places it on the left side."""

    def __init__(self, left=False):
        super().__init__()
        self.score = 0
        self.left_side = left
        self.color("blue")
        self.coordinate = (SIDE_X, UP_Y)
        if self.left_side:
            self.color("red")
            self.coordinate = (-SIDE_X, UP_Y)
        self.set_screen()

    def set_screen(self):
        """Initialize turtle appearance and position."""
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(self.coordinate)
        self.update_score(self.score)

    def update_screen(self, score):
        """Clear previous score and write the new one."""
        self.clear()
        self.write(score, align=ALIGNMENT, font=FONT)

    def update_score(self, score):
        """Set the score and refresh the display."""
        self.score = score
        self.update_screen(self.score)

    def game_over(self):
        """Display the winning message in the centre."""
        self.goto(0, 0)
        if self.left_side:
            self.write("LEFT PLAYER WINS", align=ALIGNMENT, font=GAME_OVER_FONT)
        else:
            self.write("RIGHT PLAYER WINS", align=ALIGNMENT, font=GAME_OVER_FONT)