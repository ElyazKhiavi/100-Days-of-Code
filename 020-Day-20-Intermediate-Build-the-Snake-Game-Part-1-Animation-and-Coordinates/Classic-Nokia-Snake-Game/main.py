import turtle
import time
import snake

screen = turtle.Screen()
screen.setup(width=1750, height=1750)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)

snake = snake.Snake()

print(snake)

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
