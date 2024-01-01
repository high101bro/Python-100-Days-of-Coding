
from turtle import Turtle

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
        self.write(f"Player {player} Score: {self.score}", align=ALIGNMENT, font=(FONT, SIZE, TYPE))

    def increase_score(self, player=1):
        self.score += 1
        self.clear()
        self.write(f"Player {player} Score: {self.score}", align=ALIGNMENT, font=(FONT, SIZE, TYPE))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=(FONT, SIZE, TYPE))
