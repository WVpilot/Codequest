import turtle
import time
import numpy

s = turtle.getscreen()
t = turtle.Turtle(visible=False)
cont = True
s.delay(None)
turtle.colormode(255)
turtle.colormode()
turtle.hideturtle()
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
        points[j][i] = maxHeat - 1#numpy.random.randint(0,maxHeat)

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
    turtle.tracer(0, 0)
    turtle.penup()
    turtle.goto((s.window_width()/2)*-1 + pDistX, s.window_height()/2 - pDistY)
    for j in range(10):
        for i in range(10):
            turtle.colormode(255)
            turtle.color((points[j][i] / maxHeat * 256).__int__(), (points[j][i] / maxHeat * 256).__int__(), (points[j][i] / maxHeat * 256).__int__())
            turtle.hideturtle()
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(5)
            turtle.end_fill()
            turtle.penup()
            turtle.goto((s.window_width()/2)*-1 + ((i + 1) * pDistX), s.window_height()/2 - ((j + 1) * pDistY))
    turtle.update()
    time.sleep(1 / 60)


def end():
    cont = False
s.onkeypress(end, "C")

while cont:
    #s.clear()
    updateScreen()
    #print(points)