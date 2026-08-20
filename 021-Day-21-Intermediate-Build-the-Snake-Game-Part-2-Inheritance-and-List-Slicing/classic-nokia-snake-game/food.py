import turtle
import random

RANGE = 40
NUMBER = 820
FOOD_SIZE = 1.5


def generate_random_coordinate():
    while True:
        generated_number = random.randint(-NUMBER, NUMBER)
        if generated_number % RANGE != 0:
            continue
        return generated_number


class Food(turtle.Turtle):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.shape("circle")
        self.shapesize(FOOD_SIZE)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.move_food()
        self.blinking = True
        self.blink_interval = 1000
        self.blink()

    def blink(self):
        if not self.blinking:
            return  # stop when blinking flag is turned off

        if self.isvisible():
            self.hideturtle()
            self.screen.ontimer(self.blink, self.blink_interval // 4)
        else:
            self.showturtle()
            self.screen.ontimer(self.blink, self.blink_interval)

    def move_food(self):
        self.goto(generate_random_coordinate(),generate_random_coordinate())
