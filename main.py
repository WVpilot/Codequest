import turtle
import numpy

s = turtle.getscreen()
t = turtle.Turtle()

s.delay(1 / 60)
t.hideturtle()

points = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

pDistX = s.window_width / 12
pDistY = s.window_height / 12

def updateScreen():
    for i in 10:
        for j in 10:
            if (i = 0):
                if (j = 0):
                    points[j][i] = 2

    pass

while 1:
    updateScreen()

    s.clearscreen()