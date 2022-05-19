import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []
def generateCars():
    for i in range(0,3):
        car = str(i)
        car = CarManager()
        cars.append(car)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Atravesse a tartaruga!")

score = Scoreboard()
turtle = Player()
screen.onkey(turtle.move, "Up")

game_is_on = True
count = 0
speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()

    if count%6 == 0:
        generateCars()

    for car in cars:
        car.moving()
        if turtle.distance(car) < 30:
            score.end()
            game_is_on = False

    #Fase
    if turtle.checkEnd() == True:
        turtle.reset()
        score.update_score()
        if speed == 0.00:
            speed = 0.00
        else:
            speed -= 0.01

    count += 1

screen.exitonclick()