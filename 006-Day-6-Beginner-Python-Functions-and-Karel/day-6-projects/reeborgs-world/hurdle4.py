from site_modules import turn_left
from site_modules import move
from site_modules import at_goal
from site_modules import front_is_clear
from site_modules import wall_in_front
from site_modules import wall_on_right


def go():
    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    def jump():
        up = 0
        turn_left()
        while front_is_clear() and wall_on_right():
            move()
            up += 1
        turn_right()
        move()
        turn_right()
        for i in range(
            up
        ):  # <== here you could have just used while front is clear move , but both are same (this version is has 2 move lines!)
            move()
        turn_left()

    while not at_goal():
        if front_is_clear():
            move()
        if wall_in_front():
            jump()


go()
