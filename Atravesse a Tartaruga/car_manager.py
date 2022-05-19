from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
DISTANCES = [220, 130, 40, -50, -130, -220]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.goto(260, random.choice(DISTANCES))

    def moving(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())

