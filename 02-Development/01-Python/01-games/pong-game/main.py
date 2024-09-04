# Pong game
# Decomposition
# create Player 1 and 2 bats
# create ball
# create score at top of screen
# create initial ball throw
# make sure bats are limited to min and max Y co-ordinates
# make keys work for player 1 and 2 to change direction
# # detect when ball hits player 1 bat and change direction
# detect when ball hits player 2 bat and change direction
# detect when ball collides with a wall and bounce
# detect when a ball reaches far left and player 1 loses
# detect when a ball reaches far right and player 2 loses
# keep score
from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game: Keys w & s (P1) and cursor up and down (P2)")
screen.tracer(0)
wait_time = 0.01

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect out of bounds on left
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()
    # Detect out of bounds on right
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()
    # Detect paddle hitting ball
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(
            left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    ball.move()

    screen.update()

screen.exitonclick()
