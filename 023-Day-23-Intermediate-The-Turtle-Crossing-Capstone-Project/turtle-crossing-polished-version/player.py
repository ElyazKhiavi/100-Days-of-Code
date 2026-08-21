# player.py
# ----------
# Defines the Player class (a turtle) that moves upward.

import turtle

STARTING_POSITION = (0, -840)
MOVE_DISTANCE = 15
PLAYER_SIZE = 2
FINISH_LINE_Y = 870      # Must be reached to win


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(PLAYER_SIZE)
        self.color("black")
        self.penup()
        self.return_to_start()

    def move(self):
        """Move the player forward (upward)."""
        self.forward(MOVE_DISTANCE)

    def check_win(self):
        """Return True if the player has reached the finish line."""
        return self.ycor() >= FINISH_LINE_Y

    def return_to_start(self):
        """Reset player to starting position."""
        self.goto(STARTING_POSITION)
        self.setheading(90)