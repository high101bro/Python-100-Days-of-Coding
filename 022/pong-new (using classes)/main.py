from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")

screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
scoreboard.update()
paddle_left = Paddle((-750, 0))
paddle_right = Paddle((750, 0))
paddle_middle = Paddle((0, 220))


screen.listen()
screen.onkey(paddle_left.go_up, key="w")
screen.onkey(paddle_left.go_down, key="s")
screen.onkey(paddle_left.stop, key="a")
screen.onkey(paddle_middle.go_up, key="y")
screen.onkey(paddle_middle.go_down, key="n")
screen.onkey(paddle_middle.stop, key="h")
screen.onkey(paddle_right.go_up, key="Up")
screen.onkey(paddle_right.go_down, key="Down")
screen.onkey(paddle_right.stop, key="Right")

game_is_running = True
while game_is_running:
    screen.update()
    ball.move()
    ball.bounce()
    paddle_left.move()
    paddle_right.move()
    paddle_middle.move_obstacle()

    def paddle_hit(paddle=None, bounce_direction=None):
        def bounce_ball():
            if ball.direction[0] == 'up':
                ball.direction[0] = 'up'
            elif ball.direction[0] == 'down':
                ball.direction[0] = 'down'
            print(ball.direction)

        def invert_bounce_ball():
            if ball.direction[0] == 'up':
                ball.direction[0] = 'down'
            elif ball.direction[0] == 'down':
                ball.direction[0] = 'up'
            print(ball.direction)

        if ball.distance(paddle) < 10:
            ball.ball_x_speed += 0.25
            ball.ball_y_speed -= 0.0
            ball.direction[1] = bounce_direction
            bounce_ball()
        elif ball.distance(paddle) < 20:
            ball.ball_x_speed += 0.20
            ball.ball_y_speed -= 0.05
            ball.direction[1] = bounce_direction
            bounce_ball()
        elif ball.distance(paddle) < 30:
            ball.ball_x_speed += 0.15
            ball.ball_y_speed -= 0.10
            ball.direction[1] = bounce_direction
            bounce_ball()
        elif ball.distance(paddle) < 40:
            ball.ball_x_speed += 0.10
            ball.ball_y_speed -= 0.15
            ball.direction[1] = bounce_direction
            bounce_ball()
        elif ball.distance(paddle) < 45:
            ball.ball_x_speed += 0.05
            ball.ball_y_speed -= 0.20
            ball.direction[1] = bounce_direction
            bounce_ball()
        else:
            ball.ball_x_speed += 0.00
            ball.ball_y_speed -= 0.25
            invert_bounce_ball()
        # ball.faster()


    # If the left paddle hits the ball
    if ball.distance(paddle_left) < 50 and ball.xcor() < -725:
        paddle_hit(paddle=paddle_left, bounce_direction='right')

    # If the right paddle hits the ball
    elif ball.distance(paddle_right) < 50 and ball.xcor() > 725:
        paddle_hit(paddle=paddle_right, bounce_direction='left')

    # If the middle paddle hits the ball on the right side
    elif ball.distance(paddle_middle) < 50 and ball.xcor() < 30 and ball.direction[1] == 'left':
        paddle_hit(paddle=paddle_middle, bounce_direction='right')

    # If the middle paddle hits the ball on the left side
    elif ball.distance(paddle_middle) < 50 and ball.xcor() > -30 and ball.direction[1] == 'right':
        paddle_hit(paddle=paddle_middle, bounce_direction='left')

    # Detects the score if on the right side
    elif ball.xcor() > 800:
        if ball.direction[0] == 'up':
            ball.direction[0] = 'down'
        elif ball.direction[0] == 'down':
            ball.direction[0] = 'up'

        if paddle_right.protection == True:
            ball.direction[1] = 'left'
        else:
            # game_is_running = False
            scoreboard.left_scores()
            ball.direction[1] = 'left'
            ball.reset()
            print(f"Player 1 scores")

    # Detects the score if on the left side
    elif ball.xcor() < -800:
        if ball.direction[0] == 'up':
            ball.direction[0] = 'down'
        elif ball.direction[0] == 'down':
            ball.direction[0] = 'up'

        if paddle_left.protection == True:
            ball.direction[1] = 'right'
        else:
            # game_is_running = False
            scoreboard.right_scores()
            ball.direction[1] = 'right'
            ball.reset()
            print(f"Player 2 scores")

screen.exitonclick()
