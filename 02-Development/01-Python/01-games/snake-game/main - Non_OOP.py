import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
segments = []

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# initialise 3 piece snake in middle of screen
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    # makes whole snake look like it moves in one go rather than segment at a time
    # used in conjunction with screen.tracer() method above
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()
