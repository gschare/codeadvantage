# Import
import turtle, random

# Screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Homework 4")

obj = turtle.Turtle()
obj.shape('square')
obj.color('white')
obj.penup()
obj.speed(0)

def placeShape(x,y):
    obj.setpos(x,y)
    obj.stamp()

screen.onclick(placeShape)
screen.onkeypress(obj.clearstamps,'space')


# LAST 2 LINES -----
screen.listen()
screen.mainloop()




