import turtle
screen = turtle.Screen() # not sure if this is necessary

sl = int(input("enter length of biggest H:"))
depth = int(input("enter depth (number of levels):"))



def HTree(sl, depth): # not sure if the instructions specified one main function so thats why
                      # there is nested functions

   t = turtle.Turtle()
   t.speed(0)

   def draw_H(x, y, length):
       half = length/2

       # draws left part of h without drawing what it isnt supposed to
       t.penup()
       t.goto(x-half, y-half)
       t.pendown()
       t.goto(x-half, y+half)

       #draws right part of h without drawing what it isnt supposed to
       t.penup()
       t.goto(x+half, y-half)
       t.pendown()
       t.goto(x+half, y+half)

       #draws middle line without drawing what it isnt supposed to
       t.penup()
       t.goto(x-half, y)
       t.pendown()
       t.goto(x+half, y)

   def recurse(x,y,length,depth):
       # base
       if depth == 0:
           return

       draw_H(x, y, length)

       half = length/2

       recurse(x-half, y+half, half, depth-1) # calling recurse calls draw with -1 depth and half the length
       recurse(x-half, y-half, half, depth-1) # the important part of calling recurse is that
       recurse(x+half, y+half, half, depth-1) # it starts at the 4 endpoints of said h
       recurse(x+half, y-half, half, depth-1) # (hence these 4 lines)

   recurse(0,0,sl,depth)

HTree(sl,depth) # calling HTree just calls recurse which calls draw recursively until depth = 0
turtle.done()
