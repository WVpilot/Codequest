import turtle
#import time
import numpy

s = turtle.getscreen()
t = turtle.Turtle()
cont = True
s.delay(100)
t.hideturtle()

maxHeat = 1000

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

for j in range(10):
    for i in range(10):
        points[j][i] = numpy.random.randint(0,maxHeat)

pDistX = s.window_width() / 12
pDistY = s.window_height() / 12

def updateScreen():
    for j in range(10):
        for i in range(10):
            if (j == 0):
                if (i == 0):
                    points[j][i] = round((points[j][i] + points[j + 1][i] + points[j][i + 1]) / 3)
                elif (i == 9):
                    points[j][i] = round((points[j][i] + points[j + 1][i] + points[j][i - 1]) / 3)
                else:
                    points[j][i] = round((points[j][i] + points[j + 1][i] + points[j][i + 1] + points[j][i - 1]) / 4)
            elif (j == 9):
                if (i == 0):
                    points[j][i] = round((points[j][i] + points[j - 1][i] + points[j][i + 1]) / 3)
                elif (i == 9):
                    points[j][i] = round((points[j][i] + points[j - 1][i] + points[j][i - 1]) / 3)
                else:
                    points[j][i] = round((points[j][i] + points[j - 1][i] + points[j][i + 1] + points[j][i - 1]) / 4)
            else:
                if (i == 0):
                    points[j][i] = round((points[j][i] + points[j + 1][i] + points[j - 1][i] + points[j][i + 1]) / 4)
                elif (i == 9):
                    points[j][i] = round((points[j][i] + points[j + 1][i] + points[j - 1][i] + points[j][i - 1]) / 4)
                else:
                    points[j][i] = round((points[j][i] + points[j + 1][i] + points[j - 1][i] + points[j][i + 1] + points[j][i - 1]) / 5)
    
    draw()

def draw():
    t.penup()
    t.goto((s.window_width()/2)*-1 + pDistX, s.window_height()/2 - pDistY)
    for j in range(10):
        for i in range(10):
            t.color((0, 0, 0), (numpy.floor(max(0, points[j][i] - (maxHeat / 2)) / maxHeat * 256), numpy.floor(min(maxHeat / 2, points[j][i]) / maxHeat * 256), 0))


def end():
    cont = False
s.onkeypress(end, "C")

while cont:
    s.clearscreen()
    updateScreen()
    print(points)