# main.py
# --------
# Entry point for the Turtle Crossing game.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finish_line import FinishLine


def main():
    screen = Screen()
    screen.setup(width=1800, height=1800)
    screen.bgcolor("lavender")
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    car_manager.create_car(50)        # Number of cars on screen
    finish = FinishLine()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.move, "Up")

    game_is_on = True
    level = 0

    while game_is_on:
        time.sleep(0.05)
        screen.update()

        # Move each car and check collision with player
        for car in car_manager.cars:
            car.move()
            if car.detect_collision(player):
                game_is_on = False
                scoreboard.game_over()

        # Check if player reached the finish line
        if player.check_win():
            level += 1
            scoreboard.update_level(level)
            time.sleep(0.5)           # Pause before resetting
            player.return_to_start()
            car_manager.increase_car_speed()

    screen.exitonclick()


if __name__ == "__main__":
    main()