import turtle


class Divider(turtle.Turtle):
    """Draws a dashed vertical line in the centre of the screen."""

    def __init__(self, screen_height):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("white")
        self.pensize(15)
        self.penup()
        self.draw_dotted_line(screen_height)

    def draw_dotted_line(self, screen_height):
        """
        Draw a dotted line from bottom to top of the screen.
        The line is made of alternating short segments.
        """
        half_height = screen_height // 2
        segment_length = 40
        gap_length = 20

        # Start at bottom, slightly inside the screen
        self.goto(0, -half_height + 20)
        self.setheading(90)   # face upwards

        # Draw alternating drawn/blank segments
        y = -half_height + 20
        while y < half_height - 20:
            self.pendown()
            self.forward(segment_length)
            self.penup()
            self.forward(gap_length)
            y += segment_length + gap_length