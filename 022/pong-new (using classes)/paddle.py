

from turtle import Turtle
import random
import time

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__() # Inherit Turtle class
        self.penup()
        self.shape("square")
        self.color("white")
        self.stretch_wid = 5
        self.stretch_len = 1
        self.direction = 'stop'
        self.shapesize(stretch_wid=self.stretch_wid, stretch_len=self.stretch_len)
        self.goto(coordinates)
        self.protection = False

    def move(self):
        if self.direction == 'up':
            if self.ycor() >= 300:
                self.direction = 'stop'
            else:
                new_y = self.ycor() + 5
                self.goto(self.xcor(), new_y)
        elif self.direction == 'down':
            if self.ycor() <= -300:
                self.direction = 'stop'
            else:
                new_y = self.ycor() - 5
                self.goto(self.xcor(), new_y)
        elif self.direction == 'stop':
            pass

    def go_up(self):
        self.direction = 'up'

    def go_down(self):
        self.direction = 'down'

    def stop(self):
        self.direction = 'stop'

    def move_obstacle(self):
        time.sleep(0.01)
        if self.direction == 'stop':
            random_direction = random.choice(['up', 'down'])
            self.direction = random_direction
        elif self.direction == 'up' and self.ycor() < 300:
            new_y = self.ycor() + 5
            self.goto(self.xcor(), new_y)
        elif self.direction == 'up' and self.ycor() >= 300:
            self.direction = 'down'
            new_y = self.ycor() - 5
            self.goto(self.xcor(), new_y)
        elif self.direction == 'down' and self.ycor() > -300:
            new_y = self.ycor() - 5
            self.goto(self.xcor(), new_y)
        elif self.direction == 'down' and self.ycor() <= -300:
            self.direction = 'up'
            new_y = self.ycor() + 5
            self.goto(self.xcor(), new_y)
