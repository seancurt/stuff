import turtle
import random
import math
screen = turtle.Screen()

#step1
startpoint=list(input('enter starting x, y separated by comma:\n').strip().split(','))
endpoint=list(input('enter ending x, y separated by comma:\n').strip().split(','))
startpoint = startpoint[:2] # only take 2 numbers
endpoint = endpoint[:2]
startpoint[0], startpoint[1] = int(startpoint[0]), int(startpoint[1])
endpoint[0], endpoint[1] = int(endpoint[0]), int(endpoint[1])

#step 3/4
x0 = int(startpoint[0])
y0 = int(startpoint[1])
x1 = int(endpoint[0])
y1 = int(endpoint[1])
offset_range = int(input("enter a number between 5 and 25 for offset:\n")) # not too big or small for visible results
min_distance = int(input("enter a small number for minimum distance:\n"))


def draw_brownian(x0, y0, x1, y1, min_distance, offset_range): # arguments from 4.hint
    distance = math.sqrt((x1 - x0)**2 + (y1 - y0)**2) # distance formula from google
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle() # I had to use ai to fix this issue, it was drawing a bunch of mini turtles throughout
                   # the segment. one turtle still flashes up during recursive calls though

    # base case
    if distance < min_distance:
        t.penup() # command i googled to disable drawing (goto start point without drawing)
        t.goto(x0, y0)
        t.pendown()
        t.goto(x1, y1)
        return

    # step 2
    xm = (x0 + x1) / 2
    ym = (y0 + y1) / 2
    ym += random.uniform(-offset_range, offset_range)

    # recurse
    draw_brownian(x0, y0, xm, ym, min_distance, offset_range)
    draw_brownian(xm, ym, x1, y1, min_distance, offset_range)


draw_brownian(x0, y0, x1, y1, min_distance, offset_range)
turtle.done()






