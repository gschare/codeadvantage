# Reference: https://docs.python.org/3/library/turtle.html
import turtle
import random

# setup
w, h = 1000, 400                  # define the canvas dimensions
screen = turtle.Screen()          # create the canvas
screen.setup(width=w, height=h)   # this controls the canvas dimensions
screen.tracer(0)                  # set animation delay to 0

# Draw arena boundaries
Boundary = turtle.Turtle()
Boundary.hideturtle()
boundary_top    = 150
boundary_bottom = -150
boundary_left   = -450
boundary_right  = 450

Boundary.penup()
Boundary.goto(boundary_left, boundary_top)
Boundary.pendown()
Boundary.goto(boundary_right, boundary_top)
Boundary.goto(boundary_right, boundary_bottom)
Boundary.goto(boundary_left, boundary_bottom)
Boundary.goto(boundary_left, boundary_top)

Boundary.penup()
Boundary.goto(boundary_left + 20, screen.window_height()/6)
Boundary.pendown()
Boundary.goto(boundary_left + 20, -screen.window_height()/6)

Boundary.penup()
Boundary.goto(boundary_right - 20, screen.window_height()/6)
Boundary.pendown()
Boundary.goto(boundary_right - 20, -screen.window_height()/6)

# Racing turtles
Jeff = turtle.Turtle(shape="turtle")
Jeff.color("lime")
Jeff.penup()
Jeff.goto(boundary_left + 20, screen.window_height()/12)

Fyodor = turtle.Turtle(shape="turtle")
Fyodor.color("green")
Fyodor.penup()
Fyodor.goto(boundary_left + 20, -screen.window_height()/12)

def check_finish(turtle):
    if (turtle.xcor() >= boundary_right - 20):
        return True
    else:
        return False

def frame():
    if check_finish(Fyodor)==True:
        print("Fyodor wins!")
    elif check_finish(Jeff)==True:
        print("Jeff wins!")
    else:
        Fyodor_speed = random.randint(0, 10)
        Jeff_speed = random.randint(0, 10)
        Fyodor.setx(Fyodor.xcor() + Fyodor_speed)
        Jeff.setx(Jeff.xcor() + Jeff_speed)
        screen.update()
        screen.ontimer(frame, 20)

frame()

'''
Homework:
Peruse ways to improve turtle racing.
Suggestions (Take your pick or do your own thing!):
   - use a "winner" to write a message on the screen saying who won
   - explore the turtle library documentation to make the racing arena
     look nicer, perhaps with colors and patterns
   - create functions to handle the annoying geometry for you without
     doing calculations in your head
   - add support for arbitrarily many turtles
       (hint: use classes and/or functions!)
   - for extra chaos, allow the turtles to also turn a little bit each frame
     and bounce off of walls, making it much harder for them to reach the
     finish line.
   - organize your code into functions and/or classes so it's more structured
'''
