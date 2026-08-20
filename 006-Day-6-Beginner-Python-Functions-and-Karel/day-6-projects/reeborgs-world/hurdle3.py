from site_modules import turn_left
from site_modules import move
from site_modules import at_goal
from site_modules import front_is_clear
from site_modules import wall_in_front

def go():
    def turn_right():
        turn_left()
        turn_left()
        turn_left()


    def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()


    while not at_goal():
        if front_is_clear() and not at_goal():
            move()
        if wall_in_front() and not at_goal():
            jump()
go()