import turtle
import time
from divider import Divider
from paddles import Paddle
from the_ball import TheBall
from scoreboard import Scoreboard

SCREEN_HEIGHT = 1800
SCREEN_WIDTH = 3000


def main():
    screen = turtle.Screen()
    screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
    screen.title("The Pong Game")
    screen.bgcolor("black")

    screen.tracer(0)

    divider = Divider()
    r_paddle = Paddle()
    l_paddle = Paddle(other_side=True)
    the_ball = TheBall()
    r_scoreboard = Scoreboard()
    l_scoreboard = Scoreboard(left=True)

    screen.listen()
    screen.onkey(fun=r_paddle.move_up, key="Up")
    screen.onkey(fun=r_paddle.move_down, key="Down")
    screen.onkey(fun=l_paddle.move_up, key="p")
    screen.onkey(fun=l_paddle.move_down, key="u")

    game_over = False
    right_side_score = 0
    left_side_score = 0

    while not game_over:

        match_over = False
        the_ball.home()
        while not match_over:
            time.sleep(0.01)
            screen.update()
            the_ball.move()

            if the_ball.hit_right_line():
                match_over = True
                left_side_score += 1
                l_scoreboard.update_score(left_side_score)
                break
            elif the_ball.hit_left_line():
                match_over = True
                right_side_score += 1
                r_scoreboard.update_score(right_side_score)
                break

            the_ball.check_top_bottom_collision()
            the_ball.check_paddle_collision(r_paddle, l_paddle)

        if right_side_score == 3:
            r_scoreboard.game_over()
            game_over = True
        elif left_side_score == 3:
            l_scoreboard.game_over()
            game_over = True

        time.sleep(0.7)

    screen.mainloop()


if __name__ == "__main__":
    main()
