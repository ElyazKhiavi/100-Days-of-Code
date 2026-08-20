import turtle

# Constants for paddle positioning and movement
X_POSITION = 1400          # distance from centre (half of screen width is 1500)
MAX_Y = 760                # upper limit for paddle centre (screen half = 900, paddle half height = 140)
MOVE_DISTANCE = 100


class Paddle(turtle.Turtle):
    """A paddle that can move up and down. If other_side=True, placed on the left."""

    def __init__(self, other_side=False):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=14, stretch_len=3)   # tall and narrow
        self.penup()
        self.color("white")
        self.x_position = X_POSITION
        if other_side:
            self.x_position *= -1
        self.goto(self.x_position, 0)

    def move_up(self):
        """Move the paddle up, but stop at the top boundary."""
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y > MAX_Y:
            return          # don't move past the limit
        self.sety(new_y)

    def move_down(self):
        """Move the paddle down, but stop at the bottom boundary."""
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y < -MAX_Y:
            return
        self.sety(new_y)