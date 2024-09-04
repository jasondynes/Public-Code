import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food_item = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # makes whole snake look like it moves in one go rather than segment at a time
    # used in conjunction with screen.tracer() method above
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food_item) < 15:
        food_item.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # if head collides with any segment in the tail then game over
        # if snake.head.distance(segment) < 10 and segment != snake.head:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
