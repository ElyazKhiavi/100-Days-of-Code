import turtle
import time
import snake
import food
import scoreboard

GAME_SIZE = 1800
WALLS = 880

screen = turtle.Screen()
screen.setup(width=GAME_SIZE, height=GAME_SIZE)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food(screen)
scoreboard = scoreboard.Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_over = False
while not game_over:
    snake.move()
    screen.update()
    time.sleep(0.08)

    # detect collision with food
    if snake.head.distance(food) <= 20:
        food.move_food()
        snake.extend_snake()
        scoreboard.update_score()

    # detect collision with food
    if (
        snake.head.xcor() > WALLS
        or snake.head.xcor() < -WALLS
        or snake.head.ycor() > WALLS
        or snake.head.ycor() < -WALLS
    ):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 20:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
