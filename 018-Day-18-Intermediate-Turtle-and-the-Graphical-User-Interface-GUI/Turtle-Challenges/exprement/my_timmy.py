from turtle import Turtle, Screen

little_timmy = Turtle()

little_timmy.screen.title("Day 18 - Turtle Demo")
little_timmy.screen.bgcolor("DarkSlateGray4")
little_timmy.shapesize(2, 2)
little_timmy.shape("triangle")
little_timmy.color("DarkOrchid4")


def rec(num, size):
    for i in range(num):    
        size += 25
        little_timmy.forward(size)
        little_timmy.right(90)

rec(100,50)

my_screen = Screen()
my_screen.exitonclick()
