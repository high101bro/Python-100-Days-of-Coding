

import turtle as t
import random

pencil = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color = (r, g, b)
    return color


pencil.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pencil.color(random_color())
        pencil.circle(100)
        pencil.setheading(pencil.heading() +10)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()