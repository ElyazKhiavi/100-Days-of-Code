import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3
CAR_LENGTH = 4
CAR_WIDTH = 2


def get_random_ycor():
        return random.randrange(-780,870,110)
def get_random_xcor():
        return random.randrange(-850,950,100)

class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()
        self.movement_speed = STARTING_MOVE_DISTANCE

    def initialize(self):
        self.shape("square")
        self.shapesize(CAR_WIDTH, CAR_LENGTH)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto((get_random_xcor(),get_random_ycor()))
        self.setheading(180)

    def move(self):
        self.forward(self.movement_speed)
        self.re_spawn()

    def re_spawn(self): # if it goes out the screen
        current_x = self.xcor()
        if current_x < -900:
            self.hideturtle()
            self.goto((900,get_random_ycor()))
            self.showturtle()
    
    def detect_collision(self,turtle):
        if self.distance(turtle) < 45:
            return True

class CarManager():
    def __init__(self):
        self.cars = []
    def create_car(self,amount_of_cars=1):
        for _ in range(amount_of_cars):
            car = Car()
            self.cars.append(car)
    def increase_car_speed(self):
        for car in self.cars:
            car.movement_speed += MOVE_INCREMENT
    