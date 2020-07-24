# Reference: https://docs.python.org/3/library/turtle.html
import turtle

# setup
w, h = 500, 500                   # define the canvas dimensions
screen = turtle.Screen()          # create the canvas
screen.setup(width=w, height=h)   # this controls the canvas dimensions
t = turtle.Turtle(shape="circle") # this lets us draw stuff
t.color("green")

# draw a shape with a certain number of sides
def drawShape(myTurtle, num_sides, side_length):
    degrees = ((num_sides - 2)*180)/num_sides
    for _ in range(num_sides):
        myTurtle.forward(side_length)
        myTurtle.right(180 - degrees)

def drawCircle(x, y, myTurtle=t, radius=30):
    #myTurtle.goto(x, y)
    myTurtle.circle(radius)

# tell my turtle t to draw a shape with 8 sides and side length 100 pixels
t.goto(0, 0)
drawShape(t, 3, 50)
t.goto(0, 0)
drawCircle(0, 0, t, 50)

# control turtle with mouse click
screen.onscreenclick(t.goto, btn=1)
screen.onscreenclick(drawCircle, btn=3)

#screen.mainloop()

# Homework: play around with this! See what you can do!
# We will continue using turtle in the coming classes, so get familiar.
