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
maxHeat = 1000000000

points = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,maxHeat,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
tempPoints = [range(10),
              range(10),
              range(10),
              range(10),
              range(10),
              range(10),
              range(10),
              range(10),
              range(10),
              range(10)]

for j in range(10):
    for i in range(10):
        points[j][i] = numpy.random.randint(0,maxHeat)

pDistX = s.window_width() / 12
pDistY = s.window_height() / 12

def updateScreen():
    tempPoints = points
    for j in range(10):
        for i in range(10):
            if (j == 0):
                if (i == 0):
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j][i + 1]) / 3)
                elif (i == 9):
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j][i - 1]) / 3)
                else:
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j][i + 1] + tempPoints[j][i - 1]) / 4)
            elif (j == 9):
                if (i == 0):
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1]) / 3)
                elif (i == 9):
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j - 1][i] + tempPoints[j][i - 1]) / 3)
                else:
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1] + tempPoints[j][i - 1]) / 4)
            else:
                if (i == 0):
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1]) / 4)
                elif (i == 9):
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j - 1][i] + tempPoints[j][i - 1]) / 4)
                else:
                    points[j][i] = round((tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1] + tempPoints[j][i - 1]) / 5)
    
    draw()

def draw():
    turtle.tracer(0, 0)
    turtle.penup()
    turtle.goto((s.window_width()/2)*-1 + pDistX, s.window_height()/2 - pDistY)
    for j in range(10):
        for i in range(10):
            turtle.colormode(255)
            turtle.color((points[j][i] / maxHeat * 255).__int__(), (points[j][i] / maxHeat * 255).__int__(), (points[j][i] / maxHeat * 255).__int__())
            print(((points[j][i] / maxHeat) * 255).__int__(), (points[j][i] / maxHeat * 255).__int__(), (points[j][i] / maxHeat * 255).__int__())
            turtle.hideturtle()
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(5)
            turtle.end_fill()
            turtle.penup()
            turtle.goto((s.window_width()/2)*-1 + ((i + 1) * pDistX), s.window_height()/2 - ((j + 1) * pDistY))
    turtle.update()
    time.sleep(1 / 1)


def end():
    cont = False
s.onkeypress(end, "C")
draw()
updateScreen()
while cont:
    #s.clear()
    updateScreen()
    #print(points)