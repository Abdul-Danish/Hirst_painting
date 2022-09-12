import data
from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
colors = data.colors_list
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()


def hirst_painting():
    for _ in range(10):
        for _ in range(10):
            tim.pendown()
            tim.dot(20, random.choice(colors))
            tim.penup()
            tim.forward(50)

        tim.left(90)
        tim.forward(50)
        tim.right(90)
        tim.back(500)


hirst_painting()
screen = Screen()
screen.exitonclick()
