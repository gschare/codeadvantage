# Import
import turtle

# Screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Homework 1")

# Player (turtle) object
player = turtle.Turtle()
player.shape('turtle')
player.color('red')

# Movement 
def moveForward(): player.forward(25)
def moveBackward(): player.backward(25)
def turnLeft(): player.left(45)
def turnRight(): player.right(45)


screen.onkeypress(moveForward, 'Up')
screen.onkeypress(moveBackward, 'Down')
screen.onkeypress(turnLeft, 'Left')
screen.onkeypress(turnRight, 'Right')


# LAST 2 LINES -----
screen.listen()
screen.mainloop()



