from turtle import Turtle, Screen
from random import choice

t1 = Turtle()
colors = ["red", "blue", "green", "purple", "brown"]


def draw_shape(noofsides):
    angle = 360/noofsides
    for _ in range(noofsides):
        t1.forward(100)
        t1.left(angle)
        t1.forward(100)


for i in range(3, 11):
    t1.color(choice(colors))
    draw_shape(i)

s1 = Screen()
s1.exitonclick()