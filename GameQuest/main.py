import turtle
import random       # random.randint()
from player import Player   # Player()

# Screen setup
screen = turtle.Screen()
screen.title("Game Quest")
screen.bgcolor("black")
screen.screensize(1000, 500) # canvas size
screen.setup(1050, 550)      # window size



game_borders = {
    'min_x' : -screen.window_width()/2,
    'max_x' : screen.window_width()/2,
    'min_y' : -screen.window_height()/2,
    'max_y' : screen.window_height()/2
    }

me = Player()

def move_forward():
    me.player.forward(10)
    me.update(game_borders)

def move_backward():
    me.player.backward(10)
    me.update(game_borders)

def turn_left():
    me.player.left(15)
    me.update(game_borders)

def turn_right():
    me.player.right(15)
    me.update(game_borders)

enemies = []
for _ in range(50):
    enemies.append(turtle.Turtle())
    enemies[-1].penup()
    enemies[-1].color("red")
    enemies[-1].goto(
        random.randint(game_borders['min_x'], game_borders['max_x']), # x
        random.randint(game_borders['min_y'], game_borders['max_y'])  # y
        )

def move_enemies():
    for enemy in enemies:
        enemy.forward(random.randint(0,10))
        enemy.left(random.randint(-15,15))
    screen.ontimer(move_enemies, 100)

screen.onkeypress(move_forward, 'Up')
screen.onkeypress(move_backward, 'Down')
screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_right, 'Right')

# Main loop
screen.listen()
screen.mainloop()