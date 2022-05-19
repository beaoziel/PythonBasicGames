from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset()

    def reset(self):
        self.goto(0, -280)

    def move(self):
        new_ycor = MOVE_DISTANCE + self.ycor()
        self.goto(0, new_ycor)

    def checkEnd(self):
        if self.ycor() > 240:
            return True
        else:
            return False