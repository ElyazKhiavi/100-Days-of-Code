### Turtle Race Game on turtle?!

from turtle import Turtle, Screen, TK
import turtle as t
import random

# colors = ["red", "orange", "yellow", "green", "blue", "darkblue", "purple"]
turtles = {
    "red": {"x": -950, "y": -435},
    "orange": {"x": -950, "y": -290},
    "yellow": {"x": -950, "y": -145},
    "green": {"x": -950, "y": 0},
    "blue": {"x": -950, "y": 145},
    "darkblue": {"x": -950, "y": 290},
    "purple": {"x": -950, "y": 435},
}

scr = Screen()
scr.setup(height=1200, width=2000)
t.bgcolor("lavender")


def create_turtle(color, x, y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(4)
    new_turtle.color(color)
    new_turtle.up()
    new_turtle.goto(x=x, y=y)
    return new_turtle


def assign_turtles():
    race_turtles = {}
    for turtle in turtles:
        new_turtle = create_turtle(
            color=turtle, x=turtles[turtle]["x"], y=turtles[turtle]["y"]
        )
        race_turtles[f"{turtle}"] = new_turtle
    return race_turtles


def prompt_guess():
    while True:
        guess = scr.textinput(title="Turtle Race Game", prompt="Who will win?")
        if guess not in turtles:
            TK.messagebox.showinfo(
                title="The Turtle says:",
                message='You must choose one of: "red", "orange", "yellow", "green", "blue", "darkblue", "purple" colors.',
            )
            continue
        return guess.strip().lower()


def start_race(race_turtles):
    guess = prompt_guess()
    race_over = False
    winner = None
    while not race_over:
        for turtle in race_turtles:
            race_turtles[turtle].fd(random.randint(1, 50))
            if race_turtles[turtle].pos()[0] >= 1000:
                race_over = True
                winner = turtle
                return winner, guess


def main():
    winner, guess = start_race(assign_turtles())
    print(f"{winner.capitalize()} won the race.")
    print(f"You chose {guess.capitalize()}.")
    if winner == guess:
        print("You WON.")
    else:
        print("You Lost!")


if __name__ == "__main__":
    main()


scr.exitonclick()
