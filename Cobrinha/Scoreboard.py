from turtle import *
ALIGNMENT = "center"
FONT = ("Arial", 21, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.points}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def count(self):
        self.points += 1
        self.clear()
        self.update_score()