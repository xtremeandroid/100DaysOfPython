from turtle import Turtle, Screen
from random import choice

t1 = Turtle()
colors = ["red", "blue", "green", "purple", "brown"]
directions = [0, 90, 180, 270]
size = 10
t1.speed(0)

for _ in range(200):
    t1.color(choice(colors))
    t1.pensize(size)
    t1.forward(30)
    t1.setheading(choice(directions))


s1 = Screen()
s1.exitonclick()