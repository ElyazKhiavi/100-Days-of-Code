# car_manager.py
# ---------------
# Contains the Car class and CarManager class.
# Car represents a single moving vehicle; CarManager controls all cars.

import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3         # Smaller increment for smoother difficulty
CAR_LENGTH = 4
CAR_WIDTH = 2


def get_random_ycor():
    """Return a random y-coordinate within the road area."""
    return random.randrange(-780, 870, 110)


def get_random_xcor():
    """Return a random x-coordinate for spawning cars."""
    return random.randrange(-850, 950, 100)


class Car(turtle.Turtle):
    """A single car that moves left across the screen."""

    def __init__(self):
        super().__init__()
        self.initialize()
        self.movement_speed = STARTING_MOVE_DISTANCE

    def initialize(self):
        """Set appearance and starting position."""
        self.shape("square")
        self.shapesize(CAR_WIDTH, CAR_LENGTH)   # stretch to rectangle
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(get_random_xcor(), get_random_ycor())
        self.setheading(180)                    # face left

    def move(self):
        """Move the car forward and respawn if it goes off-screen."""
        self.forward(self.movement_speed)
        self.re_spawn()

    def re_spawn(self):
        """If the car exits the left edge, move it back to the right edge."""
        if self.xcor() < -900:
            self.hideturtle()
            self.goto(900, get_random_ycor())
            self.showturtle()

    def detect_collision(self, turtle_obj):
        """Check if the car is close enough to the player."""
        return self.distance(turtle_obj) < 42


class CarManager:
    """Manages a list of cars and their collective speed."""

    def __init__(self):
        self.cars = []

    def create_car(self, amount_of_cars=1):
        """Create a given number of cars and add them to the list."""
        for _ in range(amount_of_cars):
            car = Car()
            self.cars.append(car)

    def increase_car_speed(self):
        """Increase the speed of every car by MOVE_INCREMENT."""
        for car in self.cars:
            car.movement_speed += MOVE_INCREMENT