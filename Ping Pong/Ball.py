from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10


    def move(self):
        #increase on the x and y
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #Do the inverse
        self.y_move *= -1

    def bounce_x(self):
        # Do the inverse
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()