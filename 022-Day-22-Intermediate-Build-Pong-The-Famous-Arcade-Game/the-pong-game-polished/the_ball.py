import turtle

# Ball movement constants
X_START_SPEED = 5
Y_START_SPEED = 10
TOP_BOTTOM_BORDER = 850        # max y before bounce (screen half = 900, ball radius = 40)
LEFT_RIGHT_BORDER = 1460       # max x before scoring (screen half = 1500)
BALL_SIZE = 4                  # turtle shapesize multiplier
BALL_RADIUS = BALL_SIZE * 20   # ball diameter = 80, radius = 40
PADDLE_COLLISION_DISTANCE = 80 # roughly paddle half width (30) + ball radius (40)


class TheBall(turtle.Turtle):
    """The ball that bounces around and scores points."""

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(BALL_SIZE)
        self.x_pace = X_START_SPEED
        self.y_pace = Y_START_SPEED

    def move(self):
        """Move the ball by its current pace."""
        new_x = self.xcor() + self.x_pace
        new_y = self.ycor() + self.y_pace
        self.goto(new_x, new_y)

    def reset_position(self):
        """Return ball to centre and reset speed."""
        self.goto(0, 0)
        self.x_pace = X_START_SPEED
        self.y_pace = Y_START_SPEED

    def hit_right_line(self):
        """Return True if ball passed the right boundary."""
        if self.xcor() > LEFT_RIGHT_BORDER:
            self.x_pace = X_START_SPEED   # reset speed for next point
            return True
        return False

    def hit_left_line(self):
        """Return True if ball passed the left boundary."""
        if self.xcor() < -LEFT_RIGHT_BORDER:
            self.x_pace = X_START_SPEED
            return True
        return False

    def check_top_bottom_collision(self):
        """Bounce off top and bottom walls."""
        if self.ycor() > TOP_BOTTOM_BORDER or self.ycor() < -TOP_BOTTOM_BORDER:
            self.y_pace *= -1

    def check_paddle_collision(self, r_paddle, l_paddle):
        """Bounce off paddles if ball is close enough and in front of them."""
        # Right paddle
        if self.distance(r_paddle) < PADDLE_COLLISION_DISTANCE and self.xcor() > 0:
            self.x_pace = -abs(self.x_pace)   # ensure it moves left
            self.x_pace *= 1.1                # speed up slightly
        # Left paddle
        elif self.distance(l_paddle) < PADDLE_COLLISION_DISTANCE and self.xcor() < 0:
            self.x_pace = abs(self.x_pace)    # ensure it moves right
            self.x_pace *= 1.1