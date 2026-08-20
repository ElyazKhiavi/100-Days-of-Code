import turtle
import time
from divider import Divider
from paddles import Paddle
from the_ball import TheBall
from scoreboard import Scoreboard

# Screen dimensions
SCREEN_HEIGHT = 1800
SCREEN_WIDTH = 3000

# Winning score
WINNING_SCORE = 3


def main():
    """Set up the screen, create game objects, and run the main loop."""
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("The Pong Game")
    screen.bgcolor("black")
    screen.tracer(0)  # manual screen updates for smooth animation

    # Create game objects
    divider = Divider(screen_height=SCREEN_HEIGHT)
    r_paddle = Paddle()
    l_paddle = Paddle(other_side=True)
    the_ball = TheBall()
    r_scoreboard = Scoreboard()
    l_scoreboard = Scoreboard(left=True)

    # Key bindings (Dvorak-friendly for left paddle)
    screen.listen()
    screen.onkey(fun=r_paddle.move_up, key="Up")
    screen.onkey(fun=r_paddle.move_down, key="Down")
    screen.onkey(fun=l_paddle.move_up, key="p")
    screen.onkey(fun=l_paddle.move_down, key="u")

    # Score tracking
    right_side_score = 0
    left_side_score = 0
    game_over = False

    while not game_over:
        # Reset ball for a new point
        the_ball.reset_position()
        match_over = False

        while not match_over:
            time.sleep(0.01)
            screen.update()  # refresh the screen each frame

            the_ball.move()

            # Check if ball went out of bounds
            if the_ball.hit_right_line():
                left_side_score += 1
                l_scoreboard.update_score(left_side_score)
                screen.update()  # immediately show new score
                match_over = True
                break
            elif the_ball.hit_left_line():
                right_side_score += 1
                r_scoreboard.update_score(right_side_score)
                screen.update()
                match_over = True
                break

            # Bounce off top/bottom and paddles
            the_ball.check_top_bottom_collision()
            the_ball.check_paddle_collision(r_paddle, l_paddle)

        # Check if someone won the game
        if right_side_score == WINNING_SCORE:
            r_scoreboard.game_over()
            screen.update()
            game_over = True
        elif left_side_score == WINNING_SCORE:
            l_scoreboard.game_over()
            screen.update()
            game_over = True

        time.sleep(0.7)  # pause before next point or end

    # Keep window open until user closes it
    screen.mainloop()


if __name__ == "__main__":
    main()
