import turtle
from turtle import Turtle, Screen

pencil = Turtle()

screen = Screen()

def move_forwards():
    pencil.forward(10)
def move_backwards():
    pencil.forward(-10)
def turn_left():
    new_heading = pencil.heading() + 10
    pencil.setheading(new_heading)

def turn_right():
    new_heading = pencil.heading() - 10
    pencil.setheading(new_heading)

def clear():
    pencil.clear()
    pencil.penup()
    pencil.home()
    pencil.pendown()

screen.listen()
# Note: when you pass in a funtion as an argument, you don't include the trigger ()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='space', fun=clear)











screen.exitonclick()

