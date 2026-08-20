import turtle

## THESE NUMBERS ARE EXPERIMENTAL CHANGE TO MODIFY TO FIT YOUR SCREEN SIZE
X_POSITION = 1400  # this is a little less then half the screen size
Y_POSITION = 760
PACE = 100
DISTANCE = 60


class Paddle(turtle.Turtle):
    def __init__(self, other_side=False):
        super().__init__()
        self.shape("square")
        self.shapesize(14, 3)
        self.up()
        self.color("white")
        self.x_position = X_POSITION
        if other_side:
            self.x_position *= -1
            self.goto(x=self.x_position, y=0)
        else:
            self.goto(x=self.x_position, y=0)

    def move_up(self):
        y = self.ycor()
        if self.distance(x=self.x_position, y=Y_POSITION) < DISTANCE:
            return
        y += PACE
        x = self.xcor()
        self.goto((x, y))

    def move_down(self):
        y = self.ycor()
        if self.distance(x=self.x_position, y=-Y_POSITION) < DISTANCE:
            return
        y -= PACE
        x = self.xcor()
        self.goto((x, y))
