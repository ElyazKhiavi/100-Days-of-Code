import turtle
import time

X_PACE = 5
Y_PACE = 10
TOP_BOTTOM_BORDER = 850
LEFT_RIGHT_BORDER = 1460
BALL_SIZE = 4
BALL_DIAMETER = BALL_SIZE * 20


class TheBall(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(BALL_SIZE)
        self.x_pace = X_PACE
        self.y_pace = Y_PACE

    def move(self):
        y = self.ycor() + self.y_pace
        x = self.xcor() + self.x_pace
        self.goto((x, y))

    #---------------------Go Out------------------------------
    def hit_right_line(self):
        if self.xcor() > LEFT_RIGHT_BORDER:
            self.x_pace = X_PACE
            return True
        return False

    def hit_left_line(self):
        if self.xcor() < -LEFT_RIGHT_BORDER:
            self.x_pace = X_PACE
            return True
        return False

    # ------------------Bounce------------------------
    def check_top_bottom_collision(self):
        if self.ycor() > TOP_BOTTOM_BORDER or self.ycor() < -TOP_BOTTOM_BORDER:
            self.y_pace *= -1

    #--------------------Hit Paddle--------------------

    def check_paddle_collision(self,r_paddle,l_paddle):
        if self.distance(r_paddle) < 180 and self.xcor() > 1330 or self.distance(l_paddle) < 180 and self.xcor() < -1330:
                self.x_pace *= -1.1 # increase speed by 10 percent every time
