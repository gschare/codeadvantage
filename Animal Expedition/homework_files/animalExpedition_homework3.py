# Import
import turtle, random

# Screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Homework 3")

# Player (turtle) object
player = turtle.Turtle()
player.shape('turtle')
player.color('red')
player.speed(0)

borders = {'min_x':-250,'max_x':250,'min_y':-250,'max_y':250}

def playerBorders(p):

    if (p.xcor() >= borders['max_x'] or
        p.xcor() <= borders['min_x'] or
        p.ycor() >= borders['max_y'] or
        p.ycor() <= borders['min_y']):
        p.color(['red','white','gold','blue','green'][random.randint(0,4)])
        p.rt(180)
        p.fd(50)

# Movement 
def moveForward(): player.forward(25); playerBorders(player)
def moveBackward(): player.backward(25); playerBorders(player)
def turnLeft(): player.left(45)
def turnRight(): player.right(45)

screen.onkeypress(moveForward, 'Up')
screen.onkeypress(moveBackward, 'Down')
screen.onkeypress(turnLeft, 'Left')
screen.onkeypress(turnRight, 'Right')


# LAST 2 LINES -----
screen.listen()
screen.mainloop()



