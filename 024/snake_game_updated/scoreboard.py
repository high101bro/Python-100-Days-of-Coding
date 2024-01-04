import os.path
from turtle import Turtle
import pickle

ALIGNMENT = "center"
FONT = "Arial"
SIZE = 18
TYPE = 'normal'


class Scoreboard(Turtle):
    def __init__(self, player=1, xcor=0):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(xcor, 270)
        self.score = 0
        if os.path.exists("high-score.pkl"):
            with open("high-score.pkl", "rb") as file:
                self.high_score = pickle.load(file)
        else:
            self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, SIZE, TYPE))
        with open(f"high-score.pkl", "wb") as file:
            pickle.dump(self.high_score, file)

    def increase_score(self, player=1):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            self.write(f"Game Over!\n New High Score!!!", align=ALIGNMENT, font=(FONT, SIZE, TYPE))
        else:
            self.write(f"Game Over!", align=ALIGNMENT, font=(FONT, SIZE, TYPE))
        self.score = 0
        self.update_scoreboard()
