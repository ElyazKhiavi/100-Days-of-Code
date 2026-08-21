# scoreboard.py
# --------------
# Displays the current level and game over message.

import turtle

FONT = ("Courier", 50, "bold")
GAME_OVER_FONT = ("Courier", 200, "bold")
SCOREBOARD_POSITION = (700, -880)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()
        self.update_level()

    def initialize(self):
        """Set up the scoreboard turtle."""
        self.speed("fastest")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)

    def update_level(self, level=0):
        """Clear previous text and write the current level."""
        self.clear()
        self.write(f"Level: {level}", move=False, align="center", font=FONT)

    def game_over(self):
        """Display the game over message."""
        self.home()
        self.color("red")
        self.write("GAME OVER", move=False, align="center", font=GAME_OVER_FONT)