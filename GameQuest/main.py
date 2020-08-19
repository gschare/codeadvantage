import turtle
from game import Game

# Screen setup
screen = turtle.Screen()
screen.title("Game Quest")
screen.bgcolor("black")
screen.screensize(1000, 500) # canvas size
screen.setup(1050, 550)      # window size
screen.tracer(0) # set animation time to 0

framerate = 10 # refresh screen every 1/10th of a second

game = Game(screen) # initialize our Game class, with controls all game elements

screen.onscreenclick(game.move) # Club Penguin-style click movement
screen.onscreenclick(game.shoot, btn=3)

def frame():
    game.update() # update all game elements
    screen.update() # update screen 
    screen.ontimer(frame, framerate) # repeat after 1/10th of a second

frame()

# Main loop
screen.listen() # listen for key press events
screen.mainloop() # keep window up until closed