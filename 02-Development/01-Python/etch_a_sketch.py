# turtle docs reference - https://docs.python.org/3/library/turtle.html
# etch a sketch simulator
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_left():
    turtle.left(10)


def move_right():
    turtle.right(10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
