
from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.direction = [
            random.choice(['up', 'down']),
            random.choice(['left', 'right']),
        ]
        self.penup()
        self.ball_x_speed = 3
        self.ball_y_speed = 2

    def move(self):
        if self.direction[0] == 'up' and self.direction[1] == 'right':
            new_x = self.xcor() + self.ball_x_speed
            new_y = self.ycor() + self.ball_y_speed
        elif self.direction[0] == 'up' and self.direction[1] == 'left':
            new_x = self.xcor() - self.ball_x_speed
            new_y = self.ycor() + self.ball_y_speed
        elif self.direction[0] == 'down' and self.direction[1] == 'right':
            new_x = self.xcor() + self.ball_x_speed
            new_y = self.ycor() - self.ball_y_speed
        elif self.direction[0] == 'down' and self.direction[1] == 'left':
            new_x = self.xcor() - self.ball_x_speed
            new_y = self.ycor() - self.ball_y_speed
        self.goto(new_x, new_y)

    def faster(self):
        self.ball_x_speed += 0.25

    def bounce(self):
        if self.direction[0] == 'up' and self.ycor() > 300:
            self.direction[0] = 'down'
            print(self.direction)
        elif self.direction[0] == 'down' and self.ycor() < -300:
            self.direction[0] = 'up'
            print(self.direction)

    def reset(self):
        self.ball_x_speed = 3
        self.ball_y_speed = 3
        self.goto(0, 0)