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
score = 0
while not game_over:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) <= 20:
        score += 1
        food.move_food()
        
        snake.extend_snake()

        scoreboard.update_score(score)

    # detect collision with food
    if snake.head.xcor() > WALLS or snake.head.xcor() < -WALLS  or snake.head.ycor() > WALLS or snake.head.ycor() < -WALLS:
        game_over = True
        scoreboard.game_over()

    # detect collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 20:
            game_over =  True
            scoreboard.game_over()

screen.exitonclick()
