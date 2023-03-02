from turtle import *
from random import choice
from math import atan, pi


def triangle(a, b):
    begin_fill()
    color(choice(("green", "blue", "yellow", "red")))
    forward(a)
    left(90)
    forward(b)
    goto(0, 0)
    end_fill()


speed(0)
angle = atan(20 / 200) * 180 / pi
i = 0
bgcolor("gray")
title("TRIANGLE")
while i * angle <= 360:
    triangle(200, 20)
    right(90 - angle)
    i += 1

hideturtle()
mainloop()

