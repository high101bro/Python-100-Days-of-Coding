

import turtle
import random
import time

number_of_turtles = 6
turtle_racers = []
turtle_ranking = []

north = 90
east = 0
south = 270
west = 180

lane_increment = 50
lane_increment_tracker = 0



colors = ["red", "orange", "gold", "green", "blue", "purple", "brown", "gray", "cyan", "pink"]


pencil = turtle.Turtle()
pencil.speed('fastest')
pencil.hideturtle()
pencil.penup()
pencil.setheading(south)
pencil.forward(75)
pencil.write("Welcome to Turtle Racing!", align="center", font=("Arial", 16, "normal"))
time.sleep(2)

starting_position = 0

pencil.clear()
pencil.write(f"Looks like there are {number_of_turtles} in the competition.", align="center", font=("Arial", 16, "normal"))


def create_track_lane(tr):
    # Draw Turtle Lanes
    for index, t in enumerate(tr):
        pencil.clear()
        pencil.write(f"Drawing lane {index +1}...", align="center", font=("Arial", 16, "normal"))
        if index == 0:
            inc = 50
        else:
            inc = 100
        track.pendown()
        track.setheading(north)
        track.forward(inc)
        track.setheading(east)
        track.forward(800)
        track.setheading(south)
        track.forward(50)
        track.setheading(west)
        track.forward(800)

    pencil.clear()
    pencil.write(f"Drawing the starting line...", align="center", font=("Arial", 16, "normal"))

    # Draw start line
    track.setheading(north)
    track.forward(50)
    pencil.clear()
    pencil.write(f"Oops... can't forget the finish line.", align="center", font=("Arial", 16, "normal"))
    track.setheading(east)
    track.forward(50)
    track.setheading(south)
    track.forward(50*len(tr))

    # Draw finish line
    track.setheading(east)
    track.forward(700)
    pencil.clear()
    pencil.write(f"Drawing the finish line...", align="center", font=("Arial", 16, "normal"))
    track.setheading(north)
    track.forward(50*len(tr))

    track.penup()
    track.forward(25)
    track.setheading(south)


# Creates the turtle racers
for _ in range(number_of_turtles):
    turtle_racer = turtle.Turtle()
    # turtle_racer.speed(0)
    turtle_racer.shape('turtle')
    turtle_racer.penup()
    color_choice = random.choice(colors)
    colors.remove(color_choice)
    turtle_racer.color(color_choice)
    turtle_racers.append(turtle_racer)

def go_to_starting_location(turtle_racer):
    turtle_racer.setheading(180)
    turtle_racer.forward(405)
    turtle_racer.setheading(90)
    global starting_position
    starting_position += lane_increment
    turtle_racer.forward(starting_position)
    turtle_racer.setheading(0)
    turtle_racer.forward(20)





track = turtle.Turtle()
track.shape('turtle')
track.color('black')
track.penup()
track.setheading(west)
track.forward(425)
track.setheading(north)
track.forward(25)

pencil.clear()
pencil.write(f"Please be patient as we setup the track.", align="center", font=("Arial", 16, "normal"))


create_track_lane(turtle_racers)

pencil.clear()
pencil.write(f"Turtles, please proceed to the start line...", align="center", font=("Arial", 16, "normal"))



def start_race():
    pencil.clear()
    global starting_position
    starting_position = 0

    global turtle_ranking
    if len(turtle_ranking) == 0:
        for tr in turtle_racers:
            tr.home()
    else:
        pencil.clear()
        pencil.write(f"Time to celebrate", align="center", font=("Arial", 16, "normal"))

        for tr in turtle_ranking:
            turtle_racers.append(tr)
            tr.home()
        turtle_ranking = []


    # the turtle racers go to the start position
    for turtle_racer in turtle_racers:
        go_to_starting_location(turtle_racer)

    pencil.clear()
    pencil.write(f"Press the space bar to start the race!", align="center", font=("Arial", 16, "normal"))

    pencil.clear()
    pencil.write(f"3...", align="center", font=("Arial", 16, "normal"))
    time.sleep(1)

    pencil.clear()
    pencil.write(f"2...", align="center", font=("Arial", 16, "normal"))
    time.sleep(1)

    pencil.clear()
    pencil.write(f"1...", align="center", font=("Arial", 16, "normal"))
    time.sleep(1)

    pencil.clear()
    pencil.write(f"GO!!! Scoot those scutes!!!", align="center", font=("Arial", 16, "normal"))


    racing = True
    while racing:
        # print(len(turtle_racers))
        if len(turtle_racers) > 0:
            for tr in turtle_racers:
                move = random.randint(1, 5)
                tr.forward(move)
                pencil.clear()
                # print(tr.xcor())
                if tr.xcor() >= 310:
                    xcor = tr.xcor()
                    ycor = tr.ycor()
                    tr.goto(340,ycor)
                    turtle_racers.remove(tr)
                    turtle_ranking.append(tr)
        else:
            racing = False

    pencil.clear()
    pencil.write(f"What a close race...", align="center", font=("Arial", 16, "normal"))
    time.sleep(1)

    ranking_position = 10
    for tr in turtle_ranking:
        xcor = tr.xcor()
        tr.goto(xcor, 0)
        tr.forward(10)
        tr.setheading(south)

        xcor = tr.xcor()
        ycor = tr.ycor()
        tr.goto(xcor, ycor + ranking_position)

        tr.setheading(west)
        tr.forward(200)
        ranking_position -= 25


    pencil.clear()
    pencil.write(f"""
1st place is the {turtle_ranking[0].color()[0]} turtle
2nd place is the {turtle_ranking[1].color()[0]} turtle
3rd place is the {turtle_ranking[2].color()[0]} turtle
""", align="center", font=("Arial", 16, "normal"))


screen = turtle.Screen()
screen.listen()
screen.onkey(start_race, 'space')

# screen.exitonclick()
turtle.done()

