

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

# Changing the initial speed for the turtle racers to normal
speed = 1
speed_low = 1
speed_high = 5

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
    track.speed(1)
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
    turtle_racer.speed(speed)
    turtle_racer.shape('turtle')
    turtle_racer.penup()
    turtle_racer.first = 0
    turtle_racer.second = 0
    turtle_racer.third = 0
    turtle_racer.fourth = 0
    turtle_racer.fifth = 0
    turtle_racer.sixth = 0
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
track.speed(0)
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

score = turtle.Turtle()
score.speed('fastest')
score.hideturtle()
score.penup()
score.setheading(south)
score.forward(150)
score.write("Place your bets on the pet with the fastest scute scooter.", align="center", font=("Arial", 16, "normal"))
score.setheading(west)
score.forward(10)


def toggle_speed():
    global speed
    global speed_low
    global speed_high

    if speed == 0:
        speed = 1
        speed_low = 1
        speed_high = 5
        score.write("Speed Mode == Normal", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)
        score.clear()

    elif speed == 1:
        speed = 0
        speed_low = 10
        speed_high = 50
        score.write("Speed Mode == Fast", align="center", font=("Arial", 16, "normal"))
        time.sleep(1)
        score.clear()

    try:
        for tr in turtle_racer:
            tr.speed(speed)
    except:
        for tr in turtle_ranking:
            tr.speed(speed)


continuous_race = False
def continuous():
    global continuous_race
    if continuous_race == False:
        continuous_race = True
        score.setheading(south)
        score.forward(50)
        score.write("Continuous Mode == True", align="center", font=("Arial", 16, "normal"))
        score.setheading(north)
        score.forward(50)
        time.sleep(1)
        score.clear()
        start_race(racing=True,again=True)
    elif continuous_race == True:
        continuous_race = False
        score.setheading(south)
        score.forward(50)
        score.write("Continuous Mode == False", align="center", font=("Arial", 16, "normal"))
        score.setheading(north)
        score.forward(50)
        time.sleep(1)
        score.clear()
        start_race(racing=True,again=False)


def start_race(racing=True,again=False):
       
    pencil.clear()
    # score.clear()
    global starting_position
    starting_position = 0

    global turtle_ranking
    if len(turtle_ranking) == 0:
        for tr in turtle_racers:
            tr.home()
    else:
        score.clear()
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

    score.clear()
    # score.write("Place your bets on the pet with the fastest scute scooter.", align="center", font=("Arial", 16, "normal"))


    print_scores = ""
    
    while racing:
        # print(len(turtle_racers))
        if len(turtle_racers) > 0:
            for tr in turtle_racers:
                tr.speed(speed)
                move = random.randint(speed_low, speed_high)
                tr.forward(move)
                pencil.clear()
                # print(tr.xcor())
                if tr.xcor() >= 310:
                    # print(tr.color())
                    # print(tr.xcor())
                    turtle_racers.remove(tr)
                    turtle_ranking.append(tr)
                    if len(turtle_ranking) == 1:
                        print_scores += "1st Place: "
                        tr.first += 1
                    elif len(turtle_ranking) == 2:
                        print_scores += "2nd Place: "
                        tr.second += 1
                    elif len(turtle_ranking) == 3:
                        print_scores += "3rd Place: "
                        tr.third += 1
                    elif len(turtle_ranking) == 4:
                        print_scores += "4th Place: "
                        tr.fourth += 1
                    elif len(turtle_ranking) == 5:
                        print_scores += "5th Place: "
                        tr.fifth += 1
                    elif len(turtle_ranking) == 6:
                        print_scores += "6th Place: "
                        tr.sixth += 1
                    index = len(turtle_ranking)-1
                    string = f"{turtle_ranking[index].first}|{turtle_ranking[index].second}|{turtle_ranking[index].third}|{turtle_ranking[index].fourth}|{turtle_ranking[index].fifth}|{turtle_ranking[index].sixth}"
                    # print(string)
                    print_scores += string
                    print_scores += "\n"

        else:
            racing = False

    pencil.clear()
    pencil.write(f"What a close race...", align="center", font=("Arial", 16, "normal"))
    time.sleep(1)

    ranking_position = 10
    for tr in turtle_ranking:
        ycor = tr.ycor()
        tr.goto(350,ycor)
        xcor = tr.xcor()
        tr.setheading(south)
        tr.goto(xcor, 0)
        # tr.forward(10)

        xcor = tr.xcor()
        ycor = tr.ycor()
        tr.goto(xcor, ycor + ranking_position)

        tr.setheading(west)
        tr.forward(195)
        ranking_position -= 25

    pencil.clear()
    score.clear()
    score.write(print_scores, align="center", font=("Courier New", 16, "normal"))
    time.sleep(3)

    global continuous_race
    if continuous_race == True:
        if again == True:
            start_race(racing=True,again=True)
    elif continuous_race == False:
        return



screen = turtle.Screen()
screen.listen()
screen.title("The Turtle Races")
screen.onkey(start_race, 'space')
screen.onkey(continuous, 'c')
screen.onkey(toggle_speed, 's')

# screen.exitonclick()
turtle.done()

