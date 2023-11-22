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
turtle.tracer(0)
maxHeat = 10000

td = 1/10

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
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j][i + 1]) / 3) * td)
                elif (i == 9):
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j][i - 1]) / 3) * td)
                else:
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j][i + 1] + tempPoints[j][i - 1]) / 4) * td)
            elif (j == 9):
                if (i == 0):
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1]) / 3) * td)
                elif (i == 9):
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j - 1][i] + tempPoints[j][i - 1]) / 3) * td)
                else:
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1] + tempPoints[j][i - 1]) / 4) * td)
            else:
                if (i == 0):
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1]) / 4) * td)
                elif (i == 9):
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j - 1][i] + tempPoints[j][i - 1]) / 4) * td)
                else:
                    points[j][i] -= round((points[j][i] - (tempPoints[j][i] + tempPoints[j + 1][i] + tempPoints[j - 1][i] + tempPoints[j][i + 1] + tempPoints[j][i - 1]) / 5) * td)
    
    draw()

def draw():
    turtle.penup()
    turtle.goto((s.window_width()/2)*-1 + pDistX, s.window_height()/2 - pDistY)
    for j in range(10):
        turtle.goto((s.window_width()/2)*-1 + pDistX, turtle.ycor() - pDistY)
        for i in range(10):
            turtle.goto(turtle.xcor() + pDistX, turtle.ycor()) 
            turtle.colormode(255)
            turtle.color((points[j][i] / maxHeat * 255).__int__(), (255 - (points[j][i] / maxHeat * 255)).__int__(), 0)
            turtle.hideturtle()
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()
            turtle.penup()
    time.sleep(td)

def end():
    global cont
    cont = False

def addHeat(x, y):
    global points
    clickPosX = x
    clickPosY = y - 15
    i = 0
    j = 0

    print(clickPosY)

    if (
        (abs(clickPosX % pDistX) < 15 or abs(clickPosX % pDistX) > pDistX - 15)
        and
        (abs((clickPosY) % pDistY) < 15 or abs((clickPosY) % pDistY) > pDistY - 15)
    ):
        clickPosX += ((1) if (pDistX - (clickPosX % pDistX) < clickPosX % pDistX) else (-1)) * min(clickPosX % pDistX, pDistX - (clickPosX % pDistX))
        clickPosY += ((1) if (pDistY - (clickPosY % pDistY) < clickPosY % pDistY) else (-1)) * min(clickPosY % pDistY, pDistY - (clickPosY % pDistY))
        print(clickPosY)
        i = (clickPosX / pDistX + 4).__int__()
        j = (-1 * clickPosY / pDistY + 4).__int__()
        points[j][i] += maxHeat * 0.02
        if (points [j][i] > maxHeat):
            points[j][i] = maxHeat

s.listen()
s.onkeypress(end, "c")
s.onclick(addHeat)

dX = s.window_width()
dY = s.window_height()

while cont:
    try:
        if (dX != s.window_width() or dY != s.window_height()):
            turtle.clearscreen()
            dX = s.window_width()
            dY = s.window_height()
            turtle.tracer(0)
            turtle.hideturtle()
        
        updateScreen()
        turtle.update()
    
    except:
        break
try:
    turtle.bye()
except:
    pass