from site_modules import turn_left
from site_modules import move
from site_modules import at_goal
from site_modules import front_is_clear
from site_modules import right_is_clear
from site_modules import wall_in_front
from site_modules import wall_on_right


def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not wall_on_right():
    turn_left()
    if front_is_clear():
        move()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()