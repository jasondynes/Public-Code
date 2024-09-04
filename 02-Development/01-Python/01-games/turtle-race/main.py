from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
x = -230
y = 100
is_game_on = True

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
    y -= 30

while is_game_on:
    for i in range(6):
        random_distance = random.randint(0, 10)
        all_turtles[i].forward(random_distance)
        if all_turtles[i].xcor() >= 220:
            is_game_on = False
        print(f"The winner was the {all_turtles[i].pencolor()} coloured turtle")
        if all_turtles[i].pencolor() != user_bet.lower():
            print("You lost the best!")
        else:
            print("You won the bet!")

screen.exitonclick()
