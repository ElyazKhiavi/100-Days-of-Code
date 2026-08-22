import turtle

"""
Turtle has a size of 20 * 20 and it starts at pos(0,0)
when we increase the shapesize we multiply the size by that number so now our turtles are 60*60 so when we move them we need to move them by 3 times to get to the right position 
"""
STARTING_POSITIONS = [(0, 0), (-40, 0), (-80, 0)]
MOVE_DISTANCE = 40
"""directions the snake can move"""
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(2)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend_snake(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.fd(MOVE_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]   

    """snake movements up-down-left-right"""

    def up(self):  # move up 90

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):  # move down 270

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):  # move left 180

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):  # move right 0

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def __str__(self):
        return f"Create the Snake - Current Segments: {len(self.segments)} "
