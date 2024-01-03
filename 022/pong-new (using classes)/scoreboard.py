from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-300, 200)
        self.write(self.score_left, align="center", font=("Courier", 80, "normal"))
        self.goto(300, 200)
        self.write(self.score_right, align="center", font=("Courier", 80, "normal"))

    def left_scores(self):
        self.score_left += 1
        self.update()

    def right_scores(self):
        self.score_right += 1
        self.update()
