import turtle
from game import Game

# Screen setup
screen = turtle.Screen()
screen.title("Game Quest")
screen.bgcolor("black")
screen.screensize(1000, 500) # canvas size
screen.setup(1050, 550)      # window size
screen.tracer(0) # set animation time to 0

framerate = 10

game = Game(screen)

screen.onkeypress(game.move_forward, 'Up')
screen.onkeypress(game.move_backward, 'Down')
screen.onkeypress(game.turn_left, 'Left')
screen.onkeypress(game.turn_right, 'Right')

def playermove(x,y):
    game.me.player.setheading(game.me.player.towards(x,y))
    game.me.player.forward(20)

screen.onscreenclick(playermove)

def frame():
    game.update()
    screen.update() # update screen
    screen.ontimer(frame, framerate)

frame()

# Main loop
screen.listen() # listen for key press events
screen.mainloop() # keep window up until closed