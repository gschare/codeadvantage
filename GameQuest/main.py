import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Game Quest")
screen.bgcolor("black")
screen.screensize(1000, 500) # canvas size
screen.setup(1050, 550)      # window size

# Player setup
player = turtle.Turtle()
player.shapesize(3.0, 3.0)
player.penup()
player.shape("turtle")
player.color((0.1, 0.9, 0.1)) # lime color in r,g,b
player.fillcolor("black")

game_borders = {
    'min_x' : -screen.window_width()/2,
    'max_x' : screen.window_width()/2,
    'min_y' : -screen.window_height()/2,
    'max_y' : screen.window_height()/2
    }

def check_borders(t):
    if (t.xcor() < game_borders['min_x'] or t.xcor() > game_borders['max_x'] or
        t.ycor() < game_borders['min_y'] or t.ycor() > game_borders['max_y']):
        t.backward(25)

def move_forward():
    player.forward(10)
    check_borders(player)

def move_backward():
    player.backward(10)
    check_borders(player)

def turn_left():
    player.left(15)
    check_borders(player)

def turn_right():
    player.right(15)
    check_borders(player)

screen.onkeypress(move_forward, 'Up')
screen.onkeypress(move_backward, 'Down')
screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_right, 'Right')



def f():
    r = random.uniform(0,1)
    g = random.uniform(0,1)
    b = random.uniform(0,1)
    player.color((r,g,b))
    screen.update()
    screen.ontimer(f, 250)

f()

# Main loop
screen.listen()
screen.mainloop()