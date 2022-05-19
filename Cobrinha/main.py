from turtle import Screen
from Snake import Snake
from Food import *
from Scoreboard import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.count()
    #wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #tail
    for piece in snake.body[1:]:
        if snake.head.distance(piece) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()