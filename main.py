from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

game_is_on = True
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="d", fun=snake.turn_right)


while game_is_on:
    screen.update()
    score.refresh()
    snake.move_forward()
    time.sleep(0.05)
    extender = 0

    if snake.snake_head().distance(food) < 15:
        food.refresh()
        score.score_plus()
        extender = 1
        snake.extend()

    if snake.snake_head().xcor() > 290 or snake.snake_head().ycor() > 290 or snake.snake_head().xcor() < -290 or \
            snake.snake_head().ycor() < -290:
        score.game_over()
        game_is_on = False

    for cell in snake.snake_lenght:
        if cell == snake.snake_head() or extender == 1:
            pass
        elif snake.snake_head().distance(cell) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
