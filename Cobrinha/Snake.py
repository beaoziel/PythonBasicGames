from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]  # Posições iniciais
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
distance = 20

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)


    def add_segment(self,position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(position)
        self.body.append(s)


    def extend(self):
        #last item in our list -1
        self.add_segment(self.body[-1].position())

    def move(self):
        for body_part in range(len(self.body) - 1, 0, -1):  # start, stop, step.
            # Ex:  3, 20, 2 - 3 a 20 will plus 2
            newx = self.body[body_part - 1].xcor()
            newy = self.body[body_part - 1].ycor()
            self.body[body_part].goto(newx, newy)
        self.body[0].forward(distance)

        #criar up, down, left, right
    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(270)


    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(180)


    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(0)
