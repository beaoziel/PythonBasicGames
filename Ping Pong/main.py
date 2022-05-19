from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

screen.listen()

p_left = Paddle(xcor= -350)
p_right = Paddle(xcor= 350)
ball = Ball()
scoreb = Scoreboard()

screen.onkey(p_right.go_up, "Up")
screen.onkey(p_right.go_down, "Down")

screen.onkey(p_left.go_up, "w")
screen.onkey(p_left.go_down, "s")

game_is_on = True
speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

    if ball.distance(p_right) < 50 and ball.xcor() > 320 or ball.distance(p_left) < 50 and ball.xcor() < -320:
      ball.bounce_x()
      if speed == 0.00:
          speed = 0.00
      else:
          speed -= 0.01


    if ball.xcor() > 380:
        ball.reset_position()
        scoreb.point_l()
        speed = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreb.point_r()
        speed = 0.1

screen.exitonclick()