# https://docs.python.org/3/library/turtle.html

import turtle

# setup
turtle.setup(width=500, height=500)
screen = turtle.Screen()
t = turtle.Turtle(shape="turtle")
t.color("green")

'''
def togglePen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

# script
screen.onscreenclick(t.goto, btn=1)
screen.onscreenclick(togglePen(), btn=3)
'''

# draw a shape with a certain number of sides
def drawShape(myTurtle, num_sides):
    # square: 360 deg
    # triangle: 180 deg
    # pentagon: 540 deg
    # hexagon: 720 deg
    degrees = ((num_sides - 2)*180)/num_sides
    for _ in range(num_sides):
        myTurtle.forward(100)
        myTurtle.right(180 - degrees)

drawShape(t, 8)
turtle.mainloop()


