import turtle
from turtle import Turtle, Screen
from helper import *
import random
import time
import threading, queue
import os
from PIL import Image
import copy

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
x_positions = list(range(-500, 500, 20))
y_positions = list(range(-300, 300, 20))

initial_food = 10

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()

game = Game()
game.food_queue = queue.Queue()
game.vehicle_queue = queue.Queue()


# The House
def house():
    new_width = 100
    new_height = 100

    original_house_image = Image.open(r".\images\house.gif")
    stretched_image = original_house_image.resize((new_width, new_height))
    stretched_image.save(r".\images\house-resized.gif", format="GIF")

    house_img = r".\images\house-resized.gif"
    the_house = Turtle()
    the_house.penup()
    screen.addshape(house_img)
    the_house.shape(house_img)
    the_house.shapesize(stretch_wid=-5, stretch_len=5)
    the_house.goto(-30, 300)

house()



# The Road
def road():
    new_width = SCREEN_WIDTH
    new_height = 250

    original_road_image = Image.open(r".\images\road.gif")
    stretched_image = original_road_image.resize((new_width, new_height))
    stretched_image.save(r".\images\road-resized.gif", format="GIF")

    road_img = r".\images\road-resized.gif"
    road = Turtle()
    screen.addshape(road_img)
    road.shape(road_img)
    road.shapesize(stretch_wid=-5, stretch_len=5)
    road.goto(0, 0)


road()


def blood_splater():
    new_width = 120
    new_height = 40

    original_road_image = Image.open(r".\images\blood-splatter.gif")
    stretched_image = original_road_image.resize((new_width, new_height))
    resized_image = r".\images\blood-splatter-resized.gif"
    stretched_image.save(resized_image, format="GIF")
    return resized_image


splat_img = blood_splater()
screen.addshape(splat_img)

vehicles_driving_left = []
vehicles_driving_right = []
pets = []

player_1 = Pet(
    color='pink',
    xcor=random.choice(x_positions),
    y_cor=random.choice(y_positions),
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
)

player_2 = Pet(
    color='blue',
    xcor=random.choice(x_positions),
    y_cor=random.choice(y_positions),
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
)

# Create Initial Food
for _ in range(initial_food):
    food = Food()
    food.spawn(
        xcor=random.choice(x_positions),
        y_cor=random.choice(y_positions),
    )
    game.food_list.append(food)


def randomly_spawn_food(food_queue):
    while True:
        wait_time = random.randint(15, 30)
        time.sleep(wait_time)
        food_queue.put("spawn")


spawn_thread_food = threading.Thread(target=randomly_spawn_food, args=(game.food_queue,))
spawn_thread_food.daemon = True  # Daemon thread exits when main program exits
spawn_thread_food.start()


def randomly_spawn_vehicle(vehicles_driving_left_queue):
    while True:
        wait_time = random.randint(8, 40)  # divided by 10 later to give 10ths of a second
        time.sleep(wait_time/10)
        vehicles_driving_left_queue.put("spawn")


spawn_thread_vehicle = threading.Thread(target=randomly_spawn_vehicle, args=(game.vehicles_driving_left_queue,))
spawn_thread_vehicle.daemon = True  # Daemon thread exits when main program exits
spawn_thread_vehicle.start()


def randomly_spawn_vehicle(vehicles_driving_right_queue):
    while True:
        wait_time = random.randint(8, 40)  # divided by 10 later to give 10ths of a second
        time.sleep(wait_time/10)
        vehicles_driving_right_queue.put("spawn")


spawn_thread_vehicle = threading.Thread(target=randomly_spawn_vehicle, args=(game.vehicles_driving_right_queue,))
spawn_thread_vehicle.daemon = True  # Daemon thread exits when main program exits
spawn_thread_vehicle.start()

# Create Pet Friends
# pet_colors = ['green', 'purple', 'orange', 'gold', 'red', 'black', 'gray', 'brown',]
pet_colors = ['green', 'purple', 'orange', 'gold', 'red', 'black', 'gray', 'brown',
              'green', 'purple', 'orange', 'gold', 'red', 'black', 'gray', 'brown',
              'green', 'purple', 'orange', 'gold', 'red', 'black', 'gray', 'brown',
              'green', 'purple', 'orange', 'gold', 'red', 'black', 'gray', 'brown',
              'green', 'purple', 'orange', 'gold', 'red', 'black', 'gray', 'brown',
              'green', 'purple', 'orange', 'gold', 'red', 'black', 'gray', 'brown']
# pet_colors = ['blue']
for color in pet_colors:
    pet = Pet(
        color=color,
        xcor=random.choice(x_positions),
        y_cor=random.choice(y_positions),
        screen_width=SCREEN_WIDTH,
        screen_height=SCREEN_HEIGHT,
    )
    pets.append(pet)


def player_1_eat():
    player_1.eat_food(game, scoreboard)


def player_1_poop():
    player_1.poop(game)


def player_2_eat():
    player_2.eat_food(game, scoreboard)


def player_2_poop():
    player_2.poop(game)


image_dir_left = r".\images\driving_left"
for file in os.listdir(image_dir_left):
    if file.endswith(".gif"):
        image_path = os.path.join(image_dir_left, file)
        screen.addshape(image_path)
        vehicles_driving_left.append(image_path)

for file in vehicles_driving_left:
    vehicle = Vehicle()
    vehicle.spawn(
        file=file,
        xcor=((SCREEN_WIDTH + 300) / 2),
        ycor=35,
        direction='left',
    )
    game.vehicles_driving_left_list.append(vehicle)


image_dir_right = r".\images\driving_right"
for file in os.listdir(image_dir_right):
    if file.endswith(".gif"):
        image_path = os.path.join(image_dir_right, file)
        screen.addshape(image_path)
        vehicles_driving_right.append(image_path)

for file in vehicles_driving_right:
    vehicle = Vehicle()
    vehicle.spawn(
        file=file,
        xcor=-((SCREEN_WIDTH + 300) / 2),
        ycor=-26,
        direction='right',
    )
    game.vehicles_driving_right_list.append(vehicle)


# User controls
screen.onkeypress(player_1.move_up, "Up")
screen.onkeypress(player_1.move_down, "Down")
screen.onkeypress(player_1.move_left, "Left")
screen.onkeypress(player_1.move_right, "Right")
screen.onkeypress(player_1_eat, "Shift_R")
screen.onkeypress(player_1_poop, "Return")
screen.onkeypress(player_2.move_up, "w")
screen.onkeypress(player_2.move_down, "s")
screen.onkeypress(player_2.move_left, "a")
screen.onkeypress(player_2.move_right, "d")
screen.onkeypress(player_2_eat, "e")
screen.onkeypress(player_2_poop, "q")

# The running game
while True:
    screen.update()

    # Check if there's anything in the queue
    while not game.food_queue.empty():
        command = game.food_queue.get()
        if command == "spawn":
            # Spawn food in the main thread
            food = Food()
            food.spawn(
                xcor=random.choice(x_positions),
                y_cor=random.choice(y_positions),
            )
            game.food_list.append(food)

    # Check if there's anything in the queue for vehicles driving left
    while not game.vehicles_driving_left_queue.empty():
        command = game.vehicles_driving_left_queue.get()
        if command == "spawn":
            def attempt_spawn_reset():
                vehicle = random.choice(game.vehicles_driving_left_list)
                if vehicle.moving:
                    attempt_spawn_reset()
                elif not vehicle.moving:
                    vehicle.reset(direction='left', screen_width=SCREEN_WIDTH)
                    vehicle.moving = True
            attempt_spawn_reset()

    # Check if there's anything in the queue for vehicles driving right
    while not game.vehicles_driving_right_queue.empty():
        command = game.vehicles_driving_right_queue.get()
        if command == "spawn":
            def attempt_spawn_reset():
                vehicle = random.choice(game.vehicles_driving_right_list)
                if vehicle.moving:
                    attempt_spawn_reset()
                elif not vehicle.moving:
                    vehicle.reset(direction='right', screen_width=SCREEN_WIDTH)
                    vehicle.moving = True
            attempt_spawn_reset()

    for vehicle in game.vehicles_driving_left_list:
        if vehicle.moving:
            vehicle.drive()
        if vehicle.distance(player_1) < 25:
            print('Squish!!!')
            scoreboard.turtle_squishes += 1
            splat = Splat(pet=player_1, file=splat_img, direction='left')
            player_1.reset(scoreboard)
        if vehicle.distance(player_2) < 25:
            print('Squish!!!')
            scoreboard.turtle_squishes += 1
            splat = Splat(pet=player_2, file=splat_img, direction='left')
            player_2.reset(scoreboard)
        for pet in pets:
            if vehicle.distance(pet) < 25:
                print('Squish!!!')
                scoreboard.turtle_squishes += 1
                splat = Splat(pet=pet, file=splat_img, direction='left')
                pet.reset(scoreboard)
        if vehicle.xcor() < ((SCREEN_WIDTH + 200) / 2 * -1):
            vehicle.moving = False
            vehicle.hideturtle()

    for vehicle in game.vehicles_driving_right_list:
        if vehicle.moving:
            vehicle.drive()
        if vehicle.distance(player_1) < 25:
            print('Squish!!!') 
            scoreboard.turtle_squishes += 1
            splat = Splat(pet=player_1, file=splat_img, direction='right')
            player_1.reset(scoreboard)
        if vehicle.distance(player_2) < 25:
            print('Squish!!!')
            scoreboard.turtle_squishes += 1
            splat = Splat(pet=player_2, file=splat_img, direction='right')
            player_2.reset(scoreboard)
        for pet in pets:
            if vehicle.distance(pet) < 25:
                print('Squish!!!')
                scoreboard.turtle_squishes += 1
                splat = Splat(pet=pet, file=splat_img, direction='right')
                pet.reset(scoreboard)
        if vehicle.xcor() > ((SCREEN_WIDTH + 200) / 2):
            vehicle.moving = False
            vehicle.hideturtle()

    for pet in pets:
        pet.speed(1)
        pet.move_randomly(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)


screen.exitonclick()
