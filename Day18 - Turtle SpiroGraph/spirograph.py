import turtle
from turtle import Turtle, Screen
import random

t1 = Turtle()
t1.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


def draw_spiro(gap_size):
    for _ in range(int(360/ gap_size)):
        t1.color(random_color())
        t1.circle(100)
        t1.setheading(t1.heading() + gap_size)


draw_spiro(5)
s1 = Screen()
s1.exitonclick()