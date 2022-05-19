from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.write(f"Fase: {self.score}", align="center", font=("Arial", 15, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def end(self):
        self.clear()
        self.color("black")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"FIM DE JOGO", align="center", font=("Arial", 15, "bold"))