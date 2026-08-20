from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue4")
tim.shapesize(15, 15)
tim.screen.bgcolor("ForestGreen")
tim.screen.title("Object-oriented turtle demo")


for i in range(2):
    tim.forward(750)
    tim.right(90)

number = 1500
while number:
    tim.forward(number)
    tim.right(90)
    number -=5
    

my_screen = Screen()
my_screen.exitonclick()

print(tim)
