# Classic-Nokia-Snake-Game
from turtle import Turtle, Screen
import turtle
import time

src = Screen()
src.setup(width=2000, height=2000)
src.bgcolor("black")
src.title("Classic Nokia Snake Game")
src.tracer(0)

"""
Turtle has a size of 20 * 20 and it starts at pos(0,0)
when we increase the shapesize we multiply the size by that number so now our turtles are 60*60 so when we move them we need to move them by 3 times to get to the right position 
"""

starting_positions = [(0, 0), (-40, 0), (-80, 0),(-120, 0), (-160, 0), (-200, 0),(-240, 0), (-280, 0), (-320, 0)]

snake_body = []

for position in starting_positions:
    new_turtle = Turtle("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.shapesize(2)
    new_turtle.goto(position)
    snake_body.append(new_turtle)

'''for moving the turtle instead of giving coordinates to every segment to where they gov we can just give coordinates to the first one and tell the other segments to come to the position of the segment above
in this form we start the movement from the back and every segment move on top of each other basically until we reach the first segment that has the real position to where to take the snake (other segments)'''


game_over = False
src.listen()

def move(turtle,position):
    turtle.setheading(position)
    
turtle.onkey(lambda: move(snake_body[0],90), "Up")
turtle.onkey(lambda: move(snake_body[0],270), "Down")
turtle.onkey(lambda: move(snake_body[0],180), "Left")
turtle.onkey(lambda: move(snake_body[0],0), "Right")


while not game_over:
    src.update()
    time.sleep(0.1)
    previous_segment_position = None
    for segment in snake_body:
        if segment == snake_body[0]:
            previous_segment_position=segment.pos()
            segment.fd(40)
        else:
            current_pos = segment.pos()
            segment.goto(previous_segment_position)
            previous_segment_position=current_pos

        

src.exitonclick()
