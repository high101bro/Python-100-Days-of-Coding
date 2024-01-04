from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Snake gets close to food and eats it
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with the game wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with snake's tail
    # for segment in snake.segments:
    #     Too wordy... let's try slicing
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 0:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
