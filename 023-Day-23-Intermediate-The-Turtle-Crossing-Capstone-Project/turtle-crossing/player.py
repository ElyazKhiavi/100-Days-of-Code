import turtle

STARTING_POSITION = (0, -840)
MOVE_DISTANCE = 15
PLAYER_SIZE = 2
FINISH_LINE_Y = 870


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(PLAYER_SIZE)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def check_win(self):
        ycor = self.ycor()
        if ycor >= FINISH_LINE_Y:
            return True

    def return_to_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
